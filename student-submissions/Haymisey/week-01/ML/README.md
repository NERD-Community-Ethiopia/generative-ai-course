# Breast Cancer Diagnosis Classification - Complete MLOps Project

## 🎯 Project Overview

This project implements a complete MLOps pipeline for breast cancer diagnosis classification using the Wisconsin Breast Cancer Dataset. The system includes data processing, model training, API serving, containerization, monitoring, CI/CD automation, and **PDF report generation**.

## 📊 Problem Statement

**Objective**: Classify breast tumors as either **malignant** (cancerous) or **benign** (non-cancerous) using features derived from medical imaging.

**Dataset**: Wisconsin Breast Cancer Dataset (569 samples, 30 features)
**Model**: Support Vector Machine (SVM) with RBF kernel
**Performance**: 96.49% accuracy, 96.45% F1-score

## 🆕 New Features

### ✨ PDF Report Generation
- **Professional PDF reports** with prediction results, confidence scores, and contributing factors
- **Comprehensive analysis** including SHAP explanations and feature importance
- **Medical disclaimers** ensuring proper usage for educational purposes
- **Downloadable reports** with timestamped filenames
- **Patient name integration** with personalized report headers and filenames

### 🛡️ Enhanced Medical Disclaimers
- **Prominent UI warnings** with professional styling
- **Results disclaimer** shown after each prediction
- **PDF disclaimer** included in generated reports
- **Clear educational purpose** statements throughout the application

### 👤 Patient Management
- **Patient name input** with form validation
- **Personalized reports** with patient information headers
- **Custom filenames** including patient name and timestamp
- **Patient display** in results section
- **Professional medical interface** with patient tracking

### 🧠 Explainable AI (SHAP)
- **Top 5 contributing factors** for each prediction
- **Impact direction** (increases/decreases risk)
- **Confidence scores** with visual indicators
- **Real-time explanations** for transparency

## 🏗️ Project Architecture

```
starter_mlops_project/
├── src/                    # Core ML pipeline
│   ├── data_loader.py     # Data loading and inspection
│   ├── preprocess.py      # Data preprocessing pipeline
│   ├── train.py          # Model training and evaluation
│   ├── monitor.py        # Model monitoring and drift detection
│   └── mlflow_tracking.py # Experiment tracking
├── app/                   # FastAPI application
│   ├── main.py           # REST API endpoints + PDF generation
│   └── templates/        # Web interface
│       └── index.html    # Enhanced UI with disclaimers
├── data/                  # Data storage
│   ├── raw/              # Raw dataset
│   └── processed/        # Preprocessed data
├── models/               # Trained models and artifacts
├── config/               # Configuration files
│   └── train_config.yaml # Training configuration
├── logs/                 # Logs and monitoring data
├── tests/                # Unit tests
├── notebooks/            # Jupyter notebooks
├── docs/                 # Documentation
├── .github/workflows/    # CI/CD pipelines
├── Dockerfile            # Container configuration
├── Makefile              # Automation scripts
└── requirements.txt      # Dependencies (including PDF libraries)
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Docker (optional)
- Git

### 1. Clone and Setup

```bash
git clone <repository-url>
cd starter_mlops_project
make setup
make install
```

### 2. Run Complete Pipeline

```bash
# Run everything in one command
make all

# Or step by step:
make data      # Load and preprocess data
make train     # Train the model
make api       # Start the API server
```

### 3. Test the API

```bash
# Health check
curl http://localhost:8001/health

# Make a prediction
curl -X POST "http://localhost:8001/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "features": [17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189],
    "patient_name": "John Doe"
  }'

# Generate PDF report
curl -X POST "http://localhost:8001/generate-pdf" \
  -H "Content-Type: application/json" \
  -d '{
    "features": [17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189],
    "patient_name": "John Doe"
  }' \
  --output "John_Doe_breast_cancer_prediction_report.pdf"
```

## 🌐 Web Interface

Access the web interface at `http://localhost:8001` to:

- **Input medical features** through an intuitive form
- **View real-time predictions** with confidence scores
- **See SHAP explanations** for model transparency
- **Download PDF reports** with comprehensive analysis
- **Read medical disclaimers** ensuring proper usage

## 🔌 API Endpoints

### Core Endpoints

| Endpoint | Method | Description | Response |
|----------|--------|-------------|----------|
| `/` | GET | Web interface | HTML page |
| `/predict` | POST | Make prediction | JSON with results |
| `/generate-pdf` | POST | Generate PDF report | PDF file |

