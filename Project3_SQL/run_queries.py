"""
Runs every query in queries.sql against decodelabs.db and writes the
results to query_results.md — so the SQL and its output live side by side
for anyone reviewing the portfolio.
"""

import sqlite3
import pandas as pd
import re

conn = sqlite3.connect("decodelabs.db")

with open("queries.sql") as f:
    content = f.read()

# Split into individual queries using the "-- N." comment markers
blocks = re.split(r"\n(?=-- \d+\.)", content)
blocks = [b.strip() for b in blocks if b.strip().startswith("--")]

with open("query_results.md", "w") as out:
    out.write("# Project 3 — SQL Query Results\n\n")
    out.write("Run against `decodelabs.db` (SQLite, built from the Project 1 cleaned dataset).\n\n")

    for block in blocks:
        lines = block.split("\n")
        title = lines[0].lstrip("- ").strip()
        sql = "\n".join(l for l in lines if not l.strip().startswith("--")).strip()
        if not sql:
            continue

        print(f"Running: {title}")
        df = pd.read_sql_query(sql, conn)

        out.write(f"## {title}\n\n")
        out.write("```sql\n" + sql + "\n```\n\n")
        out.write(df.to_markdown(index=False) + "\n\n")

conn.close()
print("\nDone. Results saved to query_results.md")
