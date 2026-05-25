# Procedure: DEL-033-03_construction-work-package

## Purpose

Define the procedure for producing and checking the Construction Work Package for `DEL-033-03_construction-work-package`, covering the `PKG-033` 4160V SWITCHGEAR ELECTRICAL BUILDING (830-2).

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 35.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` and supporting 4160V MCC/4.16 kV context from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv` row `DEL-033-03_construction-work-package`.
3. Read workbook Packages row 35 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-033` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `INTERFACE_REGISTER.csv` rows for `PKG-033` and populate the interface coordination matrix with all twelve applicable interfaces.
6. Read DBM electrical source slices for medium-voltage service basis (4.160 kV LRG, 5 kV TECK cable), electrical-building installation conventions (prefabricated, modular, pile-elevated, bottom-entry, n+1 HVAC, TECK/ACIC, EMT, GFI, equipment-removal doors), grounding/bonding installation, cable tray and conduit routing, and 4.16 kV motor starting (VFD/soft-starter requirements TBD).
7. Read the Comp_and_Liquids DBM 4160V MCC source slice for contextual 4.16 kV switchgear/MCC arrangement evidence.
8. Search the accessible source set for a PKG-033 package-specific construction basis. If no source-supported package-specific match is found (including 830-2 location/service), mark detailed switchgear bus/breaker/protection, foundation/pile loads, schedule/tie-in windows, and per-circuit schedules as `TBD`.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items, including the `830-2` vs `830-1` identity ruling.
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, twelve-interface list, responsibility split, MV service basis, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 35, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All twelve applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration/construction responsibilities are not conflated. |
| Source-gap handling | Switchgear bus/breaker/protection, 830-2 location/service, foundation/pile loads, schedule/tie-in windows, and per-circuit cable schedules remain `TBD` unless source-supported. |
| Human ruling items | The 830-2 vs 830-1 identity question and the absence of a package-specific switchgear basis are recorded in the Guidance conflict table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
