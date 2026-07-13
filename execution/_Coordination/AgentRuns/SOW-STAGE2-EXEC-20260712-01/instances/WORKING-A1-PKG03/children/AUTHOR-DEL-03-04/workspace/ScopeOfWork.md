---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-04
package_id: PKG-03
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
project_scope_refs: [SOW-012, SOW-015]
package_objective_refs: [OBJ-002, OBJ-003]
---

# Scope of Work — DEL-03-04

## Purpose and Objective Traceability

This migration candidate defines `DEL-03-04` in service of project scope [SOW-012, SOW-015] and package objectives [OBJ-002, OBJ-003].

- **OUT-001** — Interrupt tests, cancel cleanup tests, and a terminal event mapper for DEL-03-04 interrupt, cancellation/disconnect cleanup, lock release, and durable terminal outcomes.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":2,"line_start":1,"source_sha256":"ebe381d7c4bfe65882393ba7d13806521e765b8408f77648c9cd3871e59163a8","target_id":"CLM-001"} -->
#### Datasheet: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

<!-- sow-source-end -->

### CLM-002 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":19,"line_start":3,"source_sha256":"ebe381d7c4bfe65882393ba7d13806521e765b8408f77648c9cd3871e59163a8","target_id":"CLM-002"} -->
##### Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-03-04 |
| DeliverableName | Interrupt, Cancel, and Terminal Outcome Handling |
| PackageID | PKG-03 |
| PackageName | Runtime Engine Contract and Turn Lifecycle |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | BACKEND_FEATURE_SLICE |
| ResponsibleParty | TBD |
| ContextEnvelope | M |
| CoversScopeItems | SOW-012, SOW-015 |
| SupportsObjectives | OBJ-002, OBJ-003 |
| AnticipatedArtifacts | Interrupt tests; cancel cleanup tests; terminal event mapper |

<!-- sow-source-end -->

### CLM-003 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":34,"line_start":20,"source_sha256":"ebe381d7c4bfe65882393ba7d13806521e765b8408f77648c9cd3871e59163a8","target_id":"CLM-003"} -->
##### Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary runtime owner | `TurnEngine` owns the harness turn lifecycle; `/api/harness/turn` remains a transport adapter. | `docs/PRD.md` Section 8.12, FR-070 and FR-071; `docs/SPEC.md` Section 10.4 |
| Engine boundary | `AgentEnginePort` / `RuntimeEngineContract` is the product-owned boundary for turn execution, UI events, canonical `HarnessEvent`s, interrupt behavior, and terminal outcomes. | `docs/PRD.md` Section 6.1; `docs/SPEC.md` Section 10.1 |
| Public interrupt route | `/api/harness/interrupt` interrupts the active turn. | `docs/PRD.md` Section 8.3, FR-019; `docs/SPEC.md` Section 17.1 |
| Turn stream route | `/api/harness/turn` executes a turn and streams browser-facing UI events over SSE. | `docs/PRD.md` Section 8.3, FR-017; `docs/SPEC.md` Section 17.1 |
| Session concurrency constraint | Only one active turn may run per session; concurrent attempts return `TURN_IN_PROGRESS`. | `docs/PRD.md` Section 8.3, FR-018 |
| Accepted-turn durability | Accepted user input must be persisted before model/provider execution so an interrupted or killed turn is recoverable. | `docs/PRD.md` Section 8.3, FR-021; `docs/CONTRACT.md` Section 1.5, K-EVENT-2 |
| Terminal outcome durability | Every accepted turn must end with a durable success, failure, cancellation, or interruption outcome. | `docs/CONTRACT.md` Section 1.5, K-EVENT-3; `docs/PRD.md` Section 8.3, FR-022; `docs/SPEC.md` Section 10.1 |
| Product-owned audit mirror | `.chirality/sessions/<id>/events.jsonl` is the canonical Chirality runtime audit mirror; SDK transcripts are secondary unless imported into `HarnessEvent` form. | `docs/CONTRACT.md` Section 1.5, K-EVENT-4; `docs/SPEC.md` Section 8.4 |
| Browser event compatibility | Existing SSE event names must remain compatible during SDK adoption. | `docs/SPEC.md` Section 11 |
| PRD source state | `docs/PRD.md` is accessible but hash-mismatched against `_REFERENCES.md`; use as source-state warning, not as rejection. | `_REFERENCES.md` REF-006 |

<!-- sow-source-end -->

### CLM-004 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":45,"line_start":35,"source_sha256":"ebe381d7c4bfe65882393ba7d13806521e765b8408f77648c9cd3871e59163a8","target_id":"CLM-004"} -->
##### Conditions

