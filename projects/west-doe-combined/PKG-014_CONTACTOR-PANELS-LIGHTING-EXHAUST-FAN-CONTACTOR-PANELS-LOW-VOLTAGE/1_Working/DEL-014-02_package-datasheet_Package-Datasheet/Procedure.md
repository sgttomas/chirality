# Procedure: DEL-014-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-014-02_package-datasheet`, covering the `PKG-014` CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 16.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Voltage Levels and Services; 208/120 V Systems and SCR Heater Controls; Electrical Buildings; Grounding and Bonding; Cable, Wire, and Raceways; Lighting and Receptacles; Area Classification forced-ventilation interlock) and supporting electrical/lighting and RDC Remote I/O context from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 16 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-014` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-014-02_package-datasheet` and confirm the datasheet includes package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, source-supported equipment/design criteria, and interface-fact evidence.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-014` and populate the interface matrix with all seven applicable interfaces: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports.
7. Read DBM electrical source slices for 208/120 V system supply, contactor-panel housing in electrical buildings, lighting and exhaust-fan loads, raceway methods, grounding and bonding, forced-ventilation interlock, and RDC Remote I/O for exhaust-fan/heater control.
8. Search accessible package-specific requirements for PKG-014. If no source-supported package-specific match is found, mark detailed panel parameters (panel count, contactor ratings, schedules, feeder sizing, per-building assignment) as `TBD`.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices, ensuring each interface fact and each load class (lighting; exhaust fans / heater blowers) is addressed.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs (especially the "LOW VOLTAGE" title vs. 208/120 V utility system interpretation), and human-ruling items.
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, the seven interface facts, responsibility split, 208/120 V supply basis, forced-ventilation interlock, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 16, Gate 7 registers, or specific DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All seven applicable interfaces appear consistently across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Source-gap handling | Panel count, contactor ratings, schedules, feeder sizing, and per-building assignment remain `TBD` unless source-supported. |
| Forced-ventilation interlock | Requirement appears wherever exhaust-fan loads are addressed. |
| Human ruling items | "LOW VOLTAGE" title interpretation, lighting/exhaust-fan physical-panel split, and exhaust-fan control I/O hosting appear in the Guidance conflict table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
