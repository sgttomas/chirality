# Procedure: DEL-045-03 Construction Work Package

## Purpose

Define the current procedure for producing and checking the `PKG-045 - Instrumentation (outside of Mechanical Packages only)` construction work package from the accepted Gate 7 basis and locally accessible source materials.

This procedure is for deliverable production and controlled use of the initial CWP draft. It is not a field execution method statement.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local truth set: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_SEMANTIC.md`.
- Workbook `Packages` sheet row 47 or Gate 7 registers derived from it.
- `PACKAGE_REGISTER.csv`, row `PKG-045`.
- `DELIVERABLE_REGISTER.csv`, row `DEL-045-03_construction-work-package`.
- `ARTIFACT_REGISTER.csv`, rows `ART-F6FBF7A832`, `ART-2D467E7301`, `ART-618CCB3675`.
- `INTERFACE_REGISTER.csv`, rows 307-311 (PKG-045 interfaces).
- `SCOPE_LEDGER.csv`, row `SOW-0046`.
- Declared upstream dependencies: none declared during PREPARATION.
- Required but not currently available for closure: upstream `DEL-045-01_scope-of-work` and `DEL-045-02_package-datasheet` tagged-equipment and interface data; IFC instrumentation drawings, loop sheets, cable schedules, instrument data sheets, hazardous-area classification basis, and ITP/turnover signoff matrix.

## Steps

1. Confirm deliverable identity.
   - Verify deliverable ID `DEL-045-03_construction-work-package`, parent package `PKG-045`, package name `Instrumentation (outside of Mechanical Packages only)`, WBS `03`, discipline `Instrumentation`, and responsible party `EPC Integrator`.
   - Sources: `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 47; `DELIVERABLE_REGISTER.csv` row 250.

2. Confirm package source basis.
   - Use workbook row 47 and `PACKAGE_REGISTER.csv` row `PKG-045` for package identity, discipline, WBS, responsibility model, and interface types.
   - Do not import facts from similarly named PKG-043 or PKG-044 (WBS 01 and 02 instrumentation rows); they are separate workbook rows.

3. Establish CWP artifact set.
   - Include construction work package, installation and tie-in workface plan, and construction interface and turnover checklist.
   - Sources: `_CONTEXT.md`; `ARTIFACT_REGISTER.csv`, rows `ART-F6FBF7A832`, `ART-2D467E7301`, `ART-618CCB3675`.

4. Build the interface checklist.
   - Include Process Piping (`IFC-33F8A9F366`).
   - Include Utility Piping (`IFC-AE76B11E50`).
   - Include Electrical Power (`IFC-2D030CA850`).
   - Include I&C / Control Cabling (`IFC-210F46B073`).
   - Include Communications / Network (`IFC-9DAC4D3C4D`).
   - Apply Gate 6 disposition: field supports, power, and communications in package scope per plug-n-play philosophy.
   - Mark tie-in locations, routing, and signoff owners as `TBD` unless supported by IFC drawings or other accepted source material.

5. Build the workface plan outline.
   - Address instrument mounting and field supports, instrument loop power distribution, signal cable routing and termination, control system (I&C) terminations, communications network segments, and tie-ins to process and utility piping (tap points, sample lines, analytical hookups) only where they interface with PKG-045 scope.
   - Mark specific sequence, crew plan, equipment plan, and quantities as `TBD`.

6. Carry upstream handoff dependencies.
   - Note that tagged instrument lists, loop counts, panel/cabinet quantities, instrument data sheets, and vendor handoff acceptance criteria are owned by `DEL-045-01_scope-of-work` and `DEL-045-02_package-datasheet`.
   - Do not synthesize this content in the CWP.

7. Check scope boundary against mechanical packages.
   - Confirm the CWP scope does not pull in instrumentation already embedded in adjacent mechanical packages.
   - Mark scope-boundary conflicts as `TBD` for human ruling if upstream deliverables suggest overlap.

8. Prepare open-item list.
   - At minimum include: tagged instrument list closure, IFC instrumentation drawings (loop sheets, P&IDs, layout), cable schedules, hazardous-area classification, instrument environmental ratings, ITP hold/witness points, workface sequencing, and turnover signoff matrix.

9. Perform cross-document consistency check.
   - Confirm Datasheet attributes are reflected in Specification requirements.
   - Confirm Specification requirements have Procedure verification hooks.
   - Confirm Guidance does not overstate source support.
   - Resolve inconsistencies from the local source set or leave them as `TBD`.

10. Issue readiness check.
   - Before IFC issue, align the CWP to the upstream `DEL-045-01` scope of work, `DEL-045-02` package datasheet, plot plan / equipment list, and the construction work package register.

## Verification

| Check | Expected result |
|---|---|
| Identity check | Deliverable and package metadata match local context and Gate 7 registers. |
| Source check | All non-trivial requirements cite Gate 7 registers, workbook row 47, or the cited DBM source (with `location TBD` when slice not extracted). |
| Interface check | All five PKG-045 interface types are included; no unconfirmed interface type is added as fact. |
| Plug-n-play disposition check | Field supports, power, and communications inclusion matches Gate 6 disposition wording. |
| Open-item check | Unsupported field construction details are marked `TBD`. |
| Upstream handoff check | Tagged instrument list and vendor handoff acceptance remain open pending `DEL-045-01` / `DEL-045-02`. |
| Cross-document check | Terminology and values are consistent across Datasheet, Specification, Guidance, and Procedure. |

## Records

- Completed Construction Work Package.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Source traceability list (Gate 7 registers, workbook row 47, DBM citation).
- Open-item list for `TBD` execution details.
- Review record confirming alignment to upstream `DEL-045-01` / `DEL-045-02`, plot plan, equipment list, and construction work package register before IFC issue.
