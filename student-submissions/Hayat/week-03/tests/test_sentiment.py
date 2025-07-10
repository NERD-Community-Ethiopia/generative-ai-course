import pytest
from src.sentiment_analysis import load_data

def test_load_data():
    with open("test_data.csv", "w", encoding="utf-8") as f:
        f.write("text,sentiment\nTest text,positive")
    df = load_data("test_data.csv")
    assert not df.empty, "Dataset should not be empty"