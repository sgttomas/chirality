# Specification: Construction Work Package

## Scope

This specification defines the EPC Integrator Construction Work Package (CWP) for `PKG-078` Pig Receivers (Inlet) 4-25 at the 04-25 West Doe Deepcut expansion facility. The CWP governs physical installation, construction, inspection, turnover, and tie-in of three pig receiver skids (PR-1010-1, PR-1020-1, PR-1030-1) with associated HIPPS packages into the larger 04-25 facility (`_CONTEXT.md`; `SCOPE_LEDGER.csv` `SOW-0161`-`SOW-0164`; `4-25_Deepcut_DBM.md` line 585, Package Line-Item Requirements row 61).

In scope:
- Receiver and HIPPS skid setting on EPC-provided foundations.
- Pipeline / pigging tie-in to the incoming plant inlet pipeline and to facility process piping toward the inlet separators, including barred tees and full-port pig-handling isolation (`4-25_Deepcut_DBM.md` line 585; `SCOPE_LEDGER.csv` `SOW-0163`).
- Tie-ins for Process Piping; Relief/Flare/Vent (HP flare); Drain/Containment; Electrical Power; EHT; I&C / Control Cabling; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports (`INTERFACE_REGISTER.csv` `PKG-078` rows).
- Sweet-gas purge supply tie-in to the pig receiver barrel purge connection (`4-25_Deepcut_DBM.md` line 585; `SCOPE_LEDGER.csv` `SOW-0163`).
- HIPPS package mechanical and instrument hookup and pre-commissioning support (`SCOPE_LEDGER.csv` `SOW-0163`).
- Construction interface and turnover checklist generation and execution (`DELIVERABLE_REGISTER.csv` row `DEL-078-03_construction-work-package`).

Out of scope (by others / addressed by other deliverables):
- Vendor package engineering, design, fabrication, and supply of the receiver and HIPPS equipment (`DEL-078-04_vendor-engineered-equipment-package`).
- Vendor documentation and turnover submittals (`DEL-078-05_vendor-document-turnover-package`).
- EPC vendor package review and acceptance evidence (`DEL-078-06_epc-vendor-package-review-and-acceptance`).
- "By others" items called out in SOW-0164: interconnecting piping; DCS integration; foundations (EPC-furnished but separate civil/structural scope); electrical supply to MCC.

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| R-01 | The CWP shall sequence installation and tie-in of three (3) identical pig receiver skids (PR-1010-1, PR-1020-1, PR-1030-1), each receiver 610 mm OD (24 in.). | `SCOPE_LEDGER.csv` `SOW-0162`, `SOW-0163`; `4-25_Deepcut_DBM.md` Package Line-Item Requirements row 61 |
| R-02 | Skids shall be installed on EPC-provided dedicated structural-steel non-enclosed foundations; no enclosure construction is part of this CWP. | `SCOPE_LEDGER.csv` `SOW-0163`; `4-25_Deepcut_DBM.md` line 585 |
| R-03 | Upstream isolation valves or ESDVs on the receiver inlet skid shall be installed and configured as full-port for pigging; the CWP shall verify full-port orientation and signal continuity at turnover. | `4-25_Deepcut_DBM.md` line 585; `SCOPE_LEDGER.csv` `SOW-0163` |
| R-04 | Barred tees shall be installed where required to prevent pigs from entering facility piping; the CWP shall include a barred-tee installation and inspection check. | `4-25_Deepcut_DBM.md` line 585 |
| R-05 | A low-pressure sweet fuel-gas purge connection shall be installed downstream of the manual isolation valve at each receiver to enable barrel purge before opening for pig retrieval. | `4-25_Deepcut_DBM.md` line 585; `SCOPE_LEDGER.csv` `SOW-0163` |
| R-06 | Each pig receiver vent shall be tied into the HP flare system; vent line routing, sizing, and slope shall be verified and documented at turnover. Set pressure(s) for relief: TBD (not in accessible sources). | `4-25_Deepcut_DBM.md` line 585; `SCOPE_LEDGER.csv` `SOW-0163` |
| R-07 | Each receiver skid HIPPS package shall be installed with two upstream ESDVs (initiator + redundancy), pneumatic hi-low shutoffs, a pressure control valve, and outlet pressure transmitter, integrated to PID control that maintains inlet separator pressure within limits. Final HIPPS setpoints, SIL allocation, and proof-test intervals: TBD - to be confirmed by detailed engineering. | `SCOPE_LEDGER.csv` `SOW-0163`; `4-25_Deepcut_DBM.md` line 809 |
| R-08 | Materials and welding shall be qualified for sour service at H2S design of 1.0 mol%; CWP shall verify weld procedure specifications (WPS), procedure qualification records (PQR), and hardness/NACE compliance per project mechanical/piping specs. Specific NACE/ISO spec: location TBD. | `SCOPE_LEDGER.csv` `SOW-0163`, `SOW-0164`; `4-25_Deepcut_DBM.md` Inlet Contaminant table (line 419) |
| R-09 | Pressure test (hydrostatic or pneumatic per project piping spec) shall be witnessed and documented for each receiver assembly and its tie-in piping prior to introduction of process media. Test pressures and procedure: TBD - per project piping specification. | ASSUMPTION (industry practice + project conventions); not explicit in accessible sources |
| R-10 | Electrical Power tie-in shall connect skid-mounted electrical loads to facility power; supply from MCC is by EPC under separate scope (SOW-0164), and CWP shall coordinate energization sequencing. | `SCOPE_LEDGER.csv` `SOW-0164`; `INTERFACE_REGISTER.csv` `IFC-F2CC0221E0` |
| R-11 | EHT (electric heat trace) shall be installed on identified piping per heat-trace design; coverage map, terminations, and continuity test shall be recorded. Heat-trace circuit list: TBD - per EHT design. | `INTERFACE_REGISTER.csv` `IFC-9313950850` |
| R-12 | I&C / Control Cabling shall be installed to vendor termination drawings; DCS integration is by others (SOW-0164). CWP shall verify cable runs, terminations, loop integrity, and signal handoff at the facility marshalling termination. | `SCOPE_LEDGER.csv` `SOW-0164`; `INTERFACE_REGISTER.csv` `IFC-99C4B8C9E0` |
| R-13 | Drain / Containment tie-ins shall route receiver and skid drains to the appropriate facility closed drain or containment system; tie-in route: TBD - per facility drain design. | `INTERFACE_REGISTER.csv` `IFC-17309B535C` |
| R-14 | Grading / Site Drainage / Spill Containment around each skid shall match the facility civil grading and spill-containment design; CWP shall include a pre-set grading acceptance check. | `INTERFACE_REGISTER.csv` `IFC-3894C2DC14` |
| R-15 | Maintenance Access shall be preserved for pig handling, closure operation, and skid maintenance lifts; clearances per vendor maintenance drawings (clearance values: TBD). | `INTERFACE_REGISTER.csv` `IFC-A553991A6E` |
| R-16 | A construction interface and turnover checklist shall be generated, executed, and closed for each receiver skid before mechanical completion. | `DELIVERABLE_REGISTER.csv` row `DEL-078-03_construction-work-package` |

