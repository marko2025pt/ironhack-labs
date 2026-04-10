# Lab: Custom Dataset Creation & Evaluation with LangSmith

**Student:** Marco Martins
**Bootcamp:** Ironhack AI Consulting Bootcamp  
**Date:** April 2026

---

## Domain & Dataset Description

This lab evaluates GPT-4o-mini on a custom **Arduino programming Q&A** dataset.
Arduino is an open-source electronics platform widely used in education and prototyping.
The dataset consists of 15 manually curated question-answer pairs covering core Arduino
concepts such as pin configuration, digital/analog I/O, PWM, timing, serial communication,
and hardware libraries.

The domain was chosen because Arduino Q&A has clear, verifiable answers — making it
ideal for LLM evaluation with an LLM-as-judge correctness evaluator.

---

## Approach Overview

1. **Dataset**: 15 Arduino Q&A examples created manually and uploaded to LangSmith
2. **Target function**: GPT-4o-mini with a system prompt for Arduino expertise
3. **Evaluator**: LLM-as-judge using openevals' `CORRECTNESS_PROMPT` with GPT-4o-mini
4. **Experiment tracking**: All runs traced and stored automatically in LangSmith

---

## Repository Structure

    lab_langsmith_marco/
    │
    ├── README.md               # This file
    ├── lab_report.md           # Full evaluation report with results and analysis
    ├── lab_langsmith.ipynb     # Jupyter notebook with all implementation code
    └── .env                    # API keys (not committed to version control)

---

## How to Run

**1. Set up the environment**

    conda activate ironhack-labs-env
    pip install langsmith openai openevals python-dotenv

**2. Create a `.env` file in the root folder**

    LANGSMITH_API_KEY=your_langsmith_key_here
    OPENAI_API_KEY=your_openai_key_here
    LANGSMITH_TRACING=true
    LANGSMITH_PROJECT=arduino-qa-eval

**3. Open and run the notebook**

    jupyter notebook lab_langsmith.ipynb

Run all cells from top to bottom. The notebook will:
- Connect to LangSmith
- Create the dataset (or skip if it already exists)
- Run the target function on all 15 examples
- Evaluate results using the LLM-as-judge evaluator
- Print a summary of scores and the evaluation report

---

## LangSmith Links

| Resource   | Link |
|------------|------|
| Dataset    | https://smith.langchain.com/o/3b161d59-853b-4037-9456-e4fa9d149381/datasets/3bec138e-329b-4599-8e3d-e2987b882d40 |
| Experiment | https://smith.langchain.com/o/3b161d59-853b-4037-9456-e4fa9d149381/datasets/3bec138e-329b-4599-8e3d-e2987b882d40/compare?selectedSessions=7c0cdef6-2cf6-4a94-9e4e-e89877377fab |

---

## Key Results

| Metric          | Value       |
|-----------------|-------------|
| Total examples  | 15          |
| Pass rate       | 100%        |
| Correct answers | 15/15       |
| Judge model     | GPT-4o-mini |

---

## Notes

- The `.env` file is not committed to version control — add it manually before running
- The dataset creation step is idempotent — it skips upload if the dataset already exists
- All LLM calls are automatically traced in LangSmith via `wrap_openai` and `@traceable`