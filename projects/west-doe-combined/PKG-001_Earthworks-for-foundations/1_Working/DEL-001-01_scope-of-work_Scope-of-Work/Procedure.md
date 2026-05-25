# Procedure: DEL-001-01 Scope of Work

## Purpose

Define the procedure for producing the PKG-001 Scope of Work using the accepted Gate 7 decomposition basis and locally accessible source materials. The procedure is for document production and verification, not field execution.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md` are available.
- Workbook Packages row 2 is accessible in `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- DBM civil source slices are accessible in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, especially SEC-11 and Construction Responsibility.
- Declared upstream dependencies: none declared during PREPARATION.
- Open external inputs to track: geotechnical assessment, topographical survey/grade surface file, plot plan, detailed engineering drainage design, and any package-specific equipment/tag source.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md` and Gate 7 `DELIVERABLE_REGISTER.csv`.
2. Confirm current `_STATUS.md` permits drafting. For this run, current state was `OPEN`.
3. Read Gate 7 package basis for PKG-001 from `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, and `OBJECTIVE_PACKAGE_MAP.csv`.
4. Read workbook Packages row 2 and confirm the package identity, WBS, CoA tracking number, discipline, and marked interface columns.
5. Read relevant DBM civil source slices for civil scope, governing standards, geotechnical/topographical assumptions, site grading and surface water management, piles and foundations, external dependencies, and construction responsibility.
6. Draft the Scope of Work content so it includes:
   - package identity and source basis;
   - source-supported interfaces;
   - package function and integration narrative;
   - responsibility assignment record;
   - open inputs and `TBD` items.
7. Mark unsupported values as `TBD`; label inferences as `ASSUMPTION` if any are used.
8. Cross-check the four documents for consistent package ID, package name, WBS, CoA tracking number, interface types, responsibility language, and `TBD` treatment.
9. If source conflicts are found, add them to the Guidance conflict table with source locations and human-ruling fields.
10. Update `_STATUS.md` from `OPEN` to `INITIALIZED` only after the four documents exist and the state transition is safe.

## Verification

- Datasheet, Specification, Guidance, and Procedure all exist.
- Each document contains the default schema sections required by the four-documents skill.
- Package identity is consistent across all documents: PKG-001, DEL-001-01_scope-of-work, Earthworks for foundations, WBS 01, CoA tracking number 26020-01-42-001.
- Interface types are consistent across all documents: Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports.
- No unsupported tagged equipment, quantities, coordinates, final geotechnical values, or final survey values are introduced.
- Requirements in Specification have corresponding verification hooks in Procedure.
- Guidance contains a Conflict Table, even though no conflict was identified in this pass.

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md`
- `_run_records/TASK_RUN_2026-05-24_1628.md`
