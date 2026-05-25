# Procedure: DEL-023-05_vendor-document-turnover-package

## Purpose

Define the procedure for producing, populating, and checking the Vendor Document Turnover Package for `DEL-023-05_vendor-document-turnover-package`, covering the `PKG-023` MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD package. The procedure governs both the production of the deliverable's structure (register/transmittal/turnover shell) and the EPC interface/integration review of vendor-submitted documents.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 25.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv` (including row `ART-950E899C01`), `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (electrical voltage/service table; 4.16 kV MCC paragraph; electrical buildings paragraph; VFD/area-classification paragraph).
- Declared upstream dependencies: none declared during PREPARATION (`_DEPENDENCIES.md`).
- Companion deliverables: `DEL-023-04_vendor-engineered-equipment-package` (vendor-authored package content) and `DEL-023-06_epc-vendor-package-review-and-acceptance` (EPC review/acceptance evidence).

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv` row `DEL-023-05_vendor-document-turnover-package`.
3. Read workbook Packages row 25 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-023` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` row `ART-950E899C01` and explicitly carry the "TBD vendor document register / Vendor Documentation Gap Evidence" status into the deliverable rather than inventing register contents.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-023` and ensure the vendor document register scope covers evidence for all six applicable interfaces (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports).
7. Read DBM electrical source slices for MV VFD voltage service basis (4.16 kV), electrical-building eligibility, MV MCC PLC integration convention (treat MV VFD applicability as ASSUMPTION), and VFD-fed motor area-classification marking.
8. Search accessible package-specific requirements for PKG-023 vendor documentation. If no source-supported package-specific match is found, mark detailed vendor-document register rows, submittal numbering, and turnover record list as `TBD`.
9. Draft the Datasheet identity/attributes/conditions/construction using source-supported values only; preserve unsupported values as `TBD`.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices, including REQ-023-05-001 through REQ-023-05-009.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, MV VFD voltage-class context, and human-ruling items.
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Establish the vendor document register shell (register file or table), the submittal transmittal log shell, and the turnover record list shell within the deliverable folder (content remains `TBD`; structure is in place).
14. On receipt of vendor submittals, log each in the transmittal log with revision, date, and EPC disposition pointer; route to the EPC Integrator for interface/integration review under `DEL-023-06`.
15. Perform cross-document consistency checks for package identity, interface list, responsibility split, voltage-class context, and `TBD` items.
16. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
17. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 25, Gate 7 registers (including `ART-950E899C01`), DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All six applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor documentation authorship and EPC integration review are not conflated. |
| Source-gap handling | Vendor document register rows, submittal numbering, and turnover record list remain `TBD` unless source-supported. |
| Human ruling items | HRR-023-05-001 (register-content gap), HRR-023-05-002 (MV VFD PLC integration ASSUMPTION), and HRR-023-05-003 (area classification TBD) appear in the Guidance Conflict Table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- Vendor document register (shell; content `TBD`).
- Vendor document submittal transmittal log (shell; content populated on receipt).
- Turnover record list (shell; content `TBD`).
- `_STATUS.md` state history.
- `_run_records/TASK_RUN_*.md`.
