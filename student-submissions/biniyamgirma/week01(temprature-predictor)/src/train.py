import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os

def train_model():
    # Load processed data
    df = pd.read_csv("./data/processed_temperatures.csv")
    
    # Split features and target
    X = df.drop('Temperature (C)', axis=1)
    y = df['Temperature (C)']
    
    # Split train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"MAE: {mae:.2f}")
    print(f"MSE: {mse:.2f}")
    print(f"R2 Score: {r2:.2f}")
    
    # Save model
    os.makedirs("../models", exist_ok=True)
    joblib.dump(model, "./models/linear_regression_model.pkl")
    print("Model saved to ./models/linear_regression_model.pkl")
    
    return model, X_test, y_test

if __name__ == "__main__":
    train_model()