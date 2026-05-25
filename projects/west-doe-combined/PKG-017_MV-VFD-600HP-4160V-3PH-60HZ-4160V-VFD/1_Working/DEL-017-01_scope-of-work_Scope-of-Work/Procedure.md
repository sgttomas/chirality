# Procedure: DEL-017-01_scope-of-work

## Purpose

Define the procedure for producing and checking the EPC Scope of Work for `DEL-017-01_scope-of-work`, covering the `PKG-017` "MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD" package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 19.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`: System Voltages, Incoming Power and Transformers, 4160V MCC, 600V MCC and Standby Power, Electrical Buildings/Raceways, Area Classification, and Inlet Compressor Drive sections.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify against `DELIVERABLE_REGISTER.csv` row `DEL-017-01_scope-of-work`.
3. Read workbook Packages row 19 and record package ID, WBS, CoA tracking number, package name, discipline, and applicable interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-017` and carry forward the responsibility model, inclusion criteria, exclusions (workbook-stated TBD), source references, and objective support (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010).
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-017-01_scope-of-work` (ART-48D5FBB23A, ART-53AEA33639, ART-52F1155060, ART-2C11F1D37E) and confirm the Scope of Work includes the four required artifact slots.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-017` and populate the interface matrix with all six applicable interfaces: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
7. Read DBM electrical source slices for MV service voltage, 4160V MCC interface, starting-VFD basis (SCA-001 VE #34), capacitor-bank removal (SCA-001 VE #37), raceway/power-control separation, electrical buildings, area classification, and inlet compressor drive characteristics.
8. Search accessible package-specific requirements for PKG-017. If no source-supported package-specific match is found, mark detailed VFD parameters (rating, topology, cooling, tagged equipment, location) as `TBD`.
9. Compare the workbook title ("MV VFD - 600HP, 4160V") with DBM MV drive characteristics (4,000 V, 5,200 hp for KM-2150/KM-2250) and the 600V MCC assignment of 600 V VFDs. Capture any inconsistency in the Guidance Conflict Table and as `NEEDS_HUMAN_RULING`.
10. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
11. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
12. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
13. Draft this Procedure to make the production and checking sequence repeatable.
14. Perform cross-document consistency checks for package identity, interface list, responsibility split, MV service basis, governance citations (SCA-001 VE #34 and VE #37), and `TBD` items.
15. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
16. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 19, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All six applicable interfaces for PKG-017 are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Governance consistency | SCA-001 VE #34 (starting VFDs) and VE #37 (capacitor-bank removal where VFDs are present) are reflected as governing constraints, not pre-resolved design choices. |
| Source-gap handling | Driven-equipment identity, VFD rating, topology, tagged equipment, supports, and location remain `TBD` unless source-supported. |
| Human ruling items | Workbook-title-vs-DBM-rating conflict (HRR-017-01-001) and unidentified-tagged-equipment item (HRR-017-01-002) appear in the Guidance Conflict Table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
