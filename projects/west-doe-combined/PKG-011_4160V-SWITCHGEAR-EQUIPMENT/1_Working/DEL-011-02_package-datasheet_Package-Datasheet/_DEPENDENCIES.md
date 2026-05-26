# Dependencies: DEL-011-02_package-datasheet — Package Datasheet

**Coordination Mode:** EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is canonical; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Total rows: 11 | ACTIVE: 11 | RETIRED: 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-011-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0012 | Scope decision SOW-0012 — 4160V SWITCHGEAR EQUIPMENT | HIGH | ACTIVE |
| DEP-011-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 | HIGH | ACTIVE |
| DEP-011-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 | HIGH | ACTIVE |
| DEP-011-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 | HIGH | ACTIVE |
| DEP-011-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 | HIGH | ACTIVE |
| DEP-011-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 | HIGH | ACTIVE |
| DEP-011-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | HIGH | ACTIVE |
| DEP-011-02-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | HIGH | ACTIVE |
| DEP-011-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-011-01_scope-of-work | Scope of Work | HIGH | ACTIVE |
| DEP-011-02-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-011-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-011-02-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | — | Electrical studies (load analysis, short-circuit, arc-flash, load-flow) | HIGH | ACTIVE |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents found: `Datasheet.md` (ANCHOR_DOC, contains "datasheet"), `Specification.md`, `Guidance.md`, `Procedure.md` (EXECUTION_DOC_ORDER).
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used to validate anchor identifiers (SOW-0012, OBJ-002 through OBJ-010) and resolve canonical labels via SCOPE_LEDGER.csv, DELIVERABLE_REGISTER.csv, and OBJECTIVE_DELIVERABLE_MAP.csv.
- **RUN_ROOT:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined`
- Anchor identifiers confirmed in SCOPE_LEDGER.csv (SOW-0012) and DELIVERABLE_REGISTER.csv / OBJECTIVE_DELIVERABLE_MAP.csv (OBJ-002, OBJ-004–OBJ-006, OBJ-008–OBJ-010).
- Pass 1 (ANCHOR): parent anchor SOW-0012 emitted (IMPLEMENTS_NODE); seven objective trace anchors emitted (TRACES_TO_REQUIREMENT).
- Pass 2 (EXECUTION): three execution edges emitted — upstream PREREQUISITE from DEL-011-01 (Scope of Work provides package responsibility and identity basis required by the datasheet), downstream HANDOVER to DEL-011-04 (datasheet is the explicit technical handoff for vendor engineering), and upstream CONSTRAINT for electrical studies (required before final ratings per Specification REQ-011-02-012).
- No _REFERENCES.md document pointers were used to infer additional EXECUTION edges; only edges explicitly stated in source documents were emitted.
- Parent anchor count (ACTIVE, IMPLEMENTS_NODE): 1 — Tree integrity satisfied.
- No warnings generated.

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE | 11 |
| RETIRED | 0 |
| ANCHOR rows (ACTIVE) | 8 |
| EXECUTION rows (ACTIVE) | 3 |
| SatisfactionStatus = TBD | 10 |
| SatisfactionStatus = PENDING | 1 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — UPDATE run via dependency-extract skill; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE; decomposition path confirmed; 11 rows extracted (8 ANCHOR, 3 EXECUTION); 0 RETIRED; parent anchor check: 1 IMPLEMENTS_NODE (OK).
