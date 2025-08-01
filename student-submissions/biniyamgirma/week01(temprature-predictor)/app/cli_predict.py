from src.predict import predict_temperature

def main():
    print("Temperature Prediction CLI")
    print("Please enter the following weather features:\n")
    
    features = {
        'Apparent Temperature (C)': float(input("Apparent Temperature (C): ")),
        'Humidity': float(input("Humidity (0-1): ")),
        'Wind Speed (km/h)': float(input("Wind Speed (km/h): ")),
        'Visibility (km)': float(input("Visibility (km): ")),
        'Pressure (millibars)': float(input("Pressure (millibars): ")),
        'month': int(input("Month (1-12): "))
    }
    
    prediction = predict_temperature(features)
    print(f"\nPredicted Temperature: {prediction:.1f}°C")

if __name__ == "__main__":
    main()