# Dependencies: DEL-012-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (updated by dependency-extract run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Total ACTIVE rows: 11 | ANCHOR: 7 | EXECUTION: 4 | RETIRED: 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-012-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0013 | Scope decision SOW-0013 — 10KVA AC UPS (WBS 02) | HIGH | ACTIVE |
| DEP-012-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 | HIGH | ACTIVE |
| DEP-012-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 | HIGH | ACTIVE |
| DEP-012-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 | HIGH | ACTIVE |
| DEP-012-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 | HIGH | ACTIVE |
| DEP-012-04-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | HIGH | ACTIVE |
| DEP-012-04-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | HIGH | ACTIVE |
| DEP-012-04-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-012-01_scope-of-work | Scope of Work | HIGH | ACTIVE |
| DEP-012-04-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-012-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-012-04-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-012-05_vendor-document-turnover-package | Vendor Document Turnover Package | HIGH | ACTIVE |
| DEP-012-04-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-012-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs (AUTO):** Datasheet.md (ANCHOR_DOC), Specification.md, Procedure.md, Guidance.md (EXECUTION_DOC_ORDER)
- **Decomposition path:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (used for anchor validation and label resolution)
- **_REFERENCES.md:** Present; used to confirm decomposition path and note that no deliverable-specific source slices were copied during PREPARATION.
- **Anchor resolution:** SOW-0013 confirmed in SCOPE_LEDGER.csv; DEL-012-04 confirmed in DELIVERABLE_REGISTER.csv; OBJ-002/004/005/008/009/010 confirmed in OBJECTIVE_DELIVERABLE_MAP context from Datasheet.md.
- **Execution edges:** DEL-012-01 (Scope of Work) and DEL-012-02 (Package Datasheet) are explicit upstream prerequisites per Specification.md Scope section and Datasheet.md Attributes ("developed from the EPC package Scope of Work and Package Datasheet"). DEL-012-05 (Vendor Document Turnover Package) and DEL-012-06 (EPC Vendor Package Review and Acceptance) are downstream handover targets per Guidance.md and Procedure.md step 9.
- **Parent anchor count:** 1 (DEP-012-04-001, IMPLEMENTS_NODE, SOW-0013) — no FLOATING_NODE warning.
- **No AMBIGUOUS_ANCHOR:** exactly one IMPLEMENTS_NODE row.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. Mode: UPDATE. Strictness: CONSERVATIVE. Decomposition: GATE-07_Final_Published_2026-05-24. 11 ACTIVE rows written (7 ANCHOR, 4 EXECUTION). No warnings.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 11 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 11 |
