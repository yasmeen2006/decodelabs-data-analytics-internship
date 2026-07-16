# Project 3 — SQL Data Analysis
**DecodeLabs Data Analytics Internship, Batch 2026**

## What this is
11 SQL queries against the cleaned Project 1 dataset (loaded into SQLite),
covering SELECT, WHERE, ORDER BY, GROUP BY, HAVING, subqueries, and
aggregations (COUNT, SUM, AVG) — plus two bonus queries (percentage
contribution, monthly trend) to go past the minimum requirement.

## Files
| File | What it is |
|---|---|
| `queries.sql` | All 11 queries, commented |
| `run_queries.py` | Runs every query against `decodelabs.db`, writes results |
| `query_results.md` | Query + output side by side, for anyone reviewing without a DB tool |
| `decodelabs.db` | SQLite database (built from the Project 1 cleaned dataset) |

## How to run it
```bash
pip install pandas tabulate
python3 run_queries.py
```

## Key finding
Cancelled orders that exceed the average order value (Query 6) are the
highest-value orders being lost — worth flagging alongside Project 2's
41.4% cancel/return rate finding.
