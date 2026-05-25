# Specification: EPC / Civil Discipline Production Package

## Scope

This specification covers the source-limited EPC / Civil Discipline Production Package for `PKG-002` Earthworks for foundations, WBS `02`, CoA tracking number `26020-01-42-001`.

The deliverable is a non-vendor Civil production unit. It is limited to the discipline production package basis, a TBD discipline deliverable register, and a source-limited requirements closure record identified in Gate 7 for `DEL-002-04`.

The deliverable excludes final foundation design closure until the final geotechnical report and detailed engineering analyses are accepted. It also excludes unstated package-specific civil criteria, drawing lists, quantities, material specifications, and construction means/methods that are not present in accessible sources.

Sources: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`; Gate 7 `PACKAGE_REGISTER.csv`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.

## Requirements

| ID | Requirement | Source / status | Verification |
|---|---|---|---|
| REQ-001 | The production package shall identify `PKG-002` as Civil package "Earthworks for foundations" under WBS `02` with CoA tracking number `26020-01-42-001`. | Workbook `Packages` sheet row ID # 2; Gate 7 `PACKAGE_REGISTER.csv` row `PKG-002` | Check package identity block against source row |
| REQ-002 | The production package shall carry the applicable interfaces marked for `PKG-002`: Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports. | Workbook `Packages` sheet row ID # 2; Gate 7 `INTERFACE_REGISTER.csv` rows `IFC-E58D0EFA8E` and `IFC-0B377574CA` | Check interface matrix includes both interfaces |
| REQ-003 | Civil design basis content shall cover only source-supported civil topics: grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security. | DBM SEC-11 Site and Civil Conditions | Check topic list against DBM SEC-11 |
| REQ-004 | Foundation design closure shall remain open until the final geotechnical report is accepted. | DBM SEC-02 Design Implications; DBM SEC-11 Site and Civil Conditions | Confirm closure record marks geotechnical report as required input |
| REQ-005 | Surface-water management requirements shall address uncontrolled offsite discharge prevention, process area protection, and construction/operations access support. | DBM SEC-11 Surface Water and Drainage | Check drainage section includes these three functions |
| REQ-006 | Process-contaminated drainage shall not be treated as surface-water discharge and shall be routed to the appropriate drain or containment system. | DBM SEC-11 Surface Water and Drainage | Check interface/requirements closure record captures contaminated drainage routing |
| REQ-007 | Site-specific values used by the production package shall retain their source status where not closed: soil description is TBC, terrain type is TBD, and geotechnical placeholders are not final construction criteria. | DBM SEC-02 Geotechnical / Seismic Parameter table and Design Implications | Check datasheet/status fields preserve TBD/TBC labels |
| REQ-008 | Detailed discipline deliverable register content shall be marked `TBD` unless supported by a later accepted discipline deliverable list. | Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-002-04`; no deliverable-specific source slice copied during PREPARATION | Check register fields are not invented |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Gate 7 final published PROJECT_DECOMP snapshot | Accepted decomposition truth for package, scope, objectives, deliverable identity, artifacts, and interfaces | Authoritative decomposition basis |
| 03-25 Compressor Station and Liquids Hub DBM | Source for civil/site/foundation/drainage basis slices used in this draft | Accessible source; derivative DBM publication, not a substitute for decomposition truth |
| Final geotechnical report | Required before foundation design closure | TBD; not accessible in current source set |
| Topographical survey / plot plan / detailed engineering analyses | Needed for more specific project civil requirements where applicable | ASSUMPTION: likely required by DBM SEC-11 language; specific documents not accessible here |
| Civil codes and project specifications | TBD | No clause-level civil code/specification text available in the accessible source set |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Package identity verification | Compare identification fields to workbook row ID # 2 and Gate 7 package/deliverable registers | No mismatch in package ID, WBS, CoA tracking number, name, discipline, or deliverable ID |
| Interface verification | Compare package interface matrix to workbook row ID # 2 and Gate 7 interface register | Both applicable interface types present; no unsupported interfaces added |
| Source limitation verification | Review requirements and datasheet values against cited source slices | Unsupported values marked `TBD` or `ASSUMPTION` |
| Geotechnical closure verification | Confirm final geotechnical report remains an explicit blocker to foundation design closure | Closure record does not present placeholder geotechnical values as final criteria |
| Drainage basis verification | Confirm surface-water and contaminated-drainage requirements match DBM SEC-11 | Surface-water and contaminated drainage are separated |

## Documentation

The production package should contain or reference the following records:

- Discipline production package basis.
- Package identity and interface matrix.
- Civil/site/foundation/drainage requirement summary.
- TBD discipline deliverable register.
- Source-limited requirements closure record.
- Geotechnical input status record.
- ASSUMPTION: drawing, calculation, model, and construction support registers may be required by EPC execution, but their contents are TBD because no source-supported discipline register is available.
