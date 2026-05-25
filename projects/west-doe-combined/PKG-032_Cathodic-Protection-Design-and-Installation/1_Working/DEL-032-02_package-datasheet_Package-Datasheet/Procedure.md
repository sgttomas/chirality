# Procedure: DEL-032-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-032-02_package-datasheet`, covering the `PKG-032` Cathodic Protection Design and Installation package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 34.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM source slices: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` ("Cathodic Protection" section and SEC-12 assumptions table) and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (electrical scope paragraph).
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 34 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-032` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-032-02_package-datasheet` and confirm the datasheet includes package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, and interface fact evidence.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-032` and populate the interface matrix with Electrical Power, Grounding / Bonding, I&C / Control Cabling, and Communications / Network.
7. Read DBM source slices: the Deepcut DBM "Cathodic Protection" section and SEC-12 assumptions row; the Comp & Liquids DBM electrical scope paragraph. Record both scope positions verbatim or by cited summary; do not silently reconcile.
8. Search accessible package-specific requirements for `PKG-032`. If no source-supported package-specific match is found, mark detailed CP parameters as `TBD`.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items, including the DBM scope-position conflict.
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, interface list, responsibility split, scope-position handling, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 34, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All four applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Scope-position handling | Both DBM positions on CP scope appear in Datasheet/Guidance and are routed to human ruling, not silently reconciled. |
| Source-gap handling | CP detailed parameters remain `TBD` unless source-supported. |
| Human ruling items | DBM scope-position conflict and CP-specific source-gap items appear in the Guidance conflict table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
