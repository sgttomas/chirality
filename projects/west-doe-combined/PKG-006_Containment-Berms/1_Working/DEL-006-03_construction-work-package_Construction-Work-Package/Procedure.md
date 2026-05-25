# Procedure: Construction Work Package

## Purpose

Define the controlled steps to produce and use the Construction Work Package for `PKG-006` Containment Berms. The procedure supports construction planning, field execution readiness, inspection, interface signoff, turnover, and unresolved-item tracking.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Declared upstream dependencies: none declared during PREPARATION.
- Gate 7 rows for `DEL-006-03_construction-work-package` and `PKG-006` are available.
- DBM source slices for construction scope, site-specific data, civil/drainage requirements, and standards/regulatory status are available.
- IFC civil drawings, final hydrology inputs, final geotechnical report, project civil specifications, and detailed environmental/regulatory permit triggers are either accepted or explicitly carried as `TBD`.

## Steps

1. Confirm package identity.
   - Verify `PKG-006` Containment Berms, WBS 03, CoA tracking number `26020-03-42-006`, discipline Civil, and workbook row 7.
   - Record the package basis in the CWP cover/index.

2. Confirm deliverable scope.
   - Include the construction work package, installation and tie-in workface plan, and construction interface and turnover checklist.
   - Keep exclusions and unknown detailed criteria visible as `TBD`.

3. Build the interface checklist.
   - Add Drain / Containment.
   - Add Grading / Site Drainage / Spill Containment.
   - Add signoff fields for engineering, construction, environmental/regulatory, and turnover review where applicable.

4. Establish drainage and containment controls.
   - Confirm that surface-water management protects process areas and construction/operations access.
   - Confirm that process-contaminated drainage is routed to the proper drain or containment system rather than surface-water discharge.
   - Mark routing details `TBD` where drawings or specifications are unavailable.

5. Establish readiness gates for incomplete source criteria.
   - Hydrology: require final hydrology input or accepted exception before closing drainage and retention-related criteria.
   - Geotechnical: require final geotechnical report before closing foundation, site preparation, frost protection, settlement, or structural support criteria.
   - Standards/regulatory: require verification of unavailable standards, permits, water-regulatory triggers, and waste-management requirements before final issue for construction.

6. Prepare workface execution controls.
   - Identify work areas, access, sequencing, tie-in boundaries, inspection hold points, and turnover records.
   - ASSUMPTION: Include construction logistics only where they affect Containment Berms or their declared interfaces.

7. Perform pre-issue consistency review.
   - Check the CWP against the package datasheet, civil drawings/specifications when available, interface register, plot plan, and equipment/layout references.
   - Keep unresolved conflicts in the CWP exception register.

8. Execute field work and inspections.
   - Use approved IFC drawings/specifications and the CWP workface plan.
   - Record inspection results, exceptions, redlines, and interface signoffs.

9. Complete turnover.
   - Confirm all checklist items are signed off or carried as accepted exceptions.
   - Compile construction records, inspection records, interface records, and unresolved/open-item dispositions.

## Verification

| Verification check | Evidence |
|---|---|
| Package identity is correct | CWP cover/index matches `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`. |
| Required artifacts are present | CWP includes work package, workface plan, and interface/turnover checklist. |
| Interfaces are covered | Checklist includes Drain / Containment and Grading / Site Drainage / Spill Containment. |
| Drainage routing is controlled | Field package and inspection records show process-contaminated drainage is not routed to surface-water discharge unless separately approved. |
| Hydrology/geotechnical uncertainty is controlled | Final inputs are accepted or unresolved criteria remain `TBD`/exceptioned. |
| Standards/regulatory verification is controlled | Standards and regulatory requirements not available in the workspace remain verification-required. |
| Turnover is complete | Inspection, interface signoff, exception, and turnover records are complete. |

## Records

- Construction Work Package index and issue record.
- Installation and tie-in workface plan.
- Drain / Containment interface checklist.
- Grading / Site Drainage / Spill Containment checklist.
- Inspection and hold-point records.
- Hydrology/geotechnical/standards/regulatory `TBD` and exception register.
- Turnover checklist and signoff record.
- As-built/redline records where required by project controls.
