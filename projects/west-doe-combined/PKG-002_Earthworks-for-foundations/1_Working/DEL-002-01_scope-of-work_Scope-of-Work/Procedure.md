# Procedure: DEL-002-01_scope-of-work — Scope of Work

## Purpose

Define the working procedure for producing and checking the PKG-002 Scope of Work deliverable from the accepted Gate 7 decomposition basis and locally accessible source materials.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local files `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Workbook package/interface source is available at `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- DBM civil/site source slices are available at `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Final geotechnical report is not available in the local source set; any dependent values remain `TBD` or source-qualified preliminary values.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md`: `DEL-002-01_scope-of-work`, PKG-002, Earthworks for foundations, Civil, EPC Scope of Work, EPC Integrator.
2. Confirm accepted decomposition basis from Gate 7 registers:
   - `DELIVERABLE_REGISTER.csv` for deliverable description, artifacts, scope item, objectives, source row, and notes;
   - `PACKAGE_REGISTER.csv` for package WBS, CoA tracking number, package description, responsibility basis, interfaces, exclusions, and source references;
   - `ARTIFACT_REGISTER.csv` for required artifact records;
   - `OBJECTIVE_DELIVERABLE_MAP.csv` for objective associations.
3. Confirm workbook source row 3 in `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet:
   - WBS `02`;
   - CoA tracking number `26020-01-42-001`;
   - package `Earthworks for foundations`;
   - discipline `Civil`;
   - interface flags for Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports.
4. Read the DBM source slices for construction scope, SEC-02 geotechnical/seismic basis, SEC-11 site/civil conditions, surface water/drainage, foundations/structural supports, and SEC-12 civil/structural governing content.
5. Draft the package scope section with workbook identity, Gate 7 deliverable identity, and the two source-supported physical interface types.
6. Draft the tagged equipment and package identity list. For this Civil package, use package/workbook identity and interface categories as the supported identity list; mark tagged equipment as `TBD` if no source-specific equipment tags are provided for the earthworks/foundation scope.
7. Draft the package function and integration narrative around grading, drainage, surface-water management, foundations/supports, and civil integration with roads, retention pond, modules, tanks, pipe racks, buildings, fencing, and security where supported by DBM text.
8. Draft the responsibility assignment record:
   - EPC Integrator owns the Scope of Work deliverable;
   - package execution responsibility remains source-dependent where EPC Integrator versus discipline subcontractor assignment is not closed.
9. Add a TBD/open-item register for final geotechnical report, civil drawings, final hydrology inputs, detailed foundation criteria, package-specific exclusions, and any missing source slices.
10. Cross-check terminology and values against `Datasheet.md`, `Specification.md`, and `Guidance.md`.

## Verification

| Verification step | Expected result |
|---|---|
| Identity check | Deliverable, package, WBS, CoA tracking number, discipline, responsible party, and source row match `Datasheet.md` and Gate 7 registers. |
| Artifact check | The Scope of Work contains or explicitly plans the four required artifacts. |
| Interface check | Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports are both included; unsupported interfaces are not added as requirements. |
| Source-grounding check | Requirements cite Gate 7 registers, workbook row 3, or DBM source slices. |
| TBD discipline check | Final geotechnical report, civil drawings, hydrology, detailed construction values, and package-specific exclusions remain TBD where no source is available. |
| Conflict check | Responsibility ambiguity is carried in the Guidance conflict table until human ruling. |

## Records

- Completed `Datasheet.md`.
- Completed `Specification.md`.
- Completed `Guidance.md`, including Conflict Table CT-001.
- Completed `Procedure.md`.
- `_STATUS.md` safe state update from `OPEN` to `INITIALIZED` when Pass 1+2 completes.
- TASK run record under `_run_records/`.
