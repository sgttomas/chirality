# Procedure — DEL-047-01 Scope of Work (PKG-047 Vapour Recovery Unit 4-25)

> Operational document. Describes the procedure to **produce** the Scope of Work deliverable artifact set. (The procedure to operate the VRU itself is a downstream vendor/operations deliverable and is out of scope here.)

## Purpose

Define the repeatable steps required to author, verify, and submit the EPC Integrator Scope of Work for PKG-047, satisfying SOW-0253..SOW-0256 and supporting objectives OBJ-001, OBJ-003..OBJ-010, with full source provenance and traceability to the accepted PROJECT_DECOMP Gate-07 snapshot.

## Prerequisites

### Declared upstream dependencies
- None declared in `_DEPENDENCIES.md` (no human-declared upstream edges as of 2026-05-24).

### Required references and inputs
- `_CONTEXT.md` for deliverable identity, scope items, objectives mapping, source pointers.
- `_REFERENCES.md` for the authoritative basis set.
- Accepted PROJECT_DECOMP Gate-07 snapshot:
  - `DELIVERABLE_REGISTER.csv` (row 570: DEL-047-01).
  - `PACKAGE_REGISTER.csv` (PKG-047 entry).
  - `OBJECTIVE_DELIVERABLE_MAP.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`.
- Locally accessible source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — primary technical basis (especially §Vapour Recovery Unit lines 1681-1791 and adjacent SOC/integration sections).
- Source documents pending extraction (`location TBD` for cited content): `_Sources/26020-Package_Requirements.docx` heading 2; `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 101.

### Permissions
- Write scope limited to `{DELIVERABLE_PATH}` (the deliverable folder).
- `_STATUS.md` writable only via `tools/scaffolding/write_status.sh` and only for safe `OPEN → INITIALIZED` transition (per skill Step 7).
- `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, `_SEMANTIC.md` are read-only here.

## Steps

### Step 1 — Read deliverable-local truth set
Read `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_SEMANTIC.md` (if present). Confirm `Current State` is in `ALLOW_OVERWRITE_STATES` (`OPEN, INITIALIZED`). If not, abort with `SKIPPED_PROTECT_HUMAN_WORK`.

### Step 2 — Identify and read the decomposition row
Locate the DEL-047-01 row in `DELIVERABLE_REGISTER.csv` (row 570) and the PKG-047 row in `PACKAGE_REGISTER.csv`. Record the cross-references and the declared scope-item / objective coverage.

### Step 3 — Open and slice authoritative sources
Open `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`. Read the relevant slices:
- §Vapour Recovery Unit (lines 1681-1791) — primary VRU basis.
- §SEC-04 Inlet, Separation, Stabilization, Stabilizer Overheads (lines 569 ff) — upstream interfaces and SOC tie-in.
- §SEC-07 Sales Gas, NGL Treating, Product Handling, Vapor Recovery (lines 1397 ff) — adjacent product/handling context.
- Compressor packing-drain/vent recovery references (lines 928, 967, 1029, 1074) — secondary VRU sources.
- TEG and amine-tank vapour routing rows (lines 1227, 1232, 1373, 1562, 1663).
- VRU row in SOC interfaces table (line 750).

Note any locally inaccessible sources (workbook, package-requirements docx) as `MISSING:` and propagate as `location TBD` for cited claims.

### Step 4 — Draft Datasheet
Populate Identification (from `_CONTEXT.md`), Attributes (package function, sparing, compressor type, housing, discharge routing), Design Conditions (pressures, capacity, drivers, MAWP, cooler/dewpoint table, inlet-pressure setpoint table), Construction (scrubbers, coolers, blowdown, recycle, make-up gas, header-to-flare, sweep/purge), Inlet Composition, Gas Sources, Boundaries, Tagged Equipment List (`TBD`), Responsibility Assignment Record, References. Cite source slice on every non-trivial value.

### Step 5 — Draft Specification
Define Scope (in/out), then enumerate normative requirements REQ-VRU-001..REQ-VRU-017 with one-line source citations and per-requirement verification approaches. List Standards (with explicit `ASSUMPTION` labels where inferred). Map requirements to Documentation outputs.

### Step 6 — Draft Guidance
Write Purpose, Principles, Considerations (condensation risk, sour composition, tank-farm pressure control, cross-facility coupling, BTEX recovery), Trade-offs, Examples. Surface unresolved items in the Conflict Table.

### Step 7 — Draft this Procedure
(This document.) Describe the production procedure, prerequisites, steps, verification, records.

### Step 8 — Cross-document consistency check
Run the checks listed in §Verification below. Reconcile any inconsistencies; if not resolvable from drafts alone, re-open source slices. If still unresolved, add to the Conflict Table in `Guidance.md` and mark `TBD` rather than guess.

