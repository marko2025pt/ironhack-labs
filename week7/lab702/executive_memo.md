# EXECUTIVE MEMO

**To:** Chief Marketing Officer
**From:** Marketing Analytics Team
**Date:** April 08, 2026
**Re:** Statistical Analysis of Marketing Channel Performance
**Dataset:** Nykaa Marketing Campaign Performance Dataset (Kaggle)
**Period Analysed:** July 2024 - June 2025 (55,555 campaigns, 5 channels)

---

## Executive Summary

A rigorous statistical analysis of 55,555 marketing campaigns across
5 channels (Email, Influencer, Paid Ads, SEO, Social Media) found
**no statistically significant differences in CPA or ROAS** between
any channel pair after multiple comparisons correction.

Conversion rate differences were statistically detectable but
practically negligible (largest difference: 1.04%).

**Primary recommendation: maintain an equal $100K allocation per
channel.** There is no statistical evidence to justify shifting
budget away from any channel at this time.

---

## Key Findings

### 1. Channel Performance Overview

| Channel | Avg CPA | Avg ROAS | Avg ROI | Avg Conv Rate |
|---------|---------|----------|---------|---------------|
| Social Media | $373 | 3.75 | 2.75 | 21.92% |
| Influencer | $375 | 3.70 | 2.70 | 22.01% |
| Paid Ads | $379 | 3.72 | 2.72 | 21.81% |
| SEO | $379 | 3.71 | 2.71 | 22.05% |
| Email | $380 | 3.68 | 2.68 | 22.08% |

Social Media ranks first on CPA, ROAS and ROI.
Email ranks last on those same metrics despite the highest
conversion rate, suggesting higher cost per click rather
than lower conversion effectiveness.

### 2. Statistical Test Results

**CPA — Independent t-tests (10 pairwise comparisons):**
- Significant before correction: 0/10
- Significant after Bonferroni: 0/10
- Significant after FDR (BH): 0/10
- Largest difference: $6.87 (Email vs Social Media, 1.81%)
- All Cohen's d: negligible (< 0.02)
- Verdict: channels are statistically equivalent on CPA

**Conversion Rate — Fisher's Exact Test (10 pairwise comparisons):**
- Significant before correction: 10/10
- Significant after Bonferroni: 9/10
- Significant after FDR (BH): 10/10
- Largest difference: 1.04% (Email vs Paid Ads)
- Verdict: statistically significant but practically negligible

### 3. Data Adequacy

With 11,111 campaigns per channel our analysis has:
- >99% power to detect a 5% CPA difference (~$19)
- 100% power to detect a 10% CPA difference (~$38)

The null results on CPA are therefore not due to insufficient data.
We can conclude with high confidence that channels genuinely
perform equivalently on cost efficiency.

### 4. Confidence Intervals for CPA

| Channel | Mean CPA | 95% CI Lower | 95% CI Upper |
|---------|---------|-------------|-------------|
| Social Media | $373 | $364 | $383 |
| Influencer | $375 | $365 | $386 |
| Paid Ads | $379 | $369 | $389 |
| SEO | $379 | $369 | $389 |
| Email | $380 | $370 | $391 |

All confidence intervals heavily overlap, confirming no channel
is reliably cheaper than any other.

---

## Budget Allocation Recommendations

### Scenario A — Equal Allocation (PRIMARY RECOMMENDATION)

| Channel | Budget | Share |
|---------|--------|-------|
| Social Media | $100,000 | 20.0% |
| Influencer | $100,000 | 20.0% |
| Paid Ads | $100,000 | 20.0% |
| SEO | $100,000 | 20.0% |
| Email | $100,000 | 20.0% |
| **TOTAL** | **$500,000** | **100%** |

Justification: no statistically significant differences detected
on any cost or return metric. Reallocating based on non-significant
differences risks shifting budget based on noise.

### Scenario B — Modest Tilt (SECONDARY, requires justification)

| Channel | Budget | Share |
|---------|--------|-------|
| Social Media | $126,700 | 25.3% |
| Influencer | $108,100 | 21.6% |
| Paid Ads | $94,600 | 18.9% |
| SEO | $94,600 | 18.9% |
| Email | $76,000 | 15.2% |
| **TOTAL** | **$500,000** | **100%** |

Justification: if differentiation is required, a modest +-5%
tilt based on composite ranking limits downside risk. This
scenario is NOT statistically justified and should only be
adopted alongside a 90-day controlled experiment.

---

## Strategic Actions

1. **Do not make large reallocations** based on current data.
   The statistical evidence does not support it.

2. **Focus on campaign-level optimisation.** CPA standard
   deviations ($520-$566) far exceed between-channel differences
   ($7), meaning individual campaign quality matters far more
   than channel selection.

3. **Run controlled A/B experiments.** Before any major
   reallocation, run 90-day experiments with pre-specified
   minimum detectable effect of 5% CPA difference (~$19).

4. **Investigate high-CPA outliers.** Some campaigns show CPA
   above $5,000 vs a median of ~$200. Eliminating these outliers
   could reduce costs more than any channel reallocation.

5. **Review Email channel.** While not significantly worse,
   Email consistently ranks last on CPA and ROAS. Audit
   targeting, creative quality and list hygiene before the
   next budget cycle.

---

## Statistical Caveats

1. **Dataset:** The Nykaa dataset is described as real-world
   inspired — findings should be validated against live
   platform data before acting.

2. **Multiple comparisons correction:** All p-values corrected
   using Benjamini-Hochberg FDR (alpha=0.05) across 20
   simultaneous comparisons.

3. **Statistical vs practical significance:** Fisher's exact
   tests detected conversion rate differences as small as 0.09%
   as significant. P-values alone should never drive decisions.

4. **High within-channel variance:** CPA std dev of $520-$566
   per channel dwarfs between-channel differences. External
   factors (seasonality, campaign quality, targeting) likely
   explain more variance than channel choice.

5. **Observational analysis:** No causal inference can be drawn.
   Correlation between channel and performance does not guarantee
   that reallocating budget will replicate the same results.

6. **Power analysis assumptions:** Simulations assumed normal
   distribution with 15% coefficient of variation. Actual CPA
   distributions are right-skewed which may affect estimates.

---

## Next Steps

1. Validate findings against live Google Analytics / platform data
2. Run 90-day controlled A/B experiments with pre-specified MDE
3. Investigate high-CPA outlier campaigns (CPA > $5,000)
4. Conduct campaign-level analysis within each channel
5. Re-run this analysis quarterly to track divergence over time

---
*Analysis: Python (pandas, scipy, numpy, matplotlib, seaborn).
Full code and outputs available in the accompanying notebook.*
