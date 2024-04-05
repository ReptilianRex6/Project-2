from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from pybaseball import batting_stats

# Load in the data for each model
data = batting_stats(2014,2018)

def train_model(data, model):
    X = data[['Age', 'GB', 'LD', 'SwStr%']]
    y = data['H']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model.fit(X_train, y_train)
    return model, X_test, y_test

rf_model_instance, _, _ = train_model(data, RandomForestRegressor(n_estimators=128, random_state=78))
gb_model_instance, _, _ = train_model(data, GradientBoostingRegressor(n_estimators=190, learning_rate=0.1, max_depth=8, random_state=42))

# Get the data for the current year
data_current_year = batting_stats(2019)

# Select 5 random players
random_players = data_current_year['Name'].sample(5)

# Iterate over the selected players
for player in random_players:
    # Get the player's data
    player_data = data_current_year[data_current_year['Name'] == player]
    
    # Remove the 'Name' column
    player_data = player_data.drop('Name', axis=1)
    
    # Select only those columns from player_data
    player_data_rf = player_data[['Age', 'GB', 'LD', 'SwStr%']]

    # Run the data through the models
    rf_prediction = rf_model_instance.predict(player_data_rf)
    gb_prediction = gb_model_instance.predict(player_data_rf)

    # Print the results
    print(f"According to the Random Forest Model, {player} will have around {rf_prediction} hits in {data_current_year['Season'].values[0]}")
    print(f"According to the Gradient Boosting Model, he will have around {gb_prediction} hits in {data_current_year['Season'].values[0]}")
    print(f"Actual hits: {player_data['H'].values[0]}")
    print()