Introduction

For this report, a data set of district wide standardized test results was analyzed to search for trends or actionable insights with the goal of approving student success overall.

Overview of the Data

The analyzed data set includes information on 15 highschools with a total of 39,170 students. Parameters included are budget per school, student names and IDs, school size and math and reading scores. Below is a high level summary for the entire District.

|   | Total Schools | Total Students | Total Budget   | Average Math Score | Average Reading Score | % Passing Math | % Passing Reading | % Overall Passing Rate |
|---|---------------|----------------|----------------|--------------------|-----------------------|----------------|-------------------|------------------------|
| 0 | 15            | 39,170         | $24,649,428.00 | 78.985371          | 81.87784              | 74.98%         | 85.81%            | 80.43%                 |

Methods

Jupyter notebooks with the pandas python library was used to merge, parse and aggregate the data.

Analysis

The data was first grouped by school to find total students, per student budget, average scores and school population passing rate for both math and reading. This grouped data was then used to show the top and bottom performing schools. 
Next, scores were checked across grades to check for trends.
The final three tables show analysis of scores by school spending, size and type.

Results of Analysis

Charter schools were observed to have higher scores than district schools. When all schools are ranked, place 1-8 are occupied by Charter Schools and places 9-15 were occupied by District Schools.

Scores held steady through all grades in each school with an average sample variance by school of .25 for math and .15 for reading. In contrast, the sample variance by grade across all schools was 11 for math and 2.5 for reading.

Per student spending did not correlate with higher scores, in fact the data shows the opposite to be true with schools spending less than $615 per student achieving a 95% passing rate, schools spending $615-$645 per student find passing rates drop to 80% and schools in the highest bracket of spending suffering a further drop in passing rates to 74%.

Both school size and school type were shown to have an effect on student math and reading scores. Schools with less than 2000 students have an average 95% passing rate while schools above 2000 students average only 76% passing rate. This trend is especially pronounced in math scores, with above and below 2000 students showing 93.5% and 70% passing rate, respectively. Charter schools had an overall passing rate of 95% while District schools show only a 73% passing rate. Again this is most dramatic in math scores with a 93.5% passing rate for Charter schools and 66.5% passing rate for District schools.

Conclusions

This analysis suggests that the District should invest in building more schools to reduce number of students per school, as increasing a school's budget alone has not been shown to increase math or reading scores.

More analysis should be done on differences between Charter and District schools so that the District schools can identify changes to be implemented so that Charter school success can be emulated.
