# Gate 3 — Category Proposal (chirality-piping)

**Status:** ACCEPTED — operator-confirmed Gate 3 on 2026-06-16. 943 misassignment
candidates resolved RESOLVE_SOURCE_ROUTING (retain author placement, G3BR-006).

## Method
Faithful-to-author reconciliation (operator directive; mirrors chirality-app-dev).
The piping corpus is strongly author-structured, so categories preserve that
structure rather than re-clustering it:
- **18 execution deliverable packages PKG-00..17 → CAT-001..018** (1:1).
- **12 cross-cutting categories CAT-019..030** reconciling the docs/, governance,
  root, and code bodies.
Assignment is deterministic **source-routing** (`gate3_assign.py`, rules
G3BR-001..007): each IN atom inherits the category owning its author-placed PKG /
source group. No atom splits, no UnitStatement/ContentHash edits (lossless).

## Result
- **30 flat categories**; **21,256 IN atoms** assigned (exactly one each); 0
  unmapped, 0 bad category refs. 509 TBD + 147 OUT left uncategorized (G3BR-007).
- Per-category mass balanced (smallest CAT-029 Developer Tooling = 133; largest
  CAT-026 Core Engine Source = 2,783); no empty categories.
- Binding retrieval ratification (`gate3_ratify.py`) over the dense V2 index
  (`SRCIDX_20260617T014930Z`, BAAI/bge-base-en-v1.5, 36,263 chunks):
  **30/30 CLUSTER_COHERENT, 0 blocking.** Own-centroid cosine median
  **0.713–0.771** (every category is a tight, separable content cluster; ~21x the
  1/30 = 0.033 random baseline). Scope-query cosine + BM25 retained as diagnostics
  (0.75 human-gated, G3BR-012).
- **943 misassignment candidates** (4.4% of IN atoms) — atoms whose nearest
  content centroid is a *different* category by margin >0.05. These are semantic
  adjacencies (e.g. spec/requirements atoms near the engine features they specify;
  doc categories sharing vocabulary), correctly disambiguated by author
  document-of-origin. Resolution: RESOLVE_SOURCE_ROUTING (retain by author placement) — operator-confirmed.
- Two doc categories show low nearest-centroid cohesion — CAT-019 Product
  Requirements/Spec/Architecture (0.10) and CAT-022 Guides/Examples (0.14) — but
  both keep high own-centroid cosine (0.716 / 0.725), so the clusters are coherent;
  their atoms simply sit adjacent to neighbouring doc categories (dominant adjacent
  CAT-021 IP/Security). Expected doc-vocabulary overlap, not misassignment.

## Category taxonomy
CAT-001..018 — PKG-00..17 deliverable packages (Software Architecture Runway;
Governance/IP/Professional Responsibility; Domain Model/Units/Schemas; Piping
Components/Materials/Library; Solver Core/Numerical Methods; Loads/Load
Cases/Stress Recovery; Rule Packs/Code-Check Engine; GUI/Engineering Workflow;
Reporting/Audit/Reproducibility; Verification/Validation/Quality Oracles;
Build/Packaging/API/Interoperability; Documentation/Examples/Education;
Security/Privacy/Private Data; Physical Design Knowledge/Constraint Engine; Model
States/Analysis Runs/Comparison; Handoff/External Prover; Model Operation/Agent
Proposal; Export Format Interoperability).
CAT-019 Product Requirements/Spec/Architecture · CAT-020 Dev Process/Build/
Release/Validation · CAT-021 IP/Data Boundary/Security/Privacy Policy · CAT-022
User/Developer/Contributor Guides/Examples · CAT-023 Decomposition/Reconciliation
Records · CAT-024 Scope-Change Governance · CAT-025 Repository Operating
Posture/Contribution Governance · CAT-026 Core Engine Source · CAT-027
Application/GUI Source · CAT-028 Test Suites · CAT-029 Developer Tooling/Scripts ·
CAT-030 Validation/Quality-Oracle Implementation.

## Integrity
`validate_domain_decomposition_integrity.py`: 4 CRITICAL findings, all
expected-absent future-gate annexes (ktys/subjects → Gate 4, objectives →
Gate 4/5, coverage → Gate 5). No Gate-3 (category/ledger) integrity problem.

## Index-manifest note
The dense source index was built from a derived `_Sources/Source_Manifest.index.csv`
(non-markdown rows flipped to IncludeInIndex=NO; the v1 source-DB builder only
chunks markdown raw sources). The canonical Source_Manifest.csv is unchanged.
Code/schema atoms remain in the retrieval index as LEDGER_ATOM chunks from the
domain ledger, so ratification coverage is complete (all 21,912 atoms indexed).
