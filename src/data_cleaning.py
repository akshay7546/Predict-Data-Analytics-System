import pandas as pd

# Load dataset
df = pd.read_csv("dataset/flipkart.csv")

print("Original Shape:", df.shape)

# -----------------------------
# 1. Remove unnecessary column
# -----------------------------
if "Unnamed: 0" in df.columns:
    df.drop(columns=["Unnamed: 0"], inplace=True)

# -----------------------------
# 2. Remove duplicate records
# -----------------------------
duplicates = df.duplicated().sum()
print("Duplicate Rows:", duplicates)

df.drop_duplicates(inplace=True)

# -----------------------------
# 3. Check missing values
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# 4. Remove missing values (if any)
# -----------------------------
df.dropna(inplace=True)

# -----------------------------
# 5. Reset Index
# -----------------------------
df.reset_index(drop=True, inplace=True)

# -----------------------------
# Final Dataset Information
# -----------------------------
print("\nCleaned Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv("output/cleaned_data.csv", index=False)

print("\nCleaned dataset saved successfully!")