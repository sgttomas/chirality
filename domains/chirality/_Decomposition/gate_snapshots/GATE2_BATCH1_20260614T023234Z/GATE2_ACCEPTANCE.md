# Gate 2 Acceptance - Chirality DOMAIN_DECOMP Batch 1

Package role: snapshot / handoff artifact

Gate: Gate 2 Atomization / Normalization

Scope: `BATCH1_BINDING_GOVERNANCE_20260614T011101Z`

Status: ACCEPTED

Accepted UTC: 2026-06-14T02:32:34Z

Human confirmation:

```text
Gate 2 approved.  Proceed accordingly.
```

## Accepted Atomization

- Domain root: `domains/chirality`
- Accepted Gate 1 snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z`
- Batch 1 atomization handoff: `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/BATCH1_ATOMIZATION_HANDOFF.md`
- Source manifest: `domains/chirality/_Sources/Source_Manifest.csv`
- Source manifest SHA-256: `f072b1d43eb98b057cdb392a674bc9e7feaffbe483c7f59a06f5557219762fb1`
- Accepted partial ledger: `domains/chirality/_Decomposition/Atomic_Domain_Ledger.csv`
- Accepted partial ledger SHA-256: `ce781347e9417577127251a7ce713b1cfd9e3b7d27b54c98b270a775d1cf5bf8`
- Accepted vocabulary map: `domains/chirality/_Decomposition/Vocabulary_Map.csv`
- Accepted vocabulary map SHA-256: `a428b77b2b2bcbe60500f6f91fffdf4543d84a9f8d886d32d43d7be23b3dc98e`

## Accepted Batch 1 Telemetry

| Metric | Value |
|---|---:|
| Selected sources | 22 |
| Dispatch units | 22 |
| Per-unit atom CSVs | 22 |
| Per-unit vocabulary CSVs | 22 |
| Raw worker atom rows | 3276 |
| Merged atom ledger rows | 3274 |
| Deduped duplicate hash rows | 2 |
| IN rows after merge | 3262 |
| OUT rows after merge | 12 |
| TBD rows after merge | 0 |
| Per-source ledgers | 22 |
| Merged vocabulary terms | 670 |
| Atom-review HTML files | 22 |

## Phase 2.5 Refresh Evidence

- Source catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T023650Z`
- Catalog schema: `chirality-source-db/v2`
- Catalog validation: PASS, 0 blockers, 0 warnings
- Catalog source docs: 242
- Catalog artifacts: 485
- Catalog chunks: 12246
- Chunk types: `MARKDOWN_SECTION=4523`, `SECTION_NODE=4449`, `LEDGER_ATOM=3274`
- Retrieval status: `BM25_ONLY`
- Retrieval rows: 12246
- Retrieval smoke query: `derivative-package rule` returned `@repo/AGENTS.md` at rank 1.
- Dense embeddings: deferred, not built.
- TOC-prior matrix Markdown: `domains/chirality/_Decomposition/cross_source_toc_matrix.md`
- TOC-prior matrix Markdown SHA-256: `ecf5fcd007e79258cfe466e163bcfb7e489fe6e32215d7391f658e6b6806cfc1`
- TOC-prior matrix CSV: `domains/chirality/_Decomposition/cross_source_toc_matrix.csv`
- TOC-prior matrix CSV SHA-256: `afb903b1fc311ebe8123988a9932d71b336cfb0276039b6f7df41386d973f2a3`

## Gate 2 Verdict

The Batch 1 merged Domain Ledger is accepted as the intended binding-governance atomization surface for the selected 22-source batch.

This acceptance is batch-scoped. It does not close atomization for the remaining manifest-backed sources and does not create full-corpus Category, Knowledge Type, Knowledge Subject, hypergraph, DBM publication, or public export truth.
