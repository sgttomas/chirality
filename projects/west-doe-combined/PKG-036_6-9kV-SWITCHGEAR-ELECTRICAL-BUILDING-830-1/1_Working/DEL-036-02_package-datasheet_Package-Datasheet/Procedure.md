# Procedure: DEL-036-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-036-02_package-datasheet`, covering the `PKG-036` 6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1) package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 38.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Electrical Buildings L2971-2979, Medium-voltage services L2935, Power distribution L2917-2925, Grounding L2985-2989, Cable/raceway L2999/L3008, Area classification L2911, Distance criteria L298, Equipment list L2879-2880, Electrical-building list L2811-2816, 6.9 kV MCC scope L2955).
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv` row `DEL-036-02_package-datasheet`.
3. Read workbook Packages row 38 and record package ID, WBS, CoA tracking number, package name, discipline, and the twelve interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-036` and carry forward the responsibility model, inclusion criteria, exclusion `TBD`, source references, and objective support list.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-036-02_package-datasheet` and confirm the datasheet includes the package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, source-supported equipment/design criteria, and interface fact evidence (one per applicable interface).
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-036` and populate the interface matrix with all twelve applicable interfaces.
7. Read DBM electrical source slices listed in Prerequisites for medium-voltage service basis, electrical-building construction basis, grounding/bonding, cable/raceway, area classification, and 25 m fired-heater separation.
8. Search accessible package-specific requirements (`26020-Package_Requirements.docx`) for PKG-036 / 830-1 / 6.9 kV switchgear electrical building content. If no source-supported package-specific match is found, mark detailed switchgear / MCC / UPS / transformer / building-dimension parameters as `TBD`.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`; preserve the workbook spelling of the package name.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items, including the 830-1 building-identity conflict.
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, twelve-interface list, responsibility split, MV service basis, grounding/cable bases, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 38, Gate 7 registers, DBM source slices (with line references), or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All twelve applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Source-gap handling | Switchgear / MCC / UPS / transformer / building-dimension parameters remain `TBD` unless source-supported. |
| Human ruling items | 830-1 building-identity conflict and switchgear/equipment allocation ambiguity appear in the Guidance Conflict Table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
