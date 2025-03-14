# Final-Project-Statistical-Modelling-with-Python

## Project/Goals
The goal of this project is to analyze bike-sharing data in Luxembourg by integrating Points of Interest (POI) data from Foursquare and Yelp APIs. Using regression modeling, the project aims to uncover relationships between bike availability at stations and nearby POI characteristics, such as ratings and activity levels.
### Process
1.Data Collection:

Retrieved bike station data from the CityBikes API for Luxembourg.
Queried Foursquare and Yelp APIs to gather POI details (e.g., restaurants, bars, ratings, review counts) within 1000m of each station.
2.Data Integration:

Merged bike station data with POI data from both APIs.
Created an SQLite database to store and validate the datasets.
3.Exploratory Analysis:

Compare metrics such as business ratings and distances with station attributes.
Visualize trends and correlations using plots and charts.
4.Regression Modeling:

Perform regression analysis to model the relationship between independent variables (e.g., empty slots, free bikes, business distance) and the target variable (business rating).
Assess the performance of the model and evaluate how well the independent variables predict business ratings.

## Results
API Coverage:
Foursquare provided more POIs but lacked rich metadata like reviews and ratings compared to Yelp.
Regression Model:
POI Rating: Higher POI ratings are associated with more available bikes.
Review Count: Higher review counts (indicating busier locations) are associated with fewer available bikes.
Model Fit: The model explained 65% of the variation in bike availability (R-squared = 0.65).

## Challenges 

Limited API coverage in less busy areas reduced the richness of POI data for certain stations.
Inconsistent data formats between Foursquare and Yelp required significant cleaning and standardization.
Balancing API quotas and ensuring efficient queries was a constraint during data collection.
## Future Goals
(what would you do if you had more time?)
Incorporate real-time data on bike usage patterns to enhance the predictive power of the model.
Expand the analysis to include additional factors, such as weather conditions or time of day.
Use clustering techniques to group similar stations based on POI activity and bike availability.s
