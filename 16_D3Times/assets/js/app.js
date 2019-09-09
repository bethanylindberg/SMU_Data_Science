// set the dimensions and margins of the graph
const svgWidth = window.innerWidth * .75;
const svgHeight = window.innerHeight * .75;

const margin = {
    top: 100,
    right: 100,
    bottom: 100,
    left: 100
};

const width = svgWidth - margin.left - margin.right;
const height = svgHeight - margin.top - margin.bottom;

// append the svg object to the body of the page
const svg = d3
    .select("#scatter")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

// Append an SVG group
const chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Initial Params
let chosenXAxis = "poverty";
let chosenYAxis = "obesity";

// function used for updating x-scale upon click on axis label
function xScale(stateData, chosenXAxis) {
    // create scales
    if (chosenXAxis != "income") {
        var xLinearScale = d3.scaleLinear()
            // .domain(d3.extent(stateData, d => d[chosenXAxis]))
            .domain([d3.min(stateData, d => d[chosenXAxis]) - 1, d3.max(stateData, d => d[chosenXAxis]) + 1]) //this makes a buffer so circles are not on the edge of the graph
            .range([0, width]);
    } else {
        var xLinearScale = d3.scaleLinear()
            // .domain(d3.extent(stateData, d => d[chosenXAxis]))
            .domain([d3.min(stateData, d => d[chosenXAxis]) - 10000, d3.max(stateData, d => d[chosenXAxis]) + 10000])
            .range([0, width]);
    }

    return xLinearScale;

}

function yScale(stateData, chosenYAxis) {
    // create scales
    let yLinearScale = d3.scaleLinear()
        // .domain(d3.extent(stateData, d => d[chosenYAxis]))
        .domain([d3.min(stateData, d => d[chosenYAxis]) - 1, d3.max(stateData, d => d[chosenYAxis]) + 1])
        .range([height, 0]);

    return yLinearScale;

}

function calcLinear(values_x, values_y) {
    let sum_x = 0;
    let sum_y = 0;
    let sum_xy = 0;
    let sum_xx = 0;
    let sum_yy = 0;
    let count = 0;

    /*
     * We'll use those variables for faster read/write access.
     */
    let x = 0;
    let y = 0;
    let values_length = values_x.length;

    if (values_length != values_y.length) {
        throw new Error('The parameters values_x and values_y need to have same size!');
    }

    /*
     * Nothing to do.
     */
    if (values_length === 0) {
        return [
            [],
            []
        ];
    }

    /*
     * Calculate the sum for each of the parts necessary.
     */
    for (let v = 0; v < values_length; v++) {
        x = values_x[v];
        y = values_y[v];
        sum_x += x;
        sum_y += y;
        sum_xx += x * x;
        sum_yy += y * y;
        sum_xy += x * y;
        count++;
    }

    /*
     * Calculate m and b for the formula:
     * y = x * m + b
     */
    let m = ((sum_x / count) * (sum_y / count) - sum_xy / count) / ((sum_x / count) * (sum_x / count) - (sum_xx / count));
    let b = (sum_y / count) - (m * (sum_x / count));


    /*
     * We will make the x and y result line now
     */
    let result_values_x = [];
    let result_values_y = [];
    let seLine = 0;
    let seY = 0;

    for (let v = 0; v < values_length; v++) {
        x = values_x[v];
        y = values_y[v];
        yr = x * m + b;
        seLine += (y - yr) * (y - yr);
        seY += (y - (sum_y / count)) * (y - (sum_y / count));

        result_values_x.push(x);
        result_values_y.push(yr);
    }

    let r2 = Math.pow((count * sum_xy - sum_x * sum_y) / Math.sqrt((count * sum_xx - sum_x * sum_x) * (count * sum_yy - sum_y * sum_y)), 2);
    // return [d3.min(result_values_x),d3.min(result_values_y), d3.max(result_values_x),d3.max(result_values_y), r2];
    return [{
            "x": d3.min(result_values_x),
            "y": d3.min(result_values_y)
        },
        {
            "x": d3.max(result_values_x),
            "y": d3.max(result_values_y)
        },
        r2
    ]

}

