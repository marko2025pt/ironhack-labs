# Lab: Evaluation Score Distribution Dashboard

**Student:** Marco  
**Bootcamp:** Ironhack AI Consulting Bootcamp  
**Date:** April 2026  
**Tool:** PowerBI Desktop

---

## Dashboard Overview

An interactive evaluation score dashboard built in PowerBI Desktop for non-technical
stakeholders. The dashboard visualizes LLM evaluation performance across 5 categories
and 4 model versions, allowing stakeholders to explore results through interactive filters
without requiring access to Python notebooks or raw data.

---

## Dashboard Contents

**3 Visualizations:**

1. **Score Distribution** — histogram showing the overall distribution of evaluation
   scores across all 4,489 records, binned in groups of 10
2. **Average Score by Category** — horizontal bar chart ranking the 5 evaluation
   categories by average score, making strengths and weaknesses immediately visible
3. **Performance by Model and Category** — grouped column chart comparing all 4 models
   across all 5 categories side by side

**2 Interactive Slicers:**
- **Model Version** — filter by claude-3-opus, gpt-3.5-turbo, gpt-4, gpt-4-turbo
- **Category** — filter by code, instruction_following, knowledge, reasoning, tool_calling

---

## Key Findings

- **instruction_following** is the strongest category (avg ~72/100)
- **knowledge** is second (avg ~66/100)
- **reasoning** is the weakest category (avg ~41/100)
- **All 4 models perform similarly** — no single model dominates across categories
- Scores follow a **bell-shaped distribution** centered around 40-60

---

## Communication Layer Principles Applied

- No statistical jargon (no p-values, confidence intervals, or standard deviations)
- Focus on business language: "performance", "strongest", "weakest", "improvement areas"
- Dashboard answers **"what"** (scores by category) and **"so what"** (reasoning needs work)
- Interactive filters allow stakeholders to explore without analyst support

---

## Repository Structure

    lab_evaluation_dashboard_marco/
    │
    ├── README.md                          # This file
    ├── data_source.md                     # Data source documentation
    ├── evaluation_score_dashboard.pbix    # PowerBI dashboard file
    ├── dashboard_screenshot.png           # Screenshot of final dashboard
    └── evaluation_data.csv                # Source data (generated)

---

## How to Open the Dashboard

1. Install PowerBI Desktop (free) from https://powerbi.microsoft.com/downloads
2. Open `evaluation_score_dashboard.pbix`
3. Use the slicers on the left to filter by model or category
4. All 3 charts update automatically when filters are applied

---

## Data Source

Synthetic evaluation data generated via `generate_evaluation_data.py`.
See `data_source.md` for details.