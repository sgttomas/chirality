# Procedure: Construction Work Package

## Purpose

Define the working procedure to produce and check the PKG-009 controls Construction Work Package for Phase 2.2 initialization. The procedure is for authoring and validating the CWP artifact set, not for performing field construction.

## Prerequisites

- Accepted upstream decomposition snapshot: Gate 7 final published PROJECT_DECOMP snapshot dated 2026-05-24.
- Deliverable-local context files: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`.
- Accessible source files:
  - Gate 7 `PROJECT_DECOMP.md`, `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`;
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx`;
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`;
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Declared upstream dependencies: none declared during PREPARATION.
- Declared downstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm the deliverable identity is `DEL-009-03_construction-work-package`, parent package `PKG-009`, WBS 02, discipline Controls, responsible party EPC Integrator.
2. Confirm the deliverable is one of the mandatory EPC Integrator anchor deliverables and that its scope is construction, installation, tie-in, inspection, and turnover. Source: `PROJECT_DECOMP.md` lines 118-127 and 205.
3. Build the CWP artifact index with these required artifacts:
   - construction work package;
   - installation and tie-in workface plan;
   - construction interface and turnover checklist.
4. Add interface checklist headings for all PKG-009 applicable workbook interfaces:
   - Process Piping;
   - Utility Piping;
   - Relief / Flare / Vent;
   - Electrical Power;
   - I&C / Control Cabling;
   - Communications / Network;
   - Building HVAC / Services;
   - Fire & Gas / Safety Systems.
5. Under I&C / Control Cabling, include a Remote I/O routing/readiness check for BPCS process and safety devices where practical. Mark actual panel/cable details as `TBD` unless supported by later source slices.
6. Under Fire & Gas / Safety Systems, include a local emergency shutdown push-button tie-in check where unit control panels are applicable. Mark applicable unit panels and cause/effect references as `TBD`.
7. Under Electrical Power, Communications / Network, and Building HVAC / Services, include construction readiness checks for plant PLC/control panels, network racks, conduit or adjacent equipment interfaces only where supported by issued design documents; otherwise mark applicability `TBD`.
8. Include an environmental suitability check for exposed control panels, instrumentation, field devices, and package buildings against the -40 deg C minimum ambient condition unless a more severe process or vendor condition applies.
9. Add an open-item/human-ruling entry for controls power-panel interface treatment:
   - accepted Gate 7/Gate 6 basis: keep as interface facts/artifacts under the package datasheet with no separate package/deliverable;
   - unresolved human question: confirm whether controls power-panel interfaces should be tracked separately.
10. Review the CWP for unsupported values. Replace unsupported quantities, locations, drawing numbers, installation durations, and inspection hold points with `TBD`.
11. Cross-check the Datasheet, Specification, Guidance, and Procedure for consistent terms, interfaces, requirements, and verification hooks.

## Verification

| Check | Acceptance criterion |
|---|---|
| Identity | Deliverable ID, package ID, WBS, discipline, type, and responsible party match `_CONTEXT.md` and Gate 7 registers. |
| Artifact coverage | Construction work package, installation/tie-in workface plan, and construction interface/turnover checklist are present or listed as controlled attachments. |
| Interface coverage | All eight PKG-009 applicable interfaces appear in the checklist with either source-supported content or `TBD`. |
| Source grounding | Non-trivial requirements cite Gate 7 rows, workbook row, or DBM source slices. |
| Unknowns | Package-specific construction details not present in accessible sources are marked `TBD`. |
| Human ruling | Controls power-panel interface treatment is visible as `HRR-009-03-001`. |
| Cross-document consistency | Requirement IDs in `Specification.md` have corresponding procedural or verification hooks here. |

## Records

- Construction work package.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Open-item/human-ruling log containing `HRR-009-03-001`.
- Evidence of interface closure and turnover readiness.
