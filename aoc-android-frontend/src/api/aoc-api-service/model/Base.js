export default class Base {
    constructor(data) {
        if(data === undefined || data === null) {
            throw ReferenceError("data is undefined or null");
        }
    }
}