# Procedure: DEL-046-03 — Construction Work Package (Acid Gas Compressors)

This Procedure describes the operational sequence the EPC Integrator follows to produce, execute, and turn over the Construction Work Package for `PKG-046` Acid Gas Compressors. Where source basis is silent, steps are labeled `TBD` rather than invented.

## Prerequisites

- Accepted GATE-07 PROJECT_DECOMP snapshot referenced in `_CONTEXT.md`.
- `4-25_Deepcut_DBM.md` SEC-01 Construction Responsibility assignment and SEC-05 acid gas compressor design basis available to the construction team.
- Final geotechnical report accepted (foundation design otherwise remains placeholder per `3-25_Comp_and_Liquids_DBM.md` SEC-02).
- Vendor-Engineered Equipment Package definition from `DEL-046-04` (module count, weights, lift points, shipped-loose list) — currently TBD.
- Vendor Document Turnover Package from `DEL-046-05` available for hookup reference.
- BCER Section 12.4 site alteration permit and waste discharge permit amendment in force (`4-25_Deepcut_DBM.md` SEC-01 Permitting).
- Confirmed ISBL/OSBL tie-in responsibility matrix per R-3, R-7, R-8.
- Hazardous-area classification deliverable accepted: **TBD**.
- No declared upstream/downstream dependencies recorded in `_DEPENDENCIES.md` at PREPARATION; CWP execution is dependency-coupled in practice to `DEL-046-02` (Package Datasheet) and `DEL-046-04` (Vendor Engineered Equipment Package) — to be formalized via `dependency-extract` skill.

## Steps

### Step 1 — Construction Work Package authoring (EPC office scope)
1.1 Compile work package from this Specification, the accepted Package Datasheet (`DEL-046-02`), and vendor data (`DEL-046-04`, `DEL-046-05`).
1.2 Produce the installation and tie-in workface plan (anticipated artifact, `_CONTEXT.md`).
1.3 Produce the construction interface and turnover checklist (anticipated artifact, `_CONTEXT.md`).
1.4 Reconcile assignment of activities against `4-25_Deepcut_DBM.md` SEC-01 Construction Responsibility table; record any deviations.
1.5 Obtain Tourmaline concurrence on field-construction scope and tie-in plan (R-1, R-8).

### Step 2 — Site preparation and foundations (field, Tourmaline scope)
2.1 Grading, piling, and foundation work per accepted geotechnical report (`4-25_Deepcut_DBM.md` SEC-01; foundations basis subject to `3-25_Comp_and_Liquids_DBM.md` SEC-02).
2.2 Survey-control verification of compressor footprint, cooler bank, and tie-in stub locations.
2.3 Foundation acceptance ITR sign-off prior to module receipt.

### Step 3 — Module receipt, off-loading, and setting
3.1 Coordinate shipping logistics with vendor (module count TBD; lift plan governed by vendor data sheet — TBD).
3.2 Off-load and set compressor packages (2 operating + 1 spare), cooler bundles, and scrubber skids on prepared foundations per R-1, R-2.
3.3 Grout and torque per vendor procedure; allow grout cure before reciprocating-load application.
3.4 Setting survey acceptance ITR.

### Step 4 — Mechanical and piping hookup
4.1 Install ISBL interconnecting piping per R-3 to tie-in points; segregate hydrotest groups by stage MAWP per R-9.
4.2 Install shipped-loose instruments, valves, and components (count TBD) per R-2.
4.3 Install packing-drain and vent header to common seal pot; route seal-pot vapour to VRU suction header (R-4, per `4-25_Deepcut_DBM.md` SEC-05).
4.4 Install blowdown valve (fail-open, downstream of final aftercooler), HP and LP recycle valves (fail open, no manual isolation), and recycle piping (R-6).
4.5 Confirm sour-service material conformance via MTR reconciliation (R-4).

