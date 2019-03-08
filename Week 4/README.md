# PyCity Schools Introduction

For this report, a data set of district wide standardized test results was analyzed to search for trends or actionable insights with the goal of approving student success overall.

# Overview of the Data

The analyzed data set includes information on 15 highschools with a total of 39,170 students. Parameters included are budget per school, student names & IDs, math & reading scores and school size. Below is a high level summary for the entire District.

## District Summary
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39,170</td>
      <td>$24,649,428.00</td>
      <td>78.98</td>
      <td>81.87</td>
      <td>74.98%</td>
      <td>85.81%</td>
      <td>80.43%</td>
    </tr>
  </tbody>
</table>
</div>

# Methods

Jupyter notebooks with the pandas python library was used to merge, parse and aggregate the data. (see 'PyCity Schools.ipynb')

# Analysis

The data was first grouped by school to find total students, per student budget, average scores and school population passing rate for both math and reading.(Out[3]) 

## School Summary
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
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
      <td>4976</td>
      <td>$3,124,928.00</td>
      <td>628.0</td>
      <td>77.05</td>
      <td>81.03</td>
      <td>66.68</td>
      <td>81.93</td>
      <td>74.31</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <th>Charter</th>
      <td>1858</td>
      <td>$1,081,356.00</td>
      <td>582.0</td>
      <td>83.06</td>
      <td>83.98</td>
      <td>94.13</td>
      <td>97.04</td>
      <td>95.58</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <th>District</th>
      <td>2949</td>
      <td>$1,884,411.00</td>
      <td>639.0</td>
      <td>76.71</td>
      <td>81.16</td>
      <td>65.99</td>
      <td>80.74</td>
      <td>73.36</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <th>District</th>
      <td>2739</td>
      <td>$1,763,916.00</td>
      <td>644.0</td>
      <td>77.10</td>
      <td>80.75</td>
      <td>68.31</td>
      <td>79.30</td>
      <td>73.81</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <th>Charter</th>
      <td>1468</td>
      <td>$917,500.00</td>
      <td>625.0</td>
      <td>83.35</td>
      <td>83.82</td>
      <td>93.39</td>
      <td>97.14</td>
      <td>95.26</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <th>District</th>
      <td>4635</td>
      <td>$3,022,020.00</td>
      <td>652.0</td>
      <td>77.29</td>
      <td>80.93</td>
      <td>66.75</td>
      <td>80.86</td>
      <td>73.81</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <th>Charter</th>
      <td>427</td>
      <td>$248,087.00</td>
      <td>581.0</td>
      <td>83.80</td>
      <td>83.81</td>
      <td>92.51</td>
      <td>96.25</td>
      <td>94.38</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <th>District</th>
      <td>2917</td>
      <td>$1,910,635.00</td>
      <td>655.0</td>
      <td>76.63</td>
      <td>81.18</td>
      <td>65.68</td>
      <td>81.32</td>
      <td>73.50</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <th>District</th>
      <td>4761</td>
      <td>$3,094,650.00</td>
      <td>650.0</td>
      <td>77.07</td>
      <td>80.97</td>
      <td>66.06</td>
      <td>81.22</td>
      <td>73.64</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <th>Charter</th>
      <td>962</td>
      <td>$585,858.00</td>
      <td>609.0</td>
      <td>83.84</td>
      <td>84.04</td>
      <td>94.59</td>
      <td>95.95</td>
      <td>95.27</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <th>District</th>
      <td>3999</td>
      <td>$2,547,363.00</td>
      <td>637.0</td>
      <td>76.84</td>
      <td>80.74</td>
      <td>66.37</td>
      <td>80.22</td>
      <td>73.30</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <th>Charter</th>
      <td>1761</td>
      <td>$1,056,600.00</td>
      <td>600.0</td>
      <td>83.36</td>
      <td>83.73</td>
      <td>93.87</td>
      <td>95.85</td>
      <td>94.86</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <th>Charter</th>
      <td>1635</td>
      <td>$1,043,130.00</td>
      <td>638.0</td>
      <td>83.42</td>
      <td>83.85</td>
      <td>93.27</td>
      <td>97.31</td>
      <td>95.29</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <th>Charter</th>
      <td>2283</td>
      <td>$1,319,574.00</td>
      <td>578.0</td>
      <td>83.27</td>
      <td>83.99</td>
      <td>93.87</td>
      <td>96.54</td>
      <td>95.21</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <th>Charter</th>
      <td>1800</td>
      <td>$1,049,400.00</td>
      <td>583.0</td>
      <td>83.68</td>
      <td>83.96</td>
      <td>93.33</td>
      <td>96.61</td>
      <td>94.97</td>
    </tr>
  </tbody>