| Condition | Required Handling | Source |
|---|---|---|
| User interrupt | `POST /api/harness/interrupt` aborts the active provider request, yields interrupted `process:exit`, and persists `turn.interrupted` for explicit user interruption. | `docs/PRD.md` Section 8.3, FR-019; `docs/PRD.md` Section 7.4; D-APP-40 |
| Client disconnect | Stream cleanup must occur; once the event log exists, client disconnect cleanup must record cancellation. | `docs/SPEC.md` Section 11 |
| Runtime/provider failure after input acceptance | Accepted input remains recoverable and replay shows terminal failure/cancellation status. | `docs/PRD.md` Section 7.10 |
| Concurrent turn attempt | Must not create a second active turn for the same session; return `TURN_IN_PROGRESS`. | `docs/PRD.md` Section 8.3, FR-018 |
| Malformed trailing event log write | Replay ignores malformed trailing lines and preserves valid prior events. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` Section 7.10 |
| Secret-bearing error or payload | Runtime events, logs, tool artifacts, and provider errors must redact secrets and avoid storing API keys. | `docs/CONTRACT.md` Section 1.5, K-EVENT-6; `docs/SPEC.md` Section 9.2 |

<!-- sow-source-end -->

### CLM-005 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":55,"line_start":46,"source_sha256":"ebe381d7c4bfe65882393ba7d13806521e765b8408f77648c9cd3871e59163a8","target_id":"CLM-005"} -->
##### Construction

| Component / Artifact | Construction Target | Status |
|---|---|---|
| Interrupt tests | Cover active-turn interrupt route, provider abort propagation, SSE `process:exit`, lock release, and durable terminal outcome. | ASSUMPTION: exact test file path TBD |
| Cancel cleanup tests | Cover client disconnect and cancellation-signal cleanup, lock release, and durable cancellation record once event log exists. | ASSUMPTION: exact test file path TBD |
| Terminal event mapper | Map completion, failure, cancellation, and interruption handling into browser `UIEvent`s and persisted `HarnessEvent`s without SDK-shaped public semantics; explicit interruption uses `turn.interrupted`. | `frontend/src/lib/harness/claude-agent-sdk-manager.ts`; `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts`; D-APP-40 |
| Lock cleanup verification | Confirm interrupt, disconnect, failure, and cancellation all release session active-turn state. | Supported by DEL-03-04 scope and PRD FR-018/FR-019/FR-022 |
| Event log verification | Confirm terminal records append as newline-delimited JSONL with unique event IDs and no secrets. | `docs/SPEC.md` Section 9.2 |

<!-- sow-source-end -->

### CLM-006 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":62,"line_start":56,"source_sha256":"ebe381d7c4bfe65882393ba7d13806521e765b8408f77648c9cd3871e59163a8","target_id":"CLM-006"} -->
##### References

- `docs/CONTRACT.md` Section 1.4 and 1.5, especially K-ENGINE-1 through K-ENGINE-4 and K-EVENT-2 through K-EVENT-6.
- `docs/SPEC.md` Sections 8.4, 9, 10, 11, 17.1, 19.2, and 19.3.
- `docs/TYPES.md` Sections 7.1 through 7.4.
- `docs/PRD.md` Sections 5, 6.1, 7.4, 7.10, 8.3, and 8.12. REF-006 is reconciled under the current D-APP-38 authority corpus.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-03 / DEL-03-04 and SOW-012 / SOW-015 rows.
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":2,"line_start":1,"source_sha256":"e7b7f5930904c5e79fb35fb32c9ce551b22a4c0637d35789ee3928ecdc6a9834","target_id":"CLM-007"} -->
#### Specification: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

<!-- sow-source-end -->

### CLM-008 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":25,"line_start":3,"source_sha256":"e7b7f5930904c5e79fb35fb32c9ce551b22a4c0637d35789ee3928ecdc6a9834","target_id":"CLM-008"} -->
##### Scope

This deliverable specifies interrupt, client-disconnect, runtime-failure, cancellation, lock-release, and terminal-outcome behavior for the PKG-03 runtime lifecycle slice.

In scope:

- Handling user interrupt requests through `/api/harness/interrupt`.
- Ensuring active turn cleanup releases the per-session active-turn lock.
- Ensuring every accepted turn receives a durable terminal outcome where the event log is available.
- Preserving browser-facing SSE compatibility while terminal outcomes are mapped into product-owned `HarnessEvent`s.
- Producing interrupt tests, cancel cleanup tests, and a terminal event mapper.

Out of scope:

- SDK-specific message translation details, except where mapper behavior must preserve Chirality-owned event semantics.
- Broad session CRUD, boot metadata, and active-turn lock design assigned to DEL-03-02.
- Route-shape and general SSE compatibility documentation assigned to DEL-03-03.
- Append-only event store implementation assigned primarily to DEL-05-02, except as required to verify terminal outcomes for this slice.
- Durable terminal persistence by the deterministic UI-only stub adapter; its
  UI-visible terminal outcomes are test scaffolding, not K-EVENT-3 parity.

Source basis: `_CONTEXT.md`; `docs/PRD.md` Section 8.3 and 8.12; `docs/SPEC.md` Sections 9 through 11; decomposition DEL-03-04 row.

<!-- sow-source-end -->

### CLM-009 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":45,"line_start":26,"source_sha256":"e7b7f5930904c5e79fb35fb32c9ce551b22a4c0637d35789ee3928ecdc6a9834","target_id":"CLM-009"} -->
##### Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-03-04-REQ-001 | The implementation shall preserve the `/api/harness/interrupt` route as the public interrupt endpoint for active turns. | `docs/SPEC.md` Section 17.1; `docs/PRD.md` Section 8.3, FR-019 |
| DEL-03-04-REQ-002 | Interrupt handling shall abort the active provider/model request for the target session when one exists. | `docs/PRD.md` Section 8.3, FR-019; `docs/SPEC.md` Section 10.1 |
| DEL-03-04-REQ-003 | Interrupt handling shall yield an interrupted `process:exit` browser-facing event where an active SSE turn stream is present. | `docs/PRD.md` Section 8.3, FR-019; `docs/PRD.md` Section 7.4 |
| DEL-03-04-REQ-004 | Client disconnect cleanup shall release runtime turn resources and record cancellation once the event log exists. | `docs/SPEC.md` Section 11 |
| DEL-03-04-REQ-005 | Runtime failure after `turn.accepted` shall leave accepted user input recoverable and shall persist a terminal failure or cancellation status. | `docs/PRD.md` Section 7.10; `docs/CONTRACT.md` Section 1.5, K-EVENT-2 and K-EVENT-3 |
| DEL-03-04-REQ-006 | Every accepted turn shall terminate durably with a success, failure, cancellation, or interruption outcome. | `docs/CONTRACT.md` Section 1.5, K-EVENT-3; decomposition SOW-015 |
| DEL-03-04-REQ-006A | Explicit user interruption shall persist terminal `turn.interrupted`; `turn.cancelled` is reserved for non-user cancellation such as disconnect or system cancellation. | D-APP-40; `docs/SPEC.md` Section 9.3; `docs/TYPES.md` Section 7.3 |
| DEL-03-04-REQ-007 | Terminal outcome persistence shall use Chirality-owned `HarnessEvent` semantics, not SDK message names as public or canonical contracts. | `docs/CONTRACT.md` Section 1.4, K-ENGINE-4; `docs/SPEC.md` Section 10.3 |
| DEL-03-04-REQ-008 | Terminal event records shall follow the versioned `HarnessEvent` shape: `schemaVersion`, `eventId`, `sessionId`, optional `turnId`, optional `parentEventId`, `timestamp`, `type`, and `data`. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
| DEL-03-04-REQ-009 | Terminal event writes shall append newline-delimited JSONL, use unique event IDs, avoid secrets, and remain replayable when a malformed trailing line exists. | `docs/SPEC.md` Section 9.2 |
| DEL-03-04-REQ-010 | Browser-facing SSE event names shall remain compatible during the runtime pivot. | `docs/SPEC.md` Section 11 |
| DEL-03-04-REQ-011 | Interrupt, disconnect, failure, and cancellation paths shall release the active turn state so the session is not left in `TURN_IN_PROGRESS`. | `docs/PRD.md` Section 8.3, FR-018 and FR-019; decomposition SOW-012 |
| DEL-03-04-REQ-012 | Terminal outcome handling shall redact secrets and avoid storing API keys in runtime events, logs, provider errors, or tool artifacts. | `docs/CONTRACT.md` Section 1.5, K-EVENT-6; `docs/SPEC.md` Section 9.2 |
| DEL-03-04-REQ-013 | The terminal event mapper shall translate SDK/provider terminal signals into Chirality `UIEvent` and `HarnessEvent` terms at the adapter boundary. | `docs/SPEC.md` Section 10.3; `docs/TYPES.md` Section 7.4 |
| DEL-03-04-REQ-014 | ASSUMPTION: The implementation should expose testable cleanup hooks or observable active-turn state sufficient to prove lock release after interrupt, disconnect, failure, and cancellation; exact hook or state API remains TBD. | Decomposition anticipated artifacts; `docs/PRD.md` Section 8.3, FR-018 |

<!-- sow-source-end -->

### CLM-010 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":55,"line_start":46,"source_sha256":"e7b7f5930904c5e79fb35fb32c9ce551b22a4c0637d35789ee3928ecdc6a9834","target_id":"CLM-010"} -->
##### Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| Product-owned runtime boundary | Terminal behavior belongs behind `AgentEnginePort` / `RuntimeEngineContract`; SDK APIs do not define public semantics. | `docs/CONTRACT.md` Section 1.4, K-ENGINE-1; `docs/SPEC.md` Section 10 |
| Runtime event and audit mirror contract | Terminal outcomes are persisted as Chirality `HarnessEvent`s in append-only JSONL. | `docs/CONTRACT.md` Section 1.5; `docs/SPEC.md` Section 9 |
| Browser SSE compatibility contract | Existing browser event names remain compatible during SDK adoption. | `docs/SPEC.md` Section 11 |
| Route adapter rule | `/api/harness/turn` validates, locks, forwards to `TurnEngine`, writes SSE, and handles cleanup without owning runtime policy. | `docs/SPEC.md` Section 10.4 |
| Source-state status | `docs/PRD.md` is reconciled under the current D-APP-38 authority corpus; PRD-derived terminal-outcome requirements are accepted for this tranche. | `_REFERENCES.md` REF-006; D-APP-38 |

<!-- sow-source-end -->

### CLM-011 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":67,"line_start":56,"source_sha256":"e7b7f5930904c5e79fb35fb32c9ce551b22a4c0637d35789ee3928ecdc6a9834","target_id":"CLM-011"} -->
##### Verification

| Requirement IDs | Verification Approach |
|---|---|
| DEL-03-04-REQ-001, DEL-03-04-REQ-002, DEL-03-04-REQ-003, DEL-03-04-REQ-007 | API/integration test for `/api/harness/interrupt` during an active turn; assert provider/model abort through the product-owned runtime boundary, interrupted `process:exit` SSE behavior, and absence of SDK-shaped names in public API or event assertions. |
| DEL-03-04-REQ-004, DEL-03-04-REQ-011, DEL-03-04-REQ-014 | Terminal trigger matrix test covering successful completion, user interrupt, client disconnect, runtime/provider failure, and cancellation signal; assert each terminal path releases active-turn state through the selected observable hook/state API. |
| DEL-03-04-REQ-005, DEL-03-04-REQ-006, DEL-03-04-REQ-008, DEL-03-04-REQ-009 | Event-log replay test that simulates failure/cancellation after `turn.accepted`, appends or simulates a malformed trailing JSONL line after valid records, then confirms accepted input plus terminal outcome remain recoverable and diagnostics surface. |
| DEL-03-04-REQ-006A, DEL-03-04-REQ-007, DEL-03-04-REQ-013 | Mapper/unit tests using fixture cases for completion, failure, cancellation, and explicit interruption provider/runtime signals; assert Chirality-owned `UIEvent` / `HarnessEvent` outputs and keep provider-specific values only as adapter metadata where needed. |
| DEL-03-04-REQ-010 | SSE compatibility fixture asserting current event names remain stable: `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, `process:exit`. |
| DEL-03-04-REQ-012 | Redaction test for terminal failure/error payloads, including provider error surfaces, runtime events, run logs, and tool artifacts; assert no API keys or configured secret variants are persisted. |
| DEL-03-04-REQ-014 | Unit or integration tests around `TurnEngine`/route cleanup observability; exact hook or state API is TBD and must be resolved before implementation closure. |

