import { AoCReport, Project } from "../model";

/**
 *
 * @param {AoCReport[]} listOfAocs A list of AoCReports
 */

function calculateStatistics(listOfAocs) {
    const statistics = {
        "class": {},
        "aoc": {},
        "total": 0
    }
    listOfAocs.forEach(report => {
        let classStat = statistics["class"][report.class] ?? {
            count: 0,
        };
        let aocStat = statistics["aoc"][report.aoc] ?? {
            count: 0,
        };
        aocStat.count += 1;
        classStat.count += 1;
        statistics.total += 1;
        statistics["class"][report.class] = classStat;
        statistics["aoc"][report.aoc] = aocStat;
    });
    return statistics;
}
export { calculateStatistics };