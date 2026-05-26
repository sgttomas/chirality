# Procedure — DEL-084-02 Package Datasheet (PKG-084 Fuel Gas Skid 3-25)

> Operational procedure for **producing and issuing** the Package Datasheet artifact. (This is a production procedure for the EPC Integrator deliverable, not an operations procedure for the physical skid — the latter belongs in the vendor O&M scope under DEL-084-04.)

## Purpose

Produce a source-grounded, vendor-ready Package Datasheet for PKG-084 (LP Fuel Gas Skid) suitable for issue with `26020-02-PT-RFQ-23-001_FG_Skid_1.docx` and for transfer to the package vendor under DEL-084-04, satisfying requirements R-DS-1 through R-DS-11 in `Specification.md`.

## Prerequisites

### Documents

- `_CONTEXT.md` (read)
- `_REFERENCES.md` (read)
- `_DEPENDENCIES.md` (read)
- `_STATUS.md` (read; check current state is in `ALLOW_OVERWRITE_STATES`)
- Gate 7 snapshot (read):
  - `PACKAGE_REGISTER.csv` row PKG-084
  - `DELIVERABLE_REGISTER.csv` row DEL-084-02
  - `OBJECTIVE_DELIVERABLE_MAP.csv` / `OBJECTIVE_PACKAGE_MAP.csv` (objectives best-effort)
- Source slices (read; minimum):
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §Fuel Gas (L454-465), §Utility Integration Basis (L450-465)
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Fuel Gas Heating and Scrubbing" (L1872-1874), §Emergency Buyback (L1876-1878), §Utility table row "Fuel gas" (L1830)
- Source slices (best-effort, may be TBD/location TBD):
  - `_Sources/26020-Package_Requirements.docx` heading 37
  - `Bid Docs/Budgetary/26020-02-PT-RFQ-23-001_FG_Skid_1.docx`

### Declared upstream dependencies

Per `_DEPENDENCIES.md`: none declared at PREPARATION. Run `TASK + dependency-extract` separately if dependency tracking is required in-file.

### Tool

- `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` — for the OPEN → INITIALIZED state transition (Step 7 of `four-documents` skill).

## Steps

### Step 1 — Read context (always)

1. Read deliverable-local truth set: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`.
2. Read Gate 7 snapshot rows for PKG-084 and DEL-084-02.
3. Read source slices listed in Prerequisites.

### Step 2 — Establish DOMAIN (Pass 1)

- Discipline: Mechanical (`_CONTEXT.md`).
- Type: EPC Package Datasheet (`_CONTEXT.md`).
- Candidate standards: ASME Sec. VIII Div. 1 (scrubber), ASME B31.3 (piping), CSA/OGAOM siting (electric heater context only) — all `location TBD` per skill rule (clause text not locally accessible).

### Step 3 — Establish TASK (Pass 1)

- Subject: LP fuel gas heater + LP fuel gas scrubber (one shared skid).
- Service: low-pressure fuel gas distribution for stripping, blanketing, purge, drive gas, building heating, generator fuel.
- Constraints: source-bound values per Datasheet "Service / Process Attributes"; package boundary at skid edge; no detailed vendor engineering.

### Step 4 — Generate four documents (Pass 1)

Produce `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` per the schema in `four-documents/SKILL.md` Step 4 and the requirement set R-DS-1 through R-DS-11 in `Specification.md`. Carry all unsupported attributes as `TBD`. Label inferences `ASSUMPTION`.

### Step 5 — Cross-reference consistency check (Pass 2)

Verify that the four documents agree on:

- equipment composition (heater + scrubber, one of each);
- service-flow values (1.382 MMSCFD normal; > 1.5 MMSCFD design);
- supply pressure / MAWP table;
- scrubber K = 0.35 Imperial;
- heater electric / SCR-controlled, with skin-T override;
- conflict items (CF-01 through CF-05) are present in `Guidance.md` and referenced where impacted in `Datasheet.md` and `Specification.md`.

Open the Conflict Table in `Guidance.md` for unresolved items.

### Step 6 — Semantic lensing enrichment (Pass 3) — DEFERRED

`_SEMANTIC_LENSING.md` does not exist for this deliverable. This run executes `RUN_PASSES = P1_P2`; Pass 3 is intentionally skipped. ORCHESTRATOR Phase 2.5 (or a separate `RUN_PASSES = P3_ONLY` invocation) will perform Pass 3 after `lens-register` produces `_SEMANTIC_LENSING.md`.

### Step 7 — Update status (safe update only)

If `_STATUS.md` Current State is `OPEN`, run:

`tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`

If Current State is not `OPEN`, do not modify `_STATUS.md` (no state regression). Report status-update skipped.

## Verification

| Check | How | Pass criterion |
|---|---|---|
| Four documents exist | List `{DELIVERABLE_PATH}` | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` all present |
| Default schema sections present | Inspect each document | Datasheet (Identification, Attributes/Construction, Conditions, References); Specification (Scope, Requirements, Standards, Verification, Documentation); Guidance (Purpose, Principles, Considerations, Trade-offs, Examples); Procedure (Purpose, Prerequisites, Steps, Verification, Records) |
| Source-grounding | Spot-check non-trivial values | Cited to source slice (file + line/section) or marked `TBD` |
| Conflict Table | Inspect `Guidance.md` | CF-01..CF-05 present with required columns |
| Status update | Inspect `_STATUS.md` | If was `OPEN`: now `INITIALIZED`, history entry appended; otherwise unchanged |
| No out-of-scope writes | Inspect file modification list | Only files inside `{DELIVERABLE_PATH}` modified |
| Run record | Inspect `_run_records/` | `TASK_RUN_<timestamp>.md` present with frontmatter + body headings |

## Records

The following records result from a successful execution:

- `{DELIVERABLE_PATH}/Datasheet.md`
- `{DELIVERABLE_PATH}/Specification.md`
- `{DELIVERABLE_PATH}/Guidance.md`
- `{DELIVERABLE_PATH}/Procedure.md`
- `{DELIVERABLE_PATH}/_STATUS.md` — updated to `INITIALIZED` (safe update, if was `OPEN`)
- `{DELIVERABLE_PATH}/_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` — durable TASK run record

Subsequent passes (Pass 3 / semantic lensing enrichment) will produce additional run records under the same `_run_records/` folder and may update the four documents per `four-documents/SKILL.md` Step 6.
