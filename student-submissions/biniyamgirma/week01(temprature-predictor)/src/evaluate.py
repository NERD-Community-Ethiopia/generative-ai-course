import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split

def evaluate_model():
    # Load model and test data
    model = joblib.load("/mnt/hdd/bini/ai&robotics/generative-ai-course/student-submissions/biniyamgirma/week01(temprature-predictor)/models/linear_regression_model.pkl")
    df = pd.read_csv("/mnt/hdd/bini/ai&robotics/generative-ai-course/student-submissions/biniyamgirma/week01(temprature-predictor)/data/processed_temperatures.csv")
    
    X = df.drop('Temperature (C)', axis=1)
    y = df['Temperature (C)']
    
    _, X_test, _, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Create visualizations directory
    os.makedirs("/mnt/hdd/bini/ai&robotics/generative-ai-course/student-submissions/biniyamgirma/week01(temprature-predictor)/visuals", exist_ok=True)
    
    # Plot actual vs predicted
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=y_test, y=y_pred)
    plt.xlabel('Actual Temperature (C)')
    plt.ylabel('Predicted Temperature (C)')
    plt.title('Actual vs Predicted Temperatures')
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--')
    plt.savefig("/mnt/hdd/bini/ai&robotics/generative-ai-course/student-submissions/biniyamgirma/week01(temprature-predictor)/visuals/actual_vs_predicted.png")
    plt.close()
    
    # Plot residuals
    residuals = y_test - y_pred
    plt.figure(figsize=(10, 6))
    sns.histplot(residuals, kde=True)
    plt.xlabel('Residuals')
    plt.title('Distribution of Residuals')
    plt.savefig("/mnt/hdd/bini/ai&robotics/generative-ai-course/student-submissions/biniyamgirma/week01(temprature-predictor)/visuals/residuals_distribution.png")
    plt.close()
    
    print("Evaluation visualizations saved to ../visuals/")

if __name__ == "__main__":
    evaluate_model()