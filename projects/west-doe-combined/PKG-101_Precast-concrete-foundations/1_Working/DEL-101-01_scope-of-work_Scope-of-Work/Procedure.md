# Procedure: DEL-101-01 Scope of Work

## Purpose

Define the procedure for producing the PKG-101 Scope of Work using the accepted Gate 7 decomposition basis and locally accessible source materials. The procedure is for document production and verification, not field execution.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Deliverable-local `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md` are available.
- Workbook Packages row 102 is accessible in `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- DBM civil/structural source slices are accessible in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-11) and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Construction Scope Summary).
- Declared upstream dependencies: none declared during PREPARATION.
- Open external inputs to track: geotechnical assessment, topographical survey/grade surface file, plot plan, compressor dynamic analysis, compressor skid leak-containment arrangement, and any package-specific equipment/tag source.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md` and Gate 7 `DELIVERABLE_REGISTER.csv`.
2. Confirm current `_STATUS.md` permits drafting. For this run, current state was `OPEN`.
3. Read Gate 7 package basis for PKG-101 from `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv` (SOW-0257), `INTERFACE_REGISTER.csv` (IFC-26343B703C, IFC-BED3DE4194), `OBJECTIVE_DELIVERABLE_MAP.csv` (OBJ-001, OBJ-008), and `OBJECTIVE_PACKAGE_MAP.csv`.
4. Read workbook Packages row 102 and confirm the package identity, WBS, CoA tracking number (26020-01-36-001), discipline (Structural), and marked interface columns.
5. Read DBM-Deepcut SEC-11 source slices: Civil Scope; Governing Civil and Structural Basis; Geotechnical and Topographical Assumptions; Site Grading and Surface Water Management; Piles and Foundations (including precast applications for transformers and compressors); External Dependencies; Assumptions/TBDs.
6. Read DBM-Comp_and_Liquids Construction Scope Summary for Tourmaline field-construction responsibility assignments related to grading, piling, foundation work, and setting modules/pipe racks/equipment on foundations.
7. Draft the Scope of Work content so it includes:
   - package identity and source basis;
   - source-supported interfaces;
   - package function and integration narrative;
   - responsibility assignment record;
   - precast concrete foundation applications carried from DBM SEC-11;
   - open inputs and `TBD` items.
8. Mark unsupported values as `TBD`; label inferences as `ASSUMPTION` (e.g., objective association under PACKAGE_HEURISTIC; equipment-tag-to-package assignment).
9. Cross-check the four documents for consistent package ID, package name, WBS, CoA tracking number, interface types, foundation basis language, responsibility language, and `TBD` treatment.
10. Record source conflicts in the Guidance Conflict Table with source locations and human-ruling fields (see CONF-101-01-001, CONF-101-01-002).
11. Update `_STATUS.md` from `OPEN` to `INITIALIZED` via `tools/scaffolding/write_status.sh` only after the four documents exist and the state transition is safe.

## Verification

- Datasheet, Specification, Guidance, and Procedure all exist in the deliverable folder.
- Each document contains the default schema sections required by the four-documents skill.
- Package identity is consistent across all documents: PKG-101, DEL-101-01_scope-of-work, Precast concrete foundations, Structural, WBS 01, CoA tracking number 26020-01-36-001.
- Interface types are consistent across all documents: Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports.
- Precast foundation applications (transformers; compressors on driven steel piles subject to dynamic analysis) appear consistently in Datasheet Conditions, Specification Requirements (SOW-REQ-101-05, SOW-REQ-101-06), and Guidance Principles/Examples.
- No unsupported tagged equipment, precast element quantities, reinforcement schedules, coordinates, final geotechnical values, final survey values, or compressor dynamic analysis values are introduced.
- Each Specification requirement has a corresponding verification hook in Procedure or in the Specification Verification list.
- Guidance contains a Conflict Table with the two recorded conflicts (CONF-101-01-001, CONF-101-01-002) and TBD human-ruling fields.
- ASSUMPTION labels are present where inferences are used (objective association mode; equipment-tag-to-package mapping).

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md`
- `_run_records/TASK_RUN_2026-05-25_<HHMM>.md`
