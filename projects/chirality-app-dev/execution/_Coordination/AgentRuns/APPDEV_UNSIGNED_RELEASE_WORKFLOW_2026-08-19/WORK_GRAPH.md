# Frozen work graph v1

Status: `FROZEN BEFORE DISPATCH`

Selection authority: HELP_HUMAN Agent-0 graph v1 plus exact D-APP-97 C1 ruling.

Posture: `TERMINAL_FAN_OUT_IN`. This activation contains one engineering node. Mandatory independent review is a validation stage, not another engineering node.

1. `A2-DEL0905-IMPLEMENT-01` — one bounded `TASK + software-bounded-implementation` child may inspect, implement, test, and return within the product/build write boundary.
2. `A2-DEL0905-REVIEW-01` — fresh context-independent `TASK + software-code-review`, read-only over 100% of the manager-frozen diff after implementation and in-session checks.
3. Manager fan-in — validate return, checks, review, containment, deliverable closeout, and handoff to HELP_HUMAN/CHANGE.

Edges: `IMPLEMENT-01 -> REVIEW-01 -> manager fan-in`. Review findings require bounded remediation and a new fresh review before fan-in. There is no concurrent sibling node and no concurrent write surface.

Checks by surface:

- In-session: deterministic workflow/static validation; workflow-specific regression tests; applicable frontend typecheck/Vitest/build/package validation; instruction-root and package-integrity evidence; APP-HOLD and containment checks.
- PR CI: actual macOS unsigned artifact build, verification, and upload behavior. This proof may remain explicitly owed at manager return, with the exact check/workflow and rerun condition named.
- Host-capability: none required for selection; the artifact itself is exercised by PR CI.

Fan-in gates: least privilege and bounded triggers; unsigned CI-only macOS artifact creation and verification; explicit signing/notarization posture check without either action; no GitHub Release publication; required validation/instruction-root/package evidence retained; deterministic proof passes; frozen diff receives fresh read-only PASS; write containment is exact.

Escalation points: any signing, notarization, distribution/publication, provider/network expansion, dependency/lockfile change, lifecycle transition, root/runtime or unrelated product change, or additional engineering node returns to HELP_HUMAN rather than expanding this activation.
