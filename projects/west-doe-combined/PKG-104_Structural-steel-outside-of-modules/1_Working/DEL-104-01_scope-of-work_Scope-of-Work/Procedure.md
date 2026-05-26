# Procedure: DEL-104-01_scope-of-work — Scope of Work

> Operational procedure to PRODUCE the `PKG-104` Scope of Work deliverable
> (per the four-documents skill interpretation rule: producing the deliverable
> artifact, not operating an installed system).

## Purpose

Provide a repeatable, source-grounded procedure for the EPC Integrator (or
delegated author) to draft, review, and issue the `PKG-104` Scope of Work
deliverable so that it satisfies the specification requirements and remains
defensible against the upstream decomposition record.

## Prerequisites

### Declared upstream dependencies

- None declared during PREPARATION (`_DEPENDENCIES.md`). Authors should still
  consult the accepted Gate 7 decomposition snapshot as the upstream truth.

### Required reference materials

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local).
- Gate 7 snapshot registers under
  `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`:
  `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `SCOPE_LEDGER.csv`,
  `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`,
  `OBJECTIVE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-11 in particular; SEC-04
  for ambient).
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-04
  ambient context; SEC-11 layout context).
- `_Sources/26020-Package_Requirements.docx` (`location TBD` until parsed).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 105
  (`location TBD` until parsed).

### Required prior states

- `_STATUS.md` Current State must be `OPEN` or `INITIALIZED` (overwrite-safe).

## Steps

1. **Anchor identification.** Populate the identification block from
   `_CONTEXT.md` Identity and `PACKAGE_REGISTER.csv` row `PKG-104` (Workbook
   ID 104, CoA tracking `26020-01-36-004`, discipline Structural, WBS 01,
   workbook source row 105). Cite both sources.
2. **State scope item coverage.** Cite `SOW-0260` (IN) from `SCOPE_LEDGER.csv`
   as the scope item this deliverable covers.
3. **Set package boundary.** Write the In-Scope / Out-of-Scope sections per
   `Specification.md`. Mark "module-internal structural steel out of scope"
   as **ASSUMPTION** and note `PKG-103` Gate 6 disposition for pipe racks.
4. **Record physical interfaces.** Enumerate the two interfaces recorded for
   `PKG-104` in `INTERFACE_REGISTER.csv` (`IFC-CCDE4B56CA` Grading / Site
   Drainage / Spill Containment; `IFC-ECDD4D3A15` Structural / Foundations
   / Supports). Use them verbatim.
5. **Apply project structural basis.** Quote or cite the DBM-Deepcut SEC-11
   structural basis row-for-row (code, steel design, materials, concrete,
   foundation engineering). Do not substitute or paraphrase numeric values.
6. **State foundation default.** Note driven steel piles as the project
   default; carry geotechnical parameters as `TBD` (DBM-Deepcut SEC-11
   "Piles and Foundations"; "Geotechnical and Topographical Assumptions").
7. **Build tagged-equipment list.** Attempt to extract `PKG-104` tagged
   equipment from `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 105.
   If the row is not parsed in this run, mark the tagged-equipment artifact
   `TBD` and add a `Conflict Table` entry (see `Guidance.md` `CONF-104-01-01`).
8. **Author integration narrative.** Describe how `PKG-104` fits into the
   facility and how it supports `OBJ-001` and `OBJ-008` per the
   package-heuristic mapping. Cite `OBJECTIVE_REGISTER.csv` rows and
   DBM-Deepcut SEC-11 anchor.
9. **Record responsibility.** Mirror the `PACKAGE_REGISTER.csv` Responsibility
   note verbatim; flag the `_CONTEXT.md` divergence as `CONF-104-01-02` in
   the Conflict Table.
10. **List package-specific exclusions.** Carry as `TBD` if no source-stated
    exclusion exists (`PACKAGE_REGISTER.csv` exclusion field).
11. **Apply epistemic labels.** Ensure every non-trivial value carries either
    a source citation or a `TBD`/`ASSUMPTION` label (K-PROV-1).
12. **Cross-document consistency sweep.** Confirm identifiers, interface
    names, standards/materials, and objective IDs are consistent across
    `Datasheet.md`, `Specification.md`, `Guidance.md`, and this `Procedure.md`.
13. **Status update.** When the four documents exist and consistency is
    confirmed, advance `_STATUS.md` `OPEN -> INITIALIZED` via
    `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED
    TASK+four-documents`. Do not regress state.
14. **Run record.** Write `_run_records/TASK_RUN_<DATE>_<HHMM>.md`
    documenting RUN_PASSES, inputs read, files written, RUN_STATUS, and any
    Conflict Table entries opened.

## Verification

- **V1** — Identification block matches `PACKAGE_REGISTER.csv` row `PKG-104`
  field-for-field.
- **V2** — In-Scope/Out-of-Scope sections cite source rows or carry
  `ASSUMPTION`/`TBD` labels.
- **V3** — Interface list equals the two `PKG-104` rows in
  `INTERFACE_REGISTER.csv`.
- **V4** — Standards/materials block matches DBM-Deepcut SEC-11 lines
  2672-2677 (no paraphrase drift).
- **V5** — Responsibility wording matches `PACKAGE_REGISTER.csv` or carries
  a `Conflict Table` entry.
- **V6** — Anticipated artifacts list matches `ARTIFACT_REGISTER.csv` rows
  for `DEL-104-01_scope-of-work` exactly.
- **V7** — All four documents present; default schema sections present in
  each.
- **V8** — `_STATUS.md` updated only when safe; no state regression.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this
  deliverable's four documents).
- `_STATUS.md` (updated safely per Step 13).
- `_run_records/TASK_RUN_<DATE>_<HHMM>.md` (this run).
- Conflict Table entries in `Guidance.md` (e.g., `CONF-104-01-01..04`).
