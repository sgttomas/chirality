# Dependencies: DEL-077-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** Prefer `Dependencies.csv` when produced by `TASK + dependency-extract`; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` generated 2026-05-25 by `TASK + dependency-extract` (MODE=UPDATE, STRICTNESS=CONSERVATIVE).

**Counts:** 14 ACTIVE rows, 0 RETIRED rows.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-A90DB383 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0143 | Scope Ledger: Methanol Injection distinct flat project package WBS 01 | HIGH | ACTIVE |
| DEP-9E1CA384 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Facility Scope Objective | HIGH | ACTIVE |
| DEP-FE7EBBC2 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Vendor-Package Execution Model Objective | HIGH | ACTIVE |
| DEP-940D4E88 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Electrical Power Integration Objective | HIGH | ACTIVE |
| DEP-E44AA1E5 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Controls Integration Objective | HIGH | ACTIVE |
| DEP-785FC98D | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Shared Utilities (Fuel Gas) Objective | HIGH | ACTIVE |
| DEP-8E15E3BA | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Civil Objective | HIGH | ACTIVE |
| DEP-49B64528 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Sour-Service Safety Objective | HIGH | ACTIVE |
| DEP-1C8ABC3B | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Operability Objective | HIGH | ACTIVE |
| DEP-A5FAABAC | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Gate-07 PROJECT_DECOMP Snapshot (registers) | HIGH | ACTIVE |
| DEP-39CCFDFA | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | Workbook source slice row 72 (26020-Package_Requirements.docx / 26020-Packages_Interfaces_4_export.xlsx) | HIGH | ACTIVE |
| DEP-E833E97E | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-077-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-ECD4FB7D | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-077-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |
| DEP-F52FEB53 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-077-02_package-datasheet | Package Datasheet | MEDIUM | ACTIVE |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **DECOMPOSITION_PATH used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (resolved from `_CONTEXT.md` and `_REFERENCES.md`; provided DECOMPOSITION_PATH `GATE-07_Final_Published_2026-05-24/` did not exist as a directory — actual gate snapshot located under `_Decomposition/PROJECT_DECOMP/_GateSnapshots/`).
- **SOURCE_DOCS:** AUTO — scanned Datasheet.md, Specification.md, Guidance.md, Procedure.md, _CONTEXT.md, _REFERENCES.md (excluded _DEPENDENCIES.md as a dependency artifact).
- **ANCHOR_DOC:** Datasheet.md (highest-confidence match: contains "datasheet"; carries Identification table with WBS/scope/objective fields).
- **EXECUTION_DOC_ORDER:** Procedure.md (procedure/workflow signal), Specification.md, Guidance.md.
- **Pass 1 (ANCHOR):** 9 rows emitted. One IMPLEMENTS_NODE anchor to SOW-0143 (scope-ledger node); eight TRACES_TO_REQUIREMENT anchors to OBJ-001 and OBJ-004 through OBJ-010. All identifiers confirmed present in DELIVERABLE_REGISTER.csv and SCOPE_LEDGER.csv.
- **Pass 2 (EXECUTION):** 5 rows emitted. Two UPSTREAM PREREQUISITE rows (Gate-07 snapshot; workbook source slice row 72 — the latter has SatisfactionStatus=PENDING reflecting an open source-access gap). Two DOWNSTREAM ENABLES rows (DEL-077-04; DEL-077-06) drawn from DELIVERABLE_REGISTER.csv explicit statements. One UPSTREAM INTERFACE row to DEL-077-02 (parallel mandatory anchor deliverable sharing INTERFACE_REGISTER rows).
- **[WARNING] OPEN_PREREQUISITE:** DEP-39CCFDFA (workbook source slice row 72) has SatisfactionStatus=PENDING; tagged equipment list (REQ-077-01-03) cannot be finalized until this source is accessible.
- No legacy enum normalization required.
- No existing Dependencies.csv present prior to this run (first extraction).

## Lifecycle Summary

| Metric | Count |
|---|---|
| ACTIVE rows | 14 |
| RETIRED rows | 0 |
| ANCHOR / IMPLEMENTS_NODE | 1 |
| ANCHOR / TRACES_TO_REQUIREMENT | 8 |
| EXECUTION / UPSTREAM | 3 |
| EXECUTION / DOWNSTREAM | 2 |
| SatisfactionStatus=TBD | 13 |
| SatisfactionStatus=PENDING | 1 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run: MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (confirmed). 14 ACTIVE rows written. Schema: VALID (29 columns, 14 data rows). [WARNING] OPEN_PREREQUISITE: workbook source slice row 72 not yet accessible (DEP-39CCFDFA, SatisfactionStatus=PENDING).
