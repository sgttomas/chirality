# Procedure — DEL-091-01 Scope of Work (PKG-091 Tank Farm Pump Building 3-25)

> Operational procedure for producing and maintaining the EPC Integrator Scope
> of Work deliverable for PKG-091. This procedure governs how the deliverable
> is drafted, reviewed against source, and updated as later sibling deliverables
> (DEL-091-02 through DEL-091-06) resolve open items.

## Purpose

To produce the package Scope of Work narrative satisfying `Specification.md`
requirements R1–R8, against the accepted GATE-07 PROJECT_DECOMP snapshot, with
explicit traceability to `SCOPE_LEDGER.csv`, `PACKAGE_REGISTER.csv`, and
`INTERFACE_REGISTER.csv` rows for PKG-091.

## Prerequisites

### Inputs

- `_CONTEXT.md` (this deliverable folder) — deliverable identity, scope items,
  supported objectives, decomposition pointer.
- `_REFERENCES.md` — authoritative decomposition basis and shared source root.
- `_DEPENDENCIES.md` — declared upstream/downstream lists (none declared at
  PREPARATION; carry as `none` and update only if the human owner declares).
- GATE-07 PROJECT_DECOMP snapshot (read-only):
  - `DELIVERABLE_REGISTER.csv` — DEL-091-01_scope-of-work row.
  - `PACKAGE_REGISTER.csv` — PKG-091 row.
  - `SCOPE_LEDGER.csv` — SOW-0185, SOW-0186, SOW-0187, SOW-0188.
  - `INTERFACE_REGISTER.csv` — 15 PKG-091 rows.
  - `OBJECTIVE_DELIVERABLE_MAP.csv` — DEL-091-01 → OBJ-002…OBJ-010.
- `Datasheet.md` (this folder) — descriptive package identity and parameters.
- `Specification.md` (this folder) — normative requirements.
- `Guidance.md` (this folder) — interpretation, trade-offs, conflict table.

### Reference materials known but not locally accessible

- `_Sources/26020-Package_Requirements.docx` heading 44.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 84.
- API-682 (mechanical seal standard; cited by source).

### Roles

- **Author (EPC Integrator):** drafts the narrative, populates the tagged
  equipment list and integration narrative, owns `TBD`/`TBC` carry-forward.
- **Reviewer (EPC Integrator lead):** checks source fidelity, interface coverage,
  and absence of duplication with DEL-091-02 through DEL-091-06.
- **Human owner:** rules on items in the `Guidance.md` Conflict Table and
  confirms the `PACKAGE_HEURISTIC` objective association.

## Steps

### Step 1 — Confirm preconditions

1. Read `_STATUS.md`. Proceed only when current state is in
   `ALLOW_OVERWRITE_STATES` (`OPEN`, `INITIALIZED`, `SEMANTIC_READY`).
2. Confirm the GATE-07 snapshot path in `_REFERENCES.md` matches the snapshot
   used (`GATE-07_Final_Published_2026-05-24`).
3. Confirm `_CONTEXT.md` lists scope items SOW-0185, SOW-0186, SOW-0187,
   SOW-0188 and objectives OBJ-002…OBJ-010.

### Step 2 — Load source slices

1. Open `SCOPE_LEDGER.csv` and isolate rows SOW-0185, SOW-0186, SOW-0187,
   SOW-0188.
2. Open `PACKAGE_REGISTER.csv` and isolate row PKG-091.
3. Open `INTERFACE_REGISTER.csv` and isolate the 15 PKG-091 rows.
4. Open `OBJECTIVE_DELIVERABLE_MAP.csv` and isolate DEL-091-01 rows.
5. Record any source slice that is referenced but not locally accessible
   (Word, Excel, API-682) as `location TBD` in `Specification.md` Standards.

### Step 3 — Draft Identification and Function

1. Populate the Scope of Work identification block from `_CONTEXT.md` and
   `PACKAGE_REGISTER.csv` (tracking number, WBS, discipline, workbook row).
2. Draft the process function paragraph using only the wording in SCOPE_LEDGER
   SOW-0186 (with mechanical normalization for grammar and units).

### Step 4 — Draft Tagged Equipment List

1. For each pump tag in SOW-0187 (P-9295-2, P-9290/9293-2, P-9215/9216-2,
   P-9210/9220-2, P-9200-2, P-9230-2, P-9211/9221-2, P-9240-2), record: type,
   seal plan (where stated), power, voltage/phase/frequency (where stated),
   and rated point (from SOW-0188 where stated).
2. Where a parameter is not stated in the source slice, mark `TBC` or `TBD`
   and do not infer a value.
3. Add a row pointing to DEL-091-02 Package Datasheet for per-tag detailed
   datasheets (ASSUMPTION recorded in `Specification.md` R3.2).

