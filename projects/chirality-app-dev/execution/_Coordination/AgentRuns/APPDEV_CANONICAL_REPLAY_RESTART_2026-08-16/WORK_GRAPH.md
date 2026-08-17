# Frozen work graph v1

Posture: serialized terminal fan-out/fan-in, selected by the Agent 0 launch brief and D-APP-64 rationale in `ACTIVATION.md`.

1. `A2-PKG05-CANONICAL-REPLAY-IMPLEMENT-01` — `TASK + software-bounded-implementation`; integration owner for one dedicated PKG-05 replay test and only any necessary App-owned runtime-client/Woven repair.
2. `A2-PKG05-CANONICAL-REPLAY-REVIEW-01` — fresh `TASK + software-code-review`; read-only after node 1 freezes; review 100% of the node diff and evidence.
3. `WI-PKG05-CANONICAL-REPLAY` fan-in — accept or remediate, run focused/narrow checks, then update only minimal DEL-05-04 and managed return surfaces.

Edge: `IMPLEMENT-01 -> REVIEW-01 -> manager fan-in`. No concurrent writes; reviewer has no write target.

Fan-in gate: real daemon plus authenticated public clients; legacy records migrate lazily and non-destructively; Desktop and CLI replay structurally equal parsed canonical session identity/events before and after fresh-service restart; exact recorded `agent1` manager and `agent2` child parentage survives; bounded deterministic cleanup; no Root/PKG-08/foreign-node writes; focused tests and narrow typecheck/check selection pass; review findings are remediated.