### Request/Response Examples

#### Prediction Endpoint
```bash
POST /predict
Content-Type: application/json

{
  "features": [17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]
}
```

**Response:**
```json
{
  "prediction": "malignant",
  "confidence": 0.9408151404435728,
  "probability_benign": 0.05918485955642709,
  "probability_malignant": 0.9408151404435728,
  "patient_name": "John Doe",
  "contributing_factors": [
    {
      "name": "Area Error",
      "impact": 0.08269006222270672,
      "direction": "decreases risk"
    },
    {
      "name": "Worst Radius",
      "impact": 0.08269006222270651,
      "direction": "increases risk"
    }
  ]
}
```

#### PDF Generation Endpoint
```bash
POST /generate-pdf
Content-Type: application/json

{
  "features": [17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]
}
```

**Response:** PDF file with comprehensive report including:
- Prediction results and confidence scores
- Top contributing factors with SHAP explanations
- Input features summary
- Medical disclaimers

## ⚠️ Medical Disclaimers & Safety

### Educational Purpose Only
This application is designed **exclusively for educational and research purposes**. It is **NOT a certified medical device** and should never be used for actual clinical diagnosis, patient treatment, or medical decision-making.

### Key Safety Features
- **Prominent disclaimers** displayed throughout the application
- **Results warnings** shown after each prediction
- **PDF disclaimers** included in generated reports
- **Clear educational purpose** statements
- **Professional medical advice** recommendations

### Important Notes
- **Always consult qualified healthcare professionals** for medical decisions
- **Predictions are based on machine learning algorithms** and may not be accurate
- **This tool is for demonstration purposes** only
- **No clinical validation** has been performed
- **Use at your own risk** for educational purposes only

## 📋 Available Commands

### Development Workflow

```bash
make help          # Show all available commands
make setup         # Create project structure
make install       # Install dependencies
make data          # Run data pipeline
make train         # Train model
make api           # Start API server
make dev           # Complete development setup
```

### Testing and Quality

```bash
make test          # Run unit tests
make lint          # Code linting
make format        # Code formatting
make type-check    # Type checking
make security      # Security checks
make check         # Run all quality checks
```

### Docker Operations

```bash
make docker-build  # Build Docker image
make docker-run    # Run Docker container
make prod          # Production workflow
```

### Monitoring and Maintenance

```bash
make monitor       # Run monitoring pipeline
make backup        # Backup models
make restore       # Restore models
make clean         # Clean generated files
make status        # Show project status
```

## 🔧 Detailed Usage

### Data Pipeline

The data pipeline consists of two main steps:

1. **Data Loading** (`src/data_loader.py`):
   - Loads Wisconsin Breast Cancer Dataset
   - Performs basic data inspection
   - Splits data into train/test sets
   - Saves raw and processed data

2. **Data Preprocessing** (`src/preprocess.py`):
   - Handles missing values
   - Scales features using StandardScaler
   - Encodes target variable
   - Performs feature selection
   - Saves preprocessing artifacts

```bash
# Run data pipeline
python src/data_loader.py
python src/preprocess.py
```

### Model Training

The training pipeline includes:

- Hyperparameter tuning with GridSearchCV
- Cross-validation
- Model evaluation with multiple metrics
- Confusion matrix visualization
- Model and metadata saving

```bash
# Train with default config
python src/train.py

# Train with custom config
python src/train.py --config config/train_config.yaml
```

### API Usage

The FastAPI application provides several endpoints:

- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /predict` - Single prediction
- `POST /batch-predict` - Batch predictions
- `GET /model-info` - Model information
- `GET /features` - Feature names
- `GET /docs` - Interactive API documentation

#### Example API Calls

```python
import requests

# Health check
response = requests.get("http://localhost:8000/health")
print(response.json())

# Single prediction
data = {
    "features": [17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]
}
response = requests.post("http://localhost:8000/predict", json=data)
print(response.json())
```

### Docker Deployment

```bash
# Build image
docker build -t breast-cancer-ml .

# Run container
docker run -p 8000:8000 breast-cancer-ml

# Test container
curl http://localhost:8000/health
```

### Monitoring

The monitoring system tracks:

- Prediction logs
- Data drift detection
- Model performance over time
- Automated alerts

```bash
# Run monitoring pipeline
python src/monitor.py

