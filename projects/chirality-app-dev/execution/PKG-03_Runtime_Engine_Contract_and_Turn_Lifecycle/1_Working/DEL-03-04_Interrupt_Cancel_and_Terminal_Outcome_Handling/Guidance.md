# Guidance: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

## Purpose

This deliverable exists to make runtime turn termination explicit, testable, and auditable. Interrupts, client disconnects, provider failures, and cancellations must not leave a session locked forever or leave an accepted turn without a durable terminal outcome.

The slice supports the PKG-03 runtime pivot: routes stay thin, `TurnEngine` owns lifecycle behavior, `AgentEnginePort` / `RuntimeEngineContract` protects product-owned semantics, and browser-facing SSE behavior remains compatible while richer runtime events are persisted.

Source basis: decomposition DEL-03-04 row; `docs/PRD.md` Sections 5, 6.1, 7.4, 7.10, 8.3, and 8.12; `docs/SPEC.md` Sections 9 through 11.

## Principles

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

## Considerations

- The terminal mapper should be small and deterministic. It should map completion, failure, cancellation, and interruption-adjacent provider signals into stable browser and runtime event outputs.
- The interrupt path should be tested while an active turn is streaming, because the required browser symptom is an interrupted `process:exit` event and an updated UI state.
- Client disconnect is not necessarily user intent to interrupt, but SPEC says disconnect cleanup must record cancellation once the event log exists. The implementation should avoid overstating disconnect as an explicit user cancellation unless the data model supports a reason field.
- Use "interruption" for the user-visible active-turn interrupt path and "cancellation" for the schema-compatible terminal category unless a human ruling amends SPEC/TYPES to add `turn.interrupted`. If interruption is encoded as `turn.cancelled`, reason metadata must preserve the distinction without changing public SSE event names.
- Terminal records must not store API keys, provider secrets, or raw error data that violates redaction policy.
- Replay tolerance matters for failure paths: malformed trailing JSONL should not hide valid prior events or the accepted input that preceded failure.
- `docs/PRD.md` is hash-mismatched in `_REFERENCES.md`. Use PRD content as an accessible source-state warning and reconfirm before closure of implementation work.

## Trade-offs

| Topic | Option | Benefit | Risk / Constraint |
|---|---|---|---|
| Interruption taxonomy | Separate `turn.interrupted` event type | Directly matches decomposition and CONTRACT wording about interruption. | SPEC/TYPES initial event categories do not currently list `turn.interrupted`; adding it may require schema amendment. |
| Interruption taxonomy | Represent interruption as `turn.cancelled` with a reason such as `interrupted` | Aligns with SPEC/TYPES initial categories and client-disconnect cancellation wording. | May blur user interrupt versus transport/client cancellation unless reason semantics are explicit. |
| Cleanup ownership | Centralize terminal cleanup in `TurnEngine` | Keeps route thin and makes lifecycle behavior unit-testable. | Requires route adapter to reliably forward cancellation/disconnect signals. |
| Route-level fallback cleanup | Keep defensive cleanup in route adapter | Protects against transport errors and stream failures. | Can duplicate policy if terminal mapping is not centralized behind the runtime contract. |
| Event log write strictness | Fail closed on terminal event write failure | Avoids claiming terminal durability when no event exists. | Could make user-visible failures noisier; exact retry/fallback behavior is TBD. |
| Terminal write recovery | PROPOSAL: permit retry only when the event writer can prove idempotent append behavior through unique event IDs and replay diagnostics | Preserves the durable-terminal-outcome requirement while avoiding duplicate terminal records. | Exact retry/fallback behavior remains TBD pending event-writer design and human ruling. |

## Examples

### User interrupt during active stream

1. A turn has already persisted `turn.accepted`.
2. The user calls `/api/harness/interrupt`.
3. The active provider/model request is aborted.
4. The browser stream receives interrupted `process:exit`.
5. The active-turn lock is released.
6. A terminal runtime outcome is persisted. Exact event type for interruption is TBD pending conflict resolution.

Sources: `docs/PRD.md` Section 7.4 and Section 8.3; `docs/CONTRACT.md` Section 1.5.

### Client disconnect

1. `/api/harness/turn` is streaming SSE.
2. The client disconnects.
3. Cleanup releases active-turn state.
4. Once event logging exists, cancellation is recorded.
5. Replay preserves prior valid events and surfaces diagnostics if a trailing write is malformed.

Sources: `docs/SPEC.md` Section 11 and Section 9.2.

### Provider failure after acceptance

1. Accepted user input is already durable.
2. Provider/model execution fails.
3. Terminal failure is mapped into Chirality-owned `HarnessEvent` form.
4. Browser error/exit behavior remains SSE-compatible.
5. Runtime replay can reconstruct accepted input and terminal failure/cancellation status.

Sources: `docs/PRD.md` Section 7.10; `docs/SPEC.md` Section 9.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| DEL-03-04-CONFLICT-001 | Terminal taxonomy for interruption is not fully aligned: some sources describe interruption as a durable terminal outcome, while SPEC/TYPES initial event categories list `turn.completed`, `turn.failed`, and `turn.cancelled` but not `turn.interrupted`. | `docs/CONTRACT.md` Section 1.5 K-EVENT-3; decomposition SOW-012/SOW-015; `docs/PRD.md` Section 7.4 and FR-019 | `docs/SPEC.md` Section 9.3; `docs/TYPES.md` Section 7.3; `docs/PRD.md` Section 8.3 FR-022 | `Datasheet.md` Conditions; `Specification.md` Requirements and Verification; `Procedure.md` Steps and Verification | Treat interruption as a terminal outcome requirement, but implement event schema as either `turn.cancelled` with explicit reason metadata or amend SPEC/TYPES to add `turn.interrupted` before final implementation closure. | TBD |

## Source-State Notes

- `docs/PRD.md` is accessible but has `HASH_MISMATCH` in `_REFERENCES.md`; this draft uses it because the task explicitly directed treating that mismatch as a source-state warning.
- Exact code/module paths for interrupt tests, cancel cleanup tests, terminal event mapper, and lock-observability helpers are TBD because the authoritative source slices specify behavior and artifacts but not final file locations.
