"""
Project 2: Exploratory Data Analysis (EDA) — DecodeLabs Data Analytics Internship
Author: Yasu

Goal: analyze the cleaned Project 1 dataset to surface patterns, trends,
and outliers, then summarize what they mean for the business.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import numpy as np

sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 120

df = pd.read_excel("cleaned_dataset.xlsx")
df["Date"] = pd.to_datetime(df["Date"])
print(f"Loaded {df.shape[0]} rows, {df.shape[1]} columns\n")

# ---------------------------------------------------------------
# 1. DESCRIPTIVE STATISTICS
# ---------------------------------------------------------------
numeric_cols = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]
desc = df[numeric_cols].agg(["mean", "median", "std", "min", "max", "count"]).T
print("=== Descriptive Statistics ===")
print(desc.round(2))
desc.round(2).to_csv("outputs/descriptive_stats.csv")

# ---------------------------------------------------------------
# 2. DISTRIBUTION — is TotalPrice symmetric or skewed?
# ---------------------------------------------------------------
skew = df["TotalPrice"].skew()
print(f"\nTotalPrice skewness: {skew:.2f}")
# skew > 1 = strongly right-skewed -> median is the more honest "typical order"

fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df["TotalPrice"], bins=40, kde=True, color="#4A6B4A", ax=ax)
ax.axvline(df["TotalPrice"].mean(), color="#D97B4A", linestyle="--", label=f"Mean: ₹{df['TotalPrice'].mean():,.0f}")
ax.axvline(df["TotalPrice"].median(), color="#2C5F8A", linestyle="--", label=f"Median: ₹{df['TotalPrice'].median():,.0f}")
ax.set_title("Distribution of Order Value (TotalPrice)")
ax.set_xlabel("Order Value (₹)")
ax.legend()
plt.tight_layout()
plt.savefig("outputs/01_order_value_distribution.png")
plt.close()

# ---------------------------------------------------------------
# 3. OUTLIERS — IQR method on TotalPrice, per the project's boxplot slide
# ---------------------------------------------------------------
Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df["TotalPrice"] < lower) | (df["TotalPrice"] > upper)]
print(f"\nIQR bounds: [{lower:.2f}, {upper:.2f}]")
print(f"Outlier orders flagged: {len(outliers)} ({len(outliers)/len(df)*100:.1f}% of orders)")
outliers.to_csv("outputs/flagged_outliers.csv", index=False)

fig, ax = plt.subplots(figsize=(9, 5))
sns.boxplot(data=df, x="Product", y="TotalPrice", ax=ax, color="#8FBF8F")
ax.set_title("Order Value Spread by Product (outliers = dots beyond whiskers)")
ax.set_ylabel("Order Value (₹)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("outputs/02_boxplot_by_product.png")
plt.close()

# ---------------------------------------------------------------
# 4. TRENDS — revenue by product, monthly trend, order status mix
# ---------------------------------------------------------------
rev_by_product = df.groupby("Product")["TotalPrice"].agg(["sum", "count", "mean"]).sort_values("sum", ascending=False)
rev_by_product.columns = ["TotalRevenue", "OrderCount", "AvgOrderValue"]
print("\n=== Revenue by Product ===")
print(rev_by_product.round(2))
rev_by_product.round(2).to_csv("outputs/revenue_by_product.csv")

fig, ax = plt.subplots(figsize=(8, 5))
rev_by_product["TotalRevenue"].sort_values().plot(kind="barh", color="#4A6B4A", ax=ax)
ax.set_title("Total Revenue by Product")
ax.set_xlabel("Revenue (₹)")
ax.xaxis.set_major_formatter(mticker.StrMethodFormatter("₹{x:,.0f}"))
plt.tight_layout()
plt.savefig("outputs/03_revenue_by_product.png")
plt.close()

monthly = df.set_index("Date").resample("ME")["TotalPrice"].sum()
fig, ax = plt.subplots(figsize=(9, 5))
monthly.plot(marker="o", color="#2C5F8A", ax=ax)
ax.set_title("Monthly Revenue Trend")
ax.set_ylabel("Revenue (₹)")
ax.yaxis.set_major_formatter(mticker.StrMethodFormatter("₹{x:,.0f}"))
plt.tight_layout()
plt.savefig("outputs/04_monthly_trend.png")
plt.close()

status_counts = df["OrderStatus"].value_counts()
print("\n=== Order Status Breakdown ===")
print(status_counts)
fig, ax = plt.subplots(figsize=(7, 5))
status_counts.plot(kind="bar", color="#D97B4A", ax=ax)
ax.set_title("Orders by Status")
ax.set_ylabel("Number of Orders")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/05_order_status.png")
plt.close()

cancel_return_rate = (status_counts.get("Cancelled", 0) + status_counts.get("Returned", 0)) / len(df) * 100
print(f"\nCombined Cancelled + Returned rate: {cancel_return_rate:.1f}%")

# ---------------------------------------------------------------
# 5. CORRELATION ANALYSIS
# ---------------------------------------------------------------
corr = df[numeric_cols].corr()
print("\n=== Correlation Matrix ===")
print(corr.round(2))

fig, ax = plt.subplots(figsize=(7, 6))
sns.heatmap(corr, annot=True, cmap="RdBu_r", center=0, vmin=-1, vmax=1, ax=ax)
ax.set_title("Correlation Between Numeric Fields")
plt.tight_layout()
plt.savefig("outputs/06_correlation_heatmap.png")
plt.close()

# ---------------------------------------------------------------
# 6. PAYMENT METHOD x AVG ORDER VALUE
# ---------------------------------------------------------------
payment_summary = df.groupby("PaymentMethod")["TotalPrice"].agg(["mean", "count"]).sort_values("mean", ascending=False)
print("\n=== Avg Order Value by Payment Method ===")
print(payment_summary.round(2))

print("\nAll charts saved to project2/outputs/")
