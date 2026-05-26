# Dependencies: DEL-025-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract run 2026-05-25)
**Default maturity threshold:** ACCEPTED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

**Total ACTIVE rows:** 9 | **ANCHOR:** 3 | **EXECUTION:** 6

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetID / TargetName | SatisfactionStatus | Confidence |
|---|---|---|---|---|---|---|---|---|
| DEP-025-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0026 | TBD | HIGH |
| DEP-025-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | REQ-025-04-01 | TBD | HIGH |
| DEP-025-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | REQ-025-04-04 | TBD | HIGH |
| DEP-025-04-004 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-025-01_scope-of-work | PENDING | HIGH |
| DEP-025-04-005 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-025-02_package-datasheet | PENDING | HIGH |
| DEP-025-04-006 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-025-05_vendor-document-turnover-package | TBD | HIGH |
| DEP-025-04-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-025-06_epc-vendor-package-review-and-acceptance | TBD | HIGH |
| DEP-025-04-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | 26020-Package_Requirements.docx | PENDING | MEDIUM |
| DEP-025-04-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | 26020-Packages_Interfaces_4_export.xlsx | PENDING | MEDIUM |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; candidate source documents found: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`, `_REFERENCES.md`
- **ANCHOR_DOC:** `Datasheet.md` (contains identification, WBS, scope items, objectives — highest anchor signal)
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary execution signal), `Specification.md`, `Guidance.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used to validate anchor targets and resolve canonical deliverable IDs
- **Decomposition status:** AVAILABLE — DELIVERABLE_REGISTER.csv and PACKAGE_REGISTER.csv consulted; PKG-025 and all DEL-025-* IDs confirmed
- **Parent anchor:** DEP-025-04-001 anchors to SOW-0026 (scope item / WBS node) — 1 IMPLEMENTS_NODE row found (integrity check: PASS)
- **Trace anchors:** DEP-025-04-002 and DEP-025-04-003 trace to requirements REQ-025-04-01 and REQ-025-04-04 as representative explicit requirements with cross-deliverable interface implications
- **Binary sources not text-extractable:** `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` are referenced authoritative sources but locally inaccessible as readable text (CT-03 / HRR-025-04-003). Dependencies DEP-025-04-008 and DEP-025-04-009 registered as INTERFACE / PENDING with MEDIUM confidence pending text extraction.
- **Open conflicts:** CT-01 (motor HP rating TBD), CT-02 (per-unit VFD allocation TBD), CT-03 (binary source files) — these affect SatisfactionStatus of DEP-025-04-005 (DEL-025-02 prerequisite) but do not generate additional dependency rows under CONSERVATIVE strictness.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 9 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 5 |
| PENDING | 4 |
| SATISFIED | 0 |

**ANCHOR / EXECUTION split:** 3 ANCHOR, 6 EXECUTION

**Tree x DAG integrity:**
- IMPLEMENTS_NODE rows (ACTIVE): 1 — PASS
- FLOATING_NODE warning: NO

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE; decomposition AVAILABLE (GATE-07); 9 rows written (3 ANCHOR, 6 EXECUTION); schema VALID; no RETIRED rows (first extraction run). Binary sources 26020-Package_Requirements.docx and 26020-Packages_Interfaces_4_export.xlsx inaccessible (CT-03); registered as INTERFACE/PENDING rows DEP-025-04-008 and DEP-025-04-009.
