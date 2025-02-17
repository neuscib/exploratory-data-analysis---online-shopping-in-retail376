import yaml  # Importa el paquete PyYAML
from sqlalchemy import create_engine
import pandas as pd

# Función para cargar las credenciales desde el archivo YAML
def load_credentials(file_path='credentials.yaml'):
    """Cargar las credenciales desde el archivo YAML"""
    with open(file_path, 'r') as file:
        credentials = yaml.safe_load(file)  # Carga el contenido YAML en un diccionario
    return credentials

class RDSDatabaseConnector:
    def __init__(self, credentials):
        """Inicializa la clase con las credenciales de acceso a la base de datos"""
        self.host = credentials['RDS_HOST']
        self.password = credentials['RDS_PASSWORD']
        self.user = credentials['RDS_USER']
        self.database = credentials['RDS_DATABASE']
        self.port = credentials['RDS_PORT']
        self.engine = None

    def create_engine(self):
        """Crea el engine de SQLAlchemy para conectarse a la base de datos RDS"""
        connection_string = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        self.engine = create_engine(connection_string)

    def fetch_data(self):
        """Obtiene los datos de la tabla 'customer_activity' y los devuelve como un DataFrame de Pandas"""
        if self.engine is None:
            raise Exception("Debes crear el engine primero usando 'create_engine()'")
        
        query = "SELECT * FROM customer_activity"
        data = pd.read_sql(query, self.engine)
        return data

# Función para guardar los datos en un archivo CSV
def save_to_csv(data, file_name='customer_activity_data.csv'):
    data.to_csv(file_name, index=False)

# Ejecución principal
if __name__ == "__main__":
    # Cargar las credenciales desde el archivo YAML
    credentials = load_credentials()

    # Crear la conexión con la base de datos
    db_connector = RDSDatabaseConnector(credentials)
    db_connector.create_engine()

    # Obtener los datos de la tabla 'customer_activity'
    data = db_connector.fetch_data()

    # Guardar los datos en un archivo CSV
    save_to_csv(data)

    print("Los datos se han guardado correctamente en 'customer_activity_data.csv'")

