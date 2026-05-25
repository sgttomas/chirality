# Procedure: DEL-035-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-035-02_package-datasheet`, covering the `PKG-035` 13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1) package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 37.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, `SCOPE_LEDGER.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Power System, System Voltages, Standby Power, Electrical Buildings, Grounding and Bonding, Cable Specifications, Cable Tray and Conduit, Area Classification, building/module list line 2811) and supporting cross-facility distribution context from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 37 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-035` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-035-02_package-datasheet` and confirm the datasheet includes package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, source-supported equipment/design criteria, and twelve interface fact evidence entries.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-035` and populate the interface matrix with all twelve applicable facts.
7. Read DBM electrical source slices for 13.8 kV switchgear function, system voltages, downstream distribution, cross-facility sub-feed to 03-25, standby power changeover, electrical building construction, grounding and bonding, cable specifications, cable tray and conduit, and the 810-1 shop-fabricated building entry.
8. Search accessible package-specific requirements for PKG-035 / 810-1. If no source-supported package-specific match is found for switchgear ratings, mark detailed bus, short-circuit, breaker, relay, and arc-flash parameters as `TBD`.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, interface list (twelve facts), responsibility split, voltage class, downstream distribution list, standby-power story, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 37, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All twelve applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Source-gap handling | Switchgear bus ampacity, short-circuit, breaker count/rating, relay scheme, arc-flash energy, plot-plan location, and in-building equipment population remain `TBD` unless source-supported. |
| Human ruling items | Identity of PKG-035 / 810-1 as the same asset as the "04-25 Main Switchgear Electrical Building" sub-feed source, and the absence of numeric switchgear ratings, appear in the Guidance Conflict Table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
