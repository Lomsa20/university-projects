import pandas as pd

try:
    df = pd.read_csv('data.csv')
    print(df.head())  # Shows only first 5 rows
except FileNotFoundError:
    print("Error: 'data.csv' not found.")
except pd.errors.ParserError:
    print("Error: Could not parse CSV file.")

