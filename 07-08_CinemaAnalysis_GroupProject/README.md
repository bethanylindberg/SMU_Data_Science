# Have Streaming Services Killed Cinema?

## Introduction

Every month there seem to be less movies showing in theatres that are worth the time and effort to view. Genres have shifted to popcorn flicks and overall quality has declined (based on viewer ratings).This project is interested in the changes in aggregate quality of movies available across all platforms and if it is declining like expected, what is influencing the decline. Of particular interest is the rise in streaming services like Netflix and Hulu.

## Description of Data

The bulk of the data used for this project was retrieved from the OMDB API through a series of calls.
http://www.omdbapi.com/

The imdb titles in the first call was taken from a list of movies posted on kaggle.com and formatted before being placed in a list and called with a for loop that built a dataframe from the data retreived from the API. After closer examination of the dataset it was it was decided that the data still desired included details on tv series and movies from the year 2018 as the kaggle csv included neither. These titles were downloaded from imdb as a tab separated and gzipped file.(tsv.gz) The gzip and shutil libraries were used to unzip the files and save as csv files so they could be read into the notebook as a dataframe. The imdb file with IDs and votes was combined to complete the list for the second and third API calls.

The OMDB data was cleaned by correcting the formats of both the rotten tomatoes and imdb ratings so they were consistent for easy comparison.

Because most movies had multiple genres stored as a comma seperated string, some work needed to be done to narrow down what was included for analysis purposes. Each row was first split and expanded to have each genre on its own column and run through a loop to collect a list of unique genres. The resulting list of genres was narrowed from 23 to 7 to make a succinct analysis possible.

In addition to the above data, aggregated data was retrieved from several sources to aid in answering additional questions that arose during the course of analysis.

For revenue analysis:

Box Office Revenue Source: https://www.the-numbers.com/market/

US Population Source: https://www.multpl.com/united-states-population/table/by-year

For accurate movie releases (North America):

https://www.statista.com/statistics/187122/movie-releases-in-north-america-since-2001/

Alternative Genre Share (for illustrative purposes only): https://www.the-numbers.com/market/genres

Number of original scripted TV series in the United States from 2009 to 2018
https://www.statista.com/statistics/444870/scripted-primetime-tv-series-number-usa/



See applicable data dictionary for more information on the datasets. (located in cleaned data folder)

### Limitations of the data

Initially, there was difficulty gathering information.  Most sites required a fee to access data or limited how much data that could be accessed for free, thus restricting our options for data sources.

We discussed how to best analyze movie genres when a single movie could be categorized as 10 different genres.  We went with a method that would counts movies with multiple genres more than once which does have a possibility to skew the data but provides some insight on trends.

The OMDB dataset presented several challenges. The rotten tomatoes ratings were received in an inconsistent format and required a unique solution though in the end it was clean and usable. The Metacritic ratings and box office series were both missing enough values that they were was not usable for analysis.

If starting this project again, it is likely that collection of data would have been approached differently. By starting with a pre-curated list from kaggle instead of going straight to the imdb text files the list of movies was not as pure as it could have been. 

With more time we could have taken a similar approach to the production houses that we took with the genres and reviewed trends by producer. Additionally, with a dataset that included information such as budget and box office it would be possible to determine which genres and even plot points are most profitable.

        
## Analysis/Methodology

### Have ratings changed over time?

To answer the first question the data was grouped by year and plotted against the mean imdb ratings. The vertical lines represent the approximate years that Netflix began to offer streaming and released their first original series.

![ratingsovertime](Output/ratingsovertime.png)


Ratings were further broken out to determine if any trends could be observed. This was achieved by grouping the cleaned genre data by genre and year and plotting against mean imdb ratings after some minor data munging using unstack and list comprehension to rename the columns

![genreratingsovertime](Output/genreratingsovertime.png)

To confirm if there were any large changes in genre ratings, the percentage change between 2000 and 2018 was calculated and visualized with a bar graph.

![genreratingchangebar](Output/genreratingchangebar.png)

To visualize the relationship between several relationships at once (user ratings, critic ratings and genres). The below bubblee graph was created by grouping the data by year and plotting the mean imdb Ratings on the x axis and rotten tomatoes ratings on the y axis.

![ratingbubble](Output/ratingbubble.png)


### Has movie and TV production changed over the same time period?

TV series data was next grouped by year and year and tv count plotted to show change over time.

![tvproducedovertime](Output/tvproducedovertime.png)

Because of the limitations in the OMDB dataset and to ensure accuracy, an pre-aggregated statistic was used to show the Movie releases over the same period.

![moviesproducedovertime](Output/moviesproducedovertime.png)

The genre dataset was grouped by genre and year and divided by total per year to produce a change overtime.

![genresharesovertime](Output/genresharesovertime.png)

The percentage change was visualized in a bar graph to check for noticeable shifts.

![genrechangebar](Output/genrechangebar.png)

### What is the trend for box office revenue over the same time period?

Box office revenue can easily be visualized by plotting figures adjusted for inflation with years to produce the below line graph.

![boxofficeovertime](Output/boxofficeovertime.png)

To check that the line was not unduly affected by change in population, the below line graph was produced that shows the average tickets purchased per person in the US based on the tickets sold per year and the US population.

![ticketssoldovertime](Output/ticketssoldovertime.png)

## Results of Analysis

Although a drop in movie ratings and a rapid growth of online streaming  services such as Netflix in the last decade can be observed, there is not enough evidence to conclude that the growth of streaming service alone is the reason for this decline as there is likely to be a large number of confounding variables. 

We observed that movies ratings have been steadily declining since 2007 while TV series ratings have been consistently increasing over the same period. We further observed that users and critics tend to agree on the quality of movies.

We also noted that the average number of movie tickets sold per person and annual box office revenue have been decreasing since 2003 with a small rebound since 2011.

Finally, we observed the shift in genres popularity over the last 20 years. We noted large increase in Action, Adventure and horror movies produced and large decrease in Dramas and Comedies. Ratings for within the distinct genres remained relatively steady.


## Conclusions

We expected to find a clear decline in movie quality and a correlation between the decline and the rise of other entertainment sources such as Netflix.  However, this is not what we found. Although we saw a drop in movie ratings and a rapid growth of online streaming  services such as Netflix in the last decade, there was not enough evidence to conclude that the growth of streaming service is the reason for this decline.

We observed the shift in genres popularity over the last 20 years. We noted large increase in Action and Adventure movies produced and large decrease in Dramas and Comedies. We concluded that the shift in genres popularity may be the reason for perceived drop in quality of movies.



```python

```
