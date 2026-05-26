# Specification — DEL-072-03 Construction Work Package (Truck Product Loading Unit 4-25)

## Scope

This Construction Work Package (CWP) describes how the **Truck Product Loading Unit 4-25** (`PKG-072`, vendor package reference `26020-01-PT-23-001 — Condensate Truck Loading Stations`) will be physically received at site, installed, tied into the larger 04-25 Deep Cut Gas Plant, inspected, tested, and turned over to operations. The package services the 4-25/3-25 Deepcut truck loading interface. (Source: `_CONTEXT.md`; `26020-Package_Requirements.docx` Location/Status for section 23-001.)

**Includes (in scope of this CWP):**

- Receipt and off-loading of the truck loading station modules and bulk material at site. ASSUMPTION: site off-loading is in EPC Integrator scope (NOTE: at the 04-25 plant level, the DBM identifies "Off-loading of modules and equipment at site" as a Tourmaline field construction scope item — see `4-25_Deepcut_DBM.md` line 112; reconcile responsibility before mobilization).
- Foundations, structural supports, and anchorage for the loading station(s). (`26020-Package_Requirements.docx` Physical Interface Summary: Structural/Foundations/Supports = Yes.)
- Process piping tie-ins from upstream condensate storage / pumping systems to the truck-loading arms / metering skid. (Physical Interface Summary: Process Piping = Yes.)
- Drainage and spill containment civil works at the truck loading station. (Physical Interface Summary: Drain/Containment = Yes; Grading/Site Drainage/Spill Containment = Yes.)
- Electrical power supply, area/exterior lighting, grounding and bonding. (Physical Interface Summary: Electrical Power, Lighting, Grounding/Bonding = Yes.)
- Instrumentation & controls cabling, junction boxes, and tie-ins to DCS / Fire & Gas. (Physical Interface Summary: I&C Control Cabling = Yes, Fire & Gas/Safety Systems = Yes.)
- Inspection, pressure testing, flushing, energization, and pre-commissioning of installed scope.
- Turnover documentation to operations.

**Excludes (out of scope):**

- Vendor package supply, fabrication, and FAT (covered by vendor package contract — vendor engineering deliverables listed in `26020-Package_Requirements.docx`).
- LACT/metering ownership where LACT scope is TBD at the 04-25 level (`4-25_Deepcut_DBM.md` lines 62, 82, 171).
- Cathodic Protection, EHT, Building HVAC, Communications/Network, Maintenance Access, Utility Piping, Relief/Flare/Vent, Pipeline/Pigging (Physical Interface Summary: marked No for this package). NOTE: see Conflict Table re: section 23-001 source text containing FG-Skid prose.

## Requirements

Each requirement is grounded in an accessible source where cited; otherwise it is labeled `ASSUMPTION` or `TBD`.

| ID | Requirement | Source |
|---|---|---|
| REQ-072-03-01 | The CWP shall describe physical installation, build, inspection, turnover, and tie-in into larger facility systems for the package. | `DELIVERABLE_REGISTER.csv` (DEL-072-03 description) |
| REQ-072-03-02 | The CWP shall plan installation at the 4-25 Deep Cut Plant site (04-25 expansion) and coordinate the 4-25/3-25 Deepcut truck loading interface. | `26020-Package_Requirements.docx` Location/Status (section 23-001); `4-25_Deepcut_DBM.md` line 66 |
| REQ-072-03-03 | Minimum separation distance between pressurized bullets and the truck loading station shall be 15.24 m (50 ft) per API 2510. | `4-25_Deepcut_DBM.md` line 257 |
| REQ-072-03-04 | Minimum separation distance between bullet loading connections and ignition sources, process areas, storage tanks, or occupied structures shall be 15.24 m (50 ft) per API 2510. | `4-25_Deepcut_DBM.md` line 258 |
| REQ-072-03-05 | The CWP shall include foundations, structural supports, and anchor bolt installation per vendor STR-013 anchor bolt / embedment drawings and STR-006 foundation drawings. | `26020-Package_Requirements.docx` Vendor Engineering Deliverables (STR-006, STR-013) |
| REQ-072-03-06 | The CWP shall implement tie-in scope per PIP-004 Tie-In List / Tie-In Scope Sheets. | `26020-Package_Requirements.docx` Vendor Engineering Deliverables (PIP-004) |
| REQ-072-03-07 | The CWP shall execute pressure testing per PIP-024 Hydrotest / Pressure Test Packages and flushing per PIP-025 Flushing/Cleaning/Drying Procedure. | `26020-Package_Requirements.docx` Vendor Engineering Deliverables (PIP-024, PIP-025) |
| REQ-072-03-08 | Electrical installation shall follow ELE-027 Electrical Installation Details and ELE-028 Interconnection / Connection Diagrams, with test records per ELE-030. | `26020-Package_Requirements.docx` Vendor Engineering Deliverables |
| REQ-072-03-09 | Instrumentation installation shall follow INS-005 Instrument Location Plans, INS-006 Hook-Up Drawings, INS-009 Wiring/Termination Diagrams, INS-011 Cable Schedule. | `26020-Package_Requirements.docx` Vendor Engineering Deliverables |
| REQ-072-03-10 | Fire & Gas detection installation shall follow TSF-004 Fire and Gas Detector Layout Drawings and the SRS/F&G philosophy (TSF-011, TSF-002). | `26020-Package_Requirements.docx` Vendor Engineering Deliverables |
| REQ-072-03-11 | Grading and drainage tie-ins shall implement CIV-003 Grading Plan, CIV-004 Drainage/Stormwater Management Report, and applicable CIV-014 secondary containment drawings. | `26020-Package_Requirements.docx` Vendor Engineering Deliverables |
| REQ-072-03-12 | The CWP shall not be released for execution while LACT scope/ownership for related metering remains TBD if it materially affects truck-loading metering interfaces. ASSUMPTION: applicability of LACT TBD to this truck-loading station is to be confirmed. | `4-25_Deepcut_DBM.md` line 62 |
| REQ-072-03-13 | Permitting amendments for the truck rack shall be confirmed in place (or the package shall be staged accordingly) before site execution. | `4-25_Deepcut_DBM.md` line 133 |
| REQ-072-03-14 | The CWP shall produce a construction interface and turnover checklist covering all interface types marked "Yes" in the package interface summary. | `_CONTEXT.md` Anticipated Artifacts; `26020-Package_Requirements.docx` Physical Interface Summary |
| REQ-072-03-15 | The CWP shall produce an installation and tie-in workface plan. | `_CONTEXT.md` Anticipated Artifacts |
| REQ-072-03-16 | The CWP shall be coordinated with `SOW-0245`, `SOW-0246`, `SOW-0247`, `SOW-0248`. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |

