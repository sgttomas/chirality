# Validation R9 — D-APP-92 Attempt-8 v1.20 fresh-verifier stop

Verdict: `BLOCK_PACKET_REPAIR_REQUIRED`

## Frozen basis

- Receipt 128 remains a historical stop record and was not rewritten.
- The v1.20 manager freeze is immutable at SHA-256
  `e3e4dc3035038ebbc8c980e3a5fe587ae22b8274a8e3e31bd37c008af83da0f6`.
- The genuinely fresh adversarial-verifier brief is immutable at SHA-256
  `c5d8b65edbb261d2626800e695d4bf3d9aff758c496e892a0a31acf559d252f4`.
- The fresh verifier return is immutable at SHA-256
  `47b57dae327e247c97a8957ad2cdf602b10ff64b94546babc3c5c1b8f5dbe655`
  and returns `BLOCK_PACKET_REPAIR_REQUIRED`.
- The verifier reproduced all 17 frozen identities on its first substantive
  check and final post-review check. No frozen-byte drift was observed.

## Material blocking result

The packet is not safe for owner presentation because four material defects
remain:

1. C847 lacks an immediate PID/PPID/start-time/executable direct-child
   identity guard at the attach boundary; the earlier sentinel proof does not
   close the helper-exit/PID-reuse race.
2. Supervisor and controller child `error` events are accepted as drained
   process terminality, allowing cleanup claims without observed LLDB `close`
   or controller-owned-child `exit`.
3. Accepted C1010 SIGKILL followed by no LLDB `close` before the +149.9-second
   absolute deadline satisfies none of the claimed eight proof branches.
4. C1007 is guarded by an attempted-interrupt counter rather than accepted
   C1003 evidence, and no `child.stdin` error handler contains asynchronous
   writable-stream failure.

The claimed seven-terminal-safe/one-identity-unsafe branch model is therefore
not executable as written. No prospective owner token may be presented.

## Closeout checks

The following passed without executing a proposed R5 operation:

- exact C787-C1057 accounting: 271 unique contiguous rows;
- all ten R5 scripts: static `node --check` only;
- receipt contract through Receipt 128;
- authority corpus v18 status with no drift;
- practitioner status and App-scoped self-check;
- 349-test practitioner-harness suite;
- candidate-whitespace validation against
  `7aada3fbadf340a07ef828cc18b350c8c01b517d`;
- `git diff --check`;
- exact frontend Git cleanliness;
- fixed temporary-root and durable R5 evidence-target absence; and
- App-only write containment.

Frontend runtime gates were not repeated because no product byte changed and
the entire R5 packet remains proposal-only. No runtime, package, cache,
network, helper, GUI, LLDB, attach, signal, replay, credential, cleanup,
rollback, deletion, release, Git, Task Management, or foreign-loop operation
was executed in this closeout.
