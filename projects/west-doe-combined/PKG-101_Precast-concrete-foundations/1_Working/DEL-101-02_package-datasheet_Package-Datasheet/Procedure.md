# Procedure — DEL-101-02 Package Datasheet (PKG-101 Precast concrete foundations)

> Operational steps to produce, verify, and hand off the PKG-101 Package Datasheet artifact set. Steps where engineering judgment would be required are marked `TBD`.

## Purpose

Produce the EPC Integrator technical-handoff Package Datasheet for PKG-101 (precast concrete foundations) so third-party vendor or discipline package engineering can proceed from a source-grounded technical basis, applicable standards, geotechnical TBDs, and registered interface facts.

## Prerequisites

- Declared upstream dependencies: **None declared** during PREPARATION (`_DEPENDENCIES.md` § Declared Upstream Dependencies).
- Reference materials accessible:
  - GATE-07 snapshot registers (DELIVERABLE, PACKAGE, INTERFACE, ARTIFACT, OBJECTIVE_DELIVERABLE_MAP, PROJECT_DECOMP.md).
  - DBM `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § Civil Scope through § Assumptions/TBDs.
- Reference materials referenced but not directly read in this run (treat as `location TBD`):
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 102 (cell-level).
  - `_Sources/26020-Package_Requirements.docx` PKG-101 section (no matched DocxPackageHeading per PACKAGE_REGISTER.csv).
- `_CONTEXT.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md` present and read.
- `_STATUS.md` Current State permits overwrite per `ALLOW_OVERWRITE_STATES` (this run: OPEN).

## Steps

| # | Step | Notes |
|---|---|---|
| 1 | Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for identity, scope, and declared dependencies. | DECLARED dependency mode; no declared upstream/downstream. |
| 2 | Read the GATE-07 PACKAGE_REGISTER row for `PKG-101` and capture: CoA tracking number, WBS, discipline, responsibility model, inclusion criteria, exclusions, interface types, source refs, supports-objectives, package role flag. | PACKAGE_REGISTER.csv row PKG-101. |
| 3 | Read the GATE-07 DELIVERABLE_REGISTER row for `DEL-101-02_package-datasheet` and capture: anticipated artifacts, covers-scope-items (SOW-0257), supports-objectives (OBJ-001; OBJ-008). | DELIVERABLE_REGISTER.csv. |
| 4 | Read the GATE-07 INTERFACE_REGISTER rows where PackageID=`PKG-101` and capture: IFC-26343B703C (Grading / Site Drainage / Spill Containment), IFC-BED3DE4194 (Structural / Foundations / Supports). | INTERFACE_REGISTER.csv. |
| 5 | Read the GATE-07 ARTIFACT_REGISTER rows where ParentDeliverableID=`DEL-101-02_package-datasheet` and capture five artifact IDs (technical datasheet, vendor handoff basis, interface requirements matrix, two interface-fact records). | ARTIFACT_REGISTER.csv. |
| 6 | Open `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § "Civil Scope," "Governing Civil and Structural Basis," "Geotechnical and Topographical Assumptions," "Site Grading and Surface Water Management," "Piles and Foundations," "External Dependencies," and "Assumptions, TBDs, and Design Development Requirements." Extract precast-relevant lines (notably lines 2745-2749 and standards lines 2672-2677). | Source slice per skill glossary. |
| 7 | Where workbook cell-level data or `26020-Package_Requirements.docx` PKG-101 section is needed but not opened, mark the slice `location TBD` rather than inferring values. | PACKAGE_REGISTER.csv DocxPackageMatched=FALSE. |
| 8 | Draft `Datasheet.md`: Identification, Attributes, Conditions, Construction, Interfaces, Anticipated Artifacts, Open/TBD Items, References. Cite source path + section for every non-trivial value. | Datasheet section defaults preserved. |
| 9 | Draft `Specification.md`: Scope, Requirements (REQ-101-02-NN), Standards, Verification, Documentation. Label any inferred requirement ASSUMPTION. | Specification section defaults preserved. |
| 10 | Draft `Guidance.md`: Purpose, Principles, Considerations, Trade-offs, Examples, Conflict Table. Surface unresolved interpretation issues to the Conflict Table; do not silently resolve. | Conflict Table required for HRR per skill brief. |
| 11 | Run cross-document consistency sweep (Step 5 of skill): Datasheet ↔ Specification entities/attributes, Specification ↔ Guidance rationale, Specification ↔ Procedure verification hooks, terminology, numeric values. | Reconcile where resolvable from drafts; otherwise add to Conflict Table. |
| 12 | Update `_STATUS.md` via `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED "TASK+four-documents"` only if Current State is OPEN. | Safe update only; no state regression. |
| 13 | Write `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHMM>.md` summarizing pass selection, inputs read, outputs produced, RUN_STATUS, and disposition of any TBDs. | Run record required per scaffolding convention. |
| 14 | (Out of this run, Phase 2.5) When `_SEMANTIC_LENSING.md` exists, re-run `TASK + four-documents` with `RUN_PASSES: P3_ONLY` for Pass 3 enrichment. | Not executed in this `P1_P2` run. |

## Verification

| Check | Method |
|---|---|
| Identification fields | Compare Datasheet "Identification" against `_CONTEXT.md` and PACKAGE_REGISTER.csv row PKG-101. |
| Interface coverage | Confirm both registered interfaces (IFC-26343B703C, IFC-BED3DE4194) appear in Datasheet Interfaces and Specification REQ-101-02-03. |
| Precast-on-piles handling | Confirm Datasheet Attributes/Construction and Specification REQ-101-02-06/-07 reflect DBM lines 2745-2749 without inventing dimensions or capacities. |
| Standards | Confirm Specification Standards table lists NBC, CAN/CSA A23.3, CSA A23.1/A23.2, Canadian Foundation Engineering Manual, CAN/CSA-S16, CSA G40.20/G40.21 per DBM § Governing Civil and Structural Basis. |
| TBD discipline | Confirm bearing capacity, LPILE curves, dynamic criteria, compressor dynamic analysis, and direct skid-to-pile welding alternative are recorded as TBD (not invented). |
| No invented values | Spot-check Datasheet/Specification for any numeric or categorical claim lacking a source citation. |
| Status update safety | `_STATUS.md` updated only if prior state was OPEN; otherwise skipped. |
| Run record present | `_run_records/TASK_RUN_*.md` written with RUN_STATUS. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- `_STATUS.md` updated to `INITIALIZED` (only if prior state OPEN).
- `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHMM>.md` summarizing this invocation.
- Conflict Table in `Guidance.md` for any open interpretation conflicts (CONF-101-02-NN).
