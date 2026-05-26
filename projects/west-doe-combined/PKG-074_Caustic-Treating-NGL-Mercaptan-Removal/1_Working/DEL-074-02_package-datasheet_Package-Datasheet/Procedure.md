# Procedure — Package Datasheet (PKG-074 Caustic Treating, NGL Mercaptan Removal)

**Interpretation:** This Procedure describes the steps to **produce** the Package Datasheet artifact (the deliverable). It does not prescribe field operating procedures for the caustic package itself.

## Purpose

Produce a source-grounded, EPC-handoff-ready Package Datasheet for PKG-074 that:
- conveys the non-regenerative caustic NGL mercaptan treating design basis to a third-party proprietary process provider,
- conveys facility-side integration constraints to the EPC Integrator,
- and is traceable to authoritative source slices (DBM-Deepcut, PACKAGE_REGISTER, Word/Workbook package row).

## Prerequisites

- Read access to deliverable folder `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.
- Read access to the accepted decomposition snapshot (Gate 7) including `PACKAGE_REGISTER.csv` row 51, `DELIVERABLE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Read access to source materials under `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/`, in particular `DBM-Deepcut/4-25_Deepcut_DBM.md` (sections `## Current-Scope NGL Mercaptan Treating`, lines 1509-1572).
- (Optional) Parsed extract of `26020-Package_Requirements.docx` package heading 28 and `26020-Packages_Interfaces_4_export.xlsx` Packages row 51. (Not parsed locally for this run; location TBD within those files.)
- `_STATUS.md` Current State must be in `ALLOW_OVERWRITE_STATES` (`OPEN, INITIALIZED`).
- No declared upstream dependencies require closure (per `_DEPENDENCIES.md`).

## Steps

1. **Confirm scope and identity.** Read `_CONTEXT.md` and extract DeliverableID, Parent Package ID, package tag, discipline, scope statement, anticipated artifacts, and covered scope items/objectives.
2. **Confirm decomposition basis.** Open the Gate 7 PACKAGE_REGISTER row 51 (PKG-074, Workbook row 51, Equipment tag 26020-01-PT-27-002) and confirm package name, vendor/integrator split, interface-type set, and source pointers (`26020-Package_Requirements.docx` package heading 28; `26020-Packages_Interfaces_4_export.xlsx` Packages row 51; DBM-Deepcut/4-25_Deepcut_DBM.md).
3. **Read authoritative source slices.** In `DBM-Deepcut/4-25_Deepcut_DBM.md`, read the source slices that scope this package:
   - `## Current-Scope NGL Mercaptan Treating` (lines 1509-1572), including the design-parameter table (1517-1530), extraction-stage table (1532-1537), and sulphur-case table (1539-1546).
   - De-ethanizer-to-package interface (lines 1337-1338).
   - Waste streams (lines 526-532).
   - Pressurized caustic drain drum SOC inlet entry (lines 748, 760).
4. **Populate `Datasheet.md`.** Fill Identification from `_CONTEXT.md` and PACKAGE_REGISTER row 51; populate Attributes, Conditions, and Construction tables from the source slices above with explicit `SourcePath + SectionRef/line` citations. Mark every parameter that the source labels TBC/TBD as `TBD`. Label inferences `ASSUMPTION`.
5. **Populate `Specification.md`.** Translate the datasheet content into normative requirements R-001..R-016, each with a source citation and an epistemic label (FACT, ASSUMPTION, PROPOSAL, TBD). Populate Standards, Verification, and Documentation sections; mark standards `location TBD` when not extractable from the locally accessible sources.
6. **Populate `Guidance.md`.** Capture Purpose, Principles, Considerations, Trade-offs, and Examples grounded in the same source slices. Open a Conflict Table for any unresolved discrepancies (objective mapping, exclusions completeness, references-vs-actual-availability).
7. **Cross-document consistency sweep (Pass 2).** Verify:
   - Datasheet attributes/conditions/construction items each have a corresponding requirement in Specification (or are explicitly informational).
   - Specification requirements have rationale or trade-off coverage in Guidance and a verification entry under Verification.
   - Terminology (e.g., "non-regenerative caustic treating", "C3+ NGL", "de-ethanizer", "SOC first-stage suction") is consistent across all four documents.
   - Numeric values and units (2,385 m3/d; 2,213/1,978 kPag; 26.7/43.3/48.8 deg C; 50 wt% NaOH; 14.7 wt% NaOH; 970 ppmw S; 203.7 ppmw S; 400 bbl) are identical across documents.
8. **Resolve or escalate conflicts.** Where consistency cannot be achieved from drafts alone, re-open the source slice; if still unresolved, record in the Guidance Conflict Table with a PROPOSAL and `Human ruling: TBD`.
9. **Safe `_STATUS.md` update.** If current state is `OPEN`, transition to `INITIALIZED` via `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. If not `OPEN`, do not modify `_STATUS.md`.
10. **Write run record.** Persist a TASK run record at `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` per `agents/AGENT_TASK.md`.

## Verification

| Check | Pass criterion |
|---|---|
| Four documents present | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` all exist in `{DELIVERABLE_PATH}` |
| Default schema sections present | Each document carries the default headings from the skill schema |
| Source-grounded values | All non-trivial numeric values cite `SourcePath` + section/line, or are `TBD` |
| Cross-document consistency | Terminology and values match across the four documents |
| Status transition | `_STATUS.md` shows `OPEN -> INITIALIZED` only when prior state was `OPEN` |
| Run record | `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` exists with required frontmatter and headings |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`
- Updated `_STATUS.md` (if state transitioned)
- Run record under `_run_records/`
- Conflict Table entries in `Guidance.md` for any unresolved discrepancies
