# I4 fresh read-only backcheck Agent 2 brief

RequestedBy: WORKING_ITEMS
RunID: `ROOT_TM112_IMPLEMENT_2026-08-03`
ChildInstanceID: `I4-FRESH-BACKCHECK`
AgentType: fresh ephemeral generalist Agent 2; no delegation
Posture: final-hash read-only refutation/backcheck

## Objective

Independently try to disprove the final-hash TM-ROOT-112 candidate, verify that
M-I2-01 and M-I2-02 are actually closed without regressions, and recheck every
accepted N-STOP-1..7 clause/matrix row. Do not repair product files.

## Sealed final identity

- Accepted implementation brief: pre-normalization authoring/execution SHA-256 `b8163531fb8f41142d6c067111fa84d2065ebd28c47f1c1e32e9218c16e6a218`; later semantically identical whitespace-normalized publication SHA-256 `617512278aa93e05a07334b5f666e7a7e1f2e869882c33da6fd63b6fcdc92e9d`. I4 backchecked the candidate created from the former.
- `docs/SPEC.md`: `647eee2d8e68da9d6a4f7935b781b6b98c874ba696c824dd6d6a8f6c1b8d6a7f`.
- `runtime/packages/daemon/src/runtime-daemon.ts`: `224403008e5ff072f1f614801afe4cedba6d3ade3c000c90ce1602ae8e27ddf2`.
- `runtime/tests/daemon.test.ts`: `c853f20726c8633207246a90e79ac89122b651a15e6e0f9976b15f1910acb352`.
- I2 recovered refutation and adversarial tests; I3 return SHA-256
  `ae10f7cf4ae395a9548f290da01973c405b0f6b0e1ecaad08c6a7f52b5418dab`.

Stop on hash drift.

## Required checks

- Trace all accepted clause ordering, latch/identity/iterator behaviors,
  force/settle bounds, cleanup/failure classification/retry, Promise identity,
  concurrency, completed-response behavior, ownership, restart, and late-event
  generation isolation against code and exact tests.
- Prove M-I2-01 for a non-identifying first event then later identifying event
  before force, and prove force still forbids later identity.
- Prove M-I2-02 preservation before bind plus correct cleanup after a listener
  was actually bound; verify owner cleanup remains generation guarded.
- Confirm section 14.1 only, exact 2000/500 constants, no public timing override,
  no App/R2/process/SIGTERM claim, and exact product-write scope.
- Run each once on final hashes: strict full check, I2 adversarial cases,
  canonical daemon suite, full runtime suite, and evidence-output build. Record
  exact commands/results/platform and Node 22.19 gap.

## Tools/writes/return

Read/search/hash/diff plus preserved compiler/Vitest configs and deterministic
checks. Product files are strictly read-only. AllowedWriteTargets: only this
I4 directory except the parent launch brief. Do not install, repair, use Git,
or touch registers/receipts/App/Piping/DEL/lifecycle/other source. Agent 2 may
not delegate.

Write `BACKCHECK.md` and `RETURN.md`, classify every finding, and return
`PASS | PASS_WITH_NONBLOCKING_FINDINGS | FAIL`. Any material finding blocks
manager fan-in and must cite a bounded reproduction or exact semantic trace.
