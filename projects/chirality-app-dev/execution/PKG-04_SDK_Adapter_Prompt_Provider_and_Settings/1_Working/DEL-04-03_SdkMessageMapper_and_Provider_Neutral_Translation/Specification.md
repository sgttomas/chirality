# Specification: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation

## Scope

This deliverable specifies the backend mapping surface that translates SDK stream messages into stable browser `UIEvent`s and provider-neutral persisted `HarnessEvent`s without allowing SDK message shapes, provider identifiers, transcript paths, or tool names to define Chirality's public or canonical contracts.

In scope:

- `sdk-message-mapper.ts` or equivalent mapper module.
- Deterministic mapping from SDK message categories to browser-facing `UIEvent`s.
- Deterministic mapping from SDK message categories to versioned `HarnessEvent`s.
- Mapper tests and provider-neutral leakage tests.
- Handling of SDK session and transcript linkage only as adapter metadata when relevant to mapped events.
- Mapping hooks for SDK tool-use, tool-result, permission-denial, hook, result, compact-boundary, terminal, and subagent lifecycle messages where source-supported.

Out of scope:

- Defining the product-owned `AgentEnginePort` / `RuntimeEngineContract` itself; that is owned by DEL-03-01.
- Persisting the append-only JSONL event log; that is owned by PKG-05, with this deliverable supplying mapping outputs compatible with it.
- Building SDK options and settings isolation; that is owned by DEL-04-02.
- Confirming exact SDK package behavior and message sequence; that is owned by DEL-04-01 / OI-001.
- Expanding tool permissions, MCP wrappers, write/edit/bash behavior, or permission overlay depth beyond mapper-visible event inputs.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| DEL-04-03-R-001 | The mapper MUST keep SDK messages separate from the browser contract; SDK messages are not browser `UIEvent`s. | Unit tests assert SDK input names do not appear as browser event names. |
| DEL-04-03-R-002 | The mapper MUST keep SDK messages separate from the canonical persisted event contract; SDK messages are not `HarnessEvent`s without translation. | Unit tests assert canonical event `type` values are Chirality-owned categories. |
| DEL-04-03-R-003 | The mapper MUST translate external message names, session IDs, tool names, permission modes, transcript paths, and hook names into Chirality-owned contracts or explicit adapter metadata fields. | Provider-neutral leakage tests inspect mapped outputs for unapproved top-level SDK fields. |
| DEL-04-03-R-004 | Browser-facing output MUST use the stable SSE / `UIEvent` event names already defined for turn streams: `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, and `process:exit`. | Compatibility fixture tests compare emitted event names against the SPEC/TYPES list. |
| DEL-04-03-R-005 | Persisted runtime output MUST use versioned `HarnessEvent` records with the fields defined by the target type. | Schema tests validate `schemaVersion`, `eventId`, `sessionId`, `timestamp`, `type`, and `data`, with optional turn/parent links. |
| DEL-04-03-R-006 | The mapper MUST support initial `HarnessEvent` categories for session, turn, SDK system initialization, model request, model delta, model completion, turn completion, turn failure, and turn cancellation where corresponding source inputs are present. | Unit tests cover each initial category with representative fixtures or mark probe-dependent fixtures as `TBD`. |
| DEL-04-03-R-007 | The mapper SHOULD prepare for later categories for tool, permission, hook, compaction, subagent, and SDK mirror error events without making unsupported cases appear complete. | Tests or TODO fixtures label probe-dependent categories as `TBD` pending DEL-04-01. |
| DEL-04-03-R-008 | The mapper MUST deterministically map SDK messages into UI and runtime events. | Golden fixture tests assert identical input sequences produce identical ordered output sequences. |
| DEL-04-03-R-009 | The mapper MUST mirror SDK model/tool loop activity into Chirality events when SDK supplies the model/tool loop. | Tests cover SDK tool-use, tool-result, permission-denial, hook, result, and compact-boundary inputs once probe fixtures are available. |
| DEL-04-03-R-010 | The mapper MUST NOT treat SDK transcripts as canonical project truth or canonical runtime events. | Tests assert transcript path/store linkage is metadata only and does not replace `HarnessEvent` output. |
| DEL-04-03-R-011 | The mapper MUST preserve route and SSE compatibility during SDK adoption. | Integration or adapter tests assert existing route event shapes remain readable by the UI. |
| DEL-04-03-R-012 | Runtime event outputs MUST be compatible with redaction policy; secrets and API key material must not be emitted by mapper outputs. | Redaction fixture tests include SDK error/tool payload examples and assert configured secret variants are absent. |
| DEL-04-03-R-013 | The mapper MUST expose enough terminal outcome information for success, failure, interruption, and cancellation to be persisted by the runtime event log. | Unit tests cover terminal inputs and resulting `turn.completed`, `turn.failed`, or `turn.cancelled` style outputs. |
| DEL-04-03-R-014 | ASSUMPTION: Exact SDK message payload fixtures will be derived from the DEL-04-01 SDK probe; until then, exact payload-field mappings remain `TBD`. | Open test fixture list references OI-001. |

## Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| Product-owned runtime boundary | SDK-backed adapter behavior must satisfy Chirality contracts rather than defining them. | REF-001 Sections 2.8-2.10; REF-003 Section 10 |
| Browser SSE event contract | UI mapping must preserve stable browser event names during SDK adoption. | REF-003 Section 11; REF-004 Section 7.4 |
| `HarnessEvent` target type | Runtime mapping must emit versioned, canonical Chirality events. | REF-004 Section 7.3; REF-003 Section 10 |
| SDK adapter vocabulary boundary | SDK terms remain adapter-boundary metadata. | REF-004 Section 9 |
| PRD FR-074 / FR-116 / FR-083 | Event separation, deterministic SDK message mapping, and SDK model/tool loop mirroring. | REF-006 Section 8.12 and 8.13, HASH_MISMATCH warning applies |
| Section 9 validation IDs | Runtime validation should include `section9.sdk_message_mapper`. | REF-003 Section 19.3 |

## Verification

| Verification Item | Method | Status |
|---|---|---|
| UI event compatibility | Golden tests for browser event names and payload shape. | TBD implementation |
| Runtime event schema | Schema tests for `HarnessEvent` output fields and category values. | TBD implementation |
| Determinism | Same SDK fixture sequence produces same ordered UI/runtime event outputs. | TBD implementation |
| Provider-neutral leakage | Tests fail on unapproved SDK-shaped top-level fields, public event names, or canonical event types. | TBD implementation |
| Probe-backed SDK categories | Fixtures populated from DEL-04-01 SDK probe for exact message sequence and payloads. | BLOCKED/TBD by OI-001 |
| Redaction compatibility | Mapper output examples exclude API keys and configured secret variants. | TBD implementation |
| Conformance integration | Engine conformance suite includes mapper coverage before SDK-backed adapter becomes production default. | TBD implementation |

## Documentation

Required documentation and artifacts:

- `sdk-message-mapper.ts` or equivalent implementation file.
- Mapper fixture documentation describing supported input categories and their source/probe basis.
- Mapper tests covering UI output and runtime event output.
- Provider-neutral leakage tests.
- A `TBD` or open-issue list for any SDK message category not yet confirmed by DEL-04-01.
- Section 9 validation coverage entry for `section9.sdk_message_mapper` when validation IDs are implemented.
