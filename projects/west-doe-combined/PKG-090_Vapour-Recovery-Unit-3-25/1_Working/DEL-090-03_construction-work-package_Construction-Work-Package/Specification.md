# Specification: DEL-090-03 — Construction Work Package (Vapour Recovery Unit 3-25)

## Scope

### In scope (EPC Integrator construction scope)

This Construction Work Package (CWP) defines how the PKG-090 Vapour Recovery Unit (two 100%-capacity electric-drive VRU compressor packages, one building, lead-lag) is received, set, installed, connected, inspected, tested, and turned over inside the 03-25 West Doe Compressor Station and Liquids Hub. The scope covers all EPC Integrator-owned work between vendor package delivery at site and commissioning handover, including:

- Receipt, offloading, transport-to-foundation, and setting of the VRU building / compressor trains on piles (`26020-01-PT-12-002` scope notes: "By others: Shipping compressor packages to site, installation on piles, tie-in piping, electrical, instrumentation" — i.e. these items are vendor-excluded and therefore EPC-included).
- Process piping tie-ins: VRU suction header from condensate and produced-water tank vapour systems and selected process vents; VRU discharge routed to the 04-25 SOC suction (per SCA-002); LP flare bypass V-ball valve and suction-header free-drain to flare KO interface (DBM SEC-06).
- Utility piping tie-ins: LP fuel-gas to make-up/blanket regulator and to Plan-53 seal buffer supply; instrument air (from 04-25 per SCA-006); other vendor-listed utility connections.
- Relief / flare / vent tie-ins: primary seal vent to LP flare; PSV discharge routing; integration with the HP/Cryo and LP dual flare stack and applicable KO drum manifolds (DBM SEC-05/SEC-08).
- Drain / containment tie-ins: closed drain and packing-drain/seal-pot connections per vendor package design (cross-reference DBM SEC-05 compressor packing drain routing).
- Electrical power, EHT, grounding/bonding, and area/exterior lighting tie-ins for the VRU trains and building, including motor power feed to each 200 HP VFD driver.
- I&C / control cabling tie-ins from vendor package to facility DCS / SIS marshalling; package vendor interface specification (CTL-026) governs signal list and protocol.
- Fire and Gas / safety system tie-ins for the VRU building (detectors, alarms, ESD interfaces).
- Structural foundations and supports: pile-supported foundation under the VRU building/skids; anchor bolts and embedments per vendor STR-013.
- Maintenance access provisions (platforms, removal routes for compressor internals).
- Construction QA/QC, hydrotest and flushing of new tie-in piping, electrical/instrument loop checks, punch-list management.
- Mechanical completion, system turnover, and handover-to-commissioning of the VRU subsystem.

### Out of scope (explicit exclusions)

