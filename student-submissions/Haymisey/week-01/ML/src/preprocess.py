"""
Data preprocessing module for the Wisconsin Breast Cancer Dataset.

This module handles data cleaning, feature scaling, and preprocessing pipeline.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, f_classif
import logging
from pathlib import Path
import joblib
import yaml
from typing import Tuple, Dict, Any

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BreastCancerPreprocessor:
    """
    Data preprocessor class for the Wisconsin Breast Cancer Dataset.
    
    This class handles data cleaning, feature scaling, and preprocessing pipeline.
    """
    
    def __init__(self, data_dir: str = "data"):
        """
        Initialize the preprocessor.
        
        Args:
            data_dir (str): Directory to store data files
        """
        self.data_dir = Path(data_dir)
        self.processed_dir = self.data_dir / "processed"
        self.models_dir = Path("models")
        
        # Create directories if they don't exist
        self.processed_dir.mkdir(parents=True, exist_ok=True)
        self.models_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize preprocessing objects
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        self.feature_selector = None
        
        logger.info(f"Preprocessor initialized with data directory: {self.data_dir}")
    
    def load_split_data(self) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """
        Load the split training and testing data.
        
        Returns:
            tuple: (X_train, X_test, y_train, y_test)
        """
        logger.info("Loading split data...")
        
        # Load training data
        train_data = pd.read_csv(self.processed_dir / "train_data.csv")
        X_train = train_data.drop('target', axis=1)
        y_train = train_data['target']
        
        # Load testing data
        test_data = pd.read_csv(self.processed_dir / "test_data.csv")
        X_test = test_data.drop('target', axis=1)
        y_test = test_data['target']
        
        logger.info(f"Training set: {X_train.shape}")
        logger.info(f"Testing set: {X_test.shape}")
        
        return X_train, X_test, y_train, y_test
    
    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Handle missing values in the dataset.
        
        Args:
            df (pd.DataFrame): Input DataFrame
            
        Returns:
            pd.DataFrame: DataFrame with missing values handled
        """
        logger.info("Checking for missing values...")
        
        missing_counts = df.isnull().sum()
        total_missing = missing_counts.sum()
        
        if total_missing > 0:
            logger.warning(f"Found {total_missing} missing values")
            # For this dataset, we'll use mean imputation for numerical features
            df = df.fillna(df.mean())
            logger.info("Missing values filled with mean values")
        else:
            logger.info("No missing values found")
        
        return df
    
    def encode_target_variable(self, y: pd.Series) -> pd.Series:
        """
        Encode the target variable.
        
        Args:
            y (pd.Series): Target variable
            
        Returns:
            pd.Series: Encoded target variable
        """
        logger.info("Encoding target variable...")
        
        # Fit and transform the target variable
        y_encoded = pd.Series(
            self.label_encoder.fit_transform(y),
            index=y.index,
            name=y.name
        )
        
        logger.info(f"Target encoding mapping: {dict(zip(self.label_encoder.classes_, range(len(self.label_encoder.classes_))))}")
        
        return y_encoded
    
    def scale_features(self, X_train: pd.DataFrame, X_test: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Scale features using StandardScaler.
        
        Args:
            X_train (pd.DataFrame): Training features
            X_test (pd.DataFrame): Testing features
            
        Returns:
            tuple: (X_train_scaled, X_test_scaled)
        """
        logger.info("Scaling features...")
        
        # Fit scaler on training data
        X_train_scaled = pd.DataFrame(
            self.scaler.fit_transform(X_train),
            columns=X_train.columns,
            index=X_train.index
        )
        
        # Transform testing data
        X_test_scaled = pd.DataFrame(
            self.scaler.transform(X_test),
            columns=X_test.columns,
            index=X_test.index
        )
        
        logger.info("Features scaled successfully")
        logger.info(f"Training data - Mean: {X_train_scaled.mean().mean():.4f}, Std: {X_train_scaled.std().mean():.4f}")
        logger.info(f"Testing data - Mean: {X_test_scaled.mean().mean():.4f}, Std: {X_test_scaled.std().mean():.4f}")
        
        return X_train_scaled, X_test_scaled
    
    def select_features(self, X_train: pd.DataFrame, X_test: pd.DataFrame, 
                       y_train: pd.Series, k: int = 15) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Select top k features using ANOVA F-test.
        
        Args:
            X_train (pd.DataFrame): Training features
            X_test (pd.DataFrame): Testing features
            y_train (pd.Series): Training target
            k (int): Number of features to select
            
        Returns:
            tuple: (X_train_selected, X_test_selected)
        """
        logger.info(f"Selecting top {k} features...")
        
        # Initialize feature selector
        self.feature_selector = SelectKBest(score_func=f_classif, k=k)
        
        # Fit and transform training data
        X_train_selected = pd.DataFrame(
            self.feature_selector.fit_transform(X_train, y_train),
            columns=X_train.columns[self.feature_selector.get_support()],
            index=X_train.index
        )
        
        # Transform testing data
        X_test_selected = pd.DataFrame(
            self.feature_selector.transform(X_test),
            columns=X_test.columns[self.feature_selector.get_support()],
            index=X_test.index
        )
        
        # Get feature scores
        feature_scores = pd.DataFrame({
            'feature': X_train.columns,
            'score': self.feature_selector.scores_,
            'p_value': self.feature_selector.pvalues_
        }).sort_values('score', ascending=False)
        
        logger.info("Top 10 selected features:")
        print(feature_scores.head(10))
        
        return X_train_selected, X_test_selected
    
    def save_preprocessed_data(self, X_train: pd.DataFrame, X_test: pd.DataFrame,
                              y_train: pd.Series, y_test: pd.Series) -> None:
        """
        Save preprocessed data to disk.
        
        Args:
            X_train (pd.DataFrame): Preprocessed training features
            X_test (pd.DataFrame): Preprocessed testing features
            y_train (pd.Series): Encoded training target
            y_test (pd.Series): Encoded testing target
        """
        logger.info("Saving preprocessed data...")
        
        # Save preprocessed training data
        train_data = pd.concat([X_train, y_train], axis=1)
        train_path = self.processed_dir / "train_data_preprocessed.csv"
        train_data.to_csv(train_path, index=False)
        
        # Save preprocessed testing data
        test_data = pd.concat([X_test, y_test], axis=1)
        test_path = self.processed_dir / "test_data_preprocessed.csv"
        test_data.to_csv(test_path, index=False)
        
        # Save features and targets separately
        X_train.to_csv(self.processed_dir / "X_train_preprocessed.csv", index=False)
        X_test.to_csv(self.processed_dir / "X_test_preprocessed.csv", index=False)
        y_train.to_csv(self.processed_dir / "y_train_encoded.csv", index=False)
        y_test.to_csv(self.processed_dir / "y_test_encoded.csv", index=False)
        
        logger.info(f"Preprocessed data saved to {self.processed_dir}")
    
    def save_preprocessing_objects(self) -> None:
        """
        Save preprocessing objects (scaler, encoder, feature selector) to disk.
        """
        logger.info("Saving preprocessing objects...")
        
        # Save scaler
        scaler_path = self.models_dir / "scaler.pkl"
        joblib.dump(self.scaler, scaler_path)
        
        # Save label encoder
        encoder_path = self.models_dir / "label_encoder.pkl"
        joblib.dump(self.label_encoder, encoder_path)
        
        # Save feature selector if used
        if self.feature_selector is not None:
            selector_path = self.models_dir / "feature_selector.pkl"
            joblib.dump(self.feature_selector, selector_path)
        
        logger.info(f"Preprocessing objects saved to {self.models_dir}")
    
    def generate_preprocessing_report(self, X_train: pd.DataFrame, X_test: pd.DataFrame,
                                   y_train: pd.Series, y_test: pd.Series) -> Dict[str, Any]:
        """
        Generate a preprocessing report.
        
        Args:
            X_train (pd.DataFrame): Preprocessed training features
            X_test (pd.DataFrame): Preprocessed testing features
            y_train (pd.Series): Encoded training target
            y_test (pd.Series): Encoded testing target
            
        Returns:
            dict: Preprocessing report
        """
        logger.info("Generating preprocessing report...")
        
        report = {
            'preprocessing_steps': {
                'missing_values_handled': True,
                'target_encoded': True,
                'features_scaled': True,
                'feature_selection_applied': self.feature_selector is not None
            },
            'data_shapes': {
                'X_train_shape': X_train.shape,
                'X_test_shape': X_test.shape,
                'y_train_shape': y_train.shape,
                'y_test_shape': y_test.shape
            },
            'scaling_info': {
                'scaler_type': 'StandardScaler',
                'X_train_mean': X_train.mean().mean(),
                'X_train_std': X_train.std().mean(),
                'X_test_mean': X_test.mean().mean(),
                'X_test_std': X_test.std().mean()
            },
            'target_info': {
                'original_classes': list(self.label_encoder.classes_),
                'encoded_mapping': dict(zip(self.label_encoder.classes_, range(len(self.label_encoder.classes_)))),
                'y_train_distribution': y_train.value_counts().to_dict(),
                'y_test_distribution': y_test.value_counts().to_dict()
            }
        }
        
        if self.feature_selector is not None:
            report['feature_selection'] = {
                'method': 'SelectKBest with f_classif',
                'n_features_selected': X_train.shape[1],
                'selected_features': list(X_train.columns)
            }
        
        # Save report to file
        report_path = self.processed_dir / "preprocessing_report.yaml"
        with open(report_path, 'w') as f:
            yaml.dump(report, f, default_flow_style=False)
        
        logger.info(f"Preprocessing report saved to: {report_path}")
        
        return report
    
    def run_full_pipeline(self, use_feature_selection: bool = True, 
                         n_features: int = 15) -> Dict[str, Any]:
        """
        Run the complete preprocessing pipeline.
        
        Args:
            use_feature_selection (bool): Whether to use feature selection
            n_features (int): Number of features to select
            
        Returns:
            dict: Preprocessing results and report
        """
        logger.info("Starting preprocessing pipeline...")
        
        # Load split data
        X_train, X_test, y_train, y_test = self.load_split_data()
        
        # Handle missing values
        X_train = self.handle_missing_values(X_train)
        X_test = self.handle_missing_values(X_test)
        
        # Encode target variable
        y_train_encoded = self.encode_target_variable(y_train)
        y_test_encoded = self.encode_target_variable(y_test)
        
        # Scale features
        X_train_scaled, X_test_scaled = self.scale_features(X_train, X_test)
        
        # Feature selection (optional)
        if use_feature_selection:
            X_train_final, X_test_final = self.select_features(
                X_train_scaled, X_test_scaled, y_train_encoded, n_features
            )
        else:
            X_train_final, X_test_final = X_train_scaled, X_test_scaled
        
        # Save preprocessed data
        self.save_preprocessed_data(X_train_final, X_test_final, y_train_encoded, y_test_encoded)
        
        # Save preprocessing objects
        self.save_preprocessing_objects()
        
        # Generate report
        report = self.generate_preprocessing_report(X_train_final, X_test_final, 
                                                 y_train_encoded, y_test_encoded)
        
        logger.info("Preprocessing pipeline completed successfully!")
        
        return {
            'report': report,
            'data': {
                'X_train': X_train_final,
                'X_test': X_test_final,
                'y_train': y_train_encoded,
                'y_test': y_test_encoded
            }
        }


def main():
    """Main function to run the preprocessing pipeline."""
    # Initialize preprocessor
    preprocessor = BreastCancerPreprocessor()
    
    # Run full pipeline
    results = preprocessor.run_full_pipeline(use_feature_selection=True, n_features=15)
    
    print("\n" + "="*50)
    print("PREPROCESSING PIPELINE COMPLETED")
    print("="*50)
    print(f"Training set: {results['data']['X_train'].shape}")
    print(f"Testing set: {results['data']['X_test'].shape}")
    print(f"Features selected: {len(results['data']['X_train'].columns)}")
    print("="*50)


if __name__ == "__main__":
    main() 