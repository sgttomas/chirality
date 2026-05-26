# Dependencies: DEL-038-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

16 rows extracted (16 ACTIVE, 0 RETIRED).

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | SatisfactionStatus | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| DEP-038-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0039 | Scope Item SOW-0039 — 600V ELECTRICAL BUILDING (820-1) | SATISFIED | HIGH |
| DEP-038-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | OBJ-001 — Provide 04-25 Deepcut facility scope | SATISFIED | HIGH |
| DEP-038-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | OBJ-004 — Vendor-owned package execution | SATISFIED | HIGH |
| DEP-038-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | OBJ-005 — Facility electrical power basis | SATISFIED | HIGH |
| DEP-038-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | OBJ-006 — Controls instrumentation communications | SATISFIED | HIGH |
| DEP-038-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | OBJ-007 — Shared utilities and ancillary support | SATISFIED | HIGH |
| DEP-038-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | OBJ-008 — Civil structural site buildings | SATISFIED | HIGH |
| DEP-038-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | OBJ-009 — Safety relief flare regulatory | SATISFIED | HIGH |
| DEP-038-02-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | OBJ-010 — Operability maintainability commissioning | SATISFIED | HIGH |
| DEP-038-02-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-038-01_scope-of-work | Scope of Work — PKG-038 | SATISFIED | HIGH |
| DEP-038-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07 | Gate 7 PROJECT_DECOMP Snapshot | SATISFIED | HIGH |
| DEP-038-02-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-DEEPCUT | DBM Deepcut 4-25_Deepcut_DBM.md | SATISFIED | HIGH |
| DEP-038-02-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | WORKBOOK-PKG-ROW-40 | Workbook Packages sheet row 40 | SATISFIED | HIGH |
| DEP-038-02-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DOCUMENT | PKG-REQ-DOCX | 26020-Package_Requirements.docx — PKG-038 slice | PENDING | MEDIUM |
| DEP-038-02-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-038-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package — PKG-038 | TBD | HIGH |
| DEP-038-02-016 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-038-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance — PKG-038 | TBD | MEDIUM |

## Run Notes

- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; primary anchor doc: `Datasheet.md` (filename contains `datasheet`); execution docs: `Procedure.md`, `Guidance.md`, `Specification.md`.
- **Decomposition path:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (resolved from `_CONTEXT.md` Decomposition Reference; GATE-07 is the accepted final published snapshot).
- **Anchor resolution:** `SOW-0039` confirmed in `GATE-07/SCOPE_LEDGER.csv`. All eight objectives confirmed in `GATE-07/OBJECTIVE_REGISTER.csv`.
- **Execution edges:** DEL-038-01 identified as upstream PREREQUISITE (owns `_CONTEXT.md` / `_STATUS.md`); Gate 7 snapshot, DBM, and workbook row 40 are document prerequisites confirmed in `Procedure.md`. DEP-038-02-014 flagged PENDING: PKG-038 slice of `26020-Package_Requirements.docx` not yet processed (Guidance conflict HRR-038-02-002).
- **Downstream handover:** DEP-038-02-015 (DEL-038-04) is FACT; DEP-038-02-016 (DEL-038-06) is PROPOSAL (inferred from SOW-0039 deliverable set and EPC Integrator review responsibility).
- **Parent anchor check:** 1 IMPLEMENTS_NODE row — OK.
- **No warnings:** FLOATING_NODE, AMBIGUOUS_ANCHOR, and MISSING_DECOMPOSITION conditions are all clear.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 16 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 11 |
| PENDING | 1 |
| TBD | 2 |
| IN_PROGRESS | 0 |
| WAIVED | 0 |
| NOT_APPLICABLE | 0 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — UPDATE run; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE. Decomposition: GATE-07 snapshot confirmed. Extracted 16 rows (9 ANCHOR + 7 EXECUTION). 16 ACTIVE, 0 RETIRED. No integrity warnings.
