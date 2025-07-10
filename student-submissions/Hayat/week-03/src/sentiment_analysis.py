"""Sentiment Analysis Model for Week 3 Assignment."""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import sys

def load_data(file_path: str) -> pd.DataFrame:
    """Load dataset from CSV file."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)

        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def train_and_predict(input_file: str, output_file: str) -> None:
    """Train model and save predictions."""
    data = load_data(input_file)
    if data.empty:
        print("No data loaded.")
        return

    texts = data["text"]
    labels = data["sentiment"]

    # Transform text to TF-IDF features
    vectorizer = TfidfVectorizer(max_features=1000)
    features = vectorizer.fit_transform(texts)

    # Train model
    model = LogisticRegression(max_iter=1000)
    model.fit(features, labels)

    # Predict
    predictions = model.predict(features)

    # Save results
    pd.DataFrame({"text": texts, "prediction": predictions}).to_csv(output_file, index=False)
    print(f"Predictions saved to {output_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python sentiment-analysis.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = "output/predictions.csv"
    train_and_predict(input_file, output_file)

if __name__ == "__main__":
    main()