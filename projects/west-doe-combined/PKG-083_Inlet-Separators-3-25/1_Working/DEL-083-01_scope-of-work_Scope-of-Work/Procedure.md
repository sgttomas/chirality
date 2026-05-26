# Procedure — DEL-083-01 Scope of Work (PKG-083 Inlet Separators 3-25)

**Interpretation:** This Procedure describes steps to **produce** the Scope of Work document for PKG-083, not steps to operate the inlet separator equipment.

## Purpose

Provide a repeatable, source-anchored sequence for assembling, reviewing, and issuing the EPC Scope of Work for the Inlet Separators 3-25 package.

## Prerequisites

- Access to the accepted upstream decomposition snapshot:
  - `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - including `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Access to the governed source basis: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` and `_Sources/DBM-Comp_and_Liquids/Trace_Appendix.md`.
- Access to `26020-Package_Requirements.docx` package heading 36 (DOCX — extraction tooling **TBD**) and `26020-Packages_Interfaces_4_export.xlsx` Workbook Packages row 67 (**TBD**).
- Deliverable-local truth set: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.
- No declared upstream dependencies block this work (per `_DEPENDENCIES.md`).

## Steps

### Step 1 — Confirm deliverable identity and scope items

1. Read `_CONTEXT.md` and confirm DeliverableID, ParentPackageID, ResponsibleParty, Covers Scope Items (SOW-0123..SOW-0126), and Supports Objectives (OBJ-002..OBJ-010).
2. Confirm Discipline = Mechanical and Type = "EPC Scope of Work".
3. Record any deltas against `DELIVERABLE_REGISTER.csv` (GATE-07 snapshot).

### Step 2 — Extract tagged equipment list

1. Read DBM §SEC-04 "Inlet Separation" and extract the package equipment set (V-1600-2, V-1700-2, internals, valves, building).
2. Cross-check against `Trace_Appendix.md` KTY-04-02 Inlet-Separator KAs (KA-06 drive-gas recycle, KA-07 design parameters, KA-08 sweet-gas purge, KA-09 internal coating, KA-10 adjustable weir, KA-11 mist eliminator, KA-12 de-sanding, KA-13 inlet PCV, KA-14 produced-water LCV, KA-15 module and building).
3. Cross-check against `PACKAGE_REGISTER.csv` (GATE-07 snapshot) for any items the register places inside PKG-083 not yet captured. (PACKAGE_REGISTER not extracted in this pass — TBD.)
4. Record tag IDs that are TBD (in-package valves and instrumentation skids).

### Step 3 — Capture per-separator process duty

1. Transcribe DBM §SEC-04 table values into Datasheet.md Attributes: gas/condensate/water flows, diameter, straight-side length, pressure class, design pressure, slug handling, internal coating.
2. Carry "2 x 50%" basis explicitly and note the older "2 x 100%" language is superseded.
3. Transcribe inlet operating pressures (125 / 200 / 572 psig; normal high TBC) and inlet design temperature (8.3 deg C with reconciliation note).

### Step 4 — Define boundaries

1. Draw upstream boundary at the inlet ESDV / pig receiver interface; note Conflict CT-04 if pig-receiver package assignment is unresolved.
2. Draw gas-side downstream boundary at separator-package outlet to inlet compressor suction (KM-2150 / KM-2250).
3. Draw condensate-side boundary at separator condensate outlet to raw-condensate forwarding to 04-25 MPFS.
4. Draw water-side boundary at separator water outlet to liquids hub produced-water transfer.
5. Identify utility tie-ins (fuel gas, instrument air ex 04-25, electrical power, controls) and flare/vent tie-ins.

### Step 5 — Write package function and integration narrative

1. Compose a narrative that ties the package into DBM §SEC-01 "Facility Overview" and the §SEC-01 "Commercial and Facility Interfaces" set.
2. Highlight drive-gas recycle from downstream of inlet compressor aftercoolers (per DBM §SEC-04 "Flow Distribution and Controls" / Trace_Appendix.md KA-06) and its pressure relationship to 04-25 stabilizer flash feed separator pressure.
3. State the package's contribution to objectives OBJ-002..OBJ-010 in directional terms (PACKAGE_HEURISTIC association is an ASSUMPTION; do not commit per-objective acceptance criteria here).

### Step 6 — Build responsibility assignment record

1. Identify EPC Integrator scope (procurement, engineering, package integration, mechanical hookup).
2. Identify owner-furnished items (TBD).
3. Identify vendor-furnished package scope (vessels, internals, in-package valves, instrumentation, building).
4. Identify third-party scope (NRM LACT items excluded except for facility-side tie-in; not applicable to this package's main boundary).
5. Identify 04-25 plant scope at package interfaces (drive-gas recycle source, raw-condensate destination, instrument air supply, MPFS/stabilization downstream).

### Step 7 — Cross-document consistency sweep

1. Verify Datasheet ↔ Specification: every entity in Datasheet Attributes is reflected in at least one Specification Requirement; values match (40 MMSCFD, 4,963 kPag, 600#, etc.).
2. Verify Specification ↔ Guidance: every Specification Requirement has rationale or trade-off in Guidance Principles/Considerations.
3. Verify Specification ↔ Procedure: every Specification Requirement has a verification approach and a procedural touchpoint here (Steps 2-6).
4. Verify terminology: "inlet separator package," "V-1600-2 / V-1700-2," "2 x 50%," "drive-gas recycle," "raw condensate" are used consistently.
5. Verify the Conflict Table in `Guidance.md` covers each unresolved cross-document item.

### Step 8 — Issue and status update

1. Issue the four-document kit and the consolidated Scope of Work for EPC Integrator and owner review.
2. Update `_STATUS.md` from OPEN to INITIALIZED via `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` (this run performs the safe update).
3. Log the run record at `_run_records/TASK_RUN_<timestamp>.md`.

## Verification

| Check | Pass Criterion |
|---|---|
| Identity completeness | DeliverableID, package, discipline, responsible party match `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv`. |
| Equipment list completeness | All V-1600-2 / V-1700-2 in-package items appear; TBD tags explicitly enumerated. |
| Duty consistency | Per-separator process values match DBM §SEC-04 table exactly. |
| Boundary clarity | Upstream, downstream, utility, flare interfaces each have a named flange or signal interface. |
| Sour-service basis | NACE / sour-service language present (with ASSUMPTION label until DBM §SEC-08 citation extracted). |
| TBD discipline | Every TBC / TBD value from DBM is preserved as TBC / TBD in the SoW (no silent values inserted). |
| Conflict ledger | Every cross-source conflict appears in Guidance Conflict Table; none silently resolved. |
| Status update | `_STATUS.md` change reflects safe-update rule (OPEN -> INITIALIZED only). |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this kit)
- Updated `_STATUS.md` (state and history line)
- `_run_records/TASK_RUN_<timestamp>.md` (durable run record)
- Conflict Table entries in `Guidance.md` carried forward for human ruling
- Reconciliation log (older "2 x 100%" language; inlet temperature) — to be produced before equipment datasheets issue (TBD downstream deliverable)
