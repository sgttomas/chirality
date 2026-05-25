# Procedure: DEL-026-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-026-02_package-datasheet`, covering the `PKG-026` Transformer TXP-8300-2 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 28.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (facility electrical system, voltage/service table, transformers, electrical buildings, grounding/bonding, cable types, foundations) and supporting electrical context from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv` row `DEL-026-02_package-datasheet`.
3. Read workbook Packages row 28 and record package ID, WBS, CoA tracking number (26020-02-30-017), package name (full tri-voltage and dual-rating string), discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-026` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-026-02_package-datasheet` and confirm the datasheet includes package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, source-supported equipment/design criteria, and interface fact evidence.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-026` and populate the interface matrix with the seven applicable interfaces (`IFC-E9FC2B952D`, `IFC-FE5C9BD828`, `IFC-0230019D52`, `IFC-25E2CF2BD9`, `IFC-E6E0E1FA2B`, `IFC-93877B34D5`, `IFC-7DD82CAE51`).
7. Read DBM electrical source slices for the facility electrical system, voltage/service table (13.8 kV, 6.9 kV, 600 V classes), step-down distribution narrative, transformers paragraph (oil-filled, CEC spacing, foundations), grounding/bonding (100 A 10 s NGR on 6.9 kV; two-point ground grid; ground wells), cable types (13.8 kV TECK 15 kV / 133%, 6.9 kV TECK 8 kV / 100%), electrical buildings table, and foundations table.
8. Verify that the DBM voltage/service table does not establish a 0.4 kV service class and that the package name's 0.4 kV winding must be treated as `TBD` for service, loading, vector group, and grounding basis.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD` and ASSUMPTION labels for inferred items (oil-filled medium, location adjacency to 820-1 building, dual-rating cooling stages).
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items (0.4 kV tertiary, cooling class, QAS allocation).
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, interface list, responsibility split, medium-voltage rating, neutral grounding basis, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 28, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All seven applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Medium-voltage rating consistency | 13.8 kV primary and 6.9 kV secondary stated consistently; 0.4 kV tertiary handled as `TBD` consistently. |
| Grounding consistency | 6.9 kV neutral grounding (100 A, 10 s NGR, tripping system) stated consistently and not extended to unsupported voltage classes. |
| Source-gap handling | Cooling class, impedance, vector group, BIL, tap range, monitoring, foundation type, exact location, and tertiary winding service remain `TBD` unless source-supported. |
| Human ruling items | 0.4 kV tertiary winding ambiguity, dual-rating cooling class, and QAS allocation appear in the Guidance conflict table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
