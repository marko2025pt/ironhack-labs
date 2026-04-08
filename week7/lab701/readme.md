# Lab: Benchmark Audit & Evaluation Blueprint
Student: Marco Martins
Date: April 2026
Ironhack AI Consulting

## Chosen Scenario
A recruitment agency receives structured briefs from client companies and wants to automate the generation of polished, publish-ready job descriptions using an LLM. The evaluation focuses on three critical dimensions: faithfulness to the brief, inclusive and bias-free language, and legal safety (EU employment law compliance).

## Approach Overview
The lab is structured in two parts:

### Part 1 — Evaluation Design (Hours 1–3)

I audited three existing benchmarks (IFEval, TruthfulQA, BOLD) and found that two were unsuitable due to high contamination and saturation risk. 

I designed a custom evaluation suite of five prompts covering the core failure modes of the use case: hallucination, omission, gendered language, conflicting instructions, and discriminatory client notes. 

I then designed a full LLM-as-judge prompt with five evaluation criteria and a 1–5 scoring rubric, and wrote a professional evaluation memo comparing GPT-4o and Claude Sonnet 4.6.

### Part 2 — Implementation (Hour 4)
I implemented the evaluation pipeline in Python using the OpenAI API directly. The pipeline generates JDs with GPT-4o, evaluates them with a GPT-4o judge, applies rule-based regex checks in parallel, and saves all results to JSON with full metrics.

## Repository Structure
lab701/
├── benchmark_audit.md          # Audit of 3 existing benchmarks with evaluation cards
├── evaluation_design.md        # 5 evaluation prompts + LLM-as-judge prompt design
├── evaluation_memo.md          # 1-page client memo with results and recommendation
├── reflection.md               # Answers to 3 reflection questions
├── llm_judge_evaluation.py     # Main evaluation pipeline
├── evaluation_results.json     # Output from the last evaluation run
├── implementation_summary.md   # Key findings and recommended next steps
├── README.md                   # This file
├── .env                        # API key (not committed)
└── .gitignore                  # Excludes .env and venv/

## How to Run
1. Install dependencies:
bashpython -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
pip install openai python-dotenv

2. Set up your API key:
bashecho OPENAI_API_KEY=your_key_here > .env

3. Run the evaluation:
bashpython llm_judge_evaluation.py
Results are printed to the console and saved to evaluation_results.json.

## Key Findings

The generator adds soft skills and boilerplate sections by default — the generator prompt must include explicit prohibitions mirroring the judge criteria, not just a general instruction to "stay within the brief".
The LLM judge requires calibration — after tightening criteria, TC01 dropped from 5/5 to 2/5, suggesting the judge may be overcorrecting on standard JD conventions.

Rule-based checks are essential alongside the LLM judge — in TC02, the judge missed gendered pronouns that the regex check caught.
TC05 is the highest-risk case — the model reproduced discriminatory client instructions ("native English speakers", "young") in both runs, confirming that human review is mandatory for briefs containing freeform client notes.


## Estimated Cost
~$0.05 per full evaluation run (5 test cases, GPT-4o for both generation and judging).