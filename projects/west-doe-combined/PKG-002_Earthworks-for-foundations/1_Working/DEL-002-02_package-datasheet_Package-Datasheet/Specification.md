# Specification: Package Datasheet

## Scope

This specification defines the minimum content and source-grounding requirements for the EPC Integrator Package Datasheet for `PKG-002 - Earthworks for foundations`, a Civil package under WBS 02.

The datasheet covers the package handoff basis, package identity, civil/interface attributes, and source-supported design criteria needed for third-party vendor or discipline package engineering and design. Source: `_CONTEXT.md` Scope; Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-002-02_package-datasheet`; Gate 7 `PROJECT_DECOMP.md` deliverable-basis section.

Exclusions:

- Detailed construction sequencing is excluded unless explicitly required by a source; it belongs primarily in `DEL-002-03_construction-work-package`.
- Discipline production calculations, drawings, and detailed civil design outputs are excluded unless explicitly carried as datasheet inputs; these belong primarily in `DEL-002-04_epc-civil-discipline-production-package`.
- Unstated design quantities, material classes, compaction values, elevations, and geotechnical parameters are not to be invented.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-001 | The datasheet shall identify package `PKG-002`, package name `Earthworks for foundations`, WBS `02`, CoA tracking number `26020-01-42-001`, discipline `Civil`, and workbook row 3. | Check against `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row 3, and Gate 7 `PACKAGE_REGISTER.csv` row `PKG-002`. |
| REQ-002 | The datasheet shall state that the source package is a workbook-defined Civil package carried as a distinct flat project package for WBS 02. | Check against Gate 7 `SCOPE_LEDGER.csv` row `SOW-0002`. |
| REQ-003 | The datasheet shall include the applicable interface facts `Grading / Site Drainage / Spill Containment` and `Structural / Foundations / Supports`. | Check against `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row 3, and Gate 7 `INTERFACE_REGISTER.csv` rows `IFC-E58D0EFA8E` and `IFC-0B377574CA`. |
| REQ-004 | The datasheet shall preserve workbook interface facts as evidence and shall not promote them into standalone deliverables. | Check against Gate 7 `PROJECT_DECOMP.md` decomposition decisions and deliverable-basis text; Gate 7 `ARTIFACT_REGISTER.csv` interface fact rows for `DEL-002-02_package-datasheet`. |
| REQ-005 | The datasheet shall include the DBM civil basis that civil design covers grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security. | Check against `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Site and Civil Conditions. |
| REQ-006 | The datasheet shall state that final geotechnical report input is required before foundation design closure. | Check against `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Site and Civil Conditions. |
| REQ-007 | The datasheet shall state that surface-water management must prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. | Check against `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Site and Civil Conditions. |
| REQ-008 | The datasheet shall mark package-specific physical limits, quantities, elevations, material classifications, compaction criteria, and battery limits as `TBD` unless supported by a cited accessible source. | Review datasheet values against accessible sources and confirm unsupported values remain `TBD`. |
| REQ-009 | The datasheet shall include the Gate 7 datasheet artifacts: package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, and interface fact evidence. | Check against Gate 7 `ARTIFACT_REGISTER.csv` rows for `DEL-002-02_package-datasheet`. |
| REQ-010 | The datasheet shall not assign a separate vendor package ownership model for this package unless later source material explicitly supports that assignment. | Check against Gate 7 `PACKAGE_REGISTER.csv` row `PKG-002`, ResponsibilityModel. |

## Standards

| Standard or basis | Applicability |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package, deliverable, artifact, interface, objective, and scope mapping. |
| `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row 3 | Authoritative workbook source for package identity and interface flags. |
| `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Plant Layout, Spacing, Civil, and Buildings | Source basis for civil, drainage, and foundation design considerations. |
| NBCC | ASSUMPTION: likely applicable civil/structural code basis because the DBM compliance matrix lists NBCC under Civil/structural, but clause-level application to this datasheet is location TBD. |
| Final geotechnical report | Required for foundation design closure; report itself is TBD/not present in accessible deliverable-local sources. |

## Verification

- Confirm all identification fields match `_CONTEXT.md`, Gate 7 registers, and workbook row 3.
- Confirm the interface matrix includes only workbook-supported `X` facts for row 3.
- Confirm civil/foundation/drainage statements are traceable to DBM SEC-11 and do not exceed the cited language.
- Confirm all unsupported values are marked `TBD`.
- Confirm no requirements are derived from inaccessible or absent source slices.
- Confirm terminology is consistent across `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`.

## Documentation

The completed package datasheet package should retain or reference:

- Package technical datasheet.
- Vendor or discipline engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- `TBD` register or issue list for missing geotechnical, quantity, boundary, drawing, and construction-detail inputs.
