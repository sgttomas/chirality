# Context: DEL-05-05 ToolResultStore and Session Artifacts

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-05 |
| PackageName | Session Audit, Replay, and Tool Result Records |
| DeliverableID | DEL-05-05 |
| DeliverableName | ToolResultStore and Session Artifacts |
| ResponsibleParty | TBD |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** App session/event consumption, legacy migration participation, replay, App-side redaction, accepted project artifacts, and conformance evidence.

**InclusionCriteria:** Client compatibility, replay/projection, affected-client diagnostics, and checkout acceptance evidence.

**Exclusions:** Generic session/event/tool-result persistence and daemon operational-state ownership.

## Deliverable Scope

App consumption, previews and conformance for Runtime-owned tool results/artifacts; storage and generic custody stay Runtime-owned. D-APP-132 leaves D-APP-116 full inventory/cleanup enhancement unadopted for this undertaking.

## Anticipated Artifacts

Current App/Runtime interface and conformance records; named implementation/verification evidence: Runtime `packages/core/src/session-store.ts`, `packages/contracts/src/harness/tool-descriptor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App preview consumers; legacy `frontend/src/lib/harness/tool-result-artifacts.ts` and fixtures.

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-053, SOW-059 |
| SupportsObjectives | OBJ-003, OBJ-005 |
| ContextEnvelopeNotes | App consumption/evidence slice; generic operational result storage remains daemon-owned. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## Current interface applicability — 2026-09-22

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Current descriptor thresholds govern small-inline and artifact-backed overflow with bounded summaries and replayable relative links; no distinct medium-band representation is adopted. D-APP-42 metadata includes tool/turn identity when available, original/stored bytes, truncation, SHA-256 of exact stored bytes, session-lifetime retention and stream labels. Preserve current descriptor-defined thresholds, deterministic concurrent append order and malformed-tail recovery. Redaction must precede artifact and event persistence. No TTL, quota, independent cleanup or full inventory feature is adopted. Current fixed truncation and raw tool.progress deltas do not satisfy artifact/metadata obligations.

D-GOV-43/A2 and D-APP-127 govern current purpose and interface; prior dated alignments retain their historical scope. Existing decomposition and approval basis pins remain unchanged. The manager-owned dependency refresh separately records reviewed current row applications under the same accepted rulings; historical edge identity is preserved and actual satisfaction is evidence-bound.

2026-09-22 review repair: The distinct medium-band preview representation remains deferred under D-APP-42 and D-APP-56 R4-P08. Current small-inline and artifact-backed overflow behavior under unchanged descriptor thresholds is required; it must not be claimed as implementing the deferred distinct medium band. Adopting that band or changing thresholds/preview limits needs its own governed policy decision and boundary tests. D-APP-132's D-APP-116 inventory/cleanup disposition does not adopt it.