</table>
</div>

This grouped data was then used to show the top and bottom performing schools. (Out[4-5])

## Top Performing Schools
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
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
      <th>Cabrera High School</th>
      <th>Charter</th>
      <td>1858</td>
      <td>$1,081,356.00</td>
      <td>582.0</td>
      <td>83.06</td>
      <td>83.98</td>
      <td>94.13</td>
      <td>97.04</td>
      <td>95.58</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <th>Charter</th>
      <td>1635</td>
      <td>$1,043,130.00</td>
      <td>638.0</td>
      <td>83.42</td>
      <td>83.85</td>
      <td>93.27</td>
      <td>97.31</td>
      <td>95.29</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <th>Charter</th>
      <td>962</td>
      <td>$585,858.00</td>
      <td>609.0</td>
      <td>83.84</td>
      <td>84.04</td>
      <td>94.59</td>
      <td>95.95</td>
      <td>95.27</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <th>Charter</th>
      <td>1468</td>
      <td>$917,500.00</td>
      <td>625.0</td>
      <td>83.35</td>
      <td>83.82</td>
      <td>93.39</td>
      <td>97.14</td>
      <td>95.26</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <th>Charter</th>
      <td>2283</td>
      <td>$1,319,574.00</td>
      <td>578.0</td>
      <td>83.27</td>
      <td>83.99</td>
      <td>93.87</td>
      <td>96.54</td>
      <td>95.21</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <th>Charter</th>
      <td>1800</td>
      <td>$1,049,400.00</td>
      <td>583.0</td>
      <td>83.68</td>
      <td>83.96</td>
      <td>93.33</td>
      <td>96.61</td>
      <td>94.97</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <th>Charter</th>
      <td>1761</td>
      <td>$1,056,600.00</td>
      <td>600.0</td>
      <td>83.36</td>
      <td>83.73</td>
      <td>93.87</td>
      <td>95.85</td>
      <td>94.86</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <th>Charter</th>
      <td>427</td>
      <td>$248,087.00</td>
      <td>581.0</td>
      <td>83.80</td>
      <td>83.81</td>
      <td>92.51</td>
      <td>96.25</td>
      <td>94.38</td>
    </tr>
    <tr>
      <th>Bailey High School</th>
      <th>District</th>
      <td>4976</td>
      <td>$3,124,928.00</td>
      <td>628.0</td>
      <td>77.05</td>
      <td>81.03</td>
      <td>66.68</td>
      <td>81.93</td>
      <td>74.31</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <th>District</th>
      <td>2739</td>
      <td>$1,763,916.00</td>
      <td>644.0</td>
      <td>77.10</td>
      <td>80.75</td>
      <td>68.31</td>
      <td>79.30</td>
      <td>73.81</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <th>District</th>
      <td>4635</td>
      <td>$3,022,020.00</td>
      <td>652.0</td>
      <td>77.29</td>
      <td>80.93</td>
      <td>66.75</td>
      <td>80.86</td>
      <td>73.81</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <th>District</th>
      <td>4761</td>
      <td>$3,094,650.00</td>
      <td>650.0</td>
      <td>77.07</td>
      <td>80.97</td>
      <td>66.06</td>
      <td>81.22</td>
      <td>73.64</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <th>District</th>
      <td>2917</td>
      <td>$1,910,635.00</td>
      <td>655.0</td>
      <td>76.63</td>
      <td>81.18</td>
      <td>65.68</td>
      <td>81.32</td>
      <td>73.50</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <th>District</th>
      <td>2949</td>
      <td>$1,884,411.00</td>
      <td>639.0</td>
      <td>76.71</td>
      <td>81.16</td>
      <td>65.99</td>
      <td>80.74</td>
      <td>73.36</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <th>District</th>
      <td>3999</td>
      <td>$2,547,363.00</td>
      <td>637.0</td>
      <td>76.84</td>
      <td>80.74</td>
      <td>66.37</td>
      <td>80.22</td>
      <td>73.30</td>
    </tr>
  </tbody>
