import pandas as pd

file_path = "inventory.xlsx"

df = pd.read_excel(file_path)

print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 records:")
print(df.head())

