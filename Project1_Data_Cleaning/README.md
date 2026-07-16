# Project 1 — Data Cleaning & Preparation
**DecodeLabs Data Analytics Internship, Batch 2026**

## What this is
Audits and cleans the raw 1,200-row e-commerce dataset: checks for missing
values, duplicate IDs, duplicate rows, bad date formats, and calculation
errors, then documents every finding in a change log.

## Files
| File | What it is |
|---|---|
| `raw_dataset.xlsx` | Original, untouched dataset |
| `DecodeLabs_Project1_Cleaned_Excel.xlsx` | Cleaned via Excel workflow — includes `Raw_Data`, `Cleaned_Data`, and `Change_Log` sheets |
| `DecodeLabs_Project1_Cleaned_Pandas.xlsx` | Same cleaning, done via the Python script below |
| `clean_data_pandas.py` | Python/pandas cleaning script (audit → clean → verify) |

## How to run it
```bash
pip install pandas openpyxl
python3 clean_data_pandas.py
```

## Key finding
The dataset was largely clean already — 0 duplicate IDs, 0 bad dates, 0
calculation mismatches. The one real issue: 309 blank `CouponCode` values
(25.75% of rows), which represent "no coupon used," not missing data.
Imputed as `"NONE"` rather than deleted, to avoid losing a quarter of the
dataset. Full audit trail in the `Change_Log` sheet of the Excel file.
