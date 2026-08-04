# I2 manager-recovered refutation

Status: `FAIL / TWO MATERIAL FINDINGS / REFUTER INTERRUPTED AFTER DURABLE ADVERSARIAL EVIDENCE`
Product identity: SPEC `647eee2d...`; daemon `bbee7e40...`; tests `d36f76de...` (all exact full hashes in the launch brief).
Failure class for missing child return: `AGENT_RETURN_TIMEOUT_POSTEVIDENCE`.

I2 verified every sealed hash and independently reported the following two
material defects. It wrote `adversarial.test.ts` and an isolated Vitest config
but did not write terminal documents after repeated requests. HELP_HUMAN
directed interruption and manager recovery.

## M-I2-01 — later pre-force Agent-1 identity is not retried

`sse()` retries a latched high-level Agent-1 interrupt after only the first
iterator result. Its subsequent loop obtains and emits later events without
calling `trySseInterrupt(control)`. If the first event is non-identifying and a
later pre-force `harness:event` supplies `managerSessionId`, the tracked source
captures the identity but canonical interrupt is never invoked; force records
identity unavailable. This violates N-STOP-3's requirement to invoke as soon as
identity becomes known before force.

Classification: `MATERIAL`.

## M-I2-02 — refused foreign control path is deleted on start failure

The `start()` catch unconditionally calls `unlinkControlSocket()`, including
when `recoverStaleSocket()` rejected a non-socket/live/foreign path before the
candidate generation created or bound any listener. The call rejects as
intended but deletes the path it refused to replace. This violates the existing
fail-closed recovery safety and the accepted owned-cleanup boundary.

Classification: `MATERIAL`.

## Reproduction

The manager ran I2's frozen adversarial test file outside the Unix-socket
sandbox:

`/Users/ryan/dev/chirality/runtime/node_modules/.bin/vitest run execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I2-FRESH-REFUTER/adversarial.test.ts --config /Users/ryan/.codex/worktrees/1342/chirality/execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I2-FRESH-REFUTER/vitest.adversarial.config.mjs`

Result: expected failing reproduction, 1 file / 2 tests / 2 failed, 2.36 s:

- foreign control-path read failed `ENOENT`, proving deletion;
- later-event identity expected one interrupt but observed zero after 2,022 ms.

## Disposition

Candidate verdict: `FAIL`. Release a fresh bounded remediation Agent 2 for
exactly these two source repairs and corresponding daemon-test assertions.
Then run strict/build/bounded/full checks and dispatch a genuinely fresh
read-only backcheck. No App notice or human repair acceptance is authorized.
