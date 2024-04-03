# Actual model that recieves the data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


def get_data():
    # Get the data
    data = pd.read_csv('data.csv')
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
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, data):
    # Evaluate the model
    X = data.drop('H', axis=1)
    y = data['H']
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    # Visualize the predictions
    plt.scatter(y, y_pred)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.title('Model Predictions vs True Values')
    # plt.show()
    return mse

def main():
    # Main function
    data = get_data()
    data = preprocess_data(data)
    model = train_model(data)
    mse = evaluate_model(model, data)
    r2 = model.score(data.drop('H', axis=1), data['H'])
    print(f'Mean Squared Error: {mse:.2f}')
    print(f'R^2: {r2 * 100:.2f}%')


if __name__ == '__main__':
    main()
    model = train_model(get_data())  # Assign the trained model to the 'model' variable
    test_data = preprocess_data(get_data())
    test_r2 = model.score(test_data.drop('H', axis=1), test_data['H'])
    print(f'Test R^2: {test_r2 * 100:.2f}%')