</table>
</div>

Next, scores were checked across grades to check for trends. (Out[6-7])

## Math scores by grade
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.08</td>
      <td>77.00</td>
      <td>77.52</td>
      <td>76.49</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.09</td>
      <td>83.15</td>
      <td>82.77</td>
      <td>83.28</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.40</td>
      <td>76.54</td>
      <td>76.88</td>
      <td>77.15</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.36</td>
      <td>77.67</td>
      <td>76.92</td>
      <td>76.18</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>82.04</td>
      <td>84.23</td>
      <td>83.84</td>
      <td>83.36</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.44</td>
      <td>77.34</td>
      <td>77.14</td>
      <td>77.19</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.79</td>
      <td>83.43</td>
      <td>85.00</td>
      <td>82.86</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>77.03</td>
      <td>75.91</td>
      <td>76.45</td>
      <td>77.23</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.19</td>
      <td>76.69</td>
      <td>77.49</td>
      <td>76.86</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.63</td>
      <td>83.37</td>
      <td>84.33</td>
      <td>84.12</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.86</td>
      <td>76.61</td>
      <td>76.40</td>
      <td>77.69</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.42</td>
      <td>82.92</td>
      <td>83.38</td>
      <td>83.78</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.59</td>
      <td>83.09</td>
      <td>83.50</td>
      <td>83.50</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.09</td>
      <td>83.72</td>
      <td>83.20</td>
      <td>83.04</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.26</td>
      <td>84.01</td>
      <td>83.84</td>
      <td>83.64</td>
    </tr>
  </tbody>
</table>
</div>

## Reading Scores by Grade
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>81.30</td>
      <td>80.91</td>
      <td>80.95</td>
      <td>80.91</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.68</td>
      <td>84.25</td>
      <td>83.79</td>
      <td>84.29</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.20</td>
      <td>81.41</td>
      <td>80.64</td>
      <td>81.38</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>80.63</td>
      <td>81.26</td>
      <td>80.40</td>
      <td>80.66</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.37</td>
      <td>83.71</td>
      <td>84.29</td>
      <td>84.01</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.87</td>
      <td>80.66</td>
      <td>81.40</td>
      <td>80.86</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.68</td>
      <td>83.32</td>
      <td>83.82</td>
      <td>84.70</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.29</td>
      <td>81.51</td>
      <td>81.42</td>
      <td>80.31</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>81.26</td>
      <td>80.77</td>
      <td>80.62</td>
      <td>81.23</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.81</td>
      <td>83.61</td>
      <td>84.34</td>
      <td>84.59</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.99</td>
      <td>80.63</td>
      <td>80.86</td>
      <td>80.38</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>84.12</td>
      <td>83.44</td>
      <td>84.37</td>
      <td>82.78</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.73</td>
      <td>84.25</td>
      <td>83.59</td>
      <td>83.83</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.94</td>
      <td>84.02</td>
      <td>83.76</td>
      <td>84.32</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.83</td>
      <td>83.81</td>
      <td>84.16</td>
      <td>84.07</td>
    </tr>
  </tbody>
</table>
</div>

The final three tables show analysis of scores by school spending, size and type. (Out[8-10])

## Scores by School Spending
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Spending</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;$585</th>
      <td>83.45</td>
      <td>83.94</td>
      <td>93.46</td>
      <td>96.61</td>
      <td>95.04</td>
    </tr>
    <tr>
      <th>$585-615</th>
      <td>83.60</td>
      <td>83.88</td>
      <td>94.23</td>
      <td>95.90</td>
      <td>95.06</td>
    </tr>
    <tr>
      <th>$615-645</th>
      <td>79.08</td>
      <td>81.89</td>
      <td>75.67</td>
      <td>86.11</td>
      <td>80.89</td>
    </tr>
    <tr>
      <th>$645-675</th>
      <td>77.00</td>
      <td>81.03</td>
      <td>66.16</td>
      <td>81.13</td>
      <td>73.65</td>
    </tr>
  </tbody>
