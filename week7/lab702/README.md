# Lab: Marketing Channel ROI Comparison
## Statistical Analysis for Budget Allocation

---

## Overview

This lab performs a statistically rigorous analysis of marketing
channel performance to guide the allocation of a $500K monthly
budget across 5 channels. The analysis follows a full statistical
pipeline: data exploration, pairwise hypothesis testing, multiple
comparisons correction, power analysis, and business recommendations.

---

## Dataset

**Name:** Nykaa Marketing Campaign Performance Dataset
**Source:** Kaggle
**File:** nykaa_campaign_data.csv
**Size:** 55,555 campaigns x 16 columns
**Period:** July 2024 - June 2025
**Channels:** Email, Influencer, Paid Ads, SEO, Social Media (~11,000
campaigns per channel)

A structured, real-world inspired e-commerce marketing campaign
dataset designed for ROI analysis, performance optimization, and
predictive modeling.

---

## Key Findings

1. **No significant CPA differences:** 0/10 channel pairs showed
   statistically significant CPA differences after Bonferroni and
   FDR correction. All Cohen's d values were negligible (< 0.02).

2. **Negligible conversion rate differences:** All 10 channel pairs
   showed statistically significant conversion rate differences after
   FDR correction, but the largest difference was only 1.04% —
   practically meaningless.

3. **Data is not the limiting factor:** With 11,111 campaigns per
   channel, the analysis has >99% power to detect a 5% CPA
   difference. Null results reflect genuine channel equivalence,
   not insufficient data.

4. **Within-channel variance dominates:** CPA standard deviations
   of $520-$566 per channel dwarf between-channel differences of
   just $7, suggesting campaign-level quality matters far more
   than channel selection.

5. **Primary recommendation: equal allocation.** $100K per channel
   is the statistically defensible recommendation. A secondary
   modest tilt scenario (Social Media 25.3%, Email 15.2%) is
   provided if differentiation is required, with appropriate caveats.

---

## How to Run

1. Install dependencies:
   ```
   pip install numpy pandas matplotlib seaborn scipy
   ```

2. Place `nykaa_campaign_data.csv` in the same folder as the notebook

3. Open and run `data_exploration.ipynb` from top to bottom
   - All cells are sequential and must be run in order
   - Power analysis cells (~30 seconds to run)

4. All output files are saved automatically to the same folder

---

## File Structure

```
LAB702/
├── data_exploration.ipynb        # Main analysis notebook
├── nykaa_campaign_data.csv       # Raw dataset
├── marketing_data.csv            # Cleaned dataset
├── executive_memo.md             # Business recommendations memo
├── README.md                     # This file
├── group_metrics_overview.png    # KPI bar charts
├── group_distributions.png       # Box plots by channel
├── cpa_comparison_heatmap.png    # P-value heatmap (CPA)
├── roas_comparison_heatmap.png   # P-value heatmap (ROAS)
├── rate_comparison.png           # Conversion rate comparison
├── correction_comparison.png     # Multiple comparisons correction
├── power_analysis_cpa.png        # Power curves
├── cpa_confidence_intervals.png  # Bootstrap confidence intervals
└── budget_allocation.png         # Budget allocation scenarios
```

---

## Assumptions & Notes

- **Derived metrics:** Spend = Acquisition_Cost x Conversions;
  ROAS = Revenue / Spend; Conv_Rate = Conversions / Clicks;
  CTR = Clicks / Impressions
- **Statistical threshold:** alpha = 0.05 throughout
- **Multiple comparisons:** Benjamini-Hochberg FDR applied to all
  pairwise comparisons (20 total)
- **Power simulation:** 1,000 simulations per condition, normal
  distribution assumed with 15% coefficient of variation
- **Bootstrap CIs:** 1,000 resamples, 95% confidence level
- **Budget constraints:** Scenario B allocations constrained to
  +/-5% around equal share (20%) per channel

---

## Statistical Methods Used

| Method | Purpose |
|--------|---------|
| Independent t-test | Compare CPA and ROAS between channel pairs |
| Fisher's exact test | Compare binary conversion outcomes |
| Cohen's d | Measure practical effect size |
| Bonferroni correction | Control family-wise error rate |
| Benjamini-Hochberg FDR | Control false discovery rate |
| Empirical power simulation | Assess data adequacy |
| Bootstrap confidence intervals | Quantify CPA uncertainty |
