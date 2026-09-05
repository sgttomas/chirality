# Context: DEL-02-04 Dialogue Toolkit, Context, and Local UI State

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-02 |
| PackageName | Woven Dialogue Shell, Navigation, and Operator State |
| DeliverableID | DEL-02-04 |
| DeliverableName | Dialogue Toolkit, Context, and Local UI State |
| ResponsibleParty | TBD |
| Type | UX_UI_SLICE |
| ContextEnvelope | S |

## Package Scope

**ScopeDescription:** Dialogue-centred shell with an invariant centre dialogue,
left chat navigator, one-view-at-a-time right panel (files, document, workflows,
who is working, activity, session, settings), activity strip, composer context
line, account row and settings presentation, compatibility surfaces, and
non-authoritative local UI state.

**InclusionCriteria:** Human-agent dialogue, artifact collaboration,
coordination presentation, and operator workflow behavior.

**Exclusions:** Runtime engine internals, canonical session/evidence ownership,
arbitrary orchestration graphs, automatic intent inference, and
project-control-plane authority.

## Deliverable Scope

Expose runtime options and preserve versioned layout (per-view right-panel
widths, expand state), drafts, explicit next-turn context references, artifact
anchors, selected replay references, panel state, chat annotations, known
folders, chat rung and declined proposal triggers, and local presets as
non-authoritative convenience state with rollback-safe migration; present the
one-line activity strip in place of the resizable shelf.

Applied decomposition row L310 (SCA-APP-010 Gate 5, 2026-09-04) notes:
Convenience state stores references and presentation only; it never stores
authoritative workflow, hierarchy, permission, or acceptance conclusions; the
workflow file and the session record own rung-related truth.

## Anticipated Artifacts

Toolkit controls; workspace-state schema; resize/focus/anchor behavior;
context-reference, draft/preset, isolation, and migration guards

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-004, SOW-008, SOW-016 |
| SupportsObjectives | OBJ-001, OBJ-004 |
| ContextEnvelopeNotes | Convenience state stores references and presentation only; it never stores authoritative workflow, hierarchy, permission, parentage, lifecycle, or acceptance conclusions. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2
SOFTWARE_DECOMP working surface and retains its physical name for compatibility.
SCA-APP-004 and its owner-approved amendment prospectively control the current
presentation target. Downstream TASK work must preserve `ResponsibleParty:
TBD` until a human assigns ownership and must preserve the authority boundary
between convenience references and canonical project/runtime records.
