# Procedure: DEL-03-02 Thin TurnEngine and Session Locking

## Purpose

Define the operational procedure to implement and verify the DEL-03-02 slice: extract a thin `TurnEngine`, preserve route/SSE compatibility, enforce session-level active-turn locking, bind session/boot metadata into turn input, and prove cleanup behavior.

Sources: `_CONTEXT.md` Deliverable Scope; `docs/SPEC.md` Sections 10.1-10.4, 11, 17.1, 19.2-19.3; `docs/PRD.md` FR-014-FR-022, FR-070-FR-077; `docs/PLAN.md` R1.

## Prerequisites

| Prerequisite | Status / Note |
|---|---|
| Accepted source basis for runtime engine boundary and route rule | Available in `docs/SPEC.md` Sections 10 and 17.1. |
| Runtime vocabulary | Available in `docs/TYPES.md` Section 7. |
| Product/runtime invariants | Available in `docs/CONTRACT.md` K-CORE, K-ENGINE, K-EVENT. |
| PRD runtime requirements | Available in `docs/PRD.md`, but `_REFERENCES.md` records `HASH_MISMATCH`; revalidate before closure. |
| Declared upstream dependencies | TBD - `_DEPENDENCIES.md` has no accepted dependency edges yet. |
| Current route/session implementation path | TBD - not specified by the authoritative source corpus for this drafting pass. |
| Existing test conventions | TBD - not specified by the authoritative source corpus for this drafting pass. |

## Steps

1. Locate the current `/api/harness/turn` implementation and current session manager/lock behavior.

   Output: code pointers for route validation, active-turn guard, provider/engine invocation, SSE writing, and cleanup.  
   Verification: no implementation changes yet; mapping notes distinguish current route responsibilities from target `TurnEngine` responsibilities.

2. Define the `TurnEngine` input/output boundary.

   Include active session, normalized project root, persona, mode, resolved runtime options, content blocks, attachment summaries, and cancellation signal where applicable.  
   Source: `docs/SPEC.md` Section 10.2.  
   Verification: type/unit test can construct valid `TurnInput` without HTTP request objects.

3. Implement `TurnEngine.runTurn()` as the lifecycle owner outside HTTP.

   `TurnEngine` should invoke `AgentEnginePort.runTurn(input)` or equivalent product-owned engine boundary and yield browser-facing `UIEvent`s.  
   Source: `docs/PRD.md` FR-070; `docs/SPEC.md` Section 10.1.  
   Verification: unit test runs `TurnEngine.runTurn()` with a stub adapter and no route invocation.

4. Refactor `/api/harness/turn` into a transport adapter.

   Keep route responsibilities limited to request validation, session lock acquisition, attachment option forwarding, SSE encoding, cancellation cleanup, and error response handling.  
   Source: `docs/SPEC.md` Section 10.4; `docs/PRD.md` FR-071.  
   Verification: integration test confirms route shape and `text/event-stream` response remain compatible.

5. Enforce session-level active-turn locking.

   A concurrent turn attempt for the same session must return `TURN_IN_PROGRESS`.  
   Source: `docs/PRD.md` FR-018.  
   Verification: lock concurrency test starts one active turn and asserts the second same-session turn is rejected.

6. Implement lock release on all covered cleanup paths.

   Release the active-turn lock after normal completion, adapter failure, route abort, and cancellation cleanup.  
   Source: `docs/SPEC.md` Section 10.4; `docs/CONTRACT.md` K-EVENT-3.  
   Verification: lock cleanup tests prove a follow-up turn can start after each terminal or cleanup path.

7. Persist accepted-turn before engine execution.

   Ensure `turn.accepted` is written before SDK/model/provider execution begins.  
   Source: `docs/SPEC.md` Section 10.1; `docs/CONTRACT.md` K-EVENT-2; `docs/PRD.md` FR-021.  
   Verification: ordering test uses a stub adapter and event writer spy or recorded event sequence.

8. Persist terminal outcomes.

   Persist durable terminal records for success, failure, and cancellation.  
   Source: `docs/PRD.md` FR-022; `docs/CONTRACT.md` K-EVENT-3.  
   Verification: terminal tests assert one terminal event for each accepted turn path. Interruption-specific mapping remains coordinated with DEL-03-04.

9. Preserve browser-facing SSE event names.

   Existing event names include `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, and `process:exit`.  
   Source: `docs/SPEC.md` Section 11.  
   Verification: compatibility fixture asserts event names do not regress.

10. Check provider-neutral boundary.

   SDK-specific message names, session IDs, tool names, permission modes, transcript paths, and hook names must remain adapter metadata and not define public APIs, browser events, or canonical event schemas.  
   Source: `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` K-CORE-1, K-ENGINE-4.  
   Verification: type/schema tests and code review reject SDK-shaped public leakage.

11. Run the focused validation set.

   Minimum checks: existing tests, Section 8 validation where available, route/SSE compatibility, `TurnEngine` unit tests, lock cleanup tests, session lifecycle tests, accepted-turn ordering, and terminal outcome tests.  
   Source: `docs/SPEC.md` Sections 19.2-19.3; `docs/PRD.md` Sections 12.5-12.6.  
   Verification: record exact commands and results in implementation handoff notes.

## Verification

| Verification Item | Required Evidence |
|---|---|
| `TurnEngine` unit-testable without HTTP | Passing unit test using stub engine adapter. |
| Session lock rejects concurrent turn | Passing concurrency test asserting `TURN_IN_PROGRESS`. |
| Lock cleanup works | Passing tests for completion, failure, cancellation/abort cleanup, and subsequent turn start. |
| Accepted-turn ordering | Event sequence or spy proves `turn.accepted` precedes engine invocation. |
| Terminal outcomes | Success, failure, and cancellation each produce one durable terminal event. |
| SSE compatibility | Route fixture confirms existing browser event names and stream behavior. |
| Session lifecycle | Test confirms session binding and runtime option forwarding into `TurnInput`. |
| Provider-neutral boundary | Test/review confirms SDK-specific fields are adapter metadata only. |

## Records

Records to preserve for implementation closure:

- Code paths changed for `TurnEngine`, route adapter, session lock, and event writer integration.
- Test files and commands proving the verification items above.
- Any source-state note resolving or carrying forward the `docs/PRD.md` hash mismatch.
- Residual `TBD` decisions for exact lock storage, interrupt/cancel ownership with DEL-03-04, and current-code file path choices.
- Handoff note if dependency extraction has not yet populated `_DEPENDENCIES.md` / `Dependencies.csv`.
