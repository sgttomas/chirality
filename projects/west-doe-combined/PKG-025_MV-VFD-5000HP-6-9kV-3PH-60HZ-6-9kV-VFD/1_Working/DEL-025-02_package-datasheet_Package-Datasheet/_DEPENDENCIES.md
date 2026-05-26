# Dependencies: DEL-025-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema); this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Total ACTIVE rows: 17 | RETIRED rows: 0

### ANCHOR rows (Pass 1 — Tree)

| DependencyID | AnchorType | TargetType | TargetRefID | TargetName | Confidence |
|---|---|---|---|---|---|
| DEP-025-02-001 | IMPLEMENTS_NODE | WBS_NODE | SOW-0026 | Scope Item SOW-0026 — MV VFD 5000HP 6.9kV | HIGH |
| DEP-025-02-002 | TRACES_TO_REQUIREMENT | REQUIREMENT | OBJ-001 | Provide 04-25 Deepcut facility scope | HIGH |
| DEP-025-02-003 | TRACES_TO_REQUIREMENT | REQUIREMENT | OBJ-004 | Execute vendor-owned packages with split responsibilities | HIGH |
| DEP-025-02-004 | TRACES_TO_REQUIREMENT | REQUIREMENT | OBJ-005 | Provide and integrate facility electrical power basis | HIGH |
| DEP-025-02-005 | TRACES_TO_REQUIREMENT | REQUIREMENT | OBJ-006 | Provide and integrate controls instrumentation and communications | HIGH |
| DEP-025-02-006 | TRACES_TO_REQUIREMENT | REQUIREMENT | OBJ-008 | Provide civil structural site and construction-support scope | HIGH |
| DEP-025-02-007 | TRACES_TO_REQUIREMENT | REQUIREMENT | OBJ-009 | Carry safety regulatory and sour-service requirements | HIGH |
| DEP-025-02-008 | TRACES_TO_REQUIREMENT | REQUIREMENT | OBJ-010 | Maintain operability maintainability and vendor-documentation closure evidence | HIGH |

### EXECUTION rows (Pass 2 — DAG)

| DependencyID | Direction | DependencyType | TargetType | TargetDeliverableID / TargetRefID | TargetName | Confidence |
|---|---|---|---|---|---|---|
| DEP-025-02-009 | UPSTREAM | PREREQUISITE | DOCUMENT | DEC-001 | Gate 7 PROJECT_DECOMP Snapshot | HIGH |
| DEP-025-02-010 | UPSTREAM | PREREQUISITE | DOCUMENT | PKG_REG | PACKAGE_REGISTER.csv — Gate 7 snapshot | HIGH |
| DEP-025-02-011 | UPSTREAM | PREREQUISITE | DOCUMENT | DEL_REG | DELIVERABLE_REGISTER.csv — Gate 7 snapshot | HIGH |
| DEP-025-02-012 | UPSTREAM | PREREQUISITE | DOCUMENT | IFC_REG | INTERFACE_REGISTER.csv — Gate 7 snapshot | HIGH |
| DEP-025-02-013 | UPSTREAM | PREREQUISITE | DOCUMENT | DBM_DOC | DBM-Deepcut 4-25_Deepcut_DBM.md | HIGH |
| DEP-025-02-014 | UPSTREAM | INTERFACE | DOCUMENT | WB_SRC | Workbook Packages sheet row 27 | HIGH |
| DEP-025-02-015 | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-025-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH |
| DEP-025-02-016 | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-025-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH |
| DEP-025-02-017 | UPSTREAM | INTERFACE | DELIVERABLE | DEL-025-01_scope-of-work | Scope of Work | MEDIUM |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (from BRIEF; confirmed via SCOPE_LEDGER.csv, DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, INTERFACE_REGISTER.csv)
- **Source documents scanned (AUTO):** `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`
- **ANCHOR_DOC:** `Datasheet.md` (matches `datasheet` heuristic; confirmed as primary identity and attribute source)
- **EXECUTION_DOC_ORDER:** `Procedure.md`, `Guidance.md`, `Specification.md`, `Datasheet.md`
- **Prior Dependencies.csv:** Not present; created fresh this run.
- **DEP-025-02-017 note:** IMPLICIT / MEDIUM confidence. Procedure does not list DEL-025-01 as an explicit prerequisite input, but both deliverables share the same source basis and interface list; consistency with Scope of Work is implied by the shared Gate 7 anchor. Marked ASSUMPTION.
- No `_REFERENCES.md` document pointer resolution was needed for EXECUTION rows — all DOCUMENT targets are identified by explicit filenames cited in source docs.
- **[INFO]** Parent anchor check: 1 IMPLEMENTS_NODE row (DEP-025-02-001). Tree integrity satisfied.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 17 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 15 |
| TBD | 2 |

Notes on TBD satisfaction:
- DEP-025-02-015 (HANDOVER to DEL-025-04): downstream deliverable not yet produced; satisfaction TBD.
- DEP-025-02-016 (HANDOVER to DEL-025-06): downstream acceptance activity not yet complete; satisfaction TBD.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run (UPDATE, CONSERVATIVE); Dependencies.csv created; 17 ACTIVE rows extracted; schema validated VALID.
