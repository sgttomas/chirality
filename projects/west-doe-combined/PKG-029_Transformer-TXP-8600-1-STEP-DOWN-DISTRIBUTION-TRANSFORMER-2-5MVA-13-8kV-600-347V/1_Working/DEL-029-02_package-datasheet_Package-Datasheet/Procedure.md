# Procedure: DEL-029-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-029-02_package-datasheet`, covering the `PKG-029` Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 31.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (electrical distribution, System Voltages, Standby Power, Transformers, grounding/bonding, cable tray, conduit, electrical buildings, foundations).
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv` row `DEL-029-02_package-datasheet`.
3. Read workbook Packages row 31 and record package ID, equipment tag, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-029` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-029-02_package-datasheet` and confirm the datasheet includes package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, source-supported equipment/design criteria, and interface fact evidence for each `PKG-029` interface row.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-029` and populate the interface matrix with Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
7. Read DBM electrical source slices for facility distribution, System Voltages, Standby Power, Transformers, grounding/bonding, cable tray, conduit, electrical buildings, and foundations.
8. Search accessible package-specific requirements for PKG-029 in `_Sources/26020-Package_Requirements.docx`. If no source-supported package-specific match is found, mark detailed transformer parameters as `TBD`.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD` and label package-title-derived values as `ASSUMPTION`.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices; cite the Guidance Conflict Table where unsupported values are deferred.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items, including the 600/347V vs DBM 600 V 3-wire HRG reconciliation.
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, interface list, responsibility split, voltage basis, transformer construction basis, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 31, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All seven applicable PKG-029 interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Voltage-basis reconciliation | The 600/347V package-title notation vs DBM 600 V 3-wire HRG discrepancy is captured in the Conflict Table (HRR-029-02-001) and not silently resolved. |
| Source-gap handling | Nameplate corroboration, insulation/cooling, secondary configuration, foundation, containment, location, feeder, and load list remain `TBD` unless source-supported. |
| Human ruling items | HRR-029-02-001 (voltage basis), HRR-029-02-002 (nameplate corroboration), and HRR-029-02-003 (oil-filled vs dry-type classification) appear in the Guidance Conflict Table and the run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
