# GATE 4 — KNOWLEDGE TYPES & SUBJECTS ACCEPTANCE (chirality-piping)

Status: ACCEPTED
Accepted UTC: 20260617T153218Z
Token: GATE4_ACCEPT_20260617
Human confirmation: "1. Yes 2. Yes, as with Gate 3. Proceed accordingly."

## Result
- KTY axis = knowledge-kind (author doc-types for the 18 deliverable categories; content kinds for the 12 cross-cutting categories); subjects = per-deliverable / per-source-doc / per-source-directory. 98 Knowledge Types, 630 Knowledge Subjects.
- 21,256 IN atoms each carry one primary KTY + one primary Subject (Gate4AssignmentStatus=ACCEPTED_GATE4); 100% coverage, 0 unmapped, 0 empty KTYs; CoversUnits populated (sum=21,256).
- Binding KTY ratification (SRCIDX_20260617T014930Z, within-category nearest-centroid): 98/98 CLUSTER_COHERENT, 0 blocking; own-centroid cosine median 0.749 (0.713-0.784); within-category cohesion median 0.716 (single-KTY code cats trivially 1.0).
- 99 misassignment candidates RESOLVED_SOURCE_ROUTING (0 open).
- IntendedUsers / WhenUsed left TBD per persona allowance; CanonicalSchema set per KTY.
- Lossless: UnitStatement/ContentHash/CategoryID byte-identical vs Gate-3 ledger (0 diffs / 21,912 rows); no atom splits.

## Accepted artifact SHA-256
- Domain_Ledger_Gate4_KTY_Draft.csv: 1e72a111fbf0e064ac743d3d04c6a9ebd0036f61166acd3141836a34b041c67b
- KTY_Assignment_Findings.csv: 132a60dfe56fa35cfbfc28809031f4e750cb3b1d1cb3e31bacf5905abdbd38d6
- KTY_Assignment_Summary.csv: f9f5af950345eceebed0a38bdae96b692f7b5f1da37a042d814694eee51cc685
- KTY_Scope_Ratification.csv: e8830a501d7b7537be4295cdddffe83aa39b1e1a0ea67e24198eef996e1c6121
- Knowledge_Subject_Register.csv: 8ef97f4b6fbd43956e0c2fd24493a5b7ba6f69eecefa1101a341f21dc2fd3eb8
- Knowledge_Type_Register.csv: c29d7016f8dcdbe09193a81ac808fde539bf5b41592af3cce38d589dc1ea0866

## Scope of this acceptance
Accepts the 98 Knowledge Types + 630 Subjects + per-IN-atom KTY/Subject assignment as the basis for Gate 5 (Coverage). Does not create coverage, objectives, or publication truth.
