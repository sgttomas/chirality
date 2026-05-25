# Specification: EPC / Civil Discipline Production Package

## Scope

This specification governs the DEL-006-04 Civil discipline production package for PKG-006 Containment Berms. The package is a non-vendor EPC/discipline production unit for the civil containment-berm scope carried from the accepted Gate 7 decomposition and civil DBM support.

The package covers the source-limited discipline production basis for SOW-0006, including the accepted interface facts for Drain / Containment and Grading / Site Drainage / Spill Containment. It excludes final detailed civil design values that depend on missing or deferred inputs, including completed geotechnical report, topographical survey, grade surface file, plot plan, final hydrology inputs, and detailed engineering drainage design.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| REQ-006-04-001 | The production package shall identify PKG-006 as a Civil package for Containment Berms under WBS 03 with CoA tracking number 26020-03-42-006. | PACKAGE_REGISTER.csv, PKG-006 | Check package identity table against Gate 7 register. |
| REQ-006-04-002 | The production package shall carry Drain / Containment as an applicable interface fact. | INTERFACE_REGISTER.csv, IFC-62ACD644F9 | Check interface matrix includes this interface. |
| REQ-006-04-003 | The production package shall carry Grading / Site Drainage / Spill Containment as an applicable interface fact. | INTERFACE_REGISTER.csv, IFC-2A535A882C | Check interface matrix includes this interface. |
| REQ-006-04-004 | Surface-water management basis shall prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. | 3-25_Comp_and_Liquids_DBM.md, Surface Water and Drainage | Review grading/drainage basis notes and civil drawings when available. |
| REQ-006-04-005 | Process-contaminated drainage shall be routed to the appropriate drain or containment system rather than surface-water discharge. | 3-25_Comp_and_Liquids_DBM.md, Surface Water and Drainage | Check drainage segregation notes and tie-in list. |
| REQ-006-04-006 | Site grading and drainage shall prevent off-site surface overflow from entering the expansion facility while directing and containing on-site overflow into a retention pond. | 4-25_Deepcut_DBM.md, Site Grading and Surface Water Management | Check grading and drainage package against stated intent. |
| REQ-006-04-007 | The production package shall carry the DBM site grading principles: pipe-rack high ridges, facility pad slope of 1.5% from pipe racks, allowable 1.0% reduced slope, 3H:1V maximum grade slope unless otherwise engineered or geotechnically mandated, 0.2% minimum ditch slope, and 0.5% minimum / 1.0% preferred culvert slope. | 4-25_Deepcut_DBM.md, Site Grading and Surface Water Management | Check design criteria register and civil drawing notes. |
| REQ-006-04-008 | Ditch and culvert sizing basis shall use the 1:10 year, 15 minute IDF curve until detailed engineering confirms final IDF duration. | 4-25_Deepcut_DBM.md, Site Grading and Surface Water Management | Check drainage calculation basis. |
| REQ-006-04-009 | The package shall carry uncertainty in the NBCC 2020 Dawson Creek IDF proxy until final hydrology inputs are confirmed. | 3-25_Comp_and_Liquids_DBM.md, rainfall basis | Check closure record lists hydrology input as open/TBD. |
| REQ-006-04-010 | An on-site retention pond with berm shall be carried as required for natural runoff capture, with location and capacity left TBD pending detailed engineering and plot plan coordination. | 4-25_Deepcut_DBM.md, Site Grading and Surface Water Management | Check retention pond basis and open input log. |
| REQ-006-04-011 | For the NGL storage area, the package shall consider a berm, elevation decline, or other surface-control feature for accidental leak or spill containment and grading that redirects NGL away from pipe rack and process areas. | 4-25_Deepcut_DBM.md, Site Grading and Surface Water Management | Check civil surface-control notes for NGL storage interface, if in this package boundary. |
| REQ-006-04-012 | The package shall maintain a source-limited requirements closure record because detailed discipline requirements are not present in the current source set. | ARTIFACT_REGISTER.csv, ART-5AEDE189AA | Check closure record exists and lists open source gaps. |

## Standards

| Standard / basis | Application | Source |
|---|---|---|
| National Building Code of Canada | Building code basis. | 4-25_Deepcut_DBM.md, Governing Civil and Structural Basis |
| CAN/CSA-S16 | Steel design. | 4-25_Deepcut_DBM.md, Governing Civil and Structural Basis |
| CAN/CSA A23.3 | Concrete design. | 4-25_Deepcut_DBM.md, Governing Civil and Structural Basis |
| CSA A23.1/A23.2 | Concrete materials, construction, and testing. | 4-25_Deepcut_DBM.md, Governing Civil and Structural Basis |
| Canadian Foundation Engineering Manual | Foundation engineering. | 4-25_Deepcut_DBM.md, Governing Civil and Structural Basis |
| Rational Method, Q = CIA | Runoff calculations. | 4-25_Deepcut_DBM.md, Governing Civil and Structural Basis |
| Manning's equation | Ditch and culvert sizing. | 4-25_Deepcut_DBM.md, Governing Civil and Structural Basis |
| NFPA 30-2023 | Secondary containment basis. | 4-25_Deepcut_DBM.md, standards table |
| API 2510 | Spacing basis for pressurized bullets relative to spill containment and drainage where applicable to NGL storage interfaces. | 4-25_Deepcut_DBM.md, Atmospheric Tank and General Plant Spacing; Fired Equipment Spacing |

## Verification

| Verification item | Acceptance basis |
|---|---|
| Package identity check | Matches Gate 7 PACKAGE_REGISTER.csv and DELIVERABLE_REGISTER.csv entries for PKG-006 / DEL-006-04. |
| Interface check | Includes Drain / Containment and Grading / Site Drainage / Spill Containment as applicable interface facts. |
| Civil basis check | Cites the civil DBM source slices for grading, drainage, retention pond, and containment surface controls. |
| Open input check | Lists geotechnical report, topographical survey/grade surface file, plot plan, hydrology confirmation, and detailed drainage design as open where not available. |
| Consistency check | Datasheet attributes, specification requirements, guidance principles, and procedure verification hooks use the same terminology and source basis. |

## Documentation

The production package should include, at minimum:

- Discipline production package basis.
- TBD discipline deliverable register.
- Source-limited requirements closure record.
- Interface matrix for Drain / Containment and Grading / Site Drainage / Spill Containment.
- Civil design criteria and open-input register for geotechnical, topographical, plot-plan, hydrology, and detailed drainage dependencies.
