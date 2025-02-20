import pandas as pd

class DataFrameInfo:
    def __init__(self, df):
        """Initialize with a pandas DataFrame."""
        self.df = df
    
    def describe_columns(self):
        """Describe all columns to check their data types."""
        print(self.df.dtypes)
    
    def statistical_summary(self):
        """Generate statistical values: median, standard deviation, and mean for numerical columns only."""
        numeric_df = self.df.select_dtypes(include=['number'])  # Selecting only numerical columns
        stats = {
            'mean': numeric_df.mean(),
            'median': numeric_df.median(),
            'std_dev': numeric_df.std()
        }
        print("Statistical Summary:")
        print(pd.DataFrame(stats))

    def count_distinct_values(self):
        """Count distinct values in categorical columns."""
        categorical_columns = self.df.select_dtypes(include=['category', 'object']).columns
        print("\nDistinct Values in Categorical Columns:")
        for col in categorical_columns:
            print(f"{col}: {self.df[col].nunique()} distinct values")
    
    def print_shape(self):
        """Print out the shape of the DataFrame."""
        print(f"\nShape of the DataFrame: {self.df.shape}")
    
    def missing_values(self):
        """Generate count and percentage count of NULL values in each column."""
        null_count = self.df.isnull().sum()
        null_percentage = (null_count / len(self.df)) * 100
        null_info = pd.DataFrame({'Count': null_count, 'Percentage': null_percentage})
        print("\nMissing Values (Count and Percentage):")
        print(null_info)
    
    def additional_info(self):
        """Any other useful information (like memory usage)."""
        print(f"\nMemory Usage: {self.df.memory_usage(deep=True).sum() / (1024**2):.2f} MB")

