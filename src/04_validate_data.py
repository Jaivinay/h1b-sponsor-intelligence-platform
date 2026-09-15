import pandas as pd

# Load cleaned data
file_path = "data/processed/h1b_employer_data_2026_clean.csv"
df = pd.read_csv(file_path)

print("=== DATA VALIDATION ===")

# 1. Row count
assert len(df) == 49495, "Row count mismatch"
print("PASS: Row count =", len(df))

# 2. Column count
assert len(df.columns) == 20, "Column count mismatch"
print("PASS: Column count =", len(df.columns))

# 3. Duplicate rows
assert df.duplicated().sum() == 0, "Duplicate rows found"
print("PASS: No duplicate rows")

# 4. Fiscal year
assert set(df["fiscal_year"].unique()) == {2026}, "Unexpected fiscal year found"
print("PASS: Fiscal year = 2026")

# 5. Petition counts cannot be negative
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

assert (df[petition_columns] < 0).sum().sum() == 0, \
    "Negative petition counts found"

print("PASS: No negative petition counts")

# 6. Employer name cannot be null or blank
assert df["employer_petitioner_name"].notna().all(), \
    "Null employer names found"

assert (df["employer_petitioner_name"].str.strip() != "").all(), \
    "Blank employer names found"

print("PASS: No null/blank employer names")

print("\nALL DATA VALIDATION CHECKS PASSED")