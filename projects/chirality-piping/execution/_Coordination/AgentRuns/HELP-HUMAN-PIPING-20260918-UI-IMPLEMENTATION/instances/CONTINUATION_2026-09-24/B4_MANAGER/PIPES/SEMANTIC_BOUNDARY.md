# Pipes bounded source and verification boundary

This manager interpretation applies ROOT_BRIEF.md within the current source, not a reusable instruction amendment. Current ownership is SCA-011/DAG-011: DEL-07-02 owns selected-entity/table behavior and DEL-07-08 owns review/apply interaction; shared session/execution stay their owners. The old DEL-07-02 dependency index still names DAG-007; the current `_DAG/_LATEST.md`, accepted SCA-011 and ROOT brief supply DAG-011 authority without rewriting the historical index.

| Field | Actual operation semantics | Bounded UI behavior |
|---|---|---|
| Label, string provenance | Element Text/set_field, dimensionless; replacement normalized by engine. Non-string provenance must not be silently flattened. | Existing text-table direct/review semantics; structured route only. |
| Material | Element EntityRef/materials; stored reference string required, replacement id must exist. The backend writes an id string, not a label or arbitrary object. | Existing enum editor can show current material ids with opt-in reference metadata/validation; stale catalog/current value may not bypass backend authority. |
| Mill tolerance, present | Element OptionalQuantity(length, NonNegative). Zero is meaningful. Existing numeric value requires actual sibling unit metadata; explicit quantity payload must agree with intent unit. | Preserve actual entered unit for bare numeric edit; block missing numeric-unit metadata rather than copy project/wall units. No accidental numeric no-op equating absent with zero. |
| Mill tolerance, absent | Backend `resolve_optional_quantity` checks before `TBD` and creates the whole value/unit record only from explicit accepted entry. | Bounded opt-in combined entry `value unit` for absent slots, visibly explained. Direct and review Queue must serialize the same payload. Absence must not prevent editor entry merely because quantity sort projection is unavailable. |
| From, To, shared Section | Separate dedicated topology/assignment/detachment operations; no scalar field permission. | Readonly in this migration. |

The implementation TASK proposed and the manager accepted the existing table editor with opt-in adapter metadata and a Pipe branch of the shared LibraryTable. Source ownership is limited to ModelTree.tsx, modelTableAdapter.ts and corresponding meaningful maintained tests/e2e fixtures unless a concrete dependency is returned. No tableState/EngineeringTable/VirtualList/session/engine or geometry change is presently indicated.

Backend basis: `core/model_operations/operation_applier/src/lib.rs` field rules398–466, EntityRef6790ff, OptionalQuantity7091ff; `section_bindings.rs` geometry/cache and validate_local. The older PropertyInspector mill-tolerance fallback is not copied or independently amended by this slice. Engineering units remain the existing backend/catalog authority; no new numeric tolerance or engineering defaults are introduced.

## Verification to obtain under ROOT resource grant

- Direct/review label and string provenance through the actual operation route, equivalent captured before/after/unit intent, selection/focus, Apply/Cancel and Undo/Redo.
- Existing mill quantity in actual unit, absent explicit zero with unit, rejection of bare absent number/unknown unit/negative text/numeric missing unit, no-op distinction, raw review retention and Queue/Clear.
- Material exact id completion by keyboard/pointer, invalid/foreign/nonexistent id, stale catalog/value/unit/project protection and no passive prefix completion.
- Effective-wall and shared-cache rejections against the actual backend, with no model/history mutation; valid-bound control. Separate unbound Pipe probe is required because source validate_local currently checks geometry only within a present section_ref branch. That is a suspected backend gap, not yet an observed runtime defect or authorization to edit engine code.
- Existing Nodes/Materials/Sections interaction tests affected by shared adapter/host changes; genuine current Pipe browser editing/history and compact reach. Existing compact-fit geometry criteria stay unchanged, and completed PR883 gates are not rerun merely for recovery.

ROOT has been asked for the bounded test/build/browser lane. No test result follows from source tracing or existing tests. Native/CI/clean DEC-025 and final Git integration remain ROOT-owned.
