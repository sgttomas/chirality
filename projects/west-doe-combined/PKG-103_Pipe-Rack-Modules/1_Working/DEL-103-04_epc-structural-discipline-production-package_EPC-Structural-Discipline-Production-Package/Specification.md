# Specification: EPC / Structural Discipline Production Package — PKG-103 Pipe Rack Modules

## Scope

This specification governs the DEL-103-04 Structural discipline production package for PKG-103 Pipe Rack Modules. The package is a non-vendor EPC/discipline production unit for the structural design and supply scope of the facility pipe rack modules, carried from the accepted Gate 7 PROJECT_DECOMP snapshot and supported by the structural/civil basis in the DBM-Deepcut and DBM-Comp_and_Liquids source slices.

In scope:
- Structural design of the pipe rack modules and their foundations.
- The nine accepted physical interface facts for PKG-103 (Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; EHT; I&C / Control Cabling; Communications / Network; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports).
- Identification of source-supported design basis values (steel grades, governing codes, foundation default, ambient/site basis).
- A source-limited requirements closure record capturing detailed design values not yet available.

Excluded (carried as `TBD` until detailed engineering or external inputs are accepted):
- Final pile design parameters and bearing capacities (depend on the geotechnical report).
- Final pipe rack geometry, bay spacing, tier counts, and rack-supported commodity loading (depend on plot plan, P&IDs, and 3D model).
- Final structural load combinations beyond NBCC defaults.
- Detailed connection design, anchorages, and shop-vs-field erection split for the rack modules.
- Detailed pipe stress, anchor, and guide loads delivered by the piping discipline.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| REQ-103-04-001 | The production package shall identify PKG-103 as a Structural package for Pipe Rack Modules under WBS 03 with CoA tracking number 26020-03-36-003. | `PACKAGE_REGISTER.csv` row PKG-103 | Check package identity table against Gate 7 register. |
| REQ-103-04-002 | The production package shall carry the nine accepted PKG-103 interface facts (Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; EHT; I&C / Control Cabling; Communications / Network; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports) as applicable interfaces, each cited to its IFC ID. | `INTERFACE_REGISTER.csv` rows IFC-1B5D83EC66, IFC-AECC45897E, IFC-933A9B9DC3, IFC-3268483707, IFC-489CEA5AA8, IFC-FC76A7E07D, IFC-38D5605A15, IFC-E2FEA8FA23, IFC-BC9813EE49 | Check interface matrix includes all nine entries. |
| REQ-103-04-003 | The production package shall record that pipe racks and pipe rack modules are designed exclusively by the EPC Integrator (Gate 6 disposition carried on each PKG-103 interface fact). | `INTERFACE_REGISTER.csv` Note column for PKG-103 rows | Check responsibility note appears in the package basis. |
| REQ-103-04-004 | Structural and foundation engineering shall apply the governing civil/structural basis: National Building Code of Canada (building code), CAN/CSA-S16 (steel design), CAN/CSA A23.3 (concrete design), CSA A23.1/A23.2 (concrete materials and testing), Canadian Foundation Engineering Manual (foundation engineering). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Governing Civil and Structural Basis | Confirm design criteria register lists these standards. |
| REQ-103-04-005 | Structural steel material shall be CSA G40.20/G40.21 350W for W-flange and HSS, and 300W for channels, plates, and angles. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Governing Civil and Structural Basis | Confirm structural material spec sheet matches grades. |
| REQ-103-04-006 | The default foundation basis for pipe racks shall be driven steel piles unless detailed engineering or the geotechnical report confirms otherwise. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Piles and Foundations | Confirm foundation concept register cites driven steel piles for pipe racks. |
| REQ-103-04-007 | Foundation design for pipe racks shall consider equipment loads, snow/wind/seismic per NBCC, frost protection, vibration, settlement, and maintenance access; equipment-specific anchorage checks are required. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Foundations and Structural Supports | Confirm foundation design checklist includes each load case. |
| REQ-103-04-008 | The package shall carry the site/environmental basis of -40 deg C to +35 deg C ambient and 673 m AMSL elevation for sizing and material-selection decisions on the rack modules. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Site and Civil Conditions | Confirm design basis register includes ambient and elevation. |
| REQ-103-04-009 | Pipe rack grading interface shall observe the high equal-elevation ridge along the main pipe rack with facility pad slope of 1.5% to each side (allowable reduction to 1.0% where required for top-of-pile-cap elevations). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Site Grading and Surface Water Management | Confirm grading interface note in production package basis. |
| REQ-103-04-010 | Pipe rack areas shall be treated as outdoor general-purpose non-hazardous unless detailed classification drawings identify otherwise; this assumption shall be carried until area-classification drawings are accepted. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Area Classification | Confirm area-classification note in design basis. |
| REQ-103-04-011 | Final pile design parameters (bearing capacity, LPILE curves, dynamic design criteria) shall be marked `TBD` and the geotechnical report listed as the required external input. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Geotechnical and Topographical Assumptions; External Dependencies | Confirm closure record lists geotechnical report as open. |
| REQ-103-04-012 | Pipe rack geometry, tier count, bay spacing, and rack-supported commodity loading shall be marked `TBD` pending plot plan, P&IDs, 3D model, and pipe stress deliverables. | `INTERFACE_REGISTER.csv` Note for PKG-103 rows ("Rack-supported commodities should be confirmed against plot plan/model."); decomposition Notes | Confirm closure record lists these inputs as open. |
| REQ-103-04-013 | The shop-vs-field erection split for the pipe rack modules shall be carried as `TBD`; the DBM module/erection table does not enumerate pipe rack modules individually. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Buildings and Miscellaneous Facilities (module/erection table — no rack-module rows) | Confirm closure record lists shop/field split as open. |
| REQ-103-04-014 | The package shall maintain a source-limited requirements closure record because detailed discipline requirements are not present in the current source set. | `DELIVERABLE_REGISTER.csv` Notes, DEL-103-04 | Confirm closure record exists and enumerates open source gaps. |

