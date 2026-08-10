# Agent 2 brief — D-APP-92 Attempt-8 v1.21 bounded packet author

RequestedBy: HELP_HUMAN through WORKING_ITEMS
RunID: `APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04`
ParentInstanceID: `A1-WORKING-ITEMS-DAPP92-V1-21`
ChildInstanceID: `A2-DAPP92-A-ATTEMPT8-PACKET-08`
PackageID: D-APP-92 Option A diagnostic packet
DeliverableID: bounded Attempt-8 v1.21 derivative-packet repair

## Objective

Author proposal-only R6/v1.21 successor bytes that preserve v1.20/R5 as
immutable rejected history and repair exactly the four material blockers in
the accepted v1.20 fresh-verifier return at SHA-256
`47b57dae327e247c97a8957ad2cdf602b10ff64b94546babc3c5c1b8f5dbe655`.

## Accepted basis and declared reads

- root `AGENTS.md` and `agents/AGENT_WORKING_ITEMS.md`;
- committed App loop plan;
- Receipt 129;
- `MANAGER_FREEZE_V1_20.md`;
- `HANDOFF_STATE_R9.md`;
- the v1.20 fresh-verifier return named above;
- `COMMAND_REGISTER_AMENDMENT_V1_20_PROPOSED.md`;
- `ATTEMPT_8_REAL_RUNTIME_COMMAND_APPROVAL_REQUEST_R5.md`;
- `proposed/attempt8-r5/**`;
- earlier immutable run evidence only as needed to preserve exact existing
  timing, replay, rollback, and authority boundaries.

## Exact repair scope

1. Add an immediate, exact C847 target identity guard before any
   target-affecting progression. The guard must re-prove the controller's
   direct-child helper using exact PID, PPID, start identity, executable, and
   the accepted attach-intent/controller bindings immediately before LLDB
   spawn/attach. Failure must issue no LLDB spawn/attach or target-affecting
   operation and must enter a truthful fail-closed branch.
2. Distinguish every child `error` event from drained terminal `close`/`exit`.
   `error` alone must never satisfy terminality, cancel a settlement deadline,
   authorize cleanup, or support a no-orphan claim. This applies both to the
   LLDB supervisor and controller-owned children.
3. Represent accepted C1010 with no observed LLDB `close` by an explicit,
   truthful fail-closed proof branch. It must retain the fixed root and claim
   neither the LLDB time cap nor orphan absence/LLDB terminality. Do not
   silently classify it as identity-unsafe or terminal-safe.
4. Make C1007 depend on an accepted/successful C1003 identity-guarded signal,
   not merely an attempted interrupt. Trap and contain `child.stdin` callback
   and stream errors, preserve exact input/evidence bytes, and ensure such
   errors cannot bypass settlement or evidence of the failure state.

Do not broaden the architecture. Do not alter the 28.0-second/102.0-second
replay targets, the +149,000 ms watchdog point, the +149,900 ms supervisor
deadline, or other accepted timing. Any newly introduced operation, control,
callback, probe, receipt write, branch action, or signal must be individually
enumerated in a unique contiguous owner-gated command/action range. Existing
operation identities may be renumbered only as necessary to maintain one
literal, gap-free successor range.

## Allowed writes

Only new successor surfaces:

- `COMMAND_REGISTER_AMENDMENT_V1_21_PROPOSED.md`;
- `ATTEMPT_8_REAL_RUNTIME_COMMAND_APPROVAL_REQUEST_R6.md`;
- `proposed/attempt8-r6/**`;
- `instances/A2-DAPP92-A-ATTEMPT8-PACKET-08/TERMINAL_RETURN.md`.

Do not modify, rename, or delete any existing file, including every v1.20/R5
byte. Do not write decision-state, receipt, validation, manager-freeze,
handoff, review, Git, frontend, or foreign-loop surfaces.

## Allowed tools and execution boundary

Read-only inspection and file editing are allowed. Do not execute any proposed
command or generated script. Do not run package, runtime, cache, network,
helper, GUI, LLDB, attach, signal, replay, credential, cleanup, rollback,
deletion, product, release, Git mutation, Task Management, or foreign-loop
operation. Do not compute final SHA-256 identities. Do not run `node --check`;
the manager owns all static syntax/hash/freeze checks.

## Required output and stop protocol

Create the two proposal documents, a complete R6 script/README directory, and
a terminal-return draft recording `AUTHORING_COMPLETE — AWAITING_MANAGER_HASH`.
The proposal must include a prospective exact owner token only as derivative
packet text, clearly unadopted and non-authorizing. It must not be presented to
the owner.

After all writes are complete, message the parent with
`AUTHORING_COMPLETE_WAITING_FOR_INTERRUPT`, then remain alive and make no
further read or write. Do not return normally. The manager will interrupt the
session before independently hashing and freezing the bytes.

## Acceptance and escalation

- Exactly the four named blockers are repaired without architectural, timing,
  replay-target, or authority broadening.
- Every new action is individually enumerated and owner-gated.
- V1.20/R5 history is byte-identical.
- No proposed operation or script is executed.
- Any ambiguity, inconsistency, or inability to finish inside this bounded
  repair causes a stopped return with no hashes and no owner token claim.
