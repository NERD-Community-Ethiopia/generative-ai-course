import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split

def evaluate_models():
    # Load data
    df = pd.read_csv("./data/processed_temperatures.csv")
    X = df.drop('Temperature (C)', axis=1)
    y = df['Temperature (C)']
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create visualizations directory
    os.makedirs("./visuals", exist_ok=True)
    
    # Evaluate each model
    for model_name in ['linear_regression', 'decision_tree']:
        try:
            model = joblib.load(f"./models/{model_name}_model.pkl")
            y_pred = model.predict(X_test)
            
            # Plot actual vs predicted
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=y_test, y=y_pred)
            plt.xlabel('Actual Temperature (C)')
            plt.ylabel('Predicted Temperature (C)')
            plt.title(f'Actual vs Predicted ({model_name.replace("_", " ").title()})')
            plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--')
            plt.savefig(f"./visuals/actual_vs_predicted_{model_name}.png")
            plt.close()
            
            print(f"Evaluation visualization saved for {model_name}")
            
        except FileNotFoundError:
            print(f"Model {model_name} not found, skipping evaluation")

if __name__ == "__main__":
    evaluate_models()