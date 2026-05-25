# Procedure: DEL-029-04_vendor-engineered-equipment-package

## Purpose

Define the procedure for producing, integrating, and checking the Vendor Engineered Equipment Package for `DEL-029-04_vendor-engineered-equipment-package`, covering the `PKG-029` Transformer TXP-8600-1 (2.5 MVA, 13.8 kV / 600 / 347 V step-down distribution transformer).

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 31.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv` / `OBJECTIVE_SCOPE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (distribution transformer, grounding, foundations, cable, standby power) and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` ("Incoming Power and Transformers"; "600V MCC and Standby Power").
- EPC-authored Package Datasheet and Scope of Work (`DEL-029-02` / `DEL-029-01`) when issued; this vendor production unit consumes those EPC artifacts as integration inputs.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 31 and record package ID, WBS, CoA tracking number, package name, equipment tag (TXP-8600-1), rating (2.5 MVA, 13.8 kV / 600 / 347 V), discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-029` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-029-04_vendor-engineered-equipment-package` and confirm the vendor production unit covers both `ART-D86EE0EF6E` (vendor engineered physical equipment package) and `ART-F831FA81A1` (vendor package design basis and datasheet set).
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-029` and populate the interface response matrix with Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
7. Read DBM electrical source slices for distribution transformer service to 600 V MCCs, secondary high-resistance grounding (5 A continuous), foundations and spacing for large transformers, secondary cable type (ACWU; no single-conductor), and 600 V MCC standby power scheme.
8. Search accessible package-specific requirements for PKG-029 / TXP-8600-1 in `_Sources/26020-Package_Requirements.docx`. If no confirmed match is accessible, mark insulation, cooling, impedance, tap-changer, accessory, allocation, and location parameters as `TBD`.
9. Vendor engineering: produce vendor design basis, electrical schematic, protection scheme, general arrangement, nameplate data, factory test plan, and installation/commissioning data consistent with workbook identity and DBM facility basis.
10. Vendor design: select insulation type, cooling class, impedance, tap-changer, bushings, and accessories; record selections with explicit source/justification; raise TBDs that require EPC ruling.
11. Vendor fabrication/supply: fabricate, factory-test, and supply the physical transformer package; produce factory test certificate and turnover documentation.
12. EPC integration review: confirm the vendor package supports the seven applicable interfaces, the 600 V HRG neutral grounding scheme, ACWU secondary feeder cable, foundations/containment/spacing per CEC, and ground-grid two-point connection.
13. Perform cross-document consistency checks for package identity, tag, ratings, interface list, responsibility split, grounding scheme, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 31, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Identity consistency | TXP-8600-1, 2.5 MVA, 13.8 kV primary, and 600/347 V secondary appear consistently across the four documents. |
| Interface consistency | All seven applicable interface facts are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package responsibilities (engineering/design/documentation/equipment) and EPC integration responsibilities are not conflated. |
| Source-gap handling | Insulation, cooling, impedance, tap-changer, facility allocation, and installation location remain `TBD` unless source-supported. |
| Human ruling items | Open items HRR-029-04-001 through HRR-029-04-003 appear in the Guidance conflict table and in the run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
