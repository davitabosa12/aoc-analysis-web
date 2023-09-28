import Plot from "react-plotly.js"
function StatPieChart({ data, title }) {
    let values = [];
    let labels = [];

    console.count(`Rendered!`);
    try {
        for (const elem in data) {
            labels.push(elem);
            values.push(data[elem].count);
        }
    } catch (error) {
    }

    return (
        <div>
            <Plot
                data={
                    [{
                        labels: labels,
                        values: values,
                        title: title ?? "Pie Chart",
                        type: "pie",
                    }]
                } />
        </div>
    )
}

export {
    StatPieChart
}