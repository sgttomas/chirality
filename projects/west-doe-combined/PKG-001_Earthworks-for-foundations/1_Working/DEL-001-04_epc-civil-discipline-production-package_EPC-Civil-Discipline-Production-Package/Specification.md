# Specification: DEL-001-04_epc-civil-discipline-production-package

## Scope

This specification covers the EPC / Civil Discipline Production Package for PKG-001, Earthworks for foundations. The package is a non-vendor Civil production unit for the workbook-defined WBS 01 package row carrying the interface flags `Grading / Site Drainage / Spill Containment` and `Structural / Foundations / Supports`.

The deliverable shall provide a source-limited discipline production basis and closure record for civil earthworks/foundation production activities. It shall not invent final geotechnical, topographical, plot-plan, drainage-sizing, pavement, or detailed construction values where the accepted sources leave those values open.

Excluded from this deliverable unless later assigned by human ruling:

- Vendor-owned package engineering and vendor documentation.
- Final plot-plan drawing production.
- Final geotechnical report production.
- Final topographical survey production.
- Electrical, controls, and instrumentation implementation details except where civil support is required.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-001 | The production package shall identify PKG-001 as the Civil package `Earthworks for foundations`, WBS 01, CoA tracking number 26020-01-42-001. | 26020-Packages_Interfaces_4_export.xlsx, `Packages` sheet row 2 |
| REQ-002 | The production package shall preserve the workbook interface flags for grading/site drainage/spill containment and structural/foundations/supports as governing package interfaces. | 26020-Packages_Interfaces_4_export.xlsx, `Packages` sheet row 2 |
| REQ-003 | Civil and structural engineering shall apply the latest edition of the governing civil and structural codes and standards listed in the DBM, unless superseded by later accepted project criteria. | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Governing Civil and Structural Basis |
| REQ-004 | The package shall carry the SEC-11 civil scope basis for facility pad, drainage system, retention pond, roads, foundations, process and utility modules, permanent buildings, and ancillary buildings where applicable to Earthworks for foundations. | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Civil Scope |
| REQ-005 | The package shall treat geotechnical parameters, topographical survey/grade-surface content, retention pond location/capacity, final IDF duration, road pavement layer thicknesses, geotextile need, and compressor dynamic analysis as open until their source inputs are accepted. | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 External Dependencies and Assumptions |
| REQ-006 | Site grading and drainage criteria shall prevent off-site surface overflow from entering the expansion facility and direct/contain on-site overflow into the retention pond. | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| REQ-007 | The package shall apply the DBM-stated grading and drainage design principles unless replaced by accepted detailed engineering or geotechnical requirements. | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| REQ-008 | Foundation basis shall use driven steel piles as the default support basis for buildings, equipment, towers, tanks, modules, pipe racks, and similar structures unless a more specific foundation basis is listed or detailed engineering confirms a different support requirement. | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Piles and Foundations |
| REQ-009 | The production package shall include a source-limited requirements closure record identifying unsupported detailed discipline requirements as `TBD`, `ASSUMPTION`, or items requiring human ruling. | Gate 7 `ARTIFACT_REGISTER.csv`, ART-E0DE278193; `_CONTEXT.md` Notes |

## Standards

| Standard or Basis | Current Treatment | Source |
|---|---|---|
| National Building Code of Canada | Governing building code for civil/structural basis; edition/location detail TBD where not stated in the package-specific source slice | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Governing Civil and Structural Basis |
| CAN/CSA-S16 Design of Steel Structures | Governing steel design standard | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Governing Civil and Structural Basis |
| CAN/CSA A23.3 Design of Concrete Structures | Governing concrete design standard | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Governing Civil and Structural Basis |
| Canadian Foundation Engineering Manual | Governing foundation engineering basis | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Governing Civil and Structural Basis |
| CSA G40.20/G40.21 | Structural steel material basis: 350W for W-flange and HSS; 300W for channels, plates, and angles | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Governing Civil and Structural Basis |
| CSA A23.1/A23.2 | Concrete materials, construction, and testing basis | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Governing Civil and Structural Basis |
| Rational Method, Q = CIA | Runoff calculation basis | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Governing Civil and Structural Basis |
| Manning's equation | Ditch and culvert sizing basis | `DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Governing Civil and Structural Basis |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-001, REQ-002 | Check production package cover sheet/register against workbook row 2 and Gate 7 PKG-001/DEL-001-04 register entries. |
| REQ-003, REQ-004 | Check discipline basis section against DBM SEC-11 civil scope and governing basis table. |
| REQ-005 | Check closure record for explicit listing of open geotechnical, topographical, plot-plan, drainage, pavement, geotextile, and dynamic-analysis items. |
| REQ-006, REQ-007 | Check grading/drainage design criteria section against DBM SEC-11 design principles; any deviations require accepted source or human ruling. |
| REQ-008 | Check foundation basis section against DBM SEC-11 piles/foundations table; package-specific alternatives require accepted detailed engineering evidence. |
| REQ-009 | Check that unsupported values remain marked `TBD`, `ASSUMPTION`, or human-ruling items and are not silently resolved. |

## Documentation

The production package shall include or reference, at minimum:

- Discipline production package basis.
- TBD discipline deliverable register.
- Source-limited requirements closure record.
- Workbook row 2 package identity and interface facts.
- Gate 7 package, deliverable, artifact, and objective mapping records.
- DBM SEC-11 civil basis excerpts or traceable references.
- External input register for geotechnical report, topographical survey/grade surface, plot plan CIV-235633-5002, detailed drainage design, and applicable dynamic analysis.
