import logo from './logo.svg';
import './App.css';
import FormSearch from "./components/FormSearch";
import { useState } from 'react';
import { StatPieChart } from './components/StatPieChart';

function App() {
  const [statistics, setStatistics] = useState({});
  const handleOnReport = (stats) => {
    setStatistics(stats);
  }
  return (
    <div className="App">
      <StatPieChart title={"AoC"} data={statistics.aoc} />
      <FormSearch onReport={handleOnReport} />
    </div>
  );
}

export default App;