<!-- sow-source-end -->

### CLM-012 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":82,"line_start":68,"source_sha256":"e7b7f5930904c5e79fb35fb32c9ce551b22a4c0637d35789ee3928ecdc6a9834","target_id":"CLM-012"} -->
##### Documentation

Required artifacts for this deliverable:

- Interrupt tests.
- Cancel cleanup tests.
- Terminal event mapper.
- Mapper-facing terminal outcome documentation should cite D-APP-40 for explicit user interruption as `turn.interrupted`.

Records to update or cross-link when implementation lands:

- Runtime contract or mapper docs, exact path TBD.
- Section 9 validation coverage for runtime engine event log and session replay, exact validation IDs from `docs/SPEC.md` Section 19.3.
- Test fixtures demonstrating lock release and terminal outcome persistence.

<!-- sow-source-end -->

### CLM-013 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":85,"line_start":83,"source_sha256":"e7b7f5930904c5e79fb35fb32c9ce551b22a4c0637d35789ee3928ecdc6a9834","target_id":"CLM-013"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-117 names the landed observability basis: `RunningHarnessTurn.cancel`, post-terminal same-session acceptance, and lock-release/terminal-outcome tests. The former exact-hook/state-API TBD is retired.
<!-- sow-source-end -->

- **AC-001** — The DEL-03-04 outputs preserve the public interrupt route and SSE compatibility, release active-turn state across terminal paths, persist Chirality-owned terminal outcomes for accepted turns, and redact secrets, as specified by the exact legacy source.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":2,"line_start":1,"source_sha256":"668f1b19d4f2cc9e97fd93ce6807c1d215042bba1f6eabde2d072d6414faeda3","target_id":"CLM-014"} -->
#### Procedure: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

