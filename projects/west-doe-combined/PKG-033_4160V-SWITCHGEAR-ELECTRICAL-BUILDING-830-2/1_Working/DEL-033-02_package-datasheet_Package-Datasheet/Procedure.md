# Procedure: DEL-033-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-033-02_package-datasheet`, covering the `PKG-033` 4160V SWITCHGEAR ELECTRICAL BUILDING (830-2) package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 35.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` and supporting electrical-building context from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 35 and record package ID, WBS, CoA tracking number, package name (including building tag "830-2"), discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-033` and carry forward the responsibility model, inclusion criteria, exclusions (TBD), source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-033-02_package-datasheet` and confirm the datasheet includes package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, source-supported equipment/design criteria, and interface fact evidence for each interface.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-033` and populate the interface matrix with all twelve applicable interfaces (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports).
7. Read DBM electrical source slices for the medium-voltage services basis, electrical-buildings configuration (prefabricated, climate-controlled, n+1 HVAC, bottom cable entry, pile-supported), grounding/bonding, cable tray/conduit, area classification, and standby power.
8. Cross-check the "830-2" building tag against the DBM electrical-building list. If the tag is not explicitly enumerated, surface the ambiguity as `NEEDS_HUMAN_RULING` and do not invent a process service for the building.
9. Search accessible package-specific requirements for PKG-033 in `26020-Package_Requirements.docx`. If no confirmed package-specific match is found, mark detailed switchgear and building parameters as `TBD`.
10. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
11. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
12. Draft the Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
13. Draft this Procedure to make the production and checking sequence repeatable.
14. Perform cross-document consistency checks for package identity, interface list, responsibility split, switchgear voltage basis, building configuration, and `TBD` items.
15. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
16. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 35, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All twelve applicable interfaces are present and consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Source-gap handling | Detailed switchgear and building parameters remain `TBD` unless source-supported. |
| Human ruling items | Open ambiguity about the "830-2" building tag, MV switchgear quantity allocation, and missing package-specific requirements source appears in the Guidance conflict table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
