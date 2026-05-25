# Procedure: DEL-036-01_scope-of-work

## Purpose

Produce the four Scope-of-Work artifacts for `PKG-036` "6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)" — package scope of work, tagged equipment and package identity list, package function and whole-facility integration narrative, and package responsibility assignment record — grounded in the Gate 7 decomposition snapshot and accessible source slices.

## Prerequisites

- Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` (already present).
- Access to the Gate 7 final-published PROJECT_DECOMP snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (registers used by this Scope of Work).
- Access to `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (electrical design basis source slices used by this Scope of Work).
- Awareness that no deliverable-specific source slices were copied during PREPARATION and that `26020-Package_Requirements.docx` has not been parsed for PKG-036 in this run.
- Declared upstream dependencies: none. Declared downstream dependencies: none.

## Steps

| Step | Action | Inputs | Output |
|---|---|---|---|
| 1 | Resolve package identity from registers. | Workbook Packages row 38; `PACKAGE_REGISTER.csv` row `PKG-036`; `DELIVERABLE_REGISTER.csv` row `DEL-036-01_scope-of-work`. | Identification block populated in `Datasheet.md` and the identity statement in the Scope of Work. |
| 2 | Resolve scope-item linkage. | `SCOPE_LEDGER.csv` row `SOW-0037`. | Scope-item reference and IN-scope rationale recorded. |
| 3 | Resolve supported objectives. | `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-036-01_scope-of-work`; `OBJECTIVE_PACKAGE_MAP.csv` rows for `PKG-036`. | Objectives `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` recorded. |
| 4 | Enumerate the interface set. | `INTERFACE_REGISTER.csv` rows for `PKG-036` (12 IFC IDs). | Interface IFC IDs listed in the Datasheet Conditions table and referenced in `Specification.md` R-036-01-05. |
| 5 | Resolve anticipated artifacts. | `ARTIFACT_REGISTER.csv` rows for `DEL-036-01_scope-of-work` (`ART-74190901D1`, `ART-380568AF55`, `ART-9B0CE2B67A`, `ART-4323ADFFB1`). | Documentation section of `Specification.md` populated. |
| 6 | Draft package function and integration narrative from DBM source slices. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` voltage and service table; plant power distribution paragraph; 6.9 kV motor control paragraph; electrical-buildings list; grounding/cable-tray/HVAC paragraphs. | Datasheet Attributes; Guidance Considerations; Specification R-036-01-03. |
| 7 | Resolve the building-tag conflict. | Workbook Packages row 38 vs DBM electrical-buildings list (rows for 820-1 and 830-1). | Conflict Table entry `CT-036-01-001` in `Guidance.md`; cross-references in `Datasheet.md` and `Specification.md`. |
| 8 | Mark package-specific equipment, location, and quantity items as `TBD` where no accessible source slice supports them. | Source gap. | `TBD` cells in `Datasheet.md` Attributes / Construction; Conflict Table entry `CT-036-01-002`. |
| 9 | Run cross-document consistency sweep (Pass 2). | Drafted four documents. | Terminology and IDs consistent across Datasheet, Specification, Guidance, Procedure; conflicts captured in Conflict Table. |
| 10 | Update `_STATUS.md` from `OPEN` to `INITIALIZED` under the safe Pass 1/2 status rule. | `_STATUS.md`. | `_STATUS.md` advanced to `INITIALIZED`. |

## Verification

| Check | Method |
|---|---|
| Identity fields match registers | Cross-check against `PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv`. |
| Scope-item linkage matches ledger | Cross-check `SCOPE_LEDGER.csv` row `SOW-0037`. |
| Interface IFC IDs match register | Cross-check 12 IDs against `INTERFACE_REGISTER.csv` rows for `PKG-036`. |
| Anticipated artifacts match register | Cross-check 4 IDs against `ARTIFACT_REGISTER.csv` rows for `DEL-036-01_scope-of-work`. |
| Objectives match maps | Cross-check 8 IDs against `OBJECTIVE_DELIVERABLE_MAP.csv`. |
| Source claims cite a source slice or are marked `TBD` | Inspect each non-trivial value in `Datasheet.md` and `Specification.md`. |
| Conflict between workbook identity and DBM tag-to-function mapping is surfaced | Inspect `Guidance.md` Conflict Table for `CT-036-01-001`. |
| `_STATUS.md` only advanced when current state is `OPEN` | Inspect history block in `_STATUS.md`. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` — the four-document kit produced by this deliverable.
- `_STATUS.md` — advanced from `OPEN` to `INITIALIZED` under the safe Pass 1/2 status rule.
- `_run_records/TASK_RUN_2026-05-24_<HHMM>.md` — TASK run record for this invocation.
