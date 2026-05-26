# Procedure — Package Datasheet (DEL-064-02), PKG-064 Tanks, Water (API 650) 4-25

> Operational procedure for producing and issuing the Package Datasheet for the Process Water Storage Tanks (TK-5317-1, TK-5318-1, API 650, 04-25 Deepcut). Steps describe how the EPC Integrator assembles, verifies, and hands off the datasheet to the third-party vendor or discipline package engineer.

## Purpose

Produce a complete, source-traceable Package Datasheet so a third-party vendor (or discipline package engineer) can engineer and design two API 650 atmospheric process-water storage tanks and the package interfaces required for the 04-25 Deepcut facility, per the deliverable description in `_CONTEXT.md`.

## Prerequisites

- Accepted upstream basis available:
  - GATE-07 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - PACKAGE_REGISTER entry for PKG-064; DELIVERABLE_REGISTER row for DEL-064-02; OBJECTIVE_DELIVERABLE_MAP entries for OBJ-001 / OBJ-003 ... OBJ-010
- Accessible source materials:
  - DBM-Deepcut (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) — relevant slices identified in `Datasheet.md` References section
  - 26020-Package_Requirements.docx (heading 19) — to be parsed; currently location TBD
  - 26020-Packages_Interfaces_4_export.xlsx — to be parsed; currently location TBD
- Deliverable-local truth files in place: `_CONTEXT.md`, `_STATUS.md` (current state OPEN/INITIALIZED), `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`
- Declared upstream dependencies (per `_DEPENDENCIES.md`): none declared during PREPARATION
- No previously issued vendor datasheet for these tanks in the deliverable folder (this is a first-pass draft)

## Steps

1. **Confirm identity.** Re-read `_CONTEXT.md` and the GATE-07 PACKAGE_REGISTER row for PKG-064. Cross-check the tag list (TK-5317-1, TK-5318-1) against DBM-Deepcut line 2628 and the equipment-count table at line 2560.
2. **Resolve label mismatch.** Apply CF-064-02-001 (Guidance Conflict Table): confirm that the DBM "Tanks, Water (API 650) 2" row and the decomposition "Tanks, Water (API 650) 4-25" row refer to the same tank pair; carry as ASSUMPTION until human ruling.
3. **Extract attributes from accessible source.** From DBM-Deepcut, populate Datasheet Identification, Attributes, Conditions, and Construction tables using only the cited line references. Mark every value not present in source as TBD.
4. **Capture spacing and code basis.** Populate Conditions with NFPA 30, API 2510, OGAOM, and DPR 48 spacing values per DBM-Deepcut lines 265, 268, 270, 297.
5. **Capture mandatory plant-wide requirements.** Insulation for winter freezing (line 2509) and level-instrument drain tie-in (line 2510) are entered as requirements (REQ-064-02-002, REQ-064-02-003).
6. **Capture interfaces.** Identify Process Water Transfer Pump interface (P-5317-1, P-5318-1 in Tank Farm Pump Building 2 — lines 2555, 2621) and downstream-user interfaces (amine regeneration Module 530 — line 1132; NGL mercaptan treating make-up — line 1556). Record interface boundary at tank nozzles.
7. **Identify and surface conflicts.** Use the Guidance Conflict Table to record any source contradictions or unresolved label issues (CF-064-02-001 through -003).
8. **Mark unparsed sources.** Record 26020-Package_Requirements.docx heading 19 and 26020-Packages_Interfaces_4_export.xlsx as `location TBD; native binary not parsed in this pass`. Flag re-open trigger when parsed.
9. **Cross-check consistency.** Verify terminology (tank tags, package name, code reference) and numeric values are identical across Datasheet, Specification, Guidance, and Procedure.
10. **Update status.** When the four documents are written and the state is OPEN, advance `_STATUS.md` from `OPEN` to `INITIALIZED` via `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. If state is not OPEN, do not modify.
11. **Open items handoff.** Compile the Datasheet "Open Items / TBD" list as the resolution backlog for detailed engineering and source-document parsing. Issue handoff to EPC Integrator package owner.

## Verification

| Check | Pass Criterion |
|---|---|
| Tag list matches DBM and PACKAGE_REGISTER | TK-5317-1, TK-5318-1 present in Datasheet Identification; cross-reference to DBM-Deepcut line 2628 |
| Tank quantity = 2 | DBM-Deepcut line 2560 (x2); Datasheet Identification shows Quantity = 2 tanks |
| Insulation requirement captured | REQ-064-02-002 present and cites DBM-Deepcut line 2509 |
| Spacing values captured | Conditions table cites lines 265, 268, 270, 297 with values 30.48 m / 2.35 m / 80 m / 25 m |
| Interface boundary recorded | Pump interface (P-5317-1 / P-5318-1) and downstream users (Module 530, mercaptan treating make-up) appear in Datasheet Conditions and Spec Scope |
| TBDs explicit | All values not present in accessible source are TBD with reason |
| ASSUMPTIONs labeled | CF-064-02-001 label-mismatch ASSUMPTION explicit; project-wide foundation basis labeled ASSUMPTION |
| Source provenance present | Every non-trivial Datasheet/Spec row cites a `_Sources/` path + line range or marks `location TBD` |
| Cross-document consistency | Tank tags, code (API 650), insulation requirement, and pump interface identical across the four documents |
| Status update safe | `_STATUS.md` advanced only if current state was OPEN |

## Records

- `Datasheet.md` — primary package datasheet artifact (this deliverable)
- `Specification.md` — normative requirements derived from sources and decomposition
- `Guidance.md` — directional rationale, considerations, trade-offs, and Conflict Table
- `Procedure.md` — this document (production and issue procedure)
- `_STATUS.md` — updated `OPEN → INITIALIZED` after Pass 1/2 (safe update only)
- `_run_records/TASK_RUN_<timestamp>.md` — durable execution record for this run
- Open Items / TBD list (Datasheet Section "Open Items / TBD") — backlog handed to EPC Integrator package owner and to the source-parsing workstream (26020-Package_Requirements.docx, 26020-Packages_Interfaces_4_export.xlsx)
