import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

# Plotter class to visualize the data
class Plotter:
    def __init__(self, df):
        self.df = df

    def plot_histogram(self, column):
        """Plot a histogram to visualize the distribution of a column."""
        plt.figure(figsize=(8, 6))
        sns.histplot(self.df[column], kde=True, color='skyblue')
        plt.title(f"Distribution of {column}")
        plt.show()

    def plot_correlation_matrix(self):
        """Plot the correlation matrix as a heatmap."""
        plt.figure(figsize=(12, 8))
        
        # Filter out non-numeric columns for correlation calculation
        numeric_df = self.df.select_dtypes(include=['float64', 'int64'])
        
        # Compute the correlation matrix for numeric columns
        correlation_matrix = numeric_df.corr()
        
        # Plot the correlation matrix heatmap
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
        plt.title("Correlation Matrix")
        plt.show()

# DataFrameTransform class for EDA transformations
class DataFrameTransform:
    def __init__(self, df):
        self.df = df
        self.plotter = Plotter(df)

    # Step 1: Identify skewed columns
    def identify_skewed_columns(self, threshold=0.5):
        """Identify columns with skewness greater than the specified threshold."""
        skewness = self.df.select_dtypes(include=['float64', 'int64']).skew()
        skewed_columns = skewness[abs(skewness) > threshold].index
        return skewed_columns

    # Step 2: Transform skewed columns
    def transform_skewed_columns(self, skewed_columns):
        """Apply transformations to reduce skewness in skewed columns."""
        for column in skewed_columns:
            # Apply log transformation if the column is positively skewed
            if self.df[column].min() > 0:
                self.df[column] = np.log1p(self.df[column])
                print(f"\nLog transformation applied to {column}.")
            # Apply square root transformation if the column is positively skewed
            elif self.df[column].min() >= 0:
                self.df[column] = np.sqrt(self.df[column])
                print(f"\nSquare root transformation applied to {column}.")
            # Use Box-Cox transformation if needed
            else:
                self.df[column], _ = stats.boxcox(self.df[column] + 1)  # Box-Cox transformation
                print(f"\nBox-Cox transformation applied to {column}.")

    # Step 3: Apply transformations and check the results
    def apply_transforms_and_check(self):
        skewed_columns = self.identify_skewed_columns()
        for column in skewed_columns:
            self.plotter.plot_histogram(column)  # Visualize the original distribution of the skewed columns
        
        # Transform skewed columns
        self.transform_skewed_columns(skewed_columns)
        
        # Visualize the transformed columns
        for column in skewed_columns:
            self.plotter.plot_histogram(column)
        
        return skewed_columns

    # Step 4: Identify and remove outliers
    def identify_and_remove_outliers(self, z_threshold=3):
        """Identify and remove outliers based on Z-score."""
        numeric_df = self.df.select_dtypes(include=['float64', 'int64'])
        z_scores = np.abs(stats.zscore(numeric_df))
        outliers = (z_scores > z_threshold).all(axis=1)
        print(f"\n{sum(outliers)} outliers identified.")
        
        # Remove the rows containing outliers
        self.df = self.df[~outliers]
        print(f"\nOutliers removed. Remaining data shape: {self.df.shape}")

    # Step 5: Identify and remove highly correlated columns
    def identify_highly_correlated_columns(self, threshold=0.9):
        """Identify columns with a correlation higher than the threshold."""
        numeric_df = self.df.select_dtypes(include=['float64', 'int64'])
        correlation_matrix = numeric_df.corr()
        
        highly_correlated = set()
        
        for i in range(len(correlation_matrix.columns)):
            for j in range(i):
                if abs(correlation_matrix.iloc[i, j]) > threshold:
                    column_name = correlation_matrix.columns[i]
                    highly_correlated.add(column_name)
                    
        return list(highly_correlated)

    def remove_highly_correlated_columns(self, threshold=0.9):
        """Remove the highly correlated columns."""
        highly_correlated_columns = self.identify_highly_correlated_columns(threshold)
        
        if highly_correlated_columns:
            self.df = self.df.drop(columns=highly_correlated_columns)
            print(f"\nRemoved the following highly correlated columns: {highly_correlated_columns}")
        else:
            print("\nNo highly correlated columns were found above the threshold.")

    # Save the transformed data to a CSV file
    def save_transformed_data(self, output_file):
        """Save the transformed data to a new CSV file."""
        self.df.to_csv(output_file, index=False)
        print(f"\nTransformed data saved to {output_file}")

# Load the data (from the previous cleaned file)
file_path = r"C:\Users\nieve\exploratory-data-analysis---online-shopping-in-retail376\data_without_null_values.csv"
df = pd.read_csv(file_path)

# Create an instance of the DataFrameTransform class
data_transformer = DataFrameTransform(df)

# Step 1: Visualize the correlation matrix
data_transformer.plotter.plot_correlation_matrix()

# Step 2 and 3: Identify and remove outliers
data_transformer.identify_and_remove_outliers(z_threshold=3)

# Step 4: Identify and remove highly correlated columns
data_transformer.remove_highly_correlated_columns(threshold=0.9)

# Step 5: Save the transformed data after removing outliers and highly correlated columns
output_file = r"C:\Users\nieve\exploratory-data-analysis---online-shopping-in-retail376\data_cleaned.csv"
data_transformer.save_transformed_data(output_file)
