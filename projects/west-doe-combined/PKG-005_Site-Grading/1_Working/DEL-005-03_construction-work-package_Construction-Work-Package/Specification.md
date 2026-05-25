# Specification: DEL-005-03 Construction Work Package

## Scope

This specification governs the Site Grading Construction Work Package for `PKG-005`. The package is a Civil EPC Integrator deliverable covering physical installation, construction planning, inspection, turnover, and facility tie-in treatment for workbook-defined Site Grading scope.

Included scope is limited to the accepted Gate 7 package and deliverable basis:

- Carry the workbook-defined Civil package `Site Grading` as a distinct flat project package for WBS 03.
- Address recorded interface types: Drain / Containment and Grading / Site Drainage / Spill Containment.
- Produce the anticipated artifacts: construction work package, installation and tie-in workface plan, and construction interface and turnover checklist.

Exclusions are `TBD`; the Gate 7 package row states that no package-specific exclusions are stated in source materials.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| REQ-001 | The work package shall preserve `PKG-005` as a distinct Site Grading package and shall not merge it with other Site Grading rows or repeated tracking numbers. | SCOPE_LEDGER.csv SOW-0005; PROJECT_DECOMP DEC-001 | Check package ID, workbook row, CoA tracking number, and deliverable references in the issued CWP. |
| REQ-002 | The CWP shall address Drain / Containment and Grading / Site Drainage / Spill Containment interfaces. | PACKAGE_REGISTER.csv PKG-005 | Check the interface checklist includes both interface types or marks omitted details as `TBD`. |
| REQ-003 | Civil construction planning shall cover grading, drainage, roads, surface-water management, retention pond, piling/foundations, supports, truck-loading slabs, building foundations, fencing, and security where applicable to the Site Grading package. | DBM-Comp_and_Liquids, SEC-11 | Check CWP scope sections against civil work coverage list. |
| REQ-004 | Surface-water management shall prevent uncontrolled offsite discharge, protect process areas, support construction and operations access, and route process-contaminated drainage to appropriate drain or containment systems. | DBM-Comp_and_Liquids, SEC-11 | Review drainage and containment plan sections before issue for construction. |
| REQ-005 | Roads and access provisions shall support construction, module delivery, operations, maintenance, emergency response, and truck-loading traffic, with winter operation considered. | DBM-Comp_and_Liquids, SEC-11 | Check access plan, haul routes, and winter-access assumptions. |
| REQ-006 | Foundation, pile, settlement, frost-protection, and support criteria shall remain open until the final geotechnical report is accepted. | DBM-Comp_and_Liquids, SEC-02 and SEC-11 | Confirm final geotechnical report acceptance or retain `TBD` hold point. |
| REQ-007 | The CWP shall identify and retain the current site basis: LSD 03-25-80-15 W6M, elevation 673 m AMSL, and -40 deg C to +35 deg C ambient design range. | DBM-Comp_and_Liquids, SEC-02 | Check site data table in the CWP. |
| REQ-008 | The CWP shall include construction interface and turnover records sufficient to support EPC Integrator handoff. | DELIVERABLE_REGISTER.csv DEL-005-03 | Check turnover checklist, inspection records, and open-item register placeholders. |

## Standards

| Standard or governing content | Status |
|---|---|
| NBCC | Referenced by DBM as civil/structural governing content; clause-level requirements are location TBD. |
| Final geotechnical report | Required before foundation design closure; not available in current deliverable-local sources. |
| Site data | Available through DBM SEC-02. |
| Civil drawings | Referenced by DBM as required for plot plan, spacing, and civil verification; current drawing list is TBD. |
| Surface-water management basis | Available through DBM SEC-11, with hydrology update pending. |
| Environmental/regulatory permits | Waste management permit and BCER consultation/notification details remain TBD in current source set. |

## Verification

Before the Construction Work Package is treated as ready for downstream construction use, verify:

- Package identity and scope match Gate 7 registers.
- Interface checklist includes drain/containment and grading/site drainage/spill containment.
- Site data, precipitation basis, geotechnical placeholders, and winter-operation assumptions are stated.
- Drainage and surface-water measures do not imply uncontrolled offsite discharge.
- Hold points are included for final geotechnical report, civil drawing list, hydrology update, and regulatory/waste management permit details.
- Turnover records capture inspections, redlines/as-builts if applicable, punch items, and interface signoffs.

## Documentation

Required or expected records:

- Construction work package.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Inspection and test records for grading, drainage, access, and containment work: TBD by construction QA plan.
- Civil drawing list and IFC references: TBD.
- Geotechnical report acceptance evidence: TBD.
- Regulatory/environmental permit references affecting construction execution: TBD.
