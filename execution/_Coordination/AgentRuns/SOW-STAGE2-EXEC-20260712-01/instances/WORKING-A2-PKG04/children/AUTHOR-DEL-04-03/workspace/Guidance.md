# Guidance: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation

## Purpose

This deliverable exists to create a narrow SDK adapter mapping surface: SDK stream messages can power the runtime, but Chirality's browser stream and persisted runtime events remain product-owned, stable, and provider-neutral. The mapper is one of the control points that prevents SDK defaults, transcript shape, message names, or tool names from silently redefining Chirality behavior.

## Principles

1. Keep SDK shape at the adapter boundary.
   - SDK message names, tool names, permission modes, transcript paths, and session IDs are implementation metadata. They may be retained only where explicitly modeled as adapter metadata.

2. Preserve the browser contract.
   - Browser `UIEvent`s are compact and stable. The mapper should emit only the established SSE event names unless a later governed UI compatibility change accepts an addition.

3. Preserve the canonical runtime contract.
   - Persisted `HarnessEvent`s are Chirality-owned records. They may include richer runtime detail than UI events, but the event schema and category vocabulary must remain product-owned.

4. Treat SDK transcripts as secondary.
   - SDK transcript paths, store keys, and session IDs support resume/debugging. They do not replace append-only Chirality events.

5. Map deterministically.
   - Given the same SDK message sequence and the same mapper version, output ordering and event categories should be stable. If SDK concurrent tool activity complicates ordering, preserve source order or explicitly document the ordering rule.

6. Fail closed on unknown provider shape.
   - Unknown SDK message categories should become structured mapper errors, `TBD` probe cases, or safe diagnostic runtime events only when that behavior is accepted by the runtime contract. They should not leak raw SDK payloads into public contracts.

7. Keep redaction upstream and downstream in view.
   - The mapper should not be the only redaction boundary, but it must avoid copying secrets from SDK errors, tool outputs, or provider metadata into UI/runtime events.

## Considerations

| Topic | Guidance | Source Basis |
|---|---|---|
| UI versus audit detail | Use UI events for compact browser streaming; use `HarnessEvent`s for richer runtime records such as model, tool, permission, hook, terminal, and SDK metadata events. | REF-003 Sections 10-11; REF-004 Sections 7.3-7.4 |
| first-adapter probe dependency | The exact SDK message categories and payload fields remain dependent on DEL-04-01 / OI-001. Design fixture gaps as explicit `TBD`s rather than guessing payload details. | Decomposition SOW-044 / OI-001 |
| Probe-backed category promotion slot | After DEL-04-01 / OI-001 is accepted, update this deliverable's mapper fixtures and documentation with the observed SDK message categories that are supported inputs. Until then, the currently named SDK-side categories remain warning-qualified and must not be treated as accepted observed payload schemas. | REF-006 FR-116 and FR-123, HASH_MISMATCH warning applies; decomposition OI-001 |
| Provider neutrality | Prefer Chirality terms for public event names and canonical event types. Use adapter metadata for values like `sdkSessionId`, `sdkTranscriptPath`, and SDK tool names. | REF-001 Section 2.10; REF-004 Section 9 |
| Error handling | Convert SDK/provider failures into Chirality terminal or diagnostic events that preserve operator meaning without exposing secrets. | REF-006 FR-075, HASH_MISMATCH warning applies |
| Test strategy | Start with SPEC/TYPES event contracts and PRD/decomposition requirements; add probe-derived fixtures after DEL-04-01 confirms real SDK streams. | REF-003 Section 19.3; REF-005 R1 acceptance |

## Trade-offs

| Trade-off | Preferred Direction | Rationale |
|---|---|---|
| Raw SDK passthrough versus translation | Translate. | Raw passthrough would make SDK shape part of the product contract. |
| Rich UI stream versus compact UI stream | Keep UI compact. | SPEC and TYPES define stable browser event names; richer audit detail belongs in `HarnessEvent`s. |
| Early broad category support versus probe-backed precision | Use explicit `TBD`s for unconfirmed cases. | SOW-044 is marked open until the first-adapter probe confirms categories. |
| Mapper-local redaction versus central redaction only | Do both where practical. | Event records and logs must not expose API keys or secrets; mapper copying should be conservative. |
| SDK session data omitted versus captured as metadata | Capture only explicit metadata. | Resume/debug linkage is useful, but SDK identifiers remain adapter metadata. |

## Adapter Metadata Rationale

SDK identifiers, transcript paths, tool names, permission modes, hook names, and provider identifiers are useful for resume, diagnosis, conformance, and audit review, but they are not Chirality identity or event vocabulary. Keep them in explicit adapter metadata because REF-001 Sections 2.8-2.10 and REF-003 Section 10 make the runtime boundary, `UIEvent` schema, `HarnessEvent` schema, permission semantics, session canonicality, and audit mirror product-owned. REF-004 Section 9 also names SDK terms as adapter-boundary vocabulary. This allows the mapper to preserve needed implementation detail while leakage tests can reject SDK-shaped public event names, canonical event types, or top-level fields.

## Examples

Illustrative mappings, subject to DEL-04-01 probe confirmation:

| SDK-side input category | Browser `UIEvent` direction | `HarnessEvent` direction | Notes |
|---|---|---|---|
| SDK system/session initialization | `session:init` if the UI needs session start metadata | `sdk.system.init` with adapter metadata | Exact payload fields TBD pending first-adapter probe. |
| Partial assistant text | `chat:delta` | `model.delta` | Preserve text ordering; avoid embedding raw SDK message object. |
| Assistant completion/result | `chat:complete` or `session:complete` as appropriate | `model.completed` and/or `turn.completed` | Terminal split depends on TurnEngine contract. |
| Tool result/progress | `tool:result` for compact UI feedback | `tool.progress`, `tool.completed`, or `tool.failed` | Later category support should be fixture-backed. |
| Permission denial | `turn:error` only if it is turn-terminal or UI-actionable | `tool.permission` or `turn.failed` depending on contract | Capability-forward policy with explicit hard-deny precedence semantics are owned by policy, not the SDK name. |
| Compact boundary | Usually no direct UI event unless UI compatibility accepts it | `context.compacted` | Probe exact SDK compact message shape. |
| Subagent lifecycle | TBD for UI | `subagent.started` / `subagent.completed` | Governed subagent support is later-phase and must remain restricted. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| B-001 | REF-006 `docs/PRD.md` is accessible but has a recorded hash mismatch, while production documents use PRD-derived runtime and SDK-message requirements. This is a source-state conflict/blocker, not a resolved content contradiction. | `_REFERENCES.md` REF-006 status | REF-006 Sections 8.12 and 8.13 as cited by current production documents | Datasheet references and conditions; Specification requirements/standards; Guidance considerations/examples; Procedure prerequisites | Continue using PRD-derived slices only with HASH_MISMATCH warning and keep probe-dependent details as `TBD` until source reconciliation and DEL-04-01 / OI-001 acceptance. | TBD |
