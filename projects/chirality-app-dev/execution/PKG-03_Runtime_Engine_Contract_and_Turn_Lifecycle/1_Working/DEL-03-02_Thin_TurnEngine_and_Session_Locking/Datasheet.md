# Datasheet: DEL-03-02 Thin TurnEngine and Session Locking

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-03-02 |
| Deliverable Name | Thin TurnEngine and Session Locking |
| Package | PKG-03 Runtime Engine Contract and Turn Lifecycle |
| Decomposition Variant | SOFTWARE_DECOMP v3.2 |
| Type | BACKEND_FEATURE_SLICE |
| Context Envelope | M |
| Responsible Party | TBD |
| Primary Objective | OBJ-002 - establish product-owned runtime contracts and thin route boundaries before SDK behavior becomes production default |
| Scope Items | SOW-009, SOW-010, SOW-011, SOW-038 |

Source: `_CONTEXT.md` Identity and Traceability; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-03-02 row and OBJ-002 row.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Runtime owner | `TurnEngine` owns a single harness turn lifecycle and invokes the engine through the product-owned boundary. | `docs/TYPES.md` Section 7.1; `docs/PRD.md` FR-070 |
| Engine boundary | `AgentEnginePort` / `RuntimeEngineContract` is separate from SDK APIs. | `docs/SPEC.md` Section 10.1; `docs/CONTRACT.md` K-ENGINE-1 |
| Target type | `AgentEnginePort.runTurn(input: TurnInput): AsyncIterable<UIEvent>` with optional `interrupt(sessionId)`. | `docs/SPEC.md` Section 10.2 |
| Turn input content | Active session, normalized project root, persona, mode, resolved runtime options, content blocks, attachment summaries, and cancellation signal where applicable. | `docs/SPEC.md` Section 10.2 |
| HTTP route role | `/api/harness/turn` remains a transport adapter that validates request shape, obtains session lock, forwards input to `TurnEngine`, writes SSE, and handles cleanup. | `docs/SPEC.md` Section 10.4 |
| Session locking | Only one active turn may run per session; concurrent turn attempts return `TURN_IN_PROGRESS`. | `docs/PRD.md` FR-018 |
| Browser stream contract | Browser-facing SSE event names remain compatible during SDK adoption. | `docs/SPEC.md` Section 11; `docs/PRD.md` FR-017, FR-071 |
| Accepted-turn persistence | Accepted user input persists before model/provider/SDK execution. | `docs/SPEC.md` Section 10.1; `docs/CONTRACT.md` K-EVENT-2; `docs/PRD.md` FR-021 |
| Terminal outcomes | Success, failure, and cancellation persist as terminal runtime events. | `docs/CONTRACT.md` K-EVENT-3; `docs/PRD.md` FR-022 |
| SDK isolation | SDK-specific messages, IDs, tool names, permission modes, transcript paths, and hook names are adapter metadata, not public Chirality contracts. | `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` K-CORE-1, K-ENGINE-4 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Source state warning | `docs/PRD.md` is accessible but recorded as `HASH_MISMATCH` in `_REFERENCES.md`; PRD-derived details are used as current source content with this warning. | `_REFERENCES.md` REF-006 |
| Route compatibility constraint | Existing `/api/harness/*` route shapes remain stable during SDK adoption and TurnEngine extraction. | `docs/SPEC.md` Section 17.1 |
| Event separation constraint | Browser `UIEvent`s and persisted `HarnessEvent`s are separate contracts. | `docs/SPEC.md` Sections 9 and 11; `docs/CONTRACT.md` K-EVENT-1 |
| Session storage context | Legacy session records remain readable; vNext session layout is `.chirality/sessions/<sessionId>/` with `session.json`, `events.jsonl`, `turns/`, `artifacts/`, and `sdk/`. | `docs/SPEC.md` Sections 8.1 and 8.2 |
| Settings isolation context | Shipped builds use SDK `settingSources: []`; ambient user/local SDK settings are not allowed in shipped builds. | `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1 |
| Implementation sequencing | R1 includes thin `TurnEngine`, engine contract, session event log, SDK message mapper, prompt composer, settings isolation, and run logger before tool expansion. | `docs/PLAN.md` R1; `docs/PRD.md` R1 |

## Construction

| Artifact / Surface | Expected Construction Detail | Status |
|---|---|---|
| `turn-engine.ts` | New or equivalent runtime service exposing `TurnEngine.runTurn()` outside HTTP and invoking `AgentEnginePort` / SDK-backed adapter through the product-owned boundary. | Path proposed by PRD/PLAN as `frontend/src/lib/harness/turn-engine.ts`; exact local code path TBD until implementation starts. |
| Session lock | Active-turn lock obtained before forwarding to `TurnEngine`, released on completion, failure, cancellation, or route cleanup. | Source-supported behavior; current route uses an in-module `Set<string>` named `activeSessionTurns` in `frontend/src/app/api/harness/turn/route.ts`; this is current implementation context, not a final storage decision. |
| Boot/session binding | Turn input carries active session and previously bound `projectRoot`, persona, mode, and resolved runtime options. | Source-supported behavior; exact session manager API TBD. |
| SSE adapter | Route writes existing browser-facing event names and does not expose SDK messages as browser contract. | Source-supported behavior; exact adapter function names TBD. |
| Accepted-turn event | `turn.accepted` is persisted before SDK/model execution begins. | Source-supported behavior; exact event-writer API TBD. |
| Terminal event handling | Terminal success, failure, and cancellation outcomes are persisted. | Source-supported behavior; interruption-specific mapping overlaps DEL-03-04 and remains TBD for this slice. |
| Lock cleanup tests | Tests cover concurrent turn rejection and lock release on normal completion, error, and cancellation cleanup. | ASSUMPTION: test names/locations TBD; behavior grounded in PRD/SPEC. |
| Session lifecycle tests | Tests cover session binding, boot metadata forwarding, and stable route/SSE behavior through `TurnEngine`. | ASSUMPTION: test names/locations TBD; behavior grounded in PRD/SPEC. |

Current implementation pointers observed during Pass 3:

- Route adapter and active-turn guard: `frontend/src/app/api/harness/turn/route.ts`.
- Interrupt route: `frontend/src/app/api/harness/interrupt/route.ts`.
- Stub active-turn manager: `frontend/src/lib/harness/agent-sdk-manager.ts`.
- Anthropic active-turn manager: `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts`.
- Runtime interface types: `frontend/src/lib/harness/types.ts`.
- Current route/interrupt tests: `frontend/src/__tests__/api/harness/routes.test.ts`.

## References

| RefID | Source | Sections Used | Status |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | 2.8-2.10 | MATCH |
| REF-002 | `docs/CONTRACT.md` | 1.4-1.5 | MATCH |
| REF-003 | `docs/SPEC.md` | 8-12, 17.1, 19.2-19.3 | MATCH |
| REF-004 | `docs/TYPES.md` | 7.1-7.4 | MATCH |
| REF-005 | `docs/PLAN.md` | R1 | MATCH |
| REF-006 | `docs/PRD.md` | FR-014-FR-022, FR-070-FR-077, FR-116, FR-122-FR-128, R1, validation additions | HASH_MISMATCH source-state warning |
| REF-007 | `agents/AGENT_SOFTWARE_DECOMP.md` | Not directly used for implementation requirements in this draft. | MATCH |
