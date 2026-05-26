# Procedure — DEL-073-01 Scope of Work (PKG-073 Amine Treating Unit)

## Purpose

Operational steps to **produce** the EPC Scope of Work artifact for PKG-073 Amine Treating Unit, grounded in the GATE-07 PROJECT_DECOMP snapshot and the `_Sources` source basis. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` DEL-073-01.)

## Prerequisites

- Accepted upstream decomposition snapshot accessible at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`. (Source: `_REFERENCES.md`; `_DEPENDENCIES.md`.)
- Read access to `_Sources/26020-Package_Requirements.docx` (binary; clause-level slice extraction may be required). (Source: `_REFERENCES.md`.)
- Read access to `_Sources/26020-Packages_Interfaces_4_export.xlsx` workbook row 49. (Source: `PACKAGE_REGISTER.csv` PKG-073.)
- Read access to DBM-Deepcut/4-25_Deepcut_DBM.md design basis. (Source: `PACKAGE_REGISTER.csv`.)
- Read access to bid document `26020-01-PT-RFQ-27-001_Amine_Treat_Unit_R0.docx` (currently `location TBD`; not present in `_Sources`). (Source: `PACKAGE_REGISTER.csv`.)
- Declared upstream dependencies: none recorded in `_DEPENDENCIES.md` (PREPARATION mode DECLARED). (Source: `_DEPENDENCIES.md`.)
- Companion deliverables (DEL-073-02 through DEL-073-06) must consume this SOW; coordinate identifier and terminology stability before publishing. (Source: `DELIVERABLE_REGISTER.csv`.)

## Steps

1. **Confirm package identity.** Read `PACKAGE_REGISTER.csv` PKG-073 row and record the identity fields in the Datasheet (Identification table). Cross-check against `_CONTEXT.md`. (Verification: identifiers match across `_CONTEXT.md`, Datasheet, Specification R-073-01-01.)

2. **Extract source basis.** Read 26020-Package_Requirements.docx heading 27 (target a markdown slice extraction if not already available). Capture: package function, two-module description, equipment enumeration, scope notes, by-others list, motor electrical class, Appendix A pointers. Where binary text is not yet accessible, mark `location TBD` and add an item to the Guidance Conflict Table. (Verification: every claim in Specification has a source citation or a `TBD`/`ASSUMPTION` marker.)

3. **Populate process function and module narrative.** Transcribe the SOW-0052 text into the Specification (Scope) and Guidance (Principles) using exact source phrasing for the two-module description. (Verification: text matches SOW-0052.)

4. **Enumerate tagged equipment.** Populate the Datasheet "Construction — Tagged / Major Included Equipment" table with all items from `SCOPE_LEDGER.csv` SOW-0053 and from 26020-Package_Requirements.docx heading 27 when accessible. Flag missing items as TBD. (Verification: equipment table cross-references SOW-0053 row IDs.)

5. **Map facility interfaces.** Copy every PKG-073 row from `INTERFACE_REGISTER.csv` into the Datasheet "Package Interfaces" table and reflect them in Specification R-073-01-04. (Verification: count of interface rows in Datasheet equals count in `INTERFACE_REGISTER.csv` for PKG-073 — 13 rows.)

6. **Record motor electrical requirements.** Place the SOW-0054 motor class text into Specification R-073-01-05 and Guidance (Examples). (Verification: voltage classes and VFD-ready threshold match SOW-0054 exactly.)

7. **Record exclusions ("By Others").** Place the SOW-0054 by-others list in Datasheet "By Others" and Specification R-073-01-06. (Verification: every excluded item from SOW-0054 appears in both locations.)

8. **Record objective traceability.** List the supported objectives (OBJ-001, OBJ-003..OBJ-010) from `_CONTEXT.md` and `OBJECTIVE_DELIVERABLE_MAP.csv` in Specification R-073-01-08; label as ASSUMPTION per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`. (Verification: every listed objective ID resolves in `OBJECTIVE_REGISTER.csv`.)

9. **Draft whole-facility integration narrative.** Identify upstream sour-gas source(s) and downstream consumers (PKG-046 Acid Gas Compressors confirmed by its `PACKAGE_REGISTER.csv` row; sweet-gas downstream dehydration ASSUMPTION). Record the narrative in Specification R-073-01-09 and Guidance Considerations. (Verification: each named upstream/downstream package resolves in `PACKAGE_REGISTER.csv`.)

10. **Reconcile conflicts.** For any clause that depends on inaccessible source slices (Word heading 27 full text; Appendix A), add or update a Conflict Table row in `Guidance.md`. (Verification: every TBD-bearing requirement is either resolved by source or tracked in the Conflict Table.)

11. **Cross-document consistency sweep.** Verify terminology, IDs, and numeric values are consistent across the four documents (Datasheet ↔ Specification ↔ Guidance ↔ Procedure). (Verification: Step 5 cross-check matrix from the four-documents skill passes.)

12. **Update `_STATUS.md`.** If and only if current state is `OPEN`, run `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. Do not regress state. (Verification: `_STATUS.md` shows `INITIALIZED` with the new history entry.)

## Verification

| Check | Method | Pass Criterion |
|---|---|---|
| Identity traceability | Compare Datasheet identifiers against `PACKAGE_REGISTER.csv` PKG-073 | All identity fields equal |
| Interface completeness | Count PKG-073 rows in `INTERFACE_REGISTER.csv` vs. Datasheet | 13 == 13 |
| Source citation | Every non-trivial claim cites a source or carries `TBD`/`ASSUMPTION` | No unsourced assertions |
| Objective traceability | Each `Supports Objectives` ID resolves in `OBJECTIVE_REGISTER.csv` | All resolve |
| Conflict tracking | Every clause depending on inaccessible source has a Conflict Table entry | All present |
| Cross-document consistency | Terminology, IDs, numeric values consistent across the four documents | No discrepancies |
| Status update safety | `_STATUS.md` updated only from `OPEN`; never regressed | Compliant |

## Records

Per `_CONTEXT.md` (Anticipated Artifacts) and `DELIVERABLE_REGISTER.csv` DEL-073-01:

- This deliverable folder containing `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`.
- Updated `_STATUS.md` reflecting `OPEN → INITIALIZED`.
- Run record at `_run_records/TASK_RUN_<timestamp>.md` documenting inputs, tools, outputs, missing items, and the Conflict Table seed.
- Conflict Table seeded in `Guidance.md` capturing source-slice accessibility gaps (Word heading 27 full extract; Appendix A).
