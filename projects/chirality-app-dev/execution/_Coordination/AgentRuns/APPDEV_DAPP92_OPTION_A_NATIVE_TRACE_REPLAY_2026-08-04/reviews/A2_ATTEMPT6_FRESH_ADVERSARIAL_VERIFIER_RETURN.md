# Fresh adversarial verifier return — D-APP-92 Attempt 6 preparation

Verdict: `PASS_FOR_BOUNDED_TIMING_REPAIR_ONLY — REAL_RUNTIME_PACKET_BLOCKED`

## Independence and scope

This was a fresh, read-only adversarial review. No command was re-executed, no
repair was made, and no file outside this verifier return was written. The
review covered only the exact owner token, approval adoption, immutable v1.14
command graph and its bound proposal, frozen mock scripts, executor return,
command outcomes, LLDB transcript, current fixed-root absence, and current
frontend Git state.

## Bound-input verification

- The owner token transcribed in
  `OWNER_ATTEMPT6_PREPARATION_APPROVAL_ADOPTION.md` is byte-for-byte the token
  supplied in the HELP_HUMAN coordination session. It grants only C217-C230
  and expressly excludes attach, package, cache seed, network, helper, GUI,
  signal, replay, credential, release, Git, and all other authority.
- `COMMAND_REGISTER_AMENDMENT_V1_14.md` has current SHA-256
  `8d3adbcede92f812235406c11a68563e8fa2d52dc1bcf51ef2eba0bcbed07319`
  and incorporates the proposed graph without amendment.
- Its bound proposed-v1.14 SHA-256 independently recomputes exactly as
  `cf929fa33828a59db388576555dc37467710ac6246526ef262df0c39b42dfd45`.
- The approval-request SHA-256 independently recomputes exactly as
  `6bb8c99d3183552a4499b48d73876ebd4b4433c10bc993ed7fc162807c184797`.
- The bound prior-handoff SHA-256 independently recomputes exactly as
  `57ddd38db05a27f164d18163f014cbb97a02bd4356ee493ebb1d4d717c38bb3c`.
- The controller script independently recomputes exactly as
  `a6ebf793e38184f6cdb1b12fdda9a68360987b9e98bc84b09e966d168141538b`.
- The second-session script independently recomputes exactly as
  `02d651afbc13e7145de744977673aa54f4e9d7dd2411c06e2665537550ade11b`.

## Adversarial findings

1. **Exact command accounting is complete.** C217-C221 are recorded `PASS`;
   C222 reached its declared terminal five-second sentinel failure; C223-C224
   are recorded `PASS`; C225 correctly records the already-terminal C222
   session as `FAIL`; C226-C228 are correctly
   `NOT_EXECUTED_STOP_CONDITION` because no completed `protocol-result.json`
   existed; and mandatory C229-C230 are recorded `PASS`. Every ID C217-C230
   has exactly one disposition and no retry is claimed.

2. **The LLDB transcript is target-free.** Its only prompt commands are
   `help process attach` and `quit`. The former is a help query, not an attach
   invocation; no PID, process name, target, privilege request, or entitlement
   request appears. The startup `Could not load history file` notice is not a
   privilege or entitlement prompt. The evidence therefore supports C217-C219
   as a no-target help/quit PTY probe only.

3. **The frozen mock scripts implement the declared narrow protocol.** The
   controller spawns only its own direct child `/bin/sleep 10`, records the
   returned numeric child PID, polls for at most 100 intervals of 50 ms, and
   emits a result only after exact schema/PID/state matching and natural child
   exit. The second-session script reads only that record, validates the exact
   schema, `ATTACH_READY` state, positive safe-integer PID, and `/bin/sleep`
   executable, then writes one `SECOND_SESSION_ACKNOWLEDGED` sentinel with the
   same PID.

4. **The observed mock did not pass.** The executor return and command
   outcomes agree on direct-child PID `4457`, controller-record SHA-256
   `5b794e9a460b522e88910a40b77010e9fade519d042b3b131796ee64d4cbe535`,
   and a later schema-valid sentinel carrying PID `4457`. They also agree that
   session A exited `1` with the exact five-second sentinel error before it
   consumed that sentinel. Consequently no protocol result exists, sentinel
   consumption and natural child exit are unproved, and C226-C228 were
   correctly skipped.

5. **A bounded timing/order repair is supported, but no stronger cause is.**
   The matching-PID acknowledgment being written after the controller's
   bounded wait expired is sufficient evidence for a narrow amendment to the
   mock's waiting/coordination mechanism. It is not evidence that a longer
   wait alone is necessarily correct, and it is not real-runtime evidence.
   Because cleanup necessarily removed `controller.json` and the sentinel,
   the reported PID bytes and controller-record hash are no longer independently
   recomputable; this limits the accepted claim to the mutually consistent
   executor/outcomes record and frozen-script semantics.

6. **Cleanup and containment hold now.** The exact fixed root
   `/private/tmp/chirality-dapp92-attempt6-protocol` is absent. Both
   `git status --short -- projects/chirality-app-dev/frontend` and
   `git diff --exit-code -- projects/chirality-app-dev/frontend` are clean.
   The evidence directory contains only the command outcomes and no-target
   LLDB transcript; no protocol result is falsely presented.

7. **No excluded action is evidenced.** The complete command accounting and
   retained transcript show no target or attach, privilege or entitlement,
   package, cache seed, network, helper, GUI, signal, replay, credential,
   memory/environment inspection, release, Git, Task Management, or
   foreign-loop action. C196/C197 remain approved but unused.

## Gate disposition

Attempt 6 is accepted only as a correctly stopped preparation probe with
successful mandatory cleanup. It does **not** satisfy the mock handshake.
Preparation may proceed only to a fresh immutable, owner-gated bounded
timing/order repair packet. A real-runtime packet remains blocked until the
repaired mock produces and binds a successful protocol result with matching
PID/sentinel, controller consumption, and natural child exit. No real-runtime,
causal, remedy, implementation, release, or reliance inference is permitted.
