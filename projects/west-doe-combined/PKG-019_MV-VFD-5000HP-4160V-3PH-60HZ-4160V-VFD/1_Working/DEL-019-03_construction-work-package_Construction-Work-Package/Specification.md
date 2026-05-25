# Specification: Construction Work Package

## Scope

This specification governs the deliverable-local Construction Work Package for `PKG-019` MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD. The package is an Electrical WBS 02 scope item and is an EPC Integrator deliverable for physical installation, construction, inspection, turnover, and tie-in of the vendor-supplied MV VFD into the larger facility systems.

The Construction Work Package shall cover:

- construction work package content;
- installation and tie-in workface planning for the MV VFD package;
- construction interface and turnover checklist content;
- Electrical Power interface controls (MV feed from the 4160V MCC and output to the driven 4000V motor);
- Grounding / Bonding interface controls;
- I&C / Control Cabling interface controls;
- Communications / Network interface controls (EtherNet to plant PLC central control panel);
- Maintenance Access interface controls;
- Structural / Foundations / Supports interface controls.

Exclusions:

- Detailed VFD ratings (kVA, topology, cooling, enclosure type, harmonic filter, output filter, bypass, input transformer), foundation/seismic detailing, and harmonic/reactive-power mitigation values are `TBD` unless confirmed by vendor data, accepted project electrical specifications, IFC electrical drawings, or detailed electrical studies.
- Package engineering, package design, vendor documentation, and physical equipment supply are Package Vendor scope per `PKG-019` responsibility model and are not redefined here.

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-019-03_construction-work-package`; `PACKAGE_REGISTER.csv` row `PKG-019`; `INTERFACE_REGISTER.csv` rows for `PKG-019`.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| CWP-REQ-001 | The Construction Work Package shall identify `PKG-019` MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD, workbook row 21, WBS 02, CoA tracking number `26020-02-30-009`, Electrical discipline, and responsible party EPC Integrator. | Confirm against `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`. |
| CWP-REQ-002 | The package shall include a construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. | Confirm required artifacts are present in the package index and turnover records. |
| CWP-REQ-003 | The workface plan shall address the source-recorded interfaces: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | Check interface checklist against `INTERFACE_REGISTER.csv` rows `IFC-63D8BC58F2`, `IFC-6119784E41`, `IFC-4C2D177FE7`, `IFC-18DDF1CC28`, `IFC-031AC14F4D`, `IFC-FABC00F58B`. |
| CWP-REQ-004 | The Electrical Power interface shall reflect the MV source basis: the 4160V MCC is fed from the 13.8 kV to 4.16 kV, 12 MVA transformer and serves the 4000V driven motors (KM-2150 / KM-2250) for which the VFD is the starting basis per SCA-001 VE #34. | Confirm against `3-25_Comp_and_Liquids_DBM.md` 4160V MCC section and lines 324-326. |
| CWP-REQ-005 | The Construction Work Package shall carry a verification hold for harmonic and reactive-power mitigation pending detailed electrical studies; capacitor banks shall not be reinstated on the synchronous bus on MCC-8200 where VFDs are present. | Confirm against DBM 4160V MCC section (line 756) and the detailed-electrical-studies hold register. |
| CWP-REQ-006 | The I&C / Control Cabling and Communications / Network interfaces shall preserve EtherNet connectivity to the plant PLC central control panel and accommodate UPS-served MV breaker control and MV protective relay (120 VAC / 125 VDC). | Confirm against DBM 4160V MCC section and UPS services row (line 736). |
| CWP-REQ-007 | Foundation, structural support, seismic detailing, frost/cold-weather provisions, and settlement criteria shall not be closed until the final geotechnical report and vendor equipment load data are accepted. | Confirm readiness gate cites DBM SEC-02 / SEC-11 and the vendor equipment package. |
| CWP-REQ-008 | Cold-weather installation, handling, and commissioning controls shall reflect the -40 deg C minimum ambient governing exposed equipment, control panels, instrumentation, and field devices. | Confirm against DBM SEC-02 Design Implications. |
| CWP-REQ-009 | Standards and code references unavailable in the workspace shall be treated as verification requirements, not closed requirements. | Confirm standards register marks unavailable source locations as `location TBD` or verification-required. |
| CWP-REQ-010 | ASSUMPTION: Before issue for construction, the Construction Work Package shall be aligned with the accepted EPC Package Datasheet, vendor engineered equipment package, IFC electrical drawings, plot plan, equipment list, and protection/coordination study outputs. | Confirm against `DEL-019-02_package-datasheet`, `DEL-019-04_vendor-engineered-equipment-package`, and project IFC deliverables when available. |
| CWP-REQ-011 | The package shall preserve Maintenance Access provisions for the MV VFD enclosure (operating clearances, arc-flash boundaries, lifting access, and replacement-component access). | Confirm against vendor equipment package and IFC layout; mark `TBD` where source values are unavailable. |

## Standards

| Standard / authority | Status |
|---|---|
| NEMA MG1 | Referenced as the motor compliance basis for the VFD-driven inlet compressor motors (DBM lines 324, 533); applicability to VFD output coordination is a detailed-electrical-design verification item. |
| SCA-001 VE #34 (starting VFD basis) | Authoritative for KM-2150 / KM-2250 starting basis (DBM lines 326, 756). |
| SCA-001 VE #37 (capacitor banks on MCC-8200) | Authoritative for removal of capacitor banks where VFDs are present (DBM line 756). |
| Final geotechnical report | Required before foundation design closure; not accessible in current deliverable source set. |
| Project electrical specifications, protection/coordination studies, harmonic studies, arc-flash study | `location TBD`; required for closure of VFD ratings, mitigation, protection, and maintenance access criteria. |
| Project specifications and standards register | `location TBD`; DBM SEC-15 states unavailable citations must be verified before final issue. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Package identity | Document review | Matches `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`. |
| Interface coverage | Checklist review | Includes all six declared interface types for `PKG-019`. |
| Electrical Power tie-in | Engineering review and field inspection hold point | Source-side feed from the 4160V MCC and load-side connection to the driven motor match accepted electrical drawings; phasing, cable, termination, and grounding witnessed. |
| Grounding / Bonding | Field inspection and continuity/impedance test record | Grounding/bonding installation matches accepted electrical drawings and project grounding specification. |
| I&C / Control Cabling | Loop check and signal verification | Control wiring to MCC and PLC matches drawings; MV breaker control and protective relay signals verified. |
| Communications / Network | Network commissioning record | EtherNet connectivity to plant PLC central control panel verified. |
| Harmonic / reactive-power mitigation hold | Design readiness review | Detailed electrical studies (harmonic, reactive, protection/coordination, arc-flash) accepted or exceptioned as `TBD`. |
| Foundations / structural supports | Civil/structural inspection and turnover | Foundation, anchorage, and structural support installation matches accepted civil/structural drawings; final geotechnical inputs accepted or exceptioned. |
| Maintenance Access | Layout review and walk-down | Clearances, arc-flash boundaries, and replacement-component access verified per accepted layout. |
| Cold-weather readiness | Commissioning review | Installation, heat tracing, lubricant, and operational provisions match -40 deg C minimum ambient basis. |
| Construction turnover | Turnover package review | Construction records, inspections, exceptions, and interface signoffs complete. |
| Standards verification | Standards register check | Unavailable standards are not represented as closed. |

## Documentation

The deliverable shall include or reference:

- construction work package;
- installation and tie-in workface plan;
- construction interface and turnover checklist;
- interface checklist for Electrical Power;
- interface checklist for Grounding / Bonding;
- interface checklist for I&C / Control Cabling;
- interface checklist for Communications / Network;
- interface checklist for Maintenance Access;
- interface checklist for Structural / Foundations / Supports;
- construction inspection and turnover records;
- unresolved criteria register for VFD ratings, harmonic/reactive mitigation, geotechnical, IFC drawing, electrical specification, protection/coordination, arc-flash, and regulatory items.
