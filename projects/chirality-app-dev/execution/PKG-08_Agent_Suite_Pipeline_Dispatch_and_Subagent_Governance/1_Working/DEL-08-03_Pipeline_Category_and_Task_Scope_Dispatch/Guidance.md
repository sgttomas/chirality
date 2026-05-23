# Guidance: DEL-08-03 Pipeline Category and Task Scope Dispatch

## Purpose

This deliverable keeps the operative PIPELINE dispatch surface aligned with Chirality's agent architecture. It connects the operator-facing category controls to the governed execution model without turning UI selection into runtime authority.

The practical outcome is a user experience where operators can see the available operative lanes, choose a valid TASK scope, discover deliverable-local knowledge buckets, and understand unsupported variants because they remain visible but disabled.

## Principles

| Principle | Guidance | Source |
|---|---|---|
| Use canonical vocabulary | Use the terms `PipelineCategory`, `TaskScopeMode`, `KnowledgeTypeOption`, and `DisabledOption` consistently in implementation-facing docs, tests, and state models where applicable. | `docs/TYPES.md` Section 4.4 |
| Keep operative dispatch explicit | PIPELINE category controls should make `DECOMP`, `PREP`, `TASK`, and `AUDIT` visible as separate operative choices. | `docs/PRD.md` FR-011 |
| Separate task selection from scope selection | TASK flow should not collapse task-agent choice and scope choice into one ambiguous selector. | `docs/PRD.md` FR-012 |
| Treat knowledge-type mode as deliverable-bound | Knowledge-type targets depend on a selected deliverable and should clear when that deliverable is unavailable or stale. | `docs/PRD.md` FR-012, FR-013 |
| Show unsupported variants without enabling them | Disabled options preserve roadmap awareness while preventing accidental execution. | `docs/PRD.md` FR-011; success metric 7 |
| Do not expand authority | Selector state may request or describe a route, but Type 2 execution remains governed by agent instructions, sealed context, approval metadata, and fail-closed gates. | `docs/CONTRACT.md` Section 1.8 |

## Considerations

- Prefer source-derived option lists and vocabulary over ad hoc labels. If implementation code already has local naming, reconcile it with `docs/TYPES.md` rather than silently creating a parallel taxonomy.
- Scope scan behavior should be resilient to working-root changes. A selected deliverable or knowledge bucket that is no longer present should be cleared instead of retained as stale UI state.
- Knowledge-type discovery should account for the four-document kit first. Metadata buckets should be exposed only when the UI can use canonical `KnowledgeTypeOption` labels or an explicit mapping to them, because partial local labels would create a parallel taxonomy.
- The deliverable's anticipated artifacts are tests and discovery behavior, not new authority for runtime subagent execution.
- PRD hash mismatch is a warning. Use PRD content conservatively and preserve the mismatch in closure materials until a human reconciles the reference hash.

## Boundary Rationale

PIPELINE dispatch expresses operator intent and selects a proposed route through the operative surface. It is not an authorization boundary. Runtime authority remains with TASK and Type 2 governance checks because `docs/CONTRACT.md` requires explicit write scope, sealed context and gate metadata, no ghost inputs, and fail-closed subagent delegation. Selector state can therefore prepare or display a route, but execution must still pass the governed runtime checks before any child agent or task path is enabled.

## Human Ruling Path

| Topic | Required Ruling | Current Treatment |
|---|---|---|
| REF-006 PRD hash mismatch | Source owner or human reviewer must reconcile the expected and observed PRD hash, or explicitly accept continued conservative PRD use for this deliverable. | Keep PRD-derived requirements warning-qualified and do not treat the mismatched PRD hash as final closure evidence. |
| Closure language for PRD-derived controls | Human reviewer must approve wording that distinguishes PRD-derived source-warning content from accepted source truth before final issue. | State that PRD content is used under recorded `HASH_MISMATCH` warning until reconciled; do not upgrade the warning by implication. |

## Trade-offs

| Decision Area | Preferred Direction | Trade-off |
|---|---|---|
| Disabled options | Keep unsupported variants visible and disabled. | Operators see future or unavailable paths, but the UI must avoid implying they are executable. |
| Dynamic scope reset | Clear invalid selections aggressively. | Users may need to reselect after root changes, but stale execution targets are avoided. |
| Knowledge bucket coverage | Start from canonical document-kit and metadata bucket terms. | Implementation may need mapping if existing file names or UI labels differ. |
| Governance boundary | Let UI dispatch describe intent only; execution approval remains separate. | More state checks may be needed before invoking TASK or subagent pathways. |

## Examples

| Scenario | Expected Handling |
|---|---|
| Operator selects PIPELINE `TASK`, then switches scope mode to `KNOWLEDGE_TYPES` without selecting a deliverable. | The UI should require a target deliverable before knowledge-type targets become executable. |
| Active working root changes and the previously selected deliverable is no longer in the scope scan. | The selected deliverable and dependent knowledge target should reset. |
| A future AUDIT variant is known but not implemented. | It may be visible as a disabled option with no runtime execution path. |
| A deliverable folder has `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`. | These files should be discoverable as first-class knowledge buckets when knowledge-type scope is used. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-001 | PRD reference hash does not match expected hash in `_REFERENCES.md`. | `_REFERENCES.md` REF-006 expected hash | `_REFERENCES.md` REF-006 actual hash | All PRD-derived requirements | Continue using PRD as directed source warning for this P1/P2 run; reconcile hash before final closure. | TBD |

## Assumptions

- ASSUMPTION: OBJ-001 and OBJ-007 are relevant because the decomposition explicitly lists them for DEL-08-03.
- ASSUMPTION: The final implementation surface is frontend/UI state and tests, but specific component and test file paths are TBD until the implementation worker selects or confirms existing modules.

## Pass 3 Disposition Notes

| ItemID | Disposition |
|---|---|
| A-001 | Surfaced as conflict; the PRD hash mismatch remains in the Conflict Table and Human Ruling Path. |
| C-001 | Incorporated as rationale for exposing metadata buckets only with canonical `KnowledgeTypeOption` labels or explicit mapping. |
| D-001 | Converted to a human ruling path for REF-006 reconciliation before final closure. |
| E-001 | Incorporated as boundary rationale distinguishing UI intent from TASK and Type 2 runtime authority. |
| E-002 | Converted to human-approved closure-language requirement for PRD-derived controls under `HASH_MISMATCH`. |
