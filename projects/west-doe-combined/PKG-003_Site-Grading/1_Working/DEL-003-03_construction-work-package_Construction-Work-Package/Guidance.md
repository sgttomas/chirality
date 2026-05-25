# Guidance: DEL-003-03_construction-work-package

## Purpose

The Construction Work Package exists to convert the accepted `PKG-003` Site Grading scope into a construction-ready, inspection-ready, and turnover-ready work package. It should preserve the Gate 7 package identity and the source-supported civil/drainage basis while making unresolved design inputs visible before field execution or turnover closure.

## Principles

- Treat Gate 7 as the accepted decomposition truth for deliverable identity, package membership, scope item, anticipated artifacts, and objective mapping.
- Treat the workbook row as the package identity and interface source for WBS 01 Site Grading, including Drain / Containment and Grading / Site Drainage / Spill Containment.
- Treat DBM civil sections as the current source basis for grading, drainage, surface-water management, roads, foundations, geotechnical inputs, topographical inputs, and open design-development items.
- Do not convert preliminary DBM assumptions into closed construction criteria. Where the DBM says the geotechnical report, topographical survey, plot plan, or detailed drainage design remains pending, keep that item open in the CWP until accepted project inputs close it.
- Use field execution controls to protect drainage and containment intent: survey verification, inspection hold points, redlines, open-item tracking, and turnover checklist completion.

## Considerations

| Topic | Guidance |
|---|---|
| Site grading and drainage | The workface plan should show how installed grades will prevent offsite overflow entering the facility and direct/contain onsite overflow into the retention pond. |
| Interface management | Drain / Containment and Grading / Site Drainage / Spill Containment are not separate deliverables here; they are construction interface facts to be carried into planning, inspection, and turnover. |
| Open inputs | Geotechnical parameters, topographical data, grade-surface file contents, final IDF duration, detailed drainage design, and retention pond location/capacity are source-identified open inputs. |
| Surface-water and contaminated drainage | Surface-water management should prevent uncontrolled offsite discharge and protect process areas. Process-contaminated drainage should not be treated as ordinary surface-water discharge. |
| Construction readiness | A CWP can be drafted before all inputs are closed, but construction release should identify which open inputs are blockers, constraints, or turnover exceptions. |
| Turnover | Turnover should demonstrate that installed grading/drainage works match accepted drawings or that deviations are captured through approved field changes and open-item controls. |

## Trade-offs

| Trade-off | Treatment |
|---|---|
| Early work packaging vs. final design closure | Early packaging can support planning, but release to field execution should not hide TBD geotechnical, survey, plot-plan, or drainage-design inputs. |
| Preliminary slopes vs. constructability | DBM slope values provide a current basis; detailed engineering and geotechnical requirements may supersede them when accepted. |
| Surface-water discharge vs. process-contaminated drainage | Keep the distinction explicit. Uncontaminated surface water and process-contaminated drainage require different routing and acceptance evidence. |
| Local field adjustment vs. engineered grading intent | Minor field adjustments should be controlled by redline/as-built and approval processes when they affect drainage, containment, access, or interfaces. |

## Examples

| Example | Use |
|---|---|
| A field survey check confirms ditch slopes meet the accepted IFC drawing and the DBM minimum of 0.2%. | Accept as field verification evidence if the governing drawing has not been superseded. |
| The geotechnical report changes allowable grade slopes or pavement layer requirements. | Update CWP prerequisites, inspection criteria, and open items before releasing affected work. |
| A drain/containment interface is present in the workbook but no tie-in detail is available in the CWP source set. | Mark the tie-in detail as `TBD` and carry it into the construction interface checklist. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CWP-001 | The deliverable context lists `OBJ-010`, while `PACKAGE_REGISTER.csv` and `SCOPE_LEDGER.csv` list package/scope objectives only through `OBJ-009`; `OBJECTIVE_DELIVERABLE_MAP.csv` explicitly maps `OBJ-010` to this construction work package. | `_CONTEXT.md` Supports Objectives; `OBJECTIVE_DELIVERABLE_MAP.csv` row for `DEL-003-03` / `OBJ-010` | `PACKAGE_REGISTER.csv` `SupportsObjectives`; `SCOPE_LEDGER.csv` `ObjectiveID(s)` | Datasheet Identification; Specification Scope; Procedure Records | Treat `OBJ-010` as applicable to this deliverable because the deliverable-level map explicitly lists it, while noting package-level objective rows stop at `OBJ-009`. | TBD |
