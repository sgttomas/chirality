# Package Datasheet Specification

## Scope

This specification governs the content and verification basis for `DEL-001-02_package-datasheet`, the EPC Integrator package datasheet for `PKG-001 - Earthworks for foundations`.

The deliverable covers the package data required for third-party vendor or discipline package engineering and design, including:

- package technical datasheet content;
- vendor or discipline engineering handoff basis;
- package interface requirements matrix;
- source-supported equipment and design criteria.

Excluded or unresolved items:

- Package-specific exclusions are TBD; no exclusions are stated in the accessible source materials.
- Final geotechnical, topographical, plot-plan, drainage, and dynamic-analysis inputs are TBD where identified by the DBM.
- This datasheet does not replace detailed civil design calculations, drawings, or final discipline specifications.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-001 | The datasheet shall identify package `PKG-001`, workbook ID 1, workbook row 2, WBS 01, CoA tracking number `26020-01-42-001`, discipline Civil, and package name "Earthworks for foundations." | Check against Workbook Packages row 2 and Gate 7 PACKAGE_REGISTER.csv. |
| REQ-002 | The datasheet shall carry the two source-supported physical interface types for PKG-001: Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports. | Check against Gate 7 INTERFACE_REGISTER.csv and source workbook row 2 X-column values. |
| REQ-003 | The datasheet shall identify that the responsibility model is source-dependent and shall not infer a separate vendor-package ownership model from the current sources. | Check against Gate 7 PACKAGE_REGISTER.csv, PKG-001. |
| REQ-004 | The datasheet shall include civil/structural scope context for facility pad, drainage system, retention pond, roads, foundations, process and utility modules, permanent buildings, and ancillary buildings. | Check against DBM-Deepcut Civil Scope. |
| REQ-005 | The datasheet shall record geotechnical and topographical inputs as TBD where the DBM says they depend on future assessment, survey, or detailed engineering. | Check against DBM-Deepcut Geotechnical and Topographical Assumptions and External Dependencies. |
| REQ-006 | The datasheet shall include the current site grading and drainage criteria only where stated in the DBM, including pad slopes, ditch/culvert slopes, maximum grade slope, road widths, road crown, and current storm basis. | Check against DBM-Deepcut Site Grading and Surface Water Management and Roads. |
| REQ-007 | The datasheet shall identify default foundation basis as driven steel piles unless a more specific listed basis or detailed engineering confirms otherwise. | Check against DBM-Deepcut Piles and Foundations. |
| REQ-008 | The datasheet shall preserve unsupported values as `TBD` and label inferred associations as `ASSUMPTION` when used. | Document review. |

## Standards

| Standard or basis | Application | Source |
|---|---|---|
| National Building Code of Canada | Structural and foundation engineering; building engineering, snow/rain/wind/seismic loading, egress. | DBM-Deepcut Governing Civil and Structural Basis; Buildings and Miscellaneous Facilities |
| CAN/CSA-S16 Design of Steel Structures | Steel design. | DBM-Deepcut Governing Civil and Structural Basis |
| CAN/CSA A23.3 Design of Concrete Structures | Concrete design. | DBM-Deepcut Governing Civil and Structural Basis |
| Canadian Foundation Engineering Manual | Foundation engineering. | DBM-Deepcut Governing Civil and Structural Basis |
| CSA G40.20/G40.21 | Structural steel material basis. | DBM-Deepcut Governing Civil and Structural Basis |
| CSA A23.1/A23.2 | Concrete materials, construction, and testing. | DBM-Deepcut Governing Civil and Structural Basis |
| Rational Method, Q = CIA | Runoff calculations. | DBM-Deepcut Governing Civil and Structural Basis |
| Manning's equation | Ditch and culvert sizing. | DBM-Deepcut Governing Civil and Structural Basis |
| BCBC-2018 | Building code basis in project codes and standards register. | DBM-Deepcut Codes and Standards Summary |
| CSA S16:19 | Structural steel design in project codes and standards register. | DBM-Deepcut Codes and Standards Summary |
| CSA W59-18 | Structural welding basis. | DBM-Deepcut Codes and Standards Summary |
| NFPA 30-2023 | Secondary containment basis. | DBM-Deepcut Codes and Standards Summary |

## Verification

| Verification activity | Acceptance criterion | Evidence record |
|---|---|---|
| Source identity check | Package identity, WBS, CoA tracking number, discipline, and interface flags match source workbook row 2 and Gate 7 registers. | Marked-up datasheet review or source cross-check log. |
| Interface check | Interface matrix contains only source-supported applicable interfaces unless later source material adds more. | Interface register comparison. |
| Civil criteria check | Numeric grading/drainage/foundation criteria match DBM wording and units. | Discipline review comments or calculation basis review. |
| TBD check | Missing geotechnical, survey, plot-plan, drainage, and dynamic-analysis inputs remain TBD pending source receipt. | Open-items/TBD register. |
| Cross-document check | Datasheet, guidance, and procedure use consistent package name, IDs, interface terms, and criteria. | P2 consistency review. |

## Documentation

The deliverable package should include or reference:

- package technical datasheet;
- vendor or discipline engineering handoff basis;
- package interface requirements matrix;
- source-supported equipment and design criteria;
- TBD/open-items list for geotechnical, topographical, plot-plan, drainage, and dynamic-analysis inputs;
- source register identifying workbook row 2, Gate 7 registers, and DBM-Deepcut civil source sections.
