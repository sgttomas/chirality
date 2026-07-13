# Procedure: DEL-02-03 Working Root File Tree and Scope Scan UI

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

Define the working procedure to produce and verify the Working Root File Tree and Scope Scan UI slice without expanding into filesystem enforcement, dependency extraction, or runtime engine internals.

## Prerequisites

| Prerequisite | Status / Note | Source |
|---|---|---|
| Accepted SOFTWARE_DECOMP v3.2 entry for DEL-02-03 | Available | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| Working-root validation API contract | Available at contract level; implementation details TBD | `docs/SPEC.md` §17.2; `docs/PRD.md` FR-003 |
| File-tree API contract | Available at contract level; response shape details TBD | `docs/SPEC.md` §17.2; `docs/PRD.md` FR-004 |
| Scope-scan API contract | Available at contract level; response shape details TBD | `docs/SPEC.md` §17.2; `docs/PRD.md` FR-013 |
| Declared upstream dependencies | TBD; no accepted dependency edges extracted yet | `_DEPENDENCIES.md` |
| PRD source hash acceptance | Human ruling needed; mismatch is warning for this run | `_REFERENCES.md`; dispatch instruction |

## Steps

1. Confirm the active deliverable identity.
   - Use `PackageID=PKG-02` and `DeliverableID=DEL-02-03` as stable identity.
   - Preserve `ResponsibleParty: TBD`.
   - If folder labels disagree with stable IDs, surface the mismatch rather than renaming during this deliverable.

2. Wire or verify working-root selector integration.
   - Provide path entry, folder selection, apply, and clear controls.
   - On apply, call the working-root validation surface.
   - On clear, remove selected-root dependent UI state and disable root-dependent runtime actions.

3. Render working-root validation feedback.
   - Show failures for non-absolute, missing, inaccessible, non-directory, or instruction-root-contained paths.
   - Preserve typed-error details when available.
   - Use exact error copy from implementation or UX source when available; otherwise mark copy as `TBD`.

4. Render the bounded file tree.
   - Consume `/api/working-root/tree` or the local equivalent.
   - Display tree nodes within the bounded result set.
   - Reflect skipped, inaccessible, or truncated directories when represented in the API result.
   - Do not perform unbounded renderer-side traversal.

5. Integrate scope scan results.
   - Consume `/api/working-root/scope` or the local equivalent.
   - Present deliverables and knowledge-type directories using canonical scope vocabulary.
   - Clear invalid selections after root changes, removed deliverables, disabled knowledge markers, or stale knowledge targets.

6. Add deliverable summary widgets.
   - Show stable deliverable ID, name, package context, lifecycle state where available, and dependency snapshot status where available.
   - Route deliverable rows to PIPELINE `TASK*` with the deliverable preselected when supported.
   - Keep dependency extraction deferred; do not create `Dependencies.csv` as part of this procedure.

7. Verify ownership boundaries.
   - Confirm UI code consumes workspace APIs rather than duplicating filesystem policy enforcement.
   - Confirm runtime/filesystem deliverables retain ownership of path containment, traversal bounds, status parsing, dependency parsing, and lifecycle transition enforcement.

8. Record unresolved facts.
   - Mark missing implementation details as `TBD`.
   - Raise source/path/hash conflicts for human ruling.

## Verification

| Check | Expected Result |
|---|---|
| Working-root selection | Path entry, folder selection, apply, and clear states are available. |
| Invalid root feedback | Invalid roots produce visible feedback with typed-error information where available. |
| Clear root behavior | Root-dependent actions and stale scope selections are disabled or cleared. |
| File tree bounds | Skipped directories and truncation/inaccessible indicators match API behavior. |
| Scope scan reset | Removed or stale deliverable/knowledge selections are cleared. |
| Deliverable routing | Deliverable summary row routes to PIPELINE `TASK*` with stable deliverable identity. |
| Project truth boundary | UI state is not treated as authoritative project truth. |
| Dependency deferral | No `Dependencies.csv` is created by this deliverable procedure. |
| Unknown discipline | Unsupported facts remain `TBD`, `ASSUMPTION`, conflict, or human-ruling-needed. |
| Acceptance evidence | Test or acceptance evidence for selector, invalid-root feedback, bounded tree behavior, scope reset, and deliverable routing is required; evidence artifact location is TBD until implementation/test output exists. |

## Records

- UI implementation artifacts: file tree panel, deliverable summary widgets, scope scan integration.
- Test or acceptance evidence for root selection, invalid root display, bounded tree behavior, scope reset behavior, and deliverable routing; artifact location TBD.
- Conflict/human-ruling record for package-folder label MATCH and PRD hash status: MATCH. (reconciled under D-APP-38).
- This four-document kit: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`.

## Pass 3 Disposition Notes

| ItemID | Disposition | Evidence |
|---|---|---|
| F-001 | Incorporated as required evidence with `TBD` artifact location: Procedure now preserves acceptance evidence as required without implying it already exists. | `Procedure.md` Verification and Records; `Specification.md` Verification. |

## D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-108 supersedes run-scoped extraction deferral wording: the nine-row derivative register exists; the file-tree UI still does not own dependency extraction.
