# Procedure: DEL-004-03 Construction Work Package

## Purpose

Define the bounded procedure for producing and using the PKG-004 Site Grading construction work package during Phase 2.2 setup. This procedure supports a construction-facing CWP that identifies the package boundary, declared interfaces, source-grounded construction constraints, open maturity items, and turnover evidence.

## Prerequisites

| Prerequisite | Status |
|---|---|
| Accepted Gate 7 PROJECT_DECOMP snapshot | Available: 2026-05-24 final published snapshot. |
| Deliverable-local context files | Available: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`. |
| Declared upstream dependencies | None declared during PREPARATION. |
| Package/decomposition rows | Available for DEL-004-03, PKG-004, SOW-0004, and declared interfaces. |
| DBM civil/construction source slices | Available in `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`. |
| Issued civil drawings / grading model / survey control | TBD - not available in current source set. |
| Final hydrology inputs | TBD - current rainfall basis uses NBCC 2020 Dawson Creek IDF proxy pending site-specific update. |
| Final geotechnical report | TBD - required before foundation design closure. |

## Steps

1. Confirm package identity.
   - Verify CWP header uses DEL-004-03, PKG-004, Site Grading, WBS 02, Civil, EPC Integrator, SOW-0004, and Workbook Packages row 5.

2. Establish CWP artifact structure.
   - Include sections or attachments for the construction work package, installation and tie-in workface plan, and construction interface and turnover checklist.

3. Build the interface checklist.
   - Add `Drain / Containment` from INTERFACE_REGISTER.csv row IFC-FA26BF6895.
   - Add `Grading / Site Drainage / Spill Containment` from INTERFACE_REGISTER.csv row IFC-D2D12F4CA2.
   - Mark tie-in owner, current construction status, drawing reference, inspection status, and turnover evidence as TBD where not available.

4. Add civil and drainage constraints.
   - Carry DBM SEC-11 requirements for grading, drainage, roads, surface-water management, retention pond, foundations/supports interfaces, truck-loading slabs, building foundations, fencing, and security where affected by Site Grading.
   - Include the requirement to prevent uncontrolled offsite discharge and protect process areas.
   - Include the requirement to route process-contaminated drainage to the appropriate drain or containment system rather than surface-water discharge.

5. Add access and construction-support constraints.
   - Carry DBM SEC-11 Roads and Access requirements for construction, module delivery, operations, maintenance, emergency response, truck-loading traffic, and winter operation where affected by grading.

6. Add maturity/open-item controls.
   - Record final hydrology inputs as required before drainage and surface-water management closure.
   - Record final geotechnical report as required before foundation-related grading/foundation closure.
   - Record IFC drawings, grading limits, quantities, elevations, and inspection/turnover criteria as TBD unless accepted source files are supplied.

7. Cross-check against sibling CWP documents.
   - Confirm Datasheet conditions match Specification requirements.
   - Confirm Specification verification hooks appear in this Procedure.
   - Confirm Guidance conflict item HRR-004-03-001 remains visible until ruled.

## Verification

| Check | Pass criterion |
|---|---|
| Identity check | DEL-004-03, PKG-004, WBS 02, Civil, SOW-0004, and Workbook row 5 appear consistently. |
| Artifact check | CWP, workface plan, and interface/turnover checklist are present or explicitly listed as required attachments. |
| Interface check | Drain / Containment and Grading / Site Drainage / Spill Containment are both listed. |
| Drainage check | Offsite discharge prevention, process area protection, and contaminated-drainage segregation are included. |
| Access check | Construction, module delivery, operations, maintenance, emergency response, truck-loading, and winter access considerations are included where affected by grading. |
| Maturity check | Hydrology proxy status, preliminary geotechnical status, and missing IFC construction details are marked TBD/open. |
| Source check | Non-trivial requirements cite Gate 7 registers or DBM SEC-02/SEC-11. |

## Records

Maintain the following records with the construction work package:

- Construction work package document.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Source traceability table to DELIVERABLE_REGISTER.csv, PACKAGE_REGISTER.csv, SCOPE_LEDGER.csv, INTERFACE_REGISTER.csv, ARTIFACT_REGISTER.csv, and DBM SEC-02/SEC-11.
- Open-items register for final hydrology, final geotechnical report, civil drawings/model, workface limits, construction quantities, elevations, and inspection/turnover criteria.
- Human ruling record for HRR-004-03-001 objective-mapping discrepancy.
