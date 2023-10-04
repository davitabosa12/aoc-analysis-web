import './App.css';
import FormSearch from "./components/FormSearch";
import { useState } from 'react';
import { StatPieChart } from './components/StatPieChart';
import AoCApiService from './api/aoc-api-service/AoCApiService';
import { calculateStatistics } from './lib/aocStatistics';

function App() {
  const [statistics, setStatistics] = useState({});
  const api = new AoCApiService("http://localhost:5000");
  const handleOnReport = (aocSelected, projectSelected) => {
    api.search(projectSelected, aocSelected).then((data) => {
      setStatistics(calculateStatistics(data));
    }).catch(error => console.error(error));
  }
  return (
    <div className="App">
      <StatPieChart title={"AoC"} data={statistics.aoc} />
      <FormSearch onReport={handleOnReport} />
    </div>
  );
}

export default App;
