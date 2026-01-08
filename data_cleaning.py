import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("diabetes.csv")

# Columns where zero is medically invalid
invalid_zero_cols = [
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI"
]

# Replace 0 with NaN in those columns
df[invalid_zero_cols] = df[invalid_zero_cols].replace(0, np.nan)

print("Missing values after replacing invalid zeros:\n")
print(df.isnull().sum())

# Fill missing values with median
df_cleaned = df.fillna(df.median())

print("\nMissing values after median imputation:\n")
print(df_cleaned.isnull().sum())

# Save cleaned dataset
df_cleaned.to_csv("cleaned_diabetes_data.csv", index=False)

print("\nCleaned dataset saved as cleaned_diabetes_data.csv")
