# H1B Sponsor Intelligence Platform

An end-to-end data engineering project for profiling, cleaning, validating, and loading FY2026 H-1B employer sponsorship data into Snowflake.

The project combines a local Python data quality workflow with a Snowflake RAW-to-SILVER pipeline so employer-level sponsorship data can be prepared for analytics.

## Project Goals

- Profile raw H-1B employer data.
- Identify missing values, duplicates, and invalid petition count fields.
- Clean and standardize the source dataset.
- Validate the processed output before warehouse loading.
- Create Snowflake RAW and SILVER layers for downstream analysis.

## Repository Structure

```text
.
|-- data
|   |-- raw
|   |   `-- h1b_employer_data_2026.csv
|   `-- processed
|       `-- h1b_employer_data_2026_clean.csv
|-- sql
|   |-- 01_setup
|   |   `-- 01_snowflake_setup.sql
|   |-- 02_raw
|   |   `-- 01_create_and_load_raw.sql
|   |-- 03_silver
|   |   `-- 01_create_silver.sql
|   |-- 04_gold
|   |   `-- 01_create_gold_views.sql
|   `-- 05_validation
|       `-- 01_data_quality_checks.sql
|-- src
|   |-- 01_data_profiling.py
|   |-- 02_data_quality_assessment.py
|   |-- 03_clean_data.py
|   `-- 04_validate_data.py
|-- requirements.txt
`-- README.md
```

## Tech Stack

- Python
- pandas
- NumPy
- Snowflake
- AWS S3 external stage
- SQL

## Dataset

The raw dataset is stored at:

```text
data/raw/h1b_employer_data_2026.csv
```

The cleaned dataset is written to:

```text
data/processed/h1b_employer_data_2026_clean.csv
```

Current validation expects:

- 49,495 rows
- 20 columns
- Fiscal year 2026
- No duplicate rows
- No negative petition counts
- No null or blank employer names

## Local Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Python Data Workflow

Run the scripts from the project root.

Profile the raw data:

```bash
python src/01_data_profiling.py
```

Assess data quality issues:

```bash
python src/02_data_quality_assessment.py
```

Clean and standardize the raw file:

```bash
python src/03_clean_data.py
```

Validate the cleaned dataset:

```bash
python src/04_validate_data.py
```

Expected final validation message:

```text
ALL DATA VALIDATION CHECKS PASSED
```

## Cleaning Logic

The cleaning script performs the following transformations:

- Standardizes column names to lowercase snake case.
- Converts petition count columns to integers.
- Converts fiscal year to an integer.
- Keeps identifier fields such as tax ID, NAICS code, and ZIP code as strings.
- Trims whitespace from employer, city, and state fields.
- Fills missing employer, industry, city, and state values with `UNKNOWN`.
- Preserves missing tax ID and ZIP code values as null.

## Snowflake Pipeline

The SQL scripts create a simple warehouse pipeline:

1. Create the `H1B_SPONSOR_INTELLIGENCE` database.
2. Create `RAW`, `SILVER`, and `GOLD` schemas.
3. Define a UTF-16LE tab-delimited file format.
4. Create an AWS S3 storage integration and external stage.
5. Load source data into `RAW.H1B_EMPLOYER_RAW`.
6. Transform RAW data into `SILVER.H1B_EMPLOYER_CLEAN`.
7. Create business-ready GOLD analytics views.
8. Run data quality checks against RAW, SILVER, and GOLD objects.

Run the Snowflake scripts in this order:

```text
sql/01_setup/01_snowflake_setup.sql
sql/02_raw/01_create_and_load_raw.sql
sql/03_silver/01_create_silver.sql
sql/04_gold/01_create_gold_views.sql
sql/05_validation/01_data_quality_checks.sql
```

## Validation Checks

The project validates:

- RAW row counts.
- Key field completeness.
- Source line identifier uniqueness.
- SILVER row counts.
- Missing employer names.
- Numeric petition count fields.
- Fiscal year distribution.
- GOLD layer row counts and aggregate totals.

## Notes

- The raw source file is UTF-16 and tab-delimited.
- Python scripts should be run from the repository root so relative file paths resolve correctly.
- Snowflake loading expects the raw file to be available in the configured S3 stage.
