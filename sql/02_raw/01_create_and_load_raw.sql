-- ============================================================
-- H1B Sponsor Intelligence Platform
-- RAW Layer: Create and Load Source Data
-- ============================================================


-- 1. Create RAW table
CREATE TABLE IF NOT EXISTS
    H1B_SPONSOR_INTELLIGENCE.RAW.H1B_EMPLOYER_RAW (

    LINE_BY_LINE                         VARCHAR,
    FISCAL_YEAR                          VARCHAR,
    EMPLOYER_NAME                        VARCHAR,
    TAX_ID                               VARCHAR,
    INDUSTRY_NAICS_CODE                  VARCHAR,
    PETITIONER_CITY                      VARCHAR,
    PETITIONER_STATE                     VARCHAR,
    PETITIONER_ZIP_CODE                  VARCHAR,
    NEW_EMPLOYMENT_APPROVAL              VARCHAR,
    NEW_EMPLOYMENT_DENIAL                VARCHAR,
    CONTINUATION_APPROVAL                VARCHAR,
    CONTINUATION_DENIAL                  VARCHAR,
    CHANGE_SAME_EMPLOYER_APPROVAL        VARCHAR,
    CHANGE_SAME_EMPLOYER_DENIAL          VARCHAR,
    NEW_CONCURRENT_APPROVAL              VARCHAR,
    NEW_CONCURRENT_DENIAL                VARCHAR,
    CHANGE_EMPLOYER_APPROVAL             VARCHAR,
    CHANGE_EMPLOYER_DENIAL               VARCHAR,
    AMENDED_APPROVAL                     VARCHAR,
    AMENDED_DENIAL                       VARCHAR
);


-- 2. Load source data from S3 stage into RAW table
COPY INTO H1B_SPONSOR_INTELLIGENCE.RAW.H1B_EMPLOYER_RAW
FROM @H1B_SPONSOR_INTELLIGENCE.RAW.H1B_S3_STAGE
FILE_FORMAT = (
    FORMAT_NAME = 'H1B_SPONSOR_INTELLIGENCE.RAW.H1B_CSV_FORMAT'
)
MATCH_BY_COLUMN_NAME = NONE;