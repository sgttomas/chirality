# Procedure: DEL-027-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-027-02_package-datasheet`, covering the `PKG-027` Transformer TXP-8301-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 29.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (voltage and service table, 6.9 kV Inlet/Sales Compressor Electrical Building, 6.9 kV MCC, transformer installation and foundations, secondary containment, grounding resistors, ground grid and bonding, MV cable basis, cable tray and conduit) and supporting context from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 29 and record package ID, WBS, CoA tracking number, package name (preserving the "TXP-8301-1" tag and "13.8kV/6.9kV/0.4kV" voltage list verbatim), discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-027` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-027-02_package-datasheet` and confirm the datasheet includes package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, and interface-fact evidence rows for all seven applicable interfaces.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-027` and populate the interface matrix with Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
7. Read DBM electrical source slices for: 13.8 kV and 6.9 kV service basis; 6.9 kV Inlet/Sales Compressor Electrical Building and 6.9 kV MCC service; transformer installation and foundations; secondary containment; 6.9 kV neutral grounding resistor; facility ground grid two-point connection and ground well at power transformers; distribution-transformer separate copper ground conductor sized per CEC; MV cable basis at 13.8 kV (15 kV TECK, 133%) and 6.9 kV (8 kV TECK, 100%); cable tray and conduit routing constraints.
8. Search accessible package-specific requirements for PKG-027 in `26020-Package_Requirements.docx`. If no source-supported package-specific match has been copied into the deliverable folder, mark transformer-specific parameters (impedance, BIL, vector group, taps, sound level, temperature rise, insulating medium, accessories, cooling-stage interpretation, foundation design, installation location) as `TBD`.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD` and label inferences as `ASSUMPTION`.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices, including the binding 6.9 kV neutral grounding requirement and the MV cable basis.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items (notably the 0.4 kV interpretation, insulating-medium allocation, cooling-stage interpretation, and missing package-specific requirements source).
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity (including TXP-8301-1 tag and 20/26 MVA dual rating), interface list (seven interfaces), responsibility split, voltage basis, grounding scheme, MV cable basis, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 29, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All seven applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Voltage basis | 13.8 kV primary and 6.9 kV secondary characteristics match the DBM electrical service table; 0.4 kV is carried as identity-level metadata with service basis `TBD`. |
| Grounding scheme | 6.9 kV secondary neutral grounded via 100 A, 10 s NGR (tripping) language matches DBM. |
| MV cable basis | Primary and secondary MV cable specifications match the DBM MV cable table. |
| Source-gap handling | Transformer-specific impedance, BIL, vector group, taps, sound level, temperature rise, insulating medium, accessories, cooling-stage interpretation, foundation design, and installation location remain `TBD` unless source-supported. |
| Human ruling items | 0.4 kV interpretation, insulating-medium allocation, cooling-stage interpretation, and missing `26020-Package_Requirements.docx` slices appear in the Guidance Conflict Table and the run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
