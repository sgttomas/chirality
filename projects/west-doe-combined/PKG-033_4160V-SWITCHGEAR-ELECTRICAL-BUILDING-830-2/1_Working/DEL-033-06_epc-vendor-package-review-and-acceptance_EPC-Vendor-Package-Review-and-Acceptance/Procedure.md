# Procedure: DEL-033-06_epc-vendor-package-review-and-acceptance

## Purpose

Define the procedure for producing the EPC Integrator review-and-acceptance evidence for `DEL-033-06_epc-vendor-package-review-and-acceptance`, covering the `PKG-033` 4160V SWITCHGEAR ELECTRICAL BUILDING (830-2) package, against the accepted EPC Scope of Work, Package Datasheet, and Construction Work Package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 35.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Sibling EPC basis deliverables (read-only): `DEL-033-01_scope-of-work`, `DEL-033-02_package-datasheet`, `DEL-033-03_construction-work-package`.
- Sibling vendor inputs under review (read-only): `DEL-033-04_vendor-engineered-equipment-package`, `DEL-033-05_vendor-document-turnover-package`.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify against `DELIVERABLE_REGISTER.csv` row `DEL-033-06_epc-vendor-package-review-and-acceptance`.
3. Read workbook Packages row 35 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-033` and carry forward the responsibility model, scope, interface types, and objective support.
5. Read `INTERFACE_REGISTER.csv` rows for `PKG-033` and populate the interface matrix with all twelve applicable interfaces.
6. Read `ARTIFACT_REGISTER.csv` rows for `DEL-033-06_epc-vendor-package-review-and-acceptance` and confirm the deliverable produces the vendor document review log (`ART-221BEBC7F8`), acceptance/turnover checklist (`ART-396C3EAED7`), and factory/shop test and inspection evidence (`ART-46FF7B44A7`).
7. Identify the acceptance basis documents (`DEL-033-01`, `DEL-033-02`, `DEL-033-03`) and the vendor inputs under review (`DEL-033-04`, `DEL-033-05`); record the cross-reference plan without modifying sibling deliverable files.
8. Search accessible package-specific requirements for `PKG-033`. If no source-supported match is found (`PACKAGE_REGISTER.csv` `DocxPackageMatched=FALSE`), mark detailed acceptance criteria as `TBD`.
9. Draft the Datasheet identifying acceptance role, basis documents, artifacts, interfaces, and source gaps; preserve unsupported acceptance values as `TBD`.
10. Draft the Specification requirements (identity, artifacts, basis traceability, vendor-input traceability, interface coverage, responsibility integrity, gap discipline, turnover-readiness) and verification hooks.
11. Draft Guidance to explain conservative interpretation, basis-traceability discipline, interface-coverage scope, source gaps, and the human-ruling items.
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, interface list (twelve interfaces), basis-document IDs, responsibility split, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 35, Gate 7 registers, sibling deliverable IDs, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All twelve `INTERFACE_REGISTER.csv` interfaces for `PKG-033` are addressed consistently across the four documents. |
| Responsibility consistency | Vendor package responsibilities and EPC integration/reviewer responsibilities are not conflated. |
| Source-gap handling | Package-specific 4160V switchgear acceptance criteria remain `TBD` unless source-supported. |
| Human ruling items | Open ambiguity about missing package-specific source and sibling-maturity-at-acceptance appears in the Guidance Conflict Table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
