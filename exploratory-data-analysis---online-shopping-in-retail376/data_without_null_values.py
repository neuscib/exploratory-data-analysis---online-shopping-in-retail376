import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Plotter class to visualize insights
class Plotter:
    def __init__(self, df):
        self.df = df

    def plot_missing_values(self):
        """Visualize the missing values in the dataset using a heatmap."""
        plt.figure(figsize=(12, 8))
        sns.heatmap(self.df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
        plt.title("Missing Values Heatmap")
        plt.show()

    def plot_missing_summary(self):
        """Generate a bar plot summarizing the missing values percentage for each column."""
        missing_percentage = self.df.isnull().mean() * 100
        missing_data = missing_percentage[missing_percentage > 0]
        
        plt.figure(figsize=(12, 6))
        missing_data.sort_values().plot(kind='bar', color='orange')
        plt.title("Missing Values by Column (%)")
        plt.xlabel("Columns")
        plt.ylabel("Percentage of Missing Data")
        plt.show()

# DataFrameTransform class for EDA transformations
class DataFrameTransform:
    def __init__(self, df):
        self.df = df
        self.plotter = Plotter(df)  # Instantiating the Plotter class for visualization

    # Step 1: Drop columns with more than 30% missing data
    def drop_columns_with_missing_data(self, threshold=30):
        """Drop columns with more than 'threshold' percentage of missing data."""
        missing_percentage = self.df.isnull().mean() * 100
        columns_to_drop = missing_percentage[missing_percentage > threshold].index
        self.df = self.df.drop(columns=columns_to_drop)  # Make sure to assign back
        print(f"\nDropped columns with more than {threshold}% missing data: {list(columns_to_drop)}")

    # Step 2: Impute missing data
    def impute_missing_data(self, strategy='median'):
        """Impute missing data using the specified strategy ('mean', 'median', 'category')."""
        if strategy == 'mean':
            numerical_cols = self.df.select_dtypes(include=['float64', 'int64']).columns
            self.df.loc[:, numerical_cols] = self.df[numerical_cols].fillna(self.df[numerical_cols].mean())
            print("\nMissing values imputed with the mean for numerical columns.")
        elif strategy == 'median':
            numerical_cols = self.df.select_dtypes(include=['float64', 'int64']).columns
            self.df.loc[:, numerical_cols] = self.df[numerical_cols].fillna(self.df[numerical_cols].median())
            print("\nMissing values imputed with the median for numerical columns.")
        elif strategy == 'category':
            categorical_columns = self.df.select_dtypes(include=['object']).columns
            self.df.loc[:, categorical_columns] = self.df[categorical_columns].fillna("Unknown")
            print("\nMissing values in categorical columns imputed with 'Unknown'.")
        else:
            print("Invalid strategy. Use 'mean', 'median', or 'category'.")

    # Step 3: Remove rows with null values in the 'operating_systems' column
    def remove_missing_operating_systems(self):
        """Remove rows with null values in the 'operating_systems' column."""
        self.df = self.df.dropna(subset=['operating_systems'])  # Make sure to assign back
        rows_after = len(self.df)
        print(f"\nRemoved rows with null values in 'operating_systems'. Now there are {rows_after} rows.")

    # Step 4: Check missing data after imputation
    def check_missing_data(self):
        """Check for missing data after imputation."""
        missing_data = self.df.isnull().sum()
        missing_percentage = (missing_data / len(self.df)) * 100
        missing_summary = pd.DataFrame({
            'Count': missing_data,
            'Percentage': missing_percentage
        })
        print("\nMissing Data (Count and Percentage):")
        print(missing_summary)

    # Step 5: Visualize missing data
    def visualize_missing_data(self):
        """Call Plotter functions to visualize missing data."""
        self.plotter.plot_missing_values()  # Show the heatmap of missing values
        self.plotter.plot_missing_summary()  # Show the bar plot of missing data summary

    # Step 6: Save the cleaned data to a new CSV file
    def save_cleaned_data(self, output_file):
        """Save the cleaned data to a new CSV file."""
        self.df.to_csv(output_file, index=False)
        print(f"\nCleaned data saved to {output_file}")

# Load the data
file_path = r"C:\Users\nieve\exploratory-data-analysis---online-shopping-in-retail376\customer_activity_data.csv"
df = pd.read_csv(file_path)  # Make sure to have the file in the correct path

# Create an instance of the DataFrameTransform class
data_transformer = DataFrameTransform(df)

# Step 1: Remove rows with missing values in 'operating_systems'
data_transformer.remove_missing_operating_systems()

# Step 2: Drop columns with more than 30% missing data
data_transformer.drop_columns_with_missing_data(threshold=30)

# Step 3: Impute missing values
data_transformer.impute_missing_data(strategy='median')  # Impute numerical values with the median
data_transformer.impute_missing_data(strategy='category')  # Impute categorical values with "Unknown"

# Step 4: Check for missing data after imputation
data_transformer.check_missing_data()

# Step 5: Visualize missing data
data_transformer.visualize_missing_data()

# Step 6: Save the cleaned data to a new CSV file
output_file = r"C:\Users\nieve\exploratory-data-analysis---online-shopping-in-retail376\data_without_null_values.csv"
data_transformer.save_cleaned_data(output_file)
