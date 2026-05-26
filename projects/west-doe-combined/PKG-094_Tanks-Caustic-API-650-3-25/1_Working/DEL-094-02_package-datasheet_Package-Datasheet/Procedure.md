# Procedure — Package Datasheet (PKG-094 Tanks, Caustic API 650 3-25)

> Status: INITIALIZED. Procedure for *producing* the Package Datasheet (EPC Integrator
> workflow), with hooks to verification of the Specification.

## Purpose

Produce the EPC Integrator Package Datasheet for PKG-094 that hands off to the Package
Vendor for tank engineering, design, fabrication, and supply.

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` initialized (already complete per
  PREPARATION).
- GATE-07 PROJECT_DECOMP snapshot accessible:
  `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- 3-25 DBM (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) readable.
- 26020 Package_Requirements vendor RFQ Word source available (`location TBD` if not
  parsable in current environment — must be parsed before deliverable acceptance).
- Sibling deliverable DEL-094-01 (Scope of Work) at INITIALIZED or later (declared
  upstream is none, but content alignment is needed at consistency check).

## Steps

### Step 1 — Pull identity and package basis
1.1 Read `_CONTEXT.md` and confirm DeliverableID, PackageID, vendor package number.
1.2 Pull the PKG-094 row from `PACKAGE_REGISTER.csv` (package title, vendor number,
   function statement, owner split).
1.3 Pull the DEL-094-02 row from `DELIVERABLE_REGISTER.csv` (anticipated artifacts).

### Step 2 — Extract source-grounded design basis
2.1 Read DBM §Scope Inclusions (line 40) for the caustic tank line-item and capacity.
2.2 Read DBM §Condensate Mercaptan Treating (lines 389-402) for fluid composition,
   blanket, heating, insulation, vent routing, aluminum prohibition.
2.3 Read DBM §Drains (line 493) for caustic drain pressure/temperature and 300# governance.
2.4 Read DBM §Site Location, §Ambient, §Wind/Snow/Precipitation, §Geotechnical for
   environmental basis (capture clause references; numeric extraction is a separate task).
2.5 If 26020-Package_Requirements.docx package heading 46 is locally parsable, extract
   vendor-RFQ-derived requirements and reconcile to DBM-derived requirements. If not,
   record `location TBD` and surface in Conflict Table CONF-094-02-006.

### Step 3 — Populate Datasheet
3.1 Fill Identification, Package Function and Scope, Tank Attributes, Process Design
   Conditions, Materials and Construction, Nozzles and Connections tables in
   `Datasheet.md`.
3.2 Mark every non-source-supported value as `TBD`. Mark every inferred value as
   `ASSUMPTION`. Preserve all DBM `TBC` markers.
3.3 Populate the Interface Summary table from `INTERFACE_REGISTER.csv` (PKG-094 rows).

### Step 4 — Populate Specification
4.1 Convert each design basis item from Step 2 into a normative R# clause.
4.2 Map each clause to a verification approach (vendor document review, P&ID review,
   piping class review, HAZOP review, etc.).
4.3 List standards, marking inaccessible ones as `location TBD`.

### Step 5 — Populate Guidance and surface conflicts
5.1 Draft Principles, Considerations, Trade-offs grounded in the source slices used.
5.2 For every irreconcilable item, create a Conflict Table row with Conflict ID,
   sources, impacted sections, and a PROPOSAL; mark Human Ruling as `TBD`.

### Step 6 — Cross-document consistency check (Pass 2)
6.1 Verify every Datasheet attribute with a numeric value is reflected in a Specification
   requirement (or explicitly excluded).
6.2 Verify every Specification requirement has a Verification entry.
6.3 Verify terminology is consistent: "fresh caustic tank", "spent caustic tank",
   "caustic drain", "incinerator header", "LP fuel-gas blanket".
6.4 Verify numeric values (400 bbl, 50 wt%, SG 1.75 TBC, 300# ANSI, 121 °C / 250 °F TBC,
   80 °F, 32 oz/in²) match across documents.

### Step 7 — Status update
7.1 If `_STATUS.md` Current State is `OPEN`, run:
   `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`
7.2 Otherwise, do not modify `_STATUS.md`.

### Step 8 — Pass 3 (deferred)
8.1 Pass 3 (semantic lensing enrichment) is dispatched separately by the ORCHESTRATOR
   once `_SEMANTIC_LENSING.md` exists (Phase 2.5). Do not attempt Pass 3 in this run.

## Verification

| Step | Verification |
|---|---|
| Step 1 | DeliverableID, PackageID, vendor number on Datasheet match PACKAGE_REGISTER.csv |
| Step 2 | Every quoted DBM value carries a line-level source reference |
| Step 3 | All four default Datasheet sections present (Identification, Attributes, Conditions, Construction, References) |
| Step 4 | All four default Specification sections present (Scope, Requirements, Standards, Verification, Documentation) |
| Step 5 | All four default Guidance sections present (Purpose, Principles, Considerations, Trade-offs, Examples) plus Conflict Table |
| Step 6 | Cross-document terminology and numeric values pass consistency check or are captured as conflicts |
| Step 7 | `_STATUS.md` shows `INITIALIZED` only if it was previously `OPEN` |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- `_STATUS.md` updated to `INITIALIZED` (if previously `OPEN`).
- `_run_records/TASK_RUN_<timestamp>.md` documenting this run.
- Conflict Table entries (CONF-094-02-001 through CONF-094-02-006) in `Guidance.md`
  pending human ruling.
