# GATE 3 — CATEGORIES ACCEPTANCE (chirality-app-dev)

Status: ACCEPTED
Accepted UTC: 20260616T153015Z
Token: GATE3_ACCEPT_20260616
Human confirmation: "Everything looks good ... resolve the 330 misassignment candidates by author source-routing" (resolved; gate passed).

## Result
- 16 flat categories (CAT-001..016), faithful-to-author (PKG-00..10 preserved 1:1 + 5 cross-cutting).
- 11,140 IN atoms assigned to exactly one Category (CategoryAssignmentStatus=ACCEPTED_GATE3); 562 TBD + 107 OUT uncategorized (TBD deferred, OI-013).
- Binding dense ratification (SRCIDX_20260616T043733Z, BAAI/bge-base-en-v1.5): 16/16 CLUSTER_COHERENT, 0 blocking; own-centroid cosine median 0.71-0.77.
- 330 misassignment candidates (semantic adjacency) RESOLVED_SOURCE_ROUTING (0 open).
- Scope-query cosine + BM25 retained as diagnostics (0.75 human-gated, G3BR-012).
- Lossless: UnitStatement/ContentHash unchanged vs Atomic_Domain_Ledger.csv; no atom splits.

## Accepted artifact SHA-256
- Category_Assignment_Findings.csv: 3156099b9cca8b12ede1ae3772e0f2937565a4d1df662387af348064ebc8aada
- Category_Assignment_Summary.csv: 2ae41935afcd965d2e8ae7bf7b61f8644935ac2c0a83175428f5a2985d6181ba
- Category_Boundary_Decisions.csv: 94aa906d3e50af664f016bbb7ac0b7d7b826360908008e247fb3533226c01d02
- Category_Register.csv: 3664548d387401fcfbd497ddf05aa8a78db9cfe001bc0c6c49fba4ac6a15b13d
- Category_Scope_Ratification.csv: 34ebf60b047652e4cbd33b0d6945a8bc5f4c752f6e7aa458f3a6c42dd62b3049
- Domain_Ledger_Gate3_Category_Draft.csv: e5087f36d42c95896d84b6d8e2682726a2a6ab072b10c5d297bb20487579fdfd

## Scope of this acceptance
Accepts the 16-category structural partition + per-IN-atom CategoryID as the basis for Gate 4 (Knowledge Types). Does not create Knowledge Type, Subject, coverage, or publication truth.
