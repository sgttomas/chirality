# Dependencies: DEL-028-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (updated by dependency-extract run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

**Total ACTIVE rows:** 16
**ANCHOR rows (ACTIVE):** 8 (1 IMPLEMENTS_NODE + 7 TRACES_TO_REQUIREMENT)
**EXECUTION rows (ACTIVE):** 8 (3 UPSTREAM + 5 DOWNSTREAM)
**RETIRED rows:** 0

| DependencyID | Class | AnchorType | Dir | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-028-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0029 | Scope decision SOW-0029 — Transformer TXP-8801-1 (WBS 01) | HIGH | ACTIVE |
| DEP-028-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 — 04-25 Deepcut facility scope | HIGH | ACTIVE |
| DEP-028-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 — vendor-owned package execution model | HIGH | ACTIVE |
| DEP-028-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — facility electrical power and transformer integration | HIGH | ACTIVE |
| DEP-028-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 — controls instrumentation and communications interfaces | HIGH | ACTIVE |
| DEP-028-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — civil structural foundations and maintenance access | HIGH | ACTIVE |
| DEP-028-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — sour-service safety regulatory codes and standards | HIGH | ACTIVE |
| DEP-028-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — operability maintainability vendor documentation and turnover | HIGH | ACTIVE |
| DEP-028-01-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | — | Gate 7 decomposition registers (DELIVERABLE_REGISTER / PACKAGE_REGISTER / SCOPE_LEDGER / INTERFACE_REGISTER) | HIGH | ACTIVE |
| DEP-028-01-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | — | Workbook Packages row 30 — 26020-Packages_Interfaces_4_export | HIGH | ACTIVE |
| DEP-028-01-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | — | DBM Deepcut Electrical basis (lines 2917-2991) | HIGH | ACTIVE |
| DEP-028-01-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-028-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-028-01-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-028-03_construction-work-package | Construction Work Package | HIGH | ACTIVE |
| DEP-028-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-028-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-028-01-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-028-05_vendor-document-turnover-package | Vendor Document Turnover Package | MEDIUM | ACTIVE |
| DEP-028-01-016 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-028-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; ANCHOR_DOC: `Datasheet.md` (contains identification, scope-item, and objective fields); EXECUTION_DOCS: `Specification.md`, `Procedure.md`, `Guidance.md`.
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — used for anchor validation, canonical label resolution, and downstream deliverable ID resolution.
- **Anchor validation:** SOW-0029 confirmed in SCOPE_LEDGER.csv. OBJ-001/004/005/006/008/009/010 confirmed in OBJECTIVE_REGISTER.csv and DELIVERABLE_REGISTER.csv row DEL-028-01. Downstream deliverable IDs DEL-028-02 through DEL-028-06 confirmed in DELIVERABLE_REGISTER.csv.
- **Tree integrity:** 1 IMPLEMENTS_NODE row (DEP-028-01-001). No FLOATING_NODE or AMBIGUOUS_ANCHOR warnings.
- **Execution edges:** 3 UPSTREAM INTERFACE rows (Gate 7 registers, workbook row 30, DBM Deepcut electrical); 5 DOWNSTREAM ENABLES rows (DEL-028-02 through DEL-028-06). No geotechnical or external prerequisite dependencies were found in PKG-028 source documents — this is an Electrical/vendor package with no analogous civil/survey inputs.
- **CONSUMER_CONTEXT=NONE:** No ConsumerHint or EstimateImpactClass extension columns added.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 16 |
| RETIRED | 0 |

| SatisfactionStatus | Count (ACTIVE) |
|---|---|
| TBD | 13 |
| SATISFIED | 3 |
| PENDING | 0 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Created Dependencies.csv with 16 ACTIVE rows (8 ANCHOR + 8 EXECUTION). No RETIRED rows. Schema validation: VALID.
