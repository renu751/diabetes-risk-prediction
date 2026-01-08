import pandas as pd

# Load dataset
df = pd.read_csv("diabetes.csv")

print("Dataset shape:", df.shape)
print("\nColumn names:\n", df.columns)

print("\nMissing values:\n")
print(df.isnull().sum())

print("\nBasic statistics:\n")
print(df.describe())

print("\nSample data:\n")
print(df.head())
