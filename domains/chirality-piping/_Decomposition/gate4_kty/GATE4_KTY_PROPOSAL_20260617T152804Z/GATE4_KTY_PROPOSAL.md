# Gate 4 — Knowledge Types & Subjects Proposal (chirality-piping)

**Status:** ACCEPTED (operator, 2026-06-17). 99 candidates RESOLVED_SOURCE_ROUTING.
**Snapshot:** GATE4_KTY_PROPOSAL_20260617T152804Z

## Method
Knowledge-kind KTY axis + finest-faithful subjects (mirrors the accepted
chirality-app-dev Gate 4, generalized to the 30-category piping taxonomy). KTYs
are the knowledge KINDS the authors actually used:
- **18 deliverable categories CAT-001..018 (= PKG-00..17):** the four author
  document kinds **Datasheet→Reference / Specification / Guidance / Procedure**
  (1:1 with the persona canonical schemas), routed by the doc-kind in each atom's
  `@repo/.../DEL-NN-MM_.../​<DocKind>.md` SourceRef. Subjects = per-deliverable
  (per (KTY, DEL-NN-MM)).
- **12 cross-cutting categories CAT-019..030:** content-kind KTYs routed by
  SourceDoc (first-match-wins patterns). Subjects = per-source-doc for the doc
  categories (CAT-019..025); per-source-directory for the five code categories
  (CAT-026..030), using the author's own folder grain.

Assignment is deterministic **SOURCE_ROUTING** (`_adapter/gate4_assign.py`).
Semantic signal is NOT used to override author placement — it is reserved for the
ratification verification layer. No atom splits; lossless.

## Result
- **98 Knowledge Types**, **630 Knowledge Subjects**; all **21,256 IN atoms**
  carry one primary KTY + one primary Subject (100% coverage; **0 unmapped; 0
  empty KTYs**).
- Per-category KTY counts: 4 for each deliverable category (72 total); 1–5 for
  the cross-cutting categories (26 total).
- CoversUnits populated for every subject (sum = 21,256 = all IN atoms).
- Binding KTY ratification (`_adapter/gate4_ratify.py`, dense index
  `SRCIDX_20260617T014930Z`, BAAI/bge-base-en-v1.5; nearest-centroid cohesion
  computed WITHIN each parent category):
  **98/98 CLUSTER_COHERENT, 0 blocking.** Own-centroid cosine median
  **0.713 / 0.749 / 0.784** (min/median/max); within-category KTY cohesion
  **0.495 / 0.716 / 1.000**. Single-KTY categories (the five code categories +
  CAT-023) trivially report cohesion 1.0. Scope-query cosine + BM25 are
  diagnostic (0.75 human-gated).
- **99 misassignment candidates** (0.47% of IN atoms) — atoms whose nearest
  within-category KTY centroid differs by margin (concentrated in CAT-019
  architecture↔spec prose adjacency, plus CAT-012/018/025). Proposed
  **RESOLVE_SOURCE_ROUTING** (author doc/source placement authoritative) —
  pending operator confirmation, exactly as the 943 Gate-3 candidates were
  resolved.

## Integrity
`validate_domain_decomposition_integrity.py`: **2 CRITICAL findings, both
expected-absent future-gate annexes** (objectives → Gate 4/5 objectives layer,
coverage → Gate 5). The knowledge-types and subjects annexes that Gate 3 reported
missing are now **satisfied**. No Gate-4 problem.

## Lossless
Gate-3 columns (UnitStatement / ContentHash / CategoryID) are **byte-identical**
vs the accepted Gate-3 ledger (0 diffs over all 21,912 rows); Gate-4 columns
appended only.

## Pack contents
`Knowledge_Type_Register.csv`, `Knowledge_Subject_Register.csv`,
`KTY_Assignment_Summary.csv`, `KTY_Scope_Ratification.csv`,
`KTY_Assignment_Findings.csv`, `Domain_Ledger_Gate4_KTY_Draft.csv`,
`Domain_Integrity_Report.md`, `Domain_Integrity_Findings.csv`.
