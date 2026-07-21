# Project 4 — Data Visualization (Optional Mastery Phase)
**DecodeLabs Data Analytics Internship, Batch 2026**

## What this is
Takes the Project 2 finding (41.4% of orders are Cancelled or Returned) and
turns it into boardroom-ready visual storytelling — applying the deck's
rules directly rather than just making charts that "look nice."

## Design rules applied (from the Project 4 brief)
- **Chart type chosen by business question, not by appearance** — bar for
  comparing categories, line for a trend over time, scatter for a
  relationship. See the Chart Selection Matrix reasoning in each script comment.
- **No pie charts.** `OrderStatus` has 5 categories — the deck's own rule
  ("never use a pie chart with more than 3 slices") rules it out. Used a
  horizontal bar chart instead.
- **Zero-baseline axes** on every chart — no truncated Y-axis, no
  "Lie Factor" distortion (Tufte).
- **Direct labeling instead of legends** — every bar and key point is
  labeled on the chart itself, so no one has to cross-reference a legend.
- **Color as a spotlight, not decoration** — one accent color (`#C0392B`)
  marks only the data that matters (Cancelled/Returned, the top-revenue
  product, the peak month). Everything else is muted grey.
- **Action titles** — every chart title states the conclusion
  ("41.4% of Orders Never Complete"), not the topic ("Order Status Breakdown").
- **SCR narrative structure** in the slide deck — Situation (the dataset
  looks healthy) → Complication (41.4% of orders fail) → Resolution
  (three concrete next steps).

## Files
| File | What it is |
|---|---|
| `Project4_Boardroom_Slide.pptx` | 4-slide SCR-structured deck — the actual "boardroom-ready" deliverable |
| `visualizations.py` | Script that generates all 4 supporting charts |
| `outputs/` | The 4 charts: bar (category comparison), horizontal bar (composition, chosen over pie), line (trend), scatter (relationship) |
| `cleaned_dataset.xlsx` | Input data (from Project 1) |

## How to run it
```bash
pip install pandas matplotlib openpyxl
python3 visualizations.py
```
The `.pptx` was built separately with `pptxgenjs` (Node.js) — the charts
it embeds are already generated in `outputs/`, so you don't need Node to
view the deck, only to regenerate it.

## Exploratory vs. Explanatory — why there are two "layers" here
Per the deck's own distinction: the 4 PNGs in `outputs/` are closer to
**exploratory** analysis (multiple charts, each testing one question). The
`.pptx` deck is the **explanatory** layer — one message per slide, built
for someone who will only look at it for 5 seconds and needs to walk away
knowing what to do next.
