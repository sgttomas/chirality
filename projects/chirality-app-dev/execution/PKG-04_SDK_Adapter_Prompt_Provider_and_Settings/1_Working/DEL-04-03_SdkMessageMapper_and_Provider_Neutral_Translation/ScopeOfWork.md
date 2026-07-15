---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-03
package_id: PKG-04
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4
project_scope_refs: [SOW-040, SOW-044, SOW-051]
package_objective_refs: [OBJ-002, OBJ-004]
---

# Scope of Work — DEL-04-03

## Purpose and Objective Traceability

This Scope of Work defines `DEL-04-03` in service of project scope [SOW-040, SOW-044, SOW-051] and package objectives [OBJ-002, OBJ-004].

- **OUT-001** — Lossless SOW_V1 representation of the DEL-04-03 legacy production contract, traceable to SOW-040, SOW-044, SOW-051, OBJ-002, and OBJ-004.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation

> #### Datasheet: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | Deliverable ID | DEL-04-03 |
> | Deliverable Name | SdkMessageMapper and Provider-Neutral Translation |
> | Package ID | PKG-04 |
> | Package Name | SDK Adapter, Prompt, Provider, and Settings |
> | Decomposition Variant | SOFTWARE_DECOMP |
> | Decomposition Revision | v3.2 |
> | Type | BACKEND_FEATURE_SLICE |
> | Responsible Party | TBD |
> | Context Envelope | M |
> | Current Source State | REF-006 `docs/PRD.md` has `HASH_MISMATCH`; this run treats it as a source-state warning per task brief. |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary implementation artifact | `sdk-message-mapper.ts` | `_CONTEXT.md`; decomposition DEL-04-03 |
> | Test artifacts | Mapper tests; provider-neutral leakage tests | `_CONTEXT.md`; decomposition DEL-04-03 |
> | Scope items covered | SOW-040, SOW-044, SOW-051 | `_CONTEXT.md`; decomposition DEL-04-03 |
> | Supported objectives | OBJ-002, OBJ-004 | `_CONTEXT.md`; decomposition DEL-04-03 |
> | Browser-facing output contract | Compact `UIEvent`s / SSE events: `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, `process:exit` | REF-003 Section 11; REF-004 Section 7.4 |
> | Persisted runtime output contract | Versioned `HarnessEvent` records with `schemaVersion`, `eventId`, `sessionId`, optional `turnId`, optional `parentEventId`, `timestamp`, `type`, and `data` | REF-003 Section 10; REF-004 Section 7.3 |
> | SDK-specific data posture | SDK message names, session IDs, transcript paths, permission modes, hook names, and tool names remain adapter metadata, not public Chirality contracts | REF-001 Sections 2.8-2.10; REF-003 Section 10.3; REF-004 Section 9 |
> | Known SDK input categories | `SDKSystemMessage`, `SDKAssistantMessage`, `SDKPartialAssistantMessage`, `SDKResultMessage`, permission-denial, hook, compact-boundary, tool-progress, and subagent messages | REF-006 Section 8.12, source-state warning applies |
> | Exact observed SDK message sequence | TBD pending DEL-04-01 first-adapter probe / OI-001; current named categories are planning targets until probe-backed fixtures are accepted. | Decomposition OI-001; SOW-044; REF-006 FR-116, HASH_MISMATCH warning applies |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Route compatibility | Existing `/api/harness/turn` route shapes and SSE event names remain stable during SDK adoption. | REF-003 Sections 10.4 and 11; REF-006 Section 8.12 |
> | Runtime boundary | Mapping operates behind `AgentEnginePort` / `RuntimeEngineContract`; SDK APIs do not define public semantics. | REF-003 Section 10; REF-001 Section 2.8 |
> | Event separation | Browser `UIEvent`s and persisted `HarnessEvent`s are separate contracts. | SOW-040; REF-003 Sections 10.3 and 11; REF-006 FR-074 |
> | SDK model/tool loop | SDK supplies the model/tool loop when conformance passes; Chirality mirrors SDK tool-use, tool-result, permission-denial, hook, result, and compact-boundary messages into events. | SOW-051; REF-006 FR-083 |
> | Redaction boundary | Runtime event data and logs must not expose API keys or configured secret variants. | REF-006 FR-075; REF-005 Section 6.3 |
> | Conformance boundary | SDK-backed adapter must pass engine conformance tests before production default use. | REF-003 Section 10.3 |
> | Dependency state | `Dependencies.csv` exists with 11 ACTIVE extracted rows; satisfaction remains `TBD` for all rows, including ACTIVE upstream execution dependencies DEL-04-01, DEL-03-01, DEL-03-03, and DEL-04-02. | `_DEPENDENCIES.md`; `Dependencies.csv` |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component | Expected Construction |
> |---|---|
> | Mapper module | A backend module, anticipated as `sdk-message-mapper.ts`, that translates SDK stream/message inputs into Chirality-owned `UIEvent` and `HarnessEvent` outputs. |
> | UI mapping surface | A deterministic mapping to the stable browser SSE event names without exposing SDK message names in the browser contract. |
> | Runtime-event mapping surface | A deterministic mapping to versioned `HarnessEvent` categories, including model, tool, permission, hook, compact-boundary, terminal, and SDK metadata records where source-supported. |
> | Adapter metadata handling | SDK-specific identifiers and paths appear only under explicit adapter metadata fields or equivalent confined metadata structures. |
> | Leakage tests | Tests assert that public APIs, UI events, and canonical runtime events do not become SDK-shaped. |
> | Probe-dependent cases | ASSUMPTION: cases for exact SDK message payload shapes will be completed after DEL-04-01 confirms observed SDK message categories. |
>

### CLM-006 — References

> ##### References
>
> | RefID | Source Slice Used |
> |---|---|
> | REF-001 | `docs/DIRECTIVE.md` Sections 2.8, 2.9, 2.10 and the decision record table covering product-owned contracts, provider-neutral core, SDK metadata posture, and audit mirror canonicality. |
> | REF-003 | `docs/SPEC.md` Sections 10, 11, 12, 14, 15, and 19.3 covering runtime engine boundary, SSE events, SDK settings, tool surface, permission mapping, and validation IDs. |
> | REF-004 | `docs/TYPES.md` Sections 7.1, 7.2, 7.3, 7.4, and 9 covering `SdkMessageMapper`, `HarnessEvent`, `UIEvent`, SDK transcript, and adapter vocabulary. |
> | REF-005 | `docs/PLAN.md` R1 targets and Section 6.3 covering `sdk-message-mapper.ts`, event mapping, and redaction. |
> | REF-006 | `docs/PRD.md` Sections 8.12 and 8.13, used with HASH_MISMATCH warning per task brief. |
> | DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-04-03, SOW-040, SOW-044, SOW-051, OBJ-002, OBJ-004, and OI-001. |

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation

> #### Specification: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation
>

### CLM-008 — Scope

> ##### Scope
>
> This deliverable specifies the backend mapping surface that translates SDK stream messages into stable browser `UIEvent`s and provider-neutral persisted `HarnessEvent`s without allowing SDK message shapes, provider identifiers, transcript paths, or tool names to define Chirality's public or canonical contracts.
>
> In scope:
>
> - `sdk-message-mapper.ts` or equivalent mapper module.
> - Deterministic mapping from SDK message categories to browser-facing `UIEvent`s.
> - Deterministic mapping from SDK message categories to versioned `HarnessEvent`s.
> - Mapper tests and provider-neutral leakage tests.
> - Handling of SDK session and transcript linkage only as adapter metadata when relevant to mapped events.
> - Mapping hooks for SDK tool-use, tool-result, permission-denial, hook, result, compact-boundary, terminal, and subagent lifecycle messages where source-supported.
>
> Out of scope:
>
> - Defining the product-owned `AgentEnginePort` / `RuntimeEngineContract` itself; that is owned by DEL-03-01.
> - Persisting the append-only JSONL event log; that is owned by PKG-05, with this deliverable supplying mapping outputs compatible with it.
> - Building SDK options and settings isolation; that is owned by DEL-04-02.
> - Confirming exact SDK package behavior and message sequence; that is owned by DEL-04-01 / OI-001.
> - Expanding tool permissions, MCP wrappers, write/edit/bash behavior, or permission overlay depth beyond mapper-visible event inputs.
>

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Verification |
> |---|---|---|
> | DEL-04-03-REQ001 | The mapper MUST keep SDK messages separate from the browser contract; SDK messages are not browser `UIEvent`s. | Unit tests assert SDK input names do not appear as browser event names. |
> | DEL-04-03-REQ002 | The mapper MUST keep SDK messages separate from the canonical persisted event contract; SDK messages are not `HarnessEvent`s without translation. | Unit tests assert canonical event `type` values are Chirality-owned categories. |
> | DEL-04-03-REQ003 | The mapper MUST translate external message names, session IDs, tool names, permission modes, transcript paths, and hook names into Chirality-owned contracts or explicit adapter metadata fields. | Provider-neutral leakage tests inspect mapped outputs for unapproved top-level SDK fields. |
> | DEL-04-03-REQ004 | Browser-facing output MUST use the stable SSE / `UIEvent` event names already defined for turn streams: `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, and `process:exit`. | Compatibility fixture tests compare emitted event names against the SPEC/TYPES list. |
> | DEL-04-03-REQ005 | Persisted runtime output MUST use versioned `HarnessEvent` records with the fields defined by the target type. | Schema tests validate `schemaVersion`, `eventId`, `sessionId`, `timestamp`, `type`, and `data`, with optional turn/parent links. |
> | DEL-04-03-REQ006 | The mapper MUST support initial `HarnessEvent` categories for session, turn, SDK system initialization, model request, model delta, model completion, turn completion, turn failure, and turn cancellation where corresponding source inputs are present. | Unit tests cover each initial category with representative fixtures or mark probe-dependent fixtures as `TBD`. |
> | DEL-04-03-REQ007 | The mapper SHOULD prepare for later categories for tool, permission, hook, compaction, subagent, and SDK mirror error events without making unsupported cases appear complete. | Tests or TODO fixtures label probe-dependent categories as `TBD` pending DEL-04-01. |
> | DEL-04-03-REQ008 | The mapper MUST deterministically map SDK messages into UI and runtime events. | Golden fixture tests assert identical input sequences produce identical ordered output sequences. |
> | DEL-04-03-REQ009 | The mapper MUST mirror SDK model/tool loop activity into Chirality events when SDK supplies the model/tool loop. | Tests cover SDK tool-use, tool-result, permission-denial, hook, result, and compact-boundary inputs once probe fixtures are available. |
> | DEL-04-03-REQ010 | The mapper MUST NOT treat SDK transcripts as canonical project truth or canonical runtime events. | Tests assert transcript path/store linkage is metadata only and does not replace `HarnessEvent` output. |
> | DEL-04-03-REQ011 | The mapper MUST preserve route and SSE compatibility during SDK adoption. | Integration or adapter tests assert existing route event shapes remain readable by the UI. |
> | DEL-04-03-REQ012 | Runtime event outputs MUST be compatible with redaction policy; secrets and API key material must not be emitted by mapper outputs. | Redaction fixture tests include SDK error/tool payload examples and assert configured secret variants are absent. |
> | DEL-04-03-REQ013 | The mapper MUST expose enough terminal outcome information for success, failure, interruption, and cancellation to be persisted by the runtime event log, but it MUST NOT own upstream `TurnEngine` lock cleanup, cancellation-source classification, or accepted-turn persistence semantics. | Unit tests cover mapper-owned terminal inputs and resulting `turn.completed`, `turn.failed`, or `turn.cancelled` style outputs; integration/conformance tests owned by `TurnEngine` prove accepted-turn persistence, interrupt/cancel cleanup, and terminal durability. |
> | DEL-04-03-REQ014 | ASSUMPTION: Exact SDK message payload fixtures will be derived from the DEL-04-01 first-adapter probe; until then, exact payload-field mappings remain `TBD`. | Open test fixture list references OI-001. |
>

