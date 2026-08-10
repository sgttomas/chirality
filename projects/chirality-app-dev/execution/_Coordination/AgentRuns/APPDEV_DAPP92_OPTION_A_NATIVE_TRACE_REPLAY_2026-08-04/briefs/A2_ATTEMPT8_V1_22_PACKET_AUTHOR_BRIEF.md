# Agent 2 brief — D-APP-92 Attempt-8 v1.22 bounded packet author

RequestedBy: HELP_HUMAN through WORKING_ITEMS
RunID: `APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04`
ParentInstanceID: `A1-WORKING-ITEMS-DAPP92-V1-22-01`
ChildInstanceID: `A2-DAPP92-A-ATTEMPT8-PACKET-09`
PackageID: `APPDEV-DAPP92-OPTION-A-NATIVE-TRACE-REPLAY`
DeliverableID: bounded Attempt-8 v1.22 derivative-packet repair

## Objective

Author proposal-only R7/v1.22 successor bytes that preserve every immutable
R5/v1.20 and R6/v1.21 byte and repair exactly the four material findings in
the accepted v1.21 fresh-verifier return at SHA-256
`8a765c15ac195661ec8e82da874fec5ef8981f083c135f6e02378673b82fe423`:

1. C1015 must inspect the `Writable.end(chunk, callback)` error argument,
   persist its failure, and never mark completion successful when that
   argument is non-null.
2. C847 must bind the exact raw controller and attach-intent bytes through
   explicitly enumerated SHA-256 expectations. Every read, parse, and hash
   failure must enter a typed `FAILED_CLOSED_NO_LLDB_SPAWN` proof branch
   before any target-affecting progression.
3. Remove unbounded LLDB output callbacks from the deadline proof. Use a
   mechanically bounded output design, such as capped synchronous fd writes
   with explicit truncation evidence, so output handling cannot keep the
   supervisor alive past the absolute terminal path.
4. Enumerate and implement C1066's accepted-C1018/no-close exit-4 action
   exactly.

Do not change the replay/timing targets or broaden the architecture.

## Accepted basis and immutable history

- `AGENTS.md`
- `agents/AGENT_WORKING_ITEMS.md`
- committed standing plan selected by `loop/LOOP_INIT.md`
- `loop/LOOP_RECEIPTS.md` through Receipt 130
- `HANDOFF_STATE_R10.md`
- `MANAGER_FREEZE_V1_21.md`
- `reviews/A2_ATTEMPT8_V1_21_FRESH_ADVERSARIAL_VERIFIER_RETURN.md`
- all R5/v1.20 and R6/v1.21 packet surfaces and identities

R5/v1.20 and R6/v1.21 are immutable rejected history. Never edit, rename,
delete, or replace any existing byte in those generations.

## Declared reads

- The accepted basis above.
- `COMMAND_REGISTER_AMENDMENT_V1_20_PROPOSED.md` and
  `COMMAND_REGISTER_AMENDMENT_V1_21_PROPOSED.md`.
- `ATTEMPT_8_REAL_RUNTIME_COMMAND_APPROVAL_REQUEST_R5.md` and
  `ATTEMPT_8_REAL_RUNTIME_COMMAND_APPROVAL_REQUEST_R6.md`.
- `proposed/attempt8-r5/**` and `proposed/attempt8-r6/**`.
- Existing packet-author/verifier briefs and returns for structural precedent.

## Allowed tools

Read-only file inspection and `apply_patch` for the declared writes. Do not
run any proposed command or script. Do not run Node syntax, hashing, tests,
Git mutation, package, runtime, cache, network, helper, GUI, LLDB, attach,
signal, replay, credential, cleanup, rollback, deletion, release, Task
Management, or foreign-loop operations. The manager alone performs static
syntax, diff, whitespace, row, and hash checks after author interruption.

## Allowed write targets

Exactly these wholly new R7/v1.22 surfaces:

- `COMMAND_REGISTER_AMENDMENT_V1_22_PROPOSED.md`
- `ATTEMPT_8_REAL_RUNTIME_COMMAND_APPROVAL_REQUEST_R7.md`
- `proposed/attempt8-r7/README.md`
- `proposed/attempt8-r7/*.mjs`
- `instances/A2-DAPP92-A-ATTEMPT8-PACKET-09/TERMINAL_RETURN.md`

No other path is writable.

## Authoring contract

- Use one new, unique, contiguous command/action ID range after C1066.
- Every new read, raw-byte capture, SHA-256 computation, expected-hash bind,
  parse, typed proof write, capped write, byte-count update, truncation record,
  callback/error disposition, and process-exit action must be individually and
  literally enumerated in the new owner-gated register.
- The executable graph must not exceed the enumerated graph. Aggregate prose
  or implicit library behavior is insufficient authorization.
- Expected raw controller and attach-intent SHA-256 values must be explicit
  inputs to the supervisor invocation and must bind the exact accepted raw
  bytes. The supervisor must capture/read raw bytes once, hash those exact
  bytes, compare them before parsing, then parse those same exact bytes.
- All source read/hash/expected-hash/parse/binding failures must be caught in
  the typed fail-closed proof branch before LLDB spawn or any target-affecting
  progression.
- LLDB stdout/stderr handling must be mechanically byte bounded. Do not use
  unbounded `data` callbacks, growing arrays, or growing strings. Make
  truncation truthful and durably evidenced within the existing branch model.
- Preserve the exact 28.0-second and 102.0-second replay targets and the
  +149,000 ms and +149,900 ms supervisor targets.
- Add the distinct accepted-C1018/no-close exit-4 action literally to the
  command graph and implementation. Do not broaden other exit semantics.
- Preserve the App-only proposal scope and all existing negative authorities.
- The approval request must be decision-ready but must not claim verification,
  adoption, or authority.
- The terminal return must end with
  `AUTHORING_COMPLETE_WAITING_FOR_INTERRUPT`, identify all newly written
  paths, and state that no hashes or checks were run.

## Acceptance and escalation

Stop before computing any hash or running any check. Do not present an owner
token. If the exact four repairs cannot be represented without changing
timing targets, broadening the architecture, or touching immutable history,
write only the terminal return with a precise blocker and stop.
