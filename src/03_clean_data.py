import pandas as pd

# File paths
input_file = "data/raw/h1b_employer_data_2026.csv"
output_file = "data/processed/h1b_employer_data_2026_clean.csv"

# Load raw data
df = pd.read_csv(
    input_file,
    encoding="utf-16",
    sep="\t",
    dtype=str
)

# 1. Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r"[^a-z0-9]+", "_", regex=True)
    .str.strip("_")
)

# 2. Convert petition count columns to integers
petition_columns = [
    "new_employment_approval",
    "new_employment_denial",
    "continuation_approval",
    "continuation_denial",
    "change_with_same_employer_approval",
    "change_with_same_employer_denial",
    "new_concurrent_approval",
    "new_concurrent_denial",
    "change_of_employer_approval",
    "change_of_employer_denial",
    "amended_approval",
    "amended_denial"
]

for column in petition_columns:
    df[column] = (
        df[column]
        .str.replace(",", "", regex=False)
    )

    df[column] = pd.to_numeric(
        df[column],
        errors="raise"
    ).astype("int64")

# 3. Convert fiscal year to integer
df["fiscal_year"] = pd.to_numeric(
    df["fiscal_year"],
    errors="raise"
).astype("int64")

# 4. Keep identifier/code columns as strings
identifier_columns = [
    "line_by_line",
    "tax_id",
    "industry_naics_code",
    "petitioner_zip_code"
]

for column in identifier_columns:
    df[column] = df[column].astype("string")

# 5. Trim whitespace from text columns
text_columns = [
    "employer_petitioner_name",
    "petitioner_city",
    "petitioner_state"
]

for column in text_columns:
    df[column] = df[column].str.strip()

# 6. Handle missing values
df["employer_petitioner_name"] = (
    df["employer_petitioner_name"]
    .fillna("UNKNOWN")
)

df["industry_naics_code"] = (
    df["industry_naics_code"]
    .fillna("UNKNOWN")
)

df["petitioner_city"] = (
    df["petitioner_city"]
    .fillna("UNKNOWN")
)

df["petitioner_state"] = (
    df["petitioner_state"]
    .fillna("UNKNOWN")
)

# Keep tax_id and petitioner_zip_code as null if missing

# 7. Save cleaned dataset
df.to_csv(
    output_file,
    index=False
)

# 8. Verification
print("Cleaned file saved to:")
print(output_file)

print("\nFinal shape:")
print(df.shape)

print("\nFinal data types:")
print(df.dtypes)

print("\nMissing values after cleaning:")
print(df.isnull().sum())