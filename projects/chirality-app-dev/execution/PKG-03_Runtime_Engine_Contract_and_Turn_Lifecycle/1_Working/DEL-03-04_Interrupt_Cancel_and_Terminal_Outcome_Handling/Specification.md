# Specification: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

## Scope

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

Source basis: `_CONTEXT.md`; `docs/PRD.md` Section 8.3 and 8.12; `docs/SPEC.md` Sections 9 through 11; decomposition DEL-03-04 row.

## Requirements

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

## Standards

| Standard / Contract | Applicability | Source |
|---|---|---|
| Product-owned runtime boundary | Terminal behavior belongs behind `AgentEnginePort` / `RuntimeEngineContract`; SDK APIs do not define public semantics. | `docs/CONTRACT.md` Section 1.4, K-ENGINE-1; `docs/SPEC.md` Section 10 |
| Runtime event and audit mirror contract | Terminal outcomes are persisted as Chirality `HarnessEvent`s in append-only JSONL. | `docs/CONTRACT.md` Section 1.5; `docs/SPEC.md` Section 9 |
| Browser SSE compatibility contract | Existing browser event names remain compatible during SDK adoption. | `docs/SPEC.md` Section 11 |
| Route adapter rule | `/api/harness/turn` validates, locks, forwards to `TurnEngine`, writes SSE, and handles cleanup without owning runtime policy. | `docs/SPEC.md` Section 10.4 |
| Source-state status | `docs/PRD.md` is reconciled under the current D-APP-38 authority corpus; PRD-derived terminal-outcome requirements are accepted for this tranche. | `_REFERENCES.md` REF-006; D-APP-38 |

## Verification

| Requirement IDs | Verification Approach |
|---|---|
| DEL-03-04-REQ-001, DEL-03-04-REQ-002, DEL-03-04-REQ-003, DEL-03-04-REQ-007 | API/integration test for `/api/harness/interrupt` during an active turn; assert provider/model abort through the product-owned runtime boundary, interrupted `process:exit` SSE behavior, and absence of SDK-shaped names in public API or event assertions. |
| DEL-03-04-REQ-004, DEL-03-04-REQ-011, DEL-03-04-REQ-014 | Terminal trigger matrix test covering successful completion, user interrupt, client disconnect, runtime/provider failure, and cancellation signal; assert each terminal path releases active-turn state through the selected observable hook/state API. |
| DEL-03-04-REQ-005, DEL-03-04-REQ-006, DEL-03-04-REQ-008, DEL-03-04-REQ-009 | Event-log replay test that simulates failure/cancellation after `turn.accepted`, appends or simulates a malformed trailing JSONL line after valid records, then confirms accepted input plus terminal outcome remain recoverable and diagnostics surface. |
| DEL-03-04-REQ-006A, DEL-03-04-REQ-007, DEL-03-04-REQ-013 | Mapper/unit tests using fixture cases for completion, failure, cancellation, and explicit interruption provider/runtime signals; assert Chirality-owned `UIEvent` / `HarnessEvent` outputs and keep provider-specific values only as adapter metadata where needed. |
| DEL-03-04-REQ-010 | SSE compatibility fixture asserting current event names remain stable: `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, `process:exit`. |
| DEL-03-04-REQ-012 | Redaction test for terminal failure/error payloads, including provider error surfaces, runtime events, run logs, and tool artifacts; assert no API keys or configured secret variants are persisted. |
| DEL-03-04-REQ-014 | Unit or integration tests around `TurnEngine`/route cleanup observability; exact hook or state API is TBD and must be resolved before implementation closure. |

## Documentation

Required artifacts for this deliverable:

- Interrupt tests.
- Cancel cleanup tests.
- Terminal event mapper.
- Mapper-facing terminal outcome documentation should cite D-APP-40 for explicit user interruption as `turn.interrupted`.

Records to update or cross-link when implementation lands:

- Runtime contract or mapper docs, exact path TBD.
- Section 9 validation coverage for runtime engine event log and session replay, exact validation IDs from `docs/SPEC.md` Section 19.3.
- Test fixtures demonstrating lock release and terminal outcome persistence.

## D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-117 names the landed observability basis: `RunningHarnessTurn.cancel`, post-terminal same-session acceptance, and lock-release/terminal-outcome tests. The former exact-hook/state-API TBD is retired.
