import joblib
import pandas as pd

def predict_temperature(features):
    """
    Predict temperature based on input features.
    
    Args:
        features (dict): Dictionary containing:
            - Apparent Temperature (C)
            - Humidity
            - Wind Speed (km/h)
            - Visibility (km)
            - Pressure (millibars)
            - month (1-12)
    
    Returns:
        float: Predicted temperature in Celsius
    """
    # Load model
    model = joblib.load("/mnt/hdd/bini/ai&robotics/generative-ai-course/student-submissions/biniyamgirma/week01(temprature-predictor)/models/linear_regression_model.pkl")
    
    # Convert features to DataFrame
    input_df = pd.DataFrame([features])
    
    # Make prediction
    prediction = model.predict(input_df)
    
    return prediction[0]

if __name__ == "__main__":
    # Example usage
    example_features = {
        'Apparent Temperature (C)': 10.5,
        'Humidity': 0.8,
        'Wind Speed (km/h)': 12,
        'Visibility (km)': 15,
        'Pressure (millibars)': 1012,
        'month': 6
    }
    
    pred_temp = predict_temperature(example_features)
    print(f"Predicted Temperature: {pred_temp:.1f}°C")