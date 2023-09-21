import Base from "./Base";

class AoCReportSummary extends Base {
    constructor(data) {
        super(data);
        this.id = data.id;
        this.line = data.line;
        this.snippet = data.snippet;
        this.class = data.class;
        this.aoc = data.aoc;
        this.path = data.path;
    }
}

class AoCReportDetail extends AoCReportSummary {
    constructor(data) {
        super(data);
        this.projectId = data.projectId;
        this.project = data.project;
    }
}

export {
    AoCReportSummary, AoCReportDetail
}