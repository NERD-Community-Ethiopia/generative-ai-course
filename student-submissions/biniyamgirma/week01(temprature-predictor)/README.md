# Week 01: Temperature Predictor

## 📚 Project Overview

This project implements a machine learning pipeline to predict temperature values based on historical weather data. It includes data preprocessing, exploratory data analysis, model training (Linear Regression & Decision Tree), evaluation, and a command-line prediction interface.

---

## 📁 Folder Structure

```
week01(temprature-predictor)/
├── README.md
├── requirements.txt
├── app/
│   └── cli_predict.py
├── data/
│   ├── processed_temperatures.csv
│   └── weatherHistory.csv
├── models/
│   ├── decision_tree_model.pkl
│   └── linear_regression_model.pkl
├── notebooks/
│   ├── eda.ipynb
│   └── model_training.ipynb
├── src/
│   ├── __init__.py
│   ├── evaluate.py
│   ├── predict.py
│   ├── preprocess.py
│   └── train.py
└── visuals/
    ├── actual_vs_predicted_decision_tree.png
    ├── actual_vs_predicted_linear_regression.png
    ├── actual_vs_predicted.png
    └── residuals_distribution.png
```

---

## 🛠️ Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone <repo-url>
   cd student-submissions/biniyamgirma/week01(temprature-predictor)
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

---

## 📂 File & Module Descriptions

### `app/cli_predict.py`
- Command-line interface for making temperature predictions using trained models.
- **Run:**  
  ```bash
  python -m app.cli_predict
  ```

### `data/`
- `weatherHistory.csv`: Raw historical weather data.
- `processed_temperatures.csv`: Cleaned and preprocessed data for modeling.

### `models/`
- `linear_regression_model.pkl`: Saved Linear Regression model.
- `decision_tree_model.pkl`: Saved Decision Tree model.

### `notebooks/`
- `eda.ipynb`: Exploratory Data Analysis notebook.
- `model_training.ipynb`: Model training and evaluation notebook.

### `src/`
- `preprocess.py`: Data cleaning and preprocessing functions.
- `train.py`: Model training scripts.
- `predict.py`: Prediction utilities for loading models and making predictions.
- `evaluate.py`: Model evaluation metrics and visualization.
- `__init__.py`: Package initialization.

### `visuals/`
- Plots and figures generated during analysis and evaluation:
  - `actual_vs_predicted_decision_tree.png`
  - `actual_vs_predicted_linear_regression.png`
  - `actual_vs_predicted.png`
  - `residuals_distribution.png`

---

## 🚀 How to Run Each Component

### 1. **Preprocess Data**
```bash
python src/preprocess.py
```
- Cleans and prepares raw data for modeling.

### 2. **Train Models**
```bash
python src/train.py
```
- Trains Linear Regression and Decision Tree models.
- Saves models to `models/` directory.

### 3. **Evaluate Models**
```bash
python src/evaluate.py
```
- Evaluates trained models and generates visualizations in `visuals/`.

### 4. **Make Predictions (Programmatically)**
```bash
python src/predict.py
```
- Loads trained models and makes predictions on new data.

### 5. **Command-Line Prediction**
```bash
python -m app.cli_predict
```
- Interactive CLI for temperature prediction.

### 6. **Jupyter Notebooks**
- For step-by-step analysis and experimentation:
  ```bash
  jupyter notebook notebooks/eda.ipynb
  jupyter notebook notebooks/model_training.ipynb
  ```

---

## 📊 Outputs

- **Model files:** Saved in `models/`
- **Processed data:** Saved in `data/`
- **Visualizations:** Saved in `visuals/`
- **Evaluation metrics:** Printed to console and/or saved as images

---

## 📝 Dependencies

See [`requirements.txt`](student-submissions/biniyamgirma/week01(temprature-predictor)/requirements.txt) for all required Python packages.

---

## 💡 Learning Outcomes

- Data preprocessing and cleaning
- Exploratory data analysis
- Regression model training and evaluation
- Model serialization and loading
- CLI application development
- Visualization of results

---

## ⚠️ Notes & Tips

- Always activate your virtual environment before running scripts.
- Ensure all dependencies are installed.
- For custom predictions, use the CLI or modify `src/predict.py`.
- Visualizations are auto-generated after evaluation.

---

## 🏆 Challenges Faced

- Handling missing and noisy data
- Model selection and hyperparameter tuning
- Visualizing prediction accuracy and residuals

---

## 📞 Support

For questions or issues, please contact the course instructors or open a GitHub issue.

---