## Standards

| Standard | Applicability | Source |
|---|---|---|
| API 2510 | Spacing for pressurized bullets and truck loading stations | `4-25_Deepcut_DBM.md` lines 257-258 |
| Vendor / EPC piping, electrical, instrumentation, structural, civil standards as listed in the vendor deliverable index | Construction execution | `26020-Package_Requirements.docx` Vendor Engineering Deliverables section |
| Site-specific regulatory permits (BC Energy Regulator Determination 100120203 + truck-rack amendment) | Permitting basis | `4-25_Deepcut_DBM.md` line 133 |
| Additional codes (CSA, NFPA, ASME, NEMA, etc.) — `location TBD` | Construction execution | `location TBD` |

## Verification

| Requirement(s) | Verification Approach | Evidence |
|---|---|---|
| REQ-072-03-03, REQ-072-03-04 | Survey / as-built measurement | Site survey records (CIV-019, STR-002 GAs) |
| REQ-072-03-05 | Foundation inspection; anchor-bolt installation records; concrete compressive strength reports | QLT-013 Material Test Reports |
| REQ-072-03-06 | Tie-in walkdown using PIP-004 | Punch list / signed walkdown sheets |
| REQ-072-03-07 | Hydrotest reports; flushing/cleaning sign-off | PIP-024 packages; PIP-025 records |
| REQ-072-03-08 | Electrical inspection, megger test records, energization checklist | ELE-029, ELE-030 |
| REQ-072-03-09 | Instrument loop checks; calibration certificates | INS-008 loop diagrams + loop check sheets |
| REQ-072-03-10 | F&G mapping verification at installed-state | TSF-003, TSF-004 |
| REQ-072-03-11 | Civil walkdown; drainage flow check | CIV-019 MTO + as-built |
| REQ-072-03-14, REQ-072-03-15 | Document deliverable review and acceptance | Construction Interface & Turnover Checklist; Workface Plan |

## Documentation

Mandatory artifacts produced by this CWP (per `_CONTEXT.md` Anticipated Artifacts):

- Construction Work Package document (this deliverable set)
- Installation and tie-in workface plan
- Construction interface and turnover checklist

Cross-referenced vendor engineering deliverables consumed by this CWP (subset, per `26020-Package_Requirements.docx`):

- Mechanical: MEC-016 Equipment GA, MEC-017 Installation/Setting Drawings, MEC-018 Lifting/Handling Study, MEC-025 IOM
- Piping: PIP-003, PIP-004, PIP-006-PIP-009, PIP-017, PIP-024, PIP-025, PIP-028
- Civil: CIV-003, CIV-004, CIV-014, CIV-015, CIV-019
- Structural: STR-001, STR-002, STR-004-STR-006, STR-011-STR-014, STR-020
- Electrical: ELE-002, ELE-003, ELE-012, ELE-014-ELE-017, ELE-019, ELE-020, ELE-027-ELE-030
- Instrumentation / Control: INS-002, INS-003, INS-005, INS-006, INS-008-INS-011, INS-015-INS-018, INS-025, INS-029, CTL-003, CTL-005, CTL-006, CTL-026
- Technical Safety / F&G: TSF-002-TSF-004, TSF-009, TSF-011, TSF-013, TSF-028
- Quality: QLT-003, QLT-006, QLT-013, QLT-020, QLT-021
- Procurement/Logistics: PRQ-009, PRQ-013, PRQ-015, PRQ-016
