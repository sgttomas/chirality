# Procedure: DEL-038-03_construction-work-package

## Purpose

Define the procedure for producing and checking the Construction Work Package for `DEL-038-03_construction-work-package`, covering construction-facing installation, tie-in, inspection, and turnover for the `PKG-038` 600V Electrical Building (workbook tag 820-1) package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 40.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM-Deepcut source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, including Electrical Buildings, Area Classification, Grounding and Bonding, Cable Wire and Raceways, building-heater, and electrical-buildings table source slices.
- Upstream Package Datasheet (`DEL-038-02`) and Scope of Work (`DEL-038-01`) drafts as technical handoff context. Note: `_DEPENDENCIES.md` does not declare these as upstream constraints; treat them as directional context only and confirm if they should be declared.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify against `DELIVERABLE_REGISTER.csv` row `DEL-038-03_construction-work-package`.
3. Read workbook Packages row 40 and record package ID, WBS, CoA tracking number, package name, discipline, and applicable interface `YES` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-038` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows `ART-9F12F8D18F`, `ART-A7B67360EB`, and `ART-C554CB9646` and confirm the deliverable provides the construction work package, the installation and tie-in workface plan, and the construction interface and turnover checklist.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-038` and populate the construction-facing interface coverage with all twelve applicable interfaces (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports).
7. Read DBM-Deepcut source slices for Electrical Buildings (prefabricated/modular, n + 1 HVAC, pile-elevated, bottom cable entry, equipment-removal doors/transoms, outdoor GFI), Area Classification (general-purpose siting), Grounding and Bonding (two-point ground-grid connection, ground wells, separate copper grounds per CEC, 600 V high-resistance grounding), Cable Wire and Raceways (TECK 90/ACWU/ACIC, HL, -40 deg C, copper-to-#1/0 then ACWU aluminum, EMT between adjacent equipment, field/shop tray routing), and the electrical-buildings table (tag 820-1 descriptor).
8. Compare the workbook descriptor for tag 820-1 ("600V ELECTRICAL BUILDING (820-1)") to the DBM electrical-buildings list descriptor ("820-1 6.9 kV Inlet / Sales Compressor Electrical Building"). Record the identity discrepancy as Conflict Table item HRR-038-03-001 and hold the building's primary voltage class/role as `TBD`.
9. Read the Package Datasheet (`DEL-038-02/Datasheet.md`) as technical handoff context when it becomes available; do not redefine package design values; carry datasheet `TBD` items forward into construction work package gaps.
10. Search accessible package-specific requirements for `PKG-038`. If no source-supported package-specific match is found, mark detailed construction parameters (exact plot location, modularization/shipping splits, lift plan, feeder/conductor/conduit detail, foundation/pile/settlement detail, building-internal equipment quantities, HVAC equipment selection, ITPs, hold points, turnover-checklist line items) as `TBD`.
11. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
12. Draft the Specification requirements and verification hooks from the Datasheet basis, the construction artifact triad, the twelve applicable interfaces, and DBM source slices.
13. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items (including the identity conflict for tag 820-1).
14. Draft this Procedure to make the production and checking sequence repeatable.
15. Perform cross-document consistency checks for package identity, artifact triad coverage, twelve-interface coverage, responsibility split, building installation basis (modular/pile-elevated/bottom-entry/n + 1 HVAC), grounding basis, cable basis, area classification, pre-issue alignment, geotechnical dependency, and `TBD` items.
16. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
17. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 40, Gate 7 registers, DBM-Deepcut source slices, or are marked `TBD` / `ASSUMPTION`. |
| Artifact triad coverage | Construction work package, installation and tie-in workface plan, and construction interface and turnover checklist are all reflected in Specification, Guidance, and Procedure. |
| Interface consistency | All twelve applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility/construction integration responsibilities are not conflated. |
| Building installation basis | Modular/prefabricated, pile-elevated, bottom cable entry, n + 1 HVAC, equipment-removal-sized doors/transoms, and outdoor GFI are recorded as construction-installation requirements. |
| Source-gap handling | Exact plot location, modularization/shipping splits, lift plan, ITPs, hold points, package-specific feeder/conductor/conduit detail, building-internal equipment quantities, HVAC equipment selection, and turnover-checklist line-item content remain `TBD` unless source-supported. |
| Geotechnical / pre-issue dependency | Foundation/pile/settlement content and pre-issue alignment to plot plan, equipment list, and construction work package register are required by Specification and addressed by Guidance and Procedure. |
| Identity conflict logged | Workbook-vs-DBM descriptor mismatch for tag 820-1 appears in the Guidance Conflict Table (HRR-038-03-001) and run record. |
| Cross-deliverable consistency | The Construction Work Package accepts the Package Datasheet (`DEL-038-02`) as technical handoff basis and supports `DEL-038-05` / `DEL-038-06` consumption. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
