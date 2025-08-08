import joblib
import pandas as pd

def predict_temperature(features, model_type='linear_regression'):
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
        model_type (str): Type of model to use ('linear_regression' or 'decision_tree')
    
    Returns:
        float: Predicted temperature in Celsius
    """
    # Load model
    try:
        model = joblib.load(f"./models/{model_type}_model.pkl")
    except FileNotFoundError:
        raise ValueError(f"Model {model_type} not found. Available models: 'linear_regression', 'decision_tree'")
    
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
    
    # Predict with both models
    for model in ['linear_regression', 'decision_tree']:
        pred_temp = predict_temperature(example_features, model_type=model)
        print(f"Predicted Temperature ({model}): {pred_temp:.1f}°C")