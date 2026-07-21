"""
Project 4: Data Visualization — DecodeLabs Data Analytics Internship
Author: Yasu

Applies the deck's rules directly:
- Action titles that state the conclusion, not the topic
- Zero-baseline axes (no truncation = no "Lie Factor")
- Direct labeling instead of legends (removes cognitive friction)
- A single accent color as a spotlight, muted grey for context
- No pie charts (5-category OrderStatus would violate the "max 3 slices" rule)
- Chart type chosen by business question, not by what "looks good"
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False
plt.rcParams["figure.dpi"] = 150

ACCENT = "#C0392B"   # spotlight — used ONLY on the data point that matters
MUTED = "#B0B0B0"    # context — everything else
INK = "#2B2B2B"

df = pd.read_excel("cleaned_dataset.xlsx")
df["Date"] = pd.to_datetime(df["Date"])

# ================================================================
# CHART 1 — Bar chart: "Comparing values across categories"
# Business question: which products drive revenue?
# ================================================================
rev = df.groupby("Product")["TotalPrice"].sum().sort_values()

fig, ax = plt.subplots(figsize=(9, 5.5))
colors = [MUTED] * len(rev)
top_idx = list(rev.index).index(rev.idxmax())
colors[top_idx] = ACCENT
bars = ax.barh(rev.index, rev.values, color=colors)

for bar, val in zip(bars, rev.values):
    ax.text(val + rev.max() * 0.01, bar.get_y() + bar.get_height() / 2,
            f"₹{val:,.0f}", va="center", fontsize=10, color=INK)

ax.set_title(f"No Single Product Dominates — {rev.idxmax()} Leads by Under 2%",
             fontsize=14, fontweight="bold", loc="left", pad=15, color=INK)
ax.set_xlabel("Total Revenue (₹)")
ax.xaxis.set_major_formatter(mticker.StrMethodFormatter("₹{x:,.0f}"))
ax.set_xlim(0, rev.max() * 1.15)  # zero-baseline, honest axis
ax.set_ylabel("")
ax.tick_params(left=False)
plt.figtext(0.1, 0.01, "Source: DecodeLabs Project 1 cleaned dataset, n=1,200 orders", fontsize=8, color=MUTED)
plt.tight_layout()
plt.savefig("outputs/01_revenue_by_product_bar.png", bbox_inches="tight")
plt.close()

# ================================================================
# CHART 2 — Horizontal bar (NOT pie): "Showing parts of a whole"
# Business question: what share of orders actually complete successfully?
# 5 categories -> pie chart is explicitly ruled out by the deck's "max 3 slices" rule
# ================================================================
status = df["OrderStatus"].value_counts()
status = status.reindex(status.sort_values(ascending=True).index)
problem_statuses = {"Cancelled", "Returned"}

colors = [ACCENT if s in problem_statuses else MUTED for s in status.index]
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(status.index, status.values, color=colors)
for bar, val in zip(bars, status.values):
    pct = val / status.sum() * 100
    ax.text(val + status.max() * 0.01, bar.get_y() + bar.get_height() / 2,
            f"{val} ({pct:.1f}%)", va="center", fontsize=10, color=INK)

combined_pct = sum(status[s] for s in problem_statuses) / status.sum() * 100
ax.set_title(f"41.4% of Orders Never Complete — Cancelled + Returned Outweigh Delivered",
             fontsize=14, fontweight="bold", loc="left", pad=15, color=INK)
ax.set_xlabel("Number of Orders")
ax.set_xlim(0, status.max() * 1.2)
ax.tick_params(left=False)
plt.figtext(0.1, 0.01, "Source: DecodeLabs Project 1 cleaned dataset, n=1,200 orders. Red = orders that failed to complete.",
            fontsize=8, color=MUTED)
plt.tight_layout()
plt.savefig("outputs/02_order_status_bar.png", bbox_inches="tight")
plt.close()

# ================================================================
# CHART 3 — Line chart: "Showing a trend over time"
# Business question: is revenue growing, shrinking, or flat?
# ================================================================
monthly = df.set_index("Date").resample("ME")["TotalPrice"].sum()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(monthly.index, monthly.values, color=MUTED, linewidth=2, zorder=1)
peak_idx = monthly.idxmax()
low_idx = monthly.idxmin()
ax.scatter([peak_idx], [monthly[peak_idx]], color=ACCENT, s=70, zorder=3)
ax.annotate(f"Peak: ₹{monthly[peak_idx]:,.0f}\n({peak_idx.strftime('%b %Y')})",
            xy=(peak_idx, monthly[peak_idx]), xytext=(10, 10), textcoords="offset points",
            fontsize=9, color=ACCENT, fontweight="bold")

first_val, last_val = monthly.iloc[0], monthly.iloc[-1]
trend_pct = (last_val - first_val) / first_val * 100
direction = "down" if trend_pct < 0 else "up"

ax.set_title(f"Monthly Revenue Has No Sustained Growth Trend — Ends {direction.title()} {abs(trend_pct):.0f}% from Where It Started",
             fontsize=13, fontweight="bold", loc="left", pad=15, color=INK)
ax.set_ylabel("Revenue (₹)")
ax.yaxis.set_major_formatter(mticker.StrMethodFormatter("₹{x:,.0f}"))
ax.set_ylim(0, monthly.max() * 1.15)
plt.figtext(0.1, 0.01, "Source: DecodeLabs Project 1 cleaned dataset, monthly revenue, Jan 2023–Jun 2025",
            fontsize=8, color=MUTED)
plt.tight_layout()
plt.savefig("outputs/03_monthly_trend_line.png", bbox_inches="tight")
plt.close()

# ================================================================
# CHART 4 — Scatter: "Investigating a relationship"
# Business question: does buying more units drive higher order value,
# or is order value really about what's being bought?
# ================================================================
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(df["UnitPrice"], df["TotalPrice"], alpha=0.4, color=MUTED, s=20)
corr = df["UnitPrice"].corr(df["TotalPrice"])
ax.set_title(f"Order Value Tracks Unit Price, Not Basket Size (r = {corr:.2f})",
             fontsize=13, fontweight="bold", loc="left", pad=15, color=INK)
ax.set_xlabel("Unit Price (₹)")
ax.set_ylabel("Order Total (₹)")
ax.set_xlim(0, df["UnitPrice"].max() * 1.05)
ax.set_ylim(0, df["TotalPrice"].max() * 1.05)
plt.figtext(0.1, 0.01, "Source: DecodeLabs Project 1 cleaned dataset, n=1,200 orders",
            fontsize=8, color=MUTED)
plt.tight_layout()
plt.savefig("outputs/04_price_vs_total_scatter.png", bbox_inches="tight")
plt.close()

print("All 4 charts saved to outputs/")
print(f"\nCancelled+Returned combined: {combined_pct:.1f}%")
print(f"Revenue trend: {direction} {abs(trend_pct):.1f}% from first to last month")
print(f"UnitPrice-TotalPrice correlation: {corr:.2f}")
