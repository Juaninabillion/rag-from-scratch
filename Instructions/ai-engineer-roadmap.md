# AI Engineer Transition Plan
**Profile:** Lead SRE w/ data engineering background · Python: comfortable but rusty · Time: 1–2 hrs/day
**Positioning:** Not "generic AI engineer." You are the person who ships LLM systems to production reliably — RAG + evals + observability + cost/latency engineering. This is the scarce profile.

---

## The Strategy in One Paragraph

Build one system, deeply, in public. A retrieval-augmented question-answering system built from scratch (no frameworks first), then hardened like an SRE would harden any service: eval suites, tracing, dashboards, regression tests, hybrid retrieval, reranking. Finish with a domain capstone (incident-response copilot over runbooks/postmortems) that no bootcamp grad can replicate. Apply starting week 6. Write one short public post per week.

---

## Tech Stack (decided — don't bikeshed)

| Layer | Choice | Why |
|---|---|---|
| Language | Python 3.12 | Industry default |
| Env/deps | `uv` | Fast, modern, one tool for venv + deps |
| LLM API | Anthropic API (Claude) or OpenAI — pick one, abstract behind a thin client | You'll show provider-agnostic design |
| Embeddings | `text-embedding-3-small` (OpenAI) OR `sentence-transformers` (free, local: `bge-small-en-v1.5`) | Start local/free, swap later to show abstraction |
| Vector store | **Postgres + pgvector** (Docker) | You know Postgres ops; pgvector is what real companies actually run |
| Tokenization/chunking | `tiktoken` + your own chunker | Interviews ask about chunking. Write it yourself. |
| Keyword search | `rank_bm25` → later Postgres full-text (`tsvector`) | Hybrid search, phase 2 |
| Reranker | `bge-reranker-base` (local) or Cohere Rerank API | Phase 2 |
| API layer | FastAPI | Phase 2 |
| Evals | pytest + your own harness; `ragas` optional later | Custom harness = interview gold |
| Tracing/observability | Langfuse (self-host via Docker) + OpenTelemetry | Your SRE edge |
| Versioning | Git + GitHub from day 1, public repo | Portfolio is the product |

---

## Phase 1 — RAG From Scratch (Weeks 1–3)
**Goal:** A working CLI RAG system over a real document corpus, no LangChain/LlamaIndex, every component hand-built and understood.

**Deliverable:** Public repo `rag-from-scratch` — ingest → chunk → embed → store (pgvector) → retrieve → generate with citations. README with architecture diagram.

See day-by-day breakdown below.

## Phase 2 — Production Hardening (Weeks 4–6)
**Goal:** Turn the toy into something you'd defend in an SRE review.

1. **Eval harness (week 4).** Golden dataset of 30–50 Q/A pairs over your corpus. Metrics: retrieval recall@k, MRR; answer faithfulness via LLM-as-judge. Run as pytest suite. Now every change (chunk size, model, k) gets measured, not vibes.
2. **Hybrid search + reranking (week 5).** BM25 + vector with reciprocal rank fusion; add reranker. Publish before/after eval numbers in the README — this table is what gets interview attention.
3. **Service + observability (week 6).** Wrap in FastAPI. Langfuse tracing on every request: latency per stage, token counts, cost per query. Add a `/metrics` endpoint. Write the week-6 blog post: "I applied SRE practices to a RAG pipeline."

**Start applying to jobs at end of week 6.** Target titles: AI Engineer, LLM Engineer, ML Platform Engineer, AI Infrastructure Engineer.

## Phase 3 — Agents + Domain Capstone (Weeks 7–10)
**Goal:** The standout project + agent literacy.

1. **Tool-using agent fundamentals (week 7).** Build a minimal agent loop yourself: model + tool definitions + execution loop + conversation state. No frameworks first; then note how it maps to what frameworks do.
2. **Capstone: Incident-Response Copilot (weeks 8–10).**
   - Corpus: synthetic-but-realistic runbooks, postmortems, architecture docs (generate with an LLM, curate by hand).
   - Features: RAG over runbooks with citations; agent tools (query fake metrics API, search past incidents, draft incident timeline); eval suite; full tracing.
   - This is the project you talk about in every interview. It sits exactly at the intersection of what you know (incidents, reliability) and what they're hiring for (LLM systems).
3. MCP (Model Context Protocol) familiarity: expose one capstone tool as an MCP server. It's becoming a standard; cheap to learn, strong signal.

## Ongoing (all 10 weeks)
- **Every session ends with a commit.** No exceptions.
- **One public write-up per week** (LinkedIn or a simple blog). 300–600 words, one concrete finding ("Halving chunk size improved recall@5 from 0.62 → 0.81"). Recruiters and hiring managers actually find these.
- **Interview prep from week 6:** be able to whiteboard your own system and defend every choice (why pgvector, why that chunk size, how you'd scale it, what fails first under load — you'll be unusually good at that last one).

---

# Phase 1: Day-by-Day (Weeks 1–2)
*~1–2 hrs per day. Each day has a concrete done-condition. If a day overflows, let it spill — order matters more than the calendar.*

