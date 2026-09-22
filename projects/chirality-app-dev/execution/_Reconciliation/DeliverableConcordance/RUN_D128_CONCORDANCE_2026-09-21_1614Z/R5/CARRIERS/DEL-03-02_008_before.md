### CLM-005 — Construction

> ##### Construction
>
> | Artifact / Surface | Expected Construction Detail | Status |
> |---|---|---|
> | `turn-engine.ts` | New or equivalent runtime service exposing `TurnEngine.runTurn()` outside HTTP and invoking `AgentEnginePort` / SDK-backed adapter through the product-owned boundary. | Path proposed by PRD/PLAN as `frontend/src/lib/harness/turn-engine.ts`; exact local code path TBD until implementation starts. |
> | Session lock | Active-turn lock obtained before forwarding to `TurnEngine`, released on completion, failure, cancellation, or route cleanup. | Source-supported behavior; current route uses an in-module `Set<string>` named `activeSessionTurns` in `frontend/src/app/api/harness/turn/route.ts`; this is current implementation context, not a final storage decision. |
> | Boot/session binding | Turn input carries active session and previously bound `projectRoot`, persona, mode, and resolved runtime options. | Source-supported behavior; exact session manager API TBD. |
> | SSE adapter | Route writes existing browser-facing event names and does not expose SDK messages as browser contract. | Source-supported behavior; exact adapter function names TBD. |
> | Accepted-turn event | `turn.accepted` is persisted before SDK/model execution begins. | Source-supported behavior; exact event-writer API TBD. |
> | Terminal event handling | Terminal success, failure, cancellation, and explicit user-interruption outcomes are persisted; explicit user interruption uses `turn.interrupted` per D-APP-40. | Source-supported behavior; implementation-specific cleanup coverage remains coordinated with DEL-03-04. |
> | Lock cleanup tests | Tests cover concurrent turn rejection and lock release on normal completion, error, and cancellation cleanup. | ASSUMPTION: test names/locations TBD; behavior grounded in PRD/SPEC. |
> | Session lifecycle tests | Tests cover session binding, boot metadata forwarding, and stable route/SSE behavior through `TurnEngine`. | ASSUMPTION: test names/locations TBD; behavior grounded in PRD/SPEC. |
>
> Current implementation pointers observed during Pass 3:
>
> - Route adapter and active-turn guard: `frontend/src/app/api/harness/turn/route.ts`.
> - Interrupt route: `frontend/src/app/api/harness/interrupt/route.ts`.
> - Stub active-turn manager: `frontend/src/lib/harness/agent-sdk-manager.ts`.
> - Anthropic active-turn manager: `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts`.
> - Runtime interface types: `frontend/src/lib/harness/types.ts`.
> - Current route/interrupt tests: `frontend/src/__tests__/api/harness/routes.test.ts`.
>

