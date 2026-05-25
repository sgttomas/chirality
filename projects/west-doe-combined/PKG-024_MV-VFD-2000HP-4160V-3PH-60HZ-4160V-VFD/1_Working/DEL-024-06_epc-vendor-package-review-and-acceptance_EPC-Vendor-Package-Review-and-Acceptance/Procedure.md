# Procedure: DEL-024-06_epc-vendor-package-review-and-acceptance

## Purpose

Define the procedure for producing and checking the EPC Vendor Package Review and Acceptance deliverable for `DEL-024-06`, covering the `PKG-024` MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD package. The procedure describes how the EPC Integrator builds the review log, acceptance checklist, test/inspection evidence record, and turnover evidence, and how the cross-document consistency check is performed.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 26.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, and `SCOPE_LEDGER.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (4.16 kV MCC and electrical TBD list, electrical buildings, VFD-fed motor area marking, VFD-fed low-voltage cable type).
- For acceptance closure (later pass): issued EPC Scope of Work (`DEL-024-01`), EPC Package Datasheet (`DEL-024-02`), EPC Construction Work Package (`DEL-024-03`), Vendor Engineered Equipment Package (`DEL-024-04`), and Vendor Document Turnover Package (`DEL-024-05`).
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state (`OPEN` or `INITIALIZED`) before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify against `DELIVERABLE_REGISTER.csv` row `DEL-024-06_epc-vendor-package-review-and-acceptance`.
3. Read workbook Packages row 26 and record package ID, WBS, CoA tracking number, package name, discipline, and interface facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-024` and carry forward the responsibility model, inclusion criteria, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-024-06` and confirm the deliverable includes (a) vendor document review and comment log, (b) vendor package acceptance and turnover checklist, and (c) factory/shop test and inspection evidence.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-024` and seed the acceptance checklist with Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
7. Read DBM electrical source slices and capture conditions that constrain EPC review: 4.16 kV MCC context and electrical TBD list; electrical-building housing possibility; VFD-fed motor area marking; VFD-fed low-voltage cable type.
8. Identify the EPC anchor acceptance basis set (`DEL-024-01`, `DEL-024-02`, `DEL-024-03`). If their content is not locally consumed, record acceptance entries that depend on them as `TBD` rather than asserting acceptance.
9. Identify the vendor scope under review (`DEL-024-04`, `DEL-024-05`). The review log shall enumerate vendor submittals by row and disposition once those deliverables are populated; until then, record coverage gaps as `TBD`.
10. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
11. Draft the Specification requirements and verification hooks from the Datasheet basis, the interface register, and the DBM source slices.
12. Draft the Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items, including a Conflict Table.
13. Draft this Procedure to make the production and checking sequence repeatable.
14. Perform cross-document consistency checks for package identity, interface list, anchor-deliverable acceptance basis, responsibility split, DBM conditions, and `TBD` items.
15. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
16. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized (per skill Step 7 safe-update rule).

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 26, Gate 7 registers, DBM source slices, EPC anchor deliverables (`DEL-024-01`/`-02`/`-03`), or are marked `TBD` / `ASSUMPTION`. |
| Interface coverage | All six applicable interfaces for `PKG-024` are listed consistently across Datasheet, Specification, Guidance, and Procedure and are present as acceptance items in the checklist seed. |
| Anchor-deliverable basis | Acceptance entries cite the EPC SOW, EPC Package Datasheet, and/or EPC CWP for `PKG-024`, or are marked `TBD` pending issuance. |
| Responsibility consistency | Vendor package design/documentation responsibilities and EPC facility integration / acceptance responsibilities are not conflated. |
| Source-gap handling | Detailed VFD acceptance criteria, housing/location, Zone 2 motor marking applicability, and VFD-fed cable applicability remain `TBD` unless source-supported. |
| Human ruling items | Open ambiguity about 4.16 kV VFD requirement resolution, anchor-deliverable consumption, and PKG-024-specific package requirements content appears in the Guidance Conflict Table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
