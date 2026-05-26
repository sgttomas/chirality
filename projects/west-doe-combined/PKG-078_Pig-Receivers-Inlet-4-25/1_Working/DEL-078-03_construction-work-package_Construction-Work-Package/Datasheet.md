# Datasheet: Construction Work Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | `DEL-078-03_construction-work-package` |
| Deliverable name | Construction Work Package |
| Parent package | `PKG-078` - Pig Receivers (Inlet) 4-25 |
| Workbook row | 78 |
| WBS | 01 |
| CoA tracking number | `26020-01-35-001` |
| Discipline | Mechanical |
| Responsible party | EPC Integrator |
| Deliverable type | EPC Construction Work Package |
| Scope items | `SOW-0161`; `SOW-0162`; `SOW-0163`; `SOW-0164` |

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-078-03_construction-work-package`; `PACKAGE_REGISTER.csv` row `PKG-078`; `SCOPE_LEDGER.csv` rows `SOW-0161`-`SOW-0164`.

## Attributes

| Attribute | Current basis | Source |
|---|---|---|
| Package name | Pig Receivers (Inlet) 4-25 | `PACKAGE_REGISTER.csv` row `PKG-078` |
| Package responsibility model | Package Vendor owns package engineering, design, vendor documentation, and physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility integration. | `PACKAGE_REGISTER.csv` row `PKG-078` |
| Package scope basis | Supply 3 identical 610 mm (24 in.) OD pig receivers with HIPPS package on dedicated structural-steel non-enclosed skids; plant inlet pipeline gas enters the 04-25 facility through these receivers and flows to the inlet separators. | `SCOPE_LEDGER.csv` `SOW-0162`; `PACKAGE_REGISTER.csv` row `PKG-078` |
| Equipment identity (tag list) | PR-1010-1; PR-1020-1; PR-1030-1 (3 pig receiver assemblies on dedicated skids) | `4-25_Deepcut_DBM.md` Package Line-Item Requirements row 61; `SCOPE_LEDGER.csv` `SOW-0163` |
| Applicable interface types | Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; I&C / Control Cabling; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports; Pipeline / Pigging | `INTERFACE_REGISTER.csv` rows `IFC-49A2026DAA`, `IFC-11316BD975`, `IFC-17309B535C`, `IFC-F2CC0221E0`, `IFC-9313950850`, `IFC-99C4B8C9E0`, `IFC-A553991A6E`, `IFC-3894C2DC14`, `IFC-6798D96AAF`, `IFC-65EDB92369`; `PACKAGE_REGISTER.csv` row `PKG-078` |
| Construction work package artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | `DELIVERABLE_REGISTER.csv` row `DEL-078-03_construction-work-package` |
| Vendor scope explicitly excluded from CWP scope (by others / EPC) | Interconnecting piping; DCS integration; foundations; electrical supply to MCC | `SCOPE_LEDGER.csv` `SOW-0164` |
| Declared upstream dependencies | None declared during PREPARATION | `_DEPENDENCIES.md` |
| Declared downstream dependencies | None declared during PREPARATION | `_DEPENDENCIES.md` |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Facility context | 04-25 West Doe Deepcut expansion; plant inlet pipeline gas enters via the inlet pig receiver(s) on dedicated non-enclosed structural-steel skid(s); barred tees prevent pigs from entering facility piping; pig receiver vents to HP flare; sweet-gas purge provided downstream of manual isolation for purge before opening. | `4-25_Deepcut_DBM.md` lines 583-585 |
| Ambient design conditions | Historical ambient -19 deg C min / +22.2 deg C max; ambient design -40 deg C min / +35 deg C max | `SCOPE_LEDGER.csv` `SOW-0164` |
| Normal operating pressure (inlet gathering) | 653 psig to 725 psig; MAOP = 1300 psig | `SCOPE_LEDGER.csv` `SOW-0164`; `4-25_Deepcut_DBM.md` Inlet Pipeline Pressure table (line 626) |
| Design pressure (pig receiver / inlet skid) | Low 653 psig; normal high 725 psig; MAWP 1440 psig (TBC at plant gate per DBM) | `SCOPE_LEDGER.csv` `SOW-0164`; `4-25_Deepcut_DBM.md` line 626 |
| Service / sour basis | Sour service; design H2S 1.0 mol% | `SCOPE_LEDGER.csv` `SOW-0163`; `4-25_Deepcut_DBM.md` Inlet Contaminant table (line 419) |
| Design throughput | 225 MMSCFD; normal flow per receiver TBC | `SCOPE_LEDGER.csv` `SOW-0164` |
| Pig-trap full-port isolation | Skid-mounted isolation valves or ESDVs upstream of the pig receiver shall be full-port for pigging | `4-25_Deepcut_DBM.md` line 585; `SCOPE_LEDGER.csv` `SOW-0163` |
| HIPPS / over-pressure protection | Each receiver skid includes a HIPPS package with ESDVs upstream of the receiver; pressure control valve with outlet PT under PID to keep inlet separator pressure within limits; shutdown valve with pneumatic hi-low shutoff plus redundant shutdown valve with pneumatic hi-low to close high-pressure inlet | `SCOPE_LEDGER.csv` `SOW-0163` |
| Inlet ESDV / HIPPS interaction | The facility inlet includes a full-port piggable ESDV with position transmitters on the pig receiver inlet skid; if inlet pipeline MAOP exceeds facility inlet design pressure a HIPPS may be required to protect inlet separators; HIPPS configuration and setpoints TBC during detailed engineering | `4-25_Deepcut_DBM.md` line 809 |
| Vent / drain disposition | Pig receiver vents to HP flare system; barrel purge by low-pressure sweet fuel gas downstream of manual isolation before opening | `4-25_Deepcut_DBM.md` line 585; `SCOPE_LEDGER.csv` `SOW-0163` |

## Construction

| Construction data item | Value |
|---|---|
| Work package boundary | Physical installation, construction, inspection, turnover, and tie-in of the three pig receiver skids (PR-1010-1, PR-1020-1, PR-1030-1) at the 04-25 facility plant inlet, including HIPPS skid integration; tie-in to the plant inlet pipeline (upstream), to facility process piping toward the inlet separators (downstream), to HP flare vent, to LP sweet fuel-gas purge supply, to electrical power, to EHT, to I&C / control cabling, to grounding/bonding, and to drain/containment; structural foundations/supports and grading/site drainage interfaces are within EPC Integrator scope (vendor by others per SOW-0164). |
| Workface plan minimum contents | Installation sequence for three receiver skids; work-area limits and lay-down; offload and setting of each skid; foundation acceptance pre-set; tie-in/interface checkpoints for Process Piping, Relief/Flare/Vent, Drain/Containment, Electrical Power, EHT, I&C / Control Cabling, Maintenance Access, Grading/Site Drainage/Spill Containment, Structural/Foundations/Supports, and Pipeline/Pigging; barred-tee verification; full-port pig-handling isolation verification; sweet-gas purge connection verification; HP flare vent connection verification; inspection/hold points; turnover records; unresolved `TBD` criteria. |
| Interface checklist minimum contents | Process Piping tie-in checks (full-port pig-handling, barred tees); Relief/Flare/Vent tie-in checks (HP flare vent line, set pressures TBD); Drain/Containment tie-in checks; Electrical Power tie-in checks (supply to MCC by EPC per SOW-0164); EHT (electric heat trace) coverage and termination checks; I&C / Control Cabling and DCS integration checks (DCS integration by others per SOW-0164); Maintenance Access checks (pig handling/closure access, lifting); Grading / Site Drainage / Spill Containment checks; Structural / Foundations / Supports checks; Pipeline / Pigging checks (incoming pipeline, pig trap closure, barrel purge). |
| Detailed receiver geometry (barrel length, closure type, kicker line, signaller / detector arrangement) | TBD - not defined in accessible source slices; defined by Package Vendor engineering per `DEL-078-04_vendor-engineered-equipment-package`. |
| Foundation and structural support detailing for the receiver skids | TBD - depends on final geotechnical report and vendor equipment loads (skids supplied non-enclosed on dedicated structural steel per SOW-0163). |
| HIPPS test, certification, and proof-test acceptance procedure | TBD - to be defined from vendor HIPPS documentation and project SIL/HAZOP outputs; not stated in accessible sources. |
| Inspection and acceptance criteria (welding, NDE, pressure test, sour-service hardness, coating) | TBD - to be confirmed from IFC mechanical drawings, project piping specifications (sour service), vendor commissioning procedures, and inspection-test plans. |

## References

- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- `_REFERENCES.md`
- `DELIVERABLE_REGISTER.csv` row `DEL-078-03_construction-work-package`
- `PACKAGE_REGISTER.csv` row `PKG-078`
- `SCOPE_LEDGER.csv` rows `SOW-0161`, `SOW-0162`, `SOW-0163`, `SOW-0164`
- `INTERFACE_REGISTER.csv` rows for `PKG-078` (ten Mechanical interfaces)
- `OBJECTIVE_DELIVERABLE_MAP.csv` (objective association `PACKAGE_HEURISTIC`)
- `4-25_Deepcut_DBM.md` (Inlet Pipeline and Facility Inlet, Inlet Pipeline Pressure tables, Plant ESDV/HIPPS, Package Line-Item Requirements row 61)
