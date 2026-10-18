
import pandas as pd

# Extract data from source file
df = pd.read_csv("source_data.csv")

# Save extracted data
df.to_csv("raw_data.csv", index=False)

print("Extraction completed!")
print(df.head())
