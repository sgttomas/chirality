# Procedure: DEL-002-03 Construction Work Package

## Purpose

Define the current procedure for producing and checking the `PKG-002 - Earthworks for foundations` construction work package from the accepted Gate 7 basis and locally accessible source materials.

This procedure is for deliverable production and controlled use of the initial CWP draft. It is not a field execution method statement.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local truth set: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_SEMANTIC.md`.
- Workbook `Packages` sheet row 3 or Gate 7 registers derived from it.
- `PACKAGE_REGISTER.csv`, row `PKG-002`.
- `DELIVERABLE_REGISTER.csv`, row `DEL-002-03_construction-work-package`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-002-03_construction-work-package`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-002`.
- `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` civil and construction slices.
- Declared upstream dependencies: none declared during PREPARATION.
- Required but not currently available for closure: final geotechnical report, IFC civil/foundation drawings, detailed construction specifications, construction schedule, and ITP/turnover signoff matrix.

## Steps

1. Confirm deliverable identity.
   - Verify deliverable ID `DEL-002-03_construction-work-package`, parent package `PKG-002`, package name `Earthworks for foundations`, WBS `02`, discipline `Civil`, and responsible party `EPC Integrator`.
   - Sources: `_CONTEXT.md`; `PACKAGE_REGISTER.csv`; `DELIVERABLE_REGISTER.csv`.

2. Confirm package source basis.
   - Use workbook row 3 and `PACKAGE_REGISTER.csv` row `PKG-002` for package identity, discipline, WBS, responsibility model, and interface types.
   - Do not import facts from similarly named `PKG-001`; it is a separate workbook row and WBS.

3. Establish CWP artifact set.
   - Include construction work package, installation and tie-in workface plan, and construction interface and turnover checklist.
   - Sources: `_CONTEXT.md`; `ARTIFACT_REGISTER.csv`, rows `ART-7FC7329C6F`, `ART-2461156C48`, `ART-6716AE2168`.

4. Build the interface checklist.
   - Include Grading / Site Drainage / Spill Containment.
   - Include Structural / Foundations / Supports.
   - Mark tie-in locations, routing, and signoff owners as `TBD` unless supported by IFC drawings or other accepted source material.

5. Build the workface plan outline.
   - Address construction management, grading, piling, foundations, roads, field buildings, module offloading/setting, hookups, pipe supports, interconnecting piping, cabling/terminations, lighting, fencing, security systems, utilities, and demolition/removal only where they interface with the PKG-002 earthworks-for-foundations scope.
   - Source: `3-25_Comp_and_Liquids_DBM.md`, Construction Scope Summary.
   - Mark specific sequence, crew plan, equipment plan, and quantities as `TBD`.

6. Carry civil constraints into the CWP.
   - Include grading, drainage, surface-water management, foundations/supports, access, and maintenance-access considerations.
   - Preserve final geotechnical report dependency before foundation design closure.
   - Sources: `3-25_Comp_and_Liquids_DBM.md`, Site and Civil Conditions; Surface Water and Drainage; Roads and Access; Foundations and Structural Supports.

7. Check drainage and containment treatment.
   - Confirm process-contaminated drainage is not routed to uncontrolled surface-water discharge where applicable.
   - Mark actual drainage tie-ins and containment details as `TBD` until civil/drainage drawings are available.

8. Prepare open-item list.
   - At minimum include final geotechnical report, IFC drawings, earthworks quantities, excavation/backfill/compaction criteria, foundation-specific acceptance criteria, ITP hold/witness points, workface sequencing, and turnover signoff matrix.

9. Perform cross-document consistency check.
   - Confirm Datasheet attributes are reflected in Specification requirements.
   - Confirm Specification requirements have Procedure verification hooks.
   - Confirm Guidance does not overstate source support.
   - Resolve inconsistencies from the local source set or leave them as `TBD`.

10. Issue readiness check.
   - Before IFC issue, align the CWP to the plot plan, equipment list, and construction work package register.
   - Source: `3-25_Comp_and_Liquids_DBM.md`, miscellaneous facilities note.

## Verification

| Check | Expected result |
|---|---|
| Identity check | Deliverable and package metadata match local context and Gate 7 registers. |
| Source check | All non-trivial requirements cite Gate 7 registers, workbook row 3, or the 03-25 DBM source slices. |
| Interface check | The two PKG-002 interface types are included and no unconfirmed interface type is added as fact. |
| Open-item check | Unsupported field construction details are marked `TBD`. |
| Geotechnical check | Foundation closure remains blocked pending final geotechnical report. |
| Cross-document check | Terminology and values are consistent across Datasheet, Specification, Guidance, and Procedure. |

## Records

- Completed Construction Work Package.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Source traceability list.
- Open-item list for `TBD` execution details.
- Review record confirming alignment to plot plan, equipment list, and construction work package register before IFC issue.
