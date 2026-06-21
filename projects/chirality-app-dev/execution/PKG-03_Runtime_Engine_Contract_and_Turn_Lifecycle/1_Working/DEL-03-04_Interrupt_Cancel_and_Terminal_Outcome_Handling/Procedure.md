# Procedure: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

## Purpose

Define the working procedure for producing and verifying the DEL-03-04 backend feature slice: interrupt handling, cancellation/disconnect cleanup, lock release, and terminal outcome persistence.

This procedure is for implementation and verification planning. It does not approve final runtime behavior; human review and normal change controls remain required.

## Prerequisites

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

## Steps

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

## Verification

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

## Records

Produce or update these records as part of implementation closure:

- Interrupt tests.
- Cancel cleanup tests.
- Terminal event mapper and mapper tests.
- Evidence that active-turn locks release after interrupt, disconnect, failure, and cancellation.
- Evidence that terminal outcomes persist in append-only `HarnessEvent` JSONL.
- D-APP-40 ruling record resolving DEL-03-04-CONFLICT-001.
- Any Section 9 validation updates for runtime engine event log, session replay, and runtime contract validation.
