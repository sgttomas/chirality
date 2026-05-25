# Procedure: DEL-014-03_construction-work-package

## Purpose

Define the procedure for producing and checking the Construction Work Package for `DEL-014-03_construction-work-package`, covering the `PKG-014` "CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE" package. The procedure covers how to author the construction work package documents and how the resulting package supports field construction execution and turnover.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 16.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM source slices: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Construction Responsibility, site basis, electrical buildings) and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (electrical voltage/service table, MCC, Remote I/O, cable tray/conduit).
- Declared upstream dependencies: none declared during PREPARATION.
- Companion EPC deliverables for cross-reference: `DEL-014-01_scope-of-work` and `DEL-014-02_package-datasheet`.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state (`OPEN` or `INITIALIZED`) before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 16 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-014` and carry forward the responsibility model, inclusion criteria, exclusions (if any), source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-014-03_construction-work-package` and confirm the deliverable plans for the three artifacts: construction work package, installation and tie-in workface plan, and construction interface and turnover checklist.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-014` and populate the construction tie-in scope with all seven applicable interfaces (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports).
7. Read DBM source slices for Construction Responsibility (Deepcut DBM), site basis, electrical voltage/service table, MCC and Remote I/O paragraphs, electrical buildings, and cable tray/conduit constraints. Limit derived statements to what these slices actually support.
8. Search the accessible reference set for any package-specific PKG-014 requirements (`26020-Package_Requirements.docx`). If no source-supported package-specific match is identified, mark panel count, contactor ratings, enclosure construction/rating, lighting/exhaust-fan circuit schedules, and installation location as `TBD`.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
10. Draft the Specification requirements and verification hooks from the Datasheet basis, the interface register, and DBM source slices.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
12. Draft this Procedure to make the production, construction execution support, and checking sequence repeatable.
13. Perform cross-document consistency checks for package identity, interface list (all seven), responsibility split (Package Vendor / EPC Integrator / Tourmaline field construction), voltage service basis, environmental site basis, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance conflict table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. Plan construction execution support: identify hold points for grounding/bonding verification, cable/conduit routing inspection, contactor panel setting and anchoring, lighting tie-in, exhaust-fan controls coordination with Remote I/O, and area-classification-aware installation; detailed inspection/test plans are `TBD` pending construction execution planning.
16. Plan turnover evidence: establish the construction interface and turnover checklist structure (panel set and anchored; grounding verified; terminations complete; controls integrated; lighting circuits energized and verified; exhaust-fan contactors verified); detailed certificate templates and signature workflow are `TBD`.
17. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 16, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All seven applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design, EPC facility integration, and Tourmaline field construction scopes are not conflated. |
| Source-gap handling | Panel count, contactor ratings, enclosure construction/rating, lighting/exhaust-fan circuit schedules, and installation location remain `TBD` unless source-supported. |
| Artifact planning | The three required artifacts (construction work package; installation and tie-in workface plan; construction interface and turnover checklist) are identified and planned. |
| Human ruling items | Open ambiguity captured in the Guidance conflict table appears in the run record as `NEEDS_HUMAN_RULING`. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
- Planned construction artifacts (produced during execution): construction work package (`ART-6B7A89231D`), installation and tie-in workface plan (`ART-46CD09710D`), construction interface and turnover checklist (`ART-497FADDF9B`).
