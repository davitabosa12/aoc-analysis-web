import Plot from "react-plotly.js"
function StatPieChart({ data, title }) {
    let values = [];
    let labels = [];

    const colorFromLabel = (label) => {
        const colorMap = new Map(Object.entries({
            "Conditional Operator": "rgb(166, 206, 227)",
            "Logic as Control Flow": "rgb(31, 120, 180)",
            "Pre Increment Decrement": "rgb(178, 223, 138)",
            "Post Increment Decrement": "rgb(51, 160, 44)",
            "Type Conversion": "rgb(251, 154, 153)",
            "Infix Operator Precedence": "rgb(227, 26, 28)",
            "Change of Literal Encoding": "rgb(253, 191, 111)",
            "Repurposed Variables": "rgb(255, 127, 0)",
            "Arithmetic as Logic": "rgb(202, 178, 214)",
        }));
        return colorMap.get(label) ?? "rgb(221, 221, 221)";
    }

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
                        marker: {
                            colors: labels.map(colorFromLabel)
                        },
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