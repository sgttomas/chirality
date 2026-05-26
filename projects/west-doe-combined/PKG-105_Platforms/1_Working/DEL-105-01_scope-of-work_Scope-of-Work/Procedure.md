# Procedure: DEL-105-01 — Scope of Work (PKG-105 Platforms)

## Purpose

Produce the EPC Integrator-authored Scope of Work artifact set for PKG-105 "Platforms" such that it satisfies the requirements in `Specification.md` and conforms to the guidance in `Guidance.md`.

This procedure describes the steps to **produce** the SoW deliverable (Interpretation rule: production procedure).

## Prerequisites

- Read access to the GATE-07 Final Published PROJECT_DECOMP snapshot (`_REFERENCES.md`).
- Read access to the DBM source `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Transcribed source slice of `_Sources/26020-Package_Requirements.docx` package heading for Workbook row 106 (currently TBD — binary file, slice not transcribed).
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` reviewed.
- Declared upstream dependencies: none declared during PREPARATION (`_DEPENDENCIES.md`). Run `TASK + dependency-extract` if critical dependencies need in-file declaration (per `_DEPENDENCIES.md` Run Notes).

## Steps

1. **Confirm decomposition basis.** Open the GATE-07 snapshot and confirm the row for `DEL-105-01_scope-of-work` in DELIVERABLE_REGISTER.csv and the row for PKG-105 in PACKAGE_REGISTER.csv. Record the exact field values used.
2. **Populate package identity.** Restate Workbook ID 105 / row 106, CoA `26020-01-36-005`, WBS 01, discipline Structural, name "Platforms," responsible party EPC Integrator. (Satisfies R-105-01-01.)
3. **Build the tagged-equipment and package identity list.** Transcribe the package heading for Workbook row 106 from `26020-Package_Requirements.docx` (location TBD). Where source-supported equipment text exists, list it. Where it does not, mark `TBD`. Produce ART-21C90A2BB4. (Satisfies R-105-01-02.)
4. **Write the package function and whole-facility integration narrative.** Describe what the platforms package does (access for operation, inspection, and maintenance of equipment and piping at scale — ASSUMPTION at the generic level) and how it integrates with adjacent discipline scopes via the three declared interface types. Do not name specific platforms not in source. Produce ART-1B624DB0B8. (Satisfies R-105-01-03.)
5. **Record the responsibility assignment.** EPC Integrator owns SoW execution. Discipline subcontracting decisions (if any) are deferred to DEL-105-04 and shall not be pre-committed here. Produce ART-77976FD844. (Satisfies R-105-01-04.)
6. **Enumerate physical interfaces and Gate 6 disposition.** List the three INTERFACE_REGISTER.csv rows for PKG-105 (Area / Exterior Lighting; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports). Restate the Gate 6 disposition that platform-to-equipment tie-ins are the EPC Integrator's responsibility through the overall 3D model and integrated P&ID set. (Satisfies R-105-01-05, R-105-01-06.)
7. **Cite the governing structural basis.** Reference CSA S16, CSA G40.20/G40.21 (350W/300W per DBM line 2676), and CSA W59, as listed in the DBM "Governing Civil and Structural Basis" section. Note the geotechnical-report dependence for platform foundations (DBM line 2685). (Satisfies R-105-01-07.)
8. **Mark boundaries / exclusions / battery limits.** Where the source set states none, write "TBD — no package-specific exclusions stated in source materials" with a pointer to `26020-Package_Requirements.docx` row 106 heading for future resolution. (Satisfies R-105-01-08.)
9. **Cite upstream snapshot.** Include the GATE-07 Final Published snapshot path in the SoW provenance section. (Satisfies R-105-01-09.)
10. **Update `_STATUS.md`** via `tools/scaffolding/write_status.sh` from `OPEN` to `INITIALIZED` after Pass 1/Pass 2 complete.

## Verification

| Check | How |
|---|---|
| All four anticipated artifacts produced and referenced by ART-ID | Diff `Specification.md §Documentation` against ARTIFACT_REGISTER.csv rows for DEL-105-01. |
| All three physical interfaces carried | Diff SoW interface list against INTERFACE_REGISTER.csv rows for PKG-105. |
| Standards citations resolve to DBM lines | Spot-check each standard citation against `4-25_Deepcut_DBM.md` line numbers given in `Datasheet.md §Conditions`. |
| TBD items have source pointers | Grep for `TBD` and confirm each is paired with a source pointer or "location TBD." |
| Provenance snapshot cited | Confirm GATE-07 path appears in the SoW. |
| Status transition safe | Confirm `_STATUS.md` history shows `OPEN → INITIALIZED` only when prior state was `OPEN`. |

## Records

- The four documents in `{DELIVERABLE_PATH}`: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`.
- The `_run_records/TASK_RUN_2026-05-25_<HHMM>.md` run record produced by this TASK invocation.
- Updated `_STATUS.md` reflecting the safe state transition.
- ARTIFACT_REGISTER.csv rows ART-B537AC5EA7, ART-21C90A2BB4, ART-1B624DB0B8, ART-77976FD844 remain the registered evidence anchors for downstream consumers.
