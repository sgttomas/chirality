# Gate 4 (Knowledge Types & Subjects) — progress checkpoint

Persona: **DOMAIN_DECOMP**. Decomposing `projects/chirality-piping/` into
`domains/chirality-piping/`. cwd for all commands = monorepo root
`/Users/ryan/ai-env/projects/chirality`. WRITE_SCOPE = repo-metadata only; no
content invention (AOP-08 → TBD); commit/push only when operator asks.

## Method (mirrors accepted chirality-app-dev Gate 4)
Knowledge-kind KTY axis + finest-faithful subjects, generalized to 30 categories.
- **18 deliverable categories CAT-001..018 (PKG-00..17):** the 4 author doc kinds
  Datasheet→Reference / Specification / Guidance / Procedure (1:1 persona canonical
  schemas), routed by the `<DocKind>.md` in each atom's DEL SourceRef. Subjects =
  per (KTY, DEL-NN-MM). All 18 cats had a clean 4-doc-kind structure (0 no-match).
- **12 cross-cutting categories CAT-019..030:** content-kind KTYs routed by
  SourceDoc (first-match-wins). Subjects = per-source-doc (doc cats CAT-019..025);
  per-source-directory (code cats CAT-026..030, author folder grain).
Deterministic SOURCE_ROUTING; semantic signal reserved for ratification only.
Lossless: no atom splits, Gate-3 columns byte-identical (0 diffs / 21,912 rows).

## Adapter scripts (pack-local `_adapter/`)
- `gate4_assign.py` → embeds the hand-authored KTY taxonomy; writes
  `Knowledge_Type_Register.csv` (98 KTYs), `Knowledge_Subject_Register.csv`
  (630 subjects), `KTY_Assignment_Summary.csv`, `Domain_Ledger_Gate4_KTY_Draft.csv`.
- `gate4_ratify.py` → binding KTY ratification over the dense V2 index
  (nearest-centroid cohesion WITHIN parent category; scope-query cosine + BM25
  diagnostic) → `KTY_Scope_Ratification.csv` + `KTY_Assignment_Findings.csv`.

## DONE — assignment + ratification + proposal (awaiting operator Gate-4 confirmation)
- `gate4_assign.py`: **98 KTYs, 630 subjects, 21,256 IN atoms assigned (100%),
  0 unmapped, 0 empty KTYs.** Per-cat KTYs: 4 each for 18 deliverable cats (72);
  1–5 for cross-cutting cats (26). Subject CoversUnits sum = 21,256.
- `gate4_ratify.py` (index `SRCIDX_20260617T014930Z`, no rebuild — reused the
  READY Gate-3 dense index): **98/98 CLUSTER_COHERENT, 0 blocking.** Own-centroid
  cos median 0.713 / 0.749 / 0.784 (min/med/max); within-cat cohesion
  0.495 / 0.716 / 1.000. Single-KTY cats (5 code + CAT-023) → cohesion 1.0.
  **99 advisory misassignment candidates** (0.47% of IN; concentrated CAT-019
  arch↔spec adjacency, CAT-012/018/025) → proposed RESOLVE_SOURCE_ROUTING.
- Integrity validator: 2 CRITICAL = expected future-gate annexes (objectives →
  Gate 4/5; coverage → Gate 5). ktys/subjects annexes now satisfied. No Gate-4 problem.
- Proposal pack: `gate4_kty/GATE4_KTY_PROPOSAL_20260617T152804Z/`
  (Knowledge_Type_Register, Knowledge_Subject_Register, KTY_Assignment_Summary,
  KTY_Scope_Ratification, KTY_Assignment_Findings, Gate4 draft ledger,
  Domain_Integrity_Report/Findings, GATE4_KTY_PROPOSAL.md, HANDOFF_STATE.md).

## GATE 4 ACCEPTED (operator, 2026-06-17)
99 misassignment candidates resolved **RESOLVE_SOURCE_ROUTING** (retain author
placement, G4BR-001) — stamped Status=RESOLVED_SOURCE_ROUTING in
`KTY_Assignment_Findings.csv` (0 open); ledger `Gate4AssignmentStatus`=ACCEPTED_GATE4
for all 21,256 IN atoms; KTY + Subject register Status=ACCEPTED_GATE4; proposal MD
status = ACCEPTED. IntendedUsers/WhenUsed left TBD per persona allowance.
Acceptance snapshot: `gate_snapshots/GATE4_KTY_20260617T153218Z/` (GATE4_ACCEPTANCE.md
+ artifact SHA-256; Token GATE4_ACCEPT_20260617); `_LATEST_GATE4.md` updated.
Gate 4 frozen baseline: 98 KTYs, 630 subjects, 21,256 IN atoms assigned.

**NEXT (do NOT start until operator says so): Gate 5 (Verify Coverage)** by adapting
`domains/chirality-app-dev/_Decomposition/_adapter/gate5_*.py`.

## Frozen inputs (Gate 3 accepted baseline)
`Domain_Ledger_Gate3_Category_Draft.csv` = 21,256 IN atoms over 30 categories;
`Category_Register.csv` = 30 categories. Dense index `SRCIDX_20260617T014930Z`
(BAAI/bge-base-en-v1.5, 36,263 chunks, READY).