# View monitoring logs
ls logs/
```

## 📈 Model Performance

### Training Results

- **Accuracy**: 96.49%
- **F1-Score**: 96.45%
- **Precision**: 96.68%
- **Recall**: 96.49%
- **Cross-validation**: 95.82% ± 4.89%

### Best Hyperparameters

- **Kernel**: RBF
- **C**: 10
- **Gamma**: 0.1

## 🔄 CI/CD Pipeline

The GitHub Actions workflow includes:

1. **Testing**: Linting, type checking, unit tests
2. **Data Pipeline**: Data loading and preprocessing
3. **Model Training**: Training and evaluation
4. **API Testing**: Endpoint testing
5. **Docker Build**: Container creation and testing
6. **Deployment**: Production deployment (manual)

## 📊 Monitoring and Observability

### MLflow Integration

- Experiment tracking
- Model versioning
- Artifact logging
- Performance comparison

### Drift Detection

- Statistical drift detection
- Feature distribution monitoring
- Automated alerts
- Retraining recommendations

## 🛠️ Development

### Adding New Features

1. Create feature branch
2. Implement changes
3. Add tests
4. Run quality checks: `make check`
5. Submit pull request

### Code Quality

```bash
make format      # Format code
make lint        # Lint code
make type-check  # Type checking
make security    # Security analysis
make test        # Run tests
```

### Testing

```bash
# Run all tests
pytest tests/ -v

# Run specific test
pytest tests/test_api.py -v

# Run with coverage
pytest --cov=src tests/
```

## 🚀 Production Deployment

### Local Production

```bash
# Build and run with Docker
make docker-build
make docker-run
```

### Cloud Deployment

1. **AWS ECS**:
   ```bash
   docker tag breast-cancer-ml:latest your-account.dkr.ecr.region.amazonaws.com/breast-cancer-ml:latest
   docker push your-account.dkr.ecr.region.amazonaws.com/breast-cancer-ml:latest
   ```

2. **Google Cloud Run**:
   ```bash
   gcloud run deploy breast-cancer-ml --image gcr.io/your-project/breast-cancer-ml
   ```

3. **Azure Container Instances**:
   ```bash
   az container create --resource-group your-rg --name breast-cancer-ml --image your-registry.azurecr.io/breast-cancer-ml
   ```

## 📚 API Documentation

### Interactive Docs

Visit `http://localhost:8000/docs` for interactive API documentation.

### Endpoint Reference

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Root endpoint |
| `/health` | GET | Health check |
| `/predict` | POST | Single prediction |
| `/batch-predict` | POST | Batch predictions |
| `/model-info` | GET | Model information |
| `/features` | GET | Feature names |

### Request/Response Examples

#### Health Check
```bash
curl http://localhost:8000/health
```
```json
{
  "status": "healthy",
  "model_loaded": true,
  "timestamp": "2025-01-08T20:30:00"
}
```

#### Prediction
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"features": [17.99, 10.38, 122.8, ...]}'
```
```json
{
  "prediction": "malignant",
  "confidence": 0.95,
  "probabilities": {
    "benign": 0.05,
    "malignant": 0.95
  },
  "timestamp": "2025-01-08T20:30:00"
}
```

## 🔧 Configuration

### Training Configuration

Edit `config/train_config.yaml` to modify:

- Model hyperparameters
- Training parameters
- Evaluation metrics
- Feature selection settings

### Environment Variables

```bash
export MODEL_PATH=models/breast_cancer_model.pkl
export API_HOST=0.0.0.0
export API_PORT=8000
export LOG_LEVEL=INFO
```

## 🐛 Troubleshooting

### Common Issues

1. **Model not found**:
   ```bash
   make train  # Train the model first
   ```

2. **API not starting**:
   ```bash
   make install  # Install dependencies
   make data     # Ensure data is processed
   ```

3. **Docker build fails**:
   ```bash
   docker system prune  # Clean Docker cache
   make docker-build    # Rebuild
   ```

### Logs

Check logs in the `logs/` directory:

```bash
ls logs/
cat logs/training_metrics.json
cat logs/predictions_log.json
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Run quality checks: `make check`
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Wisconsin Breast Cancer Dataset (UCI Machine Learning Repository)
- Scikit-learn for ML algorithms
- FastAPI for API framework
- MLflow for experiment tracking

## 📞 Support

For questions or issues:

1. Check the [documentation](docs/)
2. Search existing [issues](../../issues)
3. Create a new issue with detailed information

---

**🎉 Congratulations!** You now have a complete MLOps pipeline from data to production deployment. 