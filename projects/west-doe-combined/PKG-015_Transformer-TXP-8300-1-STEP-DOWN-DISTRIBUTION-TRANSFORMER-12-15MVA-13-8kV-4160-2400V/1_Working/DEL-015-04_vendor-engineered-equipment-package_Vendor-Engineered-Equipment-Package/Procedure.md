# Procedure: DEL-015-04_vendor-engineered-equipment-package

## Purpose

Define the procedure for producing and checking the Vendor Engineered Equipment Package for `DEL-015-04_vendor-engineered-equipment-package`, covering the `PKG-015` Transformer TXP-8300-1 step-down distribution transformer package (12/15 MVA, 13.8 kV / 4160 / 2400 V).

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- EPC anchor deliverables `DEL-015-01_scope-of-work` and `DEL-015-02_package-datasheet` for `PKG-015` (upstream EPC inputs for this vendor production unit).
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 17.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (voltage/service table, Incoming Power and Transformers, 4160V MCC, power/control separation, grounding/bonding, cable tray/conduit).
- Declared upstream dependencies: none declared during PREPARATION; vendor production unit nonetheless logically consumes `DEL-015-01` and `DEL-015-02` per Gate 7 narrative.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv` row `DEL-015-04_vendor-engineered-equipment-package`.
3. Read workbook Packages row 17 and record package ID, WBS, CoA tracking number, package name, discipline, and interface facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-015` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-015-04` and confirm the vendor production unit accounts for `ART-365325DAB5` (Vendor engineered physical equipment package) and `ART-96A2C9D72C` (Vendor package design basis and datasheet set).
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-015` and populate the interface matrix with Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
7. Read DBM electrical source slices for primary feed basis, 4160V MCC, power/control separation, grounding/bonding, cable tray/conduit, and maintenance-access constraints.
8. Cross-check the DBM "13.8 kV to 4.16 kV, 12 MVA transformer" entry against TXP-8300-1 identity; record any tag-to-feeder ambiguity as a conflict-table item (HRR-015-04-002).
9. Search accessible package-specific requirements for PKG-015. If no source-supported package-specific match is found, mark detailed transformer parameters as `TBD`.
10. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD` and label inferences as `ASSUMPTION`.
11. Draft the Specification requirements and verification hooks from the Datasheet basis, the seven `PKG-015` interface facts, and source slices.
12. Draft Guidance to explain conservative interpretation, the EPC-anchor relationship, source gaps, trade-offs, and human-ruling items.
13. Draft this Procedure to make the production and checking sequence repeatable.
14. Perform cross-document consistency checks for package identity, ratings, interface list, responsibility split, primary/secondary service basis, and `TBD` items.
15. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the items into the run record as `NEEDS_HUMAN_RULING`.
16. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 17, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All seven applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package engineering/design/equipment responsibilities and EPC facility-integration-review responsibilities are not conflated. |
| Source-gap handling | Transformer parameters not present in accessible sources (cooling, vector group, impedance, BIL, tap changer, insulating medium, 2400 V service definition, site environment, area classification, factory tests, installation location) remain `TBD`. |
| Human ruling items | Open items about 2400 V secondary service basis and DBM-to-TXP-8300-1 tag mapping appear in the Guidance conflict table and run record. |
| Artifact accounting | Both `DEL-015-04` artifacts (`ART-365325DAB5`, `ART-96A2C9D72C`) are reflected in Specification Documentation. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
