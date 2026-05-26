# Procedure: DEL-076-01 — Scope of Work (Lube Oil Supply)

Pass: P1 (initial draft); Pass 2 consistency sweep applied.

**Interpretation:** This procedure describes the steps to **produce** the Scope of Work artifact for PKG-076. Operating the lube-oil package itself is out of scope for this deliverable.

## Purpose

Produce the EPC Integrator Scope of Work for PKG-076 (Lube Oil Supply) such that:

- all twelve specification requirements (R-01 through R-12) are satisfied,
- all five artifact rows in `ARTIFACT_REGISTER.csv` rows 4033-4037 are produced,
- all four scope items (SOW-0135..SOW-0138) are demonstrably covered,
- source citations are preserved and unresolved items are surfaced as `TBD`.

## Prerequisites

| Prerequisite | Source | Status |
|---|---|---|
| `_CONTEXT.md` present and complete | `_CONTEXT.md` | Present |
| `_REFERENCES.md` present | `_REFERENCES.md` | Present |
| `_DEPENDENCIES.md` present | `_DEPENDENCIES.md` | Present; no upstream/downstream declared |
| `_STATUS.md` in an overwrite-allowed state | `_STATUS.md` | OPEN at run start |
| Access to GATE-07 decomposition snapshot | `_REFERENCES.md` Authoritative Decomposition Basis | Accessible |
| Access to `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | shared source root | Accessible |
| Access to `_Sources/26020-Package_Requirements.docx` heading 30 text | shared source root | File present (binary); text-extracted slice `TBD` (not text-readable in workspace) |
| Access to `Bid Docs/Budgetary/26020-01-PT-RFQ-29-001-Lube oil supply.docx` | `PACKAGE_REGISTER.csv` row 70 | Not present in accessible workspace |

## Steps

### Step 1 — Confirm deliverable identity and overwrite safety

- Read `_STATUS.md`.
- If `Current State` is not in `ALLOW_OVERWRITE_STATES` (OPEN, INITIALIZED), STOP and return `SKIPPED_PROTECT_HUMAN_WORK`.
- Verify `_CONTEXT.md` DeliverableID matches `DEL-076-01_scope-of-work`.

Verification: identity block in Datasheet matches `_CONTEXT.md`.

### Step 2 — Pull authoritative source slices

For PKG-076, read:

1. `PACKAGE_REGISTER.csv` row 70 (full Responsibility + Description + Source Basis text).
2. `DELIVERABLE_REGISTER.csv` rows 384-389 (DEL-076-01 plus sibling deliverables for downstream pointers).
3. `SCOPE_LEDGER.csv` rows 136-139 (SOW-0135..SOW-0138).
4. `INTERFACE_REGISTER.csv` rows 557-564 (all eight interface IDs for PKG-076).
5. `ARTIFACT_REGISTER.csv` rows 4033-4037 (the five expected SoW artifacts).
6. `OBJECTIVE_REGISTER.csv` rows for OBJ-001/004/005/006/007/008/009/010.
7. `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` "Lube Oil Storage and Pump Basis" section.
8. (If text becomes available) `_Sources/26020-Package_Requirements.docx` heading 30.

Verification: each source slice is logged in `## References` of the Datasheet.

### Step 3 — Draft Datasheet (identification, attributes, tagged equipment, conditions, interfaces)

- Populate Identification block from `_CONTEXT.md` and `PACKAGE_REGISTER.csv` row 70.
- Populate Tagged Equipment table from `SCOPE_LEDGER.csv` SOW-0137 + DBM tag identifiers (P-9240-1, P-9250-1).
- Populate Conditions table from `SCOPE_LEDGER.csv` SOW-0138; mark heated-tank set point `TBD`.
- Populate Construction / Battery-Limit table from `SCOPE_LEDGER.csv` SOW-0138.
- Populate Interface table from `INTERFACE_REGISTER.csv` rows 557-564.

Verification: every row carries a source pointer.

### Step 4 — Draft Specification (R-01..R-12)

- Write each requirement R-01..R-12 with its source pointer (or `TBD`/`ASSUMPTION`).
- Add Verification table linking each R-* to its acceptance evidence.
- List `ARTIFACT_REGISTER.csv` rows 4033-4037 in Documentation.

Verification: count R-* lines and confirm twelve.

### Step 5 — Draft Guidance (principles, considerations, trade-offs, conflict table)

- Articulate the five principles (vendor/EPC split, source basis, interface set, sweet/sour service, by-others exclusions).
- Capture the tank-arrangement ambiguity and hazardous-material list gap as `Considerations`.
- Initialize Conflict Table (empty in Pass 2).

Verification: no claim in Guidance is unsupported by a source pointer or labeled ASSUMPTION.

### Step 6 — Draft Procedure (this file)

- Document the production procedure (this file).
- Verification step matches each R-* and each artifact row.

### Step 7 — Cross-document consistency sweep (Pass 2)

- Datasheet ↔ Specification: every tagged equipment item in the Datasheet appears in R-02; every interface row appears under R-08; every condition row supports R-05.
- Specification ↔ Guidance: each principle is rooted in the source basis cited by at least one R-*.
- Specification ↔ Procedure: each Step yields verification evidence for one or more R-*.
- Terminology: "cylinder lube oil"/"crank-case lube oil"/"sweet and sour service"/"transfer pump" used consistently.
- Values: tag IDs (P-9240-1, P-9250-1), storage volumes (400 bbl / 200 bbl), interface IDs, scope-item IDs consistent across documents.

Verification: no inconsistencies found; tank-arrangement noted as TBD in both Datasheet R-09 area and Guidance Considerations.

### Step 8 — Status update (safe-update only)

- If `Current State` was `OPEN`, set it to `INITIALIZED` via `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`.
- If not `OPEN`, skip and report.

Verification: `_STATUS.md` history line added; no regression.

### Step 9 — Persist run record

Write `_run_records/TASK_RUN_<timestamp>.md` capturing input echo, resolved state, tools used, outputs, missing items, and applied changes.

## Verification

The deliverable is considered complete (for the P1_P2 pass set) when:

- The four documents exist in `{DELIVERABLE_PATH}` with default schema sections present.
- Every R-* in `Specification.md` has a source pointer or `TBD`/`ASSUMPTION` label.
- The Datasheet covers all five artifact rows (`ART-853208E9E8`, `ART-558D879D67`, `ART-8DAFE7D39E`, `ART-369E16AA74`, `ART-EA90D18DCF`).
- All four scope items (`SOW-0135`..`SOW-0138`) are demonstrably traced into the Specification (R-10).
- `_STATUS.md` has been updated `OPEN → INITIALIZED` (this run) or the skip was explicitly reported.
- The run record is present in `_run_records/`.

## Records

| Record | Path |
|---|---|
| Datasheet | `{DELIVERABLE_PATH}/Datasheet.md` |
| Specification | `{DELIVERABLE_PATH}/Specification.md` |
| Guidance | `{DELIVERABLE_PATH}/Guidance.md` |
| Procedure | `{DELIVERABLE_PATH}/Procedure.md` |
| Status update | `{DELIVERABLE_PATH}/_STATUS.md` |
| Run record | `{DELIVERABLE_PATH}/_run_records/TASK_RUN_2026-05-24_*.md` |