### CLM-010 — Standards

> ##### Standards
>
> | Standard / Contract | Applicability | Source |
> |---|---|---|
> | Product-owned runtime boundary | SDK-backed adapter behavior must satisfy Chirality contracts rather than defining them. | REF-001 Sections 2.8-2.10; REF-003 Section 10 |
> | Browser SSE event contract | UI mapping must preserve stable browser event names during SDK adoption. | REF-003 Section 11; REF-004 Section 7.4 |
> | `HarnessEvent` target type | Runtime mapping must emit versioned, canonical Chirality events. | REF-004 Section 7.3; REF-003 Section 10 |
> | SDK adapter vocabulary boundary | SDK terms remain adapter-boundary metadata. | REF-004 Section 9 |
> | PRD FR-074 / FR-116 / FR-083 | Event separation, deterministic Provider/SDK message mapping, and SDK model/tool loop mirroring. | REF-006 Section 8.12 and 8.13, HASH_MISMATCH warning applies |
> | Section 9 validation IDs | Runtime validation includes the active ID `section9.adapter_message_mapper`; older `section9.sdk_message_mapper` wording is superseded by ADQ-04 reconciliation. | REF-003 Section 19.3; `frontend/scripts/validate-harness-section9.mjs`; `docs/harness/runtime_evidence_reconciliation.md` |
>

