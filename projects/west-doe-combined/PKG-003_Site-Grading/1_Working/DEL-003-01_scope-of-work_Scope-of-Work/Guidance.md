# Guidance: DEL-003-01_scope-of-work — Scope of Work

## Purpose

The Scope of Work exists to anchor the Site Grading package before downstream package datasheet, construction work package, and EPC/Civil discipline production work proceed. It should state what package is being delivered, why it exists in the facility package set, which sources define it, where its boundaries and interfaces are known, and which basis items remain open.

## Principles

- Use Gate 7 as the accepted decomposition truth for deliverable identity, package mapping, artifact expectations, interfaces, and objective association.
- Use the workbook source row as the controlling package identity slice for WBS, CoA tracking number, discipline, package name, and interface marks.
- Use the Deepcut DBM civil section as the governing accessible civil basis for site grading, drainage, retention pond, surface-control, and future external inputs.
- Keep open design inputs visible. Survey, grade surface file, plot plan, final drainage design, ditch/culvert sizing, retention pond capacity, and final pond location are not closed by this scope-of-work source slice.
- Treat objective associations as context, not as standalone detailed requirements, unless tied back to workbook or DBM source material.

## Considerations

| Topic | Guidance |
|---|---|
| Package identity | The workbook row and Gate 7 package register agree on `PKG-003`, Site Grading, Civil, WBS `01`, and CoA tracking number `26020-01-42-003`. |
| Interface framing | Drain / Containment and Grading / Site Drainage / Spill Containment are package interfaces; the scope of work should preserve them for downstream design and construction deliverables. |
| Design maturity | The DBM states that final civil requirements depend on geotechnical, topographical, plot-plan, and detailed drainage inputs. The scope of work should identify those dependencies without finalizing their values. |
| Surface-water management | The scope should carry the intent to prevent off-site surface overflow from entering the facility and direct/contain on-site overflow to a retention pond. |
| Responsibility | The deliverable owner is EPC Integrator, but the package-level responsibility model remains source-dependent for EPC Integrator versus discipline subcontractor assignment. Preserve that distinction. |
| Tagged equipment | Do not invent tagged equipment for Site Grading. Record as TBD unless later accepted sources provide tags or asset identifiers. |

## Trade-offs

| Trade-off | Direction |
|---|---|
| Completeness vs. source fidelity | Prefer source fidelity. Missing values should remain TBD rather than being filled from civil design convention. |
| Package-level scope vs. detailed design | Keep this deliverable at scope-of-work level; detailed grading and drainage design belongs to downstream discipline production and construction deliverables. |
| Objective context vs. requirements | Use `OBJ-001`, `OBJ-007`, `OBJ-008`, and `OBJ-009` to explain relevance, but avoid turning them into unqualified requirements without source support. |

## Examples

| Example statement | Status |
|---|---|
| "The Site Grading package is a Civil package under WBS 01 with CoA tracking number `26020-01-42-003`." | Supported by workbook row 4 and Gate 7 `PACKAGE_REGISTER.csv`. |
| "The package carries Drain / Containment and Grading / Site Drainage / Spill Containment interfaces." | Supported by workbook row 4 and Gate 7 `INTERFACE_REGISTER.csv`. |
| "The final retention pond capacity is [value]." | TBD; not supported by accessible source material for this deliverable. |
| "Final ditch and culvert sizing are complete." | Unsupported; DBM identifies detailed engineering drainage design as a required future input. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| None | No direct source conflict identified during P1/P2 drafting. | N/A | N/A | N/A | N/A | N/A |

## Open TBD Items

| TBD ID | Item | Reason |
|---|---|---|
| TBD-001 | Tagged grading/drainage equipment or asset list | No tagged equipment appears in the accessible row/slice for this scope-of-work deliverable. |
| TBD-002 | Package-specific exclusions | Gate 7 package register states no package-specific exclusions in source materials. |
| TBD-003 | Final topographical survey / grade surface file details | DBM states the final format, data model, and contents are TBD pending survey completion. |
| TBD-004 | Final retention pond location and capacity | DBM states these are tied to detailed engineering and plot-plan coordination. |
| TBD-005 | Final ditch and culvert sizing | DBM lists detailed engineering drainage design as a required external input. |
| TBD-006 | Final EPC Integrator versus discipline subcontractor assignment beyond deliverable ownership | Package responsibility model remains source-dependent. |