</table>
</div>

## Scores by School Size
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Small (&lt;1000)</th>
      <td>83.82</td>
      <td>83.93</td>
      <td>93.55</td>
      <td>96.10</td>
      <td>94.82</td>
    </tr>
    <tr>
      <th>Medium (1000-2000)</th>
      <td>83.37</td>
      <td>83.87</td>
      <td>93.60</td>
      <td>96.79</td>
      <td>95.19</td>
    </tr>
    <tr>
      <th>Large (2000-5000)</th>
      <td>77.74</td>
      <td>81.34</td>
      <td>69.96</td>
      <td>82.77</td>
      <td>76.37</td>
    </tr>
  </tbody>
</table>
</div>

## Scores by School Type
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>83.47</td>
      <td>83.90</td>
      <td>93.62</td>
      <td>96.59</td>
      <td>95.10</td>
    </tr>
    <tr>
      <th>District</th>
      <td>76.96</td>
      <td>80.97</td>
      <td>66.55</td>
      <td>80.80</td>
      <td>73.68</td>
    </tr>
  </tbody>
</table>
</div>

# Results of Analysis

Charter schools were observed to have higher scores than district schools. When all schools are ranked, places 1-8 are occupied by Charter Schools and places 9-15 are occupied by District Schools. (Top Performing Schools)

Scores held steady through all grades in each school with an average sample variance by school of .25 for math and .15 for reading. In contrast, the sample variance by grade across all schools was 11 for math and 2.5 for reading. (Scores by Grade)

Per student spending did not correlate with higher scores, in fact the data shows the opposite to be true with schools spending less than $615 per student achieving a 95% passing rate, schools spending $615-$645 per student find passing rates drop to 80% and schools in the highest bracket of spending suffering a further drop in passing rates to 74%. (Scores by School Spending)

Both school size and school type were shown to have an effect on student math and reading scores. Schools with less than 2000 students have an average 95% passing rate while schools above 2000 students average only 76% passing rate. This trend is especially pronounced in math scores, with above and below 2000 students showing 93.5% and 70% passing rate, respectively. Charter schools had an overall passing rate of 95% while District schools show only a 73% passing rate. Again this is most dramatic in math scores with a 93.5% passing rate for Charter schools and 66.5% passing rate for District schools. (Scores by School Size/Type)

# Conclusions

This analysis suggests that the District should invest in building more schools to reduce number of students per school, as increasing a school's budget alone has not been shown to increase math or reading scores.

More analysis should be done on differences between Charter and District schools so that the District schools can identify changes to be implemented so that Charter school success can be emulated.

__________


# Heroes of Pymoli Introduction

With free to play games such as Heroes of Pymoli, in game purchases are an important source of revenue. This analysis is intended to identify action steps to both increase profitability and improve user experience.

# Overview of the Data

The data set analyzed is a total of 780 purchases that included age and gender demographics for the purchasers as well as price, item ID and item name for the purchased items.

# Methods

Jupyter notebooks with the pandas python library was used to parse and aggregate the data.

# Analysis

The data was grouped by sign name to identify the number of unique players making purchases. 
Next a high level summary of total items, purchases and average price per item was done as a starting point.

## Item Overview
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>183</td>
      <td>$3.05</td>
      <td>780</td>
      <td>$2,379.77</td>
    </tr>
  </tbody>
</table>
</div>

Sign names were next grouped by age and gender an analyze trends in purchase count, average purchase price, total purchase value and average purchase per person for each demographic.

## Gender Demographics
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Count</th>
      <th>Percentage of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>484</td>
      <td>84.03%</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>81</td>
      <td>14.06%</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>1.91%</td>
    </tr>
  </tbody>
</table>
</div>

## Purchasing Analysis (Gender)
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Average Purchase per person</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>113</td>
      <td>$3.20</td>
      <td>$361.94</td>
      <td>$4.47</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>652</td>
      <td>$3.02</td>
      <td>$1967.64</td>
      <td>$4.07</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>15</td>
      <td>$3.35</td>
      <td>$50.19</td>
      <td>$4.56</td>
    </tr>
  </tbody>
