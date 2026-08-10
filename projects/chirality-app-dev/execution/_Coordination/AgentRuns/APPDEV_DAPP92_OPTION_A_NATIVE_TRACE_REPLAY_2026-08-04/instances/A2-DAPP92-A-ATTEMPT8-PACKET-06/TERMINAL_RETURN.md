# A2 D-APP-92 Attempt-8 packet-06 repair-author terminal return

Status: `BLOCKED_REGISTER_SYNCHRONIZATION_INCOMPLETE`

The fresh successor author applied bounded proposal-only repairs for all seven
manager findings, but stopped before owner-request authoring because the
convergence gate froze further register edits while the branch-law section was
still inconsistent with the repaired rows and scripts. The result is useful
successor proposal material, not an authoring-complete packet.

## Applied proposal-only repairs

1. Unsafe transcript capture is now admitted, including a bounded `BOTH`
   session form.
2. Unsafe-to-signal evidence accepts either a present, bound start receipt or
   a truthful absent-start state.
3. The supervisor removes its persistent SIGINT/stdin listeners, pauses stdin,
   closes its evidence descriptors, writes the terminal receipt, and uses an
   explicit bounded process exit for every branch.
4. Controller cleanup tags C954-C977 now match registration, stale, GUI,
   helper, and independent-completion operations; generic fallback outcomes
   are explicitly tagged C978-C983.
5. Replay-terminal evidence-write failure is trapped inside `finally` and can
   no longer bypass independent child settlement.
6. The proposal distinguishes a terminal-observed, 150-second-compliant trace
   from `LLDB_MAXIMUM_NOT_PROVED_IDENTITY_UNSAFE`; the latter retains the root
   and makes no cap/no-orphan claim. C1010 is described only as wholly new,
   identity-bound owner authority.
7. A watchdog-signal-accepted concurrent terminal has its own
   `WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL` receipt/proof/transcript branch.

The live R5 directory contains ten `.mjs` files plus `README.md`. The R7
statement of eleven `.mjs` files remains byte-preserved historical text; the
successor README and amendment record the corrected current count.

## Remaining blocker

`COMMAND_REGISTER_AMENDMENT_V1_20_PROPOSED.md` is not mechanically complete.
Its branch-law table still omits
`WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL`, still maps the abnormal and unsafe
branches through the superseded C861-C864 meanings, still requires a start
receipt for every unsafe case, and still says six rather than seven
terminal-safe branches. In addition, the supervisor classification order can
label a watchdog-terminal event with no initial start receipt as
`LLDB_TERMINAL_BEFORE_ATTACH_OBSERVED`; that state is not yet reconciled with
the new watchdog proof branches. A prospective exact owner token would
therefore be misleading and was not authored.

## Files changed

- `COMMAND_REGISTER_AMENDMENT_V1_20_PROPOSED.md`
- `proposed/attempt8-r5/README.md`
- `proposed/attempt8-r5/lldb-session-supervisor-r5.mjs`
- `proposed/attempt8-r5/real-runtime-controller-r5.mjs`
- `proposed/attempt8-r5/session-terminal-receipt-r5.mjs`
- `proposed/attempt8-r5/session-terminal-proof-r5.mjs`
- `proposed/attempt8-r5/transcript-capture-r5.mjs`
- this fresh `instances/A2-DAPP92-A-ATTEMPT8-PACKET-06/TERMINAL_RETURN.md`

## Static checks

- All ten current R5 `.mjs` files passed `node --check`.
- `git diff --check` passed for the amendment and R5 proposal directory.
- Targeted `rg` inspection confirmed the repaired cleanup rows and C1051-C1057
  action references, and exposed the remaining branch-law contradiction above.

No script was executed beyond static `node --check`. No proposed command,
runtime, package, cache, network, helper, GUI, LLDB, attach, signal, replay,
credential, release, Git, or foreign-loop action occurred. No SHA-256 value or
other final hash was computed. No manager freeze or verifier was created.
`ATTEMPT_8_REAL_RUNTIME_COMMAND_APPROVAL_REQUEST_R5.md` was deliberately not
created. No prospective owner token is present, presented, or adopted.
