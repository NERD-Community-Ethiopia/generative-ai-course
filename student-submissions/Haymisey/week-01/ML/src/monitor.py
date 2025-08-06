"""
Monitoring module for the Breast Cancer Classification model.

This module handles model monitoring, drift detection, and performance tracking.
"""

import pandas as pd
import numpy as np
import joblib
import json
import logging
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Tuple
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_breast_cancer

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ModelMonitor:
    """
    Model monitoring class for tracking performance and detecting drift.
    
    This class handles prediction logging, drift detection, and performance monitoring.
    """
    
    def __init__(self, model_path: str = "models/breast_cancer_model.pkl",
                 scaler_path: str = "models/scaler.pkl",
                 logs_dir: str = "logs"):
        """
        Initialize the model monitor.
        
        Args:
            model_path (str): Path to the trained model
            scaler_path (str): Path to the scaler
            logs_dir (str): Directory for monitoring logs
        """
        self.model_path = Path(model_path)
        self.scaler_path = Path(scaler_path)
        self.logs_dir = Path(logs_dir)
        
        # Create logs directory
        self.logs_dir.mkdir(parents=True, exist_ok=True)
        
        # Load model and scaler
        self.model = None
        self.scaler = None
        self.load_model()
        
        # Initialize monitoring data
        self.predictions_log = []
        self.performance_history = []
        
        logger.info("Model monitor initialized")
    
    def load_model(self):
        """Load the trained model and scaler."""
        try:
            if self.model_path.exists():
                self.model = joblib.load(self.model_path)
                logger.info("Model loaded successfully")
            else:
                logger.error(f"Model file not found: {self.model_path}")
            
            if self.scaler_path.exists():
                self.scaler = joblib.load(self.scaler_path)
                logger.info("Scaler loaded successfully")
            else:
                logger.error(f"Scaler file not found: {self.scaler_path}")
                
        except Exception as e:
            logger.error(f"Error loading model: {e}")
    
    def log_prediction(self, features: List[float], prediction: str, 
                      confidence: float, timestamp: str = None) -> None:
        """
        Log a prediction for monitoring.
        
        Args:
            features (List[float]): Input features
            prediction (str): Model prediction
            confidence (float): Prediction confidence
            timestamp (str): Timestamp of prediction
        """
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        
        prediction_log = {
            'timestamp': timestamp,
            'features': features,
            'prediction': prediction,
            'confidence': confidence
        }
        
        self.predictions_log.append(prediction_log)
        
        # Save to file
        self.save_predictions_log()
        
        logger.info(f"Prediction logged: {prediction} (confidence: {confidence:.3f})")
    
    def save_predictions_log(self):
        """Save predictions log to file."""
        log_file = self.logs_dir / "predictions_log.json"
        
        with open(log_file, 'w') as f:
            json.dump(self.predictions_log, f, indent=2)
        
        logger.info(f"Predictions log saved to: {log_file}")
    
    def load_predictions_log(self) -> List[Dict]:
        """Load predictions log from file."""
        log_file = self.logs_dir / "predictions_log.json"
        
        if log_file.exists():
            with open(log_file, 'r') as f:
                self.predictions_log = json.load(f)
            logger.info(f"Loaded {len(self.predictions_log)} prediction records")
        else:
            logger.info("No existing predictions log found")
        
        return self.predictions_log
    
    def analyze_prediction_distribution(self) -> Dict[str, Any]:
        """
        Analyze the distribution of predictions over time.
        
        Returns:
            dict: Analysis results
        """
        if not self.predictions_log:
            logger.warning("No predictions to analyze")
            return {}
        
        # Convert to DataFrame
        df = pd.DataFrame(self.predictions_log)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Analyze predictions
        prediction_counts = df['prediction'].value_counts()
        confidence_stats = df['confidence'].describe()
        
        # Time-based analysis
        df['date'] = df['timestamp'].dt.date
        daily_predictions = df.groupby('date')['prediction'].value_counts().unstack(fill_value=0)
        
        analysis = {
            'total_predictions': len(df),
            'prediction_distribution': prediction_counts.to_dict(),
            'confidence_stats': confidence_stats.to_dict(),
            'date_range': {
                'start': df['timestamp'].min().isoformat(),
                'end': df['timestamp'].max().isoformat()
            },
            'daily_predictions': daily_predictions.to_dict() if not daily_predictions.empty else {}
        }
        
        logger.info(f"Prediction analysis completed: {len(df)} predictions analyzed")
        return analysis
    
    def detect_data_drift(self, reference_data: pd.DataFrame, 
                         current_data: pd.DataFrame) -> Dict[str, Any]:
        """
        Detect data drift between reference and current data.
        
        Args:
            reference_data (pd.DataFrame): Reference dataset
            current_data (pd.DataFrame): Current dataset
            
        Returns:
            dict: Drift detection results
        """
        logger.info("Detecting data drift...")
        
        drift_results = {}
        
        for column in reference_data.columns:
            if column in current_data.columns:
                # Calculate statistical differences
                ref_mean = reference_data[column].mean()
                ref_std = reference_data[column].std()
                curr_mean = current_data[column].mean()
                curr_std = current_data[column].std()
                
                # Calculate drift metrics
                mean_drift = abs(curr_mean - ref_mean) / ref_std if ref_std > 0 else 0
                std_drift = abs(curr_std - ref_std) / ref_std if ref_std > 0 else 0
                
                drift_results[column] = {
                    'mean_drift': mean_drift,
                    'std_drift': std_drift,
                    'reference_mean': ref_mean,
                    'current_mean': curr_mean,
                    'reference_std': ref_std,
                    'current_std': curr_std,
                    'drift_detected': mean_drift > 0.5 or std_drift > 0.5  # Threshold
                }
        
        # Overall drift assessment
        drift_detected = any(result['drift_detected'] for result in drift_results.values())
        
        drift_summary = {
            'overall_drift_detected': drift_detected,
            'features_with_drift': [col for col, result in drift_results.items() 
                                  if result['drift_detected']],
            'drift_details': drift_results
        }
        
        logger.info(f"Drift detection completed. Drift detected: {drift_detected}")
        return drift_summary
    
    def simulate_drift_data(self, original_data: pd.DataFrame, 
                           drift_factor: float = 0.2) -> pd.DataFrame:
        """
        Simulate data drift for testing.
        
        Args:
            original_data (pd.DataFrame): Original dataset
            drift_factor (float): Factor to introduce drift
            
        Returns:
            pd.DataFrame: Data with simulated drift
        """
        logger.info(f"Simulating data drift with factor: {drift_factor}")
        
        drifted_data = original_data.copy()
        
        # Add noise to simulate drift
        for column in drifted_data.columns:
            noise = np.random.normal(0, drifted_data[column].std() * drift_factor, 
                                   size=len(drifted_data))
            drifted_data[column] = drifted_data[column] + noise
        
        return drifted_data
    
    def generate_drift_report(self, reference_data: pd.DataFrame) -> Dict[str, Any]:
        """
        Generate a comprehensive drift report.
        
        Args:
            reference_data (pd.DataFrame): Reference dataset
            
        Returns:
            dict: Drift report
        """
        logger.info("Generating drift report...")
        
        # Load current predictions
        self.load_predictions_log()
        
        if not self.predictions_log:
            logger.warning("No predictions available for drift analysis")
            return {}
        
        # Convert predictions to DataFrame
        predictions_df = pd.DataFrame(self.predictions_log)
        
        # Create current data from recent predictions
        recent_predictions = predictions_df.tail(100)  # Last 100 predictions
        current_features = pd.DataFrame(recent_predictions['features'].tolist())
        
        # Detect drift
        drift_results = self.detect_data_drift(reference_data, current_features)
        
        # Generate report
        report = {
            'report_date': datetime.now().isoformat(),
            'drift_analysis': drift_results,
            'prediction_analysis': self.analyze_prediction_distribution(),
            'recommendations': self.generate_recommendations(drift_results)
        }
        
        # Save report
        report_path = self.logs_dir / "drift_report.json"
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"Drift report saved to: {report_path}")
        return report
    
    def generate_recommendations(self, drift_results: Dict[str, Any]) -> List[str]:
        """
        Generate recommendations based on drift analysis.
        
        Args:
            drift_results (dict): Drift detection results
            
        Returns:
            List[str]: List of recommendations
        """
        recommendations = []
        
        if drift_results.get('overall_drift_detected', False):
            recommendations.append("Data drift detected - consider retraining the model")
            recommendations.append("Monitor model performance closely")
            
            drifted_features = drift_results.get('features_with_drift', [])
            if drifted_features:
                recommendations.append(f"Features with significant drift: {', '.join(drifted_features)}")
        else:
            recommendations.append("No significant data drift detected")
            recommendations.append("Continue monitoring as scheduled")
        
        return recommendations
    
    def plot_drift_analysis(self, reference_data: pd.DataFrame, 
                           save_path: str = "logs/drift_analysis.png") -> str:
        """
        Create visualization for drift analysis.
        
        Args:
            reference_data (pd.DataFrame): Reference dataset
            save_path (str): Path to save the plot
            
        Returns:
            str: Path to saved plot
        """
        logger.info("Creating drift analysis visualization...")
        
        # Load recent predictions
        self.load_predictions_log()
        
        if not self.predictions_log:
            logger.warning("No predictions available for visualization")
            return ""
        
        # Convert predictions to DataFrame
        predictions_df = pd.DataFrame(self.predictions_log)
        current_features = pd.DataFrame(predictions_df['features'].tail(100).tolist())
        
        # Select a few key features for visualization
        key_features = reference_data.columns[:6]  # First 6 features
        
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        axes = axes.ravel()
        
        for i, feature in enumerate(key_features):
            if feature in current_features.columns:
                # Plot distributions
                axes[i].hist(reference_data[feature], alpha=0.7, label='Reference', bins=20)
                axes[i].hist(current_features[feature], alpha=0.7, label='Current', bins=20)
                axes[i].set_title(f'Distribution of {feature}')
                axes[i].set_xlabel(feature)
                axes[i].set_ylabel('Frequency')
                axes[i].legend()
        
        plt.tight_layout()
        
        # Save plot
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Drift analysis plot saved to: {save_path}")
        return save_path
    
    def run_monitoring_pipeline(self) -> Dict[str, Any]:
        """
        Run the complete monitoring pipeline.
        
        Returns:
            dict: Monitoring results
        """
        logger.info("Starting monitoring pipeline...")
        
        # Load reference data
        cancer_data = load_breast_cancer()
        reference_data = pd.DataFrame(cancer_data.data, columns=cancer_data.feature_names)
        
        # Generate drift report
        drift_report = self.generate_drift_report(reference_data)
        
        # Create visualization
        plot_path = self.plot_drift_analysis(reference_data)
        
        # Simulate drift for testing
        drifted_data = self.simulate_drift_data(reference_data, drift_factor=0.3)
        drift_results = self.detect_data_drift(reference_data, drifted_data)
        
        logger.info("Monitoring pipeline completed successfully!")
        
        return {
            'drift_report': drift_report,
            'drift_plot_path': plot_path,
            'simulated_drift_results': drift_results
        }


def main():
    """Main function to run the monitoring pipeline."""
    # Initialize monitor
    monitor = ModelMonitor()
    
    # Run monitoring pipeline
    results = monitor.run_monitoring_pipeline()
    
    print("\n" + "="*50)
    print("MONITORING PIPELINE COMPLETED")
    print("="*50)
    
    if results.get('drift_report'):
        drift_analysis = results['drift_report']['drift_analysis']
        print(f"Drift detected: {drift_analysis.get('overall_drift_detected', False)}")
        
        if drift_analysis.get('features_with_drift'):
            print(f"Features with drift: {drift_analysis['features_with_drift']}")
    
    print("="*50)


if __name__ == "__main__":
    main() 