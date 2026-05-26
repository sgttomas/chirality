# Procedure — DEL-099-02 Package Datasheet (Truck Product Loading Unit 3-25)

Pass set: P1_P2 (drafted 2026-05-25 by TASK+four-documents)

## Purpose

This procedure describes how to **produce** the Package Datasheet for `PKG-099 — Truck Product Loading Unit 3-25` (vendor package `26020-03-PT-23-001 — Condensate Truck Loading Stations`) and how to **maintain** it through tender, vendor selection, and engineering. It is operational: it tells the EPC Integrator's package engineer the order of work, where each fact comes from, and what evidence to preserve.

## Prerequisites

- Read access to deliverable folder `DEL-099-02_package-datasheet_Package-Datasheet` and its metadata files (`_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`).
- Read access to `_Sources/26020-Package_Requirements.docx` (authoritative package scope, Heading1 `26020-03-PT-23-001`).
- Read access to `_Sources/26020-Packages_Interfaces_4_export.xlsx` (interface workbook) — required to reconcile row 98 / col M mapping. **TBD**: confirm the version reference (`.3.xlsx` → `_4_export.xlsx`).
- Read access to RFQ `RFQ/Bid Docs/26020-03-PT-RFQ-23-001_Truck_Load_stn_R0.docx` — **location TBD** within the project file tree.
- Access to Gate 7 published decomposition snapshot `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (frozen reference).
- Declared upstream/downstream dependencies: none (per `_DEPENDENCIES.md`). Coordination is DECLARED-mode; advisory only.

## Steps

### Step 1 — Establish identity and scope

1. From `_CONTEXT.md`, copy DeliverableID, Name, ParentPackageID, Discipline, Type, ResponsibleParty into Datasheet §Identification.
2. Locate the matching package in `_Sources/26020-Package_Requirements.docx` by searching for the package title and confirming the Heading1 vendor tag (`26020-03-PT-23-001 — Condensate Truck Loading Stations`). Record the vendor tag and managing project (`26020-03 3-25 Liquids Hub`).
3. Record source basis: `RFQ/Bid Docs/26020-03-PT-RFQ-23-001_Truck_Load_stn_R0.docx`.

### Step 2 — Extract Basic Scope and Function

1. Transcribe §Basic Scope into Datasheet §Attributes (Function row) and Specification §REQ-099-02-11 verbatim.
2. Verify the upstream source (Condensate Storage Tanks) and the conveyance (Truck Loading pumps) appear consistently in §Attributes and §Specification.

### Step 3 — Extract Major Included Equipment

1. Transcribe §Major Included Equipment into Datasheet §Major Included Equipment. Preserve vendor part numbers verbatim (e.g., Sureflow `0300BF300SS`).
2. Mark ESDV quantity and flow transmitter accuracy class as **TBD** unless the source supplies them.

### Step 4 — Extract Design Conditions and Scope Notes

1. From §Scope Notes, capture: design rate per station (103 m³/h), total header flow (415 m³/h, 4 lines), and the By-Others list (shipping, installation on piles, tie-in piping, electrical connections, mounting platform/stairs).
2. Note arithmetic discrepancy (4 × 103 ≠ 415) in the Guidance Conflict Table (`C-002`); do not silently reconcile.
3. Where source says "Capacity/design throughput: -" or "Operating conditions: See design conditions", carry that literal phrasing as a TBD rather than fabricating values.

### Step 5 — Transcribe Physical Interface Summary

1. Build the Datasheet §Physical Interface Summary table 1:1 from source §Physical Interface Summary.
2. Preserve the explicit source citation embedded in the Area/Exterior Lighting row (`26020-Packages_Interfaces.3.xlsx column M (row 98)`).
3. Validate this citation against `_Sources/26020-Packages_Interfaces_4_export.xlsx`. If row 98 / column M no longer corresponds, log in Guidance Conflict Table `C-003`.

### Step 6 — Compile Vendor Engineering Deliverables list

1. Transcribe each Deliverable ID and Deliverable Name from source §Vendor Engineering Deliverables into Specification §REQ-099-02-40, preserving source's category groupings (Core vendor documents; Core package engineering; Loading/metering package; Process piping; Drainage/containment; Electrical/lighting/EHT/grounding; I&C; F&G; Structural; Civil).
2. Do not add or remove deliverables relative to source.

### Step 7 — Capture Interface Coordination Notes (if any)

1. From source §Interface Coordination Notes (heading 18547), transcribe content. If source value is "TBD", record TBD in Datasheet §Open Items and Guidance Conflict Table `C-005`.

### Step 8 — Cross-document consistency sweep (Pass 2)

1. Confirm Datasheet §Identification, §Attributes, §Major Included Equipment, §Design Conditions, §Physical Interface Summary are all reflected in Specification REQs.
2. Confirm Specification §Verification table maps every numbered REQ to a verification approach.
3. Confirm Guidance §Considerations explains every non-obvious decision (custody-transfer deferral; ESDV/SIL deferral; interface-workbook version drift; Maintenance Access "No" interpretation; per-station vs. header arithmetic).
4. Confirm Conflict Table entries `C-001`..`C-005` are present and source-cited.

### Step 9 — Update `_STATUS.md`

1. Run `bash tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` (only when current state is `OPEN`).

### Step 10 — Write run record

1. Author `_run_records/TASK_RUN_2026-05-25_<HHMM>.md` summarising: pass set executed, sources read, files written, RUN_STATUS, open TBDs.

## Verification

| Check | Pass criterion | Evidence |
|---|---|---|
| Four documents present | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` exist in `DELIVERABLE_PATH`. | Directory listing |
| Default schema sections present | Datasheet (Identification, Attributes, Conditions, Construction, References); Specification (Scope, Requirements, Standards, Verification, Documentation); Guidance (Purpose, Principles, Considerations, Trade-offs, Examples); Procedure (Purpose, Prerequisites, Steps, Verification, Records). | Section headings |
| Source-grounded | Each non-trivial value cites `26020-Package_Requirements.docx` §, the interface workbook row/col, or is labelled TBD/ASSUMPTION. | Inline citations |
| Conflict Table present | Guidance §Conflict Table contains entries `C-001`..`C-005` with PROPOSAL + TBD ruling columns. | Guidance.md |
| Status safely updated | `_STATUS.md` shows `Current State: INITIALIZED` only if previous state was `OPEN`. | `_STATUS.md` |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this run).
- `_STATUS.md` updated `OPEN → INITIALIZED` (via `write_status.sh`).
- `_run_records/TASK_RUN_2026-05-25_<HHMM>.md` (this run's evidence file).
- Source slices consulted (for run record):
  - `_Sources/26020-Package_Requirements.docx` Heading1 `26020-03-PT-23-001` (paragraph indices 18191–18547) — §Location/Status, §Source Basis, §Basic Scope, §Major Included Equipment, §Scope Notes, §Physical Interface Summary, §Vendor Engineering Deliverables, §Interface Coordination Notes.
- Sources flagged for follow-up:
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` — row 98 / col M reconciliation **TBD**.
  - RFQ `26020-03-PT-RFQ-23-001_Truck_Load_stn_R0.docx` — local path **TBD**.
