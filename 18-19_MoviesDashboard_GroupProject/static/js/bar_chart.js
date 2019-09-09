// Define SVG area dimensions
var svgWidth = window.innerWidth * .3;
var svgHeight = window.innerHeight * .3;

// Define the chart's margins as an object
var chartMargin = {
  top: 30,
  right: 30,
  bottom: 30,
  left: 5
};

// Define dimensions of the chart area
var width = svgWidth - chartMargin.left - chartMargin.right;
var height = svgHeight - chartMargin.top - chartMargin.bottom;

// Select body, append SVG area to it, and set the dimensions
var svg = d3.select("#bar-chart")
  .append("svg")
  .attr("height", svgHeight)
  .attr("width", svgWidth);

// Append a group to the SVG area and shift ('translate') it to the right and to the bottom
var chartGroup = svg.append("g")
  .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);

// Load data from hours-of-tv-watched.csv
let selection = "Morgan Freeman";

d3.json("/Output/query.json").then(function(data){
  var movies = data[selection].movies;
  var moviesToCount = [];
  moviesToCount=0

  for (var i = 0; i<movies.length; i++){
    
    if (movies[i].title !== null){
//       moviesToCount.push(movies[i]);
//     }
//   }
//   moviesToCount.forEach(function(d){
//     d.title = d.title;
//   });
//   //Draw the Rectangle
//   var rectangle = chartGroup
//                   .append("rect")
//                   .attr("x", i*10)
//                   .attr("y", i)
//                   .attr("width", 5)
//                   .attr("height", moviesToCount.length)
//                   .style("fill", 000000);
// });
      moviesToCount = moviesToCount + 1;
    }
    console.log (moviesToCount)
  }
  var rectangle = chartGroup
    .append("rect")
    .attr("x", 0)
    .attr("y", 5)
    .attr("width", 100)
    .attr("height", moviesToCount)
    .attr("fill", 'red');

  var text = chartGroup.selectAll("text")
    .data(movies)
    .enter()
    .append("text");

  var textLabels = text
    .attr("x",30)
    .attr("y", 5)
    .text( moviesToCount)
    .attr("font-family", "sans-serif")
    .attr("font-size", "20px")
    .attr("height", moviesToCount+100)
    .attr("fill", "black");
});
