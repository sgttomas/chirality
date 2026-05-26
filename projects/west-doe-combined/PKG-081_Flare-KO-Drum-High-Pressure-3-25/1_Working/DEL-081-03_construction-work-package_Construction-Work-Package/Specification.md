# Specification: Construction Work Package

## Scope

This specification governs the deliverable-local Construction Work Package for `PKG-081` Flare KO Drum (High Pressure) 3-25. The package is a Mechanical WBS 02 scope item (CoA tracking number `26020-02-17-001`) and is an EPC Integrator deliverable for physical installation, construction, inspection, turnover, and tie-in of the vendor-supplied two HP flare KO drums (V-4100-2 and V-4150-2) and their two dedicated transfer pumps (P-4100-2 and P-4150-2) into the 03-25 facility.

The Construction Work Package shall cover:

- construction work package content;
- installation and tie-in workface planning for the HP KO drums and transfer pumps;
- construction interface and turnover checklist content;
- Process Piping interface controls (HP relief inlet headers, pump-out / liquid-transfer piping);
- Relief / Flare / Vent interface controls (manifolding of HP headers to the shared HP/Cryo flare stack);
- Drain / Containment interface controls (drum drains, pump-out routing to slop or truck-out);
- Electrical Power interface controls (pump motor supply, instrumentation power);
- EHT (electric heat tracing) interface controls (cold-weather provisions);
- Grounding / Bonding interface controls;
- Area / Exterior Lighting interface controls (drum/pump area lighting);
- I&C / Control Cabling interface controls (level, pressure, and pump control signals to the plant control system);
- Maintenance Access interface controls (drum manway access, pump replacement, lifting);
- Structural / Foundations / Supports interface controls.

Exclusions:

