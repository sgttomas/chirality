# Guidance: EPC / Civil Discipline Production Package

## Purpose

This deliverable turns the accepted PKG-005 Site Grading basis into a civil discipline production package. Its purpose is to preserve source-supported civil, grading, drainage, containment, and closure evidence without inventing detailed discipline requirements that are not present in the accepted source set.

Sources: `DELIVERABLE_REGISTER.csv` row `DEL-005-04_epc-civil-discipline-production-package`; `ARTIFACT_REGISTER.csv` rows `ART-84267B95AF` and `ART-3BB0AFBF4A`.

## Principles

- Treat Gate 7 registers as authoritative for identity, scope routing, artifact names, interface applicability, objective mapping, and source-limit notes.
- Treat workbook row 6 as the package identity and interface source for PKG-005.
- Treat accessible DBM civil sections as the source basis for civil grading, drainage, surface-water, containment, and open-input statements.
- Use `TBD` for the discipline deliverable register and detailed package-specific civil design inputs until source material or human ruling closes them.
- Do not infer a vendor-package ownership model; the accepted package responsibility model remains EPC Integrator or discipline subcontractor responsibility, source-dependent.

## Considerations

| Topic | Guidance |
|---|---|
| Interface handling | Drain / Containment and Grading / Site Drainage / Spill Containment are applicable to PKG-005 and should be visible in the discipline package basis, requirements closure record, and verification checklist. |
| Source limitation | The accepted decomposition explicitly says detailed discipline requirements are not present in the current source set and remain open. Do not convert this into detailed design unless the source set is expanded. |
| Civil criteria | Use source-stated civil criteria, including surface-water control, process-contaminated drainage routing, pipe-rack ridge grading, pad slope, tank-farm perimeter grading, and maximum grade slope. |
| External inputs | Geotechnical report, topographical survey/grade surface file, plot plan, and detailed drainage engineering are needed before final design closure. |
| Objective association | OBJ-002, OBJ-007, OBJ-008, and OBJ-009 are explicit for this deliverable in `OBJECTIVE_DELIVERABLE_MAP.csv`; use them as context, not as substitutes for source requirements. |

## Trade-offs

| Trade-off | Recommended handling |
|---|---|
| Early package completeness vs source fidelity | Prefer a source-limited closure record with TBDs over unsupported design details. |
| Package-level civil production vs facility-wide civil basis | Include only civil/site requirements applicable to Site Grading and its recorded interfaces; avoid importing unrelated package criteria. |
| EPC Integrator vs subcontractor responsibility | Preserve the source-dependent responsibility model until assignment is made. |
| Grading design criteria vs final geotechnical constraints | Carry source-stated grading criteria, but keep final foundation, pavement, and drainage closure tied to geotechnical/topographical/detailed engineering inputs. |

## Examples

| Example | Treatment |
|---|---|
| Workbook row 6 marks Drain / Containment with `X`. | Include it as an applicable interface and require closure evidence. |
| Workbook row 6 marks Grading / Site Drainage / Spill Containment with `X`. | Include it as an applicable interface and require closure evidence. |
| The DBM states process-contaminated drainage must route to appropriate drain or containment instead of surface-water discharge. | Include as a civil production requirement and verification check. |
| The DBM states the final geotechnical report is required before foundation design closure. | Mark foundation-related detailed criteria as TBD/open input, not final design. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-001 | Responsible party is not assigned beyond "TBD; EPC Integrator or discipline subcontractor as assigned." | `_CONTEXT.md` Identity; `DELIVERABLE_REGISTER.csv` row DEL-005-04 | `PACKAGE_REGISTER.csv` row PKG-005 responsibility model | Datasheet Identification; Specification REQ-009; Procedure Responsibilities | Keep responsible party TBD and prohibit vendor-package ownership inference until assignment. | TBD |
| HRR-002 | Discipline deliverable register is anticipated but not detailed in accessible sources. | `_CONTEXT.md` Anticipated Artifacts | `ARTIFACT_REGISTER.csv` row ART-3BB0AFBF4A source-limit note | Specification Documentation; Procedure Records | Create placeholder/closure requirement only; defer detailed register contents. | TBD |
