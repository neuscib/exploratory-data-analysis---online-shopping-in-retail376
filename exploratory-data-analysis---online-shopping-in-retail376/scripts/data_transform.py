import pandas as pd

class DataTransform:
    
    def __init__(self, df):
        self.df = df
    
    def convert_month(self):
        """Ensure all values are in a valid format before converting."""
        valid_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        self.df['month'] = self.df['month'].apply(lambda x: x if x in valid_months else 'Jan')
        
        try:
            self.df['month'] = pd.to_datetime(self.df['month'], format='%b')
        except Exception as e:
            print(f"Error converting 'month' column: {e}")

    def convert_duration_columns(self):
        """Convert duration columns (in seconds) to timedelta format."""
        duration_columns = [
            'administrative_duration',
            'informational_duration',
            'product_related_duration'
        ]
        for col in duration_columns:
            self.df[col] = pd.to_timedelta(self.df[col], unit='s')
    
    def convert_categorical_columns(self):
        """Convert categorical columns to 'category' type."""
        categorical_columns = [
            'operating_systems', 'browser', 'region', 'traffic_type', 'visitor_type'
        ]
        for col in categorical_columns:
            self.df[col] = self.df[col].astype('category', errors='ignore')
    
    def convert_booleans(self):
        """Ensure 'weekend' and 'revenue' columns are of 'bool' type."""
        self.df['weekend'] = self.df['weekend'].astype('bool', errors='ignore')
        self.df['revenue'] = self.df['revenue'].astype('bool', errors='ignore')
    
    def apply_transforms(self):
        """Apply all type transformations."""
        self.convert_month()
        self.convert_duration_columns()
        self.convert_categorical_columns()
        self.convert_booleans()
        return self.df

def main():
    """Main function to load, transform, and save the dataset."""
    input_file_path = "/content/transformed_data.csv"  # Cambia esta ruta si es necesario
    output_file_path = r"C:\Users\nieve\exploratory-data-analysis---online-shopping-in-retail376\transformed_data.csv"

    df = pd.read_csv(input_file_path)
    print(df)

    data_transformer = DataTransform(df)
    df_transformed = data_transformer.apply_transforms()

    df_transformed.to_csv(output_file_path, index=False)
    print(f"File CSV saved in: {output_file_path}")

if __name__ == "__main__":
    main()
