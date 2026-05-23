# Datasheet: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-04-03 |
| Deliverable Name | SdkMessageMapper and Provider-Neutral Translation |
| Package ID | PKG-04 |
| Package Name | SDK Adapter, Prompt, Provider, and Settings |
| Decomposition Variant | SOFTWARE_DECOMP |
| Decomposition Revision | v3.2 |
| Type | BACKEND_FEATURE_SLICE |
| Responsible Party | TBD |
| Context Envelope | M |
| Current Source State | REF-006 `docs/PRD.md` has `HASH_MISMATCH`; this run treats it as a source-state warning per task brief. |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary implementation artifact | `sdk-message-mapper.ts` | `_CONTEXT.md`; decomposition DEL-04-03 |
| Test artifacts | Mapper tests; provider-neutral leakage tests | `_CONTEXT.md`; decomposition DEL-04-03 |
| Scope items covered | SOW-040, SOW-044, SOW-051 | `_CONTEXT.md`; decomposition DEL-04-03 |
| Supported objectives | OBJ-002, OBJ-004 | `_CONTEXT.md`; decomposition DEL-04-03 |
| Browser-facing output contract | Compact `UIEvent`s / SSE events: `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, `process:exit` | REF-003 Section 11; REF-004 Section 7.4 |
| Persisted runtime output contract | Versioned `HarnessEvent` records with `schemaVersion`, `eventId`, `sessionId`, optional `turnId`, optional `parentEventId`, `timestamp`, `type`, and `data` | REF-003 Section 10; REF-004 Section 7.3 |
| SDK-specific data posture | SDK message names, session IDs, transcript paths, permission modes, hook names, and tool names remain adapter metadata, not public Chirality contracts | REF-001 Sections 2.8-2.10; REF-003 Section 10.3; REF-004 Section 9 |
| Known SDK input categories | `SDKSystemMessage`, `SDKAssistantMessage`, `SDKPartialAssistantMessage`, `SDKResultMessage`, permission-denial, hook, compact-boundary, tool-progress, and subagent messages | REF-006 Section 8.12, source-state warning applies |
| Exact observed SDK message sequence | TBD pending DEL-04-01 SDK probe / OI-001; current named categories are planning targets until probe-backed fixtures are accepted. | Decomposition OI-001; SOW-044; REF-006 FR-116, HASH_MISMATCH warning applies |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Route compatibility | Existing `/api/harness/turn` route shapes and SSE event names remain stable during SDK adoption. | REF-003 Sections 10.4 and 11; REF-006 Section 8.12 |
| Runtime boundary | Mapping operates behind `AgentEnginePort` / `RuntimeEngineContract`; SDK APIs do not define public semantics. | REF-003 Section 10; REF-001 Section 2.8 |
| Event separation | Browser `UIEvent`s and persisted `HarnessEvent`s are separate contracts. | SOW-040; REF-003 Sections 10.3 and 11; REF-006 FR-074 |
| SDK model/tool loop | SDK supplies the model/tool loop when conformance passes; Chirality mirrors SDK tool-use, tool-result, permission-denial, hook, result, and compact-boundary messages into events. | SOW-051; REF-006 FR-083 |
| Redaction boundary | Runtime event data and logs must not expose API keys or configured secret variants. | REF-006 FR-075; REF-005 Section 6.3 |
| Conformance boundary | SDK-backed adapter must pass engine conformance tests before production default use. | REF-003 Section 10.3 |
| Dependency state | `Dependencies.csv` exists with 11 ACTIVE extracted rows; satisfaction remains `TBD` for all rows, including ACTIVE upstream execution dependencies DEL-04-01, DEL-03-01, DEL-03-03, and DEL-04-02. | `_DEPENDENCIES.md`; `Dependencies.csv` |

## Construction

| Component | Expected Construction |
|---|---|
| Mapper module | A backend module, anticipated as `sdk-message-mapper.ts`, that translates SDK stream/message inputs into Chirality-owned `UIEvent` and `HarnessEvent` outputs. |
| UI mapping surface | A deterministic mapping to the stable browser SSE event names without exposing SDK message names in the browser contract. |
| Runtime-event mapping surface | A deterministic mapping to versioned `HarnessEvent` categories, including model, tool, permission, hook, compact-boundary, terminal, and SDK metadata records where source-supported. |
| Adapter metadata handling | SDK-specific identifiers and paths appear only under explicit adapter metadata fields or equivalent confined metadata structures. |
| Leakage tests | Tests assert that public APIs, UI events, and canonical runtime events do not become SDK-shaped. |
| Probe-dependent cases | ASSUMPTION: cases for exact SDK message payload shapes will be completed after DEL-04-01 confirms observed SDK message categories. |

## References

| RefID | Source Slice Used |
|---|---|
| REF-001 | `docs/DIRECTIVE.md` Sections 2.8, 2.9, 2.10 and the decision record table covering product-owned contracts, provider-neutral core, SDK metadata posture, and audit mirror canonicality. |
| REF-003 | `docs/SPEC.md` Sections 10, 11, 12, 14, 15, and 19.3 covering runtime engine boundary, SSE events, SDK settings, tool surface, permission mapping, and validation IDs. |
| REF-004 | `docs/TYPES.md` Sections 7.1, 7.2, 7.3, 7.4, and 9 covering `SdkMessageMapper`, `HarnessEvent`, `UIEvent`, SDK transcript, and adapter vocabulary. |
| REF-005 | `docs/PLAN.md` R1 targets and Section 6.3 covering `sdk-message-mapper.ts`, event mapping, and redaction. |
| REF-006 | `docs/PRD.md` Sections 8.12 and 8.13, used with HASH_MISMATCH warning per task brief. |
| DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-04-03, SOW-040, SOW-044, SOW-051, OBJ-002, OBJ-004, and OI-001. |
