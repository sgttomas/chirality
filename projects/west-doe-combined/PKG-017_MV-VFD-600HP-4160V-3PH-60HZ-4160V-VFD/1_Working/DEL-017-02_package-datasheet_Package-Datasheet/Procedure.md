# Procedure: DEL-017-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-017-02_package-datasheet`, covering the `PKG-017` MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 19.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (electrical voltage/service, electric driver basis, 4160V MCC, SCA-001 paragraphs, site basis) and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (electrical buildings paragraph, grounding/bonding paragraphs, cable/conduit paragraphs).
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state (`OPEN` or `INITIALIZED`) before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 19 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-017` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-017-02_package-datasheet` and confirm the datasheet includes package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, source-supported equipment/design criteria, and interface fact evidence.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-017` and populate the interface matrix with Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
7. Read DBM electrical source slices for the 4,160 V MV service bus, MV VFD housing in electrical buildings, harmonic/reactive-power treatment, grounding/bonding, cable/conduit separation, maintenance access, and ambient design.
8. Search accessible package-specific source material for `PKG-017` (workbook, DBMs, `26020-Package_Requirements.docx`). If no source-supported package-specific match is found for driven-motor identity, VFD output rating, duty, control profile, filters/reactors, cooling, enclosure rating, installation location, or supports, mark them `TBD`.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`. Use the documented MV service bus to ground rated input voltage; do not derive output rating or motor pairing without source.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices, including harmonic/reactive-power study deference, cable/circuit separation, grounding, maintenance-access preservation, and plant-PLC EtherNet integration pattern.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items, including the absence of a documented 600 HP MV VFD load in source and the mismatch with documented SCA-001 starting-VFD use for 5,200 HP inlet compressors.
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, interface list (all six facts), responsibility split, MV service basis, harmonic/reactive-power treatment, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 19, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All six applicable interfaces (Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports) are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Source-gap handling | Driven-motor identity, VFD output rating, duty basis, control profile, filters/reactors, cooling, enclosure, installation location, and supports remain `TBD` unless source-supported. |
| Harmonic / reactive-power treatment | Documented as a detailed electrical study item, with SCA-001 VE #37 capacitor-bank context preserved. |
| Human ruling items | Open ambiguities about the 600 HP MV VFD application, the 4160 V output side, and package-level I&C/Communications signal content appear in the Guidance conflict table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
