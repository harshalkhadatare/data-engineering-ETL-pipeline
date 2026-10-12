
import pandas as pd

# Read cleaned data
df = pd.read_csv("cleaned_data.csv")

# Load data into final output
df.to_csv("final_data.csv", index=False)

print("Loading completed!")
print("Total records loaded:", len(df))
