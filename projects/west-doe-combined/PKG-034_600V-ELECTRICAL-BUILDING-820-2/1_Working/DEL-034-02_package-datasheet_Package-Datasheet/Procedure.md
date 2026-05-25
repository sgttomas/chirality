# Procedure: DEL-034-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-034-02_package-datasheet`, covering the `PKG-034` 600V ELECTRICAL BUILDING (820-2) package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 36.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 36 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-034` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-034-02_package-datasheet` and confirm the datasheet includes the package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, source-supported equipment/design criteria, and all twelve interface-fact evidence artifacts.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-034` and populate the interface matrix with all twelve applicable interfaces.
7. Read DBM electrical-building source slices for prefabricated modular construction, general-purpose-area siting, n+1 HVAC, bottom cable entry, internal wiring (TECK/ACIC, EMT), possible housed equipment classes, grounding and bonding, cable tray, conduit, and maintenance access.
8. Read DBM Comp_and_Liquids source slices for 600 V MCC standby power (LV gen + transfer switch) and foundations basis.
9. Search accessible package-specific requirements for PKG-034 / 820-2. If no source-supported package-specific match is found, mark the internal equipment list, ratings, quantities, transformer feeder source, plot location, and area classification as `TBD`.
10. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
11. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
12. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
13. Draft this Procedure to make the production and checking sequence repeatable.
14. Perform cross-document consistency checks for package identity, interface list, responsibility split, building construction basis, and `TBD` items.
15. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
16. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 36, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All twelve applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Source-gap handling | PKG-034 internal equipment list, ratings, quantities, single-line, plot location, transformer source, area classification, and HVAC unit sizing remain `TBD` unless source-supported. |
| 820-2 identity preservation | "820-2" is carried as workbook-assigned identity; no scope is imported by analogy from other named 600 V electrical buildings. |
| Human ruling items | Open ambiguity for the "820-2" tag and PKG-034-specific scope appears in the Guidance conflict table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
