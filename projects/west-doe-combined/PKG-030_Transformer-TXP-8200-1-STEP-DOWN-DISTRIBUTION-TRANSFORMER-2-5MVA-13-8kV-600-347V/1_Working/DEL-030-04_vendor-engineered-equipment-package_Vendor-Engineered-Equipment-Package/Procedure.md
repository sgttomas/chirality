# Procedure: DEL-030-04_vendor-engineered-equipment-package

## Purpose

Define the procedure for producing and checking the Vendor Engineered Equipment Package for `DEL-030-04_vendor-engineered-equipment-package`, covering the `PKG-030` "Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V" package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Upstream EPC deliverables for vendor execution: `DEL-030-01` (Scope of Work) and `DEL-030-02` (Package Datasheet).
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 32.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (electrical voltages and services, transformers, grounding/bonding, cable types, electrical buildings, structural/foundations) and supporting context from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` where 03-25 integration is relevant.
- Declared upstream/downstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv` row `DEL-030-04`.
3. Read workbook Packages row 32 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-030` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-030-04_vendor-engineered-equipment-package` (`ART-69E26F40CD`, `ART-0A27405282`) and confirm the vendor package scope includes the vendor engineered physical equipment package and the vendor package design basis and datasheet set.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-030` and confirm all seven interfaces are coordinated (Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports).
7. Read DBM electrical source slices that ground vendor-facing requirements: voltage and grounding basis, transformer spacing/containment, cable basis (15 kV TECK primary; ACWU 600 V secondary), maintenance access constraints, and structural/foundation basis.
8. Search accessible package-specific requirements for `PKG-030`. If no source-supported package-specific match is found in `_Sources/26020-Package_Requirements.docx`, mark detailed transformer parameters as `TBD` and require EPC Package Datasheet (`DEL-030-02`) to supply them.
9. Draft the Datasheet using source-supported facility basis values and Gate 7 register data only; preserve unsupported package-specific values as `TBD`.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs (oil-filled vs. dry-type, 4-wire 600/347 V provisioning), and human-ruling items.
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, the seven interface facts, responsibility split, primary/secondary voltage basis, grounding basis, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite Workbook Packages row 32, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All seven applicable `PKG-030` interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package engineering/design/fabrication/supply/physical scope and EPC facility integration/integration review scope are not conflated. |
| Source-gap handling | Detailed transformer parameters (impedance, BIL, taps, cooling, oil type, secondary 4-wire/347 V provisioning, signal list, area classification, installation location, quantity) remain `TBD` unless source-supported. |
| Human ruling items | Open ambiguity about 4-wire 600/347 V provisioning, quantity allocation, and missing `_Sources/26020-Package_Requirements.docx` `PKG-030` match appears in the Guidance conflict table and the run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
