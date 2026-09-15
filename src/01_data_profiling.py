import pandas as pd

file_path = "data/raw/h1b_employer_data_2026.csv"

df = pd.read_csv(file_path, encoding="utf-16", sep="\t")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nBasic Statistics:")
print(df.describe(include="all"))