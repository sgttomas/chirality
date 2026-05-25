# Procedure: DEL-021-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-021-02_package-datasheet`, covering the `PKG-021` 6.9kV SWITCHGEAR EQUIPMENT package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 23.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (facility electrical system narrative, MV voltage/service table, 6.9 kV MCC paragraph, electrical buildings list, grounding/bonding, neutral grounding, MV cable table, UPS services, cable tray/conduit paragraphs) and supporting cross-facility electrical context from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 23 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-021` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-021-02_package-datasheet` and confirm the datasheet includes package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, source-supported equipment/design criteria, and interface fact evidence.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-021` and populate the interface matrix with Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
7. Read DBM electrical source slices for facility electrical architecture, MV voltage/service, 6.9 kV transformer NGR, MV cable construction, UPS services, the 6.9 kV MCC communications pattern, electrical buildings, grounding/bonding, and cable tray/conduit routing.
8. Distinguish PKG-021 scope from PKG-036 (6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)) and do not absorb PKG-036 scope or equipment counts.
9. Search accessible package-specific requirements for PKG-021. If no source-supported package-specific match is found, mark detailed switchgear parameters (bus, breaker, short-circuit, arc-resistance, relay schemes, lineup count) as `TBD`.
10. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD` and label inferences as `ASSUMPTION`.
11. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
12. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items (including the PKG-021/PKG-036 allocation question).
13. Draft this Procedure to make the production and checking sequence repeatable.
14. Perform cross-document consistency checks for package identity, interface list (six facts), responsibility split, 6.9 kV service basis, neutral-grounding basis, and `TBD` items.
15. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
16. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 23, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All six applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Source-gap handling | Switchgear detailed parameters (bus, breaker, short-circuit, relay schemes, lineup, location) remain `TBD` unless source-supported. |
| Package boundary | PKG-021 scope is kept distinct from PKG-036 scope; equipment-list quantities are not silently allocated. |
| Human ruling items | Open items on MV switchgear quantity allocation, installation building/room, and product standards appear in the Guidance conflict table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
