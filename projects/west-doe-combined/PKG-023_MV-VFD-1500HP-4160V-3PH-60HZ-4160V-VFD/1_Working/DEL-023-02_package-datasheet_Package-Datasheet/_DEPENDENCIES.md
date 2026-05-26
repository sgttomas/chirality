# Dependencies: DEL-023-02_package-datasheet — Package Datasheet

**Coordination Mode:** EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is canonical; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

16 rows extracted (all ACTIVE). Summary by class:

| DependencyClass | AnchorType / DependencyType | Direction | Count |
|---|---|---|---|
| ANCHOR | IMPLEMENTS_NODE | UPSTREAM | 1 |
| ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | 7 |
| EXECUTION | PREREQUISITE | UPSTREAM | 2 |
| EXECUTION | INTERFACE | UPSTREAM | 4 |
| EXECUTION | HANDOVER | DOWNSTREAM | 1 |

### Compact table (ACTIVE rows)

| DependencyID | Class | Type | Direction | Target |
|---|---|---|---|---|
| DEP-023-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | SOW-0024 — MV VFD 1500HP 4160V scope decision |
| DEP-023-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OBJ-001 — 04-25 Deepcut facility scope |
| DEP-023-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OBJ-004 — Vendor-owned package execution |
| DEP-023-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OBJ-005 — Electrical power basis and interfaces |
| DEP-023-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OBJ-006 — Controls instrumentation and comms |
| DEP-023-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OBJ-008 — Civil structural and foundations |
| DEP-023-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OBJ-009 — Sour-service safety and regulatory |
| DEP-023-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OBJ-010 — Operability and vendor documentation |
| DEP-023-02-009 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-023-01_scope-of-work (Scope of Work) |
| DEP-023-02-010 | EXECUTION | INTERFACE | UPSTREAM | IFC-2F6B2D3B80 — Electrical Power |
| DEP-023-02-011 | EXECUTION | INTERFACE | UPSTREAM | IFC-CEF43B776E — Grounding / Bonding |
| DEP-023-02-012 | EXECUTION | INTERFACE | UPSTREAM | IFC-488756F914 — I&C / Control Cabling |
| DEP-023-02-013 | EXECUTION | INTERFACE | UPSTREAM | IFC-FF4188D90D — Communications / Network |
| DEP-023-02-014 | EXECUTION | INTERFACE | UPSTREAM | IFC-0AED039BBE — Structural / Foundations / Supports |
| DEP-023-02-015 | EXECUTION | HANDOVER | DOWNSTREAM | DEL-023-04_vendor-engineered-equipment-package |
| DEP-023-02-016 | EXECUTION | PREREQUISITE | UPSTREAM | DBM-Deepcut 4.16 kV MCC / MV VFD requirements basis (TBD) |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; ANCHOR_DOC = `Datasheet.md` (contains `datasheet` in filename); EXECUTION_DOCS = `Datasheet.md`, `Guidance.md`, `Procedure.md`, `Specification.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used to validate anchors and resolve canonical labels
- **RUN_ROOT:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined`
- Anchor identifiers (SOW-0024, OBJ-001 through OBJ-010) confirmed against SCOPE_LEDGER.csv, DELIVERABLE_REGISTER.csv, and OBJECTIVE_REGISTER.csv in the Gate 7 snapshot.
- Interface IDs (IFC-2F6B2D3B80, IFC-CEF43B776E, IFC-488756F914, IFC-FF4188D90D, IFC-0AED039BBE) are cited explicitly in Datasheet.md Conditions section and cross-referenced to INTERFACE_REGISTER.csv.
- DEP-023-02-016 (DBM 4.16 kV MCC requirements): SatisfactionStatus=PENDING because Datasheet.md explicitly states VFD and soft-starter requirements for 4.16 kV motors are TBD pending detailed electrical design. This is a known open item.
- IFC-38BEE3F6CC (Maintenance Access) was cited in Datasheet.md but is a design/routing constraint without explicit information-flow artifact transfer; not extracted as EXECUTION edge per information-flow-only rule (CONSERVATIVE).
- No `_REFERENCES.md` document pointers were available beyond Gate 7 snapshot path; TargetLocation for DOCUMENT rows set to INTERFACE_REGISTER.csv path where applicable.
- **Tree integrity:** 1 IMPLEMENTS_NODE anchor (DEP-023-02-001) found. No FLOATING_NODE warning.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 16 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 8 |
| PENDING | 8 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE; decomposition=GATE-07_Final_Published_2026-05-24 (used); 16 ACTIVE rows extracted (8 ANCHOR, 8 EXECUTION); no prior CSV; no retired rows; schema validated VALID.
