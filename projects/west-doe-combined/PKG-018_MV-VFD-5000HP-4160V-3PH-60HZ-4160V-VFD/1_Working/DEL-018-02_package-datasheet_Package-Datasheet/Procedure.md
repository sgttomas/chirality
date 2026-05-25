# Procedure: DEL-018-02_package-datasheet

## Purpose

Produce, maintain, and hand off the EPC Package Datasheet for `PKG-018` (MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD) such that a third-party Package Vendor can perform package engineering and design under `DEL-018-04`, and downstream construction and acceptance deliverables can rely on it as the integrator-authored technical handoff basis.

## Prerequisites

- Read access to the Gate 7 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Read access to `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Packages sheet row 20).
- Read access to `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` for drive, motor, MCC, electrical-building, hazardous-area, grounding, and cable basis.
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` present in this deliverable folder.
- No declared upstream dependencies (per `_DEPENDENCIES.md`).
- Pending human ruling on Guidance Conflict Table entries CT-018-02-01, CT-018-02-02, CT-018-02-03 before the datasheet is issued externally.

## Steps

1. **Identity carry-through.** Populate the Datasheet Identification table strictly from `PACKAGE_REGISTER.csv` row `PKG-018` and workbook row 20. Do not paraphrase the package name.
2. **Interface evidence.** For each of the six `PKG-018` rows in `INTERFACE_REGISTER.csv`, record an entry in Datasheet Conditions and Specification REQ-018-02-05; link to the corresponding `ART-*` row in `ARTIFACT_REGISTER.csv`.
3. **Drive-mode basis.** From accessible source slices (Comp_and_Liquids DBM lines 324, 326, 752-760; Deepcut DBM lines 893, 2955-2963, 3013, 3088), populate the Attributes table and REQ-018-02-03/04 with source citations. Mark as ASSUMPTION any inference about driven-load assignment.
4. **Constraint pull-through.** Capture SCA-001 VE #34 (Starting VFD requirement) and SCA-001 VE #37 (no capacitor banks on the VFD-present synchronous-transfer bus) as both Standards and Requirements entries with citation.
5. **Hazardous-area and cable basis.** Capture Deepcut DBM line 2961 (Zone 2 marking and temperature code) and line 3013 (Copper TECK for LV cable fed from VFDs) as Requirements; mark MV output cable as TBD.
6. **Electrical-buildings location.** Record electrical-building housing as ASSUMPTION until a layout deliverable assigns location.
7. **Conflict capture.** For each unresolved discrepancy between workbook identity and source motor basis, write a row in the Guidance Conflict Table with `Source A`, `Source B`, impacted sections, a PROPOSAL, and `TBD` human ruling.
8. **Cross-document consistency sweep.** Verify that Datasheet attribute values, Specification requirement values, Guidance considerations, and Procedure prerequisites all use consistent terminology and numbers for: package name, CoA tag, voltage class, HP class, drive mode, capacitor-bank prohibition, Ethernet/PLC port basis, Zone 2 marking rule, grounding two-point rule, electrical-building housing assumption.
9. **Status update.** Run `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` only if current `_STATUS.md` state is `OPEN`. Append a history line dated `2026-05-24`.
10. **Run record.** Write a TASK run record at `{DELIVERABLE_PATH}/_run_records/TASK_RUN_2026-05-24_{HHmm}.md` capturing inputs, resolved skill state, outputs, MISSING items, NEEDS_HUMAN_RULING items (HRR-018-02-001 onward), and applied changes.

## Verification

- Datasheet exists with Identification, Attributes, Conditions, Construction, References sections populated and source-cited.
- Specification exists with Scope, Requirements, Standards, Verification, Documentation sections populated and source-cited.
- Guidance exists with Purpose, Principles, Considerations, Trade-offs, Examples, and a populated Conflict Table.
- Procedure exists with Purpose, Prerequisites, Steps, Verification, Records sections.
- All six `PKG-018` interface facts represented as both Conditions entries (Datasheet) and REQ-018-02-05 evidence (Specification).
- All source citations point to existing files in the Gate 7 snapshot or `_Sources`.
- Unsupported values are `TBD` or labeled `ASSUMPTION:` or surfaced as conflict-table entries; no invented values.
- `_STATUS.md` is `INITIALIZED` if and only if it was `OPEN` at the start of the run.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in this deliverable folder.
- `_STATUS.md` updated to `INITIALIZED` (or skipped per safe rule).
- `_run_records/TASK_RUN_2026-05-24_{HHmm}.md` capturing the run.
- Human rulings against Guidance Conflict Table rows CT-018-02-01, CT-018-02-02, CT-018-02-03 (recorded externally to this deliverable upon issuance; the rulings are imported into a future revision of this deliverable).
