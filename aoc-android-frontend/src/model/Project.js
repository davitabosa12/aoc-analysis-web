export default class Project {
    constructor(data) {
        this.id = data.id;
        this.name = data.name;
        this.description = data.description;
        this.package = data.package;
        this.category = data.category;
        this.aocReports = data.aocReports;
    }
}