### Step 9 — Safe status update
If `_STATUS.md` `Current State` is `OPEN`, invoke:

```
bash tools/scaffolding/write_status.sh \
  /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/PKG-047_Vapour-Recovery-Unit-4-25/1_Working/DEL-047-01_scope-of-work_Scope-of-Work \
  INITIALIZED TASK+four-documents
```

Do not modify `_STATUS.md` directly.

### Step 10 — Write run record
Write `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` per `AGENT_TASK` run-record schema (YAML frontmatter + Markdown body). Set `run-status: SUCCESS` on QA pass.

## Verification

| Check | Pass criterion |
|---|---|
| Four documents exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` present in deliverable folder |
| Default schema sections present | Datasheet (Identification, Attributes, Conditions, Construction, References); Specification (Scope, Requirements, Standards, Verification, Documentation); Guidance (Purpose, Principles, Considerations, Trade-offs, Examples); Procedure (Purpose, Prerequisites, Steps, Verification, Records) |
| Source grounding | All non-trivial values cite source slice (`SourcePath` + `SectionRef`) or `location TBD` |
| Assumptions labeled | All inferences carry `ASSUMPTION:` label |
| TBD discipline | Unknowns are `TBD` rather than invented values |
| Cross-document consistency | Equipment counts (2 x 100%), pressures (0.9 kPag suction, 483 kPag discharge), MAWP (552 / 1,034 kPag), compressor model (Ro-Flo 17S / 217M), voltage (4,000 V), discharge target (SOC first-stage suction) match across all four documents |
| Conflict capture | CT-01..CT-06 captured in `Guidance.md` |
| Scope coverage | SOW-0253, SOW-0254, SOW-0255, SOW-0256 explicitly addressed in Specification §Scope and REQ-VRU-017 |
| Objective coverage | OBJ-001, OBJ-003..OBJ-010 traced in Records §Coverage Matrix below |
| `_STATUS.md` discipline | No state regression; modified only via `write_status.sh`; or skipped with reason |
| Run record present | `_run_records/TASK_RUN_*.md` written |

## Records

### Coverage Matrix — SOW items

| SOW item | Where addressed | Notes |
|---|---|---|
| SOW-0253 | Datasheet §Identification, §Attributes; Specification §Scope; REQ-VRU-001..017 | Package scope of work |
| SOW-0254 | Datasheet §Attributes, §Construction; REQ-VRU-001..016 | Tagged equipment and package identity list (tag numbers `TBD`) |
| SOW-0255 | Datasheet §Attributes, §Boundaries; Guidance §Purpose, §Principles; REQ-VRU-015, REQ-VRU-016, REQ-VRU-017 | Package function and integration narrative |
| SOW-0256 | Datasheet §Responsibility Assignment Record; REQ-VRU-017 item 7 | Responsibility assignment record |

(`ASSUMPTION:` SOW-0253..0256 each align 1:1 to one of the four anticipated artifacts as listed; literal-text verification against `_Sources/26020-Package_Requirements.docx` is `TBD` per Conflict CT-06.)

### Coverage Matrix — Objectives

| Objective | How this deliverable supports it (ASSUMPTION — package-heuristic, per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`) |
|---|---|
| OBJ-001 | Establishes EPC package scope for VRU as part of 04-25 plant build-out |
| OBJ-003..OBJ-010 | Scope coverage at package level; objective-level confirmation deferred to human ruling — see decomposition `OBJECTIVE_DELIVERABLE_MAP.csv` |

### Document outputs produced

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` (safe-update only: `OPEN → INITIALIZED`)
- `_run_records/TASK_RUN_<timestamp>.md`

### Source-reread log (Pass 2 consistency sweep, this run)

| Source slice | Reason re-opened | Outcome |
|---|---|---|
| DBM lines 1681-1791 (§Vapour Recovery Unit) | Anchor for all requirements and design values | Confirmed values used in Datasheet and Specification; numeric consistency PASS |
| DBM line 1683 (discharge routing) | Cross-check Datasheet §Boundaries, Specification REQ-VRU-015, Guidance §Cross-Facility Coupling | Consistent |
| DBM lines 1722-1730 (setpoint ladder) | Cross-check Datasheet §Setpoint table, Specification REQ-VRU-009, Guidance §Examples | Consistent |
| DBM lines 1232, 1562, 1663, 1373 (VRU header connectivity exclusions/inclusions) | Cross-check Datasheet §Boundaries and Specification REQ-VRU-016 | Consistent |
| DBM lines 928, 967, 1029, 1074 (seal-pot vapour recovery to VRU header) | Establish secondary upstream sources | Consistent |
| DBM line 1698 (motor power conflict) | Verify literal-text wording of conflict | Recorded as CT-01 |
