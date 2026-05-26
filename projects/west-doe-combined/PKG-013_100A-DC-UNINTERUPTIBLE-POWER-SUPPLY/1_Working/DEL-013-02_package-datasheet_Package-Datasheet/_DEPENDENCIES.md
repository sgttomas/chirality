# Dependencies: DEL-013-02_package-datasheet — Package Datasheet

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

### Summary

| Class | Count (ACTIVE) |
|---|---|
| ANCHOR | 7 |
| EXECUTION | 3 |
| **Total ACTIVE** | **10** |

### Compact Table

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-013-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0014 | Scope decision SOW-0014 — 100A DC UNINTERUPTIBLE POWER SUPPLY | HIGH | ACTIVE |
| DEP-013-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 | HIGH | ACTIVE |
| DEP-013-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 | HIGH | ACTIVE |
| DEP-013-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 | HIGH | ACTIVE |
| DEP-013-02-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 | HIGH | ACTIVE |
| DEP-013-02-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | HIGH | ACTIVE |
| DEP-013-02-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | HIGH | ACTIVE |
| DEP-013-02-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-013-01_scope-of-work | Scope of Work — PKG-013 | HIGH | ACTIVE |
| DEP-013-02-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | — | DBM-Deepcut 4-25 electrical basis | HIGH | ACTIVE |
| DEP-013-02-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-013-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package — PKG-013 | HIGH | ACTIVE |

## Run Notes

### Defaults and choices

- `MODE`: UPDATE (no prior Dependencies.csv existed; file created fresh)
- `STRICTNESS`: CONSERVATIVE — anchor rows emitted only when identifiers appear explicitly in source; execution edges emitted only when explicit information/artifact transfer is stated
- `CONSUMER_CONTEXT`: NONE
- `SOURCE_DOCS`: AUTO — scanned deliverable folder; candidate docs: `Datasheet.md` (ANCHOR_DOC by name heuristic), `Guidance.md`, `Procedure.md`, `Specification.md`, `_CONTEXT.md`, `_REFERENCES.md`
- `DECOMPOSITION_PATH`: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — provided via brief; confirmed present; used for anchor validation and label resolution

### Anchor resolution

- SOW-0014 confirmed in `SCOPE_LEDGER.csv` row SOW-0014; PKG-013 listed as package; DEL-013-02_package-datasheet listed in associated deliverables column.
- OBJ-002, OBJ-004, OBJ-005, OBJ-008, OBJ-009, OBJ-010 confirmed in `DELIVERABLE_REGISTER.csv` OBJ column for DEL-013-02_package-datasheet and in `OBJECTIVE_REGISTER.csv`.

### Execution edges

- DEP-013-02-008: DEL-013-01 (Scope of Work) is an explicit upstream prerequisite. `Datasheet.md` cites `DELIVERABLE_REGISTER.csv` and `PACKAGE_REGISTER.csv` as sources; `_CONTEXT.md` states the Datasheet converts the accepted Gate 7 package basis to vendor handoff basis, meaning the SOW co-deliverable is the primary scope-definition input. Rated EXPLICIT / HIGH.
- DEP-013-02-009: DBM-Deepcut 4-25 is an explicit upstream document prerequisite. `Datasheet.md` cites `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` as the source for UPS services, standby power, electrical buildings, grounding, cable tray, and conduit basis across multiple Attributes and Conditions rows. TargetLocation is TBD at deliverable level (shared source root).
- DEP-013-02-010: DEL-013-04 (Vendor Engineered Equipment Package) is an explicit downstream handover target. `_CONTEXT.md` states anticipated artifacts include "vendor engineering handoff basis" and "package interface requirements matrix"; `DELIVERABLE_REGISTER.csv` confirms DEL-013-04 is the Package Vendor production unit developed from EPC Package Datasheet. Rated EXPLICIT / HIGH.

### Scope items not extracted

- Interface register rows (IFC-3B1ED82A25, IFC-8093ECDA51, IFC-DA9E0BAB70, IFC-CAE19AED68) are interface facts applicable to PKG-013 but are not execution dependencies between deliverables; they are evidence within the Datasheet scope rather than information-flow edges. Not extracted under CONSERVATIVE.
- DBM-Comp_and_Liquids is cited in `Datasheet.md` References but no specific content from that source is used in Datasheet Attributes or Conditions sections; not emitted under CONSERVATIVE.
- `26020-Package_Requirements.docx` is cited as searched with no PKG-013 match; no dependency edge generated.

### Tree x DAG integrity

- Parent anchor check: 1 ACTIVE ANCHOR IMPLEMENTS_NODE row (DEP-013-02-001). PASS.

## Lifecycle Summary

| Lifecycle dimension | Count |
|---|---|
| ACTIVE rows | 10 |
| RETIRED rows | 0 |
| ANCHOR ACTIVE | 7 |
| EXECUTION ACTIVE | 3 |
| SatisfactionStatus=TBD | 8 |
| SatisfactionStatus=PENDING | 2 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — UPDATE run; STRICTNESS=CONSERVATIVE; decomposition path confirmed (GATE-07_Final_Published_2026-05-24); 10 rows extracted (7 ANCHOR + 3 EXECUTION); 0 RETIRED; schema validation VALID. No warnings.
