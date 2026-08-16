# Orchestration plan v1

Posture: serialized `TERMINAL_FAN_OUT_IN`, selected by the Agent 0 launch brief and D-APP-60 calibrated independent-verification requirement.

1. `A2-PKG02-RECONNECT-IMPLEMENT-01` — `TASK + software-bounded-implementation`; inspect the existing chip, preload/control bridge, supervisor callback, and tests; select the smallest accessible design within the D-APP-64 fast-reject boundary; implement source and automated component/render plus behavior coverage; run focused registered checks and return scope evidence.
2. `A2-PKG02-RECONNECT-REVIEW-01` — fresh `TASK + software-code-review`; after implementation freezes, read-only review of 100% of the product diff and focused evidence; return `COMMIT-SAFE` or `BLOCK`.
3. `A1-PKG02-RECONNECT-01` fan-in — accept or remediate; run profile-selected/full checks required for UI work; record the D-APP-64 exercise and product evidence; remove exactly the completed DEL-02-01 Remaining item without lifecycle change.

Edge: `IMPLEMENT-01 -> REVIEW-01 -> manager fan-in`. Only the implementer owns product writes. The reviewer is read-only. Manager closeout starts only after both children terminate.

Fan-in gate: the chip is an accessible interactive reconnect affordance; one operator action reaches the existing main-process daemon status callback and supervisor immediate refresh without inventing runtime semantics; state/error/reentrancy behavior is covered; focused and required registered checks pass; exact App-only containment holds; fresh verdict is `COMMIT-SAFE`.
