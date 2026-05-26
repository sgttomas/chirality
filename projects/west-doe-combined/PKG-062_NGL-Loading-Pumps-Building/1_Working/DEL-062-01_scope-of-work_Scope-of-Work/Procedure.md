# Procedure — DEL-062-01 Scope of Work (PKG-062 NGL Loading Pumps Building)

## Purpose

Operational procedure for **producing** the DEL-062-01 Scope of Work artifact for PKG-062 (NGL Loading Pumps Building). The output is a single EPC Integrator-authored Scope of Work document containing the four anticipated artifacts listed in `_CONTEXT.md` (scope narrative, tagged equipment list, function/integration narrative, responsibility record).

## Prerequisites

### Inputs (must be available before drafting)
- `_CONTEXT.md` (deliverable identity, anticipated artifacts, SOW coverage list, objective list).
- `_REFERENCES.md` (decomposition basis pointers; source root pointer).
- `_DEPENDENCIES.md` (declared upstream/downstream; for this deliverable, none declared).
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv` — rows SOW-0153, SOW-0154, SOW-0155, SOW-0156.
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` — row 420.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — at minimum lines 73 (narrative) and 2549, 2610 (equipment table rows).

### Sources whose locally accessible portions are limited
- `26020-Package_Requirements.docx` package heading 16 — accessible only via SCOPE_LEDGER excerpts; binary docx not extracted into the deliverable folder. Treat fragments cited in SCOPE_LEDGER as authoritative; mark anything not cited there as TBD.

### Authority and approval
- EPC Integrator (responsible party per `_CONTEXT.md`).
- Human ruling required to resolve Conflict Table items (see `Guidance.md`).

## Steps

### Step 1 — Confirm package identity
1. Open `_CONTEXT.md`. Confirm DeliverableID = `DEL-062-01_scope-of-work`, ParentPackageID = `PKG-062`, workbook row = 76, source heading = "26020-Package_Requirements.docx package heading 16".
2. Cross-check against `DELIVERABLE_REGISTER.csv` row 420.

### Step 2 — Read source-anchored scope content
1. Open `SCOPE_LEDGER.csv` and locate rows for SOW-0153, SOW-0154, SOW-0155, SOW-0156.
2. Extract: in-scope statement, basic scope wording, major included equipment, capacity values (and TBC markers), driver/control basis, By Others list, building provision.
3. Open `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` and read the NGL loading narrative at line 73 and the equipment-table rows at lines 2549 and 2610.

### Step 3 — Draft package identity and tagged equipment list
1. State the package name, workbook row, source heading, discipline, and responsible party (R-SOW-01).
2. List the four equipment tags P-9510-1 / P-9520-1 / P-9530-1 / P-9540-1 with the type "Blackmer Model LGL4B rotary vane pump" (R-SOW-02).

### Step 4 — Draft package function narrative
1. State the process function from SOW-0154: pumps move LPG product from storage to LPG Truck Loading (R-SOW-03).
2. Position the package within the 04-25 Deepcut NGL system (R-SOW-09) using the DBM line-73 narrative.

### Step 5 — Draft performance and driver basis
1. Record per-pump capacity 68 m3/hr @ 345 kPad (300 USGPM @ 50 psid) TBC TDH (R-SOW-04). Carry the TBC marker forward.
2. Record driver basis: 575 V / 3 Ph / 60 Hz electric motors, fed from 600 V MCC, sized for -40 C inlet stabilizer composition start-up, local H-O-A or On-Off (R-SOW-05).
3. Record self-framing building erected at site (R-SOW-06).

### Step 6 — Draft responsibility and boundary
1. State the Package Vendor / EPC Integrator split per SOW-0153 (R-SOW-07).
2. State the By Others exclusions per SOW-0156: DCS integration, foundations, electrical supply to MCC (R-SOW-08).

### Step 7 — Trace to coverage
1. Record that this SOW covers SOW-0153, SOW-0154, SOW-0155, SOW-0156 (R-SOW-10).
2. Record the supported objectives as an ASSUMPTION (package-grouping heuristic) (R-SOW-11): OBJ-001, OBJ-003..OBJ-010.

### Step 8 — Cross-document consistency sweep
1. Confirm tags, capacity values, and By-Others items match across `Datasheet.md`, `Specification.md`, `Guidance.md`, and this `Procedure.md`.
2. Confirm any "TBC" / "TBD" markers in source are preserved (not silently filled).

### Step 9 — Surface open items
1. Add or update the Conflict Table in `Guidance.md` to surface unresolved items (objectives heuristic, missing source extract for package heading 16, TBC conditions).

### Step 10 — Submit for EPC Integrator review
1. Route the SOW to the EPC Integrator role for review.
2. Capture the human ruling for each open Conflict Table row.
3. Hand off the approved SOW as input to DEL-062-02 (Package Datasheet) and the remaining PKG-062 deliverables.

## Verification

| Check | Expected outcome |
|---|---|
| Identity fields match `_CONTEXT.md` | PASS |
| Tagged equipment list matches `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2610 | PASS |
| Capacity, driver, control, and By-Others statements match SCOPE_LEDGER SOW-0155, SOW-0156 verbatim where cited | PASS |
| TBC markers preserved | PASS |
| Coverage of SOW-0153 through SOW-0156 traceable | PASS |
| Cross-document terminology consistent | PASS |
| Conflict Table populated for unresolved items | PASS |

## Records

- This Scope of Work document (DEL-062-01) as written into `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`.
- Run record at `_run_records/TASK_RUN_<timestamp>.md`.
- Conflict Table entries in `Guidance.md` (human ruling pending).
- Coverage record traceable to `SCOPE_LEDGER.csv` rows SOW-0153..SOW-0156 and `OBJECTIVE_SCOPE_MAP.csv` rows for PKG-062.
- Status update: `_STATUS.md` advanced from OPEN to INITIALIZED upon successful Pass 1/Pass 2 completion.
