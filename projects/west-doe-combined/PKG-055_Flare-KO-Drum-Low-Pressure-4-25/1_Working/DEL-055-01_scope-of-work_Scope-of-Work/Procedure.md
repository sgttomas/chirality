# Procedure — DEL-055-01 Scope of Work (Flare KO Drum (Low Pressure) 4-25)

> Operational procedure to produce the EPC Scope of Work artifact for PKG-055.

## Purpose

To produce the EPC Scope of Work artifact for PKG-055 ("Flare KO Drum (Low Pressure) 4-25") that satisfies the requirements R-1 through R-7 in `Specification.md` and the four anticipated artifacts identified in `_CONTEXT.md`.

## Prerequisites

| Item | Source | Status |
|---|---|---|
| `_CONTEXT.md` populated with package identity, scope, anticipated artifacts, covered scope items, and supported objectives | `_CONTEXT.md` | Present |
| `_REFERENCES.md` populated with the authoritative decomposition basis (Gate 7 snapshot) and pointer to `_Sources/` | `_REFERENCES.md` | Present |
| Gate 7 final published PROJECT_DECOMP snapshot accessible | `_REFERENCES.md` | Present |
| SCOPE_LEDGER.csv rows SOW-0083, SOW-0084, SOW-0085, SOW-0086 accessible | `_REFERENCES.md`; `_CONTEXT.md` Covers Scope Items | Present |
| PACKAGE_REGISTER.csv row PKG-055 accessible | `_REFERENCES.md` | Present |
| DELIVERABLE_REGISTER.csv row `DEL-055-01_scope-of-work` accessible | `_REFERENCES.md` | Present |
| DBM-Deepcut/4-25_Deepcut_DBM.md accessible | `_Sources/DBM-Deepcut/` | Present (markdown) |
| 26020-Package_Requirements.docx heading 10 extracted to markdown | `_Sources/` | TBD — only DOCX present; not yet extracted to markdown locally |
| Declared upstream dependencies (if any) | `_DEPENDENCIES.md` | None declared at PREPARATION |

## Steps

### Step 1 — Confirm package identity and tag inventory

1. Open PACKAGE_REGISTER.csv (Gate 7 snapshot). Locate PKG-055.
2. Extract: package ID, workbook row, WBS, discipline, package name, companion equipment identifier, interface type list, responsibility description.
3. Open SCOPE_LEDGER.csv. Locate SOW-0083 through SOW-0086.
4. Open DBM-Deepcut/4-25_Deepcut_DBM.md. Locate equipment tag rows for "Flare KO Drum (Low Pressure) 2" (lines 2581-2582) for tag confirmation and line 2783 for modularization context.
5. Record the inventory in the Scope of Work artifact (satisfies R-1 and supplies inputs for R-2).

### Step 2 — Draft the package function and source basis statement

1. Quote the SOW-0084 basic scope statement.
2. Quote the SOW-0085 included-equipment statement.
3. Quote the SOW-0086 scope notes and open items statement.
4. Compose the package function paragraph that names the function (LP flare knock-out + liquid transfer + truck-out) and cites SOW-0084 and SOW-0085.

This step satisfies R-2 and R-6 for the function statement.

### Step 3 — Draft the responsibility split

1. Quote the workbook responsibility description from PACKAGE_REGISTER.csv (Responsibility Description column).
2. Restate the split as two clauses: Package Vendor scope, EPC Integrator scope.
3. Record the SOW-0083 anchor sentence to confirm the project-level direction.

This step satisfies R-3.

### Step 4 — Draft the whole-facility integration narrative

1. Read DBM-Deepcut/4-25_Deepcut_DBM.md lines 2028-2033 (Low-pressure flare row and stack arrangement) and line 1834 (flare overview row).
2. Draft a paragraph describing: connected LP equipment list, header size, KO drum and pump tags, stack arrangement (LP piggy-backed on common HP/cryo stack), and any open items (relief volumes TBD; LP stack OD TBD; shared 03-25/04-25 allocation TBD).
3. Cite each fact to DBM line numbers.

This step satisfies R-4.

### Step 5 — Build the interface type and responsibility table

1. Read the Interface Types column for PKG-055 in PACKAGE_REGISTER.csv (Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports).
2. For each interface type, assign owner (Package Vendor inside the package envelope; EPC Integrator outside the package envelope) consistent with the responsibility split from Step 3.
3. Where an interface owner is not explicitly stated in source materials, label ASSUMPTION and mark for human confirmation.

This step satisfies R-5.

### Step 6 — Write the exclusion list

1. Lift the exclusion items from SOW-0086 and DBM lines 2029, 2031: LP flare stack; common HP/cryo flare stack; air-assist blower; LP flare tip detail.
2. Cite each exclusion to its source.

This step satisfies R-7.

### Step 7 — Add objective linkage (package-grouped, ASSUMPTION)

1. Copy the supported objectives from `_CONTEXT.md` (OBJ-001, OBJ-004..010).
2. Label the block as package-grouped ASSUMPTION per `OBJECTIVE_ASSOCIATION_MODE: PACKAGE_HEURISTIC`.

This step satisfies R-8.

### Step 8 — QA cross-document consistency

1. Verify all tag identifiers (V-3900-1, P-3900-1) appear identically across Datasheet, Specification, Guidance, and Procedure.
2. Verify the responsibility split wording matches PACKAGE_REGISTER.csv.
3. Verify the exclusion list is identical in Specification (X-1..X-3) and Guidance.
4. Run the Step 5 consistency checks from `SKILL.md`. If a discrepancy is not resolvable from drafts alone, re-open the source slice and either resolve or escalate via the Conflict Table in `Guidance.md`.

### Step 9 — Status update

1. If `_STATUS.md` shows `OPEN`, update to `INITIALIZED` via `tools/scaffolding/write_status.sh` with attribution `TASK+four-documents`.
2. Otherwise do not modify `_STATUS.md`.

### Step 10 — Run record

1. Persist the run record at `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` with the run report headings populated.

## Verification

| Check | Pass Criterion |
|---|---|
| V-1 | Datasheet contains the package identifier `PKG-055` / `26020-01-PT-17-003` and lists `V-3900-1` and `P-3900-1`. |
| V-2 | Specification carries R-1 through R-7, each with a source citation. |
| V-3 | Guidance carries Purpose, Principles, Considerations, Trade-offs, Examples, and a Conflict Table. |
| V-4 | Procedure carries Prerequisites, Steps, Verification, and Records. |
| V-5 | The exclusion list (LP flare stack, common stack, air-assist blower) is present in both Specification (X-1..X-3) and Guidance. |
| V-6 | All non-trivial values cite a source slice or are labeled `TBD` / `ASSUMPTION`. |
| V-7 | `_STATUS.md` shows `INITIALIZED` (or its prior protected state, unchanged). |
| V-8 | A run record file exists in `_run_records/` for this invocation. |

## Records

| Record | Location |
|---|---|
| Scope of Work artifact (this deliverable) | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in deliverable folder |
| Status transition | `_STATUS.md` (OPEN → INITIALIZED) |
| Run record | `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` |
| Source citations | Inline references to PACKAGE_REGISTER.csv, SCOPE_LEDGER.csv, DELIVERABLE_REGISTER.csv, DBM-Deepcut/4-25_Deepcut_DBM.md |
