# A2 Attempt-8 v1.19 fresh adversarial verifier return

Status: `COMPLETE`

Verdict: `BLOCK_PACKET_REPAIR_REQUIRED`

V1.19 is not decision-ready for owner command-approval presentation. The
manager freeze is stable, and several v1.18 defects are repaired, but the
frozen controller and LLDB supervisor retain material child-orphan, deadline,
PID-identity, branch-closure, and authority-provenance defects. No proposed
operation was executed.

## Frozen-byte, row, and static results

- Verifier brief SHA-256:
  `fcee373380bd0e7a3ba101feb8f0df8c9d3c74097c04ac0834767083e16951b3`.
- Manager freeze SHA-256:
  `2bdc153c1550d20bc64dd14f53b6b0212c7c2fac020349e083ee2ee20f3dd001`.
- Amendment, request, and author-return SHA-256 values:
  `627d00ec7d520dab98e4cc9b9cf7d542ad64f5a723de4bab413b03800cecafa7`,
  `b67cf4563378fa212e6426fdbbaed41f04255c2e989ea2a578baddc519e1ad10`,
  and `2fdc2c330875ead3b5223f886b78e96fbe2b9b9afc0841e792b935966a7a78a5`.
- Accepted v1.18 verifier SHA-256:
  `b2fce5f287c06fce400d60588fee70d4d40d6dbbfab87aa46f52be591f45fe70`.
- R4 script SHA-256 values, in C531 literal path order:
  `856a2fc990cac99f9aacfee2c6393e637d16a2d165707178000e5de7db9c1786`,
  `1007d9f29cb50b2d1b26f854ab94ecbd92f019a14c9b1000311c51d9759f8a33`,
  `2c3d738831860f2b292e9822933a454e38ec311982ce2394059bf86596a8b611`,
  `09caaa917046c762fff0f73aa55bf263af3128a4d808bb39b4d338f9abc918b4`,
  `89bf3f3a884170ffe2b4f09f9808c5ec7da4de7207c946fd593d398bfe6b2ead`,
  `f739c663095423bd4844c4896ee75526227e9f8192211d287dfc3c19b2448e62`,
  `fedb6530585e38ceb8aa7d4412a0d32c6712cc5e6971ffe48d18196bbb768628`,
  `9e2244f29ff597c58b0e9808c62dddaf0cee0701d78d65bdf282f60a1cd74903`,
  `b190ec40d3511cc23bc17a936c101cbb36f25032662124f30de8c4466e3ff27b`,
  and `09181ceab9e4c0e180cabc47a12660cae400141229bcba6cc055d28dd6200650`.
- The eleven C531 paths and hashes exactly match the freeze and occur in the
  same order. All frozen hashes reproduced on two separated pre-review passes
  and on the final post-review pass. No drift was observed. The author
  instance was interrupted before review and remained interrupted at the
  final state check.
- C531-C786 is contiguous and unique: 256 rows, each ID exactly once. External
  rows C531-C636 count 106 and internal rows C637-C786 count 150. C196 and
  C197 each occur exactly once, for 258 total command/action rows.
- C196's executable and arguments match v1.9. The C197 implementation does
  not preserve its inherited control semantics; this is blocker 5 below.
- All ten R4 scripts pass `node --check`. Candidate-whitespace and
  `git diff --check` pass. The frontend scoped Git status is exactly empty.
  The fixed temporary root and durable R4 evidence target are absent.
  Historical R3 script hashes reproduce the rejected-history identities
  recorded by the v1.18 verifier.

## Blocking findings

### 1. Critical — controller settlement can cancel its watchdog and orphan a live child

`real-runtime-controller-r4.mjs` lines 100-118 clears the child's 170-second
watchdog at line 102, then calls the throwing identity-guarded `signalOwned`
at line 104 outside the `try` that invokes the direct-handle fail-safe. If the
C690/C691, C696/C697, C702/C703, or C713/C714 identity probe fails, control
jumps to `settleIndependent`, which only records `terminal:false`; C694,
C700, C708, or C717 is never called and the watchdog has already been
cancelled. The same defect exists after a successful GUI TERM if the later
C706/C707 probe throws. This contradicts amendment lines 306-312 and the
prospective token's independent bounded settlement claim. It can leave a
registration, stale-helper, GUI, or helper child live with no remaining
terminal mechanism.