## Standards

| Standard / Code | Applicability | Status |
|---|---|---|
| Project piping specification(s) (sour-service class for inlet gathering at MAWP 1440 psig TBC) | Welding, NDE, materials, hydrotest | location TBD - cited by SOW-0164 as design basis; specific project spec ID not accessible. |
| NACE MR0175 / ISO 15156 (sour-service materials) | Material/hardness selection for H2S 1.0 mol% sour service | ASSUMPTION: likely applicable for sour service; location TBD. |
| ASME B31.3 (process piping) | Tie-in piping design, fabrication, and testing | ASSUMPTION: standard project basis for facility piping; location TBD. |
| Applicable HIPPS functional-safety standard (IEC 61511 / IEC 61508) | HIPPS package SIL design, proof-test, and certification | ASSUMPTION: standard basis for HIPPS in process facilities; setpoints/SIL TBD per `4-25_Deepcut_DBM.md` line 809. |
| Project EHT design specification | EHT installation and acceptance | location TBD. |
| Project welding procedure specifications / PQRs | Field-weld qualification | location TBD. |

## Verification

| Requirement | Verification approach |
|---|---|
| R-01 | Installation log records 3 skids set, tags PR-1010-1 / PR-1020-1 / PR-1030-1 confirmed against vendor nameplates. |
| R-02 | Foundation acceptance record; skid set on EPC foundation; absence of enclosure confirmed by inspection. |
| R-03 | Isolation/ESDV bore inspection prior to install; valve datasheet review; pig-passage clearance verification. |
| R-04 | Visual inspection and ITP sign-off of barred-tee installations per IFC drawing. |
| R-05 | Sweet-fuel-gas purge tie-in pressure test and isolation function check. |
| R-06 | HP flare tie-in pressure test, slope check, and absence-of-pocket verification; vent path traced and recorded. |
| R-07 | HIPPS loop test (function and trip times); upstream ESDV stroke tests; PT calibration; PCV stroke test; PID interaction with inlet separator pressure simulated. SIL proof-test: TBD. |
| R-08 | Review of WPS/PQR coverage; hardness survey on representative welds; sour-service material certificate review. |
| R-09 | Hydrostatic or pneumatic pressure-test record per project piping spec for each receiver assembly and tie-in piping. |
| R-10 | Electrical megger / continuity tests; coordinated energization with MCC scope. |
| R-11 | EHT continuity, insulation, and as-installed coverage record. |
| R-12 | Loop checks from field device to marshalling cabinet termination; sign-off acknowledged by DCS-integration party. |
| R-13 | Drain tie-in pressure / function test per project drain spec. |
| R-14 | Grading and spill-containment as-built check vs. civil drawings. |
| R-15 | Maintenance-access walk-down with operations representative; clearance measurements recorded. |
| R-16 | Signed construction interface and turnover checklist for each receiver skid. |

## Documentation

Construction-phase records to be produced and turned over:
- Construction work package (this CWP) issued for construction (IFC)
- Installation and tie-in workface plan (`DELIVERABLE_REGISTER.csv` row `DEL-078-03_construction-work-package` anticipated artifacts)
- Construction interface and turnover checklist (per skid)
- Inspection-test plan (ITP) records (welding, NDE, hydrotest, hardness)
- HIPPS loop-test and function-test records
- EHT continuity / insulation records
- Loop-check records (I&C)
- Foundation acceptance records (interface with EPC civil scope)
- Punch list and mechanical-completion record
