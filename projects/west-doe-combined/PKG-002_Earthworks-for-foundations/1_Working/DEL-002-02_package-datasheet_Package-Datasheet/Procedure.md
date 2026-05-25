# Procedure: Package Datasheet

## Purpose

Define the working procedure for producing and checking the `PKG-002 - Earthworks for foundations` Package Datasheet from the accepted Gate 7 decomposition basis and locally accessible source material.

## Prerequisites

- Accepted Gate 7 decomposition snapshot is available at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` is readable for workbook row 3.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` is readable for SEC-11 civil/foundation/drainage basis.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Required missing inputs before design closure: final geotechnical report and package-specific design data are `TBD` unless supplied later by accepted source material.

## Steps

1. Confirm the current deliverable identity from `_CONTEXT.md`: `DEL-002-02_package-datasheet`, `PKG-002`, `Earthworks for foundations`, WBS 02, Civil, EPC Package Datasheet.
2. Confirm `_STATUS.md` permits drafting before overwriting the four documents. For this run, `OPEN`, `INITIALIZED`, and `SEMANTIC_READY` are permitted states.
3. Read the Gate 7 deliverable, package, scope, artifact, interface, and objective rows for `DEL-002-02_package-datasheet`, `PKG-002`, `SOW-0002`, `OBJ-002`, and `OBJ-008`.
4. Read workbook `Packages` sheet row 3 and record only source-supported package fields and `X` interface flags.
5. Read DBM SEC-11 civil/foundation/drainage source slices and extract only statements that apply to the civil/site/foundation basis.
6. Populate datasheet identification and attributes from `_CONTEXT.md`, workbook row 3, and Gate 7 registers.
7. Populate the interface requirements matrix with the two source-supported interface categories: `Grading / Site Drainage / Spill Containment` and `Structural / Foundations / Supports`.
8. Populate civil design conditions with DBM SEC-11 basis statements, keeping package-specific numeric values as `TBD`.
9. Check that the specification requirements reference the same package fields, interface categories, and DBM basis as the datasheet.
10. Check that guidance explains how to handle missing data without creating unsupported values.
11. Add conflict-table rows if future source slices disagree; otherwise keep source gaps as `TBD`.
12. Record outputs and unresolved `TBD` items in the TASK run record.

## Verification

- Datasheet, Specification, Guidance, and Procedure all exist.
- Default sections required by the four-documents skill are present.
- Package identification is consistent across all four documents.
- The only applicable interface categories are the two workbook row 3 `X` facts unless a later accepted source adds more.
- Package-specific quantities, physical limits, geotechnical values, elevations, material classes, and construction sequencing remain `TBD` where unsupported.
- The status update is only made from `OPEN` to `INITIALIZED` and only after Pass 1+2 drafting is complete.

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` history entry for safe state transition, if applied
- `_run_records/TASK_RUN_*.md`