### CLM-011 — Verification

> ##### Verification
>
> | Verification Item | Method | Status |
> |---|---|---|
> | UI event compatibility | Golden tests for browser event names and payload shape. | TBD implementation |
> | Runtime event schema | Schema tests for `HarnessEvent` output fields and category values. | TBD implementation |
> | Determinism | Same SDK fixture sequence produces same ordered UI/runtime event outputs. | TBD implementation |
> | Provider-neutral leakage | Tests fail on unapproved SDK-shaped top-level fields, public event names, or canonical event types. | TBD implementation |
> | Probe-backed SDK categories | Fixtures populated from DEL-04-01 first-adapter probe for exact message sequence and payloads. | BLOCKED/TBD by OI-001 |
> | Redaction compatibility | Mapper output examples exclude API keys and configured secret variants. | TBD implementation |
> | Conformance integration | Engine conformance suite includes mapper coverage before SDK-backed adapter becomes production default. | TBD implementation |
> | Terminal boundary ownership | Mapper unit tests verify translation from supported terminal SDK/runtime inputs to Chirality terminal event categories; `TurnEngine` integration/conformance tests verify cancellation source, client disconnect cleanup, accepted-turn survival, and durable terminal persistence. | TBD implementation; source-supported by REF-002 K-EVENT-2/K-EVENT-3, REF-003 Sections 9-10, REF-005 R1 acceptance, and REF-006 FR-022/FR-123; REF-006 HASH_MISMATCH warning applies |
>

