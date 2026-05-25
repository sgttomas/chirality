# Procedure: DEL-023-03_construction-work-package

## Purpose

Define the procedure for producing and checking the Construction Work Package for `DEL-023-03_construction-work-package`, covering the `PKG-023` MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD package. The procedure covers production of the EPC construction work package and the conditions under which the package will be physically installed, tied in, inspected, and turned over.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 25.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, `SCOPE_LEDGER.csv`.
- DBM electrical and construction-responsibility source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Declared upstream dependencies: none declared during PREPARATION.
- Companion EPC anchor deliverables for PKG-023 (Scope of Work `DEL-023-01`, Package Datasheet `DEL-023-02`) when available, for cross-reference only (no read in this run).

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 25 and record package ID, WBS, CoA tracking number, package name, discipline, and the six interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-023` and carry forward the responsibility model, inclusion criteria, exclusions, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-023-03_construction-work-package` and confirm the construction work package, installation and tie-in workface plan, and construction interface and turnover checklist are tracked.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-023` and populate the interface matrix with Electrical Power, Grounding/Bonding, I&C/Control Cabling, Communications/Network, Maintenance Access, and Structural/Foundations/Supports.
7. Read `SCOPE_LEDGER.csv` row `SOW-0024` and confirm the construction work package supports the workbook-defined scope item for `PKG-023`.
8. Read DBM source slices: medium-voltage services table; 4.16 kV MCC paragraph; electrical buildings paragraph; motors / area classification paragraph; cable schedule; cable tray / conduit and maintenance access paragraphs; grounding/bonding paragraphs; Construction Responsibility section.
9. Compose the construction responsibility matrix: assign grading, piling, foundation work, setting equipment on foundations, mechanical hookup, miscellaneous structural support installation, electrical terminations, and home-run cable installation to Tourmaline field construction; preserve interconnecting piping to ISBL/OSBL tie-ins as external responsibility to be confirmed per tie-in; reserve vendor package engineering/design for the Package Vendor and integration coordination for the EPC Integrator.
10. Compose the installation and tie-in workface plan: identify feeder tie-in to the 4.16 kV bus, grounding tie-in to the facility ground grid, and control/communications tie-in to the plant PLC/network as the principal tie-in classes; mark specific tie-in points `TBD` pending integration design.
11. Compose the construction interface and turnover checklist scope at the level supported by source: identity verification, interface fact verification, grounding verification (two-point major equipment grounding; CEC sizing where applicable), cable schedule conformance, maintenance access verification, area-classification verification for VFD-fed motor (Zone 2 marking and temperature code), and turnover record completeness. Mark detailed acceptance values `TBD`.
12. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
13. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
14. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
15. Draft this Procedure to make the production and checking sequence repeatable.
16. Perform cross-document consistency checks for package identity, interface list, responsibility split, construction-responsibility assignments, cable basis, area classification, and `TBD` items.
17. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
18. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 25, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All six applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design, EPC facility integration, and Tourmaline field construction responsibilities are not conflated. |
| Construction-responsibility fidelity | Field construction activities assigned to Tourmaline align with the DBM Construction Responsibility section list. |
| Cable / grounding / area-classification fidelity | Cable schedule, two-point grounding, and Zone 2 motor marking statements match cited DBM source slices. |
| Source-gap handling | VFD topology, driven motor identity, lift weights, foundation loads, energization sequence, and detailed commissioning steps remain `TBD` unless source-supported. |
| Human ruling items | Driven-motor assignment, "VFD/soft-starter at 4.16 kV are TBD" tension, and turnover checklist content scope appear in the Guidance conflict table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
