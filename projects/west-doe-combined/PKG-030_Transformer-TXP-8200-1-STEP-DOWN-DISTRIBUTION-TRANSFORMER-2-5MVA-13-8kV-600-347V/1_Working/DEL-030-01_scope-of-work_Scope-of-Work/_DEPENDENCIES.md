# Dependencies: DEL-030-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

**Register:** `Dependencies.csv` (v3.1) — 10 rows, all ACTIVE.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetID / TargetName | Confidence | SatisfactionStatus |
|---|---|---|---|---|---|---|---|---|
| DEP-030-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0031 — Scope Item | HIGH | TBD |
| DEP-030-01-002 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-030 | HIGH | TBD |
| DEP-030-01-003 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | Gate 7 DECOMP Snapshot | HIGH | TBD |
| DEP-030-01-004 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | PACKAGE_REGISTER.csv row PKG-030 | HIGH | TBD |
| DEP-030-01-005 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM Deepcut 4-25_Deepcut_DBM.md | HIGH | TBD |
| DEP-030-01-006 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-030-02 Package Datasheet | HIGH | TBD |
| DEP-030-01-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-030-03 Construction Work Package | HIGH | TBD |
| DEP-030-01-008 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-030-04 Vendor Engineered Equipment Package | HIGH | TBD |
| DEP-030-01-009 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-030-05 Vendor Document Turnover Package | HIGH | TBD |
| DEP-030-01-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-030-06 EPC Vendor Package Review and Acceptance | HIGH | TBD |

## Run Notes

**Run date:** 2026-05-25
**Mode:** UPDATE
**Strictness:** CONSERVATIVE
**Consumer context:** NONE
**Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
**Decomposition status:** PRESENT — anchor identifiers validated against SCOPE_LEDGER.csv, PACKAGE_REGISTER.csv, and DELIVERABLE_REGISTER.csv.
**Source docs scanned (AUTO):** Datasheet.md, Specification.md, Guidance.md, Procedure.md
**ANCHOR_DOC (AUTO):** Datasheet.md (contains identity fields, CoversScopeItems, ParentPackageID — highest anchor signal)
**EXECUTION_DOC_ORDER (AUTO):** Guidance.md (Purpose section explicit downstream list), Procedure.md (Prerequisites explicit upstream list), Specification.md (verification hooks)

**[WARNING] AMBIGUOUS_ANCHOR:** Two IMPLEMENTS_NODE rows emitted (DEP-030-01-001 targeting SOW-0031 as WBS_NODE, DEP-030-01-002 targeting PKG-030 as PACKAGE). These are distinct target types representing the same parent relationship viewed at different decomposition levels (scope ledger vs package register). Both are source-supported and HIGH confidence. A strict single-parent-anchor interpretation would prefer DEP-030-01-001 (scope item) as the WBS_NODE anchor; DEP-030-01-002 is the package-level anchor. No auto-repair performed under CONSERVATIVE strictness; preserved for human review.

**Previous state:** `Dependencies.csv` did not exist. This is a first extraction run.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 10 |

**ANCHOR rows (ACTIVE):** 2
**EXECUTION rows (ACTIVE):** 8
- UPSTREAM: 3 (all PREREQUISITE)
- DOWNSTREAM: 5 (all ENABLES)

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. Mode: UPDATE. Strictness: CONSERVATIVE. Decomposition: PRESENT (GATE-07_Final_Published_2026-05-24). Source docs: Datasheet.md, Specification.md, Guidance.md, Procedure.md. 10 ACTIVE rows written. Warnings: AMBIGUOUS_ANCHOR (two IMPLEMENTS_NODE rows — WBS_NODE SOW-0031 and PACKAGE PKG-030).
