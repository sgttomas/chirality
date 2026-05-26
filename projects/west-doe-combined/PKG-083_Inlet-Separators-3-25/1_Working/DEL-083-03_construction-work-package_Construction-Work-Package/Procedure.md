# Procedure — DEL-083-03 Construction Work Package (PKG-083 Inlet Separators 3-25)

## Purpose

Operational procedure for producing the Construction Work Package (CWP) deliverable and for executing the field installation, tie-in, inspection, and turnover of the PKG-083 Inlet Separators 3-25 package within the 03-25 facility scope. The procedure spans both production of the CWP artifact set (per `_CONTEXT.md` anticipated artifacts) and the field execution it controls.

## Prerequisites

### Inputs

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` — read and current.
- Accepted GATE-07 PROJECT_DECOMP snapshot (PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv, INTERFACE_REGISTER.csv).
- DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (SEC-03, SEC-04 in particular).
- 26020-Package_Requirements.docx package heading 36 — to be read at clause level when accessible (binary not parsed in this run; location TBD).
- Bid Docs/Budgetary/26020-02-PT-RFQ-17-003_Inlet Separators 1_R0.docx — to be read when accessible (location TBD).

### Pre-conditions for field execution (downstream)

- Vendor GA, certified loads, and nozzle schedule received from PKG-083 vendor.
- Foundations and saddle anchor patterns built and surveyed.
- Inlet ESDV and upstream pig receiver/isolation in place or staged.
- Facility 4.16 kV/600V power, instrument air (from 04-25), and shared flare/incinerator systems available per facility utility plan.
- Approved isolation, energization, and lift plans.
- Approved Conflict Table rulings (CT-1, CT-2, CT-3 in `Guidance.md`).

### Declared upstream dependencies

None declared during PREPARATION (`_DEPENDENCIES.md`). Run `TASK + dependency-extract` when in-file declarations become necessary.

## Steps

### Phase A — Produce the CWP artifact set (this deliverable's authoring)

A1. Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and the GATE-07 register rows for PKG-083 and DEL-083-03.
A2. Read accessible source slices in DBM-Comp_and_Liquids §SEC-03, §SEC-04, §SEC-06, §SEC-10.
A3. Populate `Datasheet.md` with package identification, attributes, conditions, and construction interface data, source-grounded with citations and `TBD` markers where not supported.
A4. Populate `Specification.md` requirements R1–R13 against the EPC-Integrator interface list in PACKAGE_REGISTER.csv row PKG-083 and the DBM slices.
A5. Populate `Guidance.md` with principles, considerations, trade-offs, and the Conflict Table (CT-1, CT-2, CT-3).
A6. Populate this `Procedure.md`.
A7. Cross-check terminology and numeric values across the four documents (Pass 2).
A8. If `_SEMANTIC_LENSING.md` later exists, dispatch Phase 2.5 (`RUN_PASSES: P3_ONLY`).

### Phase B — Pre-field engineering (CWP detailing)

B1. Resolve Conflict Table items CT-1, CT-2, CT-3 with human ruling; update affected sections.
B2. Read clause-level text from 26020-Package_Requirements.docx heading 36 and the Bid Docs RFQ when available; reconcile against Specification R1–R13.
B3. Produce the Installation and Tie-in Workface Plan (FIWP-level), broken by interface type per Specification R2–R12.
B4. Produce the Construction Interface and Turnover Checklist aligned to the Verification table in `Specification.md`.
B5. Identify hold points, NDE requirements, and inspection responsibilities for sour-service welds and nozzle tie-ins.

### Phase C — Site receipt and pre-installation

C1. Receive separator packages V-1600-2 and V-1700-2; record shipping damage; verify vendor caps/bags on mist eliminators, nozzles, and instrumentation.
C2. Inspect internal Devchem 253 coating via available access (e.g., manway) per the vendor's allowance.
C3. Confirm foundation readiness: anchor pattern survey, elevation, and grout requirements per vendor GA.

### Phase D — Setting and anchoring

D1. Execute approved lift plan; set each separator on foundations within tolerance.
D2. Anchor and grout per vendor and structural drawings.
D3. Verify levelness and alignment relative to inlet/outlet nozzles.

### Phase E — Tie-in execution (by interface type)

E1. Process Piping (R2): fabricate symmetric inlet header; install parallel inlet PCV manifold (>=2 valves) and parallel produced-water LCV manifold (>=2 valves); tie in drive-gas recycle line; bolt up and weld per piping line list; hydrotest.
E2. Utility Piping (R3): connect instrument air, fuel gas if required at package, and methanol provisions at the separator boot; downstream methanol disposition flagged TBD per Guidance.
E3. Relief / Flare / Vent (R4): tie PSV outlets and any package vents to the shared flare/incinerator headers per facility allocation.
E4. Drain / Containment (R5): connect closed and open drains; verify slope and containment.
E5. EHT (R6): install heat tracing per EHT line list (location TBD); commission later.
E6. Grounding / Bonding (R7): install grounds and bonds per facility grounding standard.
E7. Area / Exterior Lighting (R8): install lighting per facility lighting plan.
E8. I&C / Control Cabling (R9): pull and terminate field instrument cabling; perform loop checks.
E9. Fire & Gas / Safety Systems (R10): install F&G detectors per layout; terminate ESDV interlocks; functional test.
E10. Maintenance Access (R11): confirm clearance for manway, mist eliminator removal, weir adjustment, and de-sanding access remains intact post-installation.
E11. Structural / Foundations / Supports (R12): install piping supports, access platforms, ladders.

### Phase F — Mechanical completion and turnover

F1. Execute the Construction Interface and Turnover Checklist; close all hold points.
F2. Compile test and inspection records (hydrotest, NDE, loop checks, ESDV strokes, F&G calibrations, ground readings).
F3. Walk down with the Vendor Package Review and Acceptance team (consumer deliverable family DEL-*-06) and operations.
F4. Issue punch list; clear A-items; hand over to commissioning.

## Verification

- Phase A verification: all four documents exist; default schema sections present; cross-document terms and values consistent; non-trivial claims source-cited or marked `TBD`.
- Phase B verification: workface plan and turnover checklist reference Specification R-IDs; hold points and NDE plan reviewed.
- Phase C–F verification: per the Verification table in `Specification.md`.
- ESDV functional test: confirm inlet separator ESDV trips at the 635 psig basis (delivery-point ESDV value is TBC per DBM).
- Symmetry verification: as-built inlet piping isometrics confirm equivalent run length/fittings to V-1600-2 and V-1700-2 (or document deviations).

## Records

- The four CWP documents (this `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`).
- Installation and Tie-in Workface Plan.
- Construction Interface and Turnover Checklist (executed/signed).
- Test/Inspection evidence package: hydrotest reports, NDE reports, loop check sheets, ESDV stroke and interlock test records, F&G calibration sheets, ground-resistance readings, EHT commissioning records.
- Coating inspection records (Devchem 253).
- Punch list and Turnover Certificate.
- Run record: `_run_records/TASK_RUN_2026-05-24_2348.md`.
