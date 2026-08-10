# Agent 2 brief — D-APP-92 Attempt-8 v1.21 fresh adversarial verifier

RequestedBy: HELP_HUMAN through WORKING_ITEMS
RunID: `APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04`
ParentInstanceID: `A1-WORKING-ITEMS-DAPP92-V1-21`
ChildInstanceID: `A2-DAPP92-A-ATTEMPT8-V1-21-VERIFY-01`
PackageID: D-APP-92 Option A diagnostic packet
DeliverableID: complete frozen v1.21/R6 packet verification

## Independence and objective

You are a genuinely fresh, read-only adversarial verifier. You did not author
the R6/v1.21 proposal. Determine whether the exact frozen packet safely and
truthfully repairs all four blockers in the accepted v1.20 verifier return,
without broadening architecture, authority, timing, replay targets, or claims.
Return `PASS_FOR_OWNER_PRESENTATION_ONLY` or
`BLOCK_PACKET_REPAIR_REQUIRED`. Do not repair any byte.

## Frozen basis

- `MANAGER_FREEZE_V1_21.md`, accepted SHA-256
  `2040199d4d8a3431c021086d9689da018fef45a47943716c5163667badd23789`;
- every object and hash listed inside that freeze;
- accepted v1.20 verifier return SHA-256
  `47b57dae327e247c97a8957ad2cdf602b10ff64b94546babc3c5c1b8f5dbe655`;
- immutable `MANAGER_FREEZE_V1_20.md`, Receipt 129, and `HANDOFF_STATE_R9.md`;
- committed App loop plan and root/WORKING_ITEMS instructions;
- live worktree state only for containment, cleanliness, and absence checks.

## Mandatory first and final stability checks

Your first substantive act must independently reproduce the verifier brief,
manager freeze, amendment, request, PACKET-08 return, R6 README, and all ten
R6 script hashes. Confirm C787's literal ordered hash list reproduces the
accepted v1.20 verifier plus the ten scripts. Also reproduce the immutable
v1.20/R5 identities from `MANAGER_FREEZE_V1_20.md`.

After every semantic and static review, repeat the complete v1.21 hash pass as
your final substantive act. Any first/final mismatch, missing object, or R5
drift is an automatic block. Record both complete hash tables in the return.

## Required adversarial review

Review 100% of both proposal documents, README, author return, and all ten R6
scripts. At minimum prove or falsify:

1. **Enumeration and authority.** C787-C1066 is exactly 280 unique contiguous
   rows, external C787-C902 and internal C903-C1066. Every executable action,
   control, callback, timer, probe, signal, receipt write, cleanup step,
   rollback step, and deletion gate is individually enumerated. The request
   treats all authority as wholly new and infers nothing from C196/C197.
   Prospective-token language is exact, complete, non-adopted, and no broader
   than the literal command/action graph.
2. **Immediate target identity.** Before any C848 spawn/attach or other
   target-affecting progression, C847 must immediately bind exact target PID,
   PPID/controller direct-child relation, start identity, executable, accepted
   controller bytes, and attach-intent bytes. On any mismatch, the executable
   graph must issue no LLDB spawn/attach or target-affecting operation and must
   yield a truthful typed fail-closed proof.
3. **Deadline and timing.** Preserve the 28.0-second GUI target,
   102.0-second first-SIGTERM target, +149,000 ms watchdog, and +149,900 ms
   supervisor deadline. Prove there is no hidden timer reset, overrun, wait,
   unbounded callback, or exit path that contradicts the requested cap or
   branch claims.
4. **Terminal/error semantics.** For LLDB and every controller-owned child,
   `error` alone must be nonterminal. Only observed drained `close` may satisfy
   terminality, cancel settlement, authorize cleanup, support no-orphan, or
   select a terminal-safe branch. Callback/observer failures must remain
   contained and evidenced without fabricating terminality.
5. **Accepted watchdog/no-close branch.** Accepted C1018 with no drained LLDB
   close by +149,900 ms must select a unique explicit proof branch, retain the
   fixed root, withhold cleanup/durable-copy/rollback/deletion, and claim
   neither LLDB terminality, orphan absence, nor the 150-second maximum.
   Verify it cannot collide with identity-unsafe or any terminal-safe branch.
6. **C1009/C1014 stdin chain.** C1014 must require successful accepted C1009,
   its exact receipt, one supervisor ETX, exact whole-buffer equality and EOF.
   No bytes may forward before that gate or more than once. `child.stdin`
   stream and completion-callback errors must be trapped, preserve exact input
   evidence, never falsely mark success, and never bypass LLDB/controller
   settlement.
7. **Branch exhaustiveness and settlement.** Every reachable pre-controller,
   guard-failed, early-close, normal, watchdog-close, watchdog-race,
   post-start-abnormal, identity-unsafe, and accepted-watchdog/no-close state
   must map to exactly one truthful receipt/proof/cleanup disposition. Validate
   all controller-owned-child settlement paths independently, including error,
   identity-probe failure, signal rejection, delayed close, deadline, and
   cleanup-permission absence.
8. **Evidence and rollback.** Terminal-safe branches must freeze complete,
   credential-safe, deterministically sorted evidence before rollback. Both
   diagnostic retained-root branches must not claim durable-copy/rollback or
   deletion. Prove exact eight-hash rollback, empty frontend status, derivative
   absence, deletion permission, and durable-manifest postcondition.
9. **Static and boundary checks.** Run only static `node --check` on the ten R6
   scripts, row/placeholder/hash checks, candidate whitespace, and read-only
   Git/path/absence checks. Confirm frontend is clean, fixed temporary root and
   R6 durable evidence target are absent, and all new writes are App-only.

Aggregate cross-references are insufficient: reject the packet if any actual
operation or reachable state lacks a literal individual row, owner gate,
evidence binding, or truthful branch disposition.

## Tools and write boundary

Read-only file/Git inspection, hashing, static syntax checks, and mechanical
row/whitespace validation are allowed. Do not invoke a generated/proposed R6
script except `node --check`. Do not execute package, runtime, cache, network,
helper, GUI, LLDB, attach, signal, replay, credential, cleanup, rollback,
deletion, product, release, Git mutation, Task Management, or foreign-loop
operation.

Write exactly one new file:
`reviews/A2_ATTEMPT8_V1_21_FRESH_ADVERSARIAL_VERIFIER_RETURN.md`.
Do not modify any frozen object, decision state, receipt, manager, validation,
handoff, frontend, Git, or foreign-loop surface.

## Return contract

Record verdict, complete first/final hash tables, static results, each required
review disposition, exact material findings with file/line/action evidence,
branch-by-branch disposition, and explicit non-execution statement. On any
material defect return `BLOCK_PACKET_REPAIR_REQUIRED`; no token may issue and
no repair follows in this manager turn. On pass return
`PASS_FOR_OWNER_PRESENTATION_ONLY`; the prospective owner token remains
unadopted and no operation becomes authorized.
