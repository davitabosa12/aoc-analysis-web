import { AoCReportSummary } from "./model/AoCReport";
export default class AoCApiService {
    constructor(url) {
        this.url = url;
    }
    async getAllAoCReports() {
        const response = await fetch(`${this.url}/api/aoc-reports`);
        if (response.ok) {
            const listOfAocs = await response.json();
            debugger;
            return listOfAocs.map(data => new AoCReportSummary(data));
        }
        throw Error("Could not fetch AoCs.");
    }
}