### CLM-012 — Documentation

> ##### Documentation
>
> Required documentation and artifacts:
>
> - `sdk-message-mapper.ts` or equivalent implementation file.
> - Mapper fixture documentation describing supported input categories and their source/probe basis.
> - Mapper tests covering UI output and runtime event output.
> - Provider-neutral leakage tests.
> - A `TBD` or open-issue list for any SDK message category not yet confirmed by DEL-04-01.
> - Section 9 validation coverage entry for `section9.adapter_message_mapper`, the current implemented mapper validation ID.
>

### CLM-013 — D-APP-56 event-lane amendment (2026-07-12)

> ##### D-APP-56 event-lane amendment (2026-07-12)
>
> R4-P34 adds the `message.delta`, `message.completed`, and `queue.enqueued` lane emitted by `sdk-message-mapper.ts` to the REQ-006 event-category mapping, parallel to the existing `model.*` lane.

- **AC-001** — The conversion preserves and traces all legacy source content for DEL-04-03 to SOW-040, SOW-044, SOW-051, OBJ-002, and OBJ-004 without adding semantic scope, reliance claims, lifecycle meaning, or obligations.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation

> #### Procedure: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation
>

### CLM-015 — Purpose

> ##### Purpose
>
> Define the working procedure to implement and verify the `SdkMessageMapper` deliverable so SDK stream messages are translated into stable browser `UIEvent`s and provider-neutral `HarnessEvent`s without leaking SDK shape into Chirality core contracts.
>

