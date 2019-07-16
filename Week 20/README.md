# Introduction

The purpose of this report is to visualize historic rental bike data in New York City in order to search for trends that can lead to actionable insights. In a large city such as New York a diverse array of transportation options will always be necessary to serve the population and keep traffic congestion to a minimum. Bike rentals are one option of many and should be encouraged because of the availability of bike lanes and the benefit of being an environmentally friendly selection.

[The Tableau story can be viewed by clicking here](https://bethanylindberg.github.io/CitiBike/)

# Overview of the Data

The citibike data was downloaded from [citibikenyc.com](https://www.citibikenyc.com/system-data). For this analysis the time period chosen is January 2018 to June 2019. Parameters are listed below.

### Trip Data:

Tripduration: integer representing total length of trip in minutes

Starttime: Start of trip date and time e.g. 1/24/2018 7:31:33 PM

Stoptime: Stop of trip date and time e.g. Stoptime1/24/2018 7:41:08 PM

Start Station Id

Start Station Name

Start Station Latitude

Start Station Longitude

End Station Id

End Station Name

End Station Latitude

End Station Longitude

Bikeid

Usertype: User type for this trip (Customer or Subscriber)

Birth Year: User birth year if known

Gender: Integer code for gender

Date: Date of trip

Gender Text: Gender string

### Daily Ridership:

Date

Trips over the past 24-hours (midnight to 11:59pm)

Miles traveled today (midnight to 11:59 pm)

Total Annual Members (All Time)

New Members: Difference between prior day numbers and current entry

24-Hour Passes Purchased (midnight to 11:59 pm)

3-Day Passes Purchased (midnight to 11:59 pm)

Total Passes Purchased: Sum of 24-hour and 3-day passes purchase

### Weather:

Precipitation and temperature data was downloaded from [cnyweather.com](http://www.cnyweather.com/wxraindetail.php?year=2019). Parameters collected included daily accumulated precipitation in inches and daily high and low temperatures in Fahrenheit.

## Limitations of the Data

As shown in the below area graph, there is an unusual spike of birth years listed at 1969 and several records for every year between 1857 and 1939. These years were filtered out of the demographic analysis.

![ages](images/ages.PNG)

With the three above data sources joined in Tabluea, there is a total of 24,477,987 rows and 20 columns.

# Methods

The below aggregation was done in Jupyter Notebooks with Python and Pandas to estimate how many rides are taken for business purposes.

![dailyrides](images/dailyrides.PNG)

For explanatory analysis the below graphs were produced in Tableau.

## Demographics

![demographics](images/demographics.PNG)

## Peak

![Peak](images/Peak.PNG)

## Trends

![trends](images/trends.PNG)

Tableau was also used to produce two sets of maps.

## Static

Annotated map showing trips over the entire dataset
![Static](images/Static.PNG)

## Dynamic 

Map showing each day of data set

![dynamicmap](images/dynamicmap.gif)

# Results of Analysis

Demographic analysis revealed that most of the rides are taken by subscribers with less than 12% of total rides taken by an unsubscribed customer. Distribution of rides by gender and year reveals that there is a similar left skewed trend for both genders with peak birth years between 1980 and 1993. Reviewing trends by gender and age of number of rides and average trip duration shows that male users take more rides in every age group while females take longer trips at almost every birth year.

A review of trips when reviewed by time of day and week reveals that peak hours differ between weekend and weekdays. During weekdays, most trips are taken during morning and evening rush hours, while most trips are taken in the early afternoon on weekend. Overall,  more trips being taken during the weekdays than Saturday and Sunday. An analysis of peak months and dates shows that there are no outliers, all dates and months falling with a normal distribution and peak months being late Spring and early Summer while the months with the lowest number or records falling in the winter Months.

Examination of relationships between number or records and weather shows that changes in precipitation does not appear to have any association with changes in number of rides. Temperature does have a weak positive linear relationship with number of rides, but with an r2 of .54 is not a useful metric for predictive analytics.

The static map confirms what many would expect of the dataset with most trips being centered around Manhattan hot spots and the longest trips ending farther from the city center. Based on the analysis 3 of the 5 most popular Citibike  stations are near major transportations hubs:
-Grand Central (major train station)
-Union Square (major subway station where multiple lines
connect)
-Penn Station (major train station)

A review of the purchases and miles traveled over time shows a clear seasonality previously observed in the plot of peak dates. An overview shows up upward trend in number of bikes, total members and total stations and a downward trend in bikes per member.

# Conclusions

The recent downward trend in bikes available per member may result in insufficient supply during the busiest months of the year, and thus this report suggests a few proactive measures should be taken to avoid this. Bike fleet should be systematically taken out of service and all preventative maintenance done during the colder months and new bikes purchased periodically based on current fleet numbers.

Currently there is an opportunity to increase membership by recruiting more heavily among female residents and tourists. With a targeted marketing campaign and more features that would appeal to this demographic there is potential to tap into a new market segment and increase not only overall rides but also average trip duration.