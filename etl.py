import pandas as pd

# =========================
# 1. EXTRACT
# =========================

file_path = "inventory.xlsx"

df = pd.read_excel(file_path)

print("Data extracted successfully.")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# =========================
# 2. TRANSFORM
# =========================

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Remove extra spaces from text columns
text_columns = ["ItemCode", "ItemName", "Location"]

for column in text_columns:
    df[column] = df[column].astype(str).str.strip()

# Convert date
df["ReportDate"] = pd.to_datetime(
    df["ReportDate"],
    errors="coerce"
)

# Convert numeric columns
df["Qty"] = pd.to_numeric(
    df["Qty"],
    errors="coerce"
)

df["Rate"] = pd.to_numeric(
    df["Rate"],
    errors="coerce"
)

# Create Amount
df["Amount"] = df["Qty"] * df["Rate"]


# =========================
# 3. DATA QUALITY CHECKS
# =========================

print("\n--- Data Quality Checks ---")

print("Missing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nNegative quantities:")
print(df[df["Qty"] < 0])


# =========================
# 4. DISPLAY TRANSFORMED DATA
# =========================

print("\n--- Transformed Data ---")
print(df.head())

print("\nTotal Amount:", df["Amount"].sum())


print("\nETL process completed successfully.")