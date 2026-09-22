# Context: DEL-05-03 Redacted RunLogger and Secret Hygiene

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-05 |
| PackageName | Session Audit, Replay, and Tool Result Records |
| DeliverableID | DEL-05-03 |
| DeliverableName | Redacted RunLogger and Secret Hygiene |
| ResponsibleParty | TBD |
| Type | SECURITY_CONTROL |
| ContextEnvelope | S |

## Package Scope

**ScopeDescription:** App session/event consumption, legacy migration participation, replay, App-side redaction, accepted project artifacts, and conformance evidence.

**InclusionCriteria:** Client compatibility, replay/projection, affected-client diagnostics, and checkout acceptance evidence.

**Exclusions:** Generic session/event/tool-result persistence and daemon operational-state ownership.

## Deliverable Scope

App clients and diagnostics conform to Runtime-owned secret hygiene. Generic run-logger implementation belongs to Runtime under SCA-APP-005; the App owns its presentation/transport sinks and conformance evidence.

## Anticipated Artifacts

Current App/Runtime interface and conformance records; named implementation/verification evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`; App event/SSE/replay and diagnostics consumers; retained App `frontend/src/lib/harness/run-logger.ts` and redaction fixtures.

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-021, SOW-041 |
| SupportsObjectives | OBJ-003, OBJ-008 |
| ContextEnvelopeNotes | App source/presentation security and conformance; no generic run-logger ownership. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## Current interface applicability — 2026-09-22

Apply structural redaction before Runtime JSONL writes, both SSE hops, replay, App Server diagnostics, logs, errors and artifacts. Preserve safe error/status/source/event metadata and encoded-secret variants without reading Codex credential stores. D-APP-67 API-key helper scope and replacement token remain the historical helper contract; it is not a generic credential registry. Sensitive payloads require redaction before storage or display. PEC credentials and pec_session remain excluded from envelopes/logs/model context whenever that gated transport is used; no new domain activation follows.

D-GOV-43/A2 and D-APP-127 govern current purpose and interface; prior dated alignments retain their historical scope. Existing decomposition and approval basis pins remain unchanged. The manager-owned dependency refresh separately records reviewed current row applications under the same accepted rulings; historical edge identity is preserved and actual satisfaction is evidence-bound.