### CLM-016 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status / Notes |
> |---|---|
> | Deliverable context | Available in `_CONTEXT.md`. |
> | Authoritative references | Available in `_REFERENCES.md`; REF-006 `docs/PRD.md` has HASH_MISMATCH and is used as a warning-qualified source per task brief. |
> | Accepted dependency register | `Dependencies.csv` exists with ACTIVE extracted edges, but all satisfaction statuses remain `TBD`; implementation closure should verify upstream satisfaction before closing this deliverable. |
> | Declared upstream dependencies | Extracted ACTIVE upstream execution dependencies include DEL-04-01, DEL-03-01, DEL-03-03, and DEL-04-02. Their satisfaction remains `TBD` in `_DEPENDENCIES.md` / `Dependencies.csv`. |
> | first-adapter probe results | TBD / pending DEL-04-01 and OI-001 for exact SDK message categories and payload fields. |
> | Engine contract target | Product-owned `AgentEnginePort` / `RuntimeEngineContract` is defined by PKG-03 / DEL-03-01, not by this deliverable. |
> | Runtime event schema target | `HarnessEvent` target type is available in REF-004 and REF-003. |
> | Browser event target | Stable browser SSE event names are available in REF-003 and REF-004. |
> | Implementation path discovery | Concrete mapper module path, UI/HarnessEvent type import paths, and mapper test locations are `TBD` until code discovery confirms the accepted backend/runtime layout. |
>

### CLM-017 — Steps

