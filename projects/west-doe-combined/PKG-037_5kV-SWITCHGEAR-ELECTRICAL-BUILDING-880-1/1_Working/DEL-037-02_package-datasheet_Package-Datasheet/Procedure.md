# Procedure: DEL-037-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-037-02_package-datasheet`, covering the `PKG-037` 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1) package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 39.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Electrical Buildings, voltage/service table, medium-voltage cable table, electrical buildings list, grounding and bonding, cable tray, conduit, area classification) and supporting electrical-building and foundation context from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 39 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-037` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-037-02_package-datasheet` and confirm the datasheet includes package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, source-supported equipment/design criteria, and interface fact evidence rows for all twelve applicable interfaces.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-037` and populate the interface matrix with all twelve applicable interfaces.
7. Read DBM electrical source slices for: Electrical Buildings construction; voltage and service classes; medium-voltage cable insulation ratings; electrical buildings list; grounding and bonding; cable tray and conduit; area classification; and building HVAC.
8. Reconcile the package name string "5kV" and building token `880-1` against DBM voltage classes and the DBM Electrical Buildings list. Where reconciliation is not possible from the accessible source set, mark `TBD` and create or update Conflict Table entries.
9. Search accessible package-specific requirements for PKG-037. If no source-supported package-specific match is found, mark detailed switchgear/MCC/UPS/transformer/network/PLC lineup, ratings, and quantities as `TBD`.
10. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
11. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
12. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
13. Draft this Procedure to make the production and checking sequence repeatable.
14. Perform cross-document consistency checks for package identity, twelve-interface list, responsibility split, building construction basis, and `TBD` items.
15. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
16. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 39, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All twelve applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Voltage / building identifier handling | "5kV" and `880-1` are carried as workbook identity and flagged in the Conflict Table; no unsupported bus voltage or building assignment is asserted. |
| Source-gap handling | Equipment lineup, ratings, quantities, BoM, and siting coordinates remain `TBD` unless source-supported. |
| Human ruling items | Open ambiguities for voltage class, building identifier, and equipment lineup appear in the Guidance Conflict Table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
