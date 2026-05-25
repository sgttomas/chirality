# Procedure: DEL-031-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-031-02_package-datasheet`, covering the `PKG-031` Transformer TXP-8500-1 STEP DOWN DISTRIBUTION TRANSFORMER (3 MVA, 13.8 kV / 600 V / 347 V) package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 33.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (electrical systems, System Voltages, Transformers, Grounding and Bonding, Cable/Wire/Raceways, Electrical Buildings, Foundations).
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 33 and record package ID, WBS, CoA tracking number, equipment tag (TXP-8500-1), package name, discipline, ratings (3 MVA; 13.8 kV / 600 V / 347 V), and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-031` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-031-02_package-datasheet` and confirm the datasheet includes package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, source-supported equipment/design criteria, and interface fact evidence.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-031` and populate the interface matrix with Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
7. Read DBM electrical source slices for 13.8 kV distribution, System Voltages, transformer spacing/foundation/containment basis, grounding/bonding, cable types (TECK 15 kV primary; ACWU 600 V secondary), electrical buildings, and maintenance access.
8. Search accessible package-specific requirements for PKG-031 / TXP-8500-1. If no source-supported package-specific match is found, mark detailed transformer parameters (construction class, impedance, vector group, taps, BIL, cooling, losses, noise, containment outcome, installation location, relaying) as `TBD`.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, equipment tag, ratings, interface list, responsibility split, voltage/cable basis, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 33, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Identity consistency | TXP-8500-1, 3 MVA, 13.8 kV, 600 V, and 347 V appear consistently across all four documents. |
| Interface consistency | All seven applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Source-gap handling | Transformer construction class, impedance, vector group, taps, BIL, cooling, losses, noise, containment outcome, installation location, and protective relaying remain `TBD` unless source-supported. |
| Human ruling items | Open ambiguity about construction class, quantity allocation, and installation location appears in the Guidance conflict table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
