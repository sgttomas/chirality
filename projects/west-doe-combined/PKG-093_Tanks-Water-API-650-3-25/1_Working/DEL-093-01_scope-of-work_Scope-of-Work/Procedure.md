# Procedure — DEL-093-01 Scope of Work (PKG-093 Tanks, Water (API 650) 3-25)

## Purpose

Operational procedure to produce, maintain, and hand off the DEL-093-01 Scope of Work artifact set. This procedure addresses both producing the deliverable (drafting the Scope of Work content) and using the deliverable (the EPC Integrator's use of the SOW to engage the Package Vendor and govern integration). (Source: `_CONTEXT.md`; SKILL Method §4d.)

## Prerequisites

1. Accepted Gate-7 PROJECT_DECOMP snapshot is available at the path recorded in `_REFERENCES.md`.
2. SCOPE_LEDGER.csv rows SOW-0229..SOW-0232 are accessible.
3. PACKAGE_REGISTER.csv row PKG-093 is accessible.
4. DBM source material (DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md) is locally accessible, including the Produced-Water Storage, Treatment, and Transfer section.
5. Companion deliverables DEL-093-02 through DEL-093-06 exist as siblings under `PKG-093_Tanks-Water-API-650-3-25/1_Working/` for downstream consumption.
6. `_DEPENDENCIES.md` declared dependencies have been reviewed (currently none declared).

No human input is required during execution; epistemic uncertainty is captured as TBD/ASSUMPTION/CONFLICT and surfaced in `Guidance.md` for downstream ruling.

## Steps

### Step P-01 — Read context

Read `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for this deliverable. Extract identity, scope, anticipated artifacts, package assignment, and any declared dependencies.

### Step P-02 — Read decomposition truth

Read PACKAGE_REGISTER.csv (row PKG-093), DELIVERABLE_REGISTER.csv (row DEL-093-01), and SCOPE_LEDGER.csv (rows SOW-0229..SOW-0232) from the Gate-7 snapshot. Extract: package name, basic scope, major included equipment, scope notes, and excluded items.

### Step P-03 — Read source slice

Open DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md and read the Produced-Water Storage, Treatment, and Transfer section. Extract: tank counts, allocation between sour and sweet, code basis, coating, SG values, transfer pump arrangement, and integration into the 03-25 Liquids Hub.

### Step P-04 — Draft Datasheet

Populate the Datasheet identification, attributes, conditions, and construction sections from the SCOPE_LEDGER rows and the DBM section. Mark all source-incomplete items as TBD.

### Step P-05 — Draft Specification

Translate the SCOPE_LEDGER text and DBM source slices into normative REQ-093-01-NN statements, each citing the source. Provide a verification approach for every requirement.

### Step P-06 — Draft Guidance

Capture principles, considerations, trade-offs, and the Conflict Table. Every CT-NN row must identify both source positions and a proposed authority. Do not resolve conflicts unilaterally.

### Step P-07 — Cross-document consistency sweep

Verify that tag names, capacities, design conditions, and SG values are consistent across the four documents. Where sources disagree, prefer TBD and a Conflict Table entry over picking a value.

### Step P-08 — Status update

If the current state in `_STATUS.md` is OPEN, update to INITIALIZED. If the state is anything else, do not modify.

### Step P-09 — Run record

Write `_run_records/TASK_RUN_<timestamp>.md` capturing brief inputs, resolved skill, sources read, outputs produced, conflicts surfaced, and final status.

## Verification

| Check | Pass condition |
|---|---|
| All four documents exist with the default schema sections | Files present; default section headings present |
| Each non-trivial value or requirement cites a source | Source path or `location TBD` recorded |
| TBD / ASSUMPTION / CONFLICT items are surfaced, not invented | Guidance.md Conflict Table contains all unresolved items |
| Terminology consistent across documents | Tank tags TK-9060-2 / TK-9070-2, "modified API 650", "Devchem 253", "Kennilworth-type HCL float skim" used consistently |
| Status update is safe | OPEN -> INITIALIZED only; otherwise no change |

## Records

- Updated four-document set at `{DELIVERABLE_PATH}/`
- Updated `_STATUS.md` (when state was OPEN)
- New run record at `{DELIVERABLE_PATH}/_run_records/TASK_RUN_<timestamp>.md`
- Conflict Table entries CT-01..CT-05 in `Guidance.md` awaiting human ruling
