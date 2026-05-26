# Procedure — DEL-084-01 Scope of Work (PKG-084 Fuel Gas Skid 3-25)

Operational procedure for producing the EPC Integrator Scope of Work artifact for PKG-084. Pass directive: P1_P2. Interpretation: steps describe how to produce the deliverable artifact (SOW document) from the locally available sources.

## Purpose

Produce the issued Scope of Work for `PKG-084 Fuel Gas Skid 3-25`, bounded to source-supported content from 26020-Package_Requirements.docx heading 37 and the 3-25 facility DBM, with TBD/CONFLICT items explicit. (Source: `_CONTEXT.md` Scope; `_REFERENCES.md`.)

## Prerequisites

- Read access to `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for this deliverable. (Source: `_CONTEXT.md`.)
- Access to source: `_Sources/26020-Package_Requirements.docx`, in particular heading 37 (`26020-02-PT-23-001 - Fuel Gas Skid`). (Source: `_REFERENCES.md`.)
- Access to source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, in particular §"## Fuel Gas" and §Utilities. (Source: `_REFERENCES.md`.)
- Access to interface table: `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 60 (note: source filename in package heading is `26020-Packages_Interfaces.3.xlsx`; see Conflict Table CFL-084-03). (Source: 26020-Package_Requirements.docx Physical Interface Summary; `_Sources/`.)
- Accepted upstream decomposition snapshot at `GATE-07_Final_Published_2026-05-24` (DELIVERABLE_REGISTER.csv, OBJECTIVE_SCOPE_MAP.csv). (Source: `_CONTEXT.md` Decomposition Reference.)
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md` during PREPARATION. (Source: `_DEPENDENCIES.md`.)
- No `_SEMANTIC_LENSING.md` exists yet; lensing-driven enrichment will be applied in a later P3_ONLY run. (Source: `_SEMANTIC.md` placeholder; skill `four-documents` Phase 2.5.)

## Steps

1. **Confirm preconditions.** Verify all files in §Prerequisites are accessible and that `_STATUS.md` Current State is `OPEN` or another `ALLOW_OVERWRITE_STATES` value. (Verification: read `_STATUS.md`; tool `tools/scaffolding/write_status.sh` will be invoked in Step 9.)
2. **Extract source section.** Open `_Sources/26020-Package_Requirements.docx` and isolate heading 37 (`26020-02-PT-23-001 - Fuel Gas Skid`). Capture the Location/Status, Source Basis, Basic Scope, Major Included Equipment, Scope Notes / Open Items, Physical Interface Summary, and Vendor Engineering Deliverables subsections verbatim into working notes.
3. **Extract facility integration context.** From `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, capture §"## Fuel Gas", §Utilities, and §"## Fuel-Gas Sulphur and Purge Hazard Basis" into working notes.
4. **Reconcile interface table.** Cross-walk the source Physical Interface Summary against `26020-Packages_Interfaces_4_export.xlsx` row 60; record any field-level mismatches as `location TBD` or as a new Conflict Table row.
5. **Draft SOW document body.** Compose the issued SOW with: (a) package identity and tagged equipment list per R-SOW-084-1; (b) process function per R-SOW-084-2; (c) design basis table per R-SOW-084-3; (d) heater control description per R-SOW-084-4; (e) scrubber sizing rule per R-SOW-084-5; (f) responsibility split per R-SOW-084-6; (g) facility integration narrative per R-SOW-084-7; (h) interface applicability table per R-SOW-084-8; (i) vendor document references per R-SOW-084-9; (j) traceability to SOW-0095..0098 per R-SOW-084-10; (k) Open Items register per R-SOW-084-11. (Source: `Specification.md`.)
6. **Apply guidance.** Apply `Guidance.md` §Principles, §Considerations, and §Trade-offs while drafting; do not back-fill TBDs or pre-decide CFL-084-01 (emergency buyback).
7. **Cross-document consistency check.** Verify terminology, equipment tags, and numeric values match across SOW prose, `Datasheet.md`, and `Specification.md`. Re-open source slices to resolve any inconsistency that cannot be resolved from drafts alone. (Source: skill `four-documents` Step 5.)
8. **Open-items capture.** Confirm the Open Items register lists heater capacity (TBD), final flow (TBD), MAWP (TBD), CFL-084-01 emergency buyback (needs human ruling), and any new items raised in Step 4 or Step 7. (Source: `Specification.md` R-SOW-084-11; `Guidance.md` Conflict Table.)
9. **Status update.** When this skill invocation completes Pass 1 and Pass 2 successfully and `_STATUS.md` is `OPEN`, invoke `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` to advance state to `INITIALIZED`. Do not regress state. (Source: skill `four-documents` Step 7.)
10. **Write run record.** Emit `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` capturing input echo, resolved state, tools used, outputs, and any TBD/CONFLICT items. (Source: agent `AGENT_TASK.md` Run record persistence.)

## Verification

| Step | Verification Check | Source / Notes |
|---|---|---|
| 1 | `_STATUS.md` Current State is within `ALLOW_OVERWRITE_STATES` (`OPEN, INITIALIZED`) | Brief `ALLOW_OVERWRITE_STATES` override |
| 2–3 | Working notes contain verbatim source extracts with file path + section label per claim | skill `four-documents` source-grounding rule |
| 4 | Each interface row in the SOW carries a source citation or `location TBD` | `Datasheet.md` §Physical Interface Summary |
| 5 | Every SOW requirement maps to one of R-SOW-084-1..11 | `Specification.md` §Requirements |
| 6 | No invented design values; ASSUMPTION labels carried where inference was used | skill `four-documents` Epistemic controls |
| 7 | Terminology and values match across all four documents | skill `four-documents` Step 5 |
| 8 | Open Items register present in SOW and mirrors `Specification.md` R-SOW-084-11 | `Specification.md` |
| 9 | `_STATUS.md` advanced to `INITIALIZED` only when state was `OPEN`; otherwise unchanged | skill `four-documents` Step 7 |
| 10 | Run record file written under `_run_records/` with required YAML frontmatter and body headings | `AGENT_TASK.md` Run-record file format |

## Records

The following records result from this procedure:

- `Datasheet.md` — identification, attributes, conditions, construction, interfaces, references.
- `Specification.md` — scope, requirements (R-SOW-084-1..11), standards, verification, documentation.
- `Guidance.md` — purpose, principles, considerations, trade-offs, Conflict Table.
- `Procedure.md` — this file.
- `_STATUS.md` — updated `OPEN` → `INITIALIZED` only when applicable.
- `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` — durable run record.
- (Downstream, out of this deliverable's scope) the issued SOW PDF/Word artifact produced from the four-document kit by a later deliverable execution task.
