# Procedure — DEL-043-02 Package Datasheet (PKG-043)

> Operational document. Describes how to produce and verify the PKG-043 Package Datasheet artifact (ART-B02B65CCAE) and its companion handoff/interface evidence rows. Tracks `Specification.md` requirements.

## Prerequisites

- Read `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`.
- Confirm `_STATUS.md` is in a state that permits editing (`OPEN` or `INITIALIZED`) per the active overwrite policy.
- Local access to the Gate 7 Final Published PROJECT_DECOMP snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (registers used: `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`).
- Local access to the workbook source slices: `_Sources/26020-Package_Requirements.docx`, `_Sources/26020-Packages_Interfaces_4_export.xlsx`. If these are not openable as text in the current environment, the workbook-derived sections of `Datasheet.md` MUST remain `TBD` (see REQ-043-02-08).
- Declared dependencies: none at PREPARATION (`_DEPENDENCIES.md`); proceed without explicit upstream blockers.

## Steps

1. **Identification.** Populate `Datasheet.md` *Identification* table from `PACKAGE_REGISTER.csv` row 45 and `DELIVERABLE_REGISTER.csv` row 241. (REQ-043-02-01)
2. **Attributes.** Copy `ResponsibilityModel`, `PackageRole`, `OpenIssue`, `InclusionCriteria`, `Exclusions` verbatim from `PACKAGE_REGISTER.csv` row 45. (REQ-043-02-05, REQ-043-02-06)
3. **Interface inventory.** For each PKG-043 row in `INTERFACE_REGISTER.csv`, write one row in the Datasheet *Package Interface Inventory* including `InterfaceID`, `InterfaceType`, `Applicability`, and the Gate 6 disposition note. (REQ-043-02-02, REQ-043-02-03)
4. **Anticipated artifacts.** Enumerate ART-* rows for DEL-043-02 from `ARTIFACT_REGISTER.csv` in the Datasheet *Anticipated Artifacts* table. Confirm `SourceArtifactID` linkage where present. (REQ-043-02-04)
5. **Conditions / service data.** Open the workbook source slice for row 45 and extract: process service, design conditions, environmental / area classification, power supply, signal protocols. Cite `SourcePath + SectionRef`. Where a value cannot be extracted, leave the cell `TBD` with `location TBD`. (REQ-043-02-07, REQ-043-02-08, REQ-043-02-10) — TBD pending workbook extraction.
6. **Tagged equipment.** Cross-reference DEL-043-01 *Tagged equipment and package identity list* (ART-75803D0212) once produced; carry only equipment items the workbook supports for PKG-043. TBD pending DEL-043-01 production.
7. **Vendor handoff basis.** Author ART-DE833DACCC content covering battery limits, design expectations, source-supported requirements, and known unknowns (`TBD`s) as a coherent handoff narrative. (REQ-043-02-07)
8. **Interface requirements matrix.** Author ART-CAED753CC5 content. Minimum content = the five Gate 6 interface-type rows; deeper tag/loop content is `TBD` until workbook extraction. (REQ-043-02-02)
9. **Interface note disposition.** Record ART-E75CB9E824 by copying the Gate 6 disposition once and referencing it from each interface row. (REQ-043-02-03)
10. **Cross-document consistency sweep.** Verify entities, terminology, and numeric values are consistent across `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (Pass 2). Open Conflict Table entries where conflicts cannot be resolved from drafts alone.
11. **Status update.** If `_STATUS.md` is `OPEN`, run `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. Do not regress state.

## Verification

| Step | Check | Pass criterion |
|---|---|---|
| 1 | Identification fields match register row | Exact match against `PACKAGE_REGISTER.csv` row 45 / `DELIVERABLE_REGISTER.csv` row 241 |
| 2 | Attributes verbatim | String match against register row 45 |
| 3 | Interface IDs preserved | All five PKG-043 IFC IDs present, applicability `YES`, disposition note present |
| 4 | Artifact IDs preserved | All nine DEL-043-02 ART IDs present |
| 5 | Conditions cited or `TBD` | No numeric value without source or `TBD` |
| 6 | Equipment items workbook-supported | Each tag traceable to workbook row 45 source slice or marked `TBD` |
| 7 | Vendor handoff coherent | EPC Integrator engineering lead review |
| 8 | Interface matrix minimum present | Five Gate 6 interface-type rows present |
| 9 | Disposition note carried | Disposition string matches `INTERFACE_REGISTER.csv` PKG-043 Notes |
| 10 | Cross-document consistency | Pass 2 sweep finds no unresolved inconsistency, or Conflict Table entry exists |
| 11 | Status transition safe | `_STATUS.md` shows `INITIALIZED` only if prior state was `OPEN`; History updated |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in the deliverable folder.
- `_STATUS.md` updated entry (when authorized).
- Run record at `_run_records/TASK_RUN_<timestamp>.md`.
- Future: workbook source extraction notes (TBD) and `MEMORY.md` entries for human rulings and conflict resolutions.
