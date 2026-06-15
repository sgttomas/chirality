# Gate 3 Category Proposal — Chirality DOMAIN_DECOMP

Generated: 20260614T213500Z
Updated: 20260614T213548Z

## Status

Gate 3 is open. This package proposes a flat 11-category partition over the accepted Gate 2 source-unit surface. It does not close Gate 3.

Accepted upstream truth:

- `Atomic_Domain_Ledger.csv` from Gate 2: 19473 rows (`IN=19403`, `OUT=20`, `TBD=50`).
- `Gate2_Source_Unit_Register.csv`: accepted 110 source-unit authority for Phase 3.
- `Vocabulary_Map.csv` and `cross_source_toc_matrix.*`: accepted Gate 2 priors.
- Source index snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T204703Z`.

## Dense Ratification Result

Dense embeddings completed successfully for the current source_v2 index. Category scope ratification remains blocking: every proposed Category currently carries `SCOPE_REFINEMENT_NEEDED` under the default 0.75 cosine threshold.

## Proposed Categories

- `CAT-001` Epistemic and Professional-Practice Foundations — 2180 IN atoms; ambiguous findings=136; verdict=SCOPE_REFINEMENT_NEEDED.
- `CAT-002` Governance and Agent Instruction Architecture — 1109 IN atoms; ambiguous findings=25; verdict=SCOPE_REFINEMENT_NEEDED.
- `CAT-003` Decomposition Lifecycle and Domain Structuring — 2252 IN atoms; ambiguous findings=207; verdict=SCOPE_REFINEMENT_NEEDED.
- `CAT-004` Task, Skill, and Tool Execution Contracts — 2619 IN atoms; ambiguous findings=107; verdict=SCOPE_REFINEMENT_NEEDED.
- `CAT-005` Source Fidelity, Retrieval, and Validation Infrastructure — 227 IN atoms; ambiguous findings=22; verdict=SCOPE_REFINEMENT_NEEDED.
- `CAT-006` Audit, Review, Reconciliation, and Evaluation — 2563 IN atoms; ambiguous findings=174; verdict=SCOPE_REFINEMENT_NEEDED.
- `CAT-007` Publication, Aggregation, Hypergraph, and Synthesis — 2118 IN atoms; ambiguous findings=88; verdict=SCOPE_REFINEMENT_NEEDED.
- `CAT-008` Document, Asset, Drawing, and Engineering-Data Extraction — 3305 IN atoms; ambiguous findings=77; verdict=SCOPE_REFINEMENT_NEEDED.
- `CAT-009` Coordination, Change, Scheduling, and Deliverable Workflows — 1691 IN atoms; ambiguous findings=30; verdict=SCOPE_REFINEMENT_NEEDED.
- `CAT-010` Work-Surface, Project, Product, and Integration Boundaries — 1297 IN atoms; ambiguous findings=15; verdict=SCOPE_REFINEMENT_NEEDED.
- `CAT-011` Legal, License, and Public-Release Boundaries — 42 IN atoms; ambiguous findings=0; verdict=SCOPE_REFINEMENT_NEEDED.

## Registers

- `Category_Register.csv` — flat category list and source-alignment citations.
- `Domain_Ledger_Gate3_Category_Draft.csv` — accepted Gate 2 atom rows plus proposed CategoryID assignments; `Atomic_Domain_Ledger.csv` is not overwritten.
- `Category_Scope_Ratification.csv` — BM25 and dense scope ratification with blocking refinement verdicts.
- `Category_Assignment_Findings.csv` — ambiguous assignment candidates requiring Gate 3 review. Dense and BM25 misses are retained in `Category_Scope_Ratification.csv`; formal assignment review candidates remain in `Category_Assignment_Findings.csv`.
- `Category_Assignment_Summary.csv` — per-category counts.

## Gate 3 Closure Condition

Gate 3 may close only after the human confirms:

> Yes, Categories are correct, each IN-scope unit belongs to exactly one Category, every Category carries a `CLUSTER_COHERENT` ratification verdict, and all misassignment candidates have been resolved (advisory `LOW_COHESION` findings reviewed and accepted).
