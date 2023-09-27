import { AoCReportSummary } from "./model/AoCReport";
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
        const params = {
            "project_id": projectId,
            "aoc": aoc
        }
        const response = await fetch(`${this.url}/api/aoc-reports/search?` + new URLSearchParams(params));
        if (response.ok) {
            const listOfReports = JSON.parse(await response.text());
            return listOfReports.map(data => new AoCReportSummary(data));
        }
        throw Error("Could not fetch aoc reports.");
    }
}