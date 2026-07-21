# DecodeLabs Data Analytics Internship — Batch 2026

**Intern:** Yasmeen
**Duration:** July 5 – August 5, 2026 (Remote)
**Track:** Data Analytics

This repo documents my Week 1–4 project submissions for the DecodeLabs
Data Analytics Internship: cleaning a raw e-commerce dataset, exploring it
for patterns and trends, querying it with SQL, and turning the findings
into boardroom-ready visuals. Each project builds on the one before it —
same dataset throughout, so the whole thing reads as one connected
analysis rather than four separate exercises.

## Projects

### [Project 1 — Data Cleaning & Preparation](./Project1_Data_Cleaning)
Audited a 1,200-row raw dataset for missing values, duplicates, and
formatting issues. Found the dataset was largely clean already — the one
real issue was 309 blank `CouponCode` values (25.75% of rows), which
turned out to mean "no coupon used," not missing data. Imputed rather than
deleted, to avoid losing a quarter of the dataset. Full audit trail in the
change log.

**Tools:** Excel (Power Query-style cleaning) + Python (pandas)

### [Project 2 — Exploratory Data Analysis](./Project2_EDA)
Analyzed the cleaned dataset for distribution shape, outliers, revenue
trends, and correlations. Headline finding: **41.4% of all orders are
Cancelled or Returned** — the single most business-critical number in the
dataset, and the one I'd lead with in any stakeholder conversation.

**Tools:** Python (pandas, seaborn, matplotlib)

### [Project 3 — SQL Data Analysis](./Project3_SQL)
11 SQL queries against the cleaned dataset (loaded into SQLite) — SELECT,
WHERE, ORDER BY, GROUP BY, HAVING, subqueries, and aggregations. Went past
the minimum requirement with two extra queries: percentage-of-revenue
contribution by product, and a monthly revenue trend.

**Tools:** SQL (SQLite) + Python (for running/exporting query results)

### [Project 4 — Data Visualization](./Project4_Visualization)
Optional mastery phase — took the 41.4% cancel/return finding from
Project 2 and turned it into a 4-slide boardroom-ready deck, built on the
Situation-Complication-Resolution framework. Applied the deck's design
rules directly: zero-baseline axes, direct labeling instead of legends,
action titles that state the conclusion, and no pie charts (5-category
data violates the "max 3 slices" readability rule, so a sorted horizontal
bar was used instead).

**Tools:** Python (matplotlib) for charts, PowerPoint (pptxgenjs) for the deck

## Key takeaway across all four projects
The dataset's biggest issue isn't in the data quality — it's in the
business outcome. Nearly 4 in 10 orders don't complete successfully
(Cancelled + Returned). That single thread ties all four projects
together: clean the data, find the pattern, query it to confirm exactly
where the losses are concentrated, then package the finding so a
decision-maker can act on it in five seconds.

## Repo structure
```
decodelabs-data-analytics-internship/
├── README.md                       ← you are here
├── Project1_Data_Cleaning/
├── Project2_EDA/
├── Project3_SQL/
└── Project4_Visualization/
```

Each project folder has its own README with setup instructions and a
breakdown of every file inside it.

---
📞 +91 89330 06408 | 🌐 [decodelabs.tech](https://www.decodelabs.tech)