</table>
</div>

## Age Demographics
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Count</th>
      <th>Percentage of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>17</td>
      <td>2.95%</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>22</td>
      <td>3.82%</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>107</td>
      <td>18.58%</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>258</td>
      <td>44.79%</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>77</td>
      <td>13.37%</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>52</td>
      <td>9.03%</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>31</td>
      <td>5.38%</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>12</td>
      <td>2.08%</td>
    </tr>
  </tbody>
</table>
</div>

## Purchasing Analysis (Age)
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Average Purchase per person</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10-14</th>
      <td>28</td>
      <td>$2.96</td>
      <td>$82.78</td>
      <td>$3.76</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>136</td>
      <td>$3.04</td>
      <td>$412.89</td>
      <td>$3.86</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>365</td>
      <td>$3.05</td>
      <td>$1114.06</td>
      <td>$4.32</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>101</td>
      <td>$2.90</td>
      <td>$293.00</td>
      <td>$3.81</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>73</td>
      <td>$2.93</td>
      <td>$214.00</td>
      <td>$4.12</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>41</td>
      <td>$3.60</td>
      <td>$147.67</td>
      <td>$4.76</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>13</td>
      <td>$2.94</td>
      <td>$38.24</td>
      <td>$3.19</td>
    </tr>
    <tr>
      <th>&lt;10</th>
      <td>23</td>
      <td>$3.35</td>
      <td>$77.13</td>
      <td>$4.54</td>
    </tr>
  </tbody>
</table>
</div>

## Top Spenders
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lisosia93</th>
      <td>5</td>
      <td>$3.79</td>
      <td>$18.96</td>
    </tr>
    <tr>
      <th>Idastidru52</th>
      <td>4</td>
      <td>$3.86</td>
      <td>$15.45</td>
    </tr>
    <tr>
      <th>Chamjask73</th>
      <td>3</td>
      <td>$4.61</td>
      <td>$13.83</td>
    </tr>
    <tr>
      <th>Iral74</th>
      <td>4</td>
      <td>$3.40</td>
      <td>$13.62</td>
    </tr>
    <tr>
      <th>Iskadarya95</th>
      <td>3</td>
      <td>$4.37</td>
      <td>$13.10</td>
    </tr>
  </tbody>
</table>
</div>


Finally, the items themselves were grouped to identify the most popular and most profitable.

