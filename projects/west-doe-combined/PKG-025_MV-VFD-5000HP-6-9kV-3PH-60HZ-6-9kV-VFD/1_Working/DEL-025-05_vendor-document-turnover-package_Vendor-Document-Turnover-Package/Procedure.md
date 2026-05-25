# Procedure: DEL-025-05_vendor-document-turnover-package

## Purpose

Define the procedure for producing and checking the Vendor Document Turnover Package for `DEL-025-05_vendor-document-turnover-package`, covering the `PKG-025` MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD package, including the EPC Integrator interface/integration review pathway.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 27.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM source slices: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (mechanical packages organisation paragraph) and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Deepcut electrical design basis).
- Sibling deliverables for cross-traceability: `DEL-025-01` (EPC Scope of Work), `DEL-025-02` (Package Datasheet), `DEL-025-03` (Construction Work Package), `DEL-025-04` (Vendor Engineered Equipment Package), and `DEL-025-06` (EPC Vendor Package Review and Acceptance).
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv` row `DEL-025-05`.
3. Read workbook Packages row 27 and record package ID, WBS, CoA tracking number, package name, discipline, and applicable interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-025` and carry forward the responsibility model, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-025-05` and note the `ART-5D23A5F2CB` vendor documentation gap as evidence to be preserved.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-025` and populate the interface coverage list with Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
7. Read `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-025-05` and carry the supported objectives (`OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010`) as context.
8. Read the DBM mechanical packages organisation paragraph and extract the vendor-document content category checklist.
9. Search accessible package-specific requirements for `PKG-025`. If no source-supported package-specific match is found in `_Sources/26020-Package_Requirements.docx`, mark detailed register and turnover content as `TBD`.
10. Draft the vendor document register schema with the minimum useful field set; label any extensions as `ASSUMPTION` pending the project document-control standard.
11. Map the vendor document register to the DBM content category checklist; mark categories that are not applicable to a 6.9 kV MV VFD package as N/A with reason; mark required Electrical-specific items not enumerated by accessible source as `TBD`.
12. Define the vendor document submittal channel and its alignment to the EPC anchor deliverables (`DEL-025-01`, `DEL-025-02`, `DEL-025-03`) and downstream review (`DEL-025-06`).
13. Define the turnover record set placeholder; mark detailed types (FAT/SAT, certifications, calibrations, spare parts, training, as-builts) as `TBD` pending the project turnover standard.
14. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
15. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
16. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
17. Draft this Procedure so that production and checking are repeatable.
18. Perform cross-document consistency checks for package identity, interface list, responsibility split, register schema, turnover record placeholder, and `TBD` items.
19. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the items into the run record as `NEEDS_HUMAN_RULING`.
20. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 27, Gate 7 registers, the DBM mechanical packages organisation paragraph, or the DBM Deepcut electrical design basis, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All six `PKG-025` applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Package Vendor (vendor documentation) and EPC Integrator (interface/integration review) responsibilities are not conflated. |
| Artifact-class coverage | Vendor document register, submittals, source-vendor-document artifacts, and turnover records are all addressed (present or marked N/A with reason). |
| Source-gap handling | Detailed register schedule, turnover record set, and per-document content remain `TBD` unless source-supported. |
| Human ruling items | Open ambiguity about applicability of DBM mechanical content categories to an Electrical VFD package, and the vendor-document/turnover gap recorded by `ART-5D23A5F2CB`, appear in the Guidance Conflict Table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
