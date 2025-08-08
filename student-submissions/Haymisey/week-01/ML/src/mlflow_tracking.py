"""
MLflow tracking module for the Wisconsin Breast Cancer Dataset.

This module handles experiment tracking, model logging, and artifact management.
"""

import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from pathlib import Path
import json
from datetime import datetime
from typing import Dict, Any, Tuple

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MLflowTracker:
    """
    MLflow tracking class for experiment management.
    
    This class handles experiment tracking, model logging, and artifact management.
    """
    
    def __init__(self, experiment_name: str = "breast_cancer_classification"):
        """
        Initialize the MLflow tracker.
        
        Args:
            experiment_name (str): Name of the MLflow experiment
        """
        self.experiment_name = experiment_name
        self.mlflow_dir = Path("mlruns")
        self.mlflow_dir.mkdir(exist_ok=True)
        
        # Set MLflow tracking URI
        mlflow.set_tracking_uri(str(self.mlflow_dir))
        
        # Set experiment
        mlflow.set_experiment(experiment_name)
        
        logger.info(f"MLflow tracker initialized for experiment: {experiment_name}")
    
    def log_parameters(self, params: Dict[str, Any]) -> None:
        """
        Log hyperparameters to MLflow.
        
        Args:
            params (dict): Parameters to log
        """
        logger.info("Logging parameters to MLflow...")
        mlflow.log_params(params)
        logger.info(f"Logged {len(params)} parameters")
    
    def log_metrics(self, metrics: Dict[str, float]) -> None:
        """
        Log metrics to MLflow.
        
        Args:
            metrics (dict): Metrics to log
        """
        logger.info("Logging metrics to MLflow...")
        mlflow.log_metrics(metrics)
        logger.info(f"Logged {len(metrics)} metrics")
    
    def log_model(self, model: SVC, model_name: str = "breast_cancer_svm") -> None:
        """
        Log model to MLflow.
        
        Args:
            model (SVC): Trained model
            model_name (str): Name for the model
        """
        logger.info("Logging model to MLflow...")
        mlflow.sklearn.log_model(model, model_name)
        logger.info(f"Model logged as: {model_name}")
    
    def log_artifacts(self, artifact_paths: Dict[str, str]) -> None:
        """
        Log artifacts to MLflow.
        
        Args:
            artifact_paths (dict): Dictionary of artifact names and paths
        """
        logger.info("Logging artifacts to MLflow...")
        for artifact_name, artifact_path in artifact_paths.items():
            if Path(artifact_path).exists():
                mlflow.log_artifact(artifact_path, artifact_name)
                logger.info(f"Logged artifact: {artifact_name}")
            else:
                logger.warning(f"Artifact not found: {artifact_path}")
    
    def create_confusion_matrix_plot(self, y_true: pd.Series, y_pred: np.ndarray, 
                                   save_path: str = "logs/confusion_matrix.png") -> str:
        """
        Create and save confusion matrix plot.
        
        Args:
            y_true (pd.Series): True labels
            y_pred (np.ndarray): Predicted labels
            save_path (str): Path to save the plot
            
        Returns:
            str: Path to saved plot
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
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Confusion matrix saved to: {save_path}")
        return save_path
    
    def create_feature_importance_plot(self, feature_names: list, importance_scores: list,
                                     save_path: str = "logs/feature_importance.png") -> str:
        """
        Create and save feature importance plot.
        
        Args:
            feature_names (list): List of feature names
            importance_scores (list): List of importance scores
            save_path (str): Path to save the plot
            
        Returns:
            str: Path to saved plot
        """
        logger.info("Creating feature importance plot...")
        
        # Create DataFrame
        importance_df = pd.DataFrame({
            'feature': feature_names,
            'importance': importance_scores
        }).sort_values('importance', ascending=True)
        
        # Create plot
        plt.figure(figsize=(10, 8))
        plt.barh(range(len(importance_df)), importance_df['importance'])
        plt.yticks(range(len(importance_df)), importance_df['feature'])
        plt.xlabel('Importance Score')
        plt.title('Feature Importance')
        plt.tight_layout()
        
        # Save plot
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Feature importance plot saved to: {save_path}")
        return save_path
    
    def log_experiment_run(self, model: SVC, X_train: pd.DataFrame, X_test: pd.DataFrame,
                          y_train: pd.Series, y_test: pd.Series, 
                          params: Dict[str, Any], metrics: Dict[str, float],
                          cv_results: Dict[str, float] = None) -> str:
        """
        Log a complete experiment run to MLflow.
        
        Args:
            model (SVC): Trained model
            X_train (pd.DataFrame): Training features
            X_test (pd.DataFrame): Testing features
            y_train (pd.Series): Training target
            y_test (pd.Series): Testing target
            params (dict): Model parameters
            metrics (dict): Evaluation metrics
            cv_results (dict): Cross-validation results
            
        Returns:
            str: Run ID
        """
        logger.info("Starting MLflow experiment run...")
        
        with mlflow.start_run():
            # Log parameters
            self.log_parameters(params)
            
            # Log metrics
            self.log_metrics(metrics)
            
            # Log cross-validation results if available
            if cv_results:
                cv_metrics = {
                    'cv_mean': cv_results['cv_mean'],
                    'cv_std': cv_results['cv_std'],
                    'cv_min': cv_results['cv_min'],
                    'cv_max': cv_results['cv_max']
                }
                self.log_metrics(cv_metrics)
            
            # Log model
            self.log_model(model)
            
            # Create and log plots
            y_pred = model.predict(X_test)
            
            # Confusion matrix
            cm_path = self.create_confusion_matrix_plot(y_test, y_pred)
            
            # Feature importance (if available)
            if hasattr(model, 'feature_importances_'):
                fi_path = self.create_feature_importance_plot(
                    X_train.columns, model.feature_importances_
                )
                artifacts = {
                    'confusion_matrix': cm_path,
                    'feature_importance': fi_path
                }
            else:
                artifacts = {'confusion_matrix': cm_path}
            
            # Log artifacts
            self.log_artifacts(artifacts)
            
            # Log dataset info
            dataset_info = {
                'X_train_shape': X_train.shape,
                'X_test_shape': X_test.shape,
                'y_train_shape': y_train.shape,
                'y_test_shape': y_test.shape,
                'n_features': X_train.shape[1]
            }
            mlflow.log_params(dataset_info)
            
            # Get run ID
            run_id = mlflow.active_run().info.run_id
            logger.info(f"Experiment run completed. Run ID: {run_id}")
            
            return run_id
    
    def register_model(self, model_name: str = "breast_cancer_svm", 
                      model_version: str = "1.0.0") -> None:
        """
        Register the model in MLflow model registry.
        
        Args:
            model_name (str): Name for the registered model
            model_version (str): Version of the model
        """
        logger.info("Registering model in MLflow model registry...")
        
        try:
            # Register model
            mlflow.sklearn.log_model(
                model, 
                model_name,
                registered_model_name=f"{model_name}_v{model_version}"
            )
            logger.info(f"Model registered as: {model_name}_v{model_version}")
        except Exception as e:
            logger.warning(f"Could not register model: {e}")
    
    def get_experiment_runs(self, experiment_name: str = None) -> pd.DataFrame:
        """
        Get all runs for an experiment.
        
        Args:
            experiment_name (str): Name of the experiment
            
        Returns:
            pd.DataFrame: DataFrame with run information
        """
        if experiment_name is None:
            experiment_name = self.experiment_name
        
        logger.info(f"Retrieving runs for experiment: {experiment_name}")
        
        # Get experiment
        experiment = mlflow.get_experiment_by_name(experiment_name)
        if experiment is None:
            logger.warning(f"Experiment not found: {experiment_name}")
            return pd.DataFrame()
        
        # Get runs
        runs = mlflow.search_runs(experiment_ids=[experiment.experiment_id])
        
        logger.info(f"Found {len(runs)} runs")
        return runs
    
    def compare_runs(self, run_ids: list) -> pd.DataFrame:
        """
        Compare multiple runs.
        
        Args:
            run_ids (list): List of run IDs to compare
            
        Returns:
            pd.DataFrame: Comparison DataFrame
        """
        logger.info(f"Comparing {len(run_ids)} runs...")
        
        comparison_data = []
        
        for run_id in run_ids:
            run = mlflow.get_run(run_id)
            run_data = {
                'run_id': run_id,
                'start_time': run.info.start_time,
                'end_time': run.info.end_time,
                'status': run.info.status,
                **run.data.params,
                **run.data.metrics
            }
            comparison_data.append(run_data)
        
        comparison_df = pd.DataFrame(comparison_data)
        logger.info(f"Comparison completed for {len(comparison_df)} runs")
        
        return comparison_df


def main():
    """Main function to demonstrate MLflow tracking."""
    # Initialize tracker
    tracker = MLflowTracker()
    
    # Example usage
    print("MLflow tracking module initialized successfully!")
    print(f"Tracking URI: {mlflow.get_tracking_uri()}")
    print(f"Experiment: {tracker.experiment_name}")


if __name__ == "__main__":
    main() 