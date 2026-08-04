# I3 bounded-remediation Agent 2 brief

RequestedBy: WORKING_ITEMS
RunID: `ROOT_TM112_IMPLEMENT_2026-08-03`
ChildInstanceID: `I3-BOUNDED-REMEDIATION`
AgentType: fresh ephemeral generalist Agent 2; no delegation
Predecessor verdict: I2 `FAIL`, exactly two material findings.

## Objective

Repair only M-I2-01 and M-I2-02 from
`instances/I2-FRESH-REFUTER/MANAGER_RECOVERED_REFUTATION.md`, add bounded
regression assertions for each, and return a final-hash candidate. Do not
redesign unrelated shutdown behavior.

## Frozen predecessor

- `docs/SPEC.md`: `647eee2d8e68da9d6a4f7935b781b6b98c874ba696c824dd6d6a8f6c1b8d6a7f`.
- `runtime/packages/daemon/src/runtime-daemon.ts`: `bbee7e403942808c2de18cbcc02cbb2919598bcd8d6049da2da7dfcdb02ada76`.
- `runtime/tests/daemon.test.ts`: `d36f76dea9b8dcdf1d078ff98d9474ed171a63e0d3da0ff244c4a417fb38d25b`.

Verify all three before writing.

## Exact repair requirements

1. After every later iterator result in `sse()`, retry the existing single
   cancellation latch before processing completion/emission so a
   `managerSessionId` captured by a later pre-force harness event immediately
   starts the one canonical interrupt. Preserve force expiry/no-late interrupt.
2. Make `start()` failure cleanup unlink the control socket only when this
   attempted generation demonstrably bound/owned that listener path. A failure
   from stale-path recovery before binding must preserve the refused non-socket,
   live, or foreign path. Owner-record cleanup remains generation-identity
   guarded. Do not weaken normal failed-start cleanup after this generation
   actually bound the listener.
3. Add a deterministic later-event pre-force identity regression and
   preservation assertions for refused non-socket/live-owner paths in
   `runtime/tests/daemon.test.ts`. You may use I2's adversarial tests as
   evidence/design input, but the canonical suite must carry the assertions.

## Scope/tools/return

Allowed product writes only:
`runtime/packages/daemon/src/runtime-daemon.ts` and bounded additions to
`runtime/tests/daemon.test.ts`. `docs/SPEC.md` is read-only because no contract
text change is required. Write evidence only under this I3 directory. Use
apply_patch, strict check, the two adversarial cases, bounded daemon suite, full
runtime suite, and evidence-output build. Do not install dependencies or use
Git. Do not touch registers/receipts/App/Piping/DEL/lifecycle/other source.

Write `RETURN.md` with exact repaired hashes, finding-to-fix mapping, commands,
results, residual gaps, and scope statement. Stop if either repair requires
outward scope. Agent 2 may not delegate.
