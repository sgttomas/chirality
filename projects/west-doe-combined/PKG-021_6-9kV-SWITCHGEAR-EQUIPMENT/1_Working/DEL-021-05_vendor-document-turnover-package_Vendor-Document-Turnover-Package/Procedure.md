# Procedure: DEL-021-05_vendor-document-turnover-package

## Purpose

Define the procedure for producing and checking the Vendor Document Turnover Package for `DEL-021-05_vendor-document-turnover-package`, covering the `PKG-021` 6.9kV SWITCHGEAR EQUIPMENT package. The procedure covers both production of this deliverable's evidence record by the EPC Integrator (this run) and the operating sequence by which the Package Vendor assembles, and the EPC Integrator reviews, the vendor documentation set.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 23.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (medium-voltage services, 6.9 kV MCC, electrical buildings, grounding, cable tray/maintenance) and the mechanical-packages paragraph in `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Declared upstream dependencies: none declared during PREPARATION.
- Declared downstream dependencies: none declared during PREPARATION; functional downstream consumer is `DEL-021-06_epc-vendor-package-review-and-acceptance`.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv` row `DEL-021-05_vendor-document-turnover-package`.
3. Read workbook Packages row 23 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-021` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-021-05` and adjacent `DEL-021-06` rows; confirm boundary (this deliverable owns the vendor documentation set; `DEL-021-06` owns review/acceptance/turnover-checklist artifacts).
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-021` and populate the interface matrix with Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
7. Read DBM electrical source slices for medium-voltage service basis, 6.9 kV MCC Ethernet practice (analogous), electrical buildings (including the 6.9 kV Inlet/Sales Compressor Electrical Building), grounding (100 A, 10 s neutral grounding resistor for each 6.9 kV transformer), cable tray, and maintenance access.
8. Read the Comp and Liquids DBM mechanical-packages paragraph to capture the analogous expectation that package deliverables include a vendor document register; treat as directional context for an electrical package.
9. Search accessible package-specific requirements for `PKG-021`. If no source-supported package-specific match is found (as is the case in this run), record the vendor-document register content and project-wide register format as `TBD`.
10. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
11. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices, expressing each interface coverage requirement and each gap explicitly.
12. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, the boundary with `DEL-021-06`, and human-ruling items.
13. Draft this Procedure to make the production and checking sequence repeatable.
14. Perform cross-document consistency checks for package identity, interface list, responsibility split, register treatment, and `TBD` items.
15. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
16. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

### Operational steps the Package Vendor and EPC Integrator follow (described, not executed here)

A. Package Vendor proposes a vendor document register listing every vendor document for `PKG-021` (number, title, revision, status, submittal stage, intended use).
B. EPC Integrator reviews the register for completeness against the six interface coverage targets and facility integration needs; gaps flagged as `TBD` until resolved.
C. Package Vendor submits documents per the register, in stages (ASSUMPTION: for review / for approval / certified / as-built/turnover until a project-wide standard supersedes this).
D. EPC Integrator records comments in the vendor document review and comment log (`ART-5D5CAC1D6D`, owned by `DEL-021-06`).
E. Package Vendor revises and resubmits until documents are accepted.
F. Final accepted documents are consolidated into the turnover package; cross-references to the acceptance and turnover checklists (`ART-4B01C09131`) and to factory/shop test and inspection evidence (`ART-E523401B0C`) are recorded.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 23, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface coverage | All six applicable interfaces appear in the Datasheet, Specification requirements, Guidance principles, and Procedure steps. |
| Responsibility consistency | Package Vendor (vendor documentation) and EPC Integrator (review/integration) responsibilities are not conflated. |
| Deliverable boundary | The `DEL-021-05` vs `DEL-021-06` boundary is preserved; `DEL-021-06` artifacts are referenced, not duplicated. |
| Source-gap handling | Vendor document register content, register format/numbering, transmittal gating, and detailed test/inspection requirements remain `TBD` unless source-supported. |
| Human ruling items | HRR-021-05-001/002/003 appear in the Guidance conflict table and in the run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