// function used for updating axes upon click on axis label
function renderXAxis(newXScale, xAxis) {
    let bottomAxis = d3.axisBottom(newXScale);

    xAxis.transition()
        .duration(1000)
        .call(bottomAxis);

    return xAxis;
}

function renderYAxis(newYScale, yAxis) {
    let leftAxis = d3.axisLeft(newYScale);

    yAxis.transition()
        .duration(1000)
        .call(leftAxis);

    return yAxis;
}

// function used for updating circles group with a transition to
// new circles
function renderCircles(circlesGroup, newXScale, newYScale, chosenXaxis, chosenYAxis) {

    circlesGroup.transition()
        .duration(1000)
        .attr("cx", d => newXScale(d[chosenXAxis]))
        .attr("cy", d => newYScale(d[chosenYAxis]));

    return circlesGroup;
}

function renderCirclesText(circlesGroupText, newXScale, newYScale, chosenXaxis, chosenYAxis) {

    circlesGroupText.transition()
        .duration(1000)
        .attr("x", d => newXScale(d[chosenXAxis]))
        .attr("y", d => newYScale(d[chosenYAxis]));

    return circlesGroupText;
}

function renderTrend(rSquared, newValues_x, newValues_y) {

 trendData = calcLinear(newValues_x, newValues_y);

    // display r-square on the chart
    rSquared.transition()
        .duration(1000)
        .text("R-squared: " + trendData[2].toFixed(2))        
        .attr("x", width * .8)
        .attr("y", height * .05);

    return rSquared;
}

function buildTable(data) {
  let tbody = d3.select("tbody");
  // clear table
  tbody.html("");

  // Next, loop through each object in the data
  // and append a row and cells for each value in the row
  data.forEach((dataRow) => {
    // Append a row to the table body
    var row = tbody.append("tr");
    row.attr("class", "table-primary");
    // Loop through each field in the dataRow and add
    // each value as a table cell (td)
    Object.values(dataRow).forEach((val) => {
      var cell = row.append("td");
      cell.text(val);
    });
  });
}

// function used for updating circles group with new tooltip
function updateToolTip(chosenXAxis, chosenYAxis, circlesGroup) {
    let xLabel = ''
    let yLabel = ''
    // console.log(chosenXAxis);
    switch (chosenXAxis) {

        case "poverty":
            xLabel = "Percentage in Poverty";
            break;
        case "income":
            xLabel = "Median Income";
            break;
        case "age":
            xLabel = "Median Age";
            break;

    }
    switch (chosenYAxis) {
        case "obesity":
            yLabel = "Percentage Obese";
            break;
        case "healthcare":
            yLabel = "Percentage that Lacks Healthcare";
            break;
        case "smokes":
            yLabel = "Percentage of Smokers";
            break;
    }
    // console.log(xLabel);

    let toolTip = d3.tip()
        .attr("class", "tooltip")
        .offset([85, -90])
        .html(function(d) {
            return (`${d.state}<br>${yLabel}: ${d[chosenYAxis]}<br>${xLabel}: ${d[chosenXAxis]}`);
        });

    circlesGroup.call(toolTip);

    circlesGroup.on("mouseover", (d, i, n) => toolTip.show(d, n[i]));
    circlesGroup.on("mouseout", (d, i, n) => toolTip.hide(d, n[i]));

    return circlesGroup;
}

