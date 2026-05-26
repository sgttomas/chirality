# Procedure — DEL-061-02 Package Datasheet (PKG-061)

## Purpose

This procedure governs how the **PKG-061 package datasheet** is produced, updated, and verified within the deliverable folder. The datasheet artifact is consumed by package-vendor RFQ/handoff and by downstream discipline integrators.

Interpretation: this procedure describes steps to **produce** the deliverable artifact (the four-document datasheet kit) — not steps to operate the LPG booster pumps.

## Prerequisites

- Accepted upstream decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (per `_REFERENCES.md`).
- `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` present in the deliverable folder.
- `_Sources/26020-Package_Requirements.docx` reachable; package heading `26020-01-PT-18-004 - LPG Booster` (TOC heading 17) readable.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` reachable; row 58 readable.
- PACKAGE_REGISTER.csv row `PKG-061` readable in the gate snapshot.
- No upstream blockers declared (per `_DEPENDENCIES.md`: none declared during PREPARATION).

## Steps

### Step 1 — Establish identity

Populate `Datasheet.md` §Identification from `_CONTEXT.md` and PACKAGE_REGISTER.csv. Confirm PackageID = `PKG-061`, Workbook row 75, Discipline = Mechanical.

### Step 2 — Extract equipment list

From `26020-Package_Requirements.docx` §26020-01-PT-18-004 "Major Included Equipment" and DBM row 58, record the two LPG booster pumps (`P-9570-1`, `P-9580-1`) with their type (vertical multistage can, API 610), seal plan (13/52), and motor service (575 V / 3 ph / 60 Hz).

### Step 3 — Capture process/design conditions

From §"Basic Scope" and §"Scope Notes / Open Items": record service (LPG, storage → LACT), parallel arrangement, 145 m³/h @ 150% capacity, 25 psid / 172 kPad differential, TDH as `TBD`.

### Step 4 — Capture construction attributes

From §"Major Included Equipment": skid, piping, instrumentation, electrical, HVAC/enclosure, CRN/TSBC. Mark materials and area classification `TBD`.

### Step 5 — Capture interface applicability

Apply PACKAGE_REGISTER.csv "ApplicableInterfaceTypes" for PKG-061 to the datasheet interface table. Reflect each row in §"Physical Interface Summary" of the Word source as TBC (row-level details deferred to package-interface deliverable).

### Step 6 — Capture exclusions / by-others

Record "DCS integration, foundations, electrical supply to MCC — by others" from §"Scope Notes / Open Items".

### Step 7 — Enumerate vendor engineering deliverables

Copy the "Vendor Engineering Deliverables" table (core vendor documents; core package engineering; rotating equipment / pumps) from the Word source into `Datasheet.md`.

### Step 8 — Surface conflicts (do not silently reconcile)

Record CONFLICT-01 (NGL vs. LPG service-fluid label), CONFLICT-02 (building scope), CONFLICT-03 (TDH/power TBD) in the Conflict Table in `Guidance.md`.

### Step 9 — Cross-document consistency sweep

Verify Datasheet ↔ Specification ↔ Guidance ↔ Procedure:

- Equipment tags consistent (P-9570-1, P-9580-1).
- Sizing values consistent (145 m³/h, 150%, 25 psid / 172 kPad).
- Standards consistent (API 610, seal plan 13/52, CRN/TSBC).
- TBD register in `Guidance.md` matches `TBD` markers in `Datasheet.md` / `Specification.md`.

### Step 10 — Update `_STATUS.md` (safe update)

If `_STATUS.md` current state is `OPEN`, advance to `INITIALIZED` via `tools/scaffolding/write_status.sh` with method `TASK+four-documents`. Otherwise, do not modify status.

## Verification

| Check | Pass criterion |
|---|---|
| Sources read | `_Sources/26020-Package_Requirements.docx` §heading 17 and DBM row 58 cited in `Datasheet.md` references. |
| All four documents present | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` exist in the deliverable folder. |
| Default schema sections present | Each document carries the default sections defined by the `four-documents` skill. |
| Provenance discipline | Each non-trivial value either cites a source or is labeled `TBD` / `ASSUMPTION`. |
| Conflict surfacing | Conflict Table present in `Guidance.md` with at least CONFLICT-01. |
| Status update | `_STATUS.md` shows `INITIALIZED` if the run started from `OPEN`; otherwise unchanged. |
| Run record | A `_run_records/TASK_RUN_<timestamp>.md` file exists for this run. |

## Records

- `Datasheet.md` (this deliverable)
- `Specification.md` (this deliverable)
- `Guidance.md` (this deliverable, including Conflict Table)
- `Procedure.md` (this file)
- `_STATUS.md` (state advanced when allowed)
- `_run_records/TASK_RUN_<timestamp>.md` (durable run record)

## Downstream use

This datasheet feeds:

- The PKG-061 package-interface deliverable (row-level interface reconciliation against `26020-Packages_Interfaces_4_export.xlsx`).
- Vendor RFQ assembly for the LPG booster pump package (P-9570-1 / P-9580-1).
- EPC Integrator interface coordination across applicable interface types (Process Piping, Utility Piping, Relief/Flare/Vent, Drain/Containment, Electrical Power, EHT, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Building HVAC/Services, Fire & Gas/Safety Systems, Maintenance Access, Structural/Foundations/Supports).
