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

class AoCStatistics extends Base {
    constructor(data) {
        super(data);
        /**
         * @type {number}
         */
        this.count = data.count;
        /**
        * @type {Map<string, number>}
        */
        this.class = data.class;
        /**
         * @type {Map<string, number>}
         */
        this.aoc = data.aoc;
    }
}

class ProjectAoCStatistics extends AoCStatistics {
    constructor(data) {
        super(data);
        /**
         * @type {Map<string, AoCStatistics>}
         */
        this.project = data.project
    }
}

export {
    AoCReportSummary, AoCReportDetail, AoCStatistics, ProjectAoCStatistics
}