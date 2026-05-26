# Procedure — DEL-041-01 Scope of Work (PKG-041, 490-1 Standby Generator Building)

**Interpretation:** This Procedure describes the steps to **produce** the DEL-041-01 Scope of Work artifact (a documentation deliverable), not the steps to operate the standby generator package itself.

## Purpose

Provide a repeatable procedure for drafting, reviewing, and issuing the EPC Integrator Scope of Work for PKG-041 so that the package identity, ownership split, current technical basis, interfaces, tagged equipment, open items, and objective traceability are all source-grounded and auditable.

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` present in the deliverable folder.
- Read access to the accepted decomposition snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` and to PACKAGE_REGISTER.csv row 43 and DELIVERABLE_REGISTER.csv row 228.
- Read access to `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` sections "Emergency Power Generation Basis", "Standby Power", Module Assembly table, Tagged Equipment table row 69.
- Declared upstream dependencies: none currently declared in `_DEPENDENCIES.md`. (If a future revision declares upstream dependencies — e.g., site-wide electrical study, TOU standby standard — the SOW shall cite their maturity.)
- Declared downstream dependencies: none currently declared in `_DEPENDENCIES.md`. (DEL-041-02 Package Datasheet, DEL-041-03 Construction Work Package, and DEL-041-06 EPC Vendor Package Review and Acceptance are anticipated downstream consumers per DELIVERABLE_REGISTER.csv rows 229, 230, 233.)

## Steps

1. **Confirm package identity.** Record the workbook title (PACKAGE_REGISTER.csv row 43) and the design-basis module label ("490-1 Emergency Generator Module" per DBM Module Assembly table). Surface both in the SOW.
2. **Capture the current technical basis.** Quote or paraphrase the DBM "Emergency Power Generation Basis" section and "Standby Power" section, including the explicit statement that the 13.8 kV tie-in is eliminated and the basis is LV (480 V or 600 V class) TOU standby generation on LV MCC with transfer switch serving 04-25 and 03-25 critical loads.
3. **List tagged equipment.** Transcribe AC-4910-1, EGD-4950-1, EG-4950-1, ACM-4910-1 from DBM Tagged Equipment table row 69. Add no other tags.
4. **Capture ownership split.** Transcribe the Package Vendor / EPC Integrator responsibility wording verbatim from PACKAGE_REGISTER.csv row 43 (or paraphrase faithfully without altering scope).
5. **Enumerate interfaces.** Transcribe the twelve applicable interface types from PACKAGE_REGISTER.csv row 43. Map each to EPC Integrator scope.
6. **Surface open items as TBD.** Pull each "TBD" or "to be confirmed" item from the DBM "Emergency Power Generation Basis" table and the DBM Item table "Standby generator integration" row. Assign nominal owner (MLE, EPC, electrical studies) per DBM language.
7. **Surface CT-001 and CT-002.** Add the conflict entries to `Guidance.md` Conflict Table; mark them TBD pending human ruling. Do not silently reconcile in the SOW narrative.
8. **Record objective traceability.** List OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 from `_CONTEXT.md` / PACKAGE_REGISTER.csv row 43 supported-objectives column, labeled ASSUMPTION (PACKAGE_HEURISTIC).
9. **Cross-document consistency sweep.** Run the Step 5 checks from skill `four-documents`: entity/attribute alignment between Datasheet and Specification; requirement-to-rationale alignment between Specification and Guidance; requirement-to-verification alignment between Specification and Procedure; terminology and value consistency across all four documents.
10. **Status transition.** Run `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` only when the prior state is `OPEN`. Do not regress state.
11. **Persist run record.** Write `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` with full input echo, resolved state, tools used, outputs produced, MISSING, NEEDS_HUMAN_RULING, and DEPENDENCY_NOTES.

## Verification

| Check | Pass criterion |
|---|---|
| Identity | Both workbook title and module label appear in Datasheet and Specification. |
| Basis | Datasheet Attributes and Specification Scope describe the LV TOU basis and explicitly note the elimination of the 13.8 kV tie-in. |
| Tags | The four tags AC-4910-1, EGD-4950-1, EG-4950-1, ACM-4910-1 appear in Datasheet and are not contradicted elsewhere. |
| Interfaces | All twelve interface types from PACKAGE_REGISTER.csv row 43 appear in Specification R-041-01-06 and Datasheet Attributes. |
| Ownership | Vendor-vs-EPC split appears verbatim or faithfully paraphrased in Datasheet and Specification. |
| Open items | Every TBD/to-be-confirmed item from DBM "Emergency Power Generation Basis" and "Standby generator integration" item appears as an open item in Specification R-041-01-05. |
| Conflicts | CT-001 and CT-002 appear in `Guidance.md` with TBD ruling. |
| Objectives | OBJ-001 and OBJ-004 through OBJ-010 appear in Specification R-041-01-12 with ASSUMPTION label. |
| Status | `_STATUS.md` shows `INITIALIZED` only if prior state was `OPEN`. No state regression. |

## Records

- `Datasheet.md` (this folder)
- `Specification.md` (this folder)
- `Guidance.md` (this folder, includes Conflict Table)
- `Procedure.md` (this folder)
- `_STATUS.md` (state transition record)
- `_run_records/TASK_RUN_2026-05-24_2324.md` (durable run record)
