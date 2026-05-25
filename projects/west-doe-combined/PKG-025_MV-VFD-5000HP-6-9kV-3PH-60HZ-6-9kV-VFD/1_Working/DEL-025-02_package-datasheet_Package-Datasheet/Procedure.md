# Procedure: DEL-025-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-025-02_package-datasheet`, covering the `PKG-025` "MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD" package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 27.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`: voltage/service table, 6.9 kV MCC paragraph (Starting VFD KM-2150/2250 and MCC-8200), motor voltage and Zone 2 paragraph, electrical buildings paragraph, building list, grounding paragraphs, MV cable table, cable tray/conduit paragraphs, UPS services row, and inlet/sales compressor start-method paragraph.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 27 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-025` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support (OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010).
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-025-02_package-datasheet` and confirm the datasheet includes package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, and source-supported equipment/design criteria.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-025` and populate the interface matrix with all six facts: Electrical Power (`IFC-812CB082EA`), Grounding / Bonding (`IFC-3BE8D26B6B`), I&C / Control Cabling (`IFC-949E34ECEA`), Communications / Network (`IFC-EF46C006CC`), Maintenance Access (`IFC-3A60522074`), Structural / Foundations / Supports (`IFC-FB81FE736B`).
7. Read DBM electrical source slices for 6.9 kV MV service basis, Starting-VFD usage (KM-2150/2250) and synchronous transfer to MCC-8200, PF-correction-capacitor prohibition on the synchronous-transfer bus, MV cable specification, Zone 2 marking for VFD-fed motors, UPS-based MV breaker/protection control basis, grounding basis, and electrical-building housing context.
8. Search accessible package-specific requirements for PKG-025 in `_Sources/26020-Package_Requirements.docx`. If no source-supported package-specific match is found, mark detailed VFD parameters as `TBD`.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`; surface the 5,000/5,500/6,700 hp triad and the KM-2150/2250 binding question as human-ruling items rather than silently reconciling them.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
11. Draft Guidance to explain conservative interpretation, the 6.9 kV MV threshold mismatch, the Starting-VFD candidate context, the PF-correction-capacitor constraint, and human-ruling items.
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, the six-interface list, responsibility split, MV service voltage basis, Starting-VFD constraints, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 27, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All six applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Source-gap handling | VFD detailed parameters, quantity allocation, motor tag binding, and building assignment remain `TBD` unless source-supported. |
| Human ruling items | The 5,000/5,500/6,700 hp triad (HRR-025-02-001), the KM-2150/2250 Starting-VFD binding question (HRR-025-02-002), and PKG-025 quantity allocation (HRR-025-02-003) appear in the Guidance Conflict Table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
