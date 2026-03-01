# Bloyce's Protocol — Strict Complaint Processor (LangGraph)

A structured, rule-based complaint processing system for the Downside Up Bureau,
built with LangGraph as part of the NormalObjects project (Lab 2).

---

## Project Structure
```
lab401/
├── normalobjects_langgraph.ipynb  # Main notebook — all code and documentation
├── testlog.txt                    # Log of all test runs and prompt iterations
├── requirements.txt               # Python dependencies
├── .env                           # API keys (not committed to git)
├── .gitignore                     # Ignores .env
└── README.md                      # This file


## How to Run

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd lab401
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
Create a `.env` file in the project root:
```
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Launch Jupyter and run the notebook
```bash
jupyter notebook
```
Open `normalobjects_langgraph.ipynb` and run **Kernel → Restart & Run All**.

---

## Workflow

Every complaint is processed through a strict 5-step state machine:
```
[START] → intake → validate → investigate → resolve → close → [END]
                       ↓
                    reject → [END]
```

| Step | What it does |
|------|-------------|
| `intake` | Categorizes complaint into portal, monster, psychic, environmental, or other |
| `validate` | Checks if complaint has enough detail to proceed |
| `investigate` | Gathers evidence and documents findings |
| `resolve` | Proposes a specific resolution with effectiveness rating |
| `close` | Confirms resolution, verifies satisfaction, logs closure |
| `reject` | Rejects invalid complaints with a reason |

---

## Test Complaints

The system is tested with 5 complaints covering all categories:

| # | Complaint | Category | Expected outcome |
|---|-----------|----------|-----------------|
| 1 | Portal opens at different times | `portal` | ✅ Full workflow |
| 2 | Demogorgon behavior patterns | `monster` | ✅ Full workflow |
| 3 | El can't lift heavy rocks | `psychic` | ✅ Full workflow |
| 4 | Creatures and power lines | `environmental` | ✅ Full workflow |
| 5 | Random invalid complaint | `other` | ❌ Rejected |

---

## Issues Faced and How We Solved Them

### Issue 1: API Key Not Loading
**Problem:** `load_dotenv()` was not overriding a previously cached
environment variable, loading a placeholder key instead of the real one.

**Solution:** Changed to `load_dotenv(override=True)` to force re-reading
the `.env` file on every run.

---

### Issue 2: Complaint 5 Not Being Rejected (Baseline)
**Problem:** The original Lab Brief validation rule for `other` said
*"Automatically escalated for manual review"*. The LLM interpreted
"escalated" as "moves forward" and marked it as VALID instead of INVALID.

**Solution (Iteration 1):** Changed the rule to be explicit:
```
BEFORE: - other: Automatically escalated for manual review
AFTER:  - other: ALWAYS invalid - mark as VALID: no - automatically rejected
```

---

### Issue 3: Complaint 2 Non-Determinism (Monster validation)
**Problem:** The Demogorgon complaint passed validation in some runs
and failed in others — with identical code and input. This is LLM
non-determinism on borderline cases, even at `temperature=0`.

**Solution (Iteration 2):** Made the monster validation rule more explicit
with a concrete example:
```
BEFORE: - monster: Require description of creature behavior or interactions
AFTER:  - monster: VALID if the complaint mentions ANY creature activity,
          behavior, pattern, or interaction — even general observations
          like "sometimes work together, sometimes fight" count as valid
```

---

### Issue 4: All Effectiveness Ratings Were "High"
**Problem:** The resolution node rated every resolution as `high`
effectiveness regardless of how uncertain or complex the problem was.
This is a known LLM behavior — models are overly optimistic when
self-assessing their own outputs.

**Status:** Documented and flagged as a known limitation.
A production fix would require explicit rating criteria in the prompt
and ideally a separate evaluation LLM to assess resolution quality
independently.

---

## Key Learnings

### Prompt Engineering
- **Ambiguity is the enemy** — vague rules produce unpredictable results
- **Examples beat descriptions** — showing what counts as valid is more
  reliable than describing it abstractly  
- **Always establish a baseline** — run original prompts first, then iterate
- **Log everything** — you cannot improve what you cannot measure

### LangGraph vs LangChain
| | LangChain (Lab 1) | LangGraph (Lab 2) |
|---|---|---|
| Path control | LLM decides | Developer defines |
| Predictability | Variable | Guaranteed |
| Auditability | Hard | Easy |
| Best for | Creative, open-ended tasks | Structured, compliance workflows |

### Non-Determinism
Even at `temperature=0`, LLMs can produce different outputs for the
same input on borderline cases. Robust prompts must be explicit enough
that there is no grey area for the LLM to interpret differently across runs.

---

## Dependencies

- `langchain` — LLM orchestration framework
- `langchain-openai` — OpenAI integration for LangChain
- `langgraph` — State machine workflow framework
- `python-dotenv` — Environment variable management
- `jupyter` — Interactive notebook environment

---

## Author
Marco Martins — Ironhack AI Consulting Bootcamp