### Step 5 — Electrical and instrumentation hookup
5.1 Install home-run cables and terminate at MCC/VFD and at compressor package junction boxes (R-1 per `4-25_Deepcut_DBM.md` SEC-01).
5.2 Terminate and verify 1,300 hp VFD-driven 8-pole induction motor power, control, and protection wiring (per `4-25_Deepcut_DBM.md` SEC-05 driver basis).
5.3 Install area lighting and security/fencing within `PKG-046` footprint.
5.4 ESD and cause-and-effect wiring termination; bench-verify recycle and blowdown valve fail positions (R-6, R-9).

### Step 6 — Pre-commissioning
6.1 Hydrotest by MAWP-segregated groups (test code: ASME B31.3 ASSUMPTION pending standards register confirmation; test pressures derived from stage MAWP per `4-25_Deepcut_DBM.md` SEC-05).
6.2 Lube-oil flush and electric circulating heater commissioning.
6.3 Motor solo-run, rotation verification, megger, and continuity.
6.4 Instrument loop checks; ESD function test.
6.5 Packing-vent integrity test; seal-pot drain function verification.
6.6 Cooler functional test: actuated louver control, warm-air recirculation, freeze-prevention heat-medium loop (per `4-25_Deepcut_DBM.md` SEC-05 cooler basis).

### Step 7 — Tie-in execution
7.1 Joint planning meeting per R-8; confirm tie-in window with Tourmaline and adjacent EPC packages.
7.2 Execute tie-ins under approved work permits.
7.3 Acid gas injection pipeline tie-in: terminate EPC scope at facility tie-in point; install blind/spade per R-7; obtain pipeline operator acceptance signature.
7.4 Walkdown all ISBL/OSBL boundaries against responsibility matrix (R-3).

### Step 8 — Mechanical completion and turnover
8.1 Punchlist generation and disposition.
8.2 Compile Turnover Package per R-10 (as-built redlines, ITRs, hydrotest certificates, loop check records, motor records, calibration records, construction interface and turnover checklist).
8.3 Turnover Package acceptance signature from Tourmaline.
8.4 Mechanical Completion certificate issued; system handed to commissioning team.

## Verification

| Verification Activity | Criterion | Evidence Record |
|---|---|---|
| Foundation acceptance | Survey within vendor tolerance; geotechnical conformance | Foundation ITR (Step 2.3) |
| Module setting | Vendor-tolerance alignment; grout cure complete | Setting survey ITR (Step 3.4) |
| Piping hydrotest | Pass at stage-specific MAWP test pressure with no leakage | Hydrotest certificate (Step 6.1) |
| Sour-service material conformance | All MTRs reconciled; no non-conformance open | MTR reconciliation log (Step 4.5) |
| Recycle/blowdown configuration | Fail positions bench-verified; manual isolation correctly absent on recycle valves | Bench-test record (Step 5.4) |
| Motor and VFD | Rotation, megger, continuity all within spec | Motor commissioning record (Step 6.3) |
| ESD and cause-and-effect | Function test passes per cause-and-effect matrix | ESD function test record (Step 6.4) |
| Packing-vent integrity | No leak at test pressure; seal pot drains | Packing-vent test record (Step 6.5) |
| Tie-in execution | All tie-ins per joint plan; downstream pipeline operator signature obtained | Tie-in walkdown report (Step 7.4) |
| Turnover acceptance | Turnover Package signed by Tourmaline | Turnover acceptance signature (Step 8.3) |

## Records

The following records shall be retained as the Construction Turnover Package (R-10):

- Construction Work Package (this document set + execution plan)
- Installation and tie-in workface plan
- Construction interface and turnover checklist
- All ITRs identified in the Verification table
- Hydrotest certificates by MAWP-segregated group
- As-built redline package (piping isometrics, single-line diagrams, instrument loops)
- Punchlist with disposition status
- Material Test Reports (MTRs) for sour-service materials
- Cable schedules and termination records
- Loop check records
- Motor solo-run, megger, and continuity records
- Calibration records for installed instruments
- ESD function-test record and cause-and-effect verification
- Tie-in approval signatures (ISBL/OSBL responsibility matrix, acid-gas injection pipeline tie-in)
- Mechanical Completion certificate
