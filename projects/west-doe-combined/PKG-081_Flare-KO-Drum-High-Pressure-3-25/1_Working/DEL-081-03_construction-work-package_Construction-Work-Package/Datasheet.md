# Datasheet: Construction Work Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | `DEL-081-03_construction-work-package` |
| Deliverable name | Construction Work Package |
| Parent package | `PKG-081` - Flare KO Drum (High Pressure) 3-25 |
| Workbook row | 54 |
| WBS | 02 |
| CoA tracking number | `26020-02-17-001` |
| Discipline | Mechanical |
| Responsible party | EPC Integrator |
| Deliverable type | EPC Construction Work Package |
| Scope items | `SOW-0071`; `SOW-0072`; `SOW-0073`; `SOW-0074` |

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-081-03_construction-work-package`; `PACKAGE_REGISTER.csv` row `PKG-081`.

## Attributes

| Attribute | Current basis | Source |
|---|---|---|
| Package name | Flare KO Drum (High Pressure) 3-25 | `PACKAGE_REGISTER.csv` row `PKG-081` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-081` |
| Package scope basis | Supply two HP flare KO drums and two dedicated transfer pumps. Package vendor is responsible for the package engineering, design, vendor documentation, and physical equipment package; the EPC Integrator is responsible for integrating this package into the whole process facility. | `PACKAGE_REGISTER.csv` row `PKG-081` |
| Applicable interface types | Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv` row `PKG-081`; `INTERFACE_REGISTER.csv` rows `IFC-E6E19CC83E`, `IFC-1F7E9C14E8`, `IFC-2D16BB76D1`, `IFC-81D2B385AE`, `IFC-ABC65133B6`, `IFC-D38D4A85D8`, `IFC-A715F77DE6`, `IFC-4204F7F04E`, `IFC-E06624196C`, `IFC-0B6C1286C7` |
| Construction work package artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | `DELIVERABLE_REGISTER.csv` row `DEL-081-03_construction-work-package` |
| In-scope equipment context | Two HP flare knockout drums (V-4100-2 in the compressor area; V-4150-2 in the tank farm) and their dedicated transfer pumps (P-4100-2 and P-4150-2) that truck-out or transfer collected liquids to slop. HP headers from each KO drum manifold to the shared HP/Cryo flare stack. | `3-25_Comp_and_Liquids_DBM.md` Flare and Blowdown section (line 497) |
| Flare-system facility context | The HP/Cryo and LP dual flare stack is shared between 03-25 and 04-25; the sonic HP/Cryo flare stack is 660 mm OD by 60,957 mm tall. HP and LP relief headers are both carried as 508 mm (20 inch) in the current source basis. | `3-25_Comp_and_Liquids_DBM.md` Flare and Blowdown section (lines 497-499) |
| Blowdown sequencing reference | Staggered blowdown is required to limit maximum relief; external Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001 is a required detailed source for final blowdown sequencing. | `3-25_Comp_and_Liquids_DBM.md` line 501 |
| Word-source detail location | 26020-Package_Requirements.docx package heading 34 (not converted to markdown in the local source set; not directly read in this run). | `PACKAGE_REGISTER.csv` row `PKG-081` SourceReference; `_REFERENCES.md` |
| Declared upstream dependencies | None declared during PREPARATION | `_DEPENDENCIES.md` |
| Declared downstream dependencies | None declared during PREPARATION | `_DEPENDENCIES.md` |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Facility context | 03-25 West Doe Compressor Station and Liquids Hub construction scope includes module setting, mechanical hookups, ISBL/OSBL interconnecting piping, pipe supports, home-run cabling, terminations, area lighting, fencing, security, structural, foundations, and tie-ins. | `3-25_Comp_and_Liquids_DBM.md` Construction Scope Summary (line 73) |
| Ambient design implication | The -40 deg C minimum ambient governs exposed equipment, drums, package piping, control panels, instrumentation, and field devices unless a more severe condition applies; EHT (electric heat tracing) is a declared interface for `PKG-081`. | `3-25_Comp_and_Liquids_DBM.md` SEC-02 Design Implications; `INTERFACE_REGISTER.csv` row `IFC-ABC65133B6` |
| Geotechnical status | Final geotechnical report is required before foundation design closure; current geotechnical values are placeholders where marked. This bears on KO drum and pump foundations and structural supports. | `3-25_Comp_and_Liquids_DBM.md` SEC-02 Geotechnical and Seismic Basis (line 141) |
| Shared flare-system status | The HP/Cryo and LP dual flare stack and incinerator are shared-interface systems whose exact service split and owner interface remain open where source language is not fully resolved. | `3-25_Comp_and_Liquids_DBM.md` Commercial and Facility Interfaces (line 56) |
| Final blowdown loads | Final flare relief and blowdown loads, and the staggered blowdown sequence, remain TBC; the controlling shutdown-and-blowdown philosophy document was not read in this run. | `3-25_Comp_and_Liquids_DBM.md` Flare and Blowdown (line 501); SEC-08 Required Closeout |
| Standards status | Where a standard or external philosophy document is referenced but not available in the workspace, verify the citation before final issue for construction. | `3-25_Comp_and_Liquids_DBM.md` SEC-15 Specifications, Codes, and Standards |

## Construction

| Construction data item | Value |
|---|---|
| Work package boundary | Physical installation, construction, inspection, turnover, and tie-in of two HP flare KO drums (V-4100-2 and V-4150-2) and their two dedicated transfer pumps (P-4100-2 and P-4150-2) into the 03-25 facility, including all ten declared interface types for `PKG-081`. |
| Workface plan minimum contents | Installation sequence; work area limits; module/equipment offload and setting (compressor-area location for V-4100-2; tank-farm location for V-4150-2); pump installation; tie-in/interface checkpoints (Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports); inspection hold and witness points; turnover records; unresolved `TBD` criteria register. |
| Interface checklist minimum contents | Process Piping tie-in checks (HP relief header connection, 508 mm / 20 inch basis); Relief / Flare / Vent tie-in checks (manifold to HP/Cryo flare stack, 660 mm OD x 60,957 mm tall basis); Drain / Containment checks (pump-out/slop transfer routing); Electrical Power checks (pump motor supply); EHT checks (cold-weather heat-tracing per -40 deg C basis); Grounding / Bonding checks; Area / Exterior Lighting checks; I&C / Control Cabling checks (level, pressure, transfer-pump control to plant control system); Maintenance Access checks (drum/pump access, lifting, replacement); Structural / Foundations / Supports checks. |
| HP KO drum mechanical detail (dimensions, MAWP, MDMT, nozzle schedule, internals, materials, weights, lifting lugs) | TBD - not defined in accessible source slices; defined by Package Vendor in the engineered equipment package (`DEL-081-04_vendor-engineered-equipment-package`) and the package datasheet (`DEL-081-02_package-datasheet`). |
| HP transfer pump detail (type, capacity, head, NPSH, driver rating, sealing, materials) | TBD - not defined in accessible source slices; defined by Package Vendor. |
| Foundation, structural support, and seismic detailing for drums and pumps | TBD - depends on final geotechnical report and vendor equipment loads. |
| Final blowdown sequencing and relief loads | TBD - to be confirmed against the external Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001 before construction issue. |
| Shared-system interface ownership (HP/Cryo flare stack and incinerator service split) | TBD - shared between 03-25 and 04-25; final ownership and service split requires source ruling. |
| Inspection and acceptance criteria | TBD - to be confirmed from IFC piping/mechanical drawings, project mechanical and piping specifications, vendor pressure-test and commissioning procedures, and the flare-system relief/blowdown studies. |

## References

- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- `_REFERENCES.md`
- Gate 7 `DELIVERABLE_REGISTER.csv`
- Gate 7 `PACKAGE_REGISTER.csv`
- Gate 7 `INTERFACE_REGISTER.csv`
- Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`
- `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Flare and Blowdown; Construction Scope Summary; SEC-02; SEC-08; SEC-15)
- 26020-Package_Requirements.docx package heading 34 (`location TBD` - not accessible in markdown form in this run)
