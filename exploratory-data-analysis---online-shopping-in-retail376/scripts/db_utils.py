import yaml  # Import PyYAML package
from sqlalchemy import create_engine
import pandas as pd
import os

# Function to load credentials from a YAML file
def load_credentials(file_path='credentials.yaml'):
    """Load credentials from a YAML file safely."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} was not found.")
    
    try:
        with open(file_path, 'r') as file:
            credentials = yaml.safe_load(file)  # Load YAML content into a dictionary
        return credentials
    except yaml.YAMLError as e:
        raise ValueError(f"Error reading the YAML file: {e}")

class RDSDatabaseConnector:
    """Class to manage connection to an RDS database using SQLAlchemy."""
    
    def __init__(self, credentials):
        """Initialize the connection using database credentials."""
        try:
            self.host = credentials['RDS_HOST']
            self.password = credentials['RDS_PASSWORD']
            self.user = credentials['RDS_USER']
            self.database = credentials['RDS_DATABASE']
            self.port = credentials['RDS_PORT']
        except KeyError as e:
            raise KeyError(f"Missing key {e} in credentials.")

        self.engine = None

    def create_engine(self):
        """Create and return a SQLAlchemy engine for database connection."""
        try:
            connection_string = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
            self.engine = create_engine(connection_string)
        except Exception as e:
            raise ConnectionError(f"Error connecting to the database: {e}")

    def fetch_data(self, table_name='customer_activity'):
        """Retrieve data from the specified table and return it as a Pandas DataFrame."""
        if self.engine is None:
            raise Exception("You must create the engine first using 'create_engine()'")

        query = f"SELECT * FROM {table_name}"
        try:
            with self.engine.connect() as connection:
                data = pd.read_sql(query, connection)
            return data
        except Exception as e:
            raise RuntimeError(f"Error fetching data from the database: {e}")

# Function to save data to a CSV file
def save_to_csv(data, file_name='customer_activity_data.csv'):
    """Save data to a CSV file, only if the DataFrame is not empty."""
    if data.empty:
        print("Warning: The DataFrame is empty, the CSV file will not be saved.")
        return
    
    data.to_csv(file_name, index=False)
    print(f"Data successfully saved to '{file_name}'.")

# Main execution
if __name__ == "__main__":
    try:
        # Load credentials from the YAML file
        credentials = load_credentials()

        # Create the database connection
        db_connector = RDSDatabaseConnector(credentials)
        db_connector.create_engine()

        # Fetch data from the 'customer_activity' table
        data = db_connector.fetch_data()

        # Save data to a CSV file
        save_to_csv(data)

    except Exception as e:
        print(f"An error occurred: {e}")
