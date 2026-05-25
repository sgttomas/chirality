# Procedure: DEL-034-06_epc-vendor-package-review-and-acceptance

## Purpose

Define the procedure for producing and checking the EPC Vendor Package Review and Acceptance deliverable for `DEL-034-06_epc-vendor-package-review-and-acceptance`, covering the `PKG-034` 600V ELECTRICAL BUILDING (820-2) vendor package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 36.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Upstream EPC anchor deliverables: EPC Scope of Work (`DEL-034-01`); EPC Package Datasheet (`DEL-034-02`); EPC Construction Work Package (`DEL-034-03`).
- Vendor inputs: Vendor Engineered Equipment Package (`DEL-034-04`); Vendor Document Turnover Package (`DEL-034-05`).
- DBM electrical source slices from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv` row `DEL-034-06`.
3. Read workbook Packages row 36 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-034` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `DELIVERABLE_REGISTER.csv` rows `DEL-034-01` through `DEL-034-06` to establish the EPC anchor deliverables and vendor input deliverables.
6. Read `ARTIFACT_REGISTER.csv` rows for `DEL-034-06` and confirm the deliverable plans for the vendor document review and comment log (`ART-F631454830`), the vendor package acceptance and turnover checklist (`ART-8E586DD59F`), and factory/shop test and inspection evidence (`ART-853E05D6CB`).
7. Read `INTERFACE_REGISTER.csv` rows for `PKG-034` and confirm all twelve interface facts are mapped into the acceptance checklist.
8. Read DBM electrical source slices for low-voltage 600 V service, 600V MCC and standby power, electrical-building HVAC, area classification, foundations, grounding/bonding, cable tray, conduit, and maintenance access.
9. Search accessible package-specific requirements for `PKG-034`. If no source-supported match is found in `26020-Package_Requirements.docx`, record the gap and mark package-specific acceptance criteria as `TBD`.
10. Reconcile workbook building label "820-2" against the DBM Deepcut electrical-buildings inventory. If no source-supported mapping exists, record `HRR-034-06-001` and do not silently map.
11. Draft the Datasheet using source-supported values; preserve unsupported values as `TBD` and cite Gate 7 registers, workbook row 36, and DBM slices.
12. Draft the Specification with requirements anchored to the EPC Scope of Work, Package Datasheet, Construction Work Package, vendor inputs, and the twelve interface facts; mark unresolved items `TBD`.
13. Draft the Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
14. Draft this Procedure to make the production and checking sequence repeatable.
15. Perform cross-document consistency checks for package identity, anchor deliverable list, interface list, responsibility split, 600V service basis, standby power treatment, and `TBD` items.
16. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
17. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 36, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Anchor traceability | Every Specification requirement references the EPC Scope of Work, Package Datasheet, Construction Work Package, vendor input, register row, or DBM slice basis. |
| Interface consistency | All twelve applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration/acceptance responsibilities are not conflated. |
| Source-gap handling | Building "820-2" location reconciliation, standby power generator details, and vendor document register gaps remain `TBD` unless source-supported. |
| Human ruling items | Open items appear in the Guidance Conflict Table and in the run record `NEEDS_HUMAN_RULING` section. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
