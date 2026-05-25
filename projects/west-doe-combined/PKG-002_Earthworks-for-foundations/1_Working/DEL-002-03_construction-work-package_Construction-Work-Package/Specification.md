# Specification: DEL-002-03 Construction Work Package

## Scope

This specification governs the initial construction work package document set for `PKG-002 - Earthworks for foundations`, WBS `02`, discipline Civil.

The construction work package shall describe the physical installation, construction, tie-in, inspection, and turnover basis for the earthworks-for-foundations package, including the workface plan and construction interface/turnover checklist. Source: `DELIVERABLE_REGISTER.csv`, row `DEL-002-03_construction-work-package`; `ARTIFACT_REGISTER.csv`, rows for this deliverable.

Exclusions:

- Detailed earthworks quantities, excavation limits, compaction values, material specifications, and construction tolerances are `TBD` because they are not present in the accessible source slices.
- Final foundation design criteria are not closed until the final geotechnical report and detailed civil/foundation design are available. Source: `3-25_Comp_and_Liquids_DBM.md`, Site and Civil Conditions.
- Package-specific construction schedule, crew plan, and means/methods are `TBD`.

## Requirements

| ID | Requirement | Source / status | Verification |
|---|---|---|---|
| CWP-REQ-001 | The CWP shall identify the package as `PKG-002 - Earthworks for foundations`, WBS `02`, discipline Civil, tied to workbook row 3. | `PACKAGE_REGISTER.csv`, row `PKG-002`; workbook row 3. | Datasheet and cover metadata review. |
| CWP-REQ-002 | The CWP shall include or reference the three required artifact outputs: construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. | `_CONTEXT.md`; `ARTIFACT_REGISTER.csv`, rows `ART-7FC7329C6F`, `ART-2461156C48`, `ART-6716AE2168`. | Deliverable package completeness check. |
| CWP-REQ-003 | The CWP shall address the source-confirmed interfaces: Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports. | Workbook row 3; `INTERFACE_REGISTER.csv`, rows `IFC-E58D0EFA8E`, `IFC-0B377574CA`. | Interface checklist review. |
| CWP-REQ-004 | The CWP shall carry civil work planning for grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security where those scopes interface with this earthworks-for-foundations package. | `3-25_Comp_and_Liquids_DBM.md`, Site and Civil Conditions. | Scope inclusion review against the workface plan. |
| CWP-REQ-005 | The CWP shall not close foundation design or construction acceptance criteria until the final geotechnical report is available and accepted. | `3-25_Comp_and_Liquids_DBM.md`, Site and Civil Conditions; Foundations and Structural Supports. | Open-item review; geotechnical basis confirmation. |
| CWP-REQ-006 | The CWP shall account for the site ambient basis of -40 deg C to +35 deg C and the construction/access implications of the -40 deg C minimum ambient where applicable to roads, drainage, foundations, and module layout. | `3-25_Comp_and_Liquids_DBM.md`, Site and Civil Conditions; Design Implications. | Constructability review and winterization/access check. |
| CWP-REQ-007 | The CWP shall route process-contaminated drainage to the appropriate drain or containment system rather than surface-water discharge where construction interfaces affect drainage paths. | `3-25_Comp_and_Liquids_DBM.md`, Surface Water and Drainage. | Drainage/interface review. |
| CWP-REQ-008 | Before issue for construction, the CWP shall be aligned to the plot plan, equipment list, and construction work package register. | `3-25_Comp_and_Liquids_DBM.md`, miscellaneous facilities note. | IFC readiness check. |
| CWP-REQ-009 | ASSUMPTION: The EPC Integrator shall coordinate discipline subcontractor inputs because the package responsibility model is source-dependent and no vendor-package ownership model is inferred. | `PACKAGE_REGISTER.csv`, row `PKG-002`. | Responsibility assignment review. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Accepted Gate 7 PROJECT_DECOMP snapshot | Authoritative decomposition truth for package, deliverable, objective, artifact, and interface identity. | Available locally. |
| 03-25 Comp and Liquids DBM | Authoritative local civil/construction basis for the 03-25 facility scope used by this package. | Available locally. |
| Workbook `Packages` sheet row 3 | Authoritative package row and interface flags. | Available locally. |
| Final geotechnical report | Required before foundation design closure. | TBD - not locally available. |
| Detailed civil/foundation specifications and IFC drawings | Required to close execution criteria, quantities, tolerances, inspection hold points, and construction sequencing. | TBD - not locally available. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity and traceability | Compare CWP metadata to `_CONTEXT.md`, `PACKAGE_REGISTER.csv`, and `DELIVERABLE_REGISTER.csv`. | All IDs, names, WBS, and source refs match. |
| Interface coverage | Check workface plan and checklist against `INTERFACE_REGISTER.csv` for PKG-002. | Both source-confirmed interface types are covered or marked `TBD` with rationale. |
| Civil/construction scope coverage | Compare CWP scope to 03-25 DBM Site and Civil Conditions and Construction Scope Summary. | Relevant civil/construction scope is included without adding unsupported package-specific detail. |
| Geotechnical/open-item control | Review CWP for foundation criteria and acceptance criteria. | Final geotechnical-dependent values remain `TBD` until source-supported. |
| Turnover readiness | Confirm a construction interface and turnover checklist exists. | Checklist identifies required records and open `TBD` signoffs. |

## Documentation

The CWP package shall include, at minimum:

- Construction work package.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Source and traceability register for Gate 7 snapshot, workbook row 3, PKG-002 registers, and 03-25 DBM civil/construction slices.
- Open-item list for final geotechnical report, IFC civil/foundation drawings, construction quantities, ITP/hold points, and turnover signoff matrix.
