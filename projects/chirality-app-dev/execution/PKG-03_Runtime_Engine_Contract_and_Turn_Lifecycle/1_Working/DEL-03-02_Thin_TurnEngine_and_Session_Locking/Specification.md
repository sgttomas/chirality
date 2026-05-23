# Specification: DEL-03-02 Thin TurnEngine and Session Locking

## Scope

This deliverable moves the harness turn lifecycle, session binding, boot metadata forwarding, and active-turn locking behind `TurnEngine` while keeping `/api/harness/turn` as a thin SSE transport adapter.

In scope:

- `TurnEngine.runTurn()` as the product-owned lifecycle surface outside HTTP.
- Session-level active-turn locking and `TURN_IN_PROGRESS` behavior.
- Binding active session, normalized project root, persona, mode, resolved runtime options, content blocks, attachment summaries, and cancellation signal into `TurnInput`.
- Preserving browser-facing SSE event names while SDK/provider behavior stays behind adapter boundaries.
- Persisting accepted-turn and terminal turn records through the runtime event surface.
- Lock cleanup tests and session lifecycle tests.

Out of scope:

- SDK-specific message translation details, assigned to adjacent adapter deliverables.
- Full interrupt/cancel terminal semantics beyond the lock cleanup and cancellation-signal boundary, which overlap DEL-03-04.
- Canonical session folder migration, assigned to PKG-05.
- New user-visible write, bash, remote MCP, plugin, domain-operation, or subagent capability.

Sources: `_CONTEXT.md` Deliverable Scope and Package Scope; `docs/SPEC.md` Sections 10.1-10.4 and 17.1; `docs/PLAN.md` R1; `docs/PRD.md` FR-070-FR-071.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| DEL-03-02-REQ-001 | Implement a `TurnEngine` or equivalent runtime service that owns harness turn lifecycle and can be unit-tested without HTTP. | `docs/PRD.md` FR-070; `docs/TYPES.md` Section 7.1 | Unit test `TurnEngine.runTurn()` without route invocation. |
| DEL-03-02-REQ-002 | Invoke turn execution through `AgentEnginePort` / `RuntimeEngineContract`; SDK APIs must not define the public harness semantics. | `docs/SPEC.md` Sections 10.1-10.3; `docs/CONTRACT.md` K-ENGINE-1, K-ENGINE-4 | Engine boundary/conformance tests reject SDK-shaped public event/session/API leakage. |
| DEL-03-02-REQ-003 | Keep `/api/harness/turn` as a transport adapter responsible for request validation, session lock acquisition, forwarding input to `TurnEngine`, SSE writing, and cleanup. | `docs/SPEC.md` Section 10.4; `docs/PRD.md` FR-071 | Route integration test proves stable route behavior while lifecycle executes through `TurnEngine`. |
| DEL-03-02-REQ-004 | Enforce one active turn per session; concurrent turn attempts for the same session return `TURN_IN_PROGRESS`. | `docs/PRD.md` FR-018; decomposition SOW-011 | Lock concurrency test covers duplicate active-turn request. |
| DEL-03-02-REQ-005 | Ensure the session lock is released after normal completion, failure, cancellation cleanup, or route abort cleanup. | `docs/SPEC.md` Section 10.4; `docs/PRD.md` FR-019, FR-022; `docs/CONTRACT.md` K-EVENT-3 | Lock cleanup tests cover completion, failure, and cancellation/abort paths. Exact interrupt semantics TBD with DEL-03-04. |
| DEL-03-02-REQ-006 | Bind turn input to active session, normalized project root, persona, mode, resolved runtime options, content blocks, attachment summaries, and cancellation signal where applicable. | `docs/SPEC.md` Section 10.2; `docs/PRD.md` FR-015-FR-016 | Session lifecycle tests assert `TurnInput` construction and option forwarding. |
| DEL-03-02-REQ-007 | Preserve existing browser-facing SSE event names during SDK adoption and TurnEngine extraction. | `docs/SPEC.md` Section 11 and 17.1; `docs/PRD.md` FR-017, FR-071 | Route/SSE compatibility fixtures verify event names and stream media type. |
| DEL-03-02-REQ-008 | Persist `turn.accepted` before SDK/model/provider execution begins. | `docs/SPEC.md` Section 10.1; `docs/CONTRACT.md` K-EVENT-2; `docs/PRD.md` FR-021 | Unit/integration test asserts event write precedes engine adapter invocation. |
| DEL-03-02-REQ-009 | Persist durable terminal outcome events for success, failure, and cancellation. | `docs/CONTRACT.md` K-EVENT-3; `docs/PRD.md` FR-022 | Tests assert one terminal outcome for each accepted turn path. |
| DEL-03-02-REQ-010 | Keep browser `UIEvent`s separate from persisted `HarnessEvent`s; SDK messages are not the browser contract and not the canonical persisted event contract. | `docs/SPEC.md` Sections 9, 10.3, 11; `docs/CONTRACT.md` K-EVENT-1 | Event schema and mapper tests verify separation. |
| DEL-03-02-REQ-011 | Preserve legacy session readability while this slice interacts with active sessions. | `docs/SPEC.md` Section 8.1; `docs/PRD.md` FR-077 | Session lifecycle tests include legacy-readable session metadata where current code supports it. |
| DEL-03-02-REQ-012 | Do not enable new user-visible local tool capability as part of this slice. | `docs/PLAN.md` R1 Acceptance; `docs/PRD.md` R1 Acceptance | Regression check confirms no new write/bash/subagent/domain capability is exposed by route refactor. |

