
import pandas as pd

# Read extracted data
df = pd.read_csv("raw_data.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Save transformed data
df.to_csv("cleaned_data.csv", index=False)

print("Transformation completed!")
print(df.head())
