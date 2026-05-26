# Procedure — PKG-068 TEG Dehydration Unit (Package Datasheet)

This Procedure describes the steps the EPC Integrator takes to **produce, issue, and maintain** the Package Datasheet (`DEL-068-02`) handed to the third-party TEG Dehydration Unit Package Vendor. It does not describe operation of the physical TEG unit (that belongs in vendor operating manuals downstream of `DEL-068-04`/`DEL-068-05`).

## Purpose

Produce a source-grounded, internally consistent, interface-complete Package Datasheet that allows a Package Vendor to perform package engineering, package design, vendor documentation, and physical equipment supply for the 04-25 Deepcut TEG Dehydration Unit, with explicit open items surfaced for human ruling rather than silent resolution.

## Prerequisites

| # | Prerequisite | Source / Location |
|---|---|---|
| 1 | Accepted upstream decomposition snapshot | Gate 7 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` |
| 2 | Deliverable-local context | `_CONTEXT.md` populated and `_STATUS.md` = `OPEN` or `INITIALIZED` |
| 3 | Accessible source materials | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (TEG sections SEC-06, SEC-08, SEC-09); workbook registers (Deliverable, Package, Interface, Artifact, Objective) |
| 4 | Reference register | `_REFERENCES.md` enumerating decomposition basis and source root |
| 5 | Declared upstream dependencies | `_DEPENDENCIES.md` (currently none declared; PREPARATION-initialized DECLARED mode) |
| 6 | Companion sibling deliverable awareness | Sibling deliverables `DEL-068-01` (scope of work), `DEL-068-03` through `DEL-068-06` exist in `PKG-068/1_Working/` |
| 7 | Package Requirements document text access | `26020-Package_Requirements.docx` (binary; TBD — text extraction not performed this pass) |

## Steps

### Step 1 — Confirm scope and identity

1. Read `_CONTEXT.md` and confirm DeliverableID, ParentPackageID, Discipline, ResponsibleParty, and "Covers Scope Items" SOW IDs against `DELIVERABLE_REGISTER.csv` and `SCOPE_LEDGER.csv` rows.
2. Confirm Package Name, CoA tracking number, WBS, and discipline against `PACKAGE_REGISTER.csv` PKG-068 row.

Verification: identity table in `Datasheet.md` matches both `_CONTEXT.md` and `PACKAGE_REGISTER.csv`.

### Step 2 — Extract authoritative process and equipment basis

1. Read DBM SEC-06 "Process-Gas TEG Dehydration Basis" in full: Process Description, TEG Design Values, TEG Equipment and Design Requirements, TEG Open Items and Assumptions.
2. Read DBM SEC-08 (Utilities — LP fuel gas for TEG stripping gas; VRU connectivity; HP/LP flare routing).
3. Read DBM SEC-09 (Energy / heat-medium — confirm 425 degF reboiler supply; reboiler duty table row for TEG reboiler).
4. Read DBM module table (570-1 TEG Dehydration Module — Shop) and tagged-equipment row 104 for the equipment list.
5. Capture all numeric design values and explicit equipment basis statements into `Datasheet.md` Attributes/Conditions/Construction tables with source citations.

Verification: every non-trivial value in `Datasheet.md` cites `4-25_Deepcut_DBM.md` (or `PACKAGE_REGISTER.csv` for scope-list entries); `Specification.md` requirements are traceable to the same source rows.

### Step 3 — Extract interface evidence

1. Filter `INTERFACE_REGISTER.csv` for PKG-068 rows.
2. List each interface in the Datasheet's "Package interface requirements" table with Interface ID, Interface Type, and source citation.
3. Cross-reference `ARTIFACT_REGISTER.csv` PKG-068 rows for per-interface evidence artifacts (ART-F80D7E8B07, ART-D3CB519672, etc.) to ensure each interface fact is represented.

Verification: count of interface rows in Datasheet equals 13 (matches PKG-068 INTERFACE_REGISTER rows).

### Step 4 — Capture open items and conflicts

1. Identify every TBD / TBC item in DBM TEG sections (TEG Open Items and Assumptions paragraph).
2. Identify any apparent discrepancies between workbook package scope and DBM equipment basis (e.g., "Burner Control Panel" vs heat-medium-fired reboiler).
3. Identify references that are cited but not text-accessible (e.g., `26020-Package_Requirements.docx`).
4. Record each item in `Guidance.md` Conflict Table with Conflict ID, both sources, impacted sections, a PROPOSAL, and Human ruling = TBD.

Verification: Conflict Table includes pressure basis, reboiler firing, contactor sparing, lean/rich exchanger, .docx access, materials/mercaptan, and ambient basis at minimum.

### Step 5 — Cross-document consistency sweep (Pass 2)

1. Verify entities and attributes in `Datasheet.md` are reflected in `Specification.md` requirements (e.g., contactor outlet water spec ↔ REQ-068-02-001).
2. Verify requirements in `Specification.md` have rationale or trade-off treatment in `Guidance.md` where appropriate (e.g., contactor sparing ↔ Guidance "Trade-offs").
3. Verify each requirement has a verification approach in `Specification.md`'s Verification table.
4. Verify terminology consistency across all four documents (e.g., "TEG contactor", not mixed with "absorber"; "lean/rich TEG exchanger", not "regen exchanger").
5. Verify numeric values and units match across documents (e.g., 45.0 USGPM, 395 degF, 1100 psig).
6. Where inconsistencies remain unresolvable from drafted documents alone, re-open the source slice and reconcile against authority; if still unresolved, add a Conflict Table entry rather than guessing.

Verification: terminology/values consistent; Conflict Table updated for any remaining inconsistency.

### Step 6 — Update status (safe state update)

1. Read `_STATUS.md`. If Current State is `OPEN`, run:
   `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`
2. If Current State is not `OPEN`, do not modify `_STATUS.md` (no state regression).

Verification: `_STATUS.md` updated to `INITIALIZED` only when previous state was `OPEN`; otherwise update skipped and reported in run record.

### Step 7 — Write run record

1. Write `_run_records/TASK_RUN_{YYYY-MM-DD}_{HHmm}.md` per AGENT_TASK run-record format with YAML frontmatter and required body headings.
2. List all four documents in Applied Changes; list `_STATUS.md` state transition; list any MISSING references; list NEEDS_HUMAN_RULING entries from Conflict Table.

Verification: run record exists and run-status = SUCCESS (or FAILED with details).

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| All four documents exist | `ls {DELIVERABLE_PATH}` | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` present |
| Schema sections present | Inspect headings | Datasheet: Identification/Attributes/Conditions/Construction/References; Specification: Scope/Requirements/Standards/Verification/Documentation; Guidance: Purpose/Principles/Considerations/Trade-offs/Examples; Procedure: Purpose/Prerequisites/Steps/Verification/Records |
| Source-grounded values | Inspect citations | Every non-trivial value cites `4-25_Deepcut_DBM.md` SEC-06 (or PACKAGE_REGISTER.csv / INTERFACE_REGISTER.csv) or is marked `TBD` / `ASSUMPTION` |
| Interface coverage | Count interface rows | 13 rows match PKG-068 in INTERFACE_REGISTER.csv |
| Conflict Table populated | Inspect Guidance | All material TBD/TBC items from DBM TEG Open Items are represented |
| _STATUS.md updated safely | Read `_STATUS.md` | New state is `INITIALIZED` if previous was `OPEN`; otherwise unchanged |
| Out-of-scope writes | Inspect file changes | No files modified outside `{DELIVERABLE_PATH}` |

## Records

| Record | Location |
|---|---|
| Four documents | `{DELIVERABLE_PATH}/Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` |
| Status update | `{DELIVERABLE_PATH}/_STATUS.md` History line |
| Run record | `{DELIVERABLE_PATH}/_run_records/TASK_RUN_{YYYY-MM-DD}_{HHmm}.md` |
| Open items for human ruling | Conflict Table in `Guidance.md` |
| Source provenance | Inline citations across all four documents; `_REFERENCES.md` for the upstream decomposition basis |
