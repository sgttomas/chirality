# Procedure: DEL-071-01 — Scope of Work (PKG-071 Fuel Gas Skid 4-25)

This procedure describes the steps to **produce** the DEL-071-01 Scope of Work artifact set (ART-AC01900208, ART-31BC19483F, ART-5369838D71, ART-451A242BFC, ART-CD58F7CD21) for the EPC Integrator.

## Purpose

Provide an auditable, source-grounded path for the EPC Integrator to author the PKG-071 Scope of Work such that:

- it satisfies every requirement in `Specification.md`,
- it preserves source-stated TBDs,
- it makes the vendor/EPC responsibility split unambiguous, and
- it surfaces all applicable interface types for downstream integration work.

## Prerequisites

### Declared upstream dependencies

- None declared in `_DEPENDENCIES.md`. (Coordination Mode: DECLARED.)

### Required references (accessible)

- `_CONTEXT.md` (this deliverable folder).
- `_REFERENCES.md` (this deliverable folder).
- GATE-07 accepted snapshot:
  - PACKAGE_REGISTER.csv (PKG-071 row).
  - DELIVERABLE_REGISTER.csv (DEL-071-01 row).
  - SCOPE_LEDGER.csv (SOW-0099, SOW-0100, SOW-0101, SOW-0102).
  - ARTIFACT_REGISTER.csv (rows for DEL-071-01).
  - OBJECTIVE_REGISTER.csv (OBJ-001, OBJ-004..010 for cross-reference).

### Required references (currently inaccessible at clause level — location TBD)

- 26020-Package_Requirements.docx, package heading 25 (binary).
- 26020-Packages_Interfaces_4_export.xlsx, Packages row 61 (binary).

A human-readable extract or converter run for these two source files should precede Pass 3 / final acceptance.

### Required tools

- Markdown editor (any).
- Access to the GATE-07 snapshot directory (read-only).
- Optional: `tools/scaffolding/write_status.sh` for `_STATUS.md` transitions.

## Steps

1. **Read inputs.** Open `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and the four GATE-07 register files listed above. Confirm DEL-071-01 row maps to PKG-071 and the four SOW-009x..010x rows.
2. **Confirm package identity.** Verify the identity fields (Workbook ID, CoA tracking, WBS, Discipline, Package Name) against PACKAGE_REGISTER.csv. Carry them verbatim into `Datasheet.md` Identification.
3. **Extract function and basic scope.** From SCOPE_LEDGER SOW-0100, restate the package function and basic-scope sentences. Do not paraphrase the equipment count (1 heater, 1 scrubber, 1 skid).
4. **Extract major included equipment.** From SCOPE_LEDGER SOW-0101, restate the heater (SCR-controlled, skin-temp thermocouple override) and scrubber (k = 0.35 imperial max plus de-ration; vendor-designed) basis.
5. **Extract operating and design conditions.** From SCOPE_LEDGER SOW-0102, restate design flow (> 8.4 MMSCFD / 237.5 e3m3/day), outlet temperature (95 F / 35 C), operating pressure (150 psig), ambient range (-19 C to 22.2 C), design pressure (150 psig), design temperature range (-40 C to 35 C), and the explicit TBDs (Final Flow, MAWP).
6. **Extract by-others list.** From SCOPE_LEDGER SOW-0102, restate the four by-others items: shipping to site, installation, tie-in piping, electrical tie-in. Preserve these as exclusions in the SOW.
7. **Extract responsibility split.** From PACKAGE_REGISTER.csv ResponsibilityModel column, restate the vendor and EPC responsibilities. Cross-check against ART-451A242BFC.
8. **Extract applicable interface types.** From PACKAGE_REGISTER.csv applicable interfaces column, list all twelve interface types. Do not abbreviate or drop any.
9. **Cross-reference scope and objectives.** Include the four SOW IDs (0099, 0100, 0101, 0102) and the eight OBJ IDs (001, 004..010) as cross-references; do not derive new requirements from the OBJ pass-throughs.
10. **Assemble the four documents.** Populate `Datasheet.md` (identification + attributes + conditions + construction + boundaries + interfaces + responsibility), `Specification.md` (scope + requirements REQ-071-01-01..15 + standards + verification + documentation), `Guidance.md` (purpose + principles + considerations + trade-offs + examples + conflict table), and this `Procedure.md`.
11. **Conflict table.** Capture unresolved items in `Guidance.md` Conflict Table for human ruling (currently CF-071-01-01..03).
12. **Status update.** If `_STATUS.md` is OPEN, transition to INITIALIZED via `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` (or by direct edit when running this skill in-shell). Do not regress state.
13. **Run record.** Persist the run record at `_run_records/TASK_RUN_<timestamp>.md` with frontmatter, requested tasks, tools used, outputs, missing, needs-human-ruling, dependency notes, and applied changes.

## Verification

| Step(s) | Verification Check |
|---|---|
| 2, 3, 4, 5, 6, 7, 8 | Each Datasheet/Specification value can be traced to a specific SCOPE_LEDGER row or PACKAGE_REGISTER cell. |
| 9 | All four SOW IDs and all eight OBJ IDs appear in Specification REQ-071-01-13. |
| 10 | All four documents exist and contain the default schema sections defined by the four-documents skill. |
| 11 | Conflict Table is present in `Guidance.md` with at least the open items identified in this run. |
| 12 | `_STATUS.md` reflects INITIALIZED; History entry references TASK+four-documents and the run date. |
| 13 | Run record exists with `run-status: SUCCESS` (or other terminal status) and required frontmatter fields. |
| All | No TBD values from source (Final Flow, MAWP, heater capacity) are silently filled in. |
| All | No files outside `{DELIVERABLE_PATH}` were modified. |

## Records

Upon successful execution:

- `Datasheet.md` (this folder)
- `Specification.md` (this folder)
- `Guidance.md` (this folder, including Conflict Table)
- `Procedure.md` (this folder)
- `_STATUS.md` updated (OPEN → INITIALIZED) with appended History entry
- `_run_records/TASK_RUN_<timestamp>.md` persisted

These records, together with the GATE-07 source snapshot, constitute the audit trail for the initial DEL-071-01 articulation.
