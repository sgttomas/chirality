# Procedure — DEL-047-02 Package Datasheet (Vapour Recovery Unit 4-25)

> Operational procedure for **producing** the EPC Package Datasheet artifact for PKG-047. Source-grounded against DBM-Deepcut. Steps that depend on inaccessible binary sources or on detailed-engineering inputs are marked `TBD`.

## Purpose

Define the repeatable steps the EPC Integrator follows to build, validate, and issue the PKG-047 Package Datasheet for third-party vendor / discipline engineering handoff.

## Prerequisites

### Declared upstream dependencies
- None declared in `_DEPENDENCIES.md` (PREPARATION state). Coordination mode is DECLARED with no edges.

### Effective evidence dependencies (from authority hierarchy)
- Accepted upstream decomposition snapshot: GATE-07 PROJECT_DECOMP (`/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`).
- Deliverable register row `DEL-047-02_package-datasheet` (covers, supports-objectives, source reference).
- Source materials referenced by the row:
  - DBM-Deepcut `4-25_Deepcut_DBM.md` — accessible; §Vapour Recovery Unit is primary source slice; multiple interface mentions elsewhere.
  - 26020-Package_Requirements.docx package heading 2 — listed; binary not extracted; `location TBD`.
  - 26020-Packages_Interfaces_4_export.xlsx — listed; binary not extracted; `location TBD`.
- Sibling deliverable `DEL-047-01_scope-of-work` (informational; not yet drafted, decomposition row present).
- Sibling deliverable `DEL-047-04_vendor-engineered-equipment-package` (informational; vendor production unit consuming this datasheet).

### Required tooling / access
- Local repo access to deliverable folder and `_Sources/`.
- `tools/scaffolding/write_status.sh` for safe `_STATUS.md` update.
- Optional: docx/xlsx extraction utility for the two binary sources (TBD).

## Steps

1. **Read deliverable-local truth set.** Read `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`. Confirm `_STATUS.md` Current State is `OPEN` or `INITIALIZED`; otherwise stop and protect human work.
2. **Locate authoritative source slices.** Identify the deliverable in the decomposition register; read the deliverable narrative; map the source-reference column to files under `_Sources/`. Confirm which sources are locally accessible.
3. **Extract the package source slice.** From DBM-Deepcut, read §Vapour Recovery Unit in full; identify interface mentions in §SOC, §Booster, §Acid Gas Compression, §TEG dehydration, §Caustic Storage, §Condensate Storage; collect every parameter table and the inlet-pressure action table.
4. **Populate Datasheet identification, attributes, conditions, construction, references.** Use values directly from source slices; mark missing values `TBD` or `TBC` consistent with source language. Carry interface facts as evidence per `_CONTEXT.md` Notes.
5. **Derive Specification requirements.** For each design-relevant statement in the source slice, write a normative requirement (REQ-VRU-###) traceable to the source location. Mark assumptions explicitly.
6. **Map verification approaches.** For each REQ, define a vendor- or site-side verification mechanism (drawing review, performance test, loop check, hydrotest, walkdown, etc.).
7. **List governing standards.** Capture standards explicitly named in source slices (e.g., OGAOM §9.6.15, API 2000); add `location TBD` for standards that are implied by service but not named in the extracted slice (e.g., NACE MR0175).
8. **Write Guidance.** Capture principles, considerations, trade-offs grounded in the source slice; build the Conflict Table from items the source explicitly flags as TBC/TBD or where the source itself disagrees (e.g., 200 hp vs 300 hp).
9. **Cross-check consistency.** Confirm Datasheet attributes, Specification requirements, Guidance considerations, and Procedure prerequisites use the same terms, numeric values, and units. Reconcile or capture conflicts.
10. **Mark closing assumptions.** Any inferred content (e.g., NACE applicability, sour-service classification, building HVAC) labelled `ASSUMPTION` with the basis for inference.
11. **Run safe status update.** If `_STATUS.md` Current State is `OPEN` and Pass 1/Pass 2 ran, execute `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. Otherwise skip and record skip reason.
12. **Write run record.** Create `_run_records/TASK_RUN_<timestamp>.md` capturing inputs, resolved skill state, tools used, applied changes, missing items, and human-ruling requests.

## Verification

| Check | How |
|---|---|
| All four documents exist | `ls Datasheet.md Specification.md Guidance.md Procedure.md` |
| Default schema sections present | Manual heading review against `SKILL.md` Step 2 schema table |
| Every non-trivial value cites a source or carries `TBD` / `ASSUMPTION` | Inspection of Attributes/Conditions/Construction tables and Specification requirements |
| Inlet-pressure action table matches source exactly | Compare to DBM §VRU Configuration |
| Interface matrix in Datasheet aligns with all DBM interface mentions cited | Diff against grep for "VRU" in DBM-Deepcut |
| Conflict Table captures explicit source TBC items and the 200/300 hp disagreement | Review Guidance §Conflict Table |
| `_STATUS.md` updated only when current state was `OPEN`; no regression | Inspect `_STATUS.md` after Step 11 |
| Run record present in `_run_records/` with required headings | Inspect run-record file |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` — the four-document set produced by this procedure.
- `_STATUS.md` updated to `INITIALIZED` (when prerequisites met).
- `_run_records/TASK_RUN_<timestamp>.md` — input echo, resolved skill state, tools used, applied changes, missing items, human rulings requested.
- Decomposition register row remains untouched; this procedure does not modify decomposition snapshots.
