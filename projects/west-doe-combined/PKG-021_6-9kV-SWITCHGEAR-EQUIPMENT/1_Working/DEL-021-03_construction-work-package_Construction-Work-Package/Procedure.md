# Procedure: DEL-021-03_construction-work-package

## Purpose

Define the procedure for producing and checking the Construction Work Package for `DEL-021-03_construction-work-package`, covering the `PKG-021` 6.9kV SWITCHGEAR EQUIPMENT package. The procedure makes the production and checking sequence repeatable across packages and runs.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 23.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, `SCOPE_LEDGER.csv`.
- DBM electrical and construction-responsibility source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-12 Electrical Basis and Construction Responsibility sections).
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state (`OPEN` or `INITIALIZED`) before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 23 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-021` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-021-03_construction-work-package` and confirm the CWP includes a construction work package, an installation and tie-in workface plan, and a construction interface and turnover checklist.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-021` and ensure the tie-in plan covers all six interfaces: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
7. Read `SCOPE_LEDGER.csv` row `SOW-0022` to confirm scope-item coverage for the package.
8. Read DBM source slices for the 6.9 kV system voltage basis, grounding/bonding, electrical buildings, cable specifications, cable tray and conduit routing, electrical studies, governing specifications (Table 12-1), and Construction Responsibility section.
9. Search the accessible package-specific requirements source set for PKG-021 / 6.9 kV switchgear construction content. If no source-supported package-specific match is found, mark detailed installation quantities, sequencing, lift plans, and ratings as `TBD`.
10. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
11. Draft the Specification requirements and verification hooks from the Datasheet basis and the source slices, citing the governing specifications by document ID and marking clause-level locations as `TBD`.
12. Draft the Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
13. Draft this Procedure to make the production and checking sequence repeatable.
14. Perform cross-document consistency checks for package identity, six-interface coverage, three-way responsibility split (Package Vendor / EPC Integrator / Tourmaline field construction), grounding basis, governing-specification references, and `TBD` items.
15. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
16. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 23, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All six applicable interfaces are addressed consistently across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Package Vendor, EPC Integrator, and Tourmaline field construction responsibilities are not conflated. |
| Source-gap handling | Lineup quantity/rating, installation location, lift plans, sequencing, and schedule remain `TBD` unless source-supported. |
| Human-ruling items | Open ambiguity about installation location (Building 820-1), MV switchgear quantity allocation, and EPC/Tourmaline construction-execution boundary appears in the Guidance conflict table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
