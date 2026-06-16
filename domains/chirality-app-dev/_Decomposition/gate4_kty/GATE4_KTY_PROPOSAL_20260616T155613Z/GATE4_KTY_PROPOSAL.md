# Gate 4 — Knowledge Types & Subjects Proposal (chirality-app-dev)

**Status:** PROPOSED — awaiting human Gate-4 confirmation.

## Method
Knowledge-kind KTY axis + per-deliverable subjects (operator decisions). KTYs are
the knowledge KINDS the authors used: the 11 PKG categories each get the 4 document
kinds Datasheet→Reference / Specification / Guidance / Procedure (1:1 with persona
canonical schemas); the 5 cross-cutting categories get content-kind KTYs. Assignment
is deterministic SOURCE_ROUTING (doc-kind + deliverable from each atom's @repo path;
cross-cutting by SourceDoc) via _adapter/gate4_assign.py. No atom splits; lossless.

## Result
- **59 Knowledge Types**, **279 Knowledge Subjects**; 11,140 IN atoms each carry one
  primary KTY + one primary Subject (100% coverage; 0 unmapped; 0 empty KTYs).
- CoversUnits populated for every subject (sum = 11,140).
- Binding KTY ratification (gate4_ratify.py, dense index SRCIDX_20260616T043733Z;
  nearest-centroid cohesion computed WITHIN each parent category):
  **59/59 CLUSTER_COHERENT, 0 blocking.** Own-centroid cosine median 0.71–0.78;
  within-category KTY cohesion 0.65–0.84. Scope-query cosine + BM25 diagnostic
  (0.75 human-gated).
- **49 misassignment candidates** (0.4% of IN atoms) — atoms whose nearest
  within-category KTY differs (mostly CAT-012 Product-Requirements ↔
  Conceptual-Overview prose adjacency). Proposed RESOLVE_SOURCE_ROUTING (author
  doc/source placement authoritative) — pending operator confirmation.

## Integrity
validate_domain_decomposition_integrity.py: 2 CRITICAL findings, both
expected-absent future-gate annexes (objectives → Gate 4/5, coverage → Gate 5).
Knowledge-types/subjects annexes satisfied.

## Lossless
Gate-3 columns (UnitStatement/ContentHash/CategoryID) unchanged vs the Gate-3
ledger; Gate-4 columns appended only.