<!-- sow-source-end -->

### CLM-015 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":8,"line_start":3,"source_sha256":"668f1b19d4f2cc9e97fd93ce6807c1d215042bba1f6eabde2d072d6414faeda3","target_id":"CLM-015"} -->
##### Purpose

Define the working procedure for producing and verifying the DEL-03-04 backend feature slice: interrupt handling, cancellation/disconnect cleanup, lock release, and terminal outcome persistence.

This procedure is for implementation and verification planning. It does not approve final runtime behavior; human review and normal change controls remain required.

<!-- sow-source-end -->

### CLM-016 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":31,"line_start":9,"source_sha256":"668f1b19d4f2cc9e97fd93ce6807c1d215042bba1f6eabde2d072d6414faeda3","target_id":"CLM-016"} -->
##### Prerequisites

Required source context:

- `_CONTEXT.md` for deliverable identity, scope, and anticipated artifacts.
- `_REFERENCES.md` for authoritative source corpus.
- `docs/CONTRACT.md` Section 1.4 and 1.5.
- `docs/SPEC.md` Sections 9, 10, 11, 17.1, 19.2, and 19.3.
- `docs/TYPES.md` Sections 7.1 through 7.4.
- `docs/PRD.md` Sections 7.4, 7.10, 8.3, and 8.12.
- Decomposition row for DEL-03-04 and SOW-012/SOW-015.

