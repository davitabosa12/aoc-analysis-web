import { AoCReportSummary } from "../api/aoc-api-service/model/AoCReport";

export default function ReportSummary({ data }) {
    /** @type AoCReportSummary */
    const divStyle = {
        border: "1px solid",
        margin: "0.5rem"
    };
    const aocReport = data;
        return(
            <div style={divStyle}>
                <h4>{aocReport.aoc} @ {aocReport.class}</h4>
                    <div>Class: {aocReport.class}</div>
                    <div>Type: <b>{aocReport.aoc}</b></div>
                    <div>Path: {aocReport.path}</div>
                    <div>Line: {aocReport.line}</div>
                    <div>Snippet: <blockquote style={{fontFamily: "monospace"}}>
                        {aocReport.snippet}
                    </blockquote></div>
            </div>
        )
}