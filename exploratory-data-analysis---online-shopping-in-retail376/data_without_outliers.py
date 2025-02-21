import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Plotter class to visualize distributions and outliers
class Plotter:
    def __init__(self, df):
        self.df = df

    def plot_boxplot(self, column):
        """Plot a boxplot to visualize outliers in a column."""
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=self.df[column], color='skyblue')
        plt.title(f"Boxplot of {column}")
        plt.show()

    def plot_histogram(self, column):
        """Plot a histogram to visualize the distribution of a column."""
        plt.figure(figsize=(8, 6))
        sns.histplot(self.df[column], kde=True, color='skyblue')
        plt.title(f"Distribution of {column}")
        plt.show()

    def plot_outliers(self, columns):
        """Visualize the outliers in the specified columns using boxplots."""
        for column in columns:
            self.plot_boxplot(column)

# DataFrameTransform class for EDA transformations, including outlier removal
class DataFrameTransform:
    def __init__(self, df):
        self.df = df
        self.plotter = Plotter(df)

    # Step 1: Visualize the data to identify outliers
    def visualize_data_for_outliers(self):
        """Visualize columns to identify potential outliers using boxplots."""
        for column in self.df.select_dtypes(include=['float64', 'int64']).columns:
            self.plotter.plot_boxplot(column)

    # Step 2: Remove outliers using the IQR method
    def remove_outliers(self):
        """Remove outliers based on the IQR method."""
        for column in self.df.select_dtypes(include=['float64', 'int64']).columns:
            Q1 = self.df[column].quantile(0.25)
            Q3 = self.df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            # Remove the outliers from the column
            self.df = self.df[(self.df[column] >= lower_bound) & (self.df[column] <= upper_bound)]
            print(f"Outliers removed from {column}.")
    
    # Step 3: Visualize the data again after removing outliers
    def re_visualize_data(self):
        """Re-visualize the data after removing outliers."""
        for column in self.df.select_dtypes(include=['float64', 'int64']).columns:
            self.plotter.plot_boxplot(column)

    # Save the transformed data after removing outliers
    def save_transformed_data(self, output_file):
        """Save the transformed data to a new CSV file."""
        self.df.to_csv(output_file, index=False)
        print(f"\nThe data after removing outliers has been saved to {output_file}")

# Load the data (from the previous data without null values)
file_path = r"C:\Users\nieve\exploratory-data-analysis---online-shopping-in-retail376\data_without_null_values.csv"
df = pd.read_csv(file_path)

# Create an instance of the DataFrameTransform class
data_transformer = DataFrameTransform(df)

# Step 1: Visualize the data to identify outliers
data_transformer.visualize_data_for_outliers()

# Step 2: Remove outliers
data_transformer.remove_outliers()

# Step 3: Re-visualize the data after removing outliers
data_transformer.re_visualize_data()

# Step 4: Save the cleaned data to a new file
output_file = r"C:\Users\nieve\exploratory-data-analysis---online-shopping-in-retail376\data_without_outliers.csv"
data_transformer.save_transformed_data(output_file)
