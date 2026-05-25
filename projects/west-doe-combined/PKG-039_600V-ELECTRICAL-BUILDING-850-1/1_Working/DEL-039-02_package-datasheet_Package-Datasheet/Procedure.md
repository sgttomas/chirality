# Procedure: DEL-039-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-039-02_package-datasheet`, covering the `PKG-039` 600V ELECTRICAL BUILDING (850-1) package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 41.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, specifically: building list row 850-1; voltage and service table; 13.8 kV switchgear paragraph; Standby Power; Electrical Buildings; Grounding and Bonding; Cable, Wire, and Raceways; Lighting and Receptacles; building color table.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 41 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-039` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-039-02_package-datasheet` and confirm the datasheet covers the package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, source-supported equipment/design criteria, and the twelve interface-fact evidence rows.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-039` and populate the interface matrix with all twelve applicable interfaces.
7. Read DBM electrical source slices for: building 850-1 identity in the building-allocation table; low-voltage service basis (600 V); 13.8 kV switchgear distribution; standby power; electrical buildings (housed equipment, HVAC n + 1, bottom entry, pile elevation); grounding and bonding; cable/raceway; lighting and receptacles.
8. Search accessible package-specific requirements (e.g., `26020-Package_Requirements.docx`) for PKG-039 / building 850-1. If no source-supported package-specific match is found, mark detailed building lineup and sizing as `TBD`.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, interface list, responsibility split, voltage/service basis, building basis, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 41, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All twelve applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Source-gap handling | 600 V MCC bus rating, UPS sizing, distribution-transformer kVA, panelboard schedules, HVAC capacity, building footprint, foundation/pile design, fire-and-gas population, and exact siting remain `TBD` unless source-supported. |
| Human ruling items | Open ambiguity about internal lineup for 850-1 and absence of a package-specific source slice appear in the Guidance conflict table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