## Standards

| Standard / Contract Surface | Applicability |
|---|---|
| `docs/SPEC.md` Section 8 | Session metadata and canonicalization context for active session binding. |
| `docs/SPEC.md` Section 9 | `HarnessEvent` shape and append-only event semantics relevant to accepted-turn and terminal event persistence. |
| `docs/SPEC.md` Section 10 | Runtime engine contract, target type, adapter rules, and thin route rule. |
| `docs/SPEC.md` Section 11 | Browser SSE event names and compatibility rule. |
| `docs/SPEC.md` Section 17.1 | Harness API route shape stability. |
| `docs/CONTRACT.md` K-CORE, K-ENGINE, K-EVENT | Product-owned runtime semantics, SDK isolation, accepted-turn persistence, terminal outcomes, and UI/runtime event separation. |
| `docs/TYPES.md` Section 7 | Canonical vocabulary for `TurnEngine`, `AgentEnginePort`, `UIEvent`, `HarnessEvent`, session IDs, and SDK metadata. |
| `docs/PRD.md` | Product requirements used with source-state warning because `_REFERENCES.md` records `HASH_MISMATCH`. |

## Verification

Minimum verification set:

- Unit test `TurnEngine.runTurn()` can execute without HTTP and uses a stub `AgentEnginePort`.
- Unit or integration test proves concurrent turn on same session returns `TURN_IN_PROGRESS`.
- Lock cleanup tests cover normal completion, adapter failure, route abort/cancellation cleanup, and subsequent turn acceptance.
- Acceptance evidence for route abort/cancellation cleanup is limited in this slice to lock release and subsequent turn acceptance. Full interrupt/cancel terminal mapping remains a DEL-03-04 dependency and must not be claimed closed by DEL-03-02 alone.
- Session lifecycle tests cover session binding, boot metadata forwarding, runtime option forwarding, and normalized project root preservation.
- Event ordering test proves `turn.accepted` is persisted before engine adapter execution.
- Terminal outcome tests prove success, failure, and cancellation each produce exactly one durable terminal event.
- Route/SSE compatibility tests preserve `/api/harness/turn` shape, `text/event-stream`, and existing event names.
- Provider-neutral leakage test proves SDK-specific identifiers/names remain adapter metadata and do not define public APIs, `UIEvent`s, or canonical `HarnessEvent`s.

ASSUMPTION: exact test runner, fixture paths, and function names will follow existing frontend test conventions; no source slice identifies the current local test file layout.

## Documentation

Required documentation/artifacts for this deliverable:

- `turn-engine.ts` or equivalent runtime service file.
- Lock cleanup tests.
- Session lifecycle tests.
- Notes or inline docs identifying route responsibilities that remain in `/api/harness/turn` versus lifecycle responsibilities moved to `TurnEngine`.
- Any residual `TBD` decisions around lock storage, interrupt/cancel ownership, and exact session manager API.

Source-state warning:

- `_REFERENCES.md` records `docs/PRD.md` as `HASH_MISMATCH`; PRD requirements are used as accessible current source content but should be revalidated before closure.
- Closure blocker: PRD-derived requirements remain source-state-warning content until REF-006 hash reconciliation is accepted or the mismatch is explicitly carried forward by a human ruling.
