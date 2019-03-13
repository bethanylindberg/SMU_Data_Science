# Pyber Introduction

Pyber is in an exciting phase of seeking new opportunities. This report is intented to leverage historical data to aid in upcoming decisions.

# Overview of the Data

The dataset analyzed for this consists of  2,375 ride logs and a collection of city data where Pyber currently operates. Parameters include but are not limited to, driver count per city, city type and fare amounts.

# Methods

The Pandas library was used to merge, parse and aggregate the data and visualizations were created with the matplotlib library.

# Analysis

A bubble plot was created to show the relationship between the following four variables: average fare per city, total rides per city, total drivers in each city and city types. This was achieved by grouping by city and filtering by city type and setting the size by the driver count. Driver counts were pulled from the city data before it was combined to avoid counting drivers more than once.

[image]: ./Output/ridesharing.png "Ride Sharing Data (2016)"

Bar charts were then created to show the share per city type of total fares, revenue from fares and number of drivers

[image]: ./Output/faresbytype.png "Ride Sharing Data (2016)"
[image]: ./Output/ridesbytype.png "Ride Sharing Data (2016)"
[image]: ./Output/driversbytype.png "Ride Sharing Data (2016)"

# Results of Analysis

The analysis of this dataset shows that urban cities are the main driver of revenue, representing 68% of revenue and 63% of fares. Additionally, urban areas have 80% of Pyber drivers for the analyzed period, outpacing both of the other ratios.

The bubble plot shows that rural areas are producing higher on average fares, the cause of which could be that drivers are typically taking longer trips when in those areas. The average fare for rural, suburban and urban areas is $35, $31 and $25 respectively.

There is a negative relationship between number of rides per city and average fare, this is seen across all city types but more defined in suburban and urban areas.

# Conclusions

This analysis suggests that Pyber should focus on expanding into urban and suburban areas over rural for the best chance of increasing revenue. Further study should be conducted to determine the optimum driver count per citizin in cities to prevent oversupply and driving down prices.
__________

# Pymaceutical Introduction

# Overview of the Data

# Methods

# Analysis

# Results of Analysis

# Conclusions