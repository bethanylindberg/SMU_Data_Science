// from data.js
var tableData,tbody,filter,row,cell;
tableData = data;
tbody = d3.select("tbody");
row = tbody.append("tr");
cell = row.append("td");
//Select filter button
filter = d3.select('#filter-btn');
//Populate table with all data
tableData.forEach((UFOreport) => {
    row = tbody.append("tr");
    Object.entries(UFOreport).forEach(([key, value]) => {
    cell = row.append("td");
    cell.text(value);
    });
  });

//Click handler
filter.on("click",function(){
    //Clear table
    tbody.html("");
    // Prevent the page from refreshing
    d3.event.preventDefault();
    // Select the input element and get the raw HTML node
    var inputElement = d3.select(".form-control");
    // Get the value property of the input element
    var inputValue = inputElement.property("value");
    //Filter Data by Input Value
    filteredData = tableData.filter(date => date.datetime === inputValue);
    //Append filtered data to table
    filteredData.forEach((UFOreport) => {
        row = tbody.append("tr");
        Object.entries(UFOreport).forEach(([key, value]) => {
            cell = row.append("td");
            cell.text(value);
        });
    });   
});