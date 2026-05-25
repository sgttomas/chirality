# Procedure: DEL-025-03_construction-work-package

## Purpose

Define the procedure for producing and checking the Construction Work Package for `DEL-025-03_construction-work-package`, covering construction-facing installation, tie-in, inspection, and turnover for the `PKG-025` "MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD" package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 27.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM construction and electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, including construction scope summary, civil/infrastructure, MV services table, 6.9 kV MCC paragraph, electrical buildings, grounding (including the 100 A 10 s NGR rule for 6.9 kV transformers), cable tray, conduit, MV cable (TECK 8 kV), VFD-fed cable, area classification (including Zone 2 VFD-fed motor marking), remote I/O network, geotechnical, and issue-for-construction paragraphs.
- Upstream Package Datasheet (`DEL-025-02`) and Scope of Work (`DEL-025-01`) drafts as technical handoff context. Note: `_DEPENDENCIES.md` does not declare these as upstream constraints; treat them as directional context only and confirm if they should be declared.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify against `DELIVERABLE_REGISTER.csv` row `DEL-025-03_construction-work-package`.
3. Read workbook Packages row 27 and record package ID, WBS, CoA tracking number, package name, discipline, and applicable interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-025` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows `ART-15E3B51A2A`, `ART-26C6F26015`, and `ART-F23C60D66E` and confirm the deliverable provides the construction work package, the installation and tie-in workface plan, and the construction interface and turnover checklist.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-025` and populate the construction-facing interface coverage with Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
7. Read DBM source slices for construction scope, civil/infrastructure, MV services, 6.9 kV MCC, electrical buildings, grounding and bonding, cable tray and conduit routing, MV cable and VFD-fed cable types, area classification (including Zone 2 VFD-fed motor marking), remote I/O network, geotechnical, and issue-for-construction alignment.
8. Read the Package Datasheet (`DEL-025-02/Datasheet.md`) as technical handoff context. Do not redefine package design values; carry datasheet `TBD` items forward into construction work package gaps.
9. Search accessible package-specific requirements for `PKG-025`. If no source-supported package-specific match is found, mark detailed construction parameters (installation location/building assignment, modularization, lift plan, feeder/conductor/conduit detail, foundation/support detail, control schematics, network port and PRP/DLR assignments, ITPs, hold points, MV pre-energization tests, turnover-checklist line items) as `TBD`.
10. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
11. Draft the Specification requirements and verification hooks from the Datasheet basis, the construction artifact triad, and DBM source slices, including MV-specific cable type, grounding/NGR, and area-classification rules.
12. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items, including the "5000HP" vs DBM 5,500 hp / KM-2150/2250 ambiguity.
13. Draft this Procedure to make the production and checking sequence repeatable.
14. Perform cross-document consistency checks for package identity, artifact triad coverage, six-interface list, responsibility split, MV service basis, pre-issue alignment, geotechnical dependency, controls/network tie-in, and `TBD` items.
15. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
16. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 27, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Artifact triad coverage | Construction work package, installation and tie-in workface plan, and construction interface and turnover checklist are all reflected in Specification, Guidance, and Procedure. |
| Interface consistency | All six applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility/construction integration responsibilities are not conflated. |
| Source-gap handling | Installation location/building assignment, modularization, lift plan, MV pre-energization tests, ITPs, hold points, package-specific feeder/conductor/conduit detail, controls/network port assignments, and turnover-checklist content remain `TBD` unless source-supported. |
| Geotechnical / pre-issue dependency | Foundation/support content and pre-issue alignment to plot plan, equipment list, and construction work package register are required by Specification and addressed by Guidance and Procedure. |
| Cross-deliverable consistency | The Construction Work Package accepts the Package Datasheet (`DEL-025-02`) as technical handoff basis and supports `DEL-025-05` / `DEL-025-06` consumption. |
| Human ruling items | Open ambiguity about "5000HP" / KM-2150/2250 allocation, installation location, pre-issue input availability, and controls/network tie-in detail appears in the Guidance Conflict Table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
