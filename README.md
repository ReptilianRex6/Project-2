# Project-2: Baseball Hits Prediction

## Our Goal
Our primary objective is to predict the number of hits baseball players will achieve in the upcoming year, leveraging historical data and advanced statistical modeling techniques.

## How to Use This Project
This project is structured into two parts: `Data_prep` for future development, and `This Script outputs predicted hits for next year.py`

### Instructions for the Python file:
- On the main repo page, open the Python file `This Script outputs predicted hits for next year.py`

- The file loads and trains on data from given years
- You can leave as is unless there's a range of years you want to train on. In that case, fill in: ` data = batting_stats(years_go_here)`
  
![Screenshot 2024-04-03 230803](https://github.com/ReptilianRex6/Project-2/assets/149134955/0077bf11-6408-4138-8651-faf30b0dada7)
- Then, near the bottom, you can select what year to predict the hits for. Simply replace `(2019)` with the year you want.
  
![Screenshot 2024-04-03 225832](https://github.com/ReptilianRex6/Project-2/assets/149134955/ee9164c3-4fa8-4cf5-9105-806b8f6de1d2)



### Step-by-Step For future developments in `Data_prep`

#### Data Preparation (`Data_prep` folder)
1. **`getting_data.ipynb`**: Generates the initial dataset with 320 parameters for all players with at least 50 Plate Appearances annually from 2014-2019, using the `pybaseball` library to fetch batting stats from FanGraphs. Saves the dataset as `resources/full_batting_data.csv`.
2. **`players_speed_2014-2019.ipynb`**: Fetches players' speed parameters for 2015-2019 using `statcast_sprint_speed` from `pybaseball`, interacting with [Baseball Savant](https://baseballsavant.mlb.com/). (2014 data is unavailable.)
3. **`add_next_years_hits.ipynb`**: Defines the target column 'next_year_hits' for our prediction model and saves the enhanced dataset as `data2.csv`.

#### Data Merging and Cleaning
4. **`extended_dataset.ipynb`**: Merges all datasets into one, cleans, and preprocesses the data to prepare for modeling. The final cleaned dataset is saved as `resources/clean_extended_data.csv`.

### Data Modeling (`model_output` folder)
5. **`feature_selections.ipynb`**: Selects ten features that do not directly include the number of hits but are significant according to the feature importance in the RandomForestRegressor model. Creates a list of these features for modeling.
6. **`new_dataset3.ipynb`**: Combines the selected features list with `data2.csv` to form the final dataset for modeling, saved as `resources/data3.csv`.
7. **`random_forest_extended_data.ipynb`**: Applies the RandomForestRegressor model on the prepared dataset. Initial results showed room for improvement:  
   - MSE: 724.08
   - RMSE: 26.91
   - R²: 0.729

8. **`gradient_boosting.ipynb`**: Tests the dataset with a GradientBoostingRegressor model, tuning it to achieve the best performance. The final modeling results are:
   - MSE: 398.34
   - MAE: 13.66
   - R² Score: 0.851
   


### Instructions for Running the Notebooks
To achieve the best results, follow these steps in order:
1. Run all notebooks in the `Data_prep` folder sequentially (in the order described above Step-by-step) to generate and prepare the data set.
2. Proceed with the `model_output` folder's notebooks, starting with `feature_selections.ipynb` to determine the features to be used.
3. Use `new_dataset3.ipynb` to compile the final dataset with selected features.
4. Finally, run the modeling notebooks (`random_forest_extended_data.ipynb` and `gradient_boosting.ipynb`) to train and evaluate the models.


## Other Notebooks that explore model posibilities:
- XGBoost folder/ **`XGBoost.ipynb`**: Tests the dataset with the XGBoost, with hyperparameter tuning it to achieve the best performance. Final results are:
   - MSE: 400.07
   - MAE: 14.86
   - R² Score: 0.85

- Kfolds Folder:
   - Random Forest Cross Validation R^2: 0.8140286511015254
   - Gradient Boosting Cross Validation R^2: 0.775168644462665
 
- Data Prep And Model Evaluation.ipynb
   - Includes another Random Forest Evaluation
   - Has code from Matt Hergott that helped us shape the best model

## Conclusion
This project employs a data-driven approach to predict baseball players' performance in terms of hits. By meticulously preparing data, selecting relevant features, and modeling using advanced regressor algorithms, we've developed a predictive framework that can be further tuned and enhanced for better accuracy.

### Future Plans

As we move forward, the plan is to streamline and enhance the usability of this project by transforming the current Jupyter Notebooks into functions and consolidating them into a single `.python` file. This approach will not only make the process more organized but also significantly easier to use, enabling a more efficient workflow for predicting baseball players' performance in terms of hits. Through this evolution, we aim to provide a robust tool that encapsulates our comprehensive data preparation, feature selection, and modeling strategies in a cohesive and user-friendly framework.

### Data Provenance and Licensing

The data utilized in this project originates from reputable sources within the baseball analytics community, primarily through the utilization of the `pybaseball` library, which aggregates statistics from FanGraphs, and data concerning players' speed metrics sourced from [Baseball Savant](https://baseballsavant.mlb.com/) via its `statcast_sprint_speed` function. These platforms offer a wealth of detailed baseball statistics and leverage advanced technologies, such as Statcast, to provide insights into every aspect of the game.

#### Licensing and Usage Considerations
It's essential to acknowledge the licensing and usage policies of the data sources employed in this project:
- **FanGraphs** typically allows the use of its data for personal and research purposes, but it's crucial to consult their specific terms of use and citation guidelines when leveraging their data for public projects or publications.
- **Baseball Savant** and Statcast data are made available by Major League Baseball (MLB) and should be used in compliance with their guidelines. While the data is accessible for analysis and fan engagement, users should ensure that their use cases align with MLB's policies, especially regarding commercial use or redistribution.

#### Ethical Use of Data
When working with externally sourced data, especially that which is made publicly available by organizations like MLB, it's vital to use the data ethically and responsibly, crediting the sources appropriately and adhering to any specified restrictions. Transparency about data provenance, along with respect for the data's origin and intended use, underpins ethical research and analytics practices.

#### Future Considerations
As this project evolves and potentially incorporates more diverse data sources or seeks broader dissemination of its findings, we will rigorously review and adhere to the licensing agreements and ethical considerations surrounding the data we use. This commitment ensures that our work remains respectful of the creators and providers of the data that enrich our analysis and the broader baseball analytics community.