### 2. Critical — detached LLDB can escape its supervisor and the +149.9-second wait is not absolute

`lldb-session-supervisor-r4.mjs` spawns detached LLDB at lines 58-60. Its
stdout/stderr and stdin event callbacks at lines 97-152 perform throwing
synchronous writes and buffer operations outside the terminal-path
`try/catch`; an exception terminates the supervisor and its in-process
watchdog, leaving detached LLDB orphaned. Separately, line 161 awaits
`owned.exit` without a deadline. The +149.9-second race at lines 162-171 is
reached only after that await resolves or a different caught exception occurs.
If C737/C738 does not produce an exit event, the supervisor waits
indefinitely and never enforces C745. Waiting for `exit` rather than stream
`close` also allows lines 173-180 to close/hash files before all LLDB output
has drained. These paths falsify the no-orphan and observed-terminal-by-
spawn+149.9 claims in amendment lines 314-321 and in the prospective token.

### 3. Critical — C738 and the controller fail-safes are not PID-reuse safe

The alleged direct-child-handle-only escape hatches call
`ChildProcess.kill('SIGKILL')` without a current identity proof
(`lldb-session-supervisor-r4.mjs` lines 50-55; controller lines 60-64).
The JavaScript object comparison proves only that the stored object is the
same object; it does not prove that its numeric POSIX PID still names the same
OS process after an exit/reap-to-JavaScript-event race. C738 is specifically
used after the identity route fails, so the packet cannot prove that its
signal reaches only the owned LLDB child. The same issue affects C694, C700,
C708, and C717. This violates the mandatory no-PID-reuse/static-PID condition
and the token's claim that C738 can signal only that same LLDB child.

### 4. High — the five branches are not exhaustive over executable LLDB failure paths

After `lldb-start.json` exists, any non-watchdog LLDB terminal caused by
attach failure, debugger error, rejected/partial C197 input, or another
nonzero exit is labeled `NORMAL_TERMINAL` by supervisor lines 183-196. It
cannot satisfy `LLDB_TERMINAL_BEFORE_ATTACH` because a start file exists,
cannot satisfy `NORMAL_EXACT_DETACH`, and cannot satisfy
`FORCED_WATCHDOG_TERMINAL` (receipt lines 34-36; proof lines 22-33). No branch
can therefore create cleanup permission. The controller then times out C689
and withholds helper/GUI settlement. This contradicts the asserted exhaustive
five-branch law and the requirement that every early-stop path continue
independent cleanup, evidence freeze, and rollback.

### 5. High — C197 is new direct-signal authority, not the exact inherited PTY control

V1.9 approves C197 only as control of the existing LLDB PTY: send the ETX byte,
then the exact detach/quit bytes, with `no kill/security change`. R4 creates
LLDB with piped stdio, not a PTY (supervisor lines 58-60), consumes ETX as a
signal to the Node supervisor, and translates it into
`child.kill('SIGINT')` (lines 100-110; C734). Buffer-until-EOF enforcement for
the detach/quit bytes is sound, but the interrupt mechanism is not the exact
previously approved C197 operation. Although the prospective token mentions
C734, it simultaneously represents C196/C197 as separately previously
approved exact authority. That provenance statement is false and must be
repaired: C734 must be presented solely as new explicit authority, without
claiming exact inheritance from the PTY-only C197 approval.

## Prior-blocker disposition

V1.19 closes the v1.18 byte-drift blocker, forwards no detach/quit byte before
EOF and exact whole-buffer equality, replaces free-form transcript generation,
adds deterministic durable hashing, and makes exact rollback hash/status/
absence assertions. It does not close the governing orphan/deadline and
branch-closure blockers: the controller settlement bug, detached-supervisor
exception paths, unbounded exit wait, identity-free numeric signals, and
missing post-start abnormal-terminal branch remain blocking. The exact-C197
inheritance claim also remains materially inaccurate.

This verdict authorizes no token presentation or execution, acceptance,
remedy, release, reliance, Git action, Task Management action, or foreign-loop
action. No R4 proposal script or command, package, dependency, cache, network,
helper, GUI, LLDB, attach, signal, replay, credential, or product operation
was executed.
