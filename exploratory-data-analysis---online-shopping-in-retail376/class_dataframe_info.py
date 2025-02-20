import pandas as pd

# Assuming you have the transformation code for the DataFrame
class DataTransform:
    def __init__(self, df):
        self.df = df
    
    def convert_month(self):
        """Converts the 'month' column to a datetime object."""
        valid_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.df['month'] = self.df['month'].apply(lambda x: x if x in valid_months else 'Jan')
        try:
            self.df['month'] = pd.to_datetime(self.df['month'], format='%b')
        except Exception as e:
            print(f"Error converting 'month' column: {e}")
    
    def apply_transforms(self):
        """Applies all necessary transformations."""
        self.convert_month()
        return self.df

# Load the data
file_path = r"C:\Users\nieve\exploratory-data-analysis---online-shopping-in-retail376\customer_activity_data.csv"
df = pd.read_csv(file_path)

# Create and apply the transformations
data_transformer = DataTransform(df)
df_transformed = data_transformer.apply_transforms()

# Now you can apply the DataFrameInfo class
class DataFrameInfo:
    def __init__(self, df):
        """Initializes with a pandas DataFrame."""
        self.df = df
    
    def describe_columns(self):
        """Describe all columns to check their data types and null values."""
        print("Data Types:")
        print(self.df.dtypes)
        print("\nNull Values per Column:")
        print(self.df.isnull().sum())
    
    def statistical_summary(self):
        """Generate statistical values: median, standard deviation, and mean for numerical columns."""
        numeric_df = self.df.select_dtypes(include=['number'])  # Select only numerical columns
        stats = {
            'mean': numeric_df.mean(),
            'median': numeric_df.median(),
            'std_dev': numeric_df.std()
        }
        print("\nStatistical Summary:")
        print(pd.DataFrame(stats))

    def count_distinct_values(self):
        """Count distinct values in categorical columns."""
        categorical_columns = self.df.select_dtypes(include=['category', 'object']).columns
        print("\nDistinct Values in Categorical Columns:")
        for col in categorical_columns:
            print(f"{col}: {self.df[col].nunique()} distinct values")
    
    def print_shape(self):
        """Print the shape of the DataFrame."""
        print(f"\nShape of the DataFrame: {self.df.shape}")
    
    def missing_values(self):
        """Generate count and percentage count of NULL values in each column."""
        null_count = self.df.isnull().sum()
        null_percentage = (null_count / len(self.df)) * 100
        null_info = pd.DataFrame({'Count': null_count, 'Percentage': null_percentage})
        print("\nMissing Values (Count and Percentage):")
        print(null_info)
    
    def additional_info(self):
        """Any other useful information (such as memory usage)."""
        print(f"\nMemory Usage: {self.df.memory_usage(deep=True).sum() / (1024**2):.2f} MB")
        print(f"\nNumber of unique values per numerical column:")
        print(self.df.select_dtypes(include=['number']).nunique())

# Apply the DataFrameInfo class to the transformed DataFrame
df_info = DataFrameInfo(df_transformed)

# Call the methods to explore the DataFrame
df_info.describe_columns()
df_info.statistical_summary()
df_info.count_distinct_values()
df_info.print_shape()
df_info.missing_values()
df_info.additional_info()
