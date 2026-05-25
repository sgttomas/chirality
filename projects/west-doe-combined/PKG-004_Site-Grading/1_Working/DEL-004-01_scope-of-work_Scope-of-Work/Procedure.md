# Procedure: Scope of Work

## Purpose

This procedure describes how to produce and verify the PKG-004 Site Grading scope-of-work deliverable using the accepted Gate 7 decomposition snapshot, workbook row 5, and accessible DBM civil source slices.

## Prerequisites

- Accepted upstream decomposition snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`.
- Deliverable-local context files: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row 5.
- DBM source slices: `4-25_Deepcut_DBM.md`, `Geotechnical and Topographical Assumptions`, `Site Grading and Surface Water Management`; `3-25_Comp_and_Liquids_DBM.md`, civil design slices at lines 124 and 688.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md` at initialization.
- Human ruling prerequisite: resolve HRR-001 before final responsibility assignment is treated as closed.

## Steps

1. Confirm deliverable identity against `_CONTEXT.md` and Gate 7 `DELIVERABLE_REGISTER.csv`.
2. Confirm package identity against Gate 7 `PACKAGE_REGISTER.csv` and workbook row 5:
   - Package ID `PKG-004`.
   - Workbook ID `4`.
   - WBS `02`.
   - CoA tracking number `26020-01-42-003`.
   - Package name `Site Grading`.
   - Discipline `Civil`.
3. Confirm required scope-of-work artifacts against Gate 7 `ARTIFACT_REGISTER.csv` rows for `DEL-004-01_scope-of-work`.
4. Confirm recorded interfaces against Gate 7 `INTERFACE_REGISTER.csv` and workbook row 5:
   - Drain / Containment.
   - Grading / Site Drainage / Spill Containment.
5. Build the package function and integration narrative around source-supported civil grading, drainage, retention pond, surface-water management, and spill-containment considerations.
6. Insert DBM-supported grading and drainage values:
   - Main pipe rack equal-elevation ridges.
   - Facility pad slope 1.5% down from pipe racks to each side.
   - Reduced pad slope allowance of 1.0% where required for pile-cap elevations.
   - Maximum grade slope of 3H:1V unless engineered or mandated otherwise by the geotechnical report.
   - Ditch slope minimum 0.2%.
   - Culvert slope minimum 0.5%, preferred 1.0%.
   - Ditch and culvert storm basis of 1:10 year, 15 minute rainfall event, with IDF duration to be confirmed.
7. Mark values as `TBD` when closure depends on unavailable or future inputs:
   - Geotechnical report parameters.
   - Topographical survey and grade surface file format/data model/final content.
   - Retention pond location and capacity.
   - Tagged equipment list.
   - Package-specific exclusions.
   - External clause-level codes and standards.
8. Prepare the responsibility assignment record using EPC Integrator as deliverable owner and retaining the package-register uncertainty about discipline subcontractor execution support until HRR-001 is resolved.
9. Cross-check Datasheet, Specification, Guidance, and Procedure for consistent terminology, values, source references, and `TBD` treatment.
10. Record unresolved conflicts or rulings in `Guidance.md` Conflict Table.

## Verification

| Check | Acceptance basis |
|---|---|
| Identity | Matches `_CONTEXT.md`, Gate 7 `DELIVERABLE_REGISTER.csv`, Gate 7 `PACKAGE_REGISTER.csv`, and workbook row 5. |
| Interfaces | Drain / Containment and Grading / Site Drainage / Spill Containment appear consistently and are traceable to Gate 7 `INTERFACE_REGISTER.csv` and workbook row 5. |
| Artifacts | Required artifact list matches Gate 7 `ARTIFACT_REGISTER.csv`. |
| Grading and drainage values | Values match `4-25_Deepcut_DBM.md`, `Site Grading and Surface Water Management`. |
| Open values | Report-dependent and detailed-engineering-dependent values remain `TBD`. |
| Responsibility | EPC Integrator deliverable ownership is stated; package execution responsibility uncertainty is retained pending HRR-001. |
| Dependencies | No blockers are asserted because no declared upstream dependencies are listed. |

## Records

- Completed `Datasheet.md`.
- Completed `Specification.md`.
- Completed `Guidance.md`, including Conflict Table.
- Completed `Procedure.md`.
- Updated `_STATUS.md` showing `INITIALIZED` if the run started from `OPEN`.
- TASK run record under `_run_records/`.
