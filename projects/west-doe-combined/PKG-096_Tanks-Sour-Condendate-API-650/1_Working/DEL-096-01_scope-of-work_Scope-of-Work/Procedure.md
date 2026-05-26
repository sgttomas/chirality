# Procedure — DEL-096-01 Scope of Work (PKG-096 Tanks, Sour Condendate (API 650))

## Purpose

Operational procedure to produce, verify, and hand off the EPC Scope of Work for PKG-096. This procedure describes how the EPC Integrator authors the SoW so it can be consumed by the Package Vendor (DEL-096-04) and by the EPC-side facility integration deliverables (DEL-096-03, DEL-096-06).

## Prerequisites

### Required references (locally accessible)

- `_CONTEXT.md` — deliverable identity, scope, anticipated artifacts, covers/supports lists.
- `_REFERENCES.md` — pointers to the decomposition snapshot and source materials.
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — accepted upstream snapshot:
  - `DELIVERABLE_REGISTER.csv` row for `DEL-096-01_scope-of-work`.
  - `PACKAGE_REGISTER.csv` row 92 / PKG-096.
  - `SCOPE_LEDGER.csv` rows SOW-0217..SOW-0220.
  - `OBJECTIVE_PACKAGE_MAP.csv` rows for PKG-096 (OBJ-002..OBJ-010).
- `_Sources/26020-Package_Requirements.docx` — package heading 48 ("26020-03-PT-19-005 - Tanks, Sour Condensate").
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — interface row 92 (used as source for the Physical Interface Summary).

### Required references (declared but not locally accessible — location TBD)

- `Bid Docs/Budgetary/26020-03-PT-RFQ-19-005 - Sour Conde Tanks.docx` — RFQ cited as source basis by the package text. Clause-level API 650 modifications, NACE document identifier, and full design-condition basis depend on this RFQ.

### Required state

- `_STATUS.md` Current State is in `ALLOW_OVERWRITE_STATES` (`OPEN` or `INITIALIZED`).
- `_DEPENDENCIES.md` does not declare upstream blockers that prevent drafting (PKG-096 has no declared upstream dependencies in PREPARATION).

## Steps

### Step 1 — Establish identity

1. Read `_CONTEXT.md` Identity block.
2. Read the matching `DELIVERABLE_REGISTER.csv` row.
3. Populate `Datasheet.md` Identification table.

### Step 2 — Extract source basis

1. Open `_Sources/26020-Package_Requirements.docx`.
2. Locate package heading "26020-03-PT-19-005 - Tanks, Sour Condensate".
3. Read the source slice covering: Location/Status, Source Basis, Basic Scope, Major Included Equipment, Scope Notes / Open Items, Physical Interface Summary, Vendor Engineering Deliverables, Interface Coordination Notes.
4. Record verbatim equipment counts, codes, coating, relief devices, fill protection, and design conditions.

### Step 3 — Reconcile with SCOPE_LEDGER

1. Read `SCOPE_LEDGER.csv` rows SOW-0217..SOW-0220.
2. Confirm each row maps to PKG-096 and lists DEL-096-01 among `Linked Deliverables`.
3. Where the SCOPE_LEDGER restates source text (e.g., SOW-0220 carrying "Item No. 2" values), flag any discrepancy with the source slice as a Conflict Table entry in `Guidance.md`.

### Step 4 — Populate Datasheet conditions and construction

1. From the source slice, populate `Datasheet.md` Attributes, Conditions, Construction, and Interface Applicability tables.
2. Use `TBD` for unstated values; do not infer from analogous packages.
3. Use `ASSUMPTION:` for inferred values (e.g., "Ambient" interpreted as site temperature).

### Step 5 — Author Specification requirements

1. Convert source items into testable requirements (REQ-1..REQ-10).
2. Cite the source row (SOW-xxxx) or source-slice section name for every requirement.
3. Where a clause-level standard reference is needed but not locally accessible, mark `location TBD` in the Standards table.

### Step 6 — Author Guidance

1. State purpose, principles, considerations, trade-offs.
2. Populate the Conflict Table with any conflicts surfaced in Steps 2-5.
3. Do not invent rulings — leave `Human ruling` columns as `TBD`.

### Step 7 — Author this Procedure (recursive consistency)

1. Confirm steps reference only the files actually used.
2. Confirm prerequisites list both accessible and inaccessible references.

### Step 8 — Cross-document consistency sweep (Pass 2)

1. Verify entity names (TK-9110-2 / TK-9120-2), units, and code references appear identically across the four documents.
2. Verify each Specification REQ has either a Guidance rationale or a Verification approach (or both).
3. Verify Datasheet conditions match the Specification REQ-6 values.

### Step 9 — Safe status update

1. Read `_STATUS.md`.
2. If Current State is `OPEN`, run `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`.
3. If Current State is not `OPEN`, do not modify `_STATUS.md`.

### Step 10 — Run record

1. Write `_run_records/TASK_RUN_<YYYY-MM-DD_HHmm>.md` capturing inputs, sources read, outputs produced, conflicts surfaced, and any `TBD`/`ASSUMPTION` items.

## Verification

| Check | How |
|---|---|
| All four documents exist | Directory listing of `DELIVERABLE_PATH`. |
| Default schema sections present | Heading scan of each document. |
| Identity values match `_CONTEXT.md` and DELIVERABLE_REGISTER | Field-by-field comparison. |
| Design values match source slice (Item No. 1) | Compare Datasheet Conditions to package text Major Included Equipment + Scope Notes. |
| Conflicts not silently resolved | Inspect `Guidance.md` Conflict Table; ensure CFL-001..CFL-004 carry `TBD` rulings. |
| `_STATUS.md` advanced safely | Verify transition recorded only when Current State was `OPEN`. |
| No metadata files modified beyond `_STATUS.md` | git diff scoped to `DELIVERABLE_PATH`. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md` (including Conflict Table)
- `Procedure.md`
- `_STATUS.md` (history entry on safe transition)
- `_run_records/TASK_RUN_<timestamp>.md`
