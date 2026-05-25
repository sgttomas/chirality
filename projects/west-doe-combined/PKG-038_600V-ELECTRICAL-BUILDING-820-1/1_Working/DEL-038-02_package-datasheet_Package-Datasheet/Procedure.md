# Procedure: DEL-038-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-038-02_package-datasheet`, covering the `PKG-038` 600V ELECTRICAL BUILDING (820-1) package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 40.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, specifically: Low-voltage services table; 600 V MCC and SCR control paragraphs; Electrical Buildings section; Grounding and Bonding section; Cable Tray and Conduit section; Building Heaters section; and the electrical buildings list.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 40 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-038` and carry forward the responsibility model, applicable interfaces, source references, and supported objectives.
5. Check `ARTIFACT_REGISTER.csv` for `DEL-038-02_package-datasheet`; if no rows are present, use the anticipated artifacts in `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` as the output basis rather than inventing artifact-register entries.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-038` and populate the interface matrix with all twelve interfaces: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports.
7. Read DBM electrical source slices for low-voltage services, 600 V MCC and SCR, Electrical Buildings (construction, HVAC, cable entry, internal wiring), Grounding and Bonding, Cable Tray and Conduit, Building Heaters, and the electrical buildings list.
8. Search the accessible package-specific requirements source for PKG-038 content. If no source-supported PKG-038 slice is found, mark package-specific equipment counts, ratings, layout, HVAC sizing, and UPS battery autonomy as `TBD`.
9. Compare the workbook package name and the DBM electrical-buildings list for building identifier 820-1; if they disagree, preserve the workbook name as identity and create or update the Guidance Conflict Table.
10. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
11. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
12. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
13. Draft this Procedure to make the production and checking sequence repeatable.
14. Perform cross-document consistency checks for package identity, full interface list, responsibility split, 600 V service / MCC basis, grounding basis, HVAC basis, and `TBD` items.
15. If source disagreement or unsupported ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
16. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 40, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All twelve applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Source-gap handling | PKG-038-specific equipment quantities, ratings, layout, HVAC sizing, and UPS battery autonomy remain `TBD` unless source-supported. |
| Human ruling items | The 820-1 building-identifier conflict and the missing PKG-038-specific requirements source appear in the Guidance Conflict Table and in the run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
