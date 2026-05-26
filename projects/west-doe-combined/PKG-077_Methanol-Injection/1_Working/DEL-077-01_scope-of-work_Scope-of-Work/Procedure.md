# Procedure — DEL-077-01_scope-of-work (PKG-077 Methanol Injection)

## Purpose

Produce the EPC Integrator Scope of Work artifact set for PKG-077 Methanol Injection — covering identity, function, responsibility split, interfaces, boundaries, and whole-facility integration narrative — grounded in the Gate-07 PROJECT_DECOMP snapshot registers and the project workbook (row 72). Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-077-01_scope-of-work`.

## Prerequisites

- Read access to the Gate-07 snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`. Source: `_REFERENCES.md`.
- Read access to the workbook source slice for row 72: `26020-Package_Requirements.docx` and/or `26020-Packages_Interfaces_4_export.xlsx` under `_Sources`. Required to finalize REQ-077-01-03 (tagged equipment list). Source: `_Sources` listing.
- Declared upstream dependencies: none declared during PREPARATION. Source: `_DEPENDENCIES.md`.
- `_STATUS.md` is in state `OPEN` or `INITIALIZED` (otherwise this procedure must not overwrite).

## Steps

1. **Confirm package identity.** Pull DeliverableID, ParentPackageID, ParentWorkbookID, workbook row, CoA tracking number, WBS, discipline, and package name from `_CONTEXT.md` and `PACKAGE_REGISTER.csv` row `PKG-077`. Resolve to the Datasheet `Identification` table.
2. **Carry the scope-ledger anchor.** From `SCOPE_LEDGER.csv` row `SOW-0143`, transcribe the In/Out status (IN) and the scope-item statement into the Scope of Work narrative; cite SOW-0143 as the workbook-rooted scope anchor.
3. **Record responsibility split.** Transcribe the responsibility wording from `PACKAGE_REGISTER.csv` row `PKG-077` ResponsibilityNote into the responsibility assignment record (ART-1230D957BE). Source: `PACKAGE_REGISTER.csv`.
4. **Enumerate interfaces.** List all 13 interface types from `INTERFACE_REGISTER.csv` rows where `PackageID = PKG-077`. Verify each is flagged YES; cite each IFC-* row.
5. **Draft tagged-equipment list.** Open the workbook source slice (row 72) and extract the major-equipment text into the tagged equipment artifact (ART-F30A41723D). If the slice cannot be opened in this pass, leave the list as `TBD` with `location TBD` pointing at `26020-Package_Requirements.docx` row 72. Source: `ARTIFACT_REGISTER.csv`.
6. **Write the integration narrative.** Describe how Methanol Injection integrates with the process facility, citing: (a) the 13 applicable interface types; (b) the Gate 6 disposition that Methanol Injection scope is included with the Cryogenic Unit package scope (from `PACKAGE_REGISTER.csv` Notes); (c) the supported objectives (OBJ-001, OBJ-004–OBJ-010 from `DELIVERABLE_REGISTER.csv` and `OBJECTIVE_REGISTER.csv`).
7. **State exclusions explicitly.** Where `PACKAGE_REGISTER.csv` carries `TBD; no package-specific exclusions stated in source materials`, state this explicitly in the Scope of Work rather than implying no exclusions exist. Mark unsupported claims `TBD`.
8. **Cross-document check.** Verify Datasheet, Specification, Guidance, and Procedure use the same identifiers, the same 13 interface types, and the same responsibility wording. Resolve drift; add to the Conflict Table in `Guidance.md` if a source-rooted disagreement appears.
9. **Update `_STATUS.md`** via `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` if and only if the current state is `OPEN`.
10. **Write the run record** to `_run_records/TASK_RUN_<timestamp>.md` capturing inputs, sources consulted, outputs, missing items, and the status update outcome.

## Verification

| Check | Method | Source |
|---|---|---|
| Identity fields match register | Field-by-field comparison to `PACKAGE_REGISTER.csv` row `PKG-077` and `DELIVERABLE_REGISTER.csv` row `DEL-077-01_scope-of-work`. | snapshot |
| All 13 interface types present | Count and name match `INTERFACE_REGISTER.csv` rows for PKG-077. | snapshot |
| Responsibility wording preserved | String match to `PACKAGE_REGISTER.csv` ResponsibilityNote. | snapshot |
| Tagged-equipment list either populated from source or explicitly TBD with `location TBD` | Visual review of ART-F30A41723D content. | `ARTIFACT_REGISTER.csv` |
| Objective traceability complete | OBJ-001, OBJ-004–OBJ-010 each appear in the narrative or are explicitly tabled. | `OBJECTIVE_REGISTER.csv`; `DELIVERABLE_REGISTER.csv` |
| `_STATUS.md` updated only from `OPEN` → `INITIALIZED` | Pre/post inspection. | `_STATUS.md` |
| No metadata files modified (other than `_STATUS.md`) | `git diff` review. | repo |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- `_STATUS.md` updated from `OPEN` → `INITIALIZED` (safe update).
- Run record at `_run_records/TASK_RUN_<timestamp>.md`.
- Four-artifact set traceable to `ARTIFACT_REGISTER.csv` rows ART-319578C39E, ART-F30A41723D, ART-7A3F23A6BA, ART-1230D957BE.
