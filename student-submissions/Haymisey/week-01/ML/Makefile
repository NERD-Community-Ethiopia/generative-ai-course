# Makefile for Breast Cancer ML Project
# Automates the complete MLOps workflow

.PHONY: help setup install data train api docker-build docker-run test clean monitor

# Default target
help:
	@echo "Breast Cancer ML Project - MLOps Pipeline"
	@echo "=========================================="
	@echo ""
	@echo "Available commands:"
	@echo "  setup      - Initial project setup"
	@echo "  install    - Install dependencies"
	@echo "  data       - Run data pipeline (load + preprocess)"
	@echo "  train      - Train the model"
	@echo "  api        - Start the FastAPI server"
	@echo "  docker-build - Build Docker image"
	@echo "  docker-run - Run Docker container"
	@echo "  test       - Run tests"
	@echo "  monitor    - Run monitoring pipeline"
	@echo "  clean      - Clean up generated files"
	@echo "  all        - Run complete pipeline"

# Initial setup
setup:
	@echo "Setting up project structure..."
	mkdir -p data/raw data/processed models logs tests
	@echo "Project structure created!"

# Install dependencies
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt
	@echo "Dependencies installed!"

# Data pipeline
data:
	@echo "Running data pipeline..."
	python src/data_loader.py
	python src/preprocess.py
	@echo "Data pipeline completed!"

# Train model
train:
	@echo "Training model..."
	python src/train.py --config config/train_config.yaml
	@echo "Model training completed!"

# Start API server
api:
	@echo "Starting FastAPI server..."
	uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload

# Build Docker image
docker-build:
	@echo "Building Docker image..."
	docker build -t breast-cancer-ml .
	@echo "Docker image built!"

# Run Docker container
docker-run:
	@echo "Running Docker container..."
	docker run -p 8000:8000 breast-cancer-ml

# Run tests
test:
	@echo "Running tests..."
	pytest tests/ -v

# Run monitoring
monitor:
	@echo "Running monitoring pipeline..."
	python src/monitor.py
	@echo "Monitoring completed!"

# Clean up
clean:
	@echo "Cleaning up..."
	rm -rf __pycache__/
	rm -rf src/__pycache__/
	rm -rf app/__pycache__/
	rm -rf logs/*.png
	rm -rf logs/*.json
	rm -rf data/processed/*.csv
	rm -rf models/*.pkl
	@echo "Cleanup completed!"

# Run complete pipeline
all: setup install data train
	@echo "Complete pipeline finished!"

# Development workflow
dev: setup install data train api

# Production workflow
prod: setup install data train docker-build docker-run

# Quick test
quick-test:
	@echo "Running quick tests..."
	curl -f http://localhost:8001/health || echo "API not running"
	@echo "Quick test completed!"

# Format code
format:
	@echo "Formatting code..."
	black src/ app/
	@echo "Code formatted!"

# Lint code
lint:
	@echo "Linting code..."
	flake8 src/ app/ --count --select=E9,F63,F7,F82 --show-source --statistics
	@echo "Linting completed!"

# Type check
type-check:
	@echo "Running type checks..."
	mypy src/ app/
	@echo "Type checking completed!"

# Security check
security:
	@echo "Running security checks..."
	bandit -r src/ app/
	@echo "Security checks completed!"

# Generate documentation
docs:
	@echo "Generating documentation..."
	pdoc --html src/ --output-dir docs/
	@echo "Documentation generated!"

# Backup models
backup:
	@echo "Backing up models..."
	tar -czf models_backup_$(shell date +%Y%m%d_%H%M%S).tar.gz models/
	@echo "Models backed up!"

# Restore models
restore:
	@echo "Restoring models..."
	tar -xzf models_backup_*.tar.gz
	@echo "Models restored!"

# Performance test
perf-test:
	@echo "Running performance tests..."
	ab -n 100 -c 10 http://localhost:8001/health
	@echo "Performance test completed!"

# Load test
load-test:
	@echo "Running load tests..."
	python -c "
import requests
import time
import threading

def make_request():
    url = 'http://localhost:8001/predict'
    data = {'features': [17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]}
    response = requests.post(url, json=data)
    return response.status_code

start_time = time.time()
threads = []
for i in range(50):
    t = threading.Thread(target=make_request)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()
print(f'Load test completed in {end_time - start_time:.2f} seconds')
"
	@echo "Load test completed!"

# Health check
health:
	@echo "Checking system health..."
	@echo "Python version:"
	python --version
	@echo "Pip packages:"
	pip list
	@echo "Disk space:"
	df -h .
	@echo "Memory usage:"
	free -h
	@echo "Health check completed!"

# Update dependencies
update-deps:
	@echo "Updating dependencies..."
	pip install --upgrade -r requirements.txt
	@echo "Dependencies updated!"

# Create virtual environment
venv:
	@echo "Creating virtual environment..."
	python -m venv venv
	@echo "Virtual environment created!"
	@echo "Activate with: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate (Windows)"

# Install development dependencies
install-dev:
	@echo "Installing development dependencies..."
	pip install -r requirements.txt
	pip install black flake8 mypy bandit pytest
	@echo "Development dependencies installed!"

# Run all checks
check: lint type-check security test
	@echo "All checks completed!"

# Deploy to production
deploy:
	@echo "Deploying to production..."
	docker build -t breast-cancer-ml:latest .
	docker tag breast-cancer-ml:latest your-registry/breast-cancer-ml:latest
	docker push your-registry/breast-cancer-ml:latest
	@echo "Deployment completed!"

# Show project status
status:
	@echo "Project Status:"
	@echo "==============="
	@echo "Data files:"
	@ls -la data/processed/ 2>/dev/null || echo "No processed data found"
	@echo ""
	@echo "Models:"
	@ls -la models/ 2>/dev/null || echo "No models found"
	@echo ""
	@echo "Logs:"
	@ls -la logs/ 2>/dev/null || echo "No logs found"
	@echo ""
	@echo "Git status:"
	@git status --porcelain 2>/dev/null || echo "Not a git repository" 