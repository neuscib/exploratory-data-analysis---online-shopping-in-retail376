import pandas as pd  

file_path = r"C:\Users\nieve\exploratory-data-analysis---online-shopping-in-retail376\customer_activity_data.csv"
df = pd.read_csv(file_path)

# All columns
pd.set_option("display.max_columns", None)

print(f" Loaded data: {df.shape[0]} rows, {df.shape[1]} columns")
print(df.head())  # First 5 rows