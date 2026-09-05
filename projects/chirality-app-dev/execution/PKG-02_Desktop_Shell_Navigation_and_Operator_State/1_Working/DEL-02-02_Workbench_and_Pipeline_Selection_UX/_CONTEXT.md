# Context: DEL-02-02 Right-Panel Coordination, Workflows, and Proposal UX

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-02 |
| PackageName | Woven Dialogue Shell, Navigation, and Operator State |
| DeliverableID | DEL-02-02 |
| DeliverableName | Right-Panel Coordination, Workflows, and Proposal UX |
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

Present, in the right panel, the "Who is working" view over recorded
agent/session selections and Agent 0/1/2 role entry for Codex sessions with
source, authority class, responsible reference, currency, and evidence; the
Workflows view, roadmap, New workflow form, library, and bind actions over
governed workflow files; and the transcript proposal card rendered from
`proposal.*` events. Workbench and Pipeline are retired from the active shell
(code, routes, and tests retained) and the Work projection is unmounted until an
explicitly recorded plan/task source exists.

Applied decomposition row L308 (SCA-APP-010 Gate 5, 2026-09-04) notes: DEL-08-02
retains routing, DEL-08-03 retains dispatch, DEL-08-04 retains role/delegation
semantics, DEL-08-05 retains child records, DEL-05-04 retains replay/projection
semantics, DEL-07-03 owns the workflow file contract, and DEL-06-03 owns the
`propose` tool; this deliverable only composes accepted presentation, applies
human proposal decisions, and does not infer enforcement. Split trigger: if
implementation review finds cross-domain churn between the coordination and
workflow views, propose a split before widening the envelope.

## Anticipated Artifacts

Who is working view; Workflows view, roadmap, and forms; proposal card;
role-entry controls; exact `role not mechanically enforced` and `Opt-in Preview`
posture labels; provenance labels; stale/empty-state, label, and query
compatibility tests

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-006, SOW-081, SOW-082 |
| SupportsObjectives | OBJ-001, OBJ-007 |
| ContextEnvelopeNotes | This deliverable composes presentation over admitted sources; it does not create plan, dispatch, parentage, lifecycle, approval, or runtime authority. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2
SOFTWARE_DECOMP working surface and retains its physical name for compatibility.
SCA-APP-010 (applied at Gate 5, 2026-09-04; D-APP-108) controls the current
presentation target through the applied decomposition row L308 and the
SCA-APP-010 Gate-5 Current Contract section of `ScopeOfWork.md`; SCA-APP-004 and
its owner-approved amendment remain dated history. Downstream TASK work must
preserve `ResponsibleParty: TBD` until a human assigns ownership. The Who is
working view, the Workflows view, and the proposal card present accepted state
and never infer enforcement; conversational prose and panel-local state must not
be converted into project truth.
