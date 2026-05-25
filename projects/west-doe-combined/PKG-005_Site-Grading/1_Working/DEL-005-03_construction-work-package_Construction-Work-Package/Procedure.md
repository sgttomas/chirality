# Procedure: DEL-005-03 Construction Work Package

## Purpose

Define the bounded procedure for producing and using the Site Grading Construction Work Package for `PKG-005` from the accepted Gate 7 decomposition basis and accessible 3-25 DBM civil source slices.

## Prerequisites

- Gate 7 PROJECT_DECOMP snapshot is the accepted upstream decomposition truth.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md` are available.
- Current status permits writing; current state was `OPEN` at initialization.
- Declared upstream dependencies: none.
- DBM-Comp_and_Liquids SEC-02 and SEC-11 are available as source basis.
- Before construction release, obtain or confirm:
  - civil IFC drawing list and plot plan references;
  - final geotechnical report;
  - hydrology update or confirmation of DBM rainfall basis;
  - permit and environmental construction constraints;
  - project construction QA/inspection forms.

## Steps

1. Confirm package identity.
   - Verify `PKG-005`, workbook row 6, WBS 03, CoA tracking number `26020-01-42-003`, and deliverable ID `DEL-005-03_construction-work-package`.

2. Establish the construction scope boundary.
   - Include workbook-defined Site Grading scope and civil interface types.
   - Keep exclusions as `TBD` unless accepted source material defines them.

3. Build the workface plan.
   - Address grading, drainage, roads/access, surface-water management, retention pond, supports/foundations, truck-loading slabs, building foundations, fencing, and security where applicable.
   - Mark specific dimensions, quantities, sequences, and work packs as `TBD` until civil IFC sources are available.

4. Build the interface checklist.
   - Include Drain / Containment.
   - Include Grading / Site Drainage / Spill Containment.
   - Add signoff placeholders for construction, civil design, environmental/regulatory, operations, and turnover owners as applicable.

5. Insert source-based hold points.
   - Final geotechnical report before foundation design closure.
   - Hydrology update or confirmation before final retention pond and drainage sizing.
   - Civil drawings and plot plan before final issue for construction.
   - Permit and waste-management requirements before construction start where applicable.

6. Define inspection and turnover evidence.
   - Include construction inspection records for grading, drainage, access, and containment work.
   - Include redline/as-built capture if project procedures require it.
   - Include punch/open-item register and final interface signoff checklist.

7. Perform internal consistency review.
   - Confirm Datasheet attributes appear in Specification requirements where applicable.
   - Confirm Specification requirements have Procedure verification hooks.
   - Confirm all unresolved source gaps remain `TBD` or in the Human Ruling Required table.

## Verification

| Check | Acceptance basis |
|---|---|
| Identity check | Matches Gate 7 deliverable and package registers. |
| Source check | Requirements trace to Gate 7 registers or DBM-Comp_and_Liquids SEC-02/SEC-11/standards sections. |
| Interface check | Known interface types appear in the CWP checklist. |
| Hold-point check | Geotechnical, hydrology, drawing, and permit gaps are not silently closed. |
| Turnover check | Construction interface and turnover checklist is present or explicitly marked `TBD` for detailed project form. |

## Records

- Construction work package.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Inspection records: TBD by project construction QA plan.
- Geotechnical report acceptance record: TBD.
- Civil IFC drawing and plot plan references: TBD.
- Hydrology and permit confirmation records: TBD.
