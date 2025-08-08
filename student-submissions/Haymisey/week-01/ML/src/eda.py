"""
Exploratory Data Analysis for Breast Cancer Dataset.

This script performs comprehensive EDA on the Wisconsin Breast Cancer Dataset.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import warnings
from pathlib import Path
import logging

warnings.filterwarnings('ignore')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set style for better plots
plt.style.use('default')
sns.set_palette("husl")


def load_and_explore_data():
    """Load and perform basic exploration of the dataset."""
    logger.info("Loading Wisconsin Breast Cancer dataset...")
    
    # Load dataset
    cancer_data = load_breast_cancer()
    
    # Create DataFrame
    df = pd.DataFrame(cancer_data.data, columns=cancer_data.feature_names)
    df['target'] = cancer_data.target
    
    # Map target values to meaningful labels
    target_mapping = {0: 'malignant', 1: 'benign'}
    df['target'] = df['target'].map(target_mapping)
    
    logger.info(f"Dataset loaded successfully!")
    logger.info(f"Dataset shape: {df.shape}")
    logger.info(f"Features: {len(cancer_data.feature_names)}")
    logger.info(f"Samples: {len(df)}")
    
    return df


def analyze_target_distribution(df):
    """Analyze the distribution of the target variable."""
    logger.info("Analyzing target variable distribution...")
    
    target_counts = df['target'].value_counts()
    target_percentages = df['target'].value_counts(normalize=True) * 100
    
    print("\nTarget Variable Distribution:")
    print(f"Benign: {target_counts['benign']} ({target_percentages['benign']:.1f}%)")
    print(f"Malignant: {target_counts['malignant']} ({target_percentages['malignant']:.1f}%)")
    
    # Create visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Bar plot
    target_counts.plot(kind='bar', ax=ax1, color=['lightblue', 'lightcoral'])
    ax1.set_title('Target Variable Distribution')
    ax1.set_ylabel('Count')
    ax1.set_xlabel('Diagnosis')
    
    # Pie chart
    ax2.pie(target_counts.values, labels=target_counts.index, autopct='%1.1f%%', 
             colors=['lightblue', 'lightcoral'])
    ax2.set_title('Target Variable Distribution (%)')
    
    plt.tight_layout()
    plt.savefig('data/processed/target_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return target_counts


def analyze_features(df):
    """Analyze feature characteristics."""
    logger.info("Analyzing feature characteristics...")
    
    features = df.drop('target', axis=1)
    target = df['target']
    
    print("\nFeature Analysis:")
    print(f"Number of features: {len(features.columns)}")
    print(f"Feature names: {list(features.columns)}")
    
    # Check for missing values
    missing_values = features.isnull().sum()
    print(f"\nMissing values per feature:")
    if missing_values.sum() > 0:
        print(missing_values[missing_values > 0])
    else:
        print("No missing values found!")
    
    # Feature statistics by target class
    print("\nFeature Statistics by Target Class (first 5 features):")
    for feature in features.columns[:5]:
        print(f"\n{feature}:")
        benign_stats = features[target == 'benign'][feature].describe()
        malignant_stats = features[target == 'malignant'][feature].describe()
        print(f"  Benign - Mean: {benign_stats['mean']:.2f}, Std: {benign_stats['std']:.2f}")
        print(f"  Malignant - Mean: {malignant_stats['mean']:.2f}, Std: {malignant_stats['std']:.2f}")
    
    return features, target


def plot_feature_distributions(features, target):
    """Plot distribution of features by target class."""
    logger.info("Creating feature distribution plots...")
    
    # Plot distribution of first 6 features by target class
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.ravel()
    
    for i, feature in enumerate(features.columns[:6]):
        # Create histogram
        axes[i].hist(features[target == 'benign'][feature], alpha=0.7, label='Benign', bins=20)
        axes[i].hist(features[target == 'malignant'][feature], alpha=0.7, label='Malignant', bins=20)
        axes[i].set_title(f'Distribution of {feature}')
        axes[i].set_xlabel(feature)
        axes[i].set_ylabel('Frequency')
        axes[i].legend()
    
    plt.tight_layout()
    plt.savefig('data/processed/feature_distributions.png', dpi=300, bbox_inches='tight')
    plt.show()


def analyze_correlations(features):
    """Analyze feature correlations."""
    logger.info("Analyzing feature correlations...")
    
    # Calculate correlation matrix
    correlation_matrix = features.corr()
    
    # Plot correlation heatmap
    plt.figure(figsize=(12, 10))
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    sns.heatmap(correlation_matrix, mask=mask, annot=False, cmap='coolwarm', center=0,
                square=True, linewidths=0.5, cbar_kws={"shrink": .8})
    plt.title('Feature Correlation Matrix')
    plt.tight_layout()
    plt.savefig('data/processed/correlation_matrix.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Find highly correlated features
    threshold = 0.8
    high_corr_pairs = []
    
    for i in range(len(correlation_matrix.columns)):
        for j in range(i+1, len(correlation_matrix.columns)):
            if abs(correlation_matrix.iloc[i, j]) > threshold:
                high_corr_pairs.append((
                    correlation_matrix.columns[i],
                    correlation_matrix.columns[j],
                    correlation_matrix.iloc[i, j]
                ))
    
    print(f"\nFeatures with correlation > {threshold}:")
    for pair in high_corr_pairs:
        print(f"{pair[0]} - {pair[1]}: {pair[2]:.3f}")
    
    return correlation_matrix


def analyze_feature_importance(features, target):
    """Analyze feature importance using Random Forest."""
    logger.info("Analyzing feature importance...")
    
    # Encode target variable
    le = LabelEncoder()
    y_encoded = le.fit_transform(target)
    
    # Train a simple Random Forest to get feature importance
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(features, y_encoded)
    
    # Get feature importance
    feature_importance = pd.DataFrame({
        'feature': features.columns,
        'importance': rf.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\nTop 10 Most Important Features:")
    print(feature_importance.head(10))
    
    # Plot feature importance
    plt.figure(figsize=(12, 8))
    sns.barplot(data=feature_importance.head(15), x='importance', y='feature')
    plt.title('Top 15 Feature Importance')
    plt.xlabel('Importance')
    plt.tight_layout()
    plt.savefig('data/processed/feature_importance.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return feature_importance


def detect_outliers(features):
    """Detect outliers in the dataset."""
    logger.info("Detecting outliers...")
    
    def detect_outliers_iqr(df, column):
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
        return len(outliers)
    
    print("\nOutlier Analysis:")
    outlier_counts = {}
    for column in features.columns:
        outlier_count = detect_outliers_iqr(features, column)
        if outlier_count > 0:
            outlier_counts[column] = outlier_count
    
    if outlier_counts:
        print("Features with outliers:")
        for feature, count in outlier_counts.items():
            print(f"{feature}: {count} outliers")
    else:
        print("No significant outliers detected!")
    
    return outlier_counts


def generate_summary_report(df, target_counts, feature_importance, outlier_counts):
    """Generate a comprehensive summary report."""
    logger.info("Generating summary report...")
    
    features = df.drop('target', axis=1)
    
    print("\n" + "="*60)
    print("EDA SUMMARY REPORT")
    print("="*60)
    print(f"Dataset Size: {df.shape[0]} samples, {df.shape[1]-1} features")
    print(f"Target Distribution: {dict(target_counts)}")
    print(f"Missing Values: {features.isnull().sum().sum()}")
    print(f"Data Types: All numerical")
    print(f"Feature Importance: Top feature is '{feature_importance.iloc[0]['feature']}'")
    print(f"Outliers: {len(outlier_counts)} features have outliers")
    print("="*60)
    
    print("\nRECOMMENDATIONS:")
    print("1. The dataset is well-balanced with no missing values")
    print("2. Feature scaling is recommended due to different scales")
    print("3. Consider feature selection based on importance")
    print("4. SVM with RBF kernel should work well for this dataset")
    print("5. Cross-validation is recommended for robust evaluation")
    
    # Save summary to file
    summary_path = Path('data/processed/eda_summary.txt')
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(summary_path, 'w') as f:
        f.write("EDA SUMMARY REPORT\n")
        f.write("="*60 + "\n")
        f.write(f"Dataset Size: {df.shape[0]} samples, {df.shape[1]-1} features\n")
        f.write(f"Target Distribution: {dict(target_counts)}\n")
        f.write(f"Missing Values: {features.isnull().sum().sum()}\n")
        f.write(f"Data Types: All numerical\n")
        f.write(f"Feature Importance: Top feature is '{feature_importance.iloc[0]['feature']}'\n")
        f.write(f"Outliers: {len(outlier_counts)} features have outliers\n")
        f.write("="*60 + "\n")
        f.write("\nRECOMMENDATIONS:\n")
        f.write("1. The dataset is well-balanced with no missing values\n")
        f.write("2. Feature scaling is recommended due to different scales\n")
        f.write("3. Consider feature selection based on importance\n")
        f.write("4. SVM with RBF kernel should work well for this dataset\n")
        f.write("5. Cross-validation is recommended for robust evaluation\n")
    
    logger.info(f"Summary report saved to: {summary_path}")


def main():
    """Main function to run the complete EDA pipeline."""
    logger.info("Starting Exploratory Data Analysis...")
    
    # Load and explore data
    df = load_and_explore_data()
    
    # Analyze target distribution
    target_counts = analyze_target_distribution(df)
    
    # Analyze features
    features, target = analyze_features(df)
    
    # Plot feature distributions
    plot_feature_distributions(features, target)
    
    # Analyze correlations
    correlation_matrix = analyze_correlations(features)
    
    # Analyze feature importance
    feature_importance = analyze_feature_importance(features, target)
    
    # Detect outliers
    outlier_counts = detect_outliers(features)
    
    # Generate summary report
    generate_summary_report(df, target_counts, feature_importance, outlier_counts)
    
    logger.info("Exploratory Data Analysis completed successfully!")


if __name__ == "__main__":
    main() 