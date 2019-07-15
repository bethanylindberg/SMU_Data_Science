# Exoplanet Exploration

![exoplanets.jpg](Images/exoplanets.jpg)

## Background

[Exoplanet Data Source](https://www.kaggle.com/nasa/kepler-exoplanet-search-results)

Over a period of nine years in deep space, the NASA Kepler space telescope has been out on a planet-hunting mission to discover hidden planets outside of our solar system. This project will examine the raw data and experiement with different machine learnign models to find the best predictors. The data was preprocessed, scaled and then classified by one of three labels: "Candidate", "Confirmed" and "False Positive."


## Methodology

The data was preprocessed by removing unnessecary columns and null rows, leaving a total of 8744 observations with which to create a machine learning model. The data was then scaled with MinMaxScaler and separated into training and testing data.

The first algorithm used was Support Vector Machine from the SKLearn python library. Grid search was then used to hypertune the C and gamma parameters to imrove predictions. The reports produced are below.

![SVM.PNG](Images/SVM.PNG) ![SVM2.PNG](Images/SVM2.PNG)


The Random Forest and Gradient Boosting algorithms were an improvement on the SVM model.

![RandomForest.PNG](Images/RandomForest.PNG) ![Boosting.PNG](Images/Boosting.PNG)


Two Further algorithms used for this dataset were Naive Bayes and K Neighbors though neither were found to have favorable results.

![NaiveBayes.PNG](Images/NaiveBayes.PNG) ![KNeighbors.PNG](Images/KNeighbors.PNG)


## Results



