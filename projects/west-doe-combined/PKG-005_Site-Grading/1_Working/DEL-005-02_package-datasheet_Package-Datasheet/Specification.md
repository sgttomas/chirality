# Specification: DEL-005-02_package-datasheet - Package Datasheet

## Scope

This specification governs the EPC Integrator package datasheet for PKG-005 Site Grading. The datasheet covers the civil package handoff basis needed for third-party discipline engineering and design, including package identity, source basis, physical interface facts, and source-supported site grading, drainage, and containment criteria.

The datasheet excludes final civil design values not present in the accepted source basis, including final grading elevations, slopes, hydrology inputs, drainage design flow, retention sizing, and final geotechnical parameters. Those values remain `TBD` until confirmed by the civil design package, final hydrology inputs, and final geotechnical report.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| REQ-005-02-001 | The datasheet must identify PKG-005 as Site Grading, Civil discipline, WBS 03, CoA tracking number 26020-01-42-003. | 26020-Packages_Interfaces_4_export.xlsx, Packages row 6; Gate 7 PACKAGE_REGISTER row PKG-005 | Check datasheet Identification and Attributes tables. |
| REQ-005-02-002 | The datasheet must carry the workbook interface facts for Drain / Containment and Grading / Site Drainage / Spill Containment as applicable. | 26020-Packages_Interfaces_4_export.xlsx, Packages row 6; Gate 7 INTERFACE_REGISTER IFC-590C44EF2F and IFC-F6589335A4 | Check interface requirements matrix against Gate 7 INTERFACE_REGISTER. |
| REQ-005-02-003 | Surface-water management criteria in the datasheet must preserve the DBM requirement to prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-11 Surface Water and Drainage | Confirm Datasheet Conditions and Guidance Considerations state the constraint without adding unsupported numeric values. |
| REQ-005-02-004 | Process-contaminated drainage must be distinguished from surface-water discharge and routed to the appropriate drain or containment system. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-11 Surface Water and Drainage | Check datasheet conditions and procedure verification checklist. |
| REQ-005-02-005 | Current hydrology/rainfall uncertainty must be retained as an open basis item. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-02 Site and Climatic Design Basis | Confirm unsupported hydrology and retention values remain `TBD`. |
| REQ-005-02-006 | Final geotechnical closure must not be implied by this package datasheet. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-02 Geotechnical and Seismic Basis; SEC-11 Site and Civil Conditions | Confirm foundation/geotechnical dependencies are listed as `TBD` or prerequisite inputs. |
| REQ-005-02-007 | The datasheet must include the anticipated artifacts: package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, and source-supported equipment/design criteria where available. | `_CONTEXT.md`; Gate 7 ARTIFACT_REGISTER rows for DEL-005-02_package-datasheet | Check Documentation section and Datasheet references. |

## Standards

| Standard / authority | Applicability | Status |
|---|---|---|
| Gate 7 final published PROJECT_DECOMP snapshot | Accepted decomposition truth for package/deliverable identity, artifacts, objectives, and interface facts. | Accessible and used. |
| 26020-Packages_Interfaces_4_export.xlsx | Authoritative workbook source for row 6 package identity and interface applicability. | Accessible and used. |
| DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md | Source for 03-25 civil/site/drainage and design-basis constraints. | Accessible and used. |
| NBCC 2020 Dawson Creek IDF proxy | Current rainfall basis proxy pending site-specific update. | Cited by DBM; exact source table outside this deliverable is not independently reinterpreted. |
| Final geotechnical report | Required for design closure. | TBD; not present in accessible source slices. |

## Verification

1. Confirm all package identity fields match Gate 7 PACKAGE_REGISTER row PKG-005 and workbook Packages row 6.
2. Confirm the interface requirements matrix contains exactly the applicable source-supported interfaces for row 6: Drain / Containment and Grading / Site Drainage / Spill Containment.
3. Confirm civil/site design statements cite DBM SEC-02 or SEC-11 and do not introduce uncited numeric criteria.
4. Confirm all missing design values are marked `TBD`.
5. Confirm open hydrology and geotechnical basis items are preserved for human/design-team closure.

## Documentation

The package datasheet set should retain or produce:

- Package technical datasheet.
- Vendor or discipline engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria, with unsupported values marked `TBD`.
- Open-source-gap list for final hydrology, geotechnical, and package-specific grading/drainage values.
