import Base from "./Base";
class ProjectSummary extends Base {
    constructor(data){
        super(data);
        this.id = data.id;
        this.name = data.name;
        this.description = data.description;
        this.package = data.package;
        this.category = data.category;
    }
}

class ProjectDetail extends ProjectSummary {
    constructor(data) {
        super(data);
        this.aocReports = data.aocReports;
    }
}