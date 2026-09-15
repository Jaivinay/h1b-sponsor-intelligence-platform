-- ============================================================
-- H1B Sponsor Intelligence Platform
-- Snowflake Infrastructure Setup
-- ============================================================


-- 1. Create project database
CREATE DATABASE IF NOT EXISTS H1B_SPONSOR_INTELLIGENCE;


-- 2. Create RAW schema
CREATE SCHEMA IF NOT EXISTS H1B_SPONSOR_INTELLIGENCE.RAW;


-- 3. Create SILVER schema
CREATE SCHEMA IF NOT EXISTS H1B_SPONSOR_INTELLIGENCE.SILVER;


-- 4. Create GOLD schema
CREATE SCHEMA IF NOT EXISTS H1B_SPONSOR_INTELLIGENCE.GOLD;


-- 5. Define source file format
-- USCIS source file is UTF-16LE and tab-delimited
CREATE OR REPLACE FILE FORMAT
    H1B_SPONSOR_INTELLIGENCE.RAW.H1B_CSV_FORMAT
    TYPE = 'CSV'
    FIELD_DELIMITER = '\t'
    SKIP_HEADER = 1
    ENCODING = 'UTF16LE'
    EMPTY_FIELD_AS_NULL = TRUE;


-- 6. Create secure AWS S3 storage integration
CREATE OR REPLACE STORAGE INTEGRATION H1B_S3_INTEGRATION
    TYPE = EXTERNAL_STAGE
    STORAGE_PROVIDER = 'S3'
    ENABLED = TRUE
    STORAGE_AWS_ROLE_ARN =
        'arn:aws:iam::927026871352:role/h1b-snowflake-s3-role'
    STORAGE_ALLOWED_LOCATIONS =
        ('s3://h1b-sponsor-intelligence-jaivinay/raw/');


-- 7. Create Snowflake external stage pointing to S3 RAW
CREATE OR REPLACE STAGE
    H1B_SPONSOR_INTELLIGENCE.RAW.H1B_S3_STAGE
    URL = 's3://h1b-sponsor-intelligence-jaivinay/raw/'
    STORAGE_INTEGRATION = H1B_S3_INTEGRATION
    FILE_FORMAT =
        H1B_SPONSOR_INTELLIGENCE.RAW.H1B_CSV_FORMAT;