Declared upstream dependencies:

- TBD. `_DEPENDENCIES.md` reports no accepted upstream edges yet.

Implementation prerequisites:

- ASSUMPTION: DEL-03-01 should define or stabilize the `AgentEnginePort` / `RuntimeEngineContract` boundary before final mapper closure.
- ASSUMPTION: DEL-03-02 should provide testable active-turn locking and cleanup surfaces.
- ASSUMPTION: DEL-03-03 should preserve route shape and SSE compatibility fixtures.
- ASSUMPTION: DEL-05-02 should provide the append-only `HarnessEvent` JSONL writer or a compatible test seam.

<!-- sow-source-end -->

### CLM-017 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":89,"line_start":32,"source_sha256":"668f1b19d4f2cc9e97fd93ce6807c1d215042bba1f6eabde2d072d6414faeda3","target_id":"CLM-017"} -->
##### Steps

1. Confirm current runtime boundary.
   - Identify the active `TurnEngine`, `AgentEnginePort`, route adapter, and event writer surfaces.
   - Do not make SDK/provider message names part of public Chirality semantics.
   - Evidence target: source references to `docs/SPEC.md` Section 10 and `docs/CONTRACT.md` K-ENGINE invariants.

2. Define terminal trigger matrix.
   - List triggers: successful completion, user interrupt, client disconnect, runtime/provider failure, cancellation signal.
   - For each trigger, define required lock release, browser event behavior, and persisted runtime event behavior.
   - Use one evidence artifact for the trigger matrix so every terminal path is tied to lock-release proof, terminal outcome persistence, and replay expectations.
   - Apply D-APP-40: explicit user interruption persists terminal `turn.interrupted`; non-user cancellation uses `turn.cancelled`.

3. Implement or update interrupt handling.
   - Route: preserve `/api/harness/interrupt`.
   - Behavior: abort the active provider/model request for the session when present.
   - Stream effect: produce interrupted `process:exit` for an active browser stream where applicable.
   - Cleanup: release active-turn state.

4. Implement or update client-disconnect and cancellation cleanup.
   - Ensure SSE disconnect/cancellation signal handling reaches runtime cleanup.
   - Release active-turn state even when no final browser event can be delivered because the client disconnected.
   - Record cancellation once event-log support exists, and verify cleanup through state/event evidence rather than relying on receipt of a final browser SSE event.

5. Implement or update failure terminalization.
   - When execution fails after `turn.accepted`, write a terminal failure or cancellation record.
   - Preserve accepted input for replay.
   - Redact secrets from error payloads, runtime logs, and event data.

6. Implement terminal event mapping.
   - Map runtime/provider terminal signals into Chirality-owned `HarnessEvent` categories and compact browser `UIEvent`s.
   - Use the `HarnessEvent` shape from `docs/SPEC.md` Section 9.1.
   - Ensure event IDs are unique and JSONL writes append newline-delimited records.
   - Keep SDK-specific values only as explicit adapter metadata when needed.

7. Add interrupt tests.
   - Start or simulate an active turn.
   - Call `/api/harness/interrupt`.
   - Assert abort propagation, interrupted `process:exit`, active-turn lock release, and terminal outcome persistence.
   - Assert adapter-boundary behavior through Chirality-owned runtime/event terms; SDK/provider names may appear only as explicit adapter metadata.
   - Exact fixture/module path: TBD.

