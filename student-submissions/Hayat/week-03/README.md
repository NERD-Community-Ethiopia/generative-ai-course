# Week 3 Assignment: Simple Sentiment Analysis Model

## Description
This project implements a sentiment analysis model using a basic logistic regression classifier for the Week 3 assignment of the Generative AI Course.

## Installation
1. Clone the repository: `git clone https://github.com/Hayat373/generative-ai-course.git`
2. Navigate to the Week 3 directory: `cd student-submissions/Hayat/week-03`
3. Install dependencies: `pip install -r requirements.txt`

## Usage
Run the main script:
```bash
python src/sentiment-analysis.py
```
Output is saved in output/word_frequencies.txt 

## Dependencies

Python 3.8+
scikit-learn==1.0.2
pandas==1.4.3
numpy==1.22.4


## Output

The script generates a CSV file (output/predictions.csv) containing text samples and their predicted sentiments (positive or negative).

## Challenges

Handling imbalanced data: Used oversampling techniques to balance the dataset.

Model tuning: Adjusted hyperparameters to improve prediction accuracy.

## Learning Outcomes

Learned to implement logistic regression for sentiment analysis.



Gained experience with TF-IDF feature extraction and model evaluation.



Improved skills in structuring and documenting a Python project.