//Read the data
d3.csv("assets/data/data.csv").then(function(stateData) {

    // parse data
    stateData.forEach(function(data) {
        data.poverty = +data.poverty;
        data.age = +data.age;
        data.income = +data.income;
        data.healthcare = +data.healthcare;
        data.obesity = +data.obesity;
        data.smokes = +data.smokes;
    });

    // populate table
    buildTable(stateData);
  
    let xLinearScale = xScale(stateData, chosenXAxis);
    let yLinearScale = yScale(stateData, chosenYAxis);

    // Create initial axis functions
    let bottomAxis = d3.axisBottom(xLinearScale);
    let leftAxis = d3.axisLeft(yLinearScale);

    // append x axis
    let xAxis = chartGroup.append("g")
        .classed("x-axis", true)
        .attr("transform", `translate(0, ${height})`)
        .call(bottomAxis);

    // append y axis
    let yAxis = chartGroup.append("g")
        .classed("y-axis", true)
        .attr("transform", `translate(0, 0)`)
        .call(leftAxis);

    // append initial circles
    let circlesGroup = chartGroup.selectAll("circle")
        .data(stateData)
        .enter()
        .append("circle")
        .attr("cx", d => xLinearScale(d[chosenXAxis]))
        .attr("cy", d => yLinearScale(d[chosenYAxis]))
        .attr("r", 10)
        .attr("fill", "#69b3a2")
        .attr("opacity", ".5");

    let circlesGroupText = chartGroup.selectAll()
        .data(stateData)
        .enter()
        .append("text")
        .attr("x", d => xLinearScale(d[chosenXAxis]))
        .attr("y", d => yLinearScale(d[chosenYAxis]))
        .text(d => d.abbr)
        .attr("fill", "#343a40")
        .style("font-size", "8px")
        .style("text-anchor", "middle");

    let values_x = stateData.map(d => d[chosenXAxis]);
    let values_y = stateData.map(d => d[chosenYAxis]);

    let trendData = calcLinear(values_x, values_y);

    // display r-square on the chart
    let rSquared = chartGroup.append("text")
        .text("R-squared: " + trendData[2].toFixed(2))
        .attr("class", "text-label")
        .attr("x", width * .8)
        .attr("y", height * .05);

    // Create group for  3 x- axis labels
    let xLabelsGroup = chartGroup.append("g")
        .attr("transform", `translate(${width / 2}, ${height + 20})`);

    let povertyLabel = xLabelsGroup.append("text")
        .attr("x", 0)
        .attr("y", 20)
        .attr("value", "poverty") // value to grab for event listener
        .classed("active", true)
        .text("Percentage in Poverty");

    let incomeLabel = xLabelsGroup.append("text")
        .attr("x", 0)
        .attr("y", 40)
        .attr("value", "income") // value to grab for event listener
        .classed("inactive", true)
        .text("Median Income");

    let ageLabel = xLabelsGroup.append("text")
        .attr("x", 0)
        .attr("y", 60)
        .attr("value", "age") // value to grab for event listener
        .classed("inactive", true)
        .text("Median Age");

    // Create group for  3 y- axis labels
    let yLabelsGroup = chartGroup.append("g")
        .attr("transform", "rotate(-90) translate(-100, -8)")
        .attr("y", 0 - margin.left)
        .attr("x", 0 - (height / 2))
        .attr("dy", "1em")
        .classed("axis-text", true)
        .style("text-anchor", "middle")

    let obesityLabel = yLabelsGroup.append("text")
        .attr("x", 0)
        .attr("y", -20)
        .attr("value", "obesity") // value to grab for event listener
        .classed("active", true)
        .text("Percentage Obese");

    let healthcareLabel = yLabelsGroup.append("text")
        .attr("x", 0)
        .attr("y", -40)
        .attr("value", "healthcare") // value to grab for event listener
        .classed("inactive", true)
        .text("Percentage that Lack Healthcare");

    let smokerLabel = yLabelsGroup.append("text")
        .attr("x", 0)
        .attr("y", -60)
        .attr("value", "smokes") // value to grab for event listener
        .classed("inactive", true)
        .text("Percentage of Smokers");
    // updateToolTip function above csv import
    circlesGroup = updateToolTip(chosenXAxis, chosenYAxis, circlesGroup, stateData);

    // x axis labels event listener
    xLabelsGroup.selectAll("text")
        .on("click", function() {
            // get value of selection
            const value = d3.select(this).attr("value");
            if (value !== chosenXAxis) {

                // replaces chosenXAxis with value
                chosenXAxis = value;

                // console.log(chosenXAxis);

                // functions here found above csv import
                // updates x scale for new data
                xLinearScale = xScale(stateData, chosenXAxis);

                // updates x axis with transition
                xAxis = renderXAxis(xLinearScale, xAxis);

                // updates circles with new x values
                circlesGroup = renderCircles(circlesGroup, xLinearScale, yLinearScale, chosenXAxis, chosenYAxis);
                circlesGroupText = renderCirclesText(circlesGroupText, xLinearScale, yLinearScale, chosenXAxis, chosenYAxis);
                // updates tooltips with new info
                circlesGroup = updateToolTip(chosenXAxis, chosenYAxis, circlesGroup, circlesGroupText);

                // Update R squared
                values_x = stateData.map(d => d[chosenXAxis]);
                values_y = stateData.map(d => d[chosenYAxis]);
                rSquared = renderTrend(rSquared, values_x, values_y);

                // changes classes to change bold text
                switch (chosenXAxis) {
                    case "poverty":
                        povertyLabel
                            .classed("active", true)
                            .classed("inactive", false);
                        incomeLabel
                            .classed("active", false)
                            .classed("inactive", true);
                        ageLabel
                            .classed("active", false)
                            .classed("inactive", true);
                        break;
                    case "age":
                        povertyLabel
                            .classed("active", false)
                            .classed("inactive", true);
                        incomeLabel
                            .classed("active", false)
                            .classed("inactive", true);
                        ageLabel
                            .classed("active", true)
                            .classed("inactive", false);
                        break;
                    case "income":
                        povertyLabel
                            .classed("active", false)
                            .classed("inactive", true);
                        incomeLabel
                            .classed("active", true)
                            .classed("inactive", false);
                        ageLabel
                            .classed("active", false)
                            .classed("inactive", true);
                        break;
                }
            }
            // y axis labels event listener
            yLabelsGroup.selectAll("text")
                .on("click", function() {
                    // get value of selection
                    let value = d3.select(this).attr("value");
                    if (value !== chosenYAxis) {

                        // replaces chosenXAxis with value
                        chosenYAxis = value;

                        // console.log(chosenYAxis);

                        // functions here found above csv import
                        // updates y scale for new data
                        yLinearScale = yScale(stateData, chosenYAxis);

                        // updates y axis with transition
                        yAxis = renderYAxis(yLinearScale, yAxis);

                        // updates circles with new y values
                        circlesGroup = renderCircles(circlesGroup, xLinearScale, yLinearScale, chosenXAxis, chosenYAxis);
                        circlesGroupText = renderCirclesText(circlesGroupText, xLinearScale, yLinearScale, chosenXAxis, chosenYAxis);

                        // updates tooltips with new info
                        circlesGroup = updateToolTip(chosenXAxis, chosenYAxis, circlesGroup);

                        // Update R squared
                        values_x = stateData.map(d => d[chosenXAxis]);
                        values_y = stateData.map(d => d[chosenYAxis]);

                        rSquared = renderTrend(rSquared, values_x, values_y);

                        // changes classes to change bold text
                        switch (chosenYAxis) {
                            case "obesity":
                                obesityLabel
                                    .classed("active", true)
                                    .classed("inactive", false);
                                smokerLabel
                                    .classed("active", false)
                                    .classed("inactive", true);
                                healthcareLabel
                                    .classed("active", false)
                                    .classed("inactive", true);
                                break;
                            case "smokes":
                                obesityLabel
                                    .classed("active", false)
                                    .classed("inactive", true);
                                smokerLabel
                                    .classed("active", true)
                                    .classed("inactive", false);
                                healthcareLabel
                                    .classed("active", false)
                                    .classed("inactive", true);
                                break;
                            case "healthcare":
                                obesityLabel
                                    .classed("active", false)
                                    .classed("inactive", true);
                                smokerLabel
                                    .classed("active", false)
                                    .classed("inactive", true);
                                healthcareLabel
                                    .classed("active", true)
                                    .classed("inactive", false);
                                break;
                        }
                    }
                });
        });
});