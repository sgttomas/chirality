# Procedure — DEL-077-02 Package Datasheet (PKG-077 Methanol Injection)

> Operational document. Describes the steps to **produce** the PKG-077 Package Datasheet artifact (this deliverable). Source-grounded; inferences labeled `ASSUMPTION`; missing items marked `TBD`.

## Purpose

Provide the EPC Integrator producer with a repeatable, source-anchored procedure for producing the PKG-077 Package Datasheet artifact so a Package Vendor (or another discipline) can engineer and design the methanol-injection package.

## Prerequisites

1. Read deliverable-local context:
   - `_CONTEXT.md` — identity, scope, anticipated artifacts, supports/covers, decomposition references.
   - `_REFERENCES.md` — authoritative decomposition basis and source list.
   - `_DEPENDENCIES.md` — declared upstream/downstream (currently none declared).
   - `_STATUS.md` — confirm overwrite is permitted under brief.
2. Access the accepted decomposition snapshot:
   - `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row `DEL-077-02_package-datasheet`)
   - `…/PACKAGE_REGISTER.csv` (row PKG-077)
   - `…/INTERFACE_REGISTER.csv`, `…/ARTIFACT_REGISTER.csv`, `…/OBJECTIVE_DELIVERABLE_MAP.csv`
3. Access locally-accessible source materials:
   - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (methanol-injection slices; see Datasheet References).
   - `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Workbook Packages row 72) — binary; treat as **location TBD**.
   - `_Sources/26020-Package_Requirements.docx` — binary; treat as **location TBD**.
4. Be authorized to write within `{DeliverablePath}` (this folder) and to update `_STATUS.md` only.

## Steps

### Step 1 — Confirm identification block
Populate the Datasheet Identification table from `_CONTEXT.md` and PACKAGE_REGISTER.csv (PKG-077). Verify `DeliverableID`, `ParentPackageID`, `Discipline`, `WBS`, `Workbook Row`, `Vendor Document Code`.

### Step 2 — Capture package function and operating premise
From DBM-Deepcut L428, L1328:
- State the methanol-injection package function as **transient hydrate suppression**.
- State the operating premise: **inject into one point at a time**.
- State that the facility provides **no continuous hydrate suppression in raw inlet gas piping**.

### Step 3 — Enumerate injection points
List every methanol injection point with its service location and source reference. At minimum (DBM-Deepcut L1328 plus L630, L674):
- BAHX pass-inlet headers, upstream of strainers (each pass).
- J-T valve inlet.
- Inlet separators upstream of PCV.
- Inlet separators upstream of HCL and water-dump valves.
- Acid gas compressor package (capacities **TBD** per L1371).
- MPFF feed system (transient/line-pack start-up).

### Step 4 — List package equipment with tags
Populate the equipment table from DBM-Deepcut Equipment List rows (L2605, L2606) and Sparing table (L2379):
- `TK-6395-1` METHANOL STORAGE TANK — Qty 1.
- `P-6396-1` METHANOL PUMP — Qty 1; sparing: 1 installed / 100% operating.

### Step 5 — Capture storage and pump basis
From DBM-Deepcut L1329:
- Atmospheric double-walled methanol tank, adjacent to expander building.
- Triplex reciprocating injection pump.
- Tank design SG = 1.00 (pure methanol) — record as **TBC** per source.

### Step 6 — Record design conditions
- Winter hydrate temperature reference: -2.8 degC (DBM L920).
- Cryogenic-area hydrate margin: ~6 degC above expected hydrate temperature, no continuous methanol provisions (DBM L1153).
- Downstream BAHX max design temperature: 150 degF (66 degC) (DBM L1324).
- Per-point capacities, injection rates, acid-gas-compressor injection details, methanol tank SG: **TBD** (DBM L1328, L1351, L1392).

### Step 7 — Build the package interface requirements matrix
From PACKAGE_REGISTER.csv (PKG-077) Applicable Interface Types, create one matrix row per interface type:
Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports.
For each row record: nominal scope, vendor-vs-EPC ownership, source reference, and `TBD` where source-specific values are not accessible.

### Step 8 — Record responsibility split and traceability
- Responsibility: Package Vendor (engineering/design/equipment) vs. EPC Integrator (integration/interfaces). Source: PACKAGE_REGISTER.csv (PKG-077).
- Scope items covered: `SOW-0143`. Source: `_CONTEXT.md`.
- Objectives supported: `OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010`. Label as **ASSUMPTION — package-grouping heuristic** until OBJECTIVE_DELIVERABLE_MAP.csv is verified at deliverable-ID granularity.

### Step 9 — Cross-check consistency (Pass 2)
Run the four cross-document checks:
- Datasheet entities/tags reflected in Specification requirements where appropriate.
- Specification requirements have rationale/considerations in Guidance.
- Specification requirements have verification approaches.
- Terminology and units are consistent across all four documents.
Resolve in place where possible; otherwise add or update the Guidance Conflict Table and propagate `TBD` rather than guess.

### Step 10 — Update status (safe update only)
If `_STATUS.md` Current State is `OPEN`, update it to `INITIALIZED` with provenance `TASK+four-documents`. Do not regress state. (Mechanism: brief specifies `tools/scaffolding/write_status.sh`; the deliverable-local `Edit` may be substituted when the helper is not invoked.)

### Step 11 — Write run record
Write `_run_records/TASK_RUN_<timestamp>.md` capturing inputs, resolved skill state, tools used, applied changes, missing items, conflicts surfaced for human ruling, and final `run-status`.

## Verification

| Verification check | How |
|---|---|
| All four documents exist (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`). | Directory listing. |
| Default schema sections present in each. | Heading check. |
| Every non-trivial datasheet value cites a source slice or carries `TBD`/`ASSUMPTION` label. | Manual trace. |
| Injection-point list matches DBM-Deepcut L1328 (plus transient L630/L674). | Side-by-side comparison. |
| Equipment tags match DBM L2605-L2606. | Direct match. |
| Interface matrix rows = PACKAGE_REGISTER.csv interface-type list for PKG-077. | Direct match. |
| Conflict Table present in Guidance with CT-1, CT-2, CT-3 entries (or successors). | Read Guidance.md. |
| `_STATUS.md` not regressed. | Read `_STATUS.md`. |

## Records

- The four production documents in `{DeliverablePath}`.
- Updated `_STATUS.md`.
- `_run_records/TASK_RUN_<timestamp>.md`.
- Open items recorded as TBD or as Conflict Table rows pending human ruling.
