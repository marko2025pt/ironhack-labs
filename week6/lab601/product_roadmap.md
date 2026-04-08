[//]: # (Version 1.4 — Updated 2026-03-08 — V1.2 marked complete; V1.3 Intelligence Quality; versions renumbered)
# Strategic Radar — Product Roadmap
### From Demo to Deployed: V1.3 to V3.0

---

## Document Purpose

This document is the single source of truth for product direction.
All backlog items are absorbed into the version where they will be built.

Each version is a shippable increment. No version starts until the
previous one is complete and stable. The sequence is deliberate:
reliability and security before features, onboarding before scale,
intelligence depth before intelligence breadth.

**Business model — unchanged from V2.0 to V3.0:**
The consultant manages setup, KB quality, and intelligence scope for every client.
Clients configure delivery preferences and rate their briefs. That is the full client
surface area. The consultant is the product. The tool is what makes the consultant's
service remarkable.

---

## Effort Scale

| Label | Estimate |
|---|---|
| S | Half day or less |
| M | 1 day |
| L | 2–3 days |
| XL | 4+ days |

---

## Version Overview

| Version | Tagline | Theme | Gate |
|---|---|---|---|
| V1.0 | Competitor Intelligence | Core product | DONE |
| V1.1 | + Business Opportunities | Intelligence breadth | DONE |
| V1.2 | Prompt Foundation + Intelligence Quality | Client-safe + sharper briefs | DONE |
| V1.3 | Intelligence Quality II | RAG strategy · query grounding · cross-signal synthesis · token tracking | **In Progress** |
| V1.4 | + Technology Developments | Complete triple | Before first external demo |
| V1.5 | Persistent Memory | Client continuity | Before first client |
| V1.6 | Operational Hardening | Production safety | Before first paid client |
| V1.7 | Client Onboarding Engine | Onboarding speed | Gate to beta |
| V1.8 | Consultant KB Tools | Consultant efficiency | Beta sustainability |
| V1.9 | Smarter Delivery | Engagement | Beta value |
| V1.10 | White-Label + Configurability | Product feel | V2.0 readiness |
| V2.0 | Beta Launch | First paying clients — consultant-managed | Multi-client isolation |
| V2.1 | Intelligence Quality Dashboard | Learn what works | Post-beta data |
| V2.2 | Feedback Loop | Learn from clients | Brief rating data |
| V2.3 | RAG Depth | Better retrieval, richer context | Post V2.2 |
| V2.4 | Cross-Signal Intelligence | Briefs that tell stories | Run history data |
| V2.5 | Intelligence Expansion | Regulatory + product matching | Stable client base |
| V2.6 | Power Features | Scale | Mature client relationships |
| V3.0 | Strategic Intelligence Suite | Products, markets, sales + consultant licensing | Deep client relationships |

---

## Completed

### V1.0 — Competitor Intelligence
Monitor competitor moves. Evaluate strategic relevance. Deliver executive snapshot.
**Status:** ✅ Done

### V1.1 — Business Opportunities
EU public tenders, private expansion signals, pre-tender signals. Three-type opportunity taxonomy.
**Status:** ✅ Done

### V1.2 — Prompt Foundation + Intelligence Quality
**"Client-safe prompts. Meaningfully sharper briefs."**

This version made the existing two intelligence types significantly better
and made the system safe to hand to any client. No new intelligence type added.

| Feature | Effort |
|---|---|
| Session auth — all pages login-protected; `/login` + `/logout` | M |
| Dual-mode auth for `/run` — session cookie (browser) OR X-API-Key header (N8N) | S |
| `CLIENT_USERNAME`, `CLIENT_PASSWORD`, `SECRET_KEY` added to env vars | S |
| Docs dropdown nav — Presentation + Tool + Docs ▾ on all secondary pages | S |
| Static HTML pages — `/casestudy`, `/kb`, `/roadmap` — session-protected | S |
| Next Steps slide — internal links to static pages | S |
| Prompt template refactoring — `CLIENT_NAME`, `CLIENT_INDUSTRY`, `CLIENT_PRODUCTS` from env vars | M |
| Structured RAG context injection — `format_rag_context()` labels chunks by type | S |
| Explicit reasoning chain in evaluation prompts — five-step reasoning before classification | S |
| `recommended_action` + `product_affected` added to `evaluate_signals` output | S |
| Executive Takeaway synthesis rules — pattern identification, named implication, one action | S |
| Rejection logging — `rejection_reason` captured and logged for all filtered signals | S |

**Status:** ✅ Done

---

## In Progress

### V1.3 — Intelligence Quality II
**"Grounded queries. Smarter retrieval. Briefs that know what they cost."**

This version does not add a new intelligence type. It systematically addresses
the intelligence quality gaps identified in the full node-by-node pipeline review
conducted 2026-03-08. All work is in `state.py`, `nodes.py`, `graph.py`,
and `tool.html`.

Full gap analysis and implementation detail: `intelligence_imp.txt`
Full session-by-session implementation plan: `implementation_plan.txt`

Work is sequenced into 8 sessions with explicit dependencies.
Sessions must be executed in order — each builds on the previous.

---

**Session 0 — State Schema** · `state.py`

| Feature | GAP ref | Effort |
|---|---|---|
| Token tracking fields — `total_input_tokens`, `total_output_tokens` | GAP 33 | S |
| RAG context cache — `strategic_context`, `product_context` in state | GAP 2/3/18 | S |
| Cross-signal patterns field — `detected_patterns` | GAP 20/48 | S |
| Branch B typed query fields — `private_queries`, `pretender_queries` | GAP 37 | S |
| Node 7B output pools — `selected_tenders`, `selected_private`, `selected_pretender` | GAP 42 | S |

**Total effort:** S

---

**Session 1 — RAG Strategy Foundation** · `nodes.py`

| Feature | GAP ref | Effort |
|---|---|---|
| `_get_fixed_context()` helper — retrieve once, reuse across all nodes | GAP 14/18 | S |
| `_get_product_context()` helper — product catalogue retrieval | GAP 9/36 | S |
| `RAG_SCORE_THRESHOLD = 0.7` — filter low-quality chunks before prompt injection | GAP 16 | S |
| `format_rag_context()` updated to accept product_context chunks | GAP 17 | S |

**Total effort:** S

---

**Session 2 — Node 2: Query Grounding** · `nodes.py`

| Feature | GAP ref | Effort |
|---|---|---|
| Branch A: LLM-generated queries grounded in strategic context + competitor profile | GAP 2 | M |
| Branch A: Geographic targeting via `CLIENT_GEOGRAPHIES` env var | GAP 38 | S |
| Branch B: Split into typed query sets — private expansion vs pretender signals | GAP 37 | S |
| Branch B: Geographic targeting applied to both query sets | GAP 38 | S |
| Branch B: Comment cross-referencing `ted.py` CPV codes | GAP 35 | S |

**Total effort:** M

---

**Session 3 — Nodes 3 + 7: Collection Improvements** · `nodes.py`

| Feature | GAP ref | Effort |
|---|---|---|
| Strategic context injected into ReAct agent prompt | GAP 3 | S |
| Mandatory query execution — queries enforced not suggested | GAP 4 | S |
| `fetch_primary_source` — new `@lc_tool` fetching competitor/sector primary URLs | GAP 5 | M |
| Primary domain list passed into agent prompt | GAP 6 | S |
| Date filter applied at collection end, before returning | GAP 8 | S |
| Branch B: classification output includes confidence field | GAP 40 | S |
| Branch B: `low_confidence_classification` flag on uncertain signals | GAP 40 | S |

**Total effort:** M

---

**Session 4 — Node 4 + Node 7B (NEW NODE)** · `nodes.py`, `graph.py`

| Feature | GAP ref | Effort |
|---|---|---|
| Node 4: strategic + product context injected into selection prompt | GAP 9 | S |
| Node 4: `pre_selection_score` added to LLM JSON schema | GAP 12 | S |
| Node 4: dynamic signal cap — 5 / 7 / 10 based on `time_range_days` | GAP 11 | S |
| Node 4: `selection_reason` carried forward into Node 5 | GAP 10 | S |
| Node 4: improved fallback — date filter + source_type sort | GAP 13 | S |
| Node 7B: `select_opportunities` function — three LLM calls, one per pool | GAP 42 | M |
| Node 7B: pool-specific filtering (geography, product fit, classification confidence) | GAP 42 | M |
| `graph.py`: Node 7B added; old direct edge removed; new chain wired | GAP 42 | S |
| Node 8 input updated to read from `selected_*` not `raw_*` fields | GAP 42 | S |

**Total effort:** L

---

**Session 5A — Nodes 5 + 8: RAG Fixes** · `nodes.py`

| Feature | GAP ref | Effort |
|---|---|---|
| Fixed RAG context loaded once from state — no per-signal calls | GAP 14 | S |
| Conditional technology RAG — only when signal contains tech keywords | GAP 14 | S |
| RAG query built from strategic angle not signal text | GAP 15 | S |
| Convenience wrappers used — `retrieve_competitor()`, `retrieve_strategic_objectives()` | GAP 17 | S |
| Score threshold applied — chunks below 0.7 excluded from prompts | GAP 16 | S |
| Node 8: `_get_rag_context()` called once at node start, not per item | GAP 14 | S |

**Total effort:** S

---

**Session 5B — Nodes 5 + 8: Evaluation Schema** · `nodes.py`

| Feature | GAP ref | Effort |
|---|---|---|
| `CONFIDENCE_WEIGHT_*` env vars — configurable formula weights | GAP 21 Ph1 | S |
| `strategic_alignment_score` added to LLM JSON schema | GAP 21 Ph2 | S |
| `rag_score` removed from confidence formula | GAP 21 Ph2 | S |
| `reasoning_steps` field added to LLM JSON schema | GAP 19 | S |
| Product context injected into evaluation prompt — specific product name required | GAP 22 | S |
| `evaluation_failed` flag on all signal dicts | GAP 23 | S |
| Signals sorted by `pre_selection_score` before evaluation loop | GAP 24 | S |
| `recommended_action` quality instruction added to prompt | GAP 25 | S |
| Node 8: base prompt template extracted — shared across three system prompts | GAP 44 | M |
| Node 8: staleness check removed from private + pretender prompts | GAP 45 | S |
| Node 8: TED title translation confidence check | GAP 46 | S |
| Node 8: sector-specific product context injection per pool | GAP 47 | S |
| Node 8: independent budget counters per pool via env vars | GAP 49 | S |
| Node 8: competitor_alerts cross-checked against registry | GAP 43 | S |

**Total effort:** L

---

**Session 5C — Nodes 5 + 8: Synthesis + Token Tracking** · `nodes.py`

| Feature | GAP ref | Effort |
|---|---|---|
| `TokenAccumulator` callback — tracks tokens across all `llm.invoke()` and `agent.invoke()` calls | GAP 33 | M |
| Token accumulation into `state.total_input_tokens` / `state.total_output_tokens` | GAP 33 | S |
| Cost calculation from token counts + `LLM_COST_*` env vars | GAP 33 | S |
| Node 5: cross-signal synthesis step — patterns stored in `state.detected_patterns` | GAP 20 | M |
| Node 8: cross-opportunity synthesis step — patterns stored in `state.detected_patterns` | GAP 48 | M |

**Total effort:** M

---

**Session 6 — Nodes 6 + 9: Brief Generation** · `nodes.py`

| Feature | GAP ref | Effort |
|---|---|---|
| Quality gate — filter failed/low-confidence signals before generation | GAP 26/54 | S |
| `detected_patterns` consumed in Executive Takeaway prompt | GAP 28/53 | S |
| Executive Takeaway verification pass — second LLM call checks compliance | GAP 27 | M |
| Confidence rendered as labelled band — High / Medium / Low | GAP 29 | S |
| Metadata header — generated_at, calls, tokens, cost, signal counts | GAP 30 | S |
| `registry_gaps` list — companies in High/Medium signals not in registry | GAP 32 | S |
| Node 9: competitor_alerts sorted by `significance` field | GAP 51 | S |
| Node 9: Executive Takeaway pool weighting rules | GAP 52 | S |
| Node 9: grounding verification pass — flags ungrounded claims | GAP 50 | M |

**Total effort:** M

---

**Session 7 — tool.html: Full Structured Sections** · `tool.html`

| Feature | GAP ref | Effort |
|---|---|---|
| Brief parsed into sections by exact marker strings | GAP 31 partial | S |
| Executive Takeaway rendered first, full width, prominent card | GAP 31 partial | S |
| Metadata stats bar — calls, tokens, cost, signal counts as pill badges | GAP 30 | S |
| Section cards with colour-coded borders per impact/type | GAP 31 partial | S |
| Confidence badges — green / yellow / red per signal | GAP 29 | S |
| Pattern Analysis collapsible panel | GAP 20 | S |
| Registry Gaps collapsible panel (Branch A) | GAP 32 | S |
| Signals Requiring Review — collapsed by default, hidden when empty | GAP 26 | S |
| Graceful plain-text fallback if any marker missing | GAP 31 partial | S |

**Total effort:** M

---

**Total V1.3 effort:** XL
**Unlocks:** grounded queries · precise RAG · cross-signal patterns · cost visibility per brief · complete demo readiness

---

## Road to Beta

---

### V1.4 — Technology Developments
**"Complete the three-mode demo"**

Activate the third intelligence branch. The stub is already in `graph.py`.
The Technology Watchlist is already ingested (7 chunks in Pinecone).
The pattern is identical to V1.1 — low risk, well-understood.

All new nodes must be built using the V1.2 + V1.3 foundations:
`format_rag_context()`, five-step reasoning chain, `recommended_action`,
Executive Takeaway synthesis rules, `rejection_reason` logging,
`strategic_context` from state, `TokenAccumulator` tracking.

| Feature | Effort |
|---|---|
| State schema — `raw_technology_signals`, `evaluated_technology` fields | S |
| `collect_technology` node — Tavily + HackerNews, watchlist-derived queries, ReAct loop | M |
| `evaluate_technology` node — three output types: obsolescence risk / upgrade opportunity / new product gap | M |
| `generate_technology_brief` node — four-section brief with Executive Snapshot | S |
| Graph branch activation — V1.4 route in `route_after_validation()` | S |
| API response schema — technology fields added to `/run` response | S |
| UI — technology signal cards with signal type badge, watchlist match, recommended action | S |
| End-to-end test run + documentation updates | S |

**Total effort:** L
**Unlocks:** complete three-mode demo; strongest possible pitch to any prospect

---

### V1.5 — Persistent Memory
**"Reports that survive a redeploy"**

Railway's filesystem is ephemeral. Reports written to `reports/` are
wiped on every push. An SMB client who wants to compare briefs across
weeks gets nothing. Persistent storage is required before any real
client relationship begins.

This version also lays the infrastructure foundation for cross-run signal
comparison and trend detection (V2.4), and enables the brief versioning
improvement deferred from V1.3 (GAP 55).

| Feature | Effort |
|---|---|
| Supabase integration — Postgres, free tier | S |
| FastAPI writes each run result to Supabase (replaces local `reports/` write) | S |
| FastAPI reads run history from Supabase | S |
| Run history tab in tool UI — list of past runs, click to reload any brief | M |
| Signal history table — `signal_history` schema: run_id, date, intelligence_type, subject, signal_title, impact_level, confidence, strategic_link, source_url | S |
| Brief versioning — previously seen signal URLs flagged in new runs (GAP 55) | S |
| Railway deployment becomes fully stateless — no local filesystem dependency | S |

**Total effort:** M
**Unlocks:** brief comparison (V1.9), per-client analytics (V2.1), trend detection (V2.4), client continuity

---

### V1.6 — Operational Hardening
**"Production safety before the first paying client"**

Before anyone pays for this system, three questions must have answers:
Does it alert when it breaks? Can you tell clients what it costs? Are
all tunable values configurable without touching code?

Note: cost tracking per run is already available from V1.3 (GAP 33).
This version adds budget capping, alerting, and retry logic.

| Feature | Effort |
|---|---|
| Run failure alerting — N8N error handler sends alert email to operator on any failure | S |
| Monthly budget cap — `MONTHLY_BUDGET_CAP_USD` env var blocks runs when exceeded | S |
| Cost display in UI — estimated cost shown per run (data from V1.3 token tracking) | S |
| Retry logic — exponential backoff (max 3 attempts) for transient API failures in all tool files | S |
| Hard LLM budget enforcement — graph-level check routes to brief generation early if budget nearly exhausted | S |
| Environment-based configuration — all remaining hardcoded values (model name, max signals, call budget, time ranges) moved to env vars | S |

**Total effort:** M
**Unlocks:** you can answer the CFO question; you know immediately when Monday's brief fails

---

### V1.7 — Client Onboarding Engine
**"From first meeting to first brief in one day"**

The biggest bottleneck to offering beta slots is the time it takes to
build a new client's knowledge base. An LLM can draft all four KB
documents from a structured conversation. The consultant reviews,
approves, and ingests — first brief runs immediately after.

| Feature | Effort |
|---|---|
| KB generation wizard — structured intake form (10–15 questions about company, competitors, objectives, technologies) | M |
| LLM-assisted KB drafting — generates all four documents from intake answers | M |
| Consultant review + edit UI — markdown editor for each KB document before ingestion | M |
| One-click KB ingestion — chunks, embeds, and upserts to Pinecone from the UI | M |
| Onboarding runbook — internal step-by-step guide for consultant to set up a new client end to end | S |

**Total effort:** XL
**Gate:** This is the gate to beta — no beta without fast onboarding

---

### V1.8 — Consultant KB Tools
**"Maintain intelligence quality without touching code"**

After onboarding, the KB needs to evolve. Competitors change strategy.
New technologies emerge. Strategic objectives shift. The consultant
needs to update KB documents and re-ingest without a developer.

| Feature | Effort |
|---|---|
| KB document editor — edit any of the four KB documents in the UI and save | M |
| Re-ingestion trigger — re-chunk and re-embed from the editor without CLI | M |
| Chunk inspection view — show all chunks currently in Pinecone with their metadata | S |
| Competitor registry editor — add / remove competitors from the UI dropdown | S |
| Technology watchlist editor — add / remove watchlist items from the UI | S |
| Dynamic watchlist dropdown in tool UI loaded from KB at runtime (replaces hardcoded list) | S |

**Total effort:** L
**Unlocks:** consultant can maintain all clients independently; KB quality improves over time

---

### V1.9 — Smarter Delivery
**"Intelligence that fits where the client already works"**

| Feature | Effort |
|---|---|
| Slack delivery — brief posted as formatted Slack message via webhook | M |
| Brief comparison view — side-by-side view of two runs for the same subject (requires V1.5) | M |
| Delivery channel preference — client chooses email / Slack / both from UI | S |

**Total effort:** M
**Unlocks:** clients who live in Slack get value without opening email

---

### V1.10 — White-Label + Configurability
**"It feels like a product, not a demo"**

| Feature | Effort |
|---|---|
| White-label branding — `BRAND_NAME`, `BRAND_COLOR`, `BRAND_LOGO_URL` env vars replace Strategic Radar identity | M |
| Configurable brief format — client can choose between full brief / executive summary only / signal cards only | M |
| Custom email templates — client-branded HTML email, not generic Strategic Radar template | M |

**Total effort:** M
**Unlocks:** the consultant can present this as their own product to clients

---

## Beta Launch

---

### V2.0 — Beta Launch
**"First paying clients"**

The operational milestone. The consultant manages setup, KB quality, and
intelligence scope for every client. Clients configure delivery preferences
and rate their briefs. That is the full client surface area.

The increment is multi-client isolation: multiple live deployments from one
codebase, each with their own KB, branding, configuration, and brief history.

| Feature | Effort |
|---|---|
| Pinecone namespace isolation — each client has their own namespace; `PINECONE_NAMESPACE` env var routes all queries | M |
| Per-client Railway deployment — separate Railway project per client, all on main branch, differentiated by env vars | S |
| Per-client N8N workflows — copy + configure per client; independent webhook URLs, schedules, email addresses | S |
| Client delivery preferences — frequency and channel configurable from client UI | S |
| Consultant admin view — internal page listing all active clients, last run date, KB status, cost per client | M |
| Beta client onboarding runbook | S |

**Total effort:** M
**Unlocks:** recurring revenue; 10 clients × €500–1000/month

---

## Beta Phase

---

### V2.1 — Intelligence Quality Dashboard
**"Learn which sources, prompts, and KB chunks are actually working"**

After several weeks of real client runs, enough data exists to answer:
which tools produce signals that survive selection? Which RAG chunks
are never retrieved? Which intelligence types generate the most value?
The rejection logs from V1.2 and the token/cost tracking from V1.3 are
the primary data sources here.

| Feature | IQ ref | Effort |
|---|---|---|
| Tool performance metrics — signals collected vs selected vs in final brief, by tool source, per run | — | M |
| RAG chunk retrieval frequency — identify chunks never retrieved across all runs | — | S |
| Rejection pattern analysis — aggregate `rejection_reason` logs across runs; surface most common rejection patterns | IQ-8 | S |
| Per-client run analytics — average impact level, confidence scores, LLM calls, cost per run over time | — | M |
| Analytics tab in tool UI / consultant admin view | — | M |
| Prompt version tracking — record which prompt version produced each run's output | IQ-5 | S |
| Tool replacement guidance — identify underperforming tools; evaluate replacements (Perigon, NewscatcherAPI) | — | S |

**Total effort:** M
**Unlocks:** evidence-based prompt and KB improvements; data to justify tool changes

---

### V2.2 — Feedback Loop
**"The system learns from every correction"**

The most important mechanism for improving prompt quality and KB
precision over time. Every signal a client rates as irrelevant is a
data point. Every brief they find useful is a calibration signal.

| Feature | IQ ref | Effort |
|---|---|---|
| Signal rating in UI — thumbs up / thumbs down per signal (one click, no friction) | — | M |
| Brief quality classification — client marks each brief: Relevant / Partially relevant / Off target | — | S |
| Mark as irrelevant — removes signal category from future runs via exclusion list stored in Supabase | — | M |
| Brief ingestion — highly-rated briefs ingested back into KB as strategic memory; consultant approves | — | M |
| Feedback stored in Supabase alongside the run | — | S |
| Monthly feedback summary emailed to consultant — top-rated signals, most-rejected types, KB ingestion candidates | — | M |
| Confidence score calibration — empirical weight tuning based on feedback evidence (GAP 21 Phase 3) | GAP 21 | S |
| Prompt versioning — move all prompt strings to `prompts/` directory; load at startup; version per file | IQ-5 | M |

**Total effort:** L
**Unlocks:** system improves with every brief; KB grows richer over time; prompt iteration becomes systematic

---

### V2.3 — RAG Depth
**"Better retrieval, richer context"**

With V2.1 data showing which chunks are never retrieved and V2.2 feedback
showing which signals are wrongly classified, the retrieval layer can now be
improved with evidence rather than guesswork.

| Feature | IQ ref | Effort |
|---|---|---|
| Retrieval query normalisation — vocabulary mapping from news language to KB vocabulary before Pinecone query | IQ-6 | S |
| Multi-domain retrieval — fetch strategy + competitor + technology chunks simultaneously per signal | IQ-7 | S |
| Always-retrieved rules context — signal relevance rules loaded as guaranteed context, bypassing vector search | IQ-10 | S |
| Signal-to-product mapping — explicit KB document mapping signal types to product lines | IQ-11 | S |
| Structured Pinecone metadata — `vertical`, `competitor`, `technology`, `strategic_objective` added to chunk metadata; KB re-ingested | IQ-9 | M |
| Document-level summary chunks — short summary chunk per KB document for high-level orientation | — | S |

**Total effort:** M
**Prerequisite:** V2.1 (to know which chunks are underperforming before restructuring)
**Unlocks:** meaningfully better signal classification and strategic link quality; foundation for V2.4

---

### V2.4 — Cross-Signal Intelligence
**"Briefs that tell stories, not lists"**

With persistent signal history (V1.5) and better retrieval (V2.3), the system
can now reason across signals rather than treating each one in isolation.
This is the version that moves briefs from news summaries to strategic intelligence.

Note: the within-run cross-signal synthesis step shipped in V1.3 (GAP 20/48).
This version adds the cross-run, historical dimension.

| Feature | IQ ref | Effort |
|---|---|---|
| Historical signal storage — `signal_history` table queried before brief generation | IQ-12 | M |
| Trend detection across runs — `detect_patterns()` node flags when same competitor appears in High impact 3+ consecutive weeks | IQ-12 | M |
| Pattern context injected into `generate_brief` — brief LLM call receives historical pattern summary | IQ-12 | S |
| Grouped brief format — "3 stories, 7 signals" rather than "7 independent items" | IQ-13 | M |
| Multi-query ReAct strategy — agent generates follow-up queries based on what it finds | — | M |

**Total effort:** L
**Prerequisite:** V1.5 (signal history), V2.3 (retrieval quality)
**Unlocks:** the Executive Takeaway becomes genuinely executive; strategic trajectory visible across weeks

---

### V2.5 — Intelligence Expansion
**"New signal types, deeper analysis"**

Two expansions that increase strategic value and open new client segments.

| Feature | Effort |
|---|---|
| Regulatory intelligence branch — monitor regulation changes relevant to client verticals | L |
| Product-signal matching — explicit mapping from market signals to specific product lines; upgrade opportunity detection | M |
| Patent intelligence branch — monitor patent filings from competitors as early-warning signals | L |

**Total effort:** XL
**Unlocks:** clients in regulated industries; product strategy signal layer

---

### V2.6 — Power Features
**"Scale and speed for high-frequency users"**

| Feature | Effort |
|---|---|
| Batch runs — run all competitors or all sectors in one scheduled job | M |
| Run scheduling from UI — client configures frequency without touching N8N | M |
| On-demand vs scheduled toggle per intelligence type | S |

**Total effort:** M

---

## V3.0 — Strategic Intelligence Suite

The system evolves from a signal monitoring tool to a full strategic intelligence
platform. Three new intelligence modules, a quarterly synthesis layer, and a
consultant licensing programme that allows the methodology to scale beyond one consultant.

| Module | What it does |
|---|---|
| Product Intelligence | Monitor product lifecycle signals per product line — adoption curves, substitution threats, adjacent product launches |
| Market Intelligence | Track sector-level shifts — technology adoption rates, regulatory changes, investment flows |
| Sales Intelligence | Surface buying signals — expansion announcements, budget approvals, leadership changes at target accounts |
| Quarterly Synthesis | LLM-generated quarterly strategic review across all signal types, all competitors, all sectors |
| Consultant License Program | Other consultants license the methodology and system; Marco trains them and maintains the core product |

**Unlocks:** revenue that does not require direct time per client; a network of consultants improving the methodology

---

## The Arc

```
V1.2  Sharper briefs, client-safe    (prompt refactor · IQ-1/2/3/4/8 · DONE)
V1.3  Intelligence Quality II        (RAG strategy · query grounding · synthesis · token tracking)
V1.4  Complete the product           (Technology Developments — third intelligence type)
V1.5  Give it memory                 (persistent storage · signal history foundation)
V1.6  Make it reliable               (alerting · cost control · retry)
V1.7  Make it onboardable            (LLM-assisted KB setup)
V1.8  Make it maintainable           (consultant KB tools)
V1.9  Make it engaging               (Slack · comparison view)
V1.10 Make it feel like a product    (white-label · configurability)
──────────────────────────────────────────────────────────────────
V2.0  BETA LAUNCH                    (first paying clients — consultant-managed)
──────────────────────────────────────────────────────────────────
V2.1  Learn what works               (quality dashboard · rejection analysis)
V2.2  Learn from clients             (feedback loop · prompt versioning)
V2.3  Better retrieval               (RAG depth · vocabulary normalisation · metadata)
V2.4  Smarter briefs                 (cross-run synthesis · trend detection · history)
V2.5  Expand depth                   (regulatory · product matching · patents)
V2.6  More power                     (batch runs · scheduling from UI)
──────────────────────────────────────────────────────────────────
V3.0  STRATEGIC INTELLIGENCE SUITE   (products + markets + sales + licensing)
──────────────────────────────────────────────────────────────────
      The consultant is the product.
      The tool is what makes the service remarkable.
```

---

## IQ Improvements — Where Each One Ships

For traceability, every intelligence quality item is mapped to the version where it ships.

| IQ / GAP ref | Improvement | Ships in |
|---|---|---|
| IQ-1 | Structured RAG context injection (`format_rag_context()`) | V1.2 ✅ |
| IQ-2 | Explicit reasoning chain in evaluation prompts | V1.2 ✅ |
| IQ-3 | `recommended_action` + `product_affected` in `evaluate_signals` | V1.2 ✅ |
| IQ-4 | Executive Takeaway synthesis rules in `generate_brief` | V1.2 ✅ |
| IQ-5 | Prompt versioning — `prompts/` directory | V2.2 |
| IQ-6 | Retrieval query normalisation | V2.3 |
| IQ-7 | Multi-domain retrieval | V2.3 |
| IQ-8 | Rejection logging with `rejection_reason` | V1.2 ✅ |
| IQ-9 | Structured Pinecone metadata | V2.3 |
| IQ-10 | Always-retrieved relevance rules | V2.3 |
| IQ-11 | Signal-to-product mapping in KB | V2.3 |
| IQ-12 | Historical signal storage + trend detection | V2.4 |
| IQ-13 | Cross-signal synthesis step (within-run) | V1.3 |
| GAP 2 | LLM-generated queries grounded in strategic context | V1.3 |
| GAP 3 | Strategic context injected into ReAct agent | V1.3 |
| GAP 4 | Mandatory query execution in ReAct agent | V1.3 |
| GAP 5 | Primary source fetching via `fetch_primary_source` tool | V1.3 |
| GAP 6 | Primary domain list passed into agent prompt | V1.3 |
| GAP 8 | Date filter applied at collection end | V1.3 |
| GAP 9 | Selection grounded in strategic + product context | V1.3 |
| GAP 10 | `selection_reason` carried into evaluation | V1.3 |
| GAP 11 | Dynamic signal cap based on time window | V1.3 |
| GAP 12 | `pre_selection_score` in selection output | V1.3 |
| GAP 13 | Improved selection fallback | V1.3 |
| GAP 14 | Fixed RAG context cached — no per-signal calls | V1.3 |
| GAP 15 | RAG query built from strategic angle | V1.3 |
| GAP 16 | RAG score threshold — chunks below 0.7 excluded | V1.3 |
| GAP 17 | Convenience wrappers used in all nodes | V1.3 |
| GAP 18 | Structured RAG call design per node | V1.3 |
| GAP 19 | `reasoning_steps` field in evaluation output | V1.3 |
| GAP 20 | Cross-signal synthesis step (within-run) | V1.3 |
| GAP 21 Ph1+2 | Confidence formula — env var weights + `strategic_alignment_score` | V1.3 |
| GAP 21 Ph3 | Empirical confidence calibration | V2.2 |
| GAP 22 | Product context injected — specific product name required | V1.3 |
| GAP 23 | `evaluation_failed` flag on all signal dicts | V1.3 |
| GAP 24 | Signals sorted by `pre_selection_score` before eval loop | V1.3 |
| GAP 25 | `recommended_action` quality instruction | V1.3 |
| GAP 26 | Quality gate before brief generation | V1.3 |
| GAP 27 | Executive Takeaway verification pass | V1.3 |
| GAP 28 | `detected_patterns` consumed in Executive Takeaway | V1.3 |
| GAP 29 | Confidence rendered as labelled band | V1.3 |
| GAP 30 | Metadata header — calls, tokens, cost, signal counts | V1.3 |
| GAP 31 | Full structured JSON brief | V1.5 |
| GAP 32 | `registry_gaps` list in brief output | V1.3 |
| GAP 33 | Token tracking + cost per brief | V1.3 |
| GAP 34 | Node 2 query scope documented (TED vs web) | V1.3 |
| GAP 35 | Cross-reference comment to `ted.py` CPV codes | V1.3 |
| GAP 36 | Branch B queries grounded in product catalogue | V1.3 |
| GAP 37 | Branch B typed query sets — private vs pretender | V1.3 |
| GAP 38 | Geographic targeting in all query sets | V1.3 |
| GAP 39 | CPV coverage review process | V1.4 |
| GAP 40 | Classification confidence field on signals | V1.3 |
| GAP 41 | Two-agent collection strategy (Branch B) | V1.5 |
| GAP 42 | Node 7B — `select_opportunities` new node | V1.3 |
| GAP 43 | Competitor alerts cross-checked against registry | V1.3 |
| GAP 44 | Base prompt template — shared reasoning chain | V1.3 |
| GAP 45 | Staleness check removed from evaluation prompts | V1.3 |
| GAP 46 | TED title translation confidence check | V1.3 |
| GAP 47 | Sector-specific product context per pool | V1.3 |
| GAP 48 | Cross-opportunity synthesis step (Branch B) | V1.3 |
| GAP 49 | Per-pool budget allocation via env vars | V1.3 |
| GAP 50 | Grounding verification pass (Branch B brief) | V1.3 |
| GAP 51 | Competitor alerts sorted by significance | V1.3 |
| GAP 52 | Executive Takeaway pool weighting rules | V1.3 |
| GAP 53 | `detected_patterns` consumed in Branch B Takeaway | V1.3 |
| GAP 54 | Quality gate in `_build_block()` | V1.3 |
| GAP 55 | Brief versioning — previously seen signals flagged | V1.5 |

---

## Won't Build

| Item | Reason |
|---|---|
| PDF export | HTML email is lighter, links are clickable, renders on mobile, no generation dependency |
| Multi-tenant SaaS architecture | Out of scope for the consulting model — per-client Railway projects is the right pattern throughout |
| Client self-service KB management | The consultant manages the KB. Quality of intelligence depends on quality of input. This is not delegated to clients. |
| Mobile app | Not relevant for this audience or use case |
| Fully automated onboarding without consultant involvement | The strategic clarity session before KB creation is a feature, not a bug. It is where the consultant's value starts. |
| LangSmith integration | Out of scope — token tracking handled natively via `TokenAccumulator` callback from V1.3 |

---

## Continuous Improvements (No Version Gate)

These run in parallel with all versions. No sprint required — ongoing practice.

- **KB document quality** — rewrite chunks that are never retrieved (identified in V2.1). Better chunking = better retrieval = better evaluation.
- **Prompt engineering** — refine system prompts based on feedback data (V2.2) and real run output. The prompts are the product's competitive moat.
- **Competitor and sector registry** — expand the default lists as new industries are served.
- **Domain list expansion** — add industry-specific domains discovered through real client runs to `domain_lists.json`. No code changes required. Edit JSON, redeploy.
- **API tool evaluation** — from V2.1 onwards, use the performance dashboard to identify underperforming tools. Candidates: Perigon, NewscatcherAPI, sector-specific RSS feeds, LinkedIn signals, Crunchbase funding data. Track experiments in a dedicated log.
- **LLM provider evaluation** — evaluate alternatives on output quality, cost, and reliability as the model landscape evolves. Candidates: Anthropic Claude, Google Gemini, Mistral (cost-sensitive runs), Ollama (on-premise clients). Document every evaluation with prompt version, model, sample output, and cost.
