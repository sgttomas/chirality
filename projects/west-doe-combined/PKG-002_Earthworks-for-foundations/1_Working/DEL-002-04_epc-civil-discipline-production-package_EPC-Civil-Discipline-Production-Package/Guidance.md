# Guidance: EPC / Civil Discipline Production Package

## Purpose

Use this guidance to keep the `DEL-002-04` Civil production package conservative and source-grounded. The deliverable exists to carry EPC or discipline-subcontractor Civil production evidence for `PKG-002` Earthworks for foundations, while preserving the fact that detailed non-vendor package requirements remain source-limited for Gate 5 disposition.

Sources: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`; Gate 7 `ARTIFACT_REGISTER.csv`.

## Principles

- Treat Gate 7 as the accepted decomposition truth for package identity, deliverable identity, objectives, artifact expectations, and interface facts.
- Treat the accessible source materials as the basis for technical content: workbook row ID # 2, the package requirements DOCX coordination text, and the DBM Civil/site slices.
- Do not convert generic Civil engineering practice into package-specific requirements unless the accessible sources support it.
- Preserve source status. Values marked `TBD`, `TBC`, placeholder, or open in the source basis should remain visibly open in this production package.
- Keep final foundation design closure dependent on the final geotechnical report.

## Considerations

The package has two explicit workbook interfaces: Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports. These should be enough to frame the package interface matrix, but not enough to invent drawing lists, quantities, material classes, earthwork volumes, foundation types, or construction tolerances.

The DBM provides a broader Civil design coverage list for the 03-25 facility. It supports inclusion of grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security as topics. It does not, by itself, close the detailed criteria for this package.

The DBM also carries site data and geotechnical/seismic placeholders. Use those values only with their source status. For example, soil description is marked TBC and terrain type is TBD, so any foundation production package should treat them as inputs awaiting closure rather than final construction criteria.

## Trade-offs

| Trade-off | Conservative handling |
|---|---|
| Drafting a useful Civil package versus avoiding invented detail | Include source-supported topic coverage and interface facts; mark detailed discipline content `TBD`. |
| Using DBM Civil basis versus treating it as final design | Use DBM sections as current basis only; preserve final geotechnical report and detailed engineering as closure inputs. |
| Carrying package-specific interfaces versus broader facility Civil scope | Use workbook/Gate 7 interfaces for package-specific interface claims; use DBM Civil scope as supporting facility context. |
| Assigning responsibility | Keep responsible party as `TBD; EPC Integrator or discipline subcontractor as assigned` until assignment is accepted. |

## Examples

| Source-supported statement | Avoid overstatement |
|---|---|
| `PKG-002` has applicable Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports interfaces. | Do not add Process Piping, Electrical Power, or other interfaces for this package without source support. |
| Final geotechnical report is required before foundation design closure. | Do not state pile type, bearing capacity, settlement criteria, or frost protection as final values. |
| Civil design shall cover grading, drainage, roads, surface-water management, retention pond, and foundations among other listed topics. | Do not convert the topic list into complete deliverable contents or construction quantities. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-001 | No direct conflict; source gap only. Detailed Civil discipline deliverable register and closure criteria are not available in accessible sources. | Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-002-04` notes source-limited requirements remain open | `_REFERENCES.md` says no deliverable-specific source slices copied during PREPARATION | Specification Documentation; Procedure Steps; Datasheet Construction | Treat Gate 7 and accessible source slices as current authority; mark unsupported details `TBD` | TBD |
