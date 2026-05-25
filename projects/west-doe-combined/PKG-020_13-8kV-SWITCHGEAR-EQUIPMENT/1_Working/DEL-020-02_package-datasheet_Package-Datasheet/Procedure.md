# Procedure: DEL-020-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-020-02_package-datasheet`, covering the `PKG-020` 13.8kV SWITCHGEAR EQUIPMENT package (plant main power distribution center).

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 22.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Power System, System Voltages, Standby Power, Electrical Buildings, Grounding and Bonding, Cable/Wire/Raceways, SEC-12 Electrical Basis).
- Cross-facility context from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Power Supply, Standby Power, Cable/routing).
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 22 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-020` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-020-02_package-datasheet` and confirm the datasheet includes package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, and interface fact evidence.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-020` and populate the interface matrix with Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports.
7. Read DBM-Deepcut SEC-12 electrical basis source slices for the Power System paragraph, System Voltages table, Standby Power, Transformers, Electrical Buildings, Grounding and Bonding, and Cable/Wire/Raceways.
8. Read DBM-Comp_and_Liquids power-supply slices for the 03-25 sub-feed from the 04-25 13.8 kV Main Switchgear Electrical Building and the revised LV standby-power basis.
9. Search accessible package-specific requirements (`26020-Package_Requirements.docx`) for PKG-020. If no source-supported match is found, mark detailed switchgear configuration parameters as `TBD`.
10. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
11. Draft the Specification requirements and verification hooks from the Datasheet basis and DBM source slices.
12. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
13. Draft this Procedure to make the production and checking sequence repeatable.
14. Perform cross-document consistency checks for package identity, interface list, responsibility split, voltage/grounding values, standby-power scope, and `TBD` items.
15. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
16. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 22, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All six applicable interfaces (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor switchgear design responsibilities and EPC facility integration responsibilities are not conflated. |
| Voltage/grounding consistency | 13.8 kV, 3 phase, 3 wire, 60 Hz, LRG bus basis and the utility 200 A/10 s NGR are cited consistently. |
| Standby-power consistency | The datasheet does not include centralized 13.8 kV emergency-generator provisions; LV-MCC standby-power basis is reflected. |
| Source-gap handling | Breaker counts, breaker ratings, bus ampacity, short-circuit/withstand rating, metering, relaying, and arc-flash mitigation remain `TBD` unless source-supported. |
| Human ruling items | Open ambiguities about 25 kV utility voltage TBC, absence of PKG-020 in `26020-Package_Requirements.docx`, and the revised standby-power scope appear in the Guidance conflict table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
