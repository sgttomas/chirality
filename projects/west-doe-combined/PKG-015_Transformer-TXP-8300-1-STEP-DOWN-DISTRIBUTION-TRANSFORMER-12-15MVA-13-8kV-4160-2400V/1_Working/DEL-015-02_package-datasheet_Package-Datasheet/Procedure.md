# Procedure: DEL-015-02_package-datasheet

## Purpose

Define the procedure for producing and checking the Package Datasheet for `DEL-015-02_package-datasheet`, covering the `PKG-015` "Transformer TXP-8300-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 12/15MVA 13.8kV/4160/2400V" package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 17.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Basis (System Voltages, Incoming Power and Transformers, 4160V MCC, Electrical Buildings/Raceways), Area Classification, Foundations, and Buildings sections.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 17 and record package ID, WBS, CoA tracking number, package name, equipment tag (TXP-8300-1), discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-015` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-015-02_package-datasheet` and confirm the datasheet includes package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, source-supported equipment/design criteria, and interface fact evidence.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-015` and populate the interface matrix with all seven applicable interface facts (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports).
7. Read DBM electrical source slices for system voltages, incoming power and transformers, 4160V MCC loads, raceway separation, area classification, and foundations.
8. Reconcile the package-title rating "12/15 MVA" against the DBM "12 MVA" entry: record 12 MVA as source-confirmed; carry 15 MVA FA as `ASSUMPTION`.
9. Reconcile the package-title secondary "4160/2400 V" against the DBM "4.16 kV" entry: record 4.16 kV as source-confirmed; carry 2400 V tertiary as `ASSUMPTION`.
10. Search accessible package-specific requirements for PKG-015 in `26020-Package_Requirements.docx`. If no source-supported package-specific match is found, mark detailed transformer parameters (cooling class, BIL, vector group, impedance, taps, NGR, bushings, conservator, OLTC) as `TBD`.
11. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD` or `ASSUMPTION`.
12. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
13. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
14. Draft this Procedure to make the production and checking sequence repeatable.
15. Perform cross-document consistency checks for package identity, interface list (all seven), responsibility split, primary/secondary voltages, rating handling, and `TBD`/`ASSUMPTION` items.
16. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
17. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 17, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All seven applicable interfaces and their `IFC-*` IDs are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Rating/voltage handling | 12 MVA / 4.16 kV are cited from the DBM; 15 MVA FA and 2400 V tertiary are marked `ASSUMPTION`. |
| Source-gap handling | Transformer detailed parameters remain `TBD` unless source-supported. |
| Human ruling items | Open ambiguity about rating, tertiary voltage, and detailed parameter source gaps appears in the Guidance conflict table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
