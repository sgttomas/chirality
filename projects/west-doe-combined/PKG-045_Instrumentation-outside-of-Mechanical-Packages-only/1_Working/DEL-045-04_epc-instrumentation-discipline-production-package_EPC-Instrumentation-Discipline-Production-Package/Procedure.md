# Procedure: DEL-045-04 — EPC / Instrumentation Discipline Production Package

## Purpose

Describes how to produce and maintain the EPC/Instrumentation Discipline Production Package deliverable (the production package basis, the discipline deliverable register, and the source-limited requirements closure record) under present source-limited conditions, and how to use it as inputs become available.

## Prerequisites

- Deliverable-local minimum viable fileset present: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md` (verified at this run).
- Accepted upstream decomposition snapshot: `GATE-07_Final_Published_2026-05-24` (see `_REFERENCES.md`).
- Companion PKG-045 deliverables identified: `DEL-045-01`, `DEL-045-02`, `DEL-045-03`.
- Declared upstream dependencies: none declared at PREPARATION (`_DEPENDENCIES.md`). Treat as advisory; do not invent upstream constraints.
- Required references for source-grounded enrichment (currently `location TBD`): Workbook Packages row 47 section text; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md.

## Steps

1. **Initialize the production package basis document.**
   - Cite PKG-045 identity from `PACKAGE_REGISTER.csv`.
   - State the boundary: Instrumentation scope outside any Mechanical Package.
   - List applicable physical interface types from `PACKAGE_REGISTER.csv`.
   - Carry exclusions (field supports, power, comms unless confirmed).
2. **Enumerate the discipline deliverable register (TBD content).**
   - Create the register skeleton; mark line items `TBD` until source slices are localized.
   - At minimum, reserve slots for: instrument index, loop schedules, I/O list, control narratives, hazardous-area classification, calibration plan, FAT/SAT plan. Each line item: `TBD — source slice required`.
3. **Open the source-limited requirements closure record.**
   - List every requirement marked `TBD` or `ASSUMPTION` in `Specification.md` (R-8, R-9 today).
   - Tag each entry with the source it depends on and route to Gate 5.
4. **Localize source slices when access is granted.**
   - Copy the relevant section(s) of Workbook Packages row 47 into the deliverable folder (or into `_Sources` and update `_REFERENCES.md`).
   - Copy the relevant section(s) of `3-25_Comp_and_Liquids_DBM.md` similarly.
   - Re-run the four-documents skill (`RUN_PASSES: FULL`) to replace `TBD` items grounded in the localized slices.
5. **Coordinate with PKG-045 companion deliverables.**
   - Cross-reference DEL-045-01 (Scope of Work), DEL-045-02 (Package Datasheet), DEL-045-03 (Construction Work Package) for consistency in scope boundary, exclusions, and interface types.
6. **Confirm objective association.**
   - Surface the PACKAGE_HEURISTIC mapping (`OBJ-002`, `OBJ-003`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-010`) for human ruling; do not treat as hard requirement until confirmed.
7. **Update lifecycle state.**
   - On successful Pass 1/2 generation from `OPEN` state, advance `_STATUS.md` to `INITIALIZED` via `tools/scaffolding/write_status.sh`.
   - Subsequent state transitions (e.g., to `SEMANTIC_READY`) belong to downstream skills, not to this procedure.

## Verification

| Check | Method | Pass Criterion |
|---|---|---|
| Production package basis present | Inspection | Document exists and carries identity, boundary, interface types, exclusions |
| Discipline deliverable register skeleton present | Inspection | Register file exists; each line item annotated with status or `TBD` |
| Closure record present | Inspection | Each `TBD`/`ASSUMPTION` from `Specification.md` recorded with source dependency |
| Scope boundary stated explicitly | Review | "Outside of Mechanical Packages only" language present |
| Interface types match source | Cross-check | Production basis list equals `PACKAGE_REGISTER.csv` PKG-045 list |
| Exclusions match source | Cross-check | Field supports/power/comms exclusion present and matches PKG-045 Notes |
| Companion-deliverable coordination evidenced | Review | Cross-references to DEL-045-01/02/03 present |
| `_STATUS.md` advanced safely | Inspection | State moved `OPEN → INITIALIZED` only when Pass 1/2 ran and prior state was `OPEN` |
| Conflict Table populated where applicable | Review | `Guidance.md` Conflict Table either empty (with note) or carries entries with provenance |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this set).
- Discipline production package basis (anticipated artifact).
- Discipline deliverable register (anticipated artifact; TBD content).
- Source-limited requirements closure record (anticipated artifact).
- Updated `_STATUS.md` history line.
- Run record at `_run_records/TASK_RUN_<timestamp>.md` capturing inputs, resolved state, and outputs.
- Open-issues entries routed to Gate 5 as appropriate.
