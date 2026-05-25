# Specification: DEL-002-01_scope-of-work — Scope of Work

## Scope

This specification defines the minimum content requirements for the EPC Integrator's Scope of Work deliverable for PKG-002, Earthworks for foundations. The deliverable shall cover the full package scope for SOW-0002 and shall include:

- package scope of work;
- tagged equipment and package identity list;
- package function and whole-facility integration narrative;
- responsibility assignment record.

Source: Gate 7 `DELIVERABLE_REGISTER.csv` and `ARTIFACT_REGISTER.csv` rows for `DEL-002-01_scope-of-work`.

The scope-of-work document shall identify the package as a Civil package under WBS 02 with CoA tracking number 26020-01-42-001 and applicable interface types Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports. Source: Gate 7 `PACKAGE_REGISTER.csv`; `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet, Excel row 3.

Exclusions:

- Detailed engineering calculations, issued-for-construction drawings, installation work packaging, and turnover checklists are TBD unless explicitly assigned to this scope-of-work deliverable by a later human ruling.
- Package-specific exclusions are TBD because no package-specific exclusions are stated in the accessible source materials.

## Requirements

| ID | Requirement | Source / authority | Verification |
|---|---|---|---|
| SOW-REQ-001 | The Scope of Work shall identify DEL-002-01, PKG-002, package name, WBS, CoA tracking number, discipline, responsible party, scope item, supported objectives, and workbook source row. | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`; Gate 7 `PACKAGE_REGISTER.csv`; workbook Packages sheet row 3 | Document completeness check |
| SOW-REQ-002 | The Scope of Work shall include the four anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | `_CONTEXT.md`; Gate 7 `ARTIFACT_REGISTER.csv` rows for DEL-002-01 | Artifact-to-section trace check |
| SOW-REQ-003 | The package scope shall carry the two recorded physical interface types: Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports. | Workbook Packages sheet row 3; Gate 7 `PACKAGE_REGISTER.csv` | Interface list check |
| SOW-REQ-004 | The Scope of Work shall state that the final geotechnical report is required before foundation design closure. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Site and Civil Conditions | Source citation and open-item check |
| SOW-REQ-005 | The Scope of Work shall not present preliminary geotechnical values as closed construction criteria. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-02 Geotechnical and Seismic Basis | Review of assumptions/TBD register |
| SOW-REQ-006 | The Scope of Work shall include civil design coverage for grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Site and Civil Conditions | Scope coverage check |
| SOW-REQ-007 | The Scope of Work shall require surface-water management provisions to prevent uncontrolled offsite discharge, protect process areas, support access, and route process-contaminated drainage to appropriate drain or containment systems. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Surface Water and Drainage | Civil/surface-water narrative review |
| SOW-REQ-008 | The Scope of Work shall require foundations to be designed for final geotechnical report, equipment loads, snow/wind/seismic criteria, frost protection, vibration, settlement, and maintenance access. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 Foundations and Structural Supports | Foundation basis checklist |
| SOW-REQ-009 | The responsibility assignment shall state EPC Integrator responsibility for this deliverable and preserve package execution responsibility as source-dependent where the source does not close EPC Integrator versus discipline subcontractor ownership. | `_CONTEXT.md`; Gate 7 `PACKAGE_REGISTER.csv`; Gate 7 `ARTIFACT_REGISTER.csv` | Responsibility table review |

## Standards

| Standard / reference | Applicability | Status |
|---|---|---|
| NBCC | Civil/structural governing content listed for civil/structural basis | Source-listed; clause-level requirements TBD |
| Geotechnical report | Required for foundation design closure and detailed civil design parameters | Not locally available; values remain TBD/TBC |
| Site data | Governs civil design pending final geotechnical confirmation | Available through DBM source slice |
| Civil drawings | Required for layout/plot plan and civil verification | Not locally available; location TBD |
| Surface-water management | Governing civil/environmental design content | Available through DBM source slice; detailed hydrology TBD |

Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 table listing Civil/structural governing content.

## Verification

The completed Scope of Work shall be verified by the following checks:

| Check | Acceptance basis |
|---|---|
| Identity completeness | All Identification fields from `Datasheet.md` are present in the Scope of Work. |
| Artifact completeness | Each anticipated artifact from `_CONTEXT.md` and Gate 7 `ARTIFACT_REGISTER.csv` has a corresponding section or appendix. |
| Source traceability | Non-trivial values and requirements cite Gate 7 registers, workbook row 3, or DBM source slices. |
| Open-item discipline | Geotechnical report, civil drawings, final hydrology, package-specific exclusions, and detailed construction criteria remain `TBD` where source materials are not available. |
| Interface coverage | Both package interface types recorded in workbook row 3 are included. |
| Cross-document consistency | Terminology and values match `Datasheet.md`, `Guidance.md`, and `Procedure.md`. |

## Documentation

The Scope of Work shall produce or include:

- package scope of work;
- tagged equipment and package identity list, including workbook ID, WBS, CoA tracking number, package name, discipline, and recorded interface types;
- package function and whole-facility integration narrative for civil earthworks/foundation support and facility integration;
- responsibility assignment record showing EPC Integrator deliverable ownership and source-dependent execution responsibility;
- TBD/open-item register for unavailable source items, including final geotechnical report, civil drawings, hydrology inputs, detailed foundation criteria, and package-specific exclusions.