> ##### Steps
>
> 1. Confirm mapping boundaries.
>    - Read the accepted `AgentEnginePort` / `RuntimeEngineContract` once available.
>    - Confirm the mapper is an adapter component and not the owner of route policy, event persistence, SDK option construction, or permission enforcement.
>    - Before implementation closure, confirm `Dependencies.csv` has no unsatisfied blocker for the upstream runtime contract, SSE compatibility adapter, SDK options/settings isolation, or first-adapter probe evidence.
>
> 2. Create the mapper module.
>    - Add `sdk-message-mapper.ts` or equivalent in the accepted backend runtime location.
>    - Record the accepted mapper path, UI event type import path, `HarnessEvent` type import path, mapper unit-test path, and provider-neutral leakage-test path in implementation notes or fixture documentation once code discovery is complete.
>    - Define input types for SDK-side messages using probe-backed fixtures where available.
>    - Define output types for browser `UIEvent` and `HarnessEvent` results using Chirality-owned types.
>
> 3. Implement browser event mapping.
>    - Map assistant deltas, completions, session initialization, tool result summaries, terminal errors, and process completion into the stable SSE event names.
>    - Do not emit SDK message names as browser event names.
>    - Mark any unconfirmed SDK input shape as `TBD` until DEL-04-01 provides probe evidence.
>
> 4. Implement runtime event mapping.
>    - Emit versioned `HarnessEvent` records for accepted categories such as `sdk.system.init`, `model.request.started`, `model.delta`, `model.completed`, `turn.completed`, `turn.failed`, and `turn.cancelled` where inputs support them.
>    - Prepare explicit cases or fixture placeholders for later categories such as tool, permission, hook, compaction, subagent, and SDK mirror error events.
>    - Keep SDK-specific fields under explicit adapter metadata, not top-level canonical fields unless the schema accepts them.
>
> 5. Handle unknown and probe-dependent SDK inputs.
>    - For unknown categories, return a structured mapper error or safe diagnostic output according to the runtime contract.
>    - Do not pass raw SDK messages through to browser events or canonical runtime events.
>    - Record unconfirmed categories in a `TBD` fixture list tied to DEL-04-01 / OI-001.
>
> 6. Apply redaction-compatible handling.
>    - Avoid copying API keys, configured secret variants, provider error bodies, or raw tool output blobs into mapped events.
>    - Preserve enough non-secret metadata for diagnosis, replay, and terminal outcome handling.
>
> 7. Write mapper tests.
>    - Cover each stable browser event name expected from supported SDK input fixtures.
>    - Cover each supported `HarnessEvent` category and required schema field.
>    - Cover deterministic ordering for repeated runs over the same input sequence.
>    - Cover mapper-owned terminal success, failure, interruption, and cancellation translation cases.
>    - Leave accepted-turn persistence, client-disconnect cleanup, cancellation-source classification, lock cleanup, and terminal durability to `TurnEngine` / engine conformance tests; reference those results rather than duplicating ownership in the mapper.
>
> 8. Write provider-neutral leakage tests.
>    - Assert public event names are Chirality event names, not SDK message names.
>    - Assert canonical event types are Chirality categories, not SDK raw categories.
>    - Assert SDK session IDs, transcript paths, SDK tool names, and provider names appear only in approved adapter metadata locations.
>
> 9. Integrate with validation.
>    - Use `section9.adapter_message_mapper` as the active Section 9 runtime validation ID for mapper coverage.
>    - Ensure mapper tests are part of local premerge validation once the runtime validation suite lands.
>
> 10. Reconcile with first-adapter probe updates.
>    - When DEL-04-01 provides observed SDK message fixtures, replace `TBD` cases with probe-backed tests.
>    - If SDK behavior cannot support required product-owned mapping semantics, surface the issue through the reliance-boundary/fallback process rather than weakening provider neutrality.
>

### CLM-018 — Verification

> ##### Verification
>
> | Check | Expected Result |
> |---|---|
> | Four output categories | Mapper produces browser UI events, canonical runtime events, structured mapper errors, or explicit `TBD` probe cases; it does not raw-pass SDK messages. |
> | UI compatibility | Stable SSE event names remain unchanged. |
> | Runtime schema | `HarnessEvent` records validate against the target type. |
> | Provider-neutral leakage | No unapproved SDK-shaped top-level fields or event names appear in public/canonical outputs. |
> | Determinism | Identical SDK input fixtures produce identical ordered mapping outputs. |
> | Redaction | Secret-like values do not appear in mapper outputs. |
> | Probe completeness | All SDK categories named by the accepted probe have a mapping, structured rejection, or documented `TBD` requiring human/architecture action. |
>

### CLM-019 — Records

> ##### Records
>
> Expected records and evidence from implementation:
>
> - `sdk-message-mapper.ts` or equivalent implementation.
> - Mapper unit tests.
> - Provider-neutral leakage tests.
> - Fixture files or inline fixtures derived from DEL-04-01 first-adapter probe outputs.
> - `TBD` list for SDK message categories or payload fields not yet confirmed.
> - Section 9 validation entry or follow-up for `section9.adapter_message_mapper`.
> - Notes on any fallback or reliance-boundary concerns if SDK behavior cannot be mapped without weakening Chirality-owned contracts.
> - Implementation path record naming the accepted mapper module, UI/HarnessEvent type import paths, mapper unit-test path, and provider-neutral leakage-test path.
> - Dependency closure note confirming whether ACTIVE upstream dependencies remain `TBD`, blocked, or satisfied at implementation closeout.

