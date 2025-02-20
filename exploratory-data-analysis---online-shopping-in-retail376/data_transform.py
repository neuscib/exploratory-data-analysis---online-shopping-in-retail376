import pandas as pd

# File path to the dataset
file_path = r"C:\Users\nieve\exploratory-data-analysis---online-shopping-in-retail376\customer_activity_data.csv"
df = pd.read_csv(file_path)

class DataTransform:
    
    def __init__(self, df):
        self.df = df
    
    def convert_month(self):
        """Converts the 'month' column to a datetime object, representing the first day of each month."""
        # Converting 'month' to the first day of the corresponding month in datetime format
        self.df['month'] = pd.to_datetime(self.df['month'] + ' 01', format='%b %d', errors='coerce')
    
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
df