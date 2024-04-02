# Project-2

## Our Goal
Predicting the number of hits for baseball players in the next year.

## Data Sources
`getting_data.ipynb`  
The initial dataset was created using the pybaseball library and a function that calls `batting_stats`. This function, communicating with batting stats from FanGraphs, retrieved all players who had at least 50 Plate Appearances each year from 2014-2019. The dataset fetched 320 different parameters, creating our initial dataset `resources/full_batting_data.csv`.

`players_speed_2014-2019.ipynb`  
Since a player's speed is one of the factors influencing the achievement of hits (H), we utilized another function, `statcast_sprint_speed`, also part of the pybaseball library. This function communicates with [https://baseballsavant.mlb.com/](https://baseballsavant.mlb.com/), which uses advanced statcast technology for collecting game data. Here we fetched some parameters related to players' speed, resulting in data for each year from 2015 - 2019. (data for 2014 was not available)

`add_next_years_hits.ipynb`  
In this step, we defined our target column 'next_year_hits' and saved the dataset as `data2.csv`.

## Data Merging and Cleaning
`extended_dataset.ipynb`  
Next, we merged all data into one dataframe, removed unnecessary columns, and filled in missing data where necessary. We also excluded all rows related to the 2014 season and all players who appear only in one season. Finally, we removed all columns of dtype='object'. Once all columns were filled with appropriate data, we created a dataset ready for modeling: `resources/clean_extended_data.csv`.

## Data Modeling
`feature_selections.ipynb`  
Since initial modeling attempts showed that a large number of features caused data leakage, we proceeded with selecting features that could potentially give the best result. We selected ten features that do not contain the number of hits but have the highest feature importance in the RandomForestRegressor model and created a list of features.

`new_dataset3.ipynb`  
We combined the list created in the previous step with the dataset2 created earlier to obtain the final dataset `resources/data3.csv`.

`random_forest_extended_data.ipynb`  
Once all data were collected and prepared, we approached modeling again with the RandomForestRegressor model, and the results this time were better but still unsatisfactory.  
MSE: 92.94562673469386  
RMSE: 9.640831226335925  
R²: 0.9657437616910353

`baseball_project (1).ipynb`  
The next option was to see how our dataset would perform with the GradientBoostingRegressor model. We created a function that iteratively passes the model through our dataset with different parameters to establish which parameters provide the best results.

`gradient_boosting.ipynb`  
We included the best-performing parameters in our model, and these are the final results:  
MSE: 398.34215931956476  
MAE: 13.657809975591451  
R² Score: 0.8506441710830508
