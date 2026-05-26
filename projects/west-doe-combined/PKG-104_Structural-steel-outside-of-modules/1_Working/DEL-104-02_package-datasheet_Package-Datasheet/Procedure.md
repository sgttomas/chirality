# Procedure — PKG-104 Package Datasheet (Structural Steel — Outside of Modules)

> Operational steps to **produce** the DEL-104-02 Package Datasheet artifact. (Steps to **use/operate** the datasheet are limited to the vendor-handoff handshake at Step 5.) Steps are derived from the Specification requirements and the four-documents skill method. Where judgment would be needed, the step is marked `TBD`.

## Purpose

Produce, review, and issue the PKG-104 Package Datasheet such that a third-party structural-steel vendor or discipline subcontractor receives a coherent, source-grounded technical basis for outside-of-module structural-steel engineering.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (see `_CONTEXT.md`, `_REFERENCES.md`).
- Locally accessible DBM source slices:
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Civil/Structural and Codes sections).
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Site Basis, Foundations and Structural Supports).
- Workbook Packages row 105 in `_Sources/26020-Package_Requirements.docx` (binary — parsed slice required before vendor issue).
- Package interface register `_Sources/26020-Packages_Interfaces_4_export.xlsx` (binary — parsed slice required before vendor issue).
- Declared upstream dependencies (`_DEPENDENCIES.md`): none declared at PREPARATION; treat as advisory.
- `_STATUS.md` current state in `ALLOW_OVERWRITE_STATES` (OPEN, INITIALIZED) for the producing TASK.

## Steps

### Step 1 — Confirm package identity and boundary
1.1 Read `_CONTEXT.md` and confirm DeliverableID, Parent Package, Discipline, Responsible Party.
1.2 Confirm the "outside of modules" boundary against the DBM module table (`DBM-Deepcut` lines ~2766-2818). Record any boundary ambiguities in the Conflict Table in `Guidance.md`.
1.3 Verify objective association mode is `PACKAGE_HEURISTIC` and record `OBJ-001`, `OBJ-008` as **ASSUMPTION** unless human confirms.

### Step 2 — Lock the governing codes-and-standards block
2.1 Populate the codes/standards table from `DBM-Deepcut` §"Governing Civil and Structural Basis" (line ~2672) and §"Codes and Standards" (lines ~3411-3413).
2.2 Confirm CSA S16, G40.20/G40.21, W59 are cited with the editions used in source (CSA S16:19; CSA G40.20-13/G40.21-13; CSA W59-18); cite source line numbers in the datasheet `References` column.

### Step 3 — Populate environmental and material conditions
3.1 Record minimum design ambient -40 deg C from `DBM-Comp_and_Liquids` line ~145.
3.2 Record material grades 350W (W-flange, HSS) and 300W (channels, plates, angles) from `DBM-Deepcut` line ~2676.
3.3 Record snow/wind/seismic loading basis as "per NBCC, project-site values" — do not invent specific load values.

### Step 4 — Populate foundation, grading, and cable-tray interfaces
4.1 Record driven-steel-pile foundation default from `DBM-Deepcut` §"Piles and Foundations" (lines ~2740, ~2749); mark pile parameters TBD pending geotechnical report.
4.2 Record pipe-rack grading basis (high equal ridges, 1.5%/1.0% pad slopes) from `DBM-Deepcut` lines ~2708-2710.
4.3 Record cable-tray module requirements (uppermost pipe-rack location; walkway; tray brackets each side; ≥30% future growth) from `DBM-Deepcut` line ~3023.

### Step 5 — Build the supported-equipment list and interface matrix (binary-source-dependent)
5.1 **TBD** — parse `_Sources/26020-Package_Requirements.docx` (Workbook Packages row 105) and `_Sources/26020-Packages_Interfaces_4_export.xlsx` to extract the supported-equipment list and package-to-package interface rows.
5.2 Until 5.1 is performed, hold these tables as `TBD` shells in the datasheet — do not invent equipment tags or interface partners.
5.3 If parsed slices are produced, place them under the deliverable folder (or update `_REFERENCES.md` to point at them) and re-run `TASK + four-documents` with `RUN_PASSES=P3_ONLY` after `_SEMANTIC_LENSING.md` exists.

### Step 6 — Cross-document consistency sweep
6.1 Run the Pass 2 cross-reference checks (Datasheet ↔ Specification, Specification ↔ Guidance, Specification ↔ Procedure, terminology, values) per SKILL Step 5.
6.2 Reconcile or escalate to the `Guidance.md` Conflict Table.

### Step 7 — Status update
7.1 If current `_STATUS.md` state is `OPEN`, advance to `INITIALIZED` via `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` (SKILL Step 7).
7.2 If state is not `OPEN`, do not modify `_STATUS.md`; record the skip in the run record.

### Step 8 — Vendor / discipline handoff handshake (use of artifact)
8.1 Issue the datasheet bundle (this Datasheet + Specification + Guidance + Procedure + interface matrix shell) to the vendor or discipline subcontractor identified by the EPC Integrator.
8.2 Capture all vendor questions against the existing TBD list and Conflict Table; do not silently close TBDs without source-grounded resolution.
8.3 **TBD** — formal acceptance/return protocol with the vendor is outside the accessible source set; record as TBD until project-level vendor-handoff procedure is referenced.

## Verification

| Step | Verification |
|---|---|
| 1 | Identity fields match `_CONTEXT.md` exactly; boundary statement present. |
| 2 | All four CSA/NBCC codes cited with edition where source provides one; each entry traceable to a `DBM-Deepcut` line. |
| 3 | -40 deg C and 350W/300W appear verbatim in the datasheet. |
| 4 | Foundation, grading, and cable-tray interfaces are recorded with source line numbers. |
| 5 | Supported-equipment and interface tables either contain parsed source content or are explicitly marked `TBD` with rationale. |
| 6 | No silent contradictions across the four documents; any remaining conflicts appear in the Conflict Table. |
| 7 | `_STATUS.md` advanced from `OPEN` to `INITIALIZED` only when applicable; history line added. |
| 8 | Run record captures the vendor-handoff handshake outcome (or marks it TBD). |

## Records

- Updated `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- `_STATUS.md` history entry for the state transition (when applicable).
- `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHMM>.md` produced by the TASK shell — captures pass directive, sources read, source rereads (Pass 3), Conflict Table dispositions, and RUN_STATUS.
- (Future) Parsed source slices for Workbook Packages row 105 and the interface register, placed under the deliverable folder or referenced from `_REFERENCES.md`.
