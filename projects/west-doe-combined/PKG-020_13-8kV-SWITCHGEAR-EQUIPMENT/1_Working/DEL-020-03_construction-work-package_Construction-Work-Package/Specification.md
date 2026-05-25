# Specification: Construction Work Package

## Scope

This specification governs the deliverable-local Construction Work Package for `PKG-020` 13.8kV SWITCHGEAR EQUIPMENT. The package is an Electrical WBS 01 scope item (CoA tracking number `26020-01-30-011`) and is an EPC Integrator deliverable for physical installation, construction, inspection, turnover, and tie-in of the vendor-supplied 13.8 kV switchgear into the larger 04-25 facility systems as the plant main power distribution center.

The Construction Work Package shall cover:

- construction work package content;
- installation and tie-in workface planning for the 13.8 kV switchgear and its electrical building;
- construction interface and turnover checklist content;
- Electrical Power interface controls (source-side feed from the BC Hydro 25/13.8 kV, 50 MVA utility-supplied transformer; load-side radial distribution to downstream step-down transformers and electrical buildings);
- Grounding / Bonding interface controls (utility-transformer 200 A, 10 s neutral grounding resistor; plant ground grid with #2/0 main conductor; two-point ground connection at major equipment);
- I&C / Control Cabling interface controls (UPS-served 120 VAC / 125 VDC MV breaker control and MV protective relay wiring);
- Communications / Network interface controls (switchgear-to-plant-control connectivity);
- Maintenance Access interface controls (operating clearances, arc-flash boundaries, breaker/lineup withdrawal and replacement-component access);
- Structural / Foundations / Supports interface controls (switchgear lineups and Electrical Building 810-1 foundations and supports).

Exclusions:

- Detailed switchgear ratings (bus continuous, short-circuit interrupting/withstand, BIL, breaker type, arc-resistant rating, accessories), lineup count, foundation/seismic detailing, and utility interface metering/protection details are `TBD` unless confirmed by vendor data, accepted project electrical specifications, IFC electrical drawings, or detailed electrical studies.
- Package engineering, package design, vendor documentation, and physical equipment supply are Package Vendor scope per `PKG-020` responsibility model and are not redefined here.
- The previously-contemplated centralized 13.8 kV emergency generator is not in the current basis; standby power is at the 600 V MCC level via TOU LV standby generators with transfer switches.

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-020-03_construction-work-package`; `PACKAGE_REGISTER.csv` row `PKG-020`; `INTERFACE_REGISTER.csv` rows for `PKG-020`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System, Grounding and Bonding, Electrical Buildings, and Cable Specifications sections.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| CWP-REQ-001 | The Construction Work Package shall identify `PKG-020` 13.8kV SWITCHGEAR EQUIPMENT, workbook row 22, WBS 01, CoA tracking number `26020-01-30-011`, Electrical discipline, and responsible party EPC Integrator. | Confirm against `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`. |
| CWP-REQ-002 | The package shall include a construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. | Confirm required artifacts (`ART-9A5E2DBA11`, `ART-7343A1CFCD`, `ART-14E7FF268C`) are present in the package index and turnover records. |
| CWP-REQ-003 | The workface plan shall address the source-recorded interfaces: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | Check interface checklist against `INTERFACE_REGISTER.csv` rows `IFC-611474D99C`, `IFC-F3098CE7CD`, `IFC-8BF7209227`, `IFC-340091634A`, `IFC-2FB786FC10`, `IFC-08E563D004`. |
| CWP-REQ-004 | The Electrical Power interface shall reflect the source basis: the BC Hydro 25 kV (TBC) supply feeds a 25/13.8 kV, 50 MVA utility-supplied transformer that steps down to the local 13.8 kV switchgear; the 13.8 kV bus is sized for the full facility scope and distributes radially through step-down transformers to the 6.9 kV, 4.16 kV, and 600 V electrical buildings. | Confirm against `4-25_Deepcut_DBM.md` Power System section (lines 2917-2926). |
| CWP-REQ-005 | The Grounding / Bonding interface shall reflect the source basis: utility-transformer 200 A, 10 s neutral grounding resistor (tripping system); plant ground grid using driven piles and a #2/0 main conductor; major equipment grounded to the grid at two points. | Confirm against `4-25_Deepcut_DBM.md` Grounding and Bonding section (lines 2985, 2987, 2989). |
| CWP-REQ-006 | The I&C / Control Cabling interface shall preserve UPS-served (120 VAC / 125 VDC) MV breaker control and MV protective relay wiring; control wiring shall be routed and labeled per IFC drawings and project electrical specifications. | Confirm against `4-25_Deepcut_DBM.md` UPS services row (line 2939). |
| CWP-REQ-007 | The Communications / Network interface shall provide connectivity between the 13.8 kV switchgear and the plant control system (PLC/SCADA). Specific protocol and architecture shall match the accepted project controls/communications design. | `location TBD` - confirm against project controls/communications specification when available. |
| CWP-REQ-008 | The MV cable basis for 13.8 kV circuits shall be three-conductor copper TECK cable rated 15 kV with 133 percent insulation, shielded. | Confirm against `4-25_Deepcut_DBM.md` Cable Specifications (line 3007). |
| CWP-REQ-009 | Foundation, structural support, seismic detailing, and frost/cold-weather provisions for the switchgear lineups and Electrical Building 810-1 shall not be closed until the final geotechnical report and vendor equipment loads are accepted. | Confirm readiness gate cites accepted geotechnical inputs and the vendor engineered equipment package (`DEL-020-04`). |
| CWP-REQ-010 | Cold-weather installation, handling, and commissioning controls shall reflect the -40 deg C minimum ambient governing exposed equipment, control panels, instrumentation, and field devices. | Confirm against project ambient basis; mark `location TBD` if no explicit slice in this deliverable's source set. |
| CWP-REQ-011 | Tie-in scope for the utility supply (metering, protection, isolation, telemetry) and any 03-25 / 02-25 / existing-facility interfaces shall be jointly planned with the affected parties; tie-in timing shall be established as the project progresses. | Confirm against `4-25_Deepcut_DBM.md` line 127 and the project tie-in register. |
| CWP-REQ-012 | A verification hold shall be carried for protection coordination, arc-flash, and standby-power scope split until detailed electrical studies and the standby-power scope decision are accepted. | Confirm against `4-25_Deepcut_DBM.md` Power System section (line 2927) and the detailed-electrical-studies hold register. |
| CWP-REQ-013 | ASSUMPTION: Before issue for construction, the Construction Work Package shall be aligned with the accepted EPC Scope of Work (`DEL-020-01`), Package Datasheet (`DEL-020-02`), vendor engineered equipment package (`DEL-020-04`), IFC electrical drawings, plot plan, equipment list, and protection/coordination study outputs. | Confirm against the listed upstream deliverables when available. |
| CWP-REQ-014 | The package shall preserve Maintenance Access provisions for the 13.8 kV switchgear (operating clearances, arc-flash boundaries, breaker/lineup withdrawal, lifting access, replacement-component access). | Confirm against vendor equipment package and IFC layout; mark `TBD` where source values are unavailable. |
| CWP-REQ-015 | Standards and code references unavailable in the workspace shall be treated as verification requirements, not closed requirements. | Confirm the standards register marks unavailable sources as `location TBD` or verification-required. |
| CWP-REQ-016 | The Construction Work Package shall not carry scope for a centralized 13.8 kV emergency generator; standby power is at the 600 V MCC level via LV standby generators with transfer switches. | Confirm against `4-25_Deepcut_DBM.md` lines 2080, 2943. |

## Standards

| Standard / authority | Status |
|---|---|
| Project electrical specifications, protection/coordination studies, arc-flash study | `location TBD`; required for closure of switchgear ratings, protection settings, arc-flash boundaries, and acceptance criteria. |
| Project grounding specification | `location TBD`; required for closure of grounding/bonding installation and test acceptance. |
| Project controls/communications specification | `location TBD`; required for closure of CWP-REQ-007. |
| Utility (BC Hydro) interface agreement / utility coordination | `location TBD`; required for closure of utility-side scope split (CWP-REQ-011). |
| Final geotechnical report | Required before foundation design closure; not accessible in current deliverable source set. |
| Project specifications and standards register | `location TBD`; unavailable citations must be verified before final issue for construction. |
| Canadian Electrical Code (CEC) | Referenced as the governing electrical code for sizing, spacing, and grounding (`4-25_Deepcut_DBM.md` Grounding and Bonding section, Transformers section). |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Package identity | Document review | Matches `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`. |
| Interface coverage | Checklist review | Includes all six declared interface types for `PKG-020`. |
| Utility-side Electrical Power tie-in | Engineering review and field inspection hold point | Source-side feed from the 25/13.8 kV, 50 MVA utility-supplied transformer matches accepted electrical drawings; phasing, cable, termination, metering, and protection witnessed. |
| Load-side Electrical Power tie-in | Engineering review and field inspection hold point | Radial feeders to downstream step-down transformers and electrical buildings match accepted single-line and electrical drawings. |
| Grounding / Bonding | Field inspection, continuity/impedance tests, and ground-resistance test record | Utility-transformer 200 A neutral grounding resistor installed and verified; plant ground grid #2/0 main installed; two-point ground connections at the switchgear lineup verified. |
| MV cable installation | Cable test records (insulation, hi-pot, VLF as applicable), termination inspection | 13.8 kV cables match the 15 kV / 133% insulation / shielded TECK basis; routing per IFC drawings. |
| I&C / Control Cabling | Loop check and signal verification | MV breaker control and protective relay loops are UPS-served (120 VAC / 125 VDC) and verified per drawings. |
| Communications / Network | Network commissioning record | Switchgear-to-plant-control connectivity verified per the project controls/communications design. |
| Foundations / structural supports | Civil/structural inspection and turnover | Switchgear lineup and Electrical Building 810-1 foundation, anchorage, and structural support installation matches accepted civil/structural drawings; final geotechnical inputs accepted or exceptioned. |
| Maintenance Access | Layout review and walk-down | Clearances, arc-flash boundaries, breaker withdrawal envelope, and replacement-component access verified per accepted layout. |
| Cold-weather readiness | Commissioning review | Installation, heating, lubricant, and operational provisions match -40 deg C minimum ambient basis. |
| Protection / coordination / arc-flash hold | Design readiness review | Detailed electrical studies accepted, or exceptioned as `TBD`. |
| Standby-power scope split hold | Design readiness review | Standby-power scope split and protection coordination accepted, or exceptioned as `TBD`. |
| Utility coordination | Utility agreement review and joint tie-in plan | BC Hydro utility coordination, metering point, and protection split accepted. |
| Standards verification | Standards register check | Unavailable standards are not represented as closed. |
| Construction turnover | Turnover package review | Construction records, inspections, exceptions, and interface signoffs complete. |

## Documentation

The deliverable shall include or reference:

- construction work package;
- installation and tie-in workface plan;
- construction interface and turnover checklist;
- interface checklist for Electrical Power (utility-side and load-side);
- interface checklist for Grounding / Bonding;
- interface checklist for I&C / Control Cabling;
- interface checklist for Communications / Network;
- interface checklist for Maintenance Access;
- interface checklist for Structural / Foundations / Supports;
- MV cable test records and termination inspection records;
- construction inspection and turnover records;
- unresolved criteria register for switchgear ratings, foundation/geotechnical inputs, utility coordination, protection/coordination/arc-flash, standby-power scope split, project electrical specifications, and regulatory items.
