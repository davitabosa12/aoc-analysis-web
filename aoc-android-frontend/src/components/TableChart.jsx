import Plot from "react-plotly.js";
import { ProjectAoCStatistics } from "../api/aoc-api-service/model/AoCReport";


/**
 *
 * @typedef {TableChart}
 * @property {ProjectAoCStatistics} data
 */


function TableChart({
    /**
     * @type {ProjectAoCStatistics}
     */
    data,
    title
}) {
    // data.
    return (
        <Plot
            data={
                [{
                    type: "table",
                    header: {
                        values: [["foo"], ["bar"]]
                    },
                    align: "center",
                    line: { width: 1, color: 'black' },
                    fill: { color: "grey" },
                    font: { family: "Arial", size: 12, color: "white" }
                }]
            } />
    )
}

export { TableChart };