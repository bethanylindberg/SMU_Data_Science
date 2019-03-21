# Pyweather Introduction

This project will show worldwide weather patterns visually based on geo coordinates. This category of data analysis in conjunction with other worldwide trends such as spending habits or crime rates may reveal many interesting and useful insights into the world we live in.

# Overview of the Data

Open weather map API was used to retrieve weather data for a list of 500+ cities. Information gathered included maximum temperature, humidity, cloudiness and wind speed. 

## Limitations of the Data

Several iterations of the calls resulted in extreme outliers which upon closer inspection were not correct at the time the call was made. For example, one instance listed Parrita, Costa Rica as having a wind speed of 122 mph when the actual wind speed at the time was 7 mph. This is most likely a glitch existing on the open weather app. The x and y limitations of the scatter plots were adjusted to compensate where necessary.

Because this analysis was done using city names and not coordinates there are large gaps in the data resulting from unpopulated areas not being included. This is most easily understood by viewing the gmap below.

# Methods

The Numpy random function was used to generate a list of coordinates which was run through the citypy library to find the nearest city.

A nested for loop was used to retrieve data from open weather map API and loaded into a pandas DataFrame, while the time module sleep function handled the run time to control for maximum allowable calls from the API.

After some minor formatting of the DataFrame, visualizations were created with matplotlib and gmaps was used to show the locations of the visualized cities.

# Analysis

For the purpose of this analysis, latitude will serve as the independent variable for several weather conditions. This will yield scatter plots that show visually how these weather conditions vary throughout Earth and reveal if there are any visible patterns.

## Latitude vs. Temperature
![latvtemp](Output/latvtemp.png)


## Latitude vs. Humidity
![latvhumd](Output/latvhumd.png)


## Latitude vs. Cloudiness
![latvcloud](Output/latvtemp.png)


## Latitude vs. Wind Speed
![latvwind](Output/latvtemp.png)


### Finally, the cities found through the API call visualized on a map

When charting the above scatter plots there is a noticeable absence of cities located south of Latitude -60 and north of Latitude 75. It is also possible to see gaps in the data; these gaps remain approximately the same with different samples of random coordinates run through the Open Weather Map API. Laying the coordinates over a world map shows why this phenomenon is observed.
![map](Output/map.png)


# Results of Analysis

Temperatures increase closer to the equator (0 latitude) with a sharp decline around 60 latitude and more disparate temperatures 40-60 latitude.

Cloudiness and humidity do not have any observable trends between different latitudes.

Wind speed also does not have a clear pattern based on latitude, though it appears that the highest speeds are the farthest south and farthest north. While this phenomenon is observed through several iterations, it is not necessarily experienced every time the data is pulled from the API.

