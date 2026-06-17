# Gate 3 (Categories) — progress checkpoint

Persona: **DOMAIN_DECOMP**. Decomposing `projects/chirality-piping/` into
`domains/chirality-piping/`. cwd for all commands = monorepo root
`/Users/ryan/ai-env/projects/chirality`. WRITE_SCOPE = repo-metadata only; no
content invention (AOP-08 → TBD); commit/push only when operator asks.

## Method (faithful-to-author reconciliation — mirrors chirality-app-dev)
The piping corpus is strongly author-structured. Categories preserve that:
- **18 deliverable packages PKG-00..17 → CAT-001..018** (1:1 source-routing).
- **12 cross-cutting categories CAT-019..030** reconciling the docs/, governance,
  root, and code bodies.
Assignment is deterministic **source-routing** (`gate3_assign.py`, rules
G3BR-001..007): each IN atom inherits the category owning its author-placed PKG /
source group. Lossless — no atom splits, no UnitStatement/ContentHash edits.

## Adapter scripts (pack-local `_adapter/`)
- `gate3_build_register.py` → writes `Category_Register.csv` (30 categories).
- `gate3_assign.py` → source-routes IN atoms → `Domain_Ledger_Gate3_Category_Draft.csv`,
  `Category_Assignment_Summary.csv`, `Category_Boundary_Decisions.csv`,
  `Category_Assignment_Findings.csv`.
- `build_index_manifest.py` → derives `_Sources/Source_Manifest.index.csv`
  (non-.md rows flipped to IncludeInIndex=NO; canonical manifest untouched —
  the v1 source-DB builder only chunks markdown raw sources; code/schema atoms
  ride in as LEDGER_ATOM chunks from the ledger).
- `gate3_ratify.py` → binding retrieval ratification over the dense V2 index
  (nearest-centroid cohesion primary; scope-query cosine + BM25 diagnostic) →
  `Category_Scope_Ratification.csv` + appends G3M misassignment candidates to
  `Category_Assignment_Findings.csv`.

## DONE (deterministic layer)
- `Category_Register.csv` = **30 categories** (18 PKG + 12 cross-cutting).
- `gate3_assign.py`: **21,256 IN atoms assigned, 0 unmapped, 0 bad refs**.
  Per-category mass balanced (smallest CAT-029 tools=133; largest CAT-026 core=2783).
  TBD/OUT (656) left blank per G3BR-007.
- `cross_source_toc_matrix.md/.csv` built (158 sources, 197,916 keyword-alignment
  pairs; `build_toc_priors.py`, paths have spaces → invoke via argv wrapper).

## Source database + index (for ratification)
- `build_source_database.py --domain-root domains/chirality-piping
  --repo-root projects/chirality-piping
  --source-manifest domains/chirality-piping/_Sources/Source_Manifest.index.csv`
  → snapshot **`SRCIDX_20260617T014930Z`** (36,263 chunks: 21,912 LEDGER_ATOM,
  10,159 SECTION_NODE, 4,192 MARKDOWN_SECTION). All 21,912 atoms chunked.
- **Dense index build** (background, detached `nohup`): use the pack-local
  `_adapter/gate3_build_index.py <SNAPSHOT> --batch 128` (NOT the bare tool).
  It monkeypatches `build_source_index.encode_texts` with **length-sorted
  batching** and calls the tool's own main() (BM25/catalog/meta unchanged).
  When it finishes: `embeddings.npy` + `embeddings_norm.npy` + `bm25/` in the
  snapshot, `index_builds` status=READY. Log: `<snapshot>/_index_build.log`.

### Perf findings (M3, 16GB) — why sorted batching
Embeds ALL 36,263 chunks (21,912 LEDGER_ATOM @ ~151 chars + 10,159 SECTION_NODE
+ 4,192 MARKDOWN_SECTION; the section/markdown chunks have a long tail, p95
~2k-5k chars). fastembed pads each batch to its longest member, so unsorted
batches (long chunks sprinkled uniformly by chunk_id) compute the short atoms at
the 512-token cap. Measured: **unsorted 2.6/s (~4h, matches app-dev) vs
length-sorted 9.6/s (~63 min) = 3.6x**. Embeddings are identical (each vector
scattered back to its original chunk position). **GPU is NOT the lever:**
onnxruntime CoreMLExecutionProvider benchmarked equal-to-slower than CPU
(bge-base transformer ops fall back to CPU); torch/MPS not installed. The win is
batching, not the compute device.

## DONE — ratification + proposal (awaiting operator Gate-3 confirmation)
- Dense index built + verified: `SRCIDX_20260617T014930Z`, (36263,768) float32,
  status READY, row alignment spot-checked cos=1.00000 (sorted-scatter correct).
- `gate3_ratify.py`: **30/30 CLUSTER_COHERENT, 0 blocking**; own-centroid cosine
  median 0.713–0.771 (~21x the 1/30 baseline); 943 advisory misassignment
  candidates (retained by source-routing). Wrote `Category_Scope_Ratification.csv`.
- Integrity validator: 4 CRITICAL = expected future-gate annexes
  (ktys/subjects→Gate4, objectives→Gate4/5, coverage→Gate5). No Gate-3 problem.
- Proposal pack: `gate3_categories/GATE3_CATEGORY_PROPOSAL_20260617T050539Z/`
  (Category_Register, Summary, Boundary_Decisions, Scope_Ratification,
  Assignment_Findings, Gate3 draft ledger, Domain_Integrity_Report/Findings,
  GATE3_CATEGORY_PROPOSAL.md).

## GATE 3 ACCEPTED (operator, 2026-06-16)
943 misassignment candidates resolved **RESOLVE_SOURCE_ROUTING** (retain author
placement, G3BR-006) — stamped Status=RESOLVED_SOURCE_ROUTING in
`Category_Assignment_Findings.csv`; proposal MD status = ACCEPTED. No atom
reassignment. Gate 3 frozen baseline: 30 categories, 21,256 IN atoms assigned.

**NEXT (do NOT start until operator says so): Gate 4 (Knowledge Types & Subjects)**
by adapting `domains/chirality-app-dev/_Decomposition/_adapter/gate4_*.py`.
Operator explicitly held: do not proceed to Gate 4 yet.

## Frozen inputs
Gate 2 V2 baseline: `Atomic_Domain_Ledger.csv` = 21,912 atoms
(IN 21,256 / OUT 147 / TBD 509), 158 source units / 204 dispatch units,
`Vocabulary_Map.csv` = 1,812 terms. Accepted by operator 2026-06-16.
