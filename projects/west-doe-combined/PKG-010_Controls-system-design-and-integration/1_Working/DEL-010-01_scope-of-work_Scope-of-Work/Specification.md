# Specification: DEL-010-01_scope-of-work - Scope of Work

## Scope

This deliverable specifies the EPC Integrator scope-of-work basis for `PKG-010`, the WBS 03 Controls system design and integration package. It covers the package identity, source basis, controls package function, interface boundaries, integration narrative, and responsibility assignment record required for the package SOW.

Included scope:

- Package scope of work for `PKG-010`.
- Tagged equipment and package identity list where source-supported.
- Package function and whole-facility integration narrative.
- Responsibility assignment record.
- Interface boundaries recorded for process piping, utility piping, relief/flare/vent, electrical power, I&C/control cabling, communications/network, building HVAC/services, and fire and gas/safety systems.

Excluded or deferred scope:

- Detailed tagged equipment list: TBD; no deliverable-specific tagged equipment list is available in the accepted references for this SOW.
- Package-specific exclusions: TBD; Gate 7 package register states no package-specific exclusions were stated in source materials.
- Final package data maps, permissive logic, trip interfaces, alarm priorities, shutdown levels, cause-and-effect actions, and reset responsibilities: deferred to vendor integration and detailed design.
- Separate controls power-panel deliverable: excluded by Gate 6 disposition; controls power-panel interfaces remain interface facts/artifacts under the package datasheet.

Sources: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, and `INTERFACE_REGISTER.csv`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-13 and SEC-14.

## Requirements

| Req ID | Requirement | Verification |
|---|---|---|
| SOW-010-REQ-001 | The SOW shall identify `PKG-010` as the WBS 03 Controls system design and integration package with CoA tracking number `26020-01-32-001`. Source: Workbook row 11; Gate 7 `PACKAGE_REGISTER.csv` row `PKG-010`. | Confirm package identity fields match Datasheet Identification and Gate 7 package register. |
| SOW-010-REQ-002 | The SOW shall state that the package is a workbook-defined Controls package with recorded physical interfaces. Source: Gate 7 `PACKAGE_REGISTER.csv` row `PKG-010`. | Confirm package basis is included in the SOW scope narrative. |
| SOW-010-REQ-003 | The SOW shall include the mandatory EPC anchor artifacts: package scope of work, tagged equipment/package identity list, package function and whole-facility integration narrative, and responsibility assignment record. Source: Gate 7 `DELIVERABLE_REGISTER.csv` and `ARTIFACT_REGISTER.csv` rows for `DEL-010-01_scope-of-work`. | Confirm each artifact is represented or explicitly marked `TBD` where source support is missing. |
| SOW-010-REQ-004 | The SOW shall carry the source-supported interface types for `PKG-010`: Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems. Source: Workbook row 11; Gate 7 `INTERFACE_REGISTER.csv` rows for `PKG-010`. | Confirm all listed interface types appear consistently in Datasheet, Specification, Guidance, and Procedure. |
| SOW-010-REQ-005 | The SOW shall treat controls power-panel interfaces as interface facts/artifacts under the package datasheet and shall not create or imply a separate controls power-panel package or deliverable. Source: Gate 7 `INTERFACE_REGISTER.csv` notes for `PKG-010`. | Confirm the exclusion/deferred-scope section includes this disposition. |
| SOW-010-REQ-006 | The SOW shall describe the control system as centralized monitoring and control for the 03-25 Compressor Station and Liquids Hub, with the BPCS as primary process control except standalone compression Unit Control Systems integrated for monitoring and alarming. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-13. | Confirm package function narrative matches DBM SEC-13 without over-assigning compression controls to BPCS. |
| SOW-010-REQ-007 | The SOW shall include the I/O network segregation and redundant Ethernet with Parallel Redundancy Protocol as controls integration basis. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-13. | Confirm communications/network interface notes include the DBM network basis. |
| SOW-010-REQ-008 | The SOW shall identify final package data maps, permissive logic, trip interfaces, alarm priorities, trip lists, shutdown levels, cause-and-effect actions, and reset responsibilities as detailed-design/vendor-integration deliverables rather than completed SOW values. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-13 and SEC-14. | Confirm these values are marked deferred/TBD rather than invented. |
| SOW-010-REQ-009 | The SOW shall state that local 03-25 instrument-air compressor controls are not added; the 03-25 instrument-air interface is monitored and alarmed/tripped according to final cause-and-effect logic. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-13. | Confirm instrument-air controls are represented as an interface condition, not local compressor controls. |
| SOW-010-REQ-010 | ASSUMPTION: The SOW should use package-level objective associations OBJ-002, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-009, and OBJ-010 as directional context only, not as independent clause-level requirements. Source: `_CONTEXT.md`; Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` and `OBJECTIVE_PACKAGE_MAP.csv`. | Confirm objective references are framed as context unless a specific source clause supports a requirement. |

## Standards

| Standard / basis | Applicability | Source |
|---|---|---|
| Project specifications, industry standards, codes, regulations, and discipline design documents | General project basis; final standards register to be verified against latest project specification index | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-15 |
| Control system standards, BPCS/RIO architecture, detector and ESD requirements, project instrumentation specifications | Controls and instrumentation basis for this package | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-15 table row "Controls and instrumentation" |
| Project electrical specifications, voltage/MCC/grounding basis, CEC, and area classification standards | Electrical power/interface context where the controls scope touches power, buildings, raceways, grounding, and hazardous area classification | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 and SEC-15 |
| CSA Z662 | Applicable to sour-gas export overpressure protection and pipeline design; included only as adjacent facility-interface context, not a package-specific controls requirement | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-04 sour-gas export controls |

## Verification

| Verification item | Method |
|---|---|
| Package identity | Compare against `_CONTEXT.md`, Gate 7 `PACKAGE_REGISTER.csv`, and workbook row 11. |
| Interface completeness | Compare all SOW interface lists against Gate 7 `INTERFACE_REGISTER.csv` rows for `PKG-010` and workbook row 11. |
| Controls basis | Compare package function and network/control statements against DBM SEC-13. |
| Shutdown and safety interface basis | Compare deferred logic and trip responsibility statements against DBM SEC-14. |
| Deferred values | Confirm unavailable values are marked `TBD` and are not silently inferred. |
| Cross-document consistency | Confirm Datasheet, Guidance, and Procedure use the same package identity, interface list, and deferred controls/shutdown language. |

## Documentation

The SOW package shall produce or preserve these records:

- Package scope of work.
- Tagged equipment and package identity list, with unavailable tagged equipment details marked `TBD`.
- Package function and whole-facility integration narrative.
- Responsibility assignment record.
- Source-basis record citing Gate 7 snapshot rows, workbook row 11, and DBM SEC-13/SEC-14/SEC-15 slices used.
- Deferred/open item list for unavailable detailed-design values and human rulings.
