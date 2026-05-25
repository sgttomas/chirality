# Procedure: EPC / Civil Discipline Production Package

## Purpose

Define the working procedure to produce and check the DEL-006-04 Civil discipline production package for PKG-006 Containment Berms using accepted Gate 7 truth and available civil DBM source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Gate 7 PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv, ARTIFACT_REGISTER.csv, INTERFACE_REGISTER.csv, and OBJECTIVE_DELIVERABLE_MAP.csv.
- Civil source slices from:
  - DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md.
  - DBM-Deepcut/4-25_Deepcut_DBM.md.
- Declared dependencies review: no declared upstream or downstream dependencies are currently listed in `_DEPENDENCIES.md`.
- Open external inputs to be tracked as TBD until accepted: geotechnical assessment report, topographical survey and grade surface file, plot plan, detailed engineering drainage design, and final hydrology confirmation.

## Steps

1. Confirm deliverable identity against `_CONTEXT.md` and DELIVERABLE_REGISTER.csv.
2. Confirm package identity against PACKAGE_REGISTER.csv for PKG-006.
3. Record the accepted interface facts from INTERFACE_REGISTER.csv:
   - Drain / Containment.
   - Grading / Site Drainage / Spill Containment.
4. Establish the civil source basis from the DBM:
   - Civil scope and surface-water management from 3-25_Comp_and_Liquids_DBM.md.
   - Civil/structural basis, grading, drainage, retention pond, and surface-control principles from 4-25_Deepcut_DBM.md.
5. Build the discipline production package basis using only source-supported requirements and assumptions explicitly labeled as assumptions.
6. Create or update the source-limited requirements closure record, including at minimum:
   - Missing detailed discipline deliverable register.
   - Missing final geotechnical report.
   - Missing final topographical survey / grade surface file.
   - Missing final plot-plan/retention-pond location coordination.
   - Missing final hydrology and detailed drainage design values.
7. Build the interface matrix and trace each listed interface back to the Gate 7 interface register.
8. Check that process-contaminated drainage is kept separate from surface-water discharge logic.
9. Check that final design values not available in the source set remain `TBD`.
10. Prepare the package for review by the EPC Integrator or assigned civil discipline subcontractor.

## Verification

| Check | Method |
|---|---|
| Identity verification | Compare deliverable and package tables to `_CONTEXT.md`, DELIVERABLE_REGISTER.csv, and PACKAGE_REGISTER.csv. |
| Interface verification | Confirm both accepted interface facts are included and cited to INTERFACE_REGISTER.csv. |
| Source grounding | Confirm each non-trivial requirement cites Gate 7 registers or DBM source slices. |
| Open input verification | Confirm unresolved inputs are listed as `TBD` or Human Ruling Required items. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use consistent names, interface labels, and source basis. |
| Dependency check | Confirm blockers are not inferred from undeclared relationships; use declared dependency edges only. |

## Records

- Discipline production package basis.
- TBD discipline deliverable register.
- Source-limited requirements closure record.
- Interface matrix for Drain / Containment and Grading / Site Drainage / Spill Containment.
- Open input / Human Ruling Required log.
- Cross-document consistency check record.
