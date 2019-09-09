// from data.js
var tableData,tbody,filter,row,cell;
tableData = data;
// table elements variables
tbody = d3.select("tbody");
row = tbody.append("tr");
cell = row.append("td");
// Select filter button
filter = d3.select('#filter-btn');
// Populate table with all data
tableData.forEach((UFOreport) => {
    row = tbody.append("tr");
    Object.entries(UFOreport).forEach(([key, value]) => {
    cell = row.append("td");
    cell.text(value);
    });
  });

// Click handler
filter.on("click",function(){
    // Clear table
    tbody.html("");
    // Prevent the page from refreshing
    d3.event.preventDefault();
    // Select the input element and get the raw HTML node
    var inputElement = d3.selectAll(".form-control");
    // Get the value property of the input element
    var inputValue = []
    inputElement.each(function(){
        inputValue.push(this.value);
    });
    // Filter Data by Input Value
    filteredData = tableData;
    if (inputValue[0] != ''){
        filteredData = filteredData.filter(sighting => sighting.datetime === inputValue[0]);
    }
    if (inputValue[1] != ''){
        filteredData = filteredData.filter(sighting => sighting.city === inputValue[1].toLowerCase());
    }
    if (inputValue[2] != ''){
        filteredData = filteredData.filter(sighting => sighting.state === inputValue[2].toLowerCase());
    }
    if (inputValue[3] != ''){
        filteredData = filteredData.filter(sighting => sighting.country === inputValue[3].toLowerCase());
    }
    if (inputValue[4] != ''){
        filteredData = filteredData.filter(sighting => sighting.shape === inputValue[4].toLowerCase());
    }
    // Append filtered data to table
    filteredData.forEach((UFOreport) => {
        row = tbody.append("tr");
        Object.entries(UFOreport).forEach(([key, value]) => {
            cell = row.append("td");
            cell.text(value);
        });
    });   
});