### Step 5 — Draft Drivers and "By Others"

1. State the 575 V / 3 Ph / 60 Hz, DOL/VFD starting, 600 V MCC source, and
   -40 °C motor sizing basis from SOW-0188.
2. State the "by others" exclusions (DCS integration, foundations, electrical
   supply to MCC) from SOW-0188.

### Step 6 — Draft Boundary and Responsibility Split

1. Copy the responsibility split text from `PACKAGE_REGISTER.csv`
   ResponsibilityModel (Package Vendor vs. EPC Integrator).
2. Record the package tracking number and Word-source heading as the source
   basis citation.

### Step 7 — Draft Whole-Facility Integration Narrative

1. For each of the 15 interface types in `INTERFACE_REGISTER.csv` for PKG-091,
   write one paragraph or row identifying the EPC-owned tie-in/integration
   scope at the package battery limit.
2. For each "by others" item (DCS integration, foundations, electrical supply
   to MCC), explicitly cross-link it to the matching interface type
   (I&C / Control Cabling, Structural / Foundations / Supports, Electrical
   Power respectively) so the integration scope is unambiguous.
3. Where interface-specific tie-in detail is not stated in the GATE-07
   register row, mark the depth-of-narrative item `TBD`.

### Step 8 — Draft Objectives Traceability

1. Record OBJ-002…OBJ-010 as supported objectives.
2. Mark the association as `ASSUMPTION (PACKAGE_HEURISTIC)` per `Guidance.md`.

### Step 9 — Cross-check against sibling deliverables

1. Confirm the Scope of Work does not duplicate per-tag datasheet content
   (defer to DEL-091-02).
2. Confirm it does not duplicate construction installation content (defer to
   DEL-091-03).
3. Confirm it does not duplicate vendor engineering content (defer to
   DEL-091-04 and DEL-091-05).
4. Confirm acceptance criteria are not invented here (defer to DEL-091-06).

### Step 10 — Pass 2 cross-document consistency

1. Compare entity names, tag numbers, units, and values between `Datasheet.md`,
   `Specification.md`, `Guidance.md`, and the Scope of Work narrative.
2. Resolve any inconsistency by re-opening the SCOPE_LEDGER row that supports
   the value; do not resolve by inference.
3. If a contradiction cannot be resolved from the registers, add a row to the
   `Guidance.md` Conflict Table.

### Step 11 — Pass 3 (semantic lensing)

1. Run only when `_SEMANTIC_LENSING.md` exists for this deliverable.
2. For each warranted item, re-read the target document section, the source
   slice that supports the change, and sibling sections implicated.
3. Record disposition (incorporated, already covered, converted to `TBD`,
   surfaced as a conflict, or rejected with reason) per `SKILL.md` Step 6.
4. This Pass 3 is out of scope for the current run (`RUN_PASSES = P1_P2`).

### Step 12 — Status update

1. If `RUN_PASSES` includes Pass 1 or Pass 2 and the current `_STATUS.md`
   state is `OPEN`, run:
   `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`
2. Do not regress state. If state is not `OPEN`, leave `_STATUS.md` unchanged
   and record the skip in the run record.

## Verification

| Check | Method | Acceptance |
|---|---|---|
| All four documents exist after the run | Directory listing | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` all present |
| Default schema sections present in each document | Inspection | Identification/Attributes/Conditions/Construction/References (Datasheet); Scope/Requirements/Standards/Verification/Documentation (Specification); Purpose/Principles/Considerations/Trade-offs/Examples (Guidance); Purpose/Prerequisites/Steps/Verification/Records (Procedure) |
| Each non-trivial requirement traces to a SCOPE_LEDGER, PACKAGE_REGISTER, or INTERFACE_REGISTER row | Cross-reference | At least one explicit row citation per non-`TBD`/`TBC` requirement |
| All `TBD`/`TBC` items echo source-stated openness or label inferences | Inspection | No bare values without source; no source-stated `TBC` silently resolved |
| Cross-document consistency for tags, units, and values | Comparison | Identical strings for the same entity across documents |
| `_STATUS.md` transition is `OPEN → INITIALIZED` or skipped with reason | Inspection | History entry added by `write_status.sh` or skip noted in run record |

## Records

The following records result from this procedure:

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this
  deliverable folder) — the four-document kit.
- `_STATUS.md` — updated to `INITIALIZED` (when Pass 1/2 runs and prior state
  is `OPEN`).
- `_run_records/TASK_RUN_<timestamp>.md` — durable run record produced by the
  TASK shell, including resolved skill version, companion files, tools used,
  outputs, and any missing items or needed rulings.
- Optional: `Guidance.md` Conflict Table entries when contradictions are
  found that cannot be resolved from the registers.
