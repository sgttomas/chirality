# Context: DEL-05-04 Runtime Replay, Dialogue, and Agent Transcript Projection

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-05 |
| PackageName | Session Audit, Replay, and Tool Result Records |
| DeliverableID | DEL-05-04 |
| DeliverableName | Runtime Replay, Dialogue, and Agent Transcript Projection |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** App session/event consumption, legacy migration participation, replay, App-side redaction, accepted project artifacts, and conformance evidence.

**InclusionCriteria:** Client compatibility, replay/projection, affected-client diagnostics, and checkout acceptance evidence.

**Exclusions:** Generic session/event/tool-result persistence and daemon operational-state ownership.

## Deliverable Scope

Provide a labelled read-only replay projection from Runtime canonical records alongside the primary dialogue. Explicit native continuation is permitted by D-GOV-43 item 5 and must remain distinct from viewing history.

## Anticipated Artifacts

Current App/Runtime interface and conformance records; named implementation/verification evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`, right-panel Session view and selected-session/shell tests.

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-006, SOW-042, SOW-046 |
| SupportsObjectives | OBJ-001, OBJ-003 |
| ContextEnvelopeNotes | Replay/reporting slice over canonical records; projection is rebuildable and presentation-only. |

## SCA-APP-004 Ownership Boundary

- DEL-05-04 owns transcript/replay reconstruction and semantic runtime
  projection.
- DEL-08-05 remains the unchanged owner of canonical child-run records and
  exact parentage/return references.
- DEL-02-01 and DEL-02-02 own shell and Coordination Panel presentation.
- DEL-08-02 owns persona/agent/session routing and guarded selection.
- DEL-08-03 owns Pipeline dispatch semantics.
- DEL-05-04 does not own project plans, approvals, assignments, aliases,
  dispatch, child-record persistence, direct child messaging, or editable
  hierarchy.
- Missing, stale, bounded, malformed, conflicting, or unrecorded evidence is
  shown explicitly rather than inferred.

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## Current interface applicability — 2026-09-22

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Replay preserves sequence, valid events before malformed tails, terminal outcomes, tools/artifact linkage and explicit missing/stale/bounded/conflicting evidence. Use exact parent/return IDs, never inferred conversational similarity. Viewing replay must not mutate the primary draft, attachments, next-turn context, permissions or identity. An explicit continue action uses native continuation with truthful account/policy compatibility or fresh-session presentation, without silently reattaching an in-flight turn. Runtime completion is never project or lifecycle acceptance.

D-GOV-43/A2 and D-APP-127 govern current purpose and interface; prior dated alignments retain their historical scope. Existing decomposition and approval basis pins remain unchanged. The manager-owned dependency refresh separately records reviewed current row applications under the same accepted rulings; historical edge identity is preserved and actual satisfaction is evidence-bound.
