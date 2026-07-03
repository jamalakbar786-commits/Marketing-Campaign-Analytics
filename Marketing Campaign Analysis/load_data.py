import os
import pandas as pd
from config import engine

def load_csv_to_db(file_path, table_name):
    """Imports a CSV file into the specified MySQL table."""
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    print(f"Reading {file_path}...")
    # read_csv handles data types automatically
    df = pd.read_csv(file_path)

    print(f"Loading data into table '{table_name}'...")
    try:
        # if_exists='append' keeps your truncated table structure
        # index=False prevents pandas from creating an extra column for row numbers
        df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
        print(f"Successfully loaded {len(df)} rows into '{table_name}'.\n")
    except Exception as e:
        print(f"Failed to load data into '{table_name}'. Error: {e}\n")

if __name__ == "__main__":
    # Example usage:
    # Replace 'your_data.csv' with your actual file path
    # Replace 'your_table_name' with your actual MySQL table name
    
    csv_file = "C:/Users/LENOVO/Marketing_Campaign_Analytics_30.06.2026.csv"
    target_table = "customers"
    
    load_csv_to_db(csv_file, target_table)
