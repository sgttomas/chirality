# Dependencies: DEL-022-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Extracted on 2026-05-25. Total ACTIVE rows: 15.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-022-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0023 | Scope decision SOW-0023 — 5kV SWITCHGEAR EQUIPMENT | HIGH | ACTIVE |
| DEP-022-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 | HIGH | ACTIVE |
| DEP-022-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 | HIGH | ACTIVE |
| DEP-022-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 | HIGH | ACTIVE |
| DEP-022-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 | HIGH | ACTIVE |
| DEP-022-04-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 | HIGH | ACTIVE |
| DEP-022-04-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | HIGH | ACTIVE |
| DEP-022-04-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | HIGH | ACTIVE |
| DEP-022-04-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-022-01_scope-of-work | Scope of Work | HIGH | ACTIVE |
| DEP-022-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-022-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |
| DEP-022-04-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | UNKNOWN | ELC-QAS-000007-001 | Project Specification ELC-QAS-000007-001 — Medium Voltage Switchgear Rev 1 | HIGH | ACTIVE |
| DEP-022-04-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | UNKNOWN | ELC-QAS-000003-001 | Project Specification ELC-QAS-000003-001 — Electrical Requirements for Packaged Equipment Rev 2 | HIGH | ACTIVE |
| DEP-022-04-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | studies-set | Facility Electrical Studies (short-circuit; relay coordination/arc-flash; load-flow; load analysis) | HIGH | ACTIVE |
| DEP-022-04-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-022-05_vendor-document-turnover-package | Vendor Document Turnover Package | HIGH | ACTIVE |
| DEP-022-04-015 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-022-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH | ACTIVE |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 15 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 15 |

**Closure state:** All rows TBD — dependency register initialized; satisfaction tracking not yet commenced.

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder: `Datasheet.md`, `Procedure.md`, `Guidance.md`, `Specification.md`. No `_REFERENCES.md` document pointers were used to originate new rows; `_REFERENCES.md` was available but rows were driven by explicit source text.
- **ANCHOR_DOC:** `Datasheet.md` (contains Identification table with WBS, package, SOW, and objectives pointers).
- **EXECUTION_DOC_ORDER:** `Procedure.md` (prerequisites and steps), `Specification.md` (requirements), `Guidance.md` (considerations).
- **DECOMPOSITION_PATH:** `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used to validate anchor targets (SOW-0023, OBJ-* values confirmed in DELIVERABLE_REGISTER.csv row DEL-022-04).
- **Pass 1 (ANCHOR):** One parent anchor emitted (SOW-0023 per DELIVERABLE_REGISTER.csv). Seven objective trace anchors emitted (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 confirmed in DELIVERABLE_REGISTER.csv).
- **Pass 2 (EXECUTION):** Five EXECUTION rows emitted — two upstream PREREQUISITE deliverables (DEL-022-01, DEL-022-02 per Specification R-01 and Procedure prerequisites), two upstream PREREQUISITE specifications (ELC-QAS-000007-001 R-03, ELC-QAS-000003-001 R-04), one upstream PREREQUISITE document set (facility electrical studies R-05 / Procedure step 8), two downstream HANDOVER deliverables (DEL-022-05 and DEL-022-06 per Datasheet Construction section and Procedure step 10).
- **Integrity check — parent anchor count:** 1 IMPLEMENTS_NODE row (DEP-022-04-001). OK.
- **Open HRR items:** HRR-022-04-001 (bus voltage TBD), HRR-022-04-002 (equipment allocation TBD), HRR-022-04-003 (4.16 kV VFD/soft-starter TBD) are not dependency rows; they are source conflicts requiring human ruling tracked in `Guidance.md`.
- **Specification targets (ELC-QAS-*):** TargetType=UNKNOWN used because specification documents are not accessible in the project tree; TargetLocation set to "location TBD" per skill rules.
- **Facility studies target:** TargetType=DOCUMENT; TargetRefID=studies-set (synthetic label, not a stable project ID). TargetLocation set to "location TBD" — study documents not located in accessible tree.

## Run History

| Date | Mode | Strictness | Decomposition | ACTIVE | Warnings |
|---|---|---|---|---|---|
| 2026-05-24 | — | — | — | — | Initialized in DECLARED mode (PREPARATION) |
| 2026-05-25 | UPDATE | CONSERVATIVE | GATE-07_Final_Published_2026-05-24 (confirmed) | 15 | None |
