# Procedure: DEL-030-05_vendor-document-turnover-package

## Purpose

Define the procedure for producing, transmitting, reviewing, and accepting the Vendor Document Turnover Package for `DEL-030-05_vendor-document-turnover-package`, covering the `PKG-030` Transformer TXP-8200-1 (2.5 MVA, 13.8 kV / 600/347 V step-down distribution transformer).

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 32.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM source slices: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (mechanical-package deliverable menu, electrical distribution table, document-support artifact register) and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (cable tray/conduit and grounding/bonding context).
- Vendor scope of supply for the transformer package (to be issued; otherwise the register schema is defined and entries remain `TBD`).
- Project document-control / submittal standard (location TBD).
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv` row `DEL-030-05_vendor-document-turnover-package`.
3. Read workbook Packages row 32 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-030` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-030-05` and record the documented vendor-documentation gap (`ART-8B1CB2D887`).
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-030` and populate the interface evidence matrix (Electrical Power, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Communications/Network, Maintenance Access, Structural/Foundations/Supports).
7. Read DBM source slices for mechanical-package deliverable basis (line 617), electrical distribution context (line 745), document-support artifact register (line 3438+), and cable tray/conduit/grounding context.
8. Define the Vendor Document Register schema (document number, title, type, revision, submittal status, transmittal reference, EPC review status, disposition). Leave entries `TBD` where the vendor scope of supply is not yet confirmed.
9. Define the Submittal Log schema (transmittal number, date, revision, documents transmitted, EPC reviewer, disposition, response date).
10. Define the Turnover Record schema (factory acceptance test evidence, field acceptance test evidence, name-plate documentation, as-built / red-line records, acceptance signatures). Leave entries `TBD` where the vendor scope is not yet confirmed.
11. As vendor documents are received, populate the register, attach the submittal transmittals, and record EPC Integrator review dispositions. Re-issue revisions and track close-out.
12. Cross-link interface evidence: ensure each of the seven applicable interface facts is supported by at least one vendor document reference, or is explicitly carried as `TBD` with reason.
13. Hand off the completed turnover record to `DEL-030-06_epc-vendor-package-review-and-acceptance` as upstream evidence for acceptance.
14. Perform cross-document consistency checks for package identity, interface list, responsibility split, and `TBD` items across Datasheet, Specification, Guidance, and Procedure.
15. If source disagreement or unsupported ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
16. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 32, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All seven applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Package Vendor documentation authorship and EPC Integrator integration review are not conflated. |
| Register / submittal / turnover schemas | Register, submittal log, and turnover record schemas exist and are populated or `TBD` per the source-gap rule. |
| Handoff readiness | The turnover record is structured to feed `DEL-030-06` as upstream evidence. |
| Human ruling items | Open ambiguity about vendor-document enumeration, applicable transformer standards, and the `DEL-030-04 / DEL-030-05` authorship boundary appears in the Guidance Conflict Table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
- Vendor Document Register (when populated by vendor scope of supply)
- Submittal Log (when transmittals occur)
- Turnover Records (at acceptance)