- Detailed KO drum mechanical data (dimensions, MAWP, MDMT, nozzle schedule, internals, materials, weights, lifting lugs) and transfer-pump data (type, capacity, head, NPSH, driver, sealing, materials) are `TBD` unless confirmed by vendor data, accepted project mechanical/piping specifications, or IFC drawings.
- Final flare relief and blowdown loads, the staggered blowdown sequence, and the HP/Cryo flare stack shared-service split are `TBD` pending the external Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001 and applicable shared-system rulings.
- Package engineering, package design, vendor documentation, and physical equipment supply are Package Vendor scope per `PKG-081` responsibility model and are not redefined here.

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-081-03_construction-work-package`; `PACKAGE_REGISTER.csv` row `PKG-081`; `INTERFACE_REGISTER.csv` rows for `PKG-081`.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| CWP-REQ-001 | The Construction Work Package shall identify `PKG-081` Flare KO Drum (High Pressure) 3-25, workbook row 54, WBS 02, CoA tracking number `26020-02-17-001`, Mechanical discipline, and responsible party EPC Integrator. | Confirm against `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`. |
| CWP-REQ-002 | The package shall include a construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. | Confirm required artifacts are present in the package index and turnover records. |
| CWP-REQ-003 | The workface plan shall address all ten source-recorded interfaces: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports. | Check interface checklist against `INTERFACE_REGISTER.csv` rows `IFC-E6E19CC83E`, `IFC-1F7E9C14E8`, `IFC-2D16BB76D1`, `IFC-81D2B385AE`, `IFC-ABC65133B6`, `IFC-D38D4A85D8`, `IFC-A715F77DE6`, `IFC-4204F7F04E`, `IFC-E06624196C`, `IFC-0B6C1286C7`. |
| CWP-REQ-004 | The Relief / Flare / Vent interface shall reflect the source basis: HP headers from V-4100-2 (compressor area) and V-4150-2 (tank farm) manifold to the shared HP/Cryo flare stack (660 mm OD x 60,957 mm tall); HP and LP relief headers are 508 mm (20 inch) in the current basis. | Confirm against `3-25_Comp_and_Liquids_DBM.md` Flare and Blowdown section (lines 497-499). |
| CWP-REQ-005 | The Drain / Containment interface shall reflect that KO drum pumps P-4100-2 and P-4150-2 truck-out or transfer collected liquids to slop. | Confirm against `3-25_Comp_and_Liquids_DBM.md` Flare and Blowdown (line 497). |
| CWP-REQ-006 | The Construction Work Package shall carry a verification hold for final flare relief and blowdown loads and for the staggered blowdown sequence, pending acceptance of the external Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001. | Confirm hold register cites DBM Flare and Blowdown (line 501) and the external philosophy document. |
| CWP-REQ-007 | The Construction Work Package shall carry an open-interface item for the HP/Cryo flare stack and incinerator shared-service split between 03-25 and 04-25, pending source ruling. | Confirm exception register cites DBM Commercial and Facility Interfaces (line 56). |
| CWP-REQ-008 | EHT and cold-weather installation, handling, and commissioning provisions shall reflect the -40 deg C minimum ambient governing exposed drums, package piping, control panels, instrumentation, and field devices. | Confirm against DBM SEC-02 Design Implications and `INTERFACE_REGISTER.csv` row `IFC-ABC65133B6`. |
| CWP-REQ-009 | Foundation, structural support, seismic detailing, frost protection, and settlement criteria for the two HP KO drums and the two transfer pumps shall not be closed until the final geotechnical report and vendor equipment load data are accepted. | Confirm readiness gate cites DBM SEC-02 Geotechnical and Seismic Basis (line 141) and the vendor engineered equipment package. |
| CWP-REQ-010 | Standards and code references unavailable in the workspace shall be treated as verification requirements, not closed requirements. | Confirm standards register marks unavailable source locations as `location TBD` or verification-required (DBM SEC-15). |
| CWP-REQ-011 | ASSUMPTION: Before issue for construction, the Construction Work Package shall be aligned with the accepted EPC Package Datasheet (`DEL-081-02`), the vendor engineered equipment package (`DEL-081-04`), IFC piping/mechanical drawings, plot plan, equipment list, and flare-system relief/blowdown studies. | Confirm against `DEL-081-02_package-datasheet`, `DEL-081-04_vendor-engineered-equipment-package`, and project IFC deliverables when available. |
| CWP-REQ-012 | The package shall preserve Maintenance Access provisions for both HP KO drums and both transfer pumps (operating clearances, manway access, lifting/handling for internals, pump replacement, and truck-out access for collected liquids). | Confirm against vendor equipment package and IFC layout; mark `TBD` where source values are unavailable. |
| CWP-REQ-013 | Pressure-testing, NDE, and PWHT requirements for HP-rated piping and equipment tie-ins shall be defined by accepted project piping/mechanical specifications; values absent from the local source set remain `TBD`. | Confirm against project mechanical/piping specifications and IFC drawings when available. |

## Standards

| Standard / authority | Status |
|---|---|
| External Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001 | Required detailed source for final blowdown sequencing (DBM line 501); not accessible in the current deliverable source set - `location TBD`. |
| Final geotechnical report | Required before foundation design closure; not accessible in current deliverable source set. |
| Project piping / mechanical specifications, flare-system relief and blowdown studies | `location TBD`; required for closure of pressure-test, NDE, PWHT, header sizing confirmation, and relief loads. |
| Project specifications and standards register (DBM SEC-15) | `location TBD`; DBM SEC-15 states unavailable citations must be verified before final issue. |
| 26020-Package_Requirements.docx package heading 34 | Referenced by `PACKAGE_REGISTER.csv` and `_CONTEXT.md` as the Word source for `PKG-081`; not accessible in markdown form in this run - `location TBD`. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Package identity | Document review | Matches `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`. |
| Interface coverage | Checklist review | Includes all ten declared interface types for `PKG-081`. |
| Process Piping tie-in | Engineering review and field inspection hold point | Inlet HP relief connections and pump-out/transfer piping match accepted piping drawings; pressure test and NDE records witnessed. |
| Relief / Flare / Vent tie-in | Engineering review and field inspection hold point | Manifolding to HP/Cryo flare stack matches accepted flare-system drawings; 508 mm header alignment, slope, drainage to KO drum, and isolation provisions verified. |
| Drain / Containment | Field inspection | Drain routing and pump-out/slop transfer routing match accepted drawings; containment provisions verified. |
| Electrical Power | Field inspection and tie-in test | Pump motor and instrumentation power supply per accepted electrical drawings; phasing, cable, termination, and grounding witnessed. |
| EHT | Inspection and energization test | Heat tracing, insulation, and cold-weather provisions match -40 deg C basis. |
| Grounding / Bonding | Field inspection and continuity/impedance test | Grounding/bonding installation matches accepted drawings and project grounding specification. |
| Area / Exterior Lighting | Field inspection | Drum/pump area lighting matches accepted lighting drawings and access/safety needs. |
| I&C / Control Cabling | Loop check and signal verification | Level, pressure, and pump control wiring to plant control system matches drawings. |
| Maintenance Access | Layout review and walk-down | Drum/pump access, manway, lifting/replacement clearances verified per accepted layout. |
| Structural / Foundations / Supports | Civil/structural inspection and turnover | Foundation, anchorage, and structural support installation matches accepted drawings; final geotechnical inputs accepted or exceptioned. |
| Blowdown / relief readiness | Design readiness review | Final flare relief/blowdown loads and staggered-blowdown sequence accepted or exceptioned as `TBD`. |
| Shared-system interface | Design readiness review | HP/Cryo flare stack and incinerator service split with 04-25 resolved or carried as open interface. |
| Construction turnover | Turnover package review | Construction records, inspections, exceptions, and interface signoffs complete. |
| Standards verification | Standards register check | Unavailable standards and external philosophy documents are not represented as closed. |

## Documentation

The deliverable shall include or reference:

- construction work package;
- installation and tie-in workface plan;
- construction interface and turnover checklist;
- interface checklist for Process Piping;
- interface checklist for Relief / Flare / Vent;
- interface checklist for Drain / Containment;
- interface checklist for Electrical Power;
- interface checklist for EHT;
- interface checklist for Grounding / Bonding;
- interface checklist for Area / Exterior Lighting;
- interface checklist for I&C / Control Cabling;
- interface checklist for Maintenance Access;
- interface checklist for Structural / Foundations / Supports;
- construction inspection and turnover records (including pressure-test and NDE records);
- unresolved criteria register for KO drum and pump detailed data, flare relief/blowdown loads, shared-system split, geotechnical, IFC drawing, mechanical/piping specification, and regulatory items.