8. Add cancel cleanup tests.
   - Simulate SSE client disconnect and/or cancellation signal.
   - Assert active-turn lock release.
   - Assert cancellation record when the event log exists.
   - Exact fixture/module path: TBD.

9. Add terminal event mapper tests.
   - Cover fixture cases for completion, failure, non-user cancellation, and explicit user interruption.
   - Assert `UIEvent` names remain compatible.
   - Assert `HarnessEvent` output uses Chirality-owned event types and redacted data.
   - Exact fixture/module path: TBD.

10. Add replay-oriented verification.
    - Simulate malformed trailing JSONL after valid accepted-turn and terminal failure/cancellation records.
    - Assert replay preserves valid prior events, preserves terminal outcome evidence, and surfaces diagnostics.

<!-- sow-source-end -->

### CLM-018 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":104,"line_start":90,"source_sha256":"668f1b19d4f2cc9e97fd93ce6807c1d215042bba1f6eabde2d072d6414faeda3","target_id":"CLM-018"} -->
##### Verification

Minimum checks before this deliverable is considered implementation-ready:

| Check | Expected Result | Source |
|---|---|---|
| Interrupt route test | `/api/harness/interrupt` aborts active turn, yields interrupted `process:exit` where stream exists, releases lock, persists terminal outcome, and proves abort behavior without making SDK-shaped names part of the public contract. | `docs/PRD.md` Section 8.3, FR-019; `docs/CONTRACT.md` K-EVENT-3; `docs/SPEC.md` Section 10.3 |
| Terminal trigger matrix | One evidence artifact covers completion, interrupt, disconnect, runtime/provider failure, and cancellation signal; each row records lock-release proof, browser-event expectation, persisted runtime outcome expectation, and source reference. | `docs/PRD.md` Section 8.3, FR-018 and FR-019; `docs/SPEC.md` Section 10.1 |
| Disconnect cleanup test | SSE client disconnect releases active-turn state and records cancellation once event log exists; proof does not depend on delivering a final SSE event to the disconnected browser. | `docs/SPEC.md` Section 11 |
| Failure after acceptance test | `turn.accepted` remains replayable and a terminal failure/cancellation status is present. | `docs/PRD.md` Section 7.10 |
| Terminal mapper test | Completion, failure, cancellation, and explicit interruption fixtures map to Chirality `UIEvent` and `HarnessEvent` contracts, not SDK-shaped public semantics. | `docs/SPEC.md` Section 10.3; D-APP-40 |
| JSONL append/replay test | Terminal records append newline-delimited events; malformed trailing writes after a valid terminal record do not break replay of accepted input or terminal outcome evidence. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5 |
| Redaction test | API keys and configured secret variants do not appear in terminal events, runtime logs, provider errors, or tool artifacts. | `docs/CONTRACT.md` K-EVENT-6 |
| SSE compatibility test | Existing event names remain compatible: `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, `process:exit`, and `harness:event`. | `docs/SPEC.md` Section 11 |

<!-- sow-source-end -->

### CLM-019 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":115,"line_start":105,"source_sha256":"668f1b19d4f2cc9e97fd93ce6807c1d215042bba1f6eabde2d072d6414faeda3","target_id":"CLM-019"} -->
##### Records

Produce or update these records as part of implementation closure:

- Interrupt tests.
- Cancel cleanup tests.
- Terminal event mapper and mapper tests.
- Evidence that active-turn locks release after interrupt, disconnect, failure, and cancellation.
- Evidence that terminal outcomes persist in append-only `HarnessEvent` JSONL.
- D-APP-40 ruling record resolving DEL-03-04-CONFLICT-001.
- Any Section 9 validation updates for runtime engine event log, session replay, and runtime contract validation.
<!-- sow-source-end -->

- **VER-001** — Verify using the legacy source-defined interrupt, cancel cleanup, terminal trigger matrix, event mapper, replay, redaction, and SSE compatibility checks.

## Governing Values and Decisions — Axiology

### CLM-020 — Guidance: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":2,"line_start":1,"source_sha256":"5af43e9ade097532b111a027f616ccc870dfc1c9baff05e73792abfe53eada7b","target_id":"CLM-020"} -->
#### Guidance: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

<!-- sow-source-end -->

### CLM-021 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":10,"line_start":3,"source_sha256":"5af43e9ade097532b111a027f616ccc870dfc1c9baff05e73792abfe53eada7b","target_id":"CLM-021"} -->
##### Purpose

This deliverable exists to make runtime turn termination explicit, testable, and auditable. Interrupts, client disconnects, provider failures, and cancellations must not leave a session locked forever or leave an accepted turn without a durable terminal outcome.

The slice supports the PKG-03 runtime pivot: routes stay thin, `TurnEngine` owns lifecycle behavior, `AgentEnginePort` / `RuntimeEngineContract` protects product-owned semantics, and browser-facing SSE behavior remains compatible while richer runtime events are persisted.

Source basis: decomposition DEL-03-04 row; `docs/PRD.md` Sections 5, 6.1, 7.4, 7.10, 8.3, and 8.12; `docs/SPEC.md` Sections 9 through 11.

<!-- sow-source-end -->

### CLM-022 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":30,"line_start":11,"source_sha256":"5af43e9ade097532b111a027f616ccc870dfc1c9baff05e73792abfe53eada7b","target_id":"CLM-022"} -->
##### Principles

1. Persist before execution.
   Accepted input must be recorded before model/provider execution begins. This is the recovery anchor for killed, failed, or interrupted turns. Source: `docs/PRD.md` Section 8.3, FR-021; `docs/CONTRACT.md` Section 1.5, K-EVENT-2.

2. Termination is a contract, not incidental cleanup.
   Every accepted turn needs a durable terminal outcome. Cleanup code should be treated as part of the turn lifecycle, not a route-only afterthought. Source: `docs/CONTRACT.md` Section 1.5, K-EVENT-3; `docs/SPEC.md` Section 10.1.

3. Release locks in all terminal paths.
   Interrupt, client disconnect, provider failure, and cancellation are distinct triggers, but they share a session-liveness obligation: active-turn state must be released. Source: decomposition SOW-012; `docs/PRD.md` Section 8.3, FR-018 and FR-019.

4. Keep public semantics Chirality-owned.
   SDK/provider messages may inform mapping, but `UIEvent`, `HarnessEvent`, route behavior, and terminal outcome names must remain Chirality contracts. Source: `docs/CONTRACT.md` Section 1.4, K-ENGINE-4; `docs/SPEC.md` Section 10.3.

5. Preserve SSE compatibility.
   Browser event names are part of the compatibility surface. Terminal mapping can grow internally, but route streams must keep existing names compatible during SDK adoption. Source: `docs/SPEC.md` Section 11.

6. Treat runtime events as audit records, not project truth.
   Session logs explain what happened at runtime; they do not approve, issue, or certify deliverables. Source: `docs/PRD.md` Section 5; `docs/DIRECTIVE.md` Sections 3 and 8.

<!-- sow-source-end -->

### CLM-023 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":40,"line_start":31,"source_sha256":"5af43e9ade097532b111a027f616ccc870dfc1c9baff05e73792abfe53eada7b","target_id":"CLM-023"} -->
##### Considerations

- The terminal mapper should be small and deterministic. It should map completion, failure, cancellation, and interruption-adjacent provider signals into stable browser and runtime event outputs.
- The interrupt path should be tested while an active turn is streaming, because the required browser symptom is an interrupted `process:exit` event and an updated UI state.
- Client disconnect is not necessarily user intent to interrupt, but SPEC says disconnect cleanup must record cancellation once the event log exists. The implementation should avoid overstating disconnect as an explicit user cancellation unless the data model supports a reason field.
- Use "interruption" for the user-visible active-turn interrupt path and "cancellation" for non-user cancellation paths. D-APP-40 amends the runtime taxonomy so explicit user interruption persists `turn.interrupted`; `turn.cancelled` remains available for non-user cancellation such as disconnect/system cancellation.
- Terminal records must not store API keys, provider secrets, or raw error data that violates redaction policy.
- Replay tolerance matters for failure paths: malformed trailing JSONL should not hide valid prior events or the accepted input that preceded failure.
- `docs/PRD.md` is hash-mismatched in `_REFERENCES.md`. Use PRD content as an accessible source-state warning and reconfirm before closure of implementation work.

<!-- sow-source-end -->

### CLM-024 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":51,"line_start":41,"source_sha256":"5af43e9ade097532b111a027f616ccc870dfc1c9baff05e73792abfe53eada7b","target_id":"CLM-024"} -->
##### Trade-offs

| Topic | Option | Benefit | Risk / Constraint |
|---|---|---|---|
| Interruption taxonomy | Separate `turn.interrupted` event type | D-APP-40 selected this option; it directly matches decomposition and CONTRACT wording about interruption. | Requires schema/docs/tests to retain `turn.cancelled` only for non-user cancellation. |
| Interruption taxonomy | Represent interruption as `turn.cancelled` with a reason such as `interrupted` | Rejected by D-APP-40 for explicit user interruption. | May blur user interrupt versus transport/client cancellation unless reason semantics are explicit. |
| Cleanup ownership | Centralize terminal cleanup in `TurnEngine` | Keeps route thin and makes lifecycle behavior unit-testable. | Requires route adapter to reliably forward cancellation/disconnect signals. |
| Route-level fallback cleanup | Keep defensive cleanup in route adapter | Protects against transport errors and stream failures. | Can duplicate policy if terminal mapping is not centralized behind the runtime contract. |
| Event log write strictness | Fail closed on terminal event write failure | Avoids claiming terminal durability when no event exists. | Could make user-visible failures noisier; exact retry/fallback behavior is TBD. |
| Terminal write recovery | PROPOSAL: permit retry only when the event writer can prove idempotent append behavior through unique event IDs and replay diagnostics | Preserves the durable-terminal-outcome requirement while avoiding duplicate terminal records. | Exact retry/fallback behavior remains TBD pending event-writer design and human ruling. |

<!-- sow-source-end -->

### CLM-025 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":53,"line_start":52,"source_sha256":"5af43e9ade097532b111a027f616ccc870dfc1c9baff05e73792abfe53eada7b","target_id":"CLM-025"} -->
##### Examples

<!-- sow-source-end -->

### CLM-026 — User interrupt during active stream

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":64,"line_start":54,"source_sha256":"5af43e9ade097532b111a027f616ccc870dfc1c9baff05e73792abfe53eada7b","target_id":"CLM-026"} -->
###### User interrupt during active stream

1. A turn has already persisted `turn.accepted`.
2. The user calls `/api/harness/interrupt`.
3. The active provider/model request is aborted.
4. The browser stream receives interrupted `process:exit`.
5. The active-turn lock is released.
6. A terminal runtime outcome is persisted as `turn.interrupted`.

Sources: `docs/PRD.md` Section 7.4 and Section 8.3; `docs/CONTRACT.md` Section 1.5.

<!-- sow-source-end -->

### CLM-027 — Client disconnect

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":74,"line_start":65,"source_sha256":"5af43e9ade097532b111a027f616ccc870dfc1c9baff05e73792abfe53eada7b","target_id":"CLM-027"} -->
###### Client disconnect

1. `/api/harness/turn` is streaming SSE.
2. The client disconnects.
3. Cleanup releases active-turn state.
4. Once event logging exists, cancellation is recorded.
5. Replay preserves prior valid events and surfaces diagnostics if a trailing write is malformed.

Sources: `docs/SPEC.md` Section 11 and Section 9.2.

<!-- sow-source-end -->

### CLM-028 — Provider failure after acceptance

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":84,"line_start":75,"source_sha256":"5af43e9ade097532b111a027f616ccc870dfc1c9baff05e73792abfe53eada7b","target_id":"CLM-028"} -->
###### Provider failure after acceptance

1. Accepted user input is already durable.
2. Provider/model execution fails.
3. Terminal failure is mapped into Chirality-owned `HarnessEvent` form.
4. Browser error/exit behavior remains SSE-compatible.
5. Runtime replay can reconstruct accepted input and terminal failure/cancellation status.

Sources: `docs/PRD.md` Section 7.10; `docs/SPEC.md` Section 9.

<!-- sow-source-end -->

### CLM-029 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":90,"line_start":85,"source_sha256":"5af43e9ade097532b111a027f616ccc870dfc1c9baff05e73792abfe53eada7b","target_id":"CLM-029"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| DEL-03-04-CONFLICT-001 | Resolved by D-APP-40: explicit user interruption is a durable `turn.interrupted` terminal outcome; `turn.cancelled` is reserved for non-user cancellation. | `execution/_Coordination/_DECISIONS/D-APP-40_RULING_2026-06-21.md` | `docs/SPEC.md` Section 9.3; `docs/TYPES.md` Section 7.3; `docs/PRD.md` Section 8.3 FR-022 after ADQ-05 reconciliation | `Datasheet.md` Conditions; `Specification.md` Requirements and Verification; `Procedure.md` Steps and Verification | Apply D-APP-40 Option B. | Ruled 2026-06-21 |

<!-- sow-source-end -->

### CLM-030 — Source-State Notes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":95,"line_start":91,"source_sha256":"5af43e9ade097532b111a027f616ccc870dfc1c9baff05e73792abfe53eada7b","target_id":"CLM-030"} -->
##### Source-State Notes

- `docs/PRD.md` is current under the D-APP-38 authority corpus; this draft uses it as PRD-derived source text while keeping implementation proof separate.
- Exact code/module paths for interrupt tests, cancel cleanup tests, terminal event mapper, and lock-observability helpers are TBD because the authoritative source slices specify behavior and artifacts but not final file locations.

<!-- sow-source-end -->

### CLM-031 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":98,"line_start":96,"source_sha256":"5af43e9ade097532b111a027f616ccc870dfc1c9baff05e73792abfe53eada7b","target_id":"CLM-031"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-117 names the landed observability basis: `RunningHarnessTurn.cancel`, post-terminal same-session acceptance, and lock-release/terminal-outcome tests. The former exact-hook/state-API TBD is retired.
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-012 SOW-015 OBJ-002 OBJ-003 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
