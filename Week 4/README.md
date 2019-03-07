PyCity Schools Introduction

For this report, a data set of district wide standardized test results was analyzed to search for trends or actionable insights with the goal of approving student success overall.

Overview of the Data

The analyzed data set includes information on 15 highschools with a total of 39,170 students. Parameters included are budget per school, student names & IDs, math & reading scores and school size. Below is a high level summary for the entire District.

|   | Total Schools | Total Students | Total Budget   | Average Math Score | Average Reading Score | % Passing Math | % Passing Reading | % Overall Passing Rate |
|---|---------------|----------------|----------------|--------------------|-----------------------|----------------|-------------------|------------------------|
| 0 | 15            | 39,170         | $24,649,428.00 | 78.985371          | 81.87784              | 74.98%         | 85.81%            | 80.43%                 |

Methods

Jupyter notebooks with the pandas python library was used to merge, parse and aggregate the data. (see 'PyCity Schools.ipynb')

Analysis

The data was first grouped by school to find total students, per student budget, average scores and school population passing rate for both math and reading.(Out[3]) 

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>% Overall Passing Rate</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Per Student Budget</th>
      <th>Total School Budget</th>
      <th>Total Students</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th>Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <th>District</th>
      <td>74.306672</td>
      <td>66.680064</td>
      <td>81.933280</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>628.0</td>
      <td>$3,124,928.00</td>
      <td>4976</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <th>Charter</th>
      <td>95.586652</td>
      <td>94.133477</td>
      <td>97.039828</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>582.0</td>
      <td>$1,081,356.00</td>
      <td>1858</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <th>District</th>
      <td>73.363852</td>
      <td>65.988471</td>
      <td>80.739234</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>639.0</td>
      <td>$1,884,411.00</td>
      <td>2949</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <th>District</th>
      <td>73.804308</td>
      <td>68.309602</td>
      <td>79.299014</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>644.0</td>
      <td>$1,763,916.00</td>
      <td>2739</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <th>Charter</th>
      <td>95.265668</td>
      <td>93.392371</td>
      <td>97.138965</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>625.0</td>
      <td>$917,500.00</td>
      <td>1468</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <th>District</th>
      <td>73.807983</td>
      <td>66.752967</td>
      <td>80.862999</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>652.0</td>
      <td>$3,022,020.00</td>
      <td>4635</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <th>Charter</th>
      <td>94.379391</td>
      <td>92.505855</td>
      <td>96.252927</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>581.0</td>
      <td>$248,087.00</td>
      <td>427</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <th>District</th>
      <td>73.500171</td>
      <td>65.683922</td>
      <td>81.316421</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>655.0</td>
      <td>$1,910,635.00</td>
      <td>2917</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <th>District</th>
      <td>73.639992</td>
      <td>66.057551</td>
      <td>81.222432</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>650.0</td>
      <td>$3,094,650.00</td>
      <td>4761</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <th>Charter</th>
      <td>95.270270</td>
      <td>94.594595</td>
      <td>95.945946</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>609.0</td>
      <td>$585,858.00</td>
      <td>962</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <th>District</th>
      <td>73.293323</td>
      <td>66.366592</td>
      <td>80.220055</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>637.0</td>
      <td>$2,547,363.00</td>
      <td>3999</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <th>Charter</th>
      <td>94.860875</td>
      <td>93.867121</td>
      <td>95.854628</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>600.0</td>
      <td>$1,056,600.00</td>
      <td>1761</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <th>Charter</th>
      <td>95.290520</td>
      <td>93.272171</td>
      <td>97.308869</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>638.0</td>
      <td>$1,043,130.00</td>
      <td>1635</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <th>Charter</th>
      <td>95.203679</td>
      <td>93.867718</td>
      <td>96.539641</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>578.0</td>
      <td>$1,319,574.00</td>
      <td>2283</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <th>Charter</th>
      <td>94.972222</td>
      <td>93.333333</td>
      <td>96.611111</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>583.0</td>
      <td>$1,049,400.00</td>
      <td>1800</td>
    </tr>
  </tbody>
</table>
</div>


This grouped data was then used to show the top and bottom performing schools. (Out[4-5])
Next, scores were checked across grades to check for trends. (Out[6-7])
The final three tables show analysis of scores by school spending, size and type. (Out[8-10])

Results of Analysis

Charter schools were observed to have higher scores than district schools. When all schools are ranked, places 1-8 are occupied by Charter Schools and places 9-15 are occupied by District Schools. (Out[4])

Scores held steady through all grades in each school with an average sample variance by school of .25 for math and .15 for reading. In contrast, the sample variance by grade across all schools was 11 for math and 2.5 for reading. (Out[6-7])

Per student spending did not correlate with higher scores, in fact the data shows the opposite to be true with schools spending less than $615 per student achieving a 95% passing rate, schools spending $615-$645 per student find passing rates drop to 80% and schools in the highest bracket of spending suffering a further drop in passing rates to 74%. (Out[8])

Both school size and school type were shown to have an effect on student math and reading scores. Schools with less than 2000 students have an average 95% passing rate while schools above 2000 students average only 76% passing rate. This trend is especially pronounced in math scores, with above and below 2000 students showing 93.5% and 70% passing rate, respectively. Charter schools had an overall passing rate of 95% while District schools show only a 73% passing rate. Again this is most dramatic in math scores with a 93.5% passing rate for Charter schools and 66.5% passing rate for District schools. (Out[9-10])

Conclusions

This analysis suggests that the District should invest in building more schools to reduce number of students per school, as increasing a school's budget alone has not been shown to increase math or reading scores.

More analysis should be done on differences between Charter and District schools so that the District schools can identify changes to be implemented so that Charter school success can be emulated.

__________
