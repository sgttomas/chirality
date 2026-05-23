# Guidance: DEL-03-02 Thin TurnEngine and Session Locking

## Purpose

DEL-03-02 exists to make the harness turn lifecycle product-owned and testable outside HTTP. The route remains stable for the browser, but lifecycle behavior moves behind `TurnEngine` and the product-owned `AgentEnginePort` / `RuntimeEngineContract`.

Sources: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-03-02; `docs/SPEC.md` Section 10; `docs/PRD.md` FR-070-FR-071; `docs/PLAN.md` R1.

## Principles

1. Route thinness is the design boundary.

   `/api/harness/turn` should validate, lock, forward to `TurnEngine`, write SSE, and clean up. Runtime policy, engine invocation, event persistence ordering, and provider-specific behavior should not remain owned by the route. Source: `docs/SPEC.md` Section 10.4.

2. Chirality terms own the public contract.

   Public APIs, browser `UIEvent`s, canonical `HarnessEvent`s, session storage, permission decisions, and governance records must not become SDK-shaped except as adapter metadata. Source: `docs/CONTRACT.md` K-CORE-1, K-ENGINE-4; `docs/SPEC.md` Section 10.3.

3. The lock protects session semantics, not just code paths.

   The requirement is one active turn per session with `TURN_IN_PROGRESS` on concurrent attempts. Keep lock lifecycle tied to durable turn state and route cleanup so interrupted or failed paths cannot strand a session. Source: `docs/PRD.md` FR-018; `docs/SPEC.md` Section 10.4.

4. Accepted-turn persistence is a reliance boundary.

   Persist `turn.accepted` before SDK/model execution so killed or interrupted turns leave a recoverable record. This should be verified by ordering tests, not assumed from call structure. Source: `docs/CONTRACT.md` K-EVENT-2; `docs/PRD.md` FR-021.

5. SSE compatibility is not optional.

   Browser event names remain stable during SDK adoption. The internal mapping may become richer, but browser-facing names stay compact and compatible. Source: `docs/SPEC.md` Section 11 and 17.1; `docs/PRD.md` FR-017.

6. Do not use this slice to widen capability.

   R1 explicitly preserves visible behavior and does not expose new user-visible local tool capability. Keep write, bash, remote MCP, subagent, and domain-operation surfaces out of this deliverable. Source: `docs/PLAN.md` R1 Acceptance; `docs/PRD.md` R1 Acceptance.

## Considerations

| Topic | Guidance | Source |
|---|---|---|
| Lock storage | Keep the lock associated with session identity and observable turn state. Exact implementation is TBD because no source slice defines a storage mechanism. | `docs/PRD.md` FR-018; `docs/SPEC.md` Section 10.4 |
| Cleanup ownership | The route handles cleanup, but terminal lifecycle persistence belongs behind the runtime boundary. Split responsibilities so both are testable. | `docs/SPEC.md` Sections 10.1 and 10.4 |
| Cancellation signal | Include cancellation signal in `TurnInput` where applicable; full interrupt behavior should remain coordinated with DEL-03-04. | `docs/SPEC.md` Section 10.2; decomposition DEL-03-04 |
| Boot metadata | Forward active session and resolved runtime options into `TurnInput`; boot fingerprint composition belongs to adjacent prompt/options work and should not be invented here. | `docs/SPEC.md` Sections 10.2 and 13.2; `docs/PRD.md` FR-016, FR-029 |
| Legacy sessions | Do not break legacy session readability while extracting the lifecycle. | `docs/SPEC.md` Section 8.1; `docs/PRD.md` FR-077 |
| Event persistence | Keep accepted-turn and terminal events durable. Exact writer API is TBD until implementation reads current code. | `docs/SPEC.md` Sections 9 and 10.1; `docs/CONTRACT.md` K-EVENT-2, K-EVENT-3 |
| PRD hash mismatch | Treat PRD-derived rows as source-state-warning content until hash reconciliation. Do not escalate them into unsupported implementation details beyond cited requirement text. | `_REFERENCES.md` REF-006 |

## Trade-offs

| Trade-off | Preferred Direction | Rationale |
|---|---|---|
| Thin route vs. route-owned lifecycle | Prefer thin route with lifecycle in `TurnEngine`. | Required by `docs/SPEC.md` Section 10.4 and `docs/PRD.md` FR-070-FR-071. |
| Strict lock release vs. broad catch-all cleanup | Prefer explicit terminal-path cleanup plus route abort cleanup. | Avoids stranded sessions and supports testable active-turn semantics. |
| SDK-shaped internal convenience vs. Chirality-owned public contract | Prefer adapter translation and metadata-only SDK leakage. | Required by `docs/SPEC.md` Section 10.3 and `docs/CONTRACT.md` K-ENGINE-4. |
| Implement interrupt details now vs. defer full terminal semantics | Implement lock cleanup/cancellation signal boundary now; defer full interrupt/cancel outcome handling to DEL-03-04 where needed. | DEL-03-02 scope is thin `TurnEngine` and session locking; DEL-03-04 owns interrupt/cancel terminal handling. |
| Add new capabilities during refactor vs. preserve behavior | Preserve behavior and avoid new capability exposure. | R1 acceptance forbids new user-visible local tool capability beyond current surface. |

## Examples

Supported conceptual flow:

```text
POST /api/harness/turn
  -> validate request shape
  -> obtain session active-turn lock
  -> construct TurnInput from session, project root, persona, mode, options, content, attachments, cancellation signal
  -> call TurnEngine.runTurn(input)
  -> stream yielded UIEvents as existing SSE names
  -> persist accepted-turn and terminal records through runtime event layer
  -> release lock on completion, failure, cancellation, or route cleanup
```

This is a conceptual flow only. Exact function names, file paths, and call ordering details beyond the cited requirements are TBD until implementation reads the current route and session manager code.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| TBD | No direct content conflict found during Pass 1/2. `docs/PRD.md` has a hash mismatch in `_REFERENCES.md`, which is a source-state warning rather than a source-content conflict. | `_REFERENCES.md` REF-006 | `docs/PRD.md` cited sections | All PRD-derived requirements | Revalidate PRD hash before closure; keep PRD-derived details conservative. | TBD |
