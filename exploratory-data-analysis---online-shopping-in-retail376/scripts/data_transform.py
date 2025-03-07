import pandas as pd

df = pd.read_csv("/content/transformed_data.csv")  
print(df)

class DataTransform:
    
    def __init__(self, df):
        self.df = df
    
    def convert_month(self):
        # Ensure all values are in a valid format before converting
        valid_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        # Replace invalid months with 'Jan' or any other default value
        self.df['month'] = self.df['month'].apply(lambda x: x if x in valid_months else 'Jan')
        
        # Now convert to datetime, ensuring only valid values are converted
        try:
            self.df['month'] = pd.to_datetime(self.df['month'], format='%b')
        except Exception as e:
            print(f"Error converting 'month' column: {e}")

    def convert_duration_columns(self):
        """Converts duration columns (in seconds) to timedelta format."""
        duration_columns = [
            'administrative_duration',
            'informational_duration',
            'product_related_duration'
        ]
        for col in duration_columns:
            self.df[col] = pd.to_timedelta(self.df[col], unit='s')
    
    def convert_operating_systems(self):
        """Converts the 'operating_systems' column to 'category' type."""
        self.df['operating_systems'] = self.df['operating_systems'].astype('category', errors='ignore')
    
    def convert_browser(self):
        """Converts the 'browser' column to 'category' type."""
        self.df['browser'] = self.df['browser'].astype('category', errors='ignore')
    
    def convert_region(self):
        """Converts the 'region' column to 'category' type."""
        self.df['region'] = self.df['region'].astype('category', errors='ignore')
    
    def convert_traffic_type(self):
        """Converts the 'traffic_type' column to 'category' type."""
        self.df['traffic_type'] = self.df['traffic_type'].astype('category', errors='ignore')
    
    def convert_visitor_type(self):
        """Converts the 'visitor_type' column to 'category' type."""
        self.df['visitor_type'] = self.df['visitor_type'].astype('category', errors='ignore')
    
    def convert_booleans(self):
        """Ensures the 'weekend' and 'revenue' columns are of 'bool' type."""
        self.df['weekend'] = self.df['weekend'].astype('bool', errors='ignore')
        self.df['revenue'] = self.df['revenue'].astype('bool', errors='ignore')
    
    def apply_transforms(self):
        """Applies all the type transformations without reducing columns."""
        self.convert_month()
        self.convert_duration_columns()
        self.convert_operating_systems()
        self.convert_browser()
        self.convert_region()
        self.convert_traffic_type()
        self.convert_visitor_type()
        self.convert_booleans()
        return self.df

# Apply the transformations to the DataFrame
data_transformer = DataTransform(df)
df_transformed = data_transformer.apply_transforms()

# Save the transformed DataFrame to a new CSV file
output_file_path = r"C:\Users\nieve\exploratory-data-analysis---online-shopping-in-retail376\transformed_data.csv"
df_transformed.to_csv(output_file_path, index=False)

print(f"File CSV saved in: {output_file_path}")
