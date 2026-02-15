# Prompt Engineering Lab – Consistency and Reliability Analysis
Marco Martins

## Overview

This project was developed as part of the Prompt Engineering Lab (Week 2 – Lab 201).

The objective was to diagnose, improve, and systematically evaluate prompt reliability across three AI task types:

1. Sentiment Analysis (Classification)
2. Product Description Generation (Creative Generation)
3. Data Extraction (Structured Output)

The notebook serves as both the implementation and the analytical report.  
An exported HTML version is included for easier review with outputs rendered.

---

## Project Structure

week2/lab201/
│
├── prompt_engineering_lab.ipynb # Main notebook (code + report)
├── prompt_engineering_lab.html # Rendered HTML version (includes outputs)
│
├── sentiment_v1_results.txt
├── sentiment_v2_results.txt
├── sentiment_v3_results.txt
│
├── product_v1_results.txt
├── product_v2_results.txt
├── product_v3_results.txt
│
├── extraction_v1_results.txt
├── extraction_v2_results.txt
├── extraction_v3_results.txt
|
└──.vscode/


### Notes

- The `.ipynb` file contains:
  - All prompt versions (v1, v2, v3)
  - Reusable evaluation functions
  - 5, 10, and 15-run consistency tests
  - Failure analysis
  - Robustness testing
  - Final comparison tables
  - Reflection

- The `.html` file is a fully rendered export of the notebook, including outputs and tables.

- The `.txt` files store logged outputs from repeated runs to support consistency analysis.

---

## Methodology

Each task followed an iterative improvement framework:

### Version 1 – Zero-Shot Baseline
- Minimal instructions
- No structural constraints
- Used to identify variability and failure patterns

### Version 2 – Structured Constraints
- Explicit output format requirements
- Template enforcement (Product)
- JSON schema enforcement (Extraction)
- Strict label constraints (Sentiment)

### Version 3 – Advanced Prompt Engineering
- Few-shot prompting (Sentiment & Product)
- Chain-of-Thought reasoning (Extraction)
- Strict output control and schema isolation

Each version was evaluated through repeated execution (5, 10, and 15 runs) to measure consistency and reliability.

---

## Evaluation Strategy by Task Type

Because tasks differ fundamentally, metrics were adapted accordingly:

### Sentiment Analysis
- Exact-match consistency
- Taxonomy control
- Label boundary enforcement

### Product Description
- Structural consistency (primary metric)
- Exact-match consistency (secondary metric)
- Format compliance

### Data Extraction
- JSON schema consistency (primary metric)
- Exact-match consistency
- Stability under complex input

---

## Robustness Testing

Beyond baseline inputs, additional complex customer feedback examples were introduced to evaluate:

- Classification boundary robustness
- Multi-signal extraction stability
- Schema adherence under richer input
- Structural stability under repeated runs

These tests validate that improvements remain reliable beyond simple baseline examples.

---

## How to Run

1. Activate the virtual environment (`ironhack-labs-env`).
2. Ensure the OpenAI API key is configured in `.env`.
3. Open `prompt_engineering_lab.ipynb`.
4. Restart the kernel.
5. Run all cells.
6. Review results in the notebook or the HTML export.

---

## Key Insights

- Structural constraints are the strongest driver of reliability in generative tasks.
- Few-shot prompting improves semantic alignment rather than deterministic output.
- Chain-of-Thought improves reasoning stability but must remain hidden in production.
- Determinism must be evaluated differently depending on task type.

Prompt engineering is empirical and task-dependent. There is no universal consistency metric.

---

## Deliverables

- `prompt_engineering_lab.ipynb`
- `prompt_engineering_lab.html`
- Result logs (`.txt`)
- This README


