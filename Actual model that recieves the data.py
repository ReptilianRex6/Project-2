# Actual model that recieves the data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from pybaseball import standings



def get_data():
    # Get the data from the API
    standings = standings()
    return standings

def preprocess_data(data):
    # Preprocess the data
    data = data.dropna()
    return data

def train_model(data):
    # Train the model
    X = data.drop('W', axis=1)
    y = data['W']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, data):
    # Evaluate the model
    X = data.drop('W', axis=1)
    y = data['W']
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    return mse

def main():
    # Main function
    data = get_data()
    data = preprocess_data(data)
    model = train_model(data)
    mse = evaluate_model(model, data)
    print(f'Mean Squared Error: {mse}')

if __name__ == '__main__':
    main()

