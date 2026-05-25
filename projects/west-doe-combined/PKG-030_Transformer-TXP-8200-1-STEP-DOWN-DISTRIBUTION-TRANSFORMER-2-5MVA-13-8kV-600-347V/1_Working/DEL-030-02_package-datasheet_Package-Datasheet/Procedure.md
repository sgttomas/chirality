# Procedure: DEL-030-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-030-02_package-datasheet`, covering the `PKG-030` Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 32.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (System Voltages, Transformers, Standby Power, Electrical Buildings, Grounding, Cable schedule, Foundations).
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 32 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-030` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-030-02_package-datasheet` and confirm the datasheet covers package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, source-supported equipment/design criteria, and the seven interface fact evidences.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-030` and populate the interface matrix with Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
7. Read DBM-Deepcut electrical source slices: System Voltages (13.8 kV primary, 600 V LV service), Transformers paragraph (CEC spacing, oil-filled vs. dry-type framing, containment review), Foundations table (precast concrete bearing foundations / structural-steel transformer bases), grounding paragraphs (two-point ground grid, ground wells at power transformers, separate copper ground conductor per CEC, 5 A HRG on 600 V secondary, alarm-only 600 V ground-fault), and the cable schedule (ACWU for 600 V transformer secondary to 600 V MCCs, single-conductor avoided).
8. Search accessible package-specific requirements for PKG-030 in `26020-Package_Requirements.docx`. If no source-supported package-specific match is found, mark detailed nameplate, construction-type, location, containment, cable, and protection parameters as `TBD`.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`; flag the 347 V leg as `ASSUMPTION` (industry-standard 600/347 V wye interpretation).
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, interface list, responsibility split, primary/secondary voltages, grounding scheme, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 32, Gate 7 registers, DBM-Deepcut source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All seven applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Source-gap handling | Transformer nameplate parameters, construction type, location, containment, cable schedule, and protection settings remain `TBD` unless source-supported. |
| Human ruling items | 347 V interpretation, construction-type assignment, and installation-location items appear in the Guidance conflict table and the run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
