import pandas as pd
df = pd.read_csv("students_raw.csv")
print("\nOriginal data:")
print(df)
print("\nOriginal shape:", df.shape)
# Check missing values
print("\nMissing values:")
print(df.isnull().sum())
# Check duplicates
print("\nDuplicate rows:", df.duplicated().sum())
# Remove duplicate rows
df = df.drop_duplicates()
# Fix data types
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
# Handle missing values
df["age"] = df["age"].fillna(df["age"].median())
df["marks"] = df["marks"].fillna(df["marks"].mean())
df["city"] = df["city"].fillna("Unknown")
# Standardize text
df["name"] = df["name"].str.strip().str.title()
df["city"] = df["city"].str.strip().str.title()
df["department"] = df["department"].str.strip().str.upper()
# Handle invalid marks
invalid = (df["marks"] < 0) | (df["marks"] > 100)
print("\nInvalid marks found:", invalid.sum())
df.loc[invalid, "marks"] = float("nan")
# Fill invalid marks using the median
df["marks"] = df["marks"].fillna(df["marks"].median())
# Convert age to integer
df["age"] = df["age"].round().astype(int)
# Reset index
df = df.reset_index(drop=True)
# Final report
print("\nCLEANED DATA")
print(df)
print("\nFinal shape:", df.shape)
print("\nMissing values after cleaning:")
print(df.isnull().sum())
print("\nDuplicates after cleaning:", df.duplicated().sum())
# Save cleaned dataset
df.to_csv("cleaned_students_raw.csv", index=False)
print("\nCleaned data saved successfully!")