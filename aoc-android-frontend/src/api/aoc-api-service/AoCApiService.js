import { AoCReportSummary, ProjectAoCStatistics } from "./model/AoCReport";
import { ProjectSummary } from "./model/Project";
export default class AoCApiService {
    constructor(url) {
        this.url = url;
    }
    async getAllAoCReports() {
        const response = await fetch(`${this.url}/api/aoc-reports`);
        if (response.ok) {
            const listOfAocs = await response.json();
            return listOfAocs.map(data => new AoCReportSummary(data));
        }
        throw Error("Could not fetch AoCs.");
    }
    async getAllAoCTypes() {
        const response = await fetch(`${this.url}/api/aoc`);
        if (response.ok) {
            const listOfAocs = JSON.parse(await response.text());
            return listOfAocs;
        }
        throw Error("Could not fetch AoCs.");
    }

    /**
     * 
     * @returns {Promise<ProjectSummary[]>}
     */
    async getAllProjects() {
        const response = await fetch(`${this.url}/api/project`);
        if (response.ok) {
            const listOfProjects = JSON.parse(await response.text());
            return listOfProjects.map(data => new ProjectSummary(data));
        }
        throw Error("Could not fetch projects.");
    }

    async search(projectId, aoc) {
        const params = {}
        if (projectId !== undefined && projectId !== null) {
            params["project_id"] = projectId;
        }
        if (aoc !== undefined && aoc !== null) {
            params["aoc"] = aoc;
        }
        const response = await fetch(`${this.url}/api/aoc-reports/search?` + new URLSearchParams(params));
        if (response.ok) {
            const listOfReports = JSON.parse(await response.text());
            return listOfReports.map(data => new AoCReportSummary(data));
        }
        throw Error("Could not fetch aoc reports.");
    }

    async searchStatistics(projectId, aoc) {
        const params = {}
        if (projectId !== undefined && projectId !== null) {
            params["project_id"] = projectId;
        }
        if (aoc !== undefined && aoc !== null) {
            params["aoc"] = aoc;
        }
        const response = await fetch(`${this.url}/api/aoc-reports/search/statistics?` + new URLSearchParams(params));
        if (response.ok) {
            const listOfReports = JSON.parse(await response.text());
            return new ProjectAoCStatistics(listOfReports);
        }
    }
}