- Package engineering, package design, vendor documentation, and the physical vendor-supplied equipment package itself (these are the Package Vendor's scope per `PACKAGE_REGISTER.csv` PKG-090).
- 03-25 local SOC, local condensate stabilization, local heat-medium, and local instrument-air compression — removed/superseded by SCA-002 / SCA-006 (DBM SEC-04, SEC-06, SEC-07). The CWP shall not reintroduce these systems.
- Cathodic Protection, Communications/Network, Grading / Site Drainage / Spill Containment, Product Loading, and Pipeline/Pigging interfaces — `26020-01-PT-12-002` lists these as "No". (Note: facility-level grading and spill containment continue under their own packages; they are simply not interfaces of this VRU CWP.)
- LACT equipment scope (NRM third-party); not a VRU CWP item.

## Requirements

R-CWP-090-001. Two (2) 100% capacity VRU compressor packages shall be installed in a lead-lag configuration, both housed in one building. (`26020-01-PT-12-002 / Basic Scope`)

R-CWP-090-002. Each train shall be installed and connected such that a single 200 HP VFD electric motor drives both stages of that train. (`26020-01-PT-12-002 / Major Included Equipment`)

R-CWP-090-003. All tie-in piping in sour service shall meet NACE materials/qualification requirements consistent with the 0.3557 mol% H2S, 0.9434 mol% CO2 service basis. (`26020-01-PT-12-002 / Major Included Equipment`)

R-CWP-090-004. The dual mechanical pressurized barrier (Plan 53 type) seal system shall be tied in to LP fuel-gas buffer supply with alarms and primary seal vent routed to LP flare. (`26020-01-PT-12-002 / Major Included Equipment`)

R-CWP-090-005. VRU second-stage discharge shall be tied in to the 04-25 SOC suction line; the CWP shall not provide a local 03-25 SOC tie-in. (DBM SEC-06; SCA-002 in DBM SEC-04)

R-CWP-090-006. The VRU suction header shall include the LP flare bypass V-ball valve operated by VRU suction pressure, and shall be installed to free-drain or slope toward the flare KO drum interface as defined by detailed design. (DBM SEC-06)

R-CWP-090-007. The VRU recycle line (second-stage discharge back to first-stage suction) shall be installed and verified for the sizing duty of 100% flow at minimum driver speed and lowest discharge pressure. (DBM SEC-06)

R-CWP-090-008. A low-pressure fuel-gas make-up / blanket regulator shall be installed on the VRU suction system to maintain minimum suction pressure at maximum turndown. (DBM SEC-06)

R-CWP-090-009. Construction shall implement all interfaces flagged `Yes` in the PT-12-002 Physical Interface Summary (Process Piping, Utility Piping, Relief/Flare/Vent, Drain/Containment, Electrical Power, Area/Exterior Lighting, EHT, Grounding/Bonding, I&C/Control Cabling, Fire & Gas/Safety Systems, Maintenance Access, Structural/Foundations/Supports) and shall not introduce interfaces flagged `No` (Cathodic Protection, Communications/Network, Building HVAC/Services per Package Requirements row, Grading/Site Drainage/Spill Containment, Product Loading, Pipeline/Pigging). HVAC discrepancy with `PACKAGE_REGISTER.csv` is logged in the Guidance Conflict Table; ruling required.

R-CWP-090-010. The CWP shall ensure execution of the "by others" items called out by the vendor scope (shipping to site, installation on piles, tie-in piping, electrical, instrumentation) as EPC Integrator scope. (`26020-01-PT-12-002` package scope notes)

R-CWP-090-011. The CWP shall produce a construction interface and turnover checklist mapping every PT-12-002 `Yes` interface to a verifiable acceptance step. (`_CONTEXT.md` Anticipated Artifacts)

R-CWP-090-012. The CWP shall produce an installation and tie-in workface plan that sequences foundation completion, building/skid set, tie-in piping, electrical/I&C connections, leak/loop testing, and ready-for-commissioning. (`_CONTEXT.md` Anticipated Artifacts)

R-CWP-090-013. Hydrotest, flushing, cleaning, and drying of new tie-in piping shall follow the package piping interface deliverables (PIP-024 Hydrotest Packages and PIP-025 Flushing/Cleaning/Drying Procedure). (`26020-01-PT-12-002` Vendor Engineering Deliverables — Process piping interfaces)

R-CWP-090-014. Electrical FAT/SAT, energization, and instrument loop checks shall be executed and recorded against vendor-issued ELE-029/ELE-030 and INS deliverables. (`26020-01-PT-12-002` Vendor Engineering Deliverables — Electrical / I&C sections)

R-CWP-090-015. Lifting and handling of major equipment shall be performed against vendor-issued MEC-018 Lifting/Handling Study. (`26020-01-PT-12-002` Vendor Engineering Deliverables — Core package engineering)

R-CWP-090-016. Structural installation (anchor bolts, embedments, module set) shall conform to vendor-issued STR-005, STR-006, and STR-013 packages. (`26020-01-PT-12-002` Vendor Engineering Deliverables — Structural section)

R-CWP-090-017. Pressure equipment registration and code compliance for installed pressure parts shall be supported by vendor-issued REG-022 Pressure Equipment Registration Package. (`26020-01-PT-12-002` Vendor Engineering Deliverables — Rotating equipment section)

R-CWP-090-018. ASSUMPTION — Provincial pressure equipment, electrical, and fire-code authorities having jurisdiction for north-east BC shall be addressed at the construction stage; specific code clauses are TBD pending the deliverable's regulatory reference being attached to `_REFERENCES.md`.

## Standards

| Standard / Code | Application | Location |
|---|---|---|
| NACE materials standards for sour service | Tie-in piping and components in VRU sour service | location TBD; cited by `26020-01-PT-12-002 / Major Included Equipment` |
| API piping seal Plan 53 type | Reference for dual mechanical pressurized barrier seal system | location TBD; cited by `26020-01-PT-12-002 / Major Included Equipment` |
| Provincial Pressure Equipment Safety (BC) | Pressure equipment registration | location TBD; referenced by vendor REG-022 |
| Canadian Electrical Code / provincial electrical safety | Power, lighting, EHT, grounding/bonding | location TBD |
| Applicable fire and gas / SIL standards | Fire & gas integration | location TBD; referenced by vendor TSF-009/TSF-011 |

Specific clause-level requirements are TBD because the standard texts are not in the local source set.

## Verification

| Requirement | Verification approach |
|---|---|
| R-CWP-090-001 / R-CWP-090-002 | Visual + dimensional check that two 100%-capacity trains are set in one building; motor nameplate confirms 200 HP VFD; vendor MEC-016/MEC-017 used as reference. |
| R-CWP-090-003 | Material test reports (QLT-013) reviewed for sour-service compliance; weld procedures and NDE per piping ITP. |
| R-CWP-090-004 | Seal vent line continuity test; LP flare tie-in confirmed open and free-draining; fuel-gas buffer pressure setpoint verified against vendor seal data. |
| R-CWP-090-005 | Walkdown verifying no local-SOC tie-in present at 03-25; routing to 04-25 SOC suction confirmed against P&IDs and tie-in list. |
| R-CWP-090-006 | LP flare bypass V-ball valve installed and stroke-tested; suction header slope checked against piping isometrics. |
| R-CWP-090-007 | Recycle line size and routing checked against vendor PRO-008 P&IDs; loop check during commissioning confirms recycle valve action. |
| R-CWP-090-008 | Make-up regulator installed and set; bench check at turndown condition during commissioning. |
| R-CWP-090-009 | Interface checklist with one row per PT-12-002 `Yes` interface; sign-off by EPC and vendor. |
| R-CWP-090-010 | Workface plan deliverables show foundation set, piping/electrical/I&C tie-in scope items closed. |
| R-CWP-090-011 / R-CWP-090-012 | The CWP and workface plan exist, are reviewed, and approved per EPC PMP. |
| R-CWP-090-013 | Hydrotest packages (PIP-024) signed off; flush/clean records on file. |
| R-CWP-090-014 | ELE-029 FAT/SAT records and ELE-030 test records on file; instrument loops closed per INS-008. |
| R-CWP-090-015 | Lift plan referenced; lifts executed per MEC-018. |
| R-CWP-090-016 | Foundation/anchor inspection reports vs STR-005/006/013. |
| R-CWP-090-017 | Pressure equipment registration package (REG-022) accepted by AHJ. |

## Documentation

The CWP shall produce, at minimum, the following deliverable artifacts (per `_CONTEXT.md`):

- Construction work package (this CWP — narrative + scope + interface register + sequence).
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.

It shall reference and consume the vendor engineering deliverables listed in `26020-01-PT-12-002 / Vendor Engineering Deliverables` (core vendor docs, core package engineering, rotating equipment, relief/flare/vent design, process piping, utility piping, drainage/containment, electrical/lighting/EHT/grounding, I&C, fire and gas, structural). These are inputs to construction; the CWP shall track receipt and acceptance of each.
