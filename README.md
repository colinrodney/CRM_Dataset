# Project: Customer Relationship Management (CRM) Data Cleansing & Standardization

## Problem
The original dataset contained formatting / inconsistency issues such as blank/null/ N/A field values for email addresses, phone numbers, city names, registration dates  which made it unreliable for reporting, including:
- Duplicate customer records
- Inconsistent name and address formatting
- Missing values in key fields
- Inconsistent phone number formatting

These issues caused inaccurate reporting and difficulty matching records across systems.

## Objective
Clean and standardize the dataset so it is:
- Deduplicated
- Consistently formatted
- Validated against business rules
- Ready for analytics and downstream processing

## Dataset
- Rows: 500
- Columns: 6
- Source Type: CSV / Exported CRM file

_(Only sample records are shared for privacy.)_

## Approach & Cleaning Steps
1. **Profiling & Assessment**
   - Identified null fields, type mismatches, formatting issues

2. **Standardization Rules Applied**
   - Name casing normalized
   - Phone numbers converted to E.164 format *
   - Dates converted to ISO format *
   - Trimming whitespace and special characters *

3. **Deduplication Logic**
   - Unique keys defined using: [rule]
   - Fuzzy matching threshold: [if applicable] *

4. **Validation & QA**
   - Row counts before vs after
   - Spot-checks for edge cases
   - Business rule checks 

## Before vs After (Samples) *
- `/before/sample_raw.csv`
- `/after/sample_clean.csv`

## Tools Used
- Python (pandas)
- Jupyter Notebook / VS Code
- Excel (for validation review)

## Outcome / Impact
- Reduced duplicate records by **X%**
- Improved data consistency for reporting
- Eliminated formatting errors that previously caused failures

## Repository Contents
- `/notebooks` — walkthrough & logic explanation
- `/before` — anonymized raw sample
- `/after` — cleaned sample output
- `/scripts` (optional) — reusable cleaning functions

