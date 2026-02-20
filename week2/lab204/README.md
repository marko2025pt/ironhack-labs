# 🧩 RAG Lab: Different Ways to Chunk Podcast and PDF

## Overview

This lab explores and compares four chunking strategies for building a
RAG (Retrieval-Augmented Generation) system using two real-world content types:

- 🎙️ **Podcast audio** — *The Blueprint For Trustworthy AI* (`.m4a`)
- 📄 **PDF document** — *Living Repository of AI Literacy Practices* (73 pages)

Chunking is one of the most critical steps in any RAG pipeline. The way you
split documents directly impacts retrieval quality, context preservation, and
overall system performance. This lab provides hands-on experience with four
strategies and delivers evidence-based recommendations for each content type.

---

## 📁 Files in This Project

| File | Description |
|---|---|
| `chunking_strategies.ipynb` | Main Jupyter notebook — full code, explanations, and recommendations |
| `requirements.txt` | Python dependencies to install before running the notebook |
| `recommendations.md` | Final chunking strategy recommendations (also included in the notebook) |
| `podcast_transcript.txt` | Whisper-generated transcript of the podcast (auto-created on first run) |
| `chunk_distributions.png` | Histogram chart comparing chunk size distributions across strategies |
| `chunk_count_comparison.png` | Bar chart comparing total chunk counts per strategy |
| `The_Blueprint_For_Trustworthy_AI.m4a` | Source podcast audio file |
| `Living_Repository_AI_Literacy_Practices.pdf` | Source PDF document |

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Install ffmpeg (required for audio processing)
Download from https://ffmpeg.org/download.html and install system-wide.

> ⚠️ If ffmpeg is installed but not in your PATH, update these lines
> at the top of the notebook with your actual ffmpeg location:
> ```python
> AudioSegment.converter = r"C:\ffmpeg\fullbuild\bin\ffmpeg.exe"
> AudioSegment.ffprobe   = r"C:\ffmpeg\fullbuild\bin\ffprobe.exe"
> ```

### 3. Set your OpenAI API key
Create a `.env` file in this directory:
```
OPENAI_API_KEY=sk-your-key-here
```

### 4. Run the notebook
Open `chunking_strategies.ipynb` in Jupyter and run all cells from top to bottom.

> 💡 The podcast transcript is saved locally after the first run — subsequent
> runs will load it from disk and skip the Whisper API call entirely.

---

## 📓 Notebook Structure

The notebook `chunking_strategies.ipynb` is organized into 11 steps,
each with a markdown explanation followed by the corresponding code cell.

### Step 1 — Install & Import Dependencies
Installs and imports all required libraries: LangChain, pypdf, tiktoken,
sentence-transformers, pydub, openai, matplotlib, and numpy.

### Step 2 — Configure API Key
Loads the OpenAI API key from the `.env` file and initializes the client.

### Step 3 — Transcribe the Podcast (Whisper API)
Sends the podcast audio to OpenAI's `whisper-1` model for transcription.
Automatically splits files larger than 24MB into chunks to stay within
the API's file size limit. Saves the transcript locally for reuse.

> ⚠️ **Issue encountered:** The podcast file was 28.8MB — over the 25MB
> Whisper API limit. Solved by splitting the audio into 2 chunks with `pydub`.

### Step 4 — Load the PDF Document
Extracts text from all 73 pages of the PDF using `pypdf`, joining pages
with double newlines to preserve document structure.

### Step 5 — Helper Functions
Defines three utility functions used throughout the lab:
- `count_tokens()` — counts tokens using the GPT-4 tokenizer
- `chunk_stats()` — computes chunk count, avg/min/max chars and tokens
- `check_sentence_breaks_v2()` — measures percentage of mid-sentence cuts

### Step 6 — Strategy 1: Fixed-Size Chunking
Splits text at exactly N characters using `CharacterTextSplitter`.
Tests configurations: 500, 1000, and 2000 chars with varying overlap.
Includes visual inspection of chunk boundaries and sentence break analysis.

**Result:** PDF 30% mid-sentence breaks, Podcast 80% mid-sentence breaks.

### Step 7 — Strategy 2: Recursive Character Chunking
Uses `RecursiveCharacterTextSplitter` with separator priority:
`['\n\n', '\n', '. ', ' ', '']` — tries paragraph breaks first,
falling back to sentence endings, then word boundaries.

Includes a corrected sentence break measurement after discovering
that the splitter consumes periods, causing misleading metrics.

**Result:** PDF 0% mid-sentence breaks, Podcast 80% (no paragraph structure).

### Step 8 — Strategy 3: Token-Based Chunking
Uses `TokenTextSplitter` with `cl100k_base` encoding (same as GPT-4).
Tests 256, 512, and 1024 token configurations. Verifies that actual
token counts match requested sizes exactly.

**Result:** Tightest distribution of all strategies — every chunk hits
exactly 512 tokens regardless of character count variation.

### Step 9 — Strategy 4: Semantic Chunking (Advanced)
Uses `sentence-transformers` (`all-MiniLM-L6-v2`) to embed sentences
and split where cosine similarity drops between adjacent sentences.
Applied to a 5000-character sample due to CPU processing cost.

Includes a diagnostic step that revealed PDF table-of-contents dotted
lines (`"......."`) were corrupting similarity scores — solved with a
`clean_text_for_semantic()` preprocessing function.

**Result:** Works well for podcast (correctly identifies topic shifts),
struggles with noisy PDF structure.

### Step 10 — Visualizations
Generates two charts saved as `.png` files:
- `chunk_distributions.png` — 2×4 histogram grid across all strategies
- `chunk_count_comparison.png` — grouped bar chart of total chunk counts

### Step 11 — Final Summary & Recommendations
Prints a complete comparison table across all strategies and content types,
followed by evidence-based recommendations for production use.

---

## 🏆 Key Recommendations

### For PDF Documents → Token-Based (512 tokens, 50 overlap)
Guarantees LLM context window compliance with a tight 430–512 token range.
The PDF's structural noise makes semantic chunking unreliable, and recursive
produces too many small chunks (299) from short header lines.

### For Podcast Transcripts → Recursive Character (1000 chars, 200 overlap)
Sentence-level separators `['. ', '? ', '! ']` respect spoken thoughts.
20% overlap preserves conversational continuity across chunk boundaries.
Token-based produces too few chunks (8) for meaningful retrieval on a
short transcript.

---

## ⚠️ Issues Encountered & Solved

| Issue | Cause | Solution |
|---|---|---|
| Whisper 413 error | Audio file 28.8MB > 25MB limit | Split audio into chunks with `pydub` |
| ffmpeg not found | Installed but not in system PATH | Hardcoded executable path in notebook |
| Misleading break metrics | Recursive splitter consumes periods | Rewrote `check_sentence_breaks_v2()` |
| Semantic chunks too small | Threshold too high (0.75) | Tuned down to 0.05 iteratively |
| PDF noise corrupting embeddings | Dotted lines scoring similarity=1.0 | Added `clean_text_for_semantic()` |

---

## 📚 References

- [LangChain Text Splitters Documentation](https://python.langchain.com/docs/modules/data_connection/document_transformers/)
- [OpenAI Whisper API](https://platform.openai.com/docs/guides/speech-to-text)
- [tiktoken — OpenAI Tokenizer](https://github.com/openai/tiktoken)
- [Sentence Transformers](https://www.sbert.net/)
- [ChunkViz — Visualize Chunking Strategies](https://chunkviz.up.railway.app/)