- **VER-001** — Validate the candidate schema and exact identity/reference bindings, then verify complete source-marker coverage and byte-for-byte source text parity against the four manifest-bound legacy documents.

## Governing Values and Decisions — Axiology

### CLM-020 — Guidance: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation

> #### Guidance: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation
>

### CLM-021 — Purpose

> ##### Purpose
>
> This deliverable exists to create a narrow SDK adapter mapping surface: SDK stream messages can power the runtime, but Chirality's browser stream and persisted runtime events remain product-owned, stable, and provider-neutral. The mapper is one of the control points that prevents SDK defaults, transcript shape, message names, or tool names from silently redefining Chirality behavior.
>

### CLM-022 — Principles

> ##### Principles
>
> 1. Keep SDK shape at the adapter boundary.
>    - SDK message names, tool names, permission modes, transcript paths, and session IDs are implementation metadata. They may be retained only where explicitly modeled as adapter metadata.
>
> 2. Preserve the browser contract.
>    - Browser `UIEvent`s are compact and stable. The mapper should emit only the established SSE event names unless a later governed UI compatibility change accepts an addition.
>
> 3. Preserve the canonical runtime contract.
>    - Persisted `HarnessEvent`s are Chirality-owned records. They may include richer runtime detail than UI events, but the event schema and category vocabulary must remain product-owned.
>
> 4. Treat SDK transcripts as secondary.
>    - SDK transcript paths, store keys, and session IDs support resume/debugging. They do not replace append-only Chirality events.
>
> 5. Map deterministically.
>    - Given the same SDK message sequence and the same mapper version, output ordering and event categories should be stable. If SDK concurrent tool activity complicates ordering, preserve source order or explicitly document the ordering rule.
>
> 6. Fail closed on unknown provider shape.
>    - Unknown SDK message categories should become structured mapper errors, `TBD` probe cases, or safe diagnostic runtime events only when that behavior is accepted by the runtime contract. They should not leak raw SDK payloads into public contracts.
>
> 7. Keep redaction upstream and downstream in view.
>    - The mapper should not be the only redaction boundary, but it must avoid copying secrets from SDK errors, tool outputs, or provider metadata into UI/runtime events.
>

### CLM-023 — Considerations

> ##### Considerations
>
> | Topic | Guidance | Source Basis |
> |---|---|---|
> | UI versus audit detail | Use UI events for compact browser streaming; use `HarnessEvent`s for richer runtime records such as model, tool, permission, hook, terminal, and SDK metadata events. | REF-003 Sections 10-11; REF-004 Sections 7.3-7.4 |
> | first-adapter probe dependency | The exact SDK message categories and payload fields remain dependent on DEL-04-01 / OI-001. Design fixture gaps as explicit `TBD`s rather than guessing payload details. | Decomposition SOW-044 / OI-001 |
> | Probe-backed category promotion slot | After DEL-04-01 / OI-001 is accepted, update this deliverable's mapper fixtures and documentation with the observed SDK message categories that are supported inputs. Until then, the currently named SDK-side categories remain warning-qualified and must not be treated as accepted observed payload schemas. | REF-006 FR-116 and FR-123, HASH_MISMATCH warning applies; decomposition OI-001 |
> | Provider neutrality | Prefer Chirality terms for public event names and canonical event types. Use adapter metadata for values like `sdkSessionId`, `sdkTranscriptPath`, and SDK tool names. | REF-001 Section 2.10; REF-004 Section 9 |
> | Error handling | Convert SDK/provider failures into Chirality terminal or diagnostic events that preserve operator meaning without exposing secrets. | REF-006 FR-075, HASH_MISMATCH warning applies |
> | Test strategy | Start with SPEC/TYPES event contracts and PRD/decomposition requirements; add probe-derived fixtures after DEL-04-01 confirms real SDK streams. | REF-003 Section 19.3; REF-005 R1 acceptance |
>

