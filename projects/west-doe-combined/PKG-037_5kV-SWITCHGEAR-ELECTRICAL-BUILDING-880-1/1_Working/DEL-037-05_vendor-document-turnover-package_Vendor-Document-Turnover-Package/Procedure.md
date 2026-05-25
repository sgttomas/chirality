# Procedure: DEL-037-05_vendor-document-turnover-package

## Purpose

Define the procedure for producing and checking the Vendor Document Turnover Package for `DEL-037-05_vendor-document-turnover-package`, covering the `PKG-037` 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1) package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 39.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Package requirements source slice: `_Sources/26020-Package_Requirements.docx`, Core vendor documents table (`PRQ-009` Vendor Document Index; `DOC-008` Vendor Document Control Procedure).
- DBM source slices: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical package deliverables paragraph (line 617); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph and MV cable table (line 3009).
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv` row `DEL-037-05_vendor-document-turnover-package`.
3. Read workbook Packages row 39 and record package ID, WBS, CoA tracking number, package name (preserving "(880-1)"), discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-037` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-037-05` and confirm the deliverable carries the vendor document register, submittals, turnover records, and source-set gap evidence (`ART-8E3FB7B466`).
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-037` and confirm the vendor documentation must address each of the twelve applicable interfaces where vendor scope crosses them.
7. Read DBM source slices for package-deliverable basis (vendor document registers) and 5 kV insulation-class basis.
8. Read `26020-Package_Requirements.docx` for core vendor-document entries and preserve `PRQ-009` Vendor Document Index and `DOC-008` Vendor Document Control Procedure. If no source-supported package-specific match is found, mark detailed register schema, hold/issue codes, submittal stages, and turnover acceptance criteria as `TBD`.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices, including the explicit scope boundary against `DEL-037-06_epc-vendor-package-review-and-acceptance`.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, interface list, responsibility split, 5 kV interpretation, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 39, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All twelve applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor documentation production and EPC interface/integration review are not conflated; EPC acceptance is routed to `DEL-037-06`. |
| Source-gap handling | Core `PRQ-009` / `DOC-008` entries are preserved; package-specific vendor document register schema, hold/issue codes, submittal stages, and turnover acceptance criteria remain `TBD` unless source-supported. |
| Human ruling items | Open ambiguity about 5 kV meaning and missing vendor document register schema appears in the Guidance Conflict Table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
