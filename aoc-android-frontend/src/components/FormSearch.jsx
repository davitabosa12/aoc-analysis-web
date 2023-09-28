import { useEffect, useState, useRef } from "react";
import AoCApiService from "../api/aoc-api-service/AoCApiService";
import ReportSummary from "./ReportSummary";
import { calculateStatistics } from "../lib/aocStatistics";
export default function FormSearch({ onReport }) {
    let [aocReports, setAocReports] = useState([]);
    let [aocs, setAocs] = useState([]);
    // @type {sas}
    let [projects, setProjects] = useState([]);
    let projectSelectRef = useRef();
    let aocSelectRef = useRef();
    const api = new AoCApiService("http://localhost:5000");
    useEffect(() => {
        api.getAllAoCTypes().then(listOfAocs => {
            setAocs(listOfAocs);
        });
        api.getAllProjects().then(listOfProjects => {
            setProjects(listOfProjects)
        });
    }, []);
    const triggerOnReport = (statistics) => {
        if (typeof onReport == "function") {
            onReport(statistics);
        }
    }
    return (
        <>
            <form>
                <label htmlFor="">Project</label>
                <select ref={projectSelectRef}>
                    {projects ? projects.map(project => <option value={project.id}>{project.name}</option>) : <option disabled>No projects</option>}
                </select>
                <label htmlFor="">Atom</label>
                <select name="" id="" ref={aocSelectRef}>
                    <option value={"%%ALL_AOCS%%"}>~All Atoms~</option>
                    {aocs ? aocs.map(val => <option value={val}>{val}</option>) : null}
                </select>
                <input type="submit" value="Search" onClick={(e) => {
                    e.preventDefault();
                    const currentProject = projectSelectRef.current.value;
                    let currentAoc = aocSelectRef.current.value;
                    if (currentAoc.startsWith("%")) {
                        currentAoc = undefined;
                    }
                    console.log(`Fetch project with id ${currentProject} and pick aoc ${currentAoc}.`);
                    api.search(currentProject, currentAoc).then(listOfReports => {
                        setAocReports(listOfReports);
                        triggerOnReport(calculateStatistics(listOfReports));
                    });
                }} />
            </form>
            {aocReports ? aocReports.map(aoc => <ReportSummary data={aoc} />) : undefined}
        </>
    )
}