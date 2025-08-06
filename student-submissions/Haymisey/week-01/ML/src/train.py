"""
Model training module for the Wisconsin Breast Cancer Dataset.

This module handles model training, evaluation, and saving.
"""

import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score, GridSearchCV
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import json
import logging
import argparse
from pathlib import Path
import yaml
from datetime import datetime
from typing import Dict, Any, Tuple

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BreastCancerTrainer:
    """
    Model trainer class for the Wisconsin Breast Cancer Dataset.
    
    This class handles model training, hyperparameter tuning, and evaluation.
    """
    
    def __init__(self, config_path: str = None):
        """
        Initialize the trainer.
        
        Args:
            config_path (str): Path to configuration file
        """
        self.config = self.load_config(config_path)
        self.data_dir = Path("data")
        self.models_dir = Path("models")
        self.logs_dir = Path("logs")
        
        # Create directories if they don't exist
        self.models_dir.mkdir(parents=True, exist_ok=True)
        self.logs_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize model
        self.model = None
        self.best_model = None
        
        logger.info("Trainer initialized successfully")
    
    def load_config(self, config_path: str = None) -> Dict[str, Any]:
        """
        Load configuration from file or use defaults.
        
        Args:
            config_path (str): Path to configuration file
            
        Returns:
            dict: Configuration dictionary
        """
        if config_path and Path(config_path).exists():
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
            logger.info(f"Configuration loaded from {config_path}")
        else:
            # Default configuration
            config = {
                'model': {
                    'type': 'svm',
                    'kernel': 'rbf',
                    'C': 1.0,
                    'gamma': 'scale'
                },
                'training': {
                    'test_size': 0.2,
                    'random_state': 42,
                    'cv_folds': 5
                },
                'hyperparameter_tuning': {
                    'enable': True,
                    'param_grid': {
                        'C': [0.1, 1, 10, 100],
                        'gamma': ['scale', 'auto', 0.001, 0.01, 0.1],
                        'kernel': ['rbf', 'linear']
                    }
                },
                'evaluation': {
                    'metrics': ['accuracy', 'precision', 'recall', 'f1']
                }
            }
            logger.info("Using default configuration")
        
        return config
    
    def load_preprocessed_data(self) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """
        Load preprocessed training and testing data.
        
        Returns:
            tuple: (X_train, X_test, y_train, y_test)
        """
        logger.info("Loading preprocessed data...")
        
        # Load preprocessed data
        X_train = pd.read_csv(self.data_dir / "processed" / "X_train_preprocessed.csv")
        X_test = pd.read_csv(self.data_dir / "processed" / "X_test_preprocessed.csv")
        y_train = pd.read_csv(self.data_dir / "processed" / "y_train_encoded.csv").iloc[:, 0]
        y_test = pd.read_csv(self.data_dir / "processed" / "y_test_encoded.csv").iloc[:, 0]
        
        logger.info(f"Training set: {X_train.shape}")
        logger.info(f"Testing set: {X_test.shape}")
        
        return X_train, X_test, y_train, y_test
    
    def create_model(self) -> SVC:
        """
        Create and configure the SVM model.
        
        Returns:
            SVC: Configured SVM model
        """
        logger.info("Creating SVM model...")
        
        model_params = self.config['model']
        model = SVC(
            kernel=model_params['kernel'],
            C=model_params['C'],
            gamma=model_params['gamma'],
            random_state=self.config['training']['random_state'],
            probability=True
        )
        
        logger.info(f"Model created with parameters: {model_params}")
        return model
    
    def perform_hyperparameter_tuning(self, X_train: pd.DataFrame, y_train: pd.Series) -> SVC:
        """
        Perform hyperparameter tuning using GridSearchCV.
        
        Args:
            X_train (pd.DataFrame): Training features
            y_train (pd.Series): Training target
            
        Returns:
            SVC: Best model with tuned hyperparameters
        """
        logger.info("Performing hyperparameter tuning...")
        
        # Create base model
        base_model = SVC(random_state=self.config['training']['random_state'], probability=True)
        
        # Perform grid search
        grid_search = GridSearchCV(
            estimator=base_model,
            param_grid=self.config['hyperparameter_tuning']['param_grid'],
            cv=self.config['training']['cv_folds'],
            scoring='accuracy',
            n_jobs=-1,
            verbose=1
        )
        
        # Fit the grid search
        grid_search.fit(X_train, y_train)
        
        # Get best model
        best_model = grid_search.best_estimator_
        
        logger.info(f"Best parameters: {grid_search.best_params_}")
        logger.info(f"Best cross-validation score: {grid_search.best_score_:.4f}")
        
        return best_model
    
    def train_model(self, X_train: pd.DataFrame, y_train: pd.Series) -> SVC:
        """
        Train the model.
        
        Args:
            X_train (pd.DataFrame): Training features
            y_train (pd.Series): Training target
            
        Returns:
            SVC: Trained model
        """
        logger.info("Training model...")
        
        # Create model
        if self.config['hyperparameter_tuning']['enable']:
            self.model = self.perform_hyperparameter_tuning(X_train, y_train)
        else:
            self.model = self.create_model()
            self.model.fit(X_train, y_train)
        
        logger.info("Model training completed")
        return self.model
    
    def evaluate_model(self, model: SVC, X_test: pd.DataFrame, y_test: pd.Series) -> Dict[str, float]:
        """
        Evaluate the trained model.
        
        Args:
            model (SVC): Trained model
            X_test (pd.DataFrame): Testing features
            y_test (pd.Series): Testing target
            
        Returns:
            dict: Evaluation metrics
        """
        logger.info("Evaluating model...")
        
        # Make predictions
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)
        
        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)
        
        # Get detailed classification report
        report = classification_report(y_test, y_pred, output_dict=True)
        
        # Calculate additional metrics
        metrics = {
            'accuracy': accuracy,
            'precision': report['weighted avg']['precision'],
            'recall': report['weighted avg']['recall'],
            'f1_score': report['weighted avg']['f1-score'],
            'precision_benign': report['0']['precision'],
            'recall_benign': report['0']['recall'],
            'f1_benign': report['0']['f1-score'],
            'precision_malignant': report['1']['precision'],
            'recall_malignant': report['1']['recall'],
            'f1_malignant': report['1']['f1-score']
        }
        
        # Log metrics
        logger.info("Model Performance:")
        logger.info(f"Accuracy: {accuracy:.4f}")
        logger.info(f"Precision: {metrics['precision']:.4f}")
        logger.info(f"Recall: {metrics['recall']:.4f}")
        logger.info(f"F1-Score: {metrics['f1_score']:.4f}")
        
        # Create confusion matrix plot
        self.plot_confusion_matrix(y_test, y_pred)
        
        return metrics
    
    def plot_confusion_matrix(self, y_true: pd.Series, y_pred: np.ndarray) -> None:
        """
        Plot confusion matrix.
        
        Args:
            y_true (pd.Series): True labels
            y_pred (np.ndarray): Predicted labels
        """
        logger.info("Creating confusion matrix plot...")
        
        # Calculate confusion matrix
        cm = confusion_matrix(y_true, y_pred)
        
        # Create plot
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                    xticklabels=['Benign', 'Malignant'],
                    yticklabels=['Benign', 'Malignant'])
        plt.title('Confusion Matrix')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.tight_layout()
        
        # Save plot
        plot_path = self.logs_dir / "confusion_matrix.png"
        plt.savefig(plot_path, dpi=300, bbox_inches='tight')
        plt.close()  # Close the plot to avoid blocking
        
        logger.info(f"Confusion matrix saved to: {plot_path}")
    
    def perform_cross_validation(self, model: SVC, X_train: pd.DataFrame, y_train: pd.Series) -> Dict[str, float]:
        """
        Perform cross-validation.
        
        Args:
            model (SVC): Model to validate
            X_train (pd.DataFrame): Training features
            y_train (pd.Series): Training target
            
        Returns:
            dict: Cross-validation results
        """
        logger.info("Performing cross-validation...")
        
        # Perform cross-validation
        cv_scores = cross_val_score(
            model, X_train, y_train, 
            cv=self.config['training']['cv_folds'],
            scoring='accuracy'
        )
        
        cv_results = {
            'cv_scores': cv_scores.tolist(),
            'cv_mean': cv_scores.mean(),
            'cv_std': cv_scores.std(),
            'cv_min': cv_scores.min(),
            'cv_max': cv_scores.max()
        }
        
        logger.info(f"Cross-validation results:")
        logger.info(f"Mean: {cv_results['cv_mean']:.4f} (+/- {cv_results['cv_std'] * 2:.4f})")
        logger.info(f"Min: {cv_results['cv_min']:.4f}")
        logger.info(f"Max: {cv_results['cv_max']:.4f}")
        
        return cv_results
    
    def save_model(self, model: SVC, metrics: Dict[str, float], cv_results: Dict[str, float]) -> None:
        """
        Save the trained model and metadata.
        
        Args:
            model (SVC): Trained model
            metrics (dict): Evaluation metrics
            cv_results (dict): Cross-validation results
        """
        logger.info("Saving model and metadata...")
        
        # Save model
        model_path = self.models_dir / "breast_cancer_model.pkl"
        joblib.dump(model, model_path)
        
        # Save metrics
        metrics_path = self.logs_dir / "training_metrics.json"
        with open(metrics_path, 'w') as f:
            json.dump({
                'metrics': metrics,
                'cv_results': cv_results,
                'model_info': {
                    'model_type': 'SVM',
                    'kernel': model.kernel,
                    'C': model.C,
                    'gamma': model.gamma,
                    'training_date': datetime.now().isoformat()
                }
            }, f, indent=2)
        
        logger.info(f"Model saved to: {model_path}")
        logger.info(f"Metrics saved to: {metrics_path}")
    
    def run_training_pipeline(self) -> Dict[str, Any]:
        """
        Run the complete training pipeline.
        
        Returns:
            dict: Training results
        """
        logger.info("Starting training pipeline...")
        
        # Load data
        X_train, X_test, y_train, y_test = self.load_preprocessed_data()
        
        # Train model
        model = self.train_model(X_train, y_train)
        
        # Perform cross-validation
        cv_results = self.perform_cross_validation(model, X_train, y_train)
        
        # Evaluate model
        metrics = self.evaluate_model(model, X_test, y_test)

        logger.info("Saving SHAP background data...")
        background_data = X_train.sample(100, random_state=42)
        background_data.to_csv(self.models_dir / "shap_background.csv", index=False)
        logger.info(f"SHAP background data saved to: {self.models_dir / 'shap_background.csv'}")
        
        # Save model and results
        self.save_model(model, metrics, cv_results)
        
        logger.info("Training pipeline completed successfully!")
        
        return {
            'model': model,
            'metrics': metrics,
            'cv_results': cv_results,
            'data_shapes': {
                'X_train': X_train.shape,
                'X_test': X_test.shape,
                'y_train': y_train.shape,
                'y_test': y_test.shape
            }
        }


def main():
    """Main function to run the training pipeline."""
    parser = argparse.ArgumentParser(description='Train breast cancer classification model')
    parser.add_argument('--config', type=str, help='Path to configuration file')
    args = parser.parse_args()
    
    # Initialize trainer
    trainer = BreastCancerTrainer(config_path=args.config)
    
    # Run training pipeline
    results = trainer.run_training_pipeline()
    
    print("\n" + "="*50)
    print("TRAINING PIPELINE COMPLETED")
    print("="*50)
    print(f"Model trained successfully!")
    print(f"Accuracy: {results['metrics']['accuracy']:.4f}")
    print(f"F1-Score: {results['metrics']['f1_score']:.4f}")
    print(f"Cross-validation mean: {results['cv_results']['cv_mean']:.4f}")
    print("="*50)


if __name__ == "__main__":
    main() 