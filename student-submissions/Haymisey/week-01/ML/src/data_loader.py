"""
Data loader module for the Wisconsin Breast Cancer Dataset.

This module handles downloading, loading, and basic inspection of the dataset.
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import logging
from pathlib import Path
import yaml

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BreastCancerDataLoader:
    """
    Data loader class for the Wisconsin Breast Cancer Dataset.
    
    This class handles downloading, loading, and basic data inspection.
    """
    
    def __init__(self, data_dir: str = "data"):
        """
        Initialize the data loader.
        
        Args:
            data_dir (str): Directory to store data files
        """
        self.data_dir = Path(data_dir)
        self.raw_dir = self.data_dir / "raw"
        self.processed_dir = self.data_dir / "processed"
        
        # Create directories if they don't exist
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Data loader initialized with data directory: {self.data_dir}")
    
    def load_data(self) -> tuple[pd.DataFrame, pd.Series]:
        """
        Load the Wisconsin Breast Cancer dataset.
        
        Returns:
            tuple: (features_df, target_series) - Features and target variables
        """
        logger.info("Loading Wisconsin Breast Cancer dataset...")
        
        # Load dataset from sklearn
        cancer_data = load_breast_cancer()
        
        # Create features DataFrame
        features_df = pd.DataFrame(
            cancer_data.data,
            columns=cancer_data.feature_names
        )
        
        # Create target Series
        target_series = pd.Series(
            cancer_data.target,
            name='target'
        )
        
        # Map target values to meaningful labels
        target_mapping = {0: 'malignant', 1: 'benign'}
        target_series = target_series.map(target_mapping)
        
        logger.info(f"Dataset loaded successfully!")
        logger.info(f"Features shape: {features_df.shape}")
        logger.info(f"Target shape: {target_series.shape}")
        
        return features_df, target_series
    
    def save_raw_data(self, features_df: pd.DataFrame, target_series: pd.Series) -> None:
        """
        Save raw data to disk.
        
        Args:
            features_df (pd.DataFrame): Features DataFrame
            target_series (pd.Series): Target Series
        """
        # Combine features and target
        raw_data = pd.concat([features_df, target_series], axis=1)
        
        # Save to CSV
        raw_data_path = self.raw_dir / "breast_cancer_raw.csv"
        raw_data.to_csv(raw_data_path, index=False)
        
        logger.info(f"Raw data saved to: {raw_data_path}")
    
    def inspect_data(self, features_df: pd.DataFrame, target_series: pd.Series) -> dict:
        """
        Perform basic data inspection.
        
        Args:
            features_df (pd.DataFrame): Features DataFrame
            target_series (pd.Series): Target Series
            
        Returns:
            dict: Data inspection summary
        """
        logger.info("Performing data inspection...")
        
        inspection_summary = {
            'dataset_info': {
                'total_samples': len(features_df),
                'total_features': len(features_df.columns),
                'target_classes': target_series.value_counts().to_dict(),
                'missing_values': features_df.isnull().sum().sum(),
                'duplicate_rows': features_df.duplicated().sum()
            },
            'feature_info': {
                'feature_names': list(features_df.columns),
                'feature_types': features_df.dtypes.to_dict(),
                'feature_ranges': {
                    col: {
                        'min': features_df[col].min(),
                        'max': features_df[col].max(),
                        'mean': features_df[col].mean(),
                        'std': features_df[col].std()
                    }
                    for col in features_df.columns
                }
            },
            'target_info': {
                'class_distribution': target_series.value_counts().to_dict(),
                'class_balance': target_series.value_counts(normalize=True).to_dict()
            }
        }
        
        # Log summary
        logger.info(f"Dataset Summary:")
        logger.info(f"  - Total samples: {inspection_summary['dataset_info']['total_samples']}")
        logger.info(f"  - Total features: {inspection_summary['dataset_info']['total_features']}")
        logger.info(f"  - Target classes: {inspection_summary['dataset_info']['target_classes']}")
        logger.info(f"  - Missing values: {inspection_summary['dataset_info']['missing_values']}")
        logger.info(f"  - Duplicate rows: {inspection_summary['dataset_info']['duplicate_rows']}")
        
        return inspection_summary
    
    def split_data(self, features_df: pd.DataFrame, target_series: pd.Series, 
                   test_size: float = 0.2, random_state: int = 42) -> tuple:
        """
        Split data into training and testing sets.
        
        Args:
            features_df (pd.DataFrame): Features DataFrame
            target_series (pd.Series): Target Series
            test_size (float): Proportion of data for testing
            random_state (int): Random seed for reproducibility
            
        Returns:
            tuple: (X_train, X_test, y_train, y_test)
        """
        logger.info(f"Splitting data with test_size={test_size}, random_state={random_state}")
        
        X_train, X_test, y_train, y_test = train_test_split(
            features_df, target_series,
            test_size=test_size,
            random_state=random_state,
            stratify=target_series
        )
        
        logger.info(f"Training set size: {len(X_train)}")
        logger.info(f"Testing set size: {len(X_test)}")
        
        return X_train, X_test, y_train, y_test
    
    def save_split_data(self, X_train: pd.DataFrame, X_test: pd.DataFrame,
                       y_train: pd.Series, y_test: pd.Series) -> None:
        """
        Save split datasets to disk.
        
        Args:
            X_train (pd.DataFrame): Training features
            X_test (pd.DataFrame): Testing features
            y_train (pd.Series): Training targets
            y_test (pd.Series): Testing targets
        """
        # Save training data
        train_data = pd.concat([X_train, y_train], axis=1)
        train_path = self.processed_dir / "train_data.csv"
        train_data.to_csv(train_path, index=False)
        
        # Save testing data
        test_data = pd.concat([X_test, y_test], axis=1)
        test_path = self.processed_dir / "test_data.csv"
        test_data.to_csv(test_path, index=False)
        
        # Save features and targets separately
        X_train.to_csv(self.processed_dir / "X_train.csv", index=False)
        X_test.to_csv(self.processed_dir / "X_test.csv", index=False)
        y_train.to_csv(self.processed_dir / "y_train.csv", index=False)
        y_test.to_csv(self.processed_dir / "y_test.csv", index=False)
        
        logger.info(f"Split data saved to {self.processed_dir}")
    
    def run_full_pipeline(self) -> dict:
        """
        Run the complete data loading pipeline.
        
        Returns:
            dict: Pipeline results and inspection summary
        """
        logger.info("Starting data loading pipeline...")
        
        # Load data
        features_df, target_series = self.load_data()
        
        # Save raw data
        self.save_raw_data(features_df, target_series)
        
        # Inspect data
        inspection_summary = self.inspect_data(features_df, target_series)
        
        # Split data
        X_train, X_test, y_train, y_test = self.split_data(features_df, target_series)
        
        # Save split data
        self.save_split_data(X_train, X_test, y_train, y_test)
        
        logger.info("Data loading pipeline completed successfully!")
        
        return {
            'inspection_summary': inspection_summary,
            'data_splits': {
                'X_train_shape': X_train.shape,
                'X_test_shape': X_test.shape,
                'y_train_shape': y_train.shape,
                'y_test_shape': y_test.shape
            }
        }


def main():
    """Main function to run the data loading pipeline."""
    # Initialize data loader
    data_loader = BreastCancerDataLoader()
    
    # Run full pipeline
    results = data_loader.run_full_pipeline()
    
    print("\n" + "="*50)
    print("DATA LOADING PIPELINE COMPLETED")
    print("="*50)
    print(f"Dataset loaded successfully!")
    print(f"Training set: {results['data_splits']['X_train_shape']}")
    print(f"Testing set: {results['data_splits']['X_test_shape']}")
    print("="*50)


if __name__ == "__main__":
    main() 