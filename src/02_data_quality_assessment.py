import pandas as pd

file_path = "data/raw/h1b_employer_data_2026.csv"

df = pd.read_csv(
    file_path,
    encoding="utf-16",
    sep="\t",
    dtype=str
)

print("\n=== NULL VALUES ===")
print(df.isnull().sum())

print("\n=== NON-NUMERIC VALUES IN PETITION COLUMNS ===")

petition_columns = [
    "New Employment Approval",
    "New Employment Denial",
    "Continuation Approval",
    "Continuation Denial",
    "Change with Same Employer Approval",
    "Change with Same Employer Denial",
    "New Concurrent Approval",
    "New Concurrent Denial",
    "Change of Employer Approval",
    "Change of Employer Denial",
    "Amended Approval",
    "Amended Denial"
]

for column in petition_columns:
    numeric = pd.to_numeric(df[column], errors="coerce")

    bad_values = df.loc[
        numeric.isna() & df[column].notna(),
        column
    ].unique()

    print(f"\n{column}:")
    print(bad_values)


print("\n=== ROWS WITH MISSING EMPLOYER NAME ===")

print(
    df[df["Employer (Petitioner) Name"].isna()]
)