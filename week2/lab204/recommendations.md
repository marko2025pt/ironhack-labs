## Chunking Strategy Recommendations

### For PDF Documents:
**Recommended Strategy:** Token-Based Chunking
**Config:** chunk_size=512 tokens, chunk_overlap=50

**Reasoning:**
- This PDF (73 pages, 226k chars) is a structured repository with headers,
  tables of contents, and dotted separators that confuse semantic splitters
- Token-based gives exactly 94 chunks with a tight 430-512 token range,
  guaranteeing compliance with LLM context windows
- Recursive produced 299 chunks (too granular) due to the many short lines
  and headers in the document
- Semantic chunking struggled with the noisy table of contents structure

**Optimal config:** 512 tokens, 50 overlap (~10% overlap rate)

---

### For Podcast Transcripts:
**Recommended Strategy:** Recursive Character Chunking
**Config:** chunk_size=1000, chunk_overlap=200
**Separators:** ['. ', '? ', '! ', ' ', '']

**Reasoning:**
- Whisper transcripts are one continuous block with no paragraph breaks,
  so paragraph-based splitting offers no advantage
- Recursive with sentence-level separators produces 22 meaningful chunks
  that respect spoken thoughts
- Token-based gives only 8 chunks (too coarse for a 16k char transcript)
- Fixed-size cuts mid-sentence 80% of the time — worst option for speech
- Larger overlap (200 chars) preserves conversational continuity across boundaries

**Optimal config:** 1000 chars, 200 overlap (~20% overlap rate)

---

### Trade-offs Summary:

| Strategy      | Pros                              | Cons                          | Best For                  |
|---------------|-----------------------------------|-------------------------------|---------------------------|
| Fixed-Size    | Simple, fast, predictable         | Cuts mid-sentence often       | Uniform homogeneous text  |
| Recursive     | Respects structure, flexible      | Uneven sizes, more chunks     | Transcripts, prose docs   |
| Token-Based   | Exact LLM context compliance      | Ignores semantic boundaries   | Production RAG pipelines  |
| Semantic      | Groups by meaning                 | Slow, noisy PDFs break it     | Clean narrative content   |

---

### Key Findings:
1. **Content type matters more than strategy choice** — the PDF structural
   noise (dotted lines, headers) was the biggest obstacle across all strategies
2. **Semantic chunking requires clean input** — it correctly split the podcast
   by topic (bridge metaphor vs AI algorithms) but failed on the noisy PDF
3. **Token-based is safest for production** — guaranteed context window compliance
   regardless of content type
4. **Overlap is critical for transcripts** — 20% overlap recommended to preserve
   conversational context across boundaries
