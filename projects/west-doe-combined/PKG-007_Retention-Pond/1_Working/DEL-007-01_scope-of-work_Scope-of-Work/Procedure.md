# Procedure: DEL-007-01_scope-of-work — Scope of Work

## Purpose

Define the procedure for producing and checking the PKG-007 Retention Pond Scope of Work so the deliverable remains aligned with accepted Gate 7 decomposition truth and accessible source materials.

## Prerequisites

- Accepted Gate 7 final published PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Source materials are accessible:
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx`, worksheet row 8.
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, rainfall basis table, "Geotechnical and Seismic Basis", "Site and Civil Conditions", and "Surface Water and Drainage".
- Declared upstream dependencies: none declared during PREPARATION. Source: `_DEPENDENCIES.md`.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md` and Gate 7 `DELIVERABLE_REGISTER.csv` row 26.
2. Confirm package identity from workbook export worksheet row 8 and Gate 7 `PACKAGE_REGISTER.csv` row 8:
   - PKG-007.
   - Retention Pond.
   - WBS 02.
   - CoA tracking number 26020-02-42-007.
   - Civil discipline.
3. Confirm governed scope unit SOW-0007 from Gate 7 `SCOPE_LEDGER.csv` row 8.
4. List required Scope of Work artifacts from Gate 7 `ARTIFACT_REGISTER.csv` rows 86-89:
   - Package scope of work.
   - Tagged equipment and package identity list.
   - Package function and whole-facility integration narrative.
   - Responsibility assignment record.
5. Confirm package interfaces from Gate 7 `INTERFACE_REGISTER.csv` rows 14-15 and workbook export worksheet row 8:
   - Drain / Containment.
   - Grading / Site Drainage / Spill Containment.
6. Draft the package function narrative from the DBM civil and surface-water source slices:
   - Civil design covers grading, drainage, surface-water management, retention pond, and related civil/site systems.
   - Surface-water management prevents uncontrolled offsite discharge, protects process areas, and supports construction and operations access.
   - Process-contaminated drainage is routed to the appropriate drain or containment system rather than surface-water discharge.
7. Record current basis conditions and open items:
   - Rainfall values and NBCC 2020 Dawson Creek proxy status.
   - Final hydrology update as `TBD`.
   - Preliminary geotechnical basis and final geotechnical report as `TBD`.
   - Package-specific retention pond geometry, capacity, discharge details, and exclusions as `TBD` unless source-supported.
8. Prepare the responsibility assignment record with EPC Integrator as deliverable owner and mark any discipline subcontractor split as `TBD` unless source-supported.
9. Perform the cross-document consistency checks listed in the four-documents skill:
   - Datasheet attributes align with Specification requirements.
   - Specification requirements have Procedure verification hooks.
   - Guidance rationale does not overstate source support.
   - Terminology and numeric values are consistent.

## Verification

| Check | Acceptance criterion |
|---|---|
| Identity check | Deliverable ID, package ID, WBS, CoA tracking number, discipline, and responsible party match `_CONTEXT.md`, Gate 7 registers, and workbook export row 8. |
| Interface check | Only Drain / Containment and Grading / Site Drainage / Spill Containment are listed as declared interfaces unless later source-supported. |
| Source-grounding check | All non-trivial requirements cite Gate 7 rows, workbook row 8, or DBM civil/surface-water slices. |
| TBD check | Pond capacity, geometry, final hydrology, final geotechnical data, exclusions, and subcontractor split remain `TBD` where unsupported. |
| Dependency check | No advisory blocker is asserted because no declared upstream dependencies are present. |

## Records

- Completed `Datasheet.md`.
- Completed `Specification.md`.
- Completed `Guidance.md`, including Conflict Table / human-ruling items.
- Completed `Procedure.md`.
- Updated `_STATUS.md` if the current state permits safe `OPEN` to `INITIALIZED` transition.
- TASK run record under `_run_records/`.