## Most Popular Items
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>178</th>
      <th>Oathbreaker, Last Hope of the Breaking Storm</th>
      <td>12</td>
      <td>$4.23</td>
      <td>$50.76</td>
    </tr>
    <tr>
      <th>145</th>
      <th>Fiery Glass Crusader</th>
      <td>9</td>
      <td>$4.58</td>
      <td>$41.22</td>
    </tr>
    <tr>
      <th>108</th>
      <th>Extraction, Quickblade Of Trembling Hands</th>
      <td>9</td>
      <td>$3.53</td>
      <td>$31.77</td>
    </tr>
    <tr>
      <th>82</th>
      <th>Nirvana</th>
      <td>9</td>
      <td>$4.90</td>
      <td>$44.10</td>
    </tr>
    <tr>
      <th>19</th>
      <th>Pursuit, Cudgel of Necromancy</th>
      <td>8</td>
      <td>$1.02</td>
      <td>$8.16</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>8</td>
      <td>$4.35</td>
      <td>$34.80</td>
    </tr>
    <tr>
      <th>75</th>
      <th>Brutality Ivory Warmace</th>
      <td>8</td>
      <td>$2.42</td>
      <td>$19.36</td>
    </tr>
    <tr>
      <th>72</th>
      <th>Winter's Bite</th>
      <td>8</td>
      <td>$3.77</td>
      <td>$30.16</td>
    </tr>
    <tr>
      <th>60</th>
      <th>Wolf</th>
      <td>8</td>
      <td>$3.54</td>
      <td>$28.32</td>
    </tr>
    <tr>
      <th>59</th>
      <th>Lightning, Etcher of the King</th>
      <td>8</td>
      <td>$4.23</td>
      <td>$33.84</td>
    </tr>
    <tr>
      <th>37</th>
      <th>Shadow Strike, Glory of Ending Hope</th>
      <td>8</td>
      <td>$3.16</td>
      <td>$25.28</td>
    </tr>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>8</td>
      <td>$2.22</td>
      <td>$17.76</td>
    </tr>
    <tr>
      <th>92</th>
      <th>Final Critic</th>
      <td>8</td>
      <td>$4.88</td>
      <td>$39.04</td>
    </tr>
    <tr>
      <th>53</th>
      <th>Vengeance Cleaver</th>
      <td>7</td>
      <td>$2.05</td>
      <td>$14.35</td>
    </tr>
    <tr>
      <th>110</th>
      <th>Suspension</th>
      <td>7</td>
      <td>$1.44</td>
      <td>$10.08</td>
    </tr>
    <tr>
      <th>7</th>
      <th>Thorn, Satchel of Dark Souls</th>
      <td>7</td>
      <td>$1.33</td>
      <td>$9.31</td>
    </tr>
    <tr>
      <th>71</th>
      <th>Demise</th>
      <td>7</td>
      <td>$1.61</td>
      <td>$11.27</td>
    </tr>
    <tr>
      <th>117</th>
      <th>Heartstriker, Legacy of the Light</th>
      <td>7</td>
      <td>$1.79</td>
      <td>$12.53</td>
    </tr>
    <tr>
      <th>159</th>
      <th>Oathbreaker, Spellblade of Trials</th>
      <td>7</td>
      <td>$3.08</td>
      <td>$21.56</td>
    </tr>
    <tr>
      <th>85</th>
      <th>Malificent Bag</th>
      <td>7</td>
      <td>$1.75</td>
      <td>$12.25</td>
    </tr>
    <tr>
      <th>164</th>
      <th>Exiled Doomblade</th>
      <td>7</td>
      <td>$1.63</td>
      <td>$11.41</td>
    </tr>
    <tr>
      <th>141</th>
      <th>Persuasion</th>
      <td>7</td>
      <td>$3.19</td>
      <td>$22.33</td>
    </tr>
    <tr>
      <th>78</th>
      <th>Glimmer, Ender of the Moon</th>
      <td>7</td>
      <td>$4.40</td>
      <td>$30.80</td>
    </tr>
    <tr>
      <th>102</th>
      <th>Avenger</th>
      <td>6</td>
      <td>$3.44</td>
      <td>$20.64</td>
    </tr>
    <tr>
      <th>129</th>
      <th>Fate, Vengeance of Eternal Justice</th>
      <td>6</td>
      <td>$1.54</td>
      <td>$9.24</td>
    </tr>
  </tbody>
</table>
</div>

