# Lab 302 — Relevance Scoring and Rerankers

## 1. Objectives

This lab builds a complete Retrieval-Augmented Generation (RAG) pipeline with progressively improved retrieval quality. Starting from a basic vector similarity search, each step adds a layer of sophistication until a production-grade pipeline is assembled.

By the end of the lab, the student should be able to:

- Load, clean, and chunk documents from multiple sources (PDF and audio)
- Build and query a ChromaDB vector store using OpenAI embeddings
- Understand why pure vector similarity search is insufficient for production RAG
- Implement LLM-based relevance scoring to rerank retrieved chunks
- Use a Cross-Encoder model as a faster, cheaper alternative to LLM scoring
- Apply metadata filtering to restrict retrieval to relevant document subsets
- Assemble a full RAG pipeline combining all of the above
- Evaluate retrieval quality by comparing baseline vs. reranked results

---

## 2. Project Setup

### Requirements

```
pip install -r requirements.txt
```

### requirements.txt

```
langchain
langchain-openai
langchain-community
langchain-text-splitters
chromadb
pypdf
sentence-transformers
openai
python-dotenv
pandas
```

### Environment Variables

Create a `.env` file in the project root with your OpenAI API key:

```
OPENAI_API_KEY=sk-...
```

### FFmpeg (for podcast transcription)

The podcast transcription step requires FFmpeg. Download from https://ffmpeg.org and update the `FFMPEG_PATH` variable in the notebook to point to your local installation:

```python
FFMPEG_PATH = r"C:\ffmpeg\fullbuild\bin\ffmpeg.exe"
```

---

## 3. Project Structure

```
lab302/
│
├── relevance_scoring_rerankersV3_with_logging.ipynb   # Main notebook
├── requirements.txt                                    # Python dependencies
├── README.md                                           # This report
│
├── Living_Repository_AI_Literacy_Practices.pdf        # Source document (PDF)
├── The_Blueprint_For_Trustworthy_AI.m4a               # Source document (podcast)
│
├── company_segmentation.txt                           # Output: 28 company blocks extracted from PDF
├── company_chunking.txt                               # Output: 56 LangChain documents from PDF
├── podcast_transcript.txt                             # Output: Full podcast transcript (Whisper)
├── podcast_chunking.txt                               # Output: 79 LangChain documents from podcast
│
├── notebooklog.txt                                    # Output: Appended log of all cell outputs
└── chroma_db/                                         # Output: Persisted ChromaDB vector store
```

---

## 4. Steps — Compact Summary

### Step 1 — Data Ingestion

- **PDF:** EU AI Act Living Repository processed with pypdf. Pages cleaned, company sections segmented, metadata extracted (name, size, sector, HQ, implementation status).  
  → Split into organisation + AI literacy documents = **56 docs**.
- **Podcast:** Audio split into 10-minute chunks (FFmpeg) to meet Whisper API limits, transcribed and merged. Transcript chunked into groups of 5 timestamp lines.  
  → **79 docs**.
- **Total corpus:** **135 documents** (56 PDF + 79 podcast).

### Step 2 — Embeddings & Vector Store

- All documents embedded using **text-embedding-3-small** (1536-dim vectors).
- Stored in persistent **ChromaDB**.
- Baseline similarity search confirms retrieval works.

### Step 3 — LLM Relevance Scoring

- GPT assigns relevance scores (1–10) to retrieved chunks.
- Combined metric:  
  `final = rel_score - sim_score`
- Results reranked using combined score.

### Step 4 — Cross-Encoder Reranking

- HuggingFace **cross-encoder/ms-marco-MiniLM-L-6-v2** used.
- Scores query + document jointly.
- Faster and cheaper than GPT scoring.
- Produced stronger direct relevance ranking.

### Step 5 — Metadata Filtering

- ChromaDB filters applied before similarity search.
- `smart_search()` auto-detects keywords and applies filters (e.g., fully implemented).
- Filtering validated through test queries.

### Step 6 — Complete RAG Pipeline

Pipeline structure:

1. `smart_retriever()` → retrieve k=50 candidates  
2. `rerank_docs()` → Cross-Encoder reranks, keeps top 5  
3. `ask_rag()` → GPT answers using top chunks

### Step 7 — Evaluation

- Compared:
  - **Baseline:** vector search only
  - **Full pipeline:** retrieval + reranking
- Tested on two representative queries.

---

## 5. Analysis — Compact Summary

### Baseline Vector Search

- Conceptual queries returned mainly podcast chunks.
- Similarity scores weak (0.75–0.86).
- Vocabulary overlap ≠ true relevance.

### LLM Relevance Scoring

- Corrected ranking effectively.
- LLM signal dominated because similarity scores varied little.
- Combined score added little beyond LLM ranking.

### Cross-Encoder Reranking

- Produced substantially different ranking.
- Correctly prioritised structurally direct answers.
- Strong disagreements with LLM scoring highlighted deeper relevance understanding.

### Metadata Filtering

- Successfully restricted results to correct implementation status.
- Improved retrieval precision.
- Cannot fix missing content in corpus.

### Evaluation (Baseline vs Reranked)

- **“Fully implemented organisations”**
  - Baseline: 2 companies
  - Reranked pipeline: 5 companies
  - True total in corpus: 13 → limitation caused by small k.
- **“Trustworthy AI principles”**
  - Both approaches incomplete due to chunk boundaries splitting concepts.

---

## 6. Concluding Analysis — Key Insight

The main lesson is **data quality over algorithm complexity**.

- Retrieval tools (vector search, rerankers, filters) worked correctly.
- Performance limits came from:
  - corpus mismatch
  - chunking decisions
  - metadata design

Key observations:

- Wrong or incomplete source material cannot be fixed by better retrieval.
- Chunking defines what retrieval can ever find.
- Metadata enables powerful routing only when extracted correctly.
- Embedding quality depends on corpus coherence.

Core takeaway:

> RAG quality is determined upstream — data, chunking, and metadata — not by retrieval sophistication.

---

## 7. Further Development — Podcast Chunking

Problem:

- Current chunks (5 lines) are too small.
- Ideas split across chunks → incomplete answers.

Observed effect:

- High-ranking chunks introduced concepts but excluded explanations.

Proposed improvements:

- Increase chunk size to **10–15 lines**.
- Add **2–3 line overlap**.
- Move toward **semantic chunking** based on topic boundaries.

Final learning:

- Identifying data structure problems is more important than adding new tools.
