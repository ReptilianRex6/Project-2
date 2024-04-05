# Actual model that recieves the data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt


def get_data():
    # Get the data
    data = pd.read_csv('resources\data.csv')
    return data

def preprocess_data(data):
    # Preprocess the data
    data = data.dropna()
    return data

def train_model(data):
    # Train the model
    X = data.drop('H', axis=1)
    y = data['H']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model = RandomForestRegressor(n_estimators=128, random_state=78)
    model.fit(X_train, y_train)
    gb_model = GradientBoostingRegressor(n_estimators=190, learning_rate=0.1, max_depth=8, random_state=42)
    gb_model.fit(X_train, y_train)
    return model, gb_model, X_test, y_test

def evaluate_model(model, data):
    # Evaluate the model
    X = data.drop('H', axis=1)
    y = data['H']
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    return mse

def main():
    # Main function
    data = get_data()
    data = preprocess_data(data)
    rf_model, gb_model, X_test, y_test = train_model(data)
    test_data = pd.concat([X_test, y_test], axis=1)
    rf_mse = evaluate_model(rf_model, test_data)
    gb_mse = evaluate_model(gb_model, test_data)
    rf_r2 = rf_model.score(X_test, y_test)
    gb_r2 = gb_model.score(X_test, y_test)
    print(f'Random Forest Mean Squared Error: {rf_mse:.2f}')
    print(f'Random Forest R^2: {rf_r2 * 100:.2f}%')
    print(f'Gradient Boost Mean Squared Error: {gb_mse:.2f}')
    print(f'Gradient Boost R^2: {gb_r2 * 100:.2f}%')

    # Additional code to evaluate the models on the test data
    rf_test_r2 = rf_model.score(test_data.drop('H', axis=1), test_data['H'])
    gb_test_r2 = gb_model.score(test_data.drop('H', axis=1), test_data['H'])
    print(f'Random Forest Test R^2: {rf_test_r2 * 100:.2f}%')
    print(f'Gradient Boost Test R^2: {gb_test_r2 * 100:.2f}%')

if __name__ == '__main__':
    main()


#Run kfold cross validation on the model to verify which model will perform best on unseen data to prevent overfitting
from sklearn.model_selection import KFold
import numpy as np

def kfold_cross_validation(data, model):
    X = data.drop('H', axis=1)
    y = data['H']
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    r2_scores = []
    for train_index, test_index in kf.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        model.fit(X_train, y_train)
        r2_scores.append(model.score(X_test, y_test))
    return np.mean(r2_scores)


data = pd.read_csv('resources\data.csv')

print('Random Forest Cross Validation R^2:', kfold_cross_validation(data, RandomForestRegressor(n_estimators=128, random_state=78)))
print('Gradient Boosting Cross Validation R^2:', kfold_cross_validation(data, GradientBoostingRegressor(n_estimators=190, learning_rate=0.1, max_depth=8, random_state=42)))
