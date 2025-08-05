from src.predict import predict_temperature

def main():
    print("Temperature Prediction CLI")
    print("Available models:")
    print("1. Linear Regression")
    print("2. Decision Tree")
    
    choice = input("\nSelect model (1 or 2): ")
    model_type = 'linear_regression' if choice == '1' else 'decision_tree'
    
    print("\nPlease enter the following weather features:\n")
    
    features = {
        'Apparent Temperature (C)': float(input("Apparent Temperature (C): ")),
        'Humidity': float(input("Humidity (0-1): ")),
        'Wind Speed (km/h)': float(input("Wind Speed (km/h): ")),
        'Visibility (km)': float(input("Visibility (km): ")),
        'Pressure (millibars)': float(input("Pressure (millibars): ")),
        'month': int(input("Month (1-12): "))
    }
    
    prediction = predict_temperature(features, model_type=model_type)
    print(f"\nPredicted Temperature ({model_type}): {prediction:.1f}°C")

if __name__ == "__main__":
    main()