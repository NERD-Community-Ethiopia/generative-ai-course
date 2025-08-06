
# ✅ MLOps Workshop Checklist: From Prompt to Production

This checklist guides you step-by-step to build a production-ready ML project from a simple prompt. Complete each task to track your progress.
Convert all this checklist into the prompts to inside your Agentic Development enviroment. Mkae sure to go step by step to learn the process and debug small chunks of changes. Good luck.

---

## 🧱 Phase 1: Project Setup

- [ ] Create project folder starter_mlops_project/
- [ ] Initialize Git repository
- [ ] Create and activate virtual environment
- [ ] Set up requirements.txt with essential libraries
- [ ] Install core packages: pandas, scikit-learn, fastapi, joblib, uvicorn
- [ ] Create base folder structure: src/, data/, models/, app/, notebooks/, config/
- [ ] Add .gitignore for Python and environment files
- [ ] Write basic README.md
- [ ] Add LICENSE (MIT or other)
- [ ] Create GitHub repo and push initial code

---

## 📊 Phase 2: Define the Problem - Pick any problem for can be solved using Machine learning. You can prompt the process of finding the problems as well.

- [ ] Write problem statement in README.md
- [ ] Define objective: Predict churn from account logs
- [ ] Describe expected model inputs and outputs
- [ ] Choose evaluation metrics (Accuracy, F1-score, etc.)
- [ ] Define success criteria for the model

---

## 📥 Phase 3: Data Collection & Loading

- [ ] Download or create churn dataset (e.g., from Kaggle)
- [ ] Save raw data under data/raw/
- [ ] Create src/data_loader.py
- [ ] Load data using pandas
- [ ] Inspect column types and missing values
- [ ] Check target class distribution
- [ ] Create notebooks/eda.ipynb for visualizations
- [ ] Generate basic data stats (mean, median, etc.)
- [ ] Visualize correlations
- [ ] Save cleaned data under data/processed/

---

## 🧹 Phase 4: Data Cleaning & Preprocessing

- [ ] Handle missing values
- [ ] Encode categorical features
- [ ] Normalize/standardize numerical features
- [ ] Drop irrelevant columns
- [ ] Create features/labels split
- [ ] Create src/preprocess.py with reusable functions
- [ ] Use train_test_split() to split data
- [ ] Save split datasets to disk
- [ ] Add logging to preprocessing steps
- [ ] Document pipeline steps in README.md

---

## 🧪 Phase 5: Model Training

- [ ] Create src/train.py
- [ ] Train a RandomForestClassifier
- [ ] Log training metrics (Accuracy, F1-score)
- [ ] Add CLI interface with argparse
- [ ] Save model to models/model.pkl
- [ ] Write training metrics to metrics.json
- [ ] Log training runtime
- [ ] Use config/train_config.yaml for hyperparameters
- [ ] Add cross-validation support
- [ ] Plot confusion matrix

---

## 🧠 Phase 6: Experiment Tracking

- [ ] Install and set up MLflow
- [ ] Log training runs and metadata
- [ ] Log hyperparameters and metrics
- [ ] Log artifacts (model, plots)
- [ ] Register trained model with MLflow
- [ ] Launch MLflow UI dashboard
- [ ] Create helper module mlflow_tracking.py
- [ ] Store experiment name/version
- [ ] Include plots in MLflow logs
- [ ] Integrate MLflow with training script

---

## 🚀 Phase 7: Model Serving with FastAPI

- [ ] Create app/main.py with FastAPI app
- [ ] Add /predict route
- [ ] Load model.pkl using joblib
- [ ] Accept and validate input using Pydantic schema
- [ ] Return prediction results as JSON
- [ ] Add /health endpoint for uptime checks
- [ ] Create reusable input schema in app/schemas.py
- [ ] Write sample input payload for testing
- [ ] Run API with uvicorn
- [ ] Test endpoint using curl or Postman

---

## 🐳 Phase 8: Containerization with Docker

- [ ] Write a Dockerfile
- [ ] Use minimal Python base image
- [ ] Install dependencies from requirements.txt
- [ ] Set FastAPI app as entrypoint
- [ ] Create .dockerignore file
- [ ] Build Docker image locally
- [ ] Tag the image appropriately
- [ ] Run container and test endpoint
- [ ] Test containerized app with Postman
- [ ] (Optional) Push image to DockerHub

---

## ⚙️ Phase 9: CI/CD with GitHub Actions

- [ ] Create .github/workflows/deploy.yml

Natnael Kebede, [7/31/2025 12:47 PM]
- [ ] Add install dependencies step
- [ ] Add Docker build job
- [ ] Add linting job (flake8 or black)
- [ ] Add test job (for /predict endpoint)
- [ ] Set trigger on main branch push
- [ ] Commit and test the CI pipeline
- [ ] Add build status badge to README.md
- [ ] Store secrets in GitHub Actions (if deploying)
- [ ] Document pipeline in project

---

## 📈 Phase 10: Monitoring & Logging

- [ ] Create src/monitor.py script
- [ ] Log each prediction request to a file
- [ ] Log prediction results and confidence
- [ ] Simulate drift using altered test data
- [ ] Generate accuracy drift report/alert

---

## 🧼 Phase 11: Refactoring & Cleanup

- [ ] Split code into proper src/ submodules
- [ ] Rename scripts to be consistent and clear
- [ ] Add type hints throughout the codebase
- [ ] Add meaningful docstrings to all functions
- [ ] Format code using black or ruff

---

## 📘 Phase 12: Final Docs & Wrap-Up

- [ ] Update README.md with usage instructions
- [ ] Add system architecture diagram or flowchart
- [ ] Write section for local setup and usage
- [ ] Write section for Docker deployment
- [ ] Create a Makefile or setup.sh to automate flow

---

You're done! 🎉 You now have a full ML project with MLOps practices from prompt to production.