### Day 1 — Environment + repo skeleton
- Install `uv`, Python 3.12, Docker.
- `uv init rag-from-scratch`; deps: `anthropic` (or `openai`), `psycopg`, `pgvector`, `tiktoken`, `sentence-transformers`, `pytest`, `python-dotenv`, `rich`.
- Docker compose with `pgvector/pgvector:pg16`. Confirm you can `CREATE EXTENSION vector;`.
- Push repo with README stub.
- **Done when:** `uv run python -c "import psycopg"` works and Postgres answers.

### Day 2 — Pick + ingest the corpus
- Corpus suggestion: the SRE Book (Google, free HTML) or Kubernetes docs — domain-relevant, you can judge answer quality yourself. ~50–200 pages.
- Write `ingest.py`: download/parse to clean text (use `beautifulsoup4` or `markdownify`), store as markdown files with source metadata (title, URL, section).
- **Done when:** `data/` holds clean .md files with a metadata sidecar (JSON).

### Day 3 — Chunking, by hand
- Write `chunker.py`: split on headings first, then token-window fallback (e.g., 400 tokens, 50 overlap) using `tiktoken`. Preserve metadata per chunk.
- Write 3 pytest tests: no chunk exceeds max tokens, overlap behaves, metadata survives.
- **Done when:** tests pass; you can print any chunk with its source.

### Day 4 — Embeddings
- Write `embedder.py` with a thin interface: `embed(texts: list[str]) -> list[list[float]]`. Two backends: local `bge-small-en-v1.5` (free) and the API model. Batch properly.
- Manually verify: embed "database failover" and "postgres replica promotion" — cosine similarity should beat unrelated pairs. Write this as a test.
- **Done when:** similarity sanity test passes for both backends.

### Day 5 — Vector store
- Schema: `chunks(id, doc_id, content, metadata jsonb, embedding vector(384))`.
- Write `store.py`: upsert chunks, similarity search via `embedding <=> $1 ORDER BY ... LIMIT k`. Add an HNSW index; read the pgvector docs on why/when.
- **Done when:** full ingest pipeline runs end-to-end: docs → chunks → embeddings → rows in Postgres.

### Day 6 — Retrieval + inspection
- Write `retrieve.py`: query → embed → top-k with scores + sources.
- Build a tiny CLI (`rich` tables): type a question, see the k chunks, scores, sources. **Spend real time here** — eyeball 10 queries, note where retrieval is bad and why (this becomes your week-1 blog post).
- **Done when:** you have written notes on 3 retrieval failure modes you observed.

### Day 7 — Buffer / write-up
- Catch up on overflow. Write post #1: "I built retrieval before generation, here's what surprised me."
- **Done when:** post published, repo README updated with architecture sketch.

### Day 8 — Generation with citations
- Write `generate.py`: prompt template that injects retrieved chunks with source IDs, instructs the model to cite `[1]`, `[2]`. Thin LLM client wrapper (one function, provider-swappable).
- **Done when:** CLI answers questions with inline citations mapping to real sources.

### Day 9 — The full RAG CLI
- Wire it together: `rag ask "how should I size an error budget?"` → retrieve → generate → answer + cited sources + timing per stage printed.
- Add `--k`, `--model`, `--show-chunks` flags.
- **Done when:** one command, end to end, with stage timings.

### Day 10 — Failure hunting (the interview goldmine)
- Write 20 test questions spanning easy/hard/multi-hop/out-of-corpus. Run all. Categorize failures: retrieval miss vs. bad chunking vs. hallucination vs. should-have-said-I-don't-know.
- **Done when:** a `FINDINGS.md` with the 20 Q's, results, and failure taxonomy. (This file *is* your seed eval set for Phase 2.)

### Day 11 — First improvement loop
- Pick the worst failure mode from Day 10 and fix it (likely: chunk size/overlap, or adding section-title context to chunks, or k). Re-run the 20 questions. Record before/after.
- **Done when:** FINDINGS.md shows one measured improvement.

### Day 12 — "I don't know" + prompt hardening
- Add out-of-scope handling: if top score below threshold or judge says context insufficient → refuse with explanation. Test against your out-of-corpus questions.
- **Done when:** system declines questions the corpus can't answer instead of hallucinating.

### Day 13 — Polish + diagram
- README: architecture diagram (Mermaid is fine), setup instructions a stranger could follow, the before/after table from Day 11, honest "limitations" section.
- **Done when:** a friend could clone and run it from the README alone.

### Day 14 — Write-up + Phase 2 prep
- Post #2: your failure taxonomy and the measured fix. Skim the `ragas` docs and Langfuse docs (read-only, no code) so Phase 2 starts warm.
- **Done when:** post published; you can explain recall@k out loud in one sentence.

**Week 3** continues Phase 1 spillover + converts Day 10's 20 questions into a proper 40–50 item golden dataset — the bridge into Phase 2.

---

## Anti-rules
- No LangChain/LlamaIndex until you've built it raw. (Learn them in week 7+ for resume keywords — it'll take a day because you'll already understand the concepts.)
- No course-hopping. No "I'll just watch one more video." Building > watching, 80/20.
- No private repos. Public from day 1, imperfect is fine.
- Don't skip the write-ups. They are half the job-search value of this plan.