## Standards

| Standard / basis | Application | Source |
|---|---|---|
| National Building Code of Canada (NBCC) | Building code; snow/wind/seismic load basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Governing Civil and Structural Basis |
| CAN/CSA-S16 | Steel design of pipe rack steelwork. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Governing Civil and Structural Basis |
| CAN/CSA A23.3 | Concrete design (foundations, pile caps where applicable). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Governing Civil and Structural Basis |
| CSA A23.1/A23.2 | Concrete materials, construction, and testing. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Governing Civil and Structural Basis |
| Canadian Foundation Engineering Manual | Foundation engineering basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Governing Civil and Structural Basis |
| CSA G40.20/G40.21 | Structural steel material (350W W-flange/HSS; 300W channels, plates, angles). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Governing Civil and Structural Basis |

## Verification

| Verification item | Acceptance basis |
|---|---|
| Package identity check | Matches Gate 7 PACKAGE_REGISTER.csv and DELIVERABLE_REGISTER.csv entries for PKG-103 / DEL-103-04. |
| Interface check | All nine accepted PKG-103 interface facts included, each cited to its IFC ID; Gate 6 EPC Integrator disposition recorded. |
| Standards check | Design criteria register cites NBCC, CAN/CSA-S16, CAN/CSA A23.3, CSA A23.1/A23.2, Canadian Foundation Engineering Manual, and CSA G40.20/G40.21. |
| Material check | Structural steel grades 350W (W-flange/HSS) and 300W (channels/plates/angles) appear in the structural material spec. |
| Foundation check | Default driven steel pile basis stated for pipe racks; deviation requires geotechnical justification. |
| Open input check | Geotechnical report, topographical survey/grade surface file, plot plan, P&ID/3D model rack loading, and shop/field split listed as `TBD` in the closure record. |
| Site basis check | Ambient temperature range (-40 to +35 deg C), elevation (673 m AMSL), and NBCC snow/wind/seismic appear in the design basis register. |
| Cross-document consistency | Datasheet attributes, Specification requirements, Guidance principles, and Procedure verification hooks use the same terminology, interface IDs, and source citations. |

## Documentation

The production package should include, at minimum:

- Discipline production package basis (structural).
- TBD discipline deliverable register.
- Source-limited requirements closure record (geotechnical report; topographical survey/grade surface file; plot plan; P&ID/3D model rack-loading data; piping stress loads; shop-vs-field erection split; final pile parameters).
- Interface matrix for the nine PKG-103 interfaces, each cited to its IFC ID.
- Structural design criteria sheet citing NBCC, CAN/CSA-S16, CAN/CSA A23.3, CSA A23.1/A23.2, Canadian Foundation Engineering Manual, CSA G40.20/G40.21, site ambient/elevation, and snow/wind/seismic basis.
- Foundation concept register stating driven steel piles as the default pipe rack support and listing open geotechnical parameters.
- Area-classification carry-over note stating outdoor pipe rack baseline as general-purpose non-hazardous pending detailed classification drawings.
