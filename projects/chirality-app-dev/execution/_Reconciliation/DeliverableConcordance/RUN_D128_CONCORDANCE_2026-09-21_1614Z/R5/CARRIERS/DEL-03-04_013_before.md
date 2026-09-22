### CLM-005 — Construction

> ##### Construction
>
> | Component / Artifact | Construction Target | Status |
> |---|---|---|
> | Interrupt tests | Cover active-turn interrupt route, provider abort propagation, SSE `process:exit`, lock release, and durable terminal outcome. | ASSUMPTION: exact test file path TBD |
> | Cancel cleanup tests | Cover client disconnect and cancellation-signal cleanup, lock release, and durable cancellation record once event log exists. | ASSUMPTION: exact test file path TBD |
> | Terminal event mapper | Map completion, failure, cancellation, and interruption handling into browser `UIEvent`s and persisted `HarnessEvent`s without SDK-shaped public semantics; explicit interruption uses `turn.interrupted`. | `frontend/src/lib/harness/claude-agent-sdk-manager.ts`; `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts`; D-APP-40 |
> | Lock cleanup verification | Confirm interrupt, disconnect, failure, and cancellation all release session active-turn state. | Supported by DEL-03-04 scope and PRD FR-018/FR-019/FR-022 |
> | Event log verification | Confirm terminal records append as newline-delimited JSONL with unique event IDs and no secrets. | `docs/SPEC.md` Section 9.2 |
>

