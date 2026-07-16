"""
Project 1: Data Cleaning & Preparation — DecodeLabs Data Analytics Internship
Author: Yasu
Approach: pandas (Python)

This script performs the same audit + cleaning as the Excel workbook,
so you can compare both workflows.
"""

import pandas as pd

# 1. LOAD RAW DATA
df = pd.read_excel("Dataset_for_Data_Analytics.xlsx")
print(f"Loaded {df.shape[0]} rows, {df.shape[1]} columns\n")

# 2. AUDIT — always audit before touching anything
print("=== AUDIT REPORT ===")
print("Missing values per column:")
print(df.isnull().sum()[df.isnull().sum() > 0])

dup_ids = df["OrderID"].duplicated().sum()
dup_rows = df.duplicated().sum()
print(f"\nDuplicate OrderIDs: {dup_ids}")
print(f"Fully duplicate rows: {dup_rows}")

calc_total = (df["Quantity"] * df["UnitPrice"]).round(2)
mismatches = (calc_total - df["TotalPrice"]).abs().gt(0.01).sum()
print(f"TotalPrice calculation mismatches: {mismatches}")

bad_numeric = ((df["Quantity"] <= 0) | (df["UnitPrice"] <= 0)).sum()
print(f"Negative/zero Quantity or UnitPrice: {bad_numeric}")

# 3. CLEAN
df_clean = df.copy()

# CR001 — CouponCode blanks mean "no coupon used", not missing data.
# Impute rather than delete (deleting would drop 309 valid rows / ~26% of data).
df_clean["CouponCode"] = df_clean["CouponCode"].fillna("NONE")

# CR004 — Standardize date format to ISO 8601
df_clean["Date"] = pd.to_datetime(df_clean["Date"]).dt.strftime("%Y-%m-%d")

# 4. VERIFY — the project's "0% error" gate before handing off
assert df_clean["OrderID"].duplicated().sum() == 0, "Duplicate OrderIDs found!"
assert df_clean["CouponCode"].isnull().sum() == 0, "CouponCode still has nulls!"
print("\nVerification passed: 0 duplicate IDs, 0 remaining nulls in CouponCode.")

# 5. SAVE
df_clean.to_excel("cleaned_data_pandas.xlsx", index=False)
print("\nSaved cleaned_data_pandas.xlsx")
