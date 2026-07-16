# Project 2 — Exploratory Data Analysis
**DecodeLabs Data Analytics Internship | Yasu | Week 3**

## 1. Problem Statement
Now that the dataset is clean (Project 1), the question is: what is it actually
telling us? This analysis digs into the 1,200-order e-commerce dataset to find
the patterns, trends, and outliers that matter for the business — not just to
report numbers, but to explain what they mean.

## 2. Methodology
Built on the cleaned dataset from Project 1 (CouponCode nulls resolved, dates
standardized). Used Python (pandas, seaborn, matplotlib) to:
- Calculate descriptive statistics (mean, median, std) for all numeric fields
- Test the shape of the order-value distribution (skew check)
- Flag outliers using the IQR method (Q1 - 1.5×IQR to Q3 + 1.5×IQR)
- Break down revenue by product, by month, and by payment method
- Run a correlation analysis across Quantity, UnitPrice, ItemsInCart, and TotalPrice

## 3. Key Findings

**Order values are moderately skewed, so the median tells the truer story.**
Mean order value is ₹1,053.97, but the median is ₹823.62 — a meaningful gap
(skewness = 0.89). A handful of high-value orders are pulling the average up.
For "typical customer" reporting, lead with the median.

**Only 8 orders (0.7%) are statistical outliers.** Using the IQR method, order
values stay tightly within [₹0, ₹3,330]. This is a clean revenue base — no
runaway data entry errors distorting the picture.

**Revenue is nearly evenly split across products, with Chairs and Printers
narrowly on top** (₹195.6K and ₹195.6K respectively), followed closely by
Laptops (₹192.1K). No single product dominates — this is a diversified
catalog, not a one-hit business.

**The standout number: 41.4% of all orders are Cancelled or Returned.**
Cancelled (250) and Returned (247) orders combined outnumber Delivered orders
(231) and Shipped (235) combined. This is the single most business-critical
finding in the dataset — worth flagging to any stakeholder before anything else.

**UnitPrice and Quantity barely move together (r = 0.01)** — customers aren't
buying more units of cheaper items or fewer of expensive ones in any
predictable way. **TotalPrice correlates most with UnitPrice (r = 0.72)**,
confirming that order value is driven more by what customers buy than how
many units they order.

**Credit Card orders have the highest average value (₹1,127.55)**; Debit Card
the lowest (₹1,001.56) — a ₹126 spread across payment methods.

## 4. Recommendations
- **Investigate the 41.4% cancel/return rate as priority #1.** That's not a
  rounding error — it's a structural issue worth a root-cause analysis
  (checkout friction? fulfillment delays? product mismatch?).
- **Report typical order value using the median (₹823.62), not the mean**,
  to avoid overstating what a "normal" customer spends.
- **No need to chase outliers** — at 0.7%, they're not distorting revenue
  reporting and don't need special handling before further analysis.
- **Product strategy can stay diversified** — revenue isn't overly reliant
  on any single SKU, which reduces concentration risk.

---
*All supporting charts are in `/outputs`. Full code in `eda_analysis.py`.*
