import pandas as pd
import numpy as np
from datetime import datetime

def preprocess_data(input_path, output_path):
    # Load data
    df = pd.read_csv(input_path)
    
    # Drop rows with missing values
    df = df.dropna()
    
    # Convert date and extract features
    df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
    df['month'] = df['Formatted Date'].dt.month
    
    # Select relevant features
    features = [
        'Apparent Temperature (C)', 
        'Humidity',
        'Wind Speed (km/h)',
        'Visibility (km)',
        'Pressure (millibars)',
        'month'
    ]
    
    target = 'Temperature (C)'
    
    # Create processed DataFrame
    processed_df = df[features + [target]].copy()
    
    # Save to CSV
    processed_df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")
    
    return processed_df

if __name__ == "__main__":
    preprocess_data(
        input_path="./data/weatherHistory.csv",
        output_path="./data/processed_temperatures.csv"
    )
