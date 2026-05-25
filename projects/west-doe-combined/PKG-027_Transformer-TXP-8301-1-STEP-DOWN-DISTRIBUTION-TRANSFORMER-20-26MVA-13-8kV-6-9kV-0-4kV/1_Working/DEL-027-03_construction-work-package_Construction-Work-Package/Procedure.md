# Procedure: DEL-027-03_construction-work-package

## Purpose

Define the procedure for producing and checking the Construction Work Package for `DEL-027-03_construction-work-package`, covering the `PKG-027` Transformer TXP-8301-1 — STEP DOWN DISTRIBUTION TRANSFORMER — 20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 29.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical and foundation source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (electrical system architecture, transformers, foundations, grounding, cable tray, conduit, electrical buildings).
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 29 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-027` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-027-03_construction-work-package` and confirm the construction work package includes the construction work package narrative, the installation and tie-in workface plan, and the construction interface and turnover checklist.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-027` and populate the construction interface scope with Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
7. Read DBM electrical and foundation source slices for transformer spacing, foundation type, grounding architecture, NGR scheme, cable tray and conduit routing, electrical building housing possibilities, and maintenance access.
8. Search accessible package-specific requirements for PKG-027. If no source-supported package-specific match is found, mark detailed construction parameters (rigging, oil handling, FAT/SAT, foundation footing, location, termination drawings) as `TBD`.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
12. Draft this Procedure to make the production and checking sequence repeatable.
13. Plan construction execution (after detailed engineering): mobilize site, install foundation, receive and set transformer, install grounding (two-point to ground grid; ground well; coordinate NGR scheme for 6.9 kV winding), terminate primary/secondary cabling, terminate I&C/communications cabling, energize per project commissioning standard, perform SAT, and complete turnover checklist.
14. Perform cross-document consistency checks for package identity, interface list, responsibility split, grounding/foundation/spacing requirements, and `TBD` items.
15. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
16. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 29, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All seven applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility integration / construction responsibilities are not conflated. |
| Source-gap handling | Construction-of-the-unit, rigging, oil handling, FAT/SAT/commissioning, foundation footing, physical location, and termination drawings remain `TBD` unless source-supported. |
| Human ruling items | Open ambiguity about oil-filled vs. dry-type construction, 6.9 kV NGR applicability to TXP-8301-1, and absence of package-specific construction requirements appear in the Guidance conflict table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
