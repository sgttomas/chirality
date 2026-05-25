# Procedure: DEL-032-06_epc-vendor-package-review-and-acceptance

## Purpose

Define the procedure for producing and checking the EPC Integrator-led vendor package review and acceptance evidence for `DEL-032-06`, covering the `PKG-032` Cathodic Protection Design and Installation package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 34.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM cathodic-protection and electrical source slices: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (section "Cathodic Protection"; electrical design basis and grounding paragraphs) and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (electrical design scope and cathodic protection sentences).
- Sibling deliverables consumed as acceptance basis: `DEL-032-01` (Scope of Work), `DEL-032-02` (Package Datasheet), `DEL-032-03` (Construction Work Package), `DEL-032-04` (Vendor Engineered Equipment Package), `DEL-032-05` (Vendor Document Turnover Package).
- Declared upstream dependencies: none declared during PREPARATION; vendor submittals from `DEL-032-04` and `DEL-032-05` are functional inputs once available.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify against `DELIVERABLE_REGISTER.csv` row `DEL-032-06`.
3. Read workbook Packages row 34 and `PACKAGE_REGISTER.csv` row `PKG-032`; record package ID, WBS, CoA tracking number, discipline, responsibility model, and interface `X` facts.
4. Read `INTERFACE_REGISTER.csv` rows for `PKG-032` and seed the per-interface acceptance matrix with Electrical Power, Grounding / Bonding, I&C / Control Cabling, and Communications / Network.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-032-06` and confirm the deliverable will produce the vendor document review log, acceptance/turnover checklist, and test/inspection evidence.
6. Read the DBM cathodic-protection and electrical source slices and record the facility-design exclusion of CP engineering/supply and the facility electrical scope of supporting CP interface power.
7. Read sibling deliverable definitions (`DEL-032-01..05`) and treat their accepted scope, datasheet basis, and construction basis as the acceptance criteria against which vendor outputs are reviewed.
8. Search accessible package-specific requirements for PKG-032 (`26020-Package_Requirements.docx`). If no source-supported match is found, mark vendor-detail acceptance items as `TBD`.
9. Draft the Datasheet using source-supported identity, attributes, conditions (interfaces), and construction responsibilities; preserve unsupported vendor-detail values as `TBD`.
10. Draft the Specification requirements (REQ-032-06-001..009) and verification hooks from the Datasheet basis and source slices.
11. Draft the Guidance to explain conservative interpretation, the DBM scope split, source gaps, trade-offs, and human-ruling items (Conflict Table).
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, interface list, responsibility split, scope boundary (CP exclusion), and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry items into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 34, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All four applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration responsibilities are not conflated. |
| Scope boundary | DBM facility-design exclusion of cathodic-protection engineering and supply is preserved in acceptance language. |
| Source-gap handling | Vendor document register, vendor test plan, owner CP spec, and CP design parameters remain `TBD` unless source-supported. |
| Human ruling items | Conflict items appear in the Guidance conflict table and run record `NEEDS_HUMAN_RULING`. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
