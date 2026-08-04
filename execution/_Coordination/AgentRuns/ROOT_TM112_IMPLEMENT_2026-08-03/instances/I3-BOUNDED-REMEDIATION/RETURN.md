# I3 bounded-remediation return

Status: `PASS / M-I2-01 AND M-I2-02 REPAIRED / FINAL-HASH CANDIDATE`

## Frozen-input verification

Before writing, I3 verified all three frozen predecessor hashes exactly:

| File | Frozen SHA-256 | Result |
|---|---|---|
| `docs/SPEC.md` | `647eee2d8e68da9d6a4f7935b781b6b98c874ba696c824dd6d6a8f6c1b8d6a7f` | match |
| `runtime/packages/daemon/src/runtime-daemon.ts` | `bbee7e403942808c2de18cbcc02cbb2919598bcd8d6049da2da7dfcdb02ada76` | match |
| `runtime/tests/daemon.test.ts` | `d36f76dea9b8dcdf1d078ff98d9474ed171a63e0d3da0ff244c4a417fb38d25b` | match |

## Final product identity

| File | Final SHA-256 |
|---|---|
| `docs/SPEC.md` | `647eee2d8e68da9d6a4f7935b781b6b98c874ba696c824dd6d6a8f6c1b8d6a7f` |
| `runtime/packages/daemon/src/runtime-daemon.ts` | `224403008e5ff072f1f614801afe4cedba6d3ade3c000c90ce1602ae8e27ddf2` |
| `runtime/tests/daemon.test.ts` | `c853f20726c8633207246a90e79ac89122b651a15e6e0f9976b15f1910acb352` |

`docs/SPEC.md` remained byte-identical and read-only.

## Finding-to-fix map

### M-I2-01 — repaired

After each later `iterator.next()` result, `sse()` now retries the existing
single cancellation latch before testing completion or emitting the event.
Consequently a later pre-force `harness:event` that first supplies the manager
session identity immediately begins the one canonical interruption. The
existing `forceExpired` guard remains unchanged, so force still expires the
latch and forbids a late interrupt.

The canonical daemon suite now contains a deterministic case that emits one
non-identifying event, latches stop, releases a later identifying event before
force, and proves exactly one interrupt plus terminal `STOPPED` lifecycle.

### M-I2-02 — repaired

`start()` now records successful control-socket binding in the listen callback
and unlinks the control path during failure cleanup only when that attempted
generation demonstrably bound it. Pre-bind refusal by stale-path recovery can
no longer delete a non-socket, absent-live-owner, or other foreign path. Normal
failed-start cleanup after this generation actually binds remains intact.
Generation-identity-guarded owner-record cleanup was not changed.

The canonical stale-path case now proves the refused non-socket bytes remain
unchanged, and proves the absent-socket/live-owner record remains byte-identical
while the absent socket path remains absent.

## Final-byte validation

Environment: macOS Darwin arm64; Node `v24.18.0`; Vitest `v3.2.4`; TypeScript
from `/Users/ryan/dev/chirality/runtime/node_modules/.bin/tsc`.

1. Bounded strict source/test check:

   `/Users/ryan/dev/chirality/runtime/node_modules/.bin/tsc -p execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I3-BOUNDED-REMEDIATION/tsconfig.check.json`

   Result: exit 0.

2. Full package-scope strict check:

   `/Users/ryan/dev/chirality/runtime/node_modules/.bin/tsc -p execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I3-BOUNDED-REMEDIATION/tsconfig.full-check.json`

   Result: exit 0.

3. Frozen I2 adversarial cases:

   `/Users/ryan/dev/chirality/runtime/node_modules/.bin/vitest run execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I2-FRESH-REFUTER/adversarial.test.ts --config /Users/ryan/.codex/worktrees/1342/chirality/execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I2-FRESH-REFUTER/vitest.adversarial.config.mjs`

   Result: exit 0; 1 file / 2 tests passed; 2.32 s. Both original material
   reproductions now pass.

4. Bounded canonical daemon suite:

   `/Users/ryan/dev/chirality/runtime/node_modules/.bin/vitest run tests/daemon.test.ts --config /Users/ryan/.codex/worktrees/1342/chirality/execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I1B-IMPLEMENTER/vitest.config.mjs`

   Result outside the Unix-socket filesystem sandbox: exit 0; 1 file / 15
   tests passed; 13.90 s. The new later-identity regression passed, as did the
   strengthened refused-path preservation assertions.

5. Full runtime suite:

   `/Users/ryan/dev/chirality/runtime/node_modules/.bin/vitest run --config /Users/ryan/.codex/worktrees/1342/chirality/execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I1B-IMPLEMENTER/vitest.config.mjs`

   Result outside the Unix-socket filesystem sandbox: exit 0; 8 files / 74
   tests passed; 14.01 s; daemon matrix 15/15 passed within the full run.

6. Evidence-output build check:

   `/Users/ryan/dev/chirality/runtime/node_modules/.bin/tsc -p execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I3-BOUNDED-REMEDIATION/tsconfig.build-check.json`

   Result: exit 0; 47 emitted JavaScript files / 404 KiB under this I3
   evidence directory. No runtime package `dist/` path was written.

7. `git diff --check -- runtime/packages/daemon/src/runtime-daemon.ts runtime/tests/daemon.test.ts`

   Result: exit 0.

## Residual gaps and scope statement

- Node 22.19 remains unavailable locally; the supported-floor compatibility
  run remains unexecuted. All checks used installed Node 24.18.0 tooling.
- The worktree has no local `runtime/node_modules`; the preserved check configs
  point at the installed main-checkout compiler, Vitest, and type definitions.
- I3 repaired only M-I2-01 and M-I2-02. It made no other shutdown redesign and
  no claim about App R2 causality or process/SIGTERM behavior.
- Product writes were limited to `runtime-daemon.ts` and bounded canonical
  `daemon.test.ts` additions. Evidence writes were limited to this I3 carrier.
  No register, receipt, App, Piping, DEL, lifecycle, other source, or Git action
  was taken.
- This is a final-hash implementation candidate for genuinely fresh read-only
  backcheck. App notice, lifecycle acceptance, publication, and human repair
  acceptance remain held.