## Most Profitable Items
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>178</th>
      <th>Oathbreaker, Last Hope of the Breaking Storm</th>
      <td>12</td>
      <td>$4.23</td>
      <td>$50.76</td>
    </tr>
    <tr>
      <th>82</th>
      <th>Nirvana</th>
      <td>9</td>
      <td>$4.90</td>
      <td>$44.10</td>
    </tr>
    <tr>
      <th>145</th>
      <th>Fiery Glass Crusader</th>
      <td>9</td>
      <td>$4.58</td>
      <td>$41.22</td>
    </tr>
    <tr>
      <th>92</th>
      <th>Final Critic</th>
      <td>8</td>
      <td>$4.88</td>
      <td>$39.04</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>8</td>
      <td>$4.35</td>
      <td>$34.80</td>
    </tr>
    <tr>
      <th>59</th>
      <th>Lightning, Etcher of the King</th>
      <td>8</td>
      <td>$4.23</td>
      <td>$33.84</td>
    </tr>
    <tr>
      <th>108</th>
      <th>Extraction, Quickblade Of Trembling Hands</th>
      <td>9</td>
      <td>$3.53</td>
      <td>$31.77</td>
    </tr>
    <tr>
      <th>78</th>
      <th>Glimmer, Ender of the Moon</th>
      <td>7</td>
      <td>$4.40</td>
      <td>$30.80</td>
    </tr>
    <tr>
      <th>72</th>
      <th>Winter's Bite</th>
      <td>8</td>
      <td>$3.77</td>
      <td>$30.16</td>
    </tr>
    <tr>
      <th>60</th>
      <th>Wolf</th>
      <td>8</td>
      <td>$3.54</td>
      <td>$28.32</td>
    </tr>
    <tr>
      <th>179</th>
      <th>Wolf, Promise of the Moonwalker</th>
      <td>6</td>
      <td>$4.48</td>
      <td>$26.88</td>
    </tr>
    <tr>
      <th>160</th>
      <th>Azurewrath</th>
      <td>6</td>
      <td>$4.40</td>
      <td>$26.40</td>
    </tr>
    <tr>
      <th>25</th>
      <th>Hero Cane</th>
      <td>6</td>
      <td>$4.35</td>
      <td>$26.10</td>
    </tr>
    <tr>
      <th>37</th>
      <th>Shadow Strike, Glory of Ending Hope</th>
      <td>8</td>
      <td>$3.16</td>
      <td>$25.28</td>
    </tr>
    <tr>
      <th>139</th>
      <th>Mercy, Katana of Dismay</th>
      <td>5</td>
      <td>$4.94</td>
      <td>$24.70</td>
    </tr>
    <tr>
      <th>128</th>
      <th>Blazeguard, Reach of Eternity</th>
      <td>5</td>
      <td>$4.91</td>
      <td>$24.55</td>
    </tr>
    <tr>
      <th>138</th>
      <th>Peacekeeper, Wit of Dark Magic</th>
      <td>5</td>
      <td>$4.74</td>
      <td>$23.70</td>
    </tr>
    <tr>
      <th>141</th>
      <th>Persuasion</th>
      <td>7</td>
      <td>$3.19</td>
      <td>$22.33</td>
    </tr>
    <tr>
      <th>87</th>
      <th>Deluge, Edge of the West</th>
      <td>5</td>
      <td>$4.43</td>
      <td>$22.15</td>
    </tr>
    <tr>
      <th>159</th>
      <th>Oathbreaker, Spellblade of Trials</th>
      <td>7</td>
      <td>$3.08</td>
      <td>$21.56</td>
    </tr>
    <tr>
      <th>136</th>
      <th>Ghastly Adamantite Protector</th>
      <td>6</td>
      <td>$3.58</td>
      <td>$21.48</td>
    </tr>
    <tr>
      <th>65</th>
      <th>Conqueror Adamantite Mace</th>
      <td>5</td>
      <td>$4.24</td>
      <td>$21.20</td>
    </tr>
    <tr>
      <th>101</th>
      <th>Final Critic</th>
      <td>5</td>
      <td>$4.19</td>
      <td>$20.95</td>
    </tr>
    <tr>
      <th>102</th>
      <th>Avenger</th>
      <td>6</td>
      <td>$3.44</td>
      <td>$20.64</td>
    </tr>
    <tr>
      <th>133</th>
      <th>Faith's Scimitar</th>
      <td>5</td>
      <td>$4.09</td>
      <td>$20.45</td>
    </tr>
  </tbody>
</table>
</div>

# Results of Analysis

This dataset was comprised of 780 purchases made by 576 unique players. Of the 576 players, 84% identified as male, 14% as female and 2% were other or non-disclosed. (Gender Demographics)

When reviewing purchases by gender it can be observed that while purchase counts were proportionate to the share of the population(84% male, 14% female and 2% other), females and non-disclosed players tended to purchase higher priced items and have a higher average purchase per player than the male players. (Purchasing Analysis(Gender))

The peak age demographic for Heroes of Pymoli is 15-29 with ages 20-24 representing approximately 45% of players and revenue and ages 15-29 representing approximately 75%. (Age Demographics and Purchasing Analysis)

A review of top spenders shows that no single player spent over $20 within this dataset. (Top Spenders)

# Conclusions

This analysis suggests that a key part of revenue generation is having a wide range of players and items available to purchase. This is because players are not found to spend a great deal of money individually. Recruitment of new players should be focused on males aged 15-29 but in a way designed not to exclude females from becoming interested. While males are more likely have a larger total purchase, females appear to be drawn to higher priced items which can drive profitability.

Below is a list of item IDs that intersected in the most profitable and most popular items, these items should be studied by the designers when creating new products.

(178, 145, 108, 82, 19, 103, 75, 72, 60, 59, 53, 117, 85, 102)


