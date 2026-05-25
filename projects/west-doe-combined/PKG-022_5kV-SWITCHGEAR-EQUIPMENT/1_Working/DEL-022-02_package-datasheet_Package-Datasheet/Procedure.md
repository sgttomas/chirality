# Procedure: DEL-022-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-022-02_package-datasheet`, covering the `PKG-022` 5kV SWITCHGEAR EQUIPMENT package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 24.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` and cross-facility electrical interface context from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 24 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-022` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-022-02_package-datasheet` and confirm the datasheet covers package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, source-supported equipment/design criteria, and the six interface fact evidence entries.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-022` and populate the interface matrix with Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
7. Read DBM electrical source slices for plant power distribution, system voltages, standby power, electrical buildings, grounding/bonding, cable/wire/raceways, motor control, and the governing electrical specifications table.
8. Confirm the governing equipment specifications named in DBM Table 12-1 that apply (`ELC-QAS-000007-001` Medium Voltage Switchgear and `ELC-QAS-000003-001` Electrical Requirements for Packaged Equipment). Mark document locations as `TBD` if the documents themselves are not accessible.
9. Search accessible package-specific requirements for `PKG-022`. If no source-supported package-specific match is found, mark detailed switchgear parameters (nominal voltage, bus ampacity, short-circuit rating, breaker complement, protection scheme) as `TBD`.
10. Surface the voltage-class discrepancy between the package title "5kV SWITCHGEAR EQUIPMENT" and the DBM medium-voltage levels (13.8 kV main, 6.9 kV, 4.160 kV; "5 kV" only as 4.16 kV cable insulation class) as a human-ruling item. Do not silently resolve.
11. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
12. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
13. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items, including the voltage-class conflict.
14. Draft this Procedure to make the production and checking sequence repeatable.
15. Perform cross-document consistency checks for package identity, interface list, responsibility split, governing specifications, and `TBD` items.
16. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
17. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 24, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All six applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Source-gap handling | Switchgear detailed parameters (including nominal voltage) remain `TBD` unless source-supported. |
| Human ruling items | Voltage-class disambiguation, equipment-list allocation, and governing-specification accessibility appear in the Guidance conflict table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
