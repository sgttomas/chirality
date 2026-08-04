# Root evidence fitness — D-APP-88 R3 sequencing release

Verdict: `PASS — R2 SEQUENCING REQUIREMENT SATISFIED; APP REBUILD RELEASED`

## Accepted authority and byte identity

The routed App notice cites the signed Root acceptance transcript SHA-256
`a10bda1c05fe1e1249a7efa266401ddf71752e4d9a8ab0448ec96251d5973046`.
The current committed Root product bytes exactly match the accepted hashes:

| Surface | Accepted/current SHA-256 |
|---|---|
| `docs/SPEC.md` | `647eee2d8e68da9d6a4f7935b781b6b98c874ba696c824dd6d6a8f6c1b8d6a7f` |
| `runtime/packages/daemon/src/runtime-daemon.ts` | `224403008e5ff072f1f614801afe4cedba6d3ade3c000c90ce1602ae8e27ddf2` |
| `runtime/tests/daemon.test.ts` | `c853f20726c8633207246a90e79ac89122b651a15e6e0f9976b15f1910acb352` |

The accepted evidence is Node 24 strict, adversarial 2/2, daemon 15/15,
full-runtime 74/74, build, and fresh backcheck. Node 22.19 execution remains
explicitly unexecuted.

## Exact R2 blocker comparison

R2 required Root reproduction or disproof with active Unix-socket/SSE clients,
explicit graceful drain/termination semantics, socket/owner cleanup proof, and
reciprocal Root evidence before rebuilding App helper bytes. Its exact failed
App conjunct was the absence of auditable post-GUI first-signal graceful-stop
proof; retained R2 logs showed GUI contact followed by no shutdown entry and
eventual transport loss, while operator-only process/socket observations were
not evidence.

The accepted Root `G2 + C1 + F1` bytes now supply the needed generic behavior:

- stop is generation-bound and closes listener admission;
- active known SSE turns receive canonical interrupt requests;
- the graceful interval is exactly 2,000 ms;
- after that deadline Root calls `closeAllConnections()` and destroys every
  residual tracked socket for the generation;
- transport settlement receives a further bounded 500 ms;
- control-socket unlink and owner cleanup are then attempted; and
- canonical tests cover completed keep-alive transport, forced incomplete
  requests, live SSE, cleanup, restart, and generation safety.

This is fit to rerun the App process/SIGTERM/package proof on final helper bits.
No additional generic Root semantic is required by the prior blocker.

## Limits and non-inferences

- This fitness finding does not prove R2 causality or R2 process/SIGTERM facts.
- It does not substitute Root's Node 24 test evidence for the required App
  post-GUI first-signal process/socket snapshot.
- It does not cover Node 22.19.
- It does not accept D-APP-88, authorize Root edits, or fire TM-APP-036 by
  itself. The rider fires only if the rebuilt D-APP-88 implementation is
  accepted after fresh verification.
