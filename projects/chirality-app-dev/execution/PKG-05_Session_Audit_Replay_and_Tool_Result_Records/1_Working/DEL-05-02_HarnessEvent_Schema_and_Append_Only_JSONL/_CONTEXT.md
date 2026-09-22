# Context: DEL-05-02 HarnessEvent Schema and Append-Only JSONL

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-05 |
| PackageName | Session Audit, Replay, and Tool Result Records |
| DeliverableID | DEL-05-02 |
| DeliverableName | HarnessEvent Schema and Append-Only JSONL |
| ResponsibleParty | TBD |
| Type | DATA_MODEL_CHANGE |
| ContextEnvelope | M |

## Package Scope

**ScopeDescription:** App session/event consumption, legacy migration participation, replay, App-side redaction, accepted project artifacts, and conformance evidence.

**InclusionCriteria:** Client compatibility, replay/projection, affected-client diagnostics, and checkout acceptance evidence.

**Exclusions:** Generic session/event/tool-result persistence and daemon operational-state ownership.

## Deliverable Scope

Consume the Runtime-owned extensible HarnessEvent stream and its canonical append-only audit mirror; preserve proposal-interaction audit/replay meaning under SOW-082.

## Anticipated Artifacts

Current App/Runtime interface and conformance records; named implementation/verification evidence: Runtime `packages/core/src/session-store.ts`, `packages/daemon/src/codex-supervisor.ts`, `packages/contracts/src/harness/transcript-replay.ts`; App event/proposal/replay consumers.

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-014, SOW-015, SOW-039, SOW-082 |
| SupportsObjectives | OBJ-003 |
| ContextEnvelopeNotes | App event-consumption and conformance slice; generic persistence remains Root-owned. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## Current interface applicability — 2026-09-22

The application-owned Runtime service is the canonical session/event writer. Its store is `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/`; project-local `.chirality/sessions` is a legacy source. Runtime state is operational, not authoritative project truth. Provider thread/transcript references remain secondary linkage. Preserve the complete Codex notification/request stream, including upstream method names, identifiers and payloads after required redaction. Known events may have normalized views; unfamiliar notifications remain inspectable and every server request receives a truthful response. The closed event vocabulary and a prohibition on all upstream-shaped data are superseded, while canonical event ownership, terminal outcomes and secret protection remain. Preserve required envelope identity/version/time/parent/turn linkage, unique IDs and append sequence, accepted-before-execution and durable terminal outcomes. Ignore a malformed trailing line while retaining valid events and emitting diagnostics. Structural secret redaction and large-payload budgeting/artifact references occur before persistence, SSE and replay sinks. Evolution remains backward-compatible or explicitly versioned; no closed schema-v2 approval gate survives.

D-GOV-43/A2 and D-APP-127 govern current purpose and interface; prior dated alignments retain their historical scope. Existing decomposition and approval basis pins remain unchanged. The manager-owned dependency refresh separately records reviewed current row applications under the same accepted rulings; historical edge identity is preserved and actual satisfaction is evidence-bound.
