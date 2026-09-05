# Context: DEL-02-01 Woven Dialogue Shell and Compatibility Navigation

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-02 |
| PackageName | Woven Dialogue Shell, Navigation, and Operator State |
| DeliverableID | DEL-02-01 |
| DeliverableName | Woven Dialogue Shell and Compatibility Navigation |
| ResponsibleParty | TBD |
| Type | UX_UI_SLICE |
| ContextEnvelope | M |

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

Compose the persistent primary human–agent transcript and composer with its
context line (folder, agent, permissions, delegation, rung), the header-less
three-panel frame, the left-panel chat navigator with local organisation,
per-chat folder selection over the known-folder set, the account row host, and
compatibility navigation without creating a second evidence store.

Applied decomposition row L307 (SCA-APP-010 Gate 5, 2026-09-04) notes: Shell
integration owns presentation only; work, hierarchy, transcript, and artifact
facts remain governed by their existing semantic owners; the direct shell items
are seated as Remaining work by the owner, not by this row.

## Anticipated Artifacts

Dialogue shell; inline artifact/focus views; Work/Agents panel; Activity Shelf;
route/query and compatibility tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-001, SOW-005 |
| SupportsObjectives | OBJ-001 |
| ContextEnvelopeNotes | Shell integration owns presentation only; work, hierarchy, transcript, and artifact facts remain governed by their existing semantic owners. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2
SOFTWARE_DECOMP working surface and retains its physical name for compatibility.
SCA-APP-004 and its owner-approved amendment prospectively control the current
presentation target. Downstream TASK work must preserve `ResponsibleParty:
TBD` until a human assigns ownership and must not treat this presentation slice
as canonical work, session, replay, artifact, lifecycle, or runtime authority.