### CLM-024 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Preferred Direction | Rationale |
> |---|---|---|
> | Raw SDK passthrough versus translation | Translate. | Raw passthrough would make SDK shape part of the product contract. |
> | Rich UI stream versus compact UI stream | Keep UI compact. | SPEC and TYPES define stable browser event names; richer audit detail belongs in `HarnessEvent`s. |
> | Early broad category support versus probe-backed precision | Use explicit `TBD`s for unconfirmed cases. | SOW-044 is marked open until the first-adapter probe confirms categories. |
> | Mapper-local redaction versus central redaction only | Do both where practical. | Event records and logs must not expose API keys or secrets; mapper copying should be conservative. |
> | SDK session data omitted versus captured as metadata | Capture only explicit metadata. | Resume/debug linkage is useful, but SDK identifiers remain adapter metadata. |
>

### CLM-025 — Adapter Metadata Rationale

> ##### Adapter Metadata Rationale
>
> SDK identifiers, transcript paths, tool names, permission modes, hook names, and provider identifiers are useful for resume, diagnosis, conformance, and audit review, but they are not Chirality identity or event vocabulary. Keep them in explicit adapter metadata because REF-001 Sections 2.8-2.10 and REF-003 Section 10 make the runtime boundary, `UIEvent` schema, `HarnessEvent` schema, permission semantics, session canonicality, and audit mirror product-owned. REF-004 Section 9 also names SDK terms as adapter-boundary vocabulary. This allows the mapper to preserve needed implementation detail while leakage tests can reject SDK-shaped public event names, canonical event types, or top-level fields.
>

### CLM-026 — Examples

> ##### Examples
>
> Illustrative mappings, subject to DEL-04-01 probe confirmation:
>
> | SDK-side input category | Browser `UIEvent` direction | `HarnessEvent` direction | Notes |
> |---|---|---|---|
> | SDK system/session initialization | `session:init` if the UI needs session start metadata | `sdk.system.init` with adapter metadata | Exact payload fields TBD pending first-adapter probe. |
> | Partial assistant text | `chat:delta` | `model.delta` | Preserve text ordering; avoid embedding raw SDK message object. |
> | Assistant completion/result | `chat:complete` or `session:complete` as appropriate | `model.completed` and/or `turn.completed` | Terminal split depends on TurnEngine contract. |
> | Tool result/progress | `tool:result` for compact UI feedback | `tool.progress`, `tool.completed`, or `tool.failed` | Later category support should be fixture-backed. |
> | Permission denial | `turn:error` only if it is turn-terminal or UI-actionable | `tool.permission` or `turn.failed` depending on contract | Capability-forward policy with explicit hard-deny precedence semantics are owned by policy, not the SDK name. |
> | Compact boundary | Usually no direct UI event unless UI compatibility accepts it | `context.compacted` | Probe exact SDK compact message shape. |
> | Subagent lifecycle | TBD for UI | `subagent.started` / `subagent.completed` | Governed subagent support is later-phase and must remain restricted. |
>

### CLM-027 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | B-001 | REF-006 `docs/PRD.md` is accessible but has a recorded hash mismatch, while production documents use PRD-derived runtime and SDK-message requirements. This is a source-state conflict/blocker, not a resolved content contradiction. | `_REFERENCES.md` REF-006 status | REF-006 Sections 8.12 and 8.13 as cited by current production documents | Datasheet references and conditions; Specification requirements/standards; Guidance considerations/examples; Procedure prerequisites | Continue using PRD-derived slices only with HASH_MISMATCH warning and keep probe-dependent details as `TBD` until source reconciliation and DEL-04-01 / OI-001 acceptance. | TBD |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-040 SOW-044 SOW-051 OBJ-002 OBJ-004 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
