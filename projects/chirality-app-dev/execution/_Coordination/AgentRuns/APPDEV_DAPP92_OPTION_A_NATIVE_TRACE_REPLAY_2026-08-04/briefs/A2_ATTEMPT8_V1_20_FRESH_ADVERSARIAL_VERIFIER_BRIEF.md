# A2 brief — D-APP-92 Attempt-8 v1.20 fresh adversarial verifier

RequestedBy: `WORKING_ITEMS`
RunID: `APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04`
ParentInstanceID: `WI-DAPP92-A-R5-DOCFREEZE-01`
ChildInstanceID: `A2-DAPP92-A-ATTEMPT8-V1-20-VERIFY-01`
PackageID: `PKG-09`
DeliverableID: `DEL-09-04`

## Objective

Perform one genuinely fresh, read-only adversarial review of the exact frozen
v1.20 R5 command packet. Return either
`PASS_FOR_OWNER_PRESENTATION_ONLY` or `BLOCK_PACKET_REPAIR_REQUIRED`. Do not
repair any byte and do not execute any proposed command, control, or script.

## Frozen basis

- manager freeze:
  `MANAGER_FREEZE_V1_20.md`
  SHA-256 `e3e4dc3035038ebbc8c980e3a5fe587ae22b8274a8e3e31bd37c008af83da0f6`;
- amendment:
  `COMMAND_REGISTER_AMENDMENT_V1_20_PROPOSED.md`
  SHA-256 `e281e17e13a080cc0e045cf4fb3f435c8f6a0bf47976302cd194ef4ce037c771`;
- request:
  `ATTEMPT_8_REAL_RUNTIME_COMMAND_APPROVAL_REQUEST_R5.md`
  SHA-256 `9a928ea97472ac6cd77b5b89885439d0ef536f629fc6b7157b3a41a3f68eca9d`;
- PACKET-07 return:
  `instances/A2-DAPP92-A-ATTEMPT8-PACKET-07/TERMINAL_RETURN.md`
  SHA-256 `90ab9c698e5c8f3fe42939fd0f0692b27eb72920bdb74a381fe6e875266fef28`;
- rejected v1.19 verifier:
  `reviews/A2_ATTEMPT8_V1_19_FRESH_ADVERSARIAL_VERIFIER_RETURN.md`
  SHA-256 `2c8f8a1db7e207783a556c4a2e5d5f6f676cb32f63ade9cc4b384f2dc7302e8b`;
- all R5 script and README hashes exactly as listed in the manager freeze.

## Reads and tools

Read root `AGENTS.md`, `agents/AGENT_TASK.md`, the frozen basis above, R7/R8
handoffs and validations, PACKET-06 blocker return, all ten R5 `.mjs` files,
R5 `README.md`, and the exact trace script. You may use read-only `rg`,
`shasum`, `node --check`, `git diff --check`, candidate-whitespace validation,
scoped Git status, and fixed-path absence tests. Do not invoke an R5 script
except `node --check`; do not run any C787-C1057 operation.

AllowedWriteTargets: only
`reviews/A2_ATTEMPT8_V1_20_FRESH_ADVERSARIAL_VERIFIER_RETURN.md`.

## Acceptance audit

1. Recompute every frozen hash as the first substantive act and again as the
   final act. Any drift is `BLOCK`.
2. Prove C787-C1057 contains exactly 271 unique contiguous rows, with no
   placeholder, aggregate prior-range invocation, or free-form substitute.
   Recompute C787's ordered hashes literally.
3. Cross-check every external row and every internal action against the exact
   scripts. In particular audit all child spawns, identity probes, signals,
   interrupt/stdin operations, absolute deadlines, callback/error paths,
   evidence writes, transcript operations, cleanup, durable copy, rollback,
   and deletion gates. An operation not individually enumerated is `BLOCK`.
4. Prove the controller child registry, current PID/PPID/start/executable
   identity guards, already-live settlement deadlines, independent settlement,
   and replay-terminal write-failure path match the claims. No identity-free
   or static-PID signal may be hidden.
5. Prove the supervisor is non-detached, installs terminal/deadline observers
   before waits, tears down listeners, drains through stream `close`, writes
   bound receipts, and terminates every observed-terminal branch within the
   stated bound. Audit the C1008/C1009 late C999 start receipt before C1010 and
   the classification ordering for both SIGKILL and concurrent-race terminal.
6. Audit the eight mutually exclusive branches end to end through external
   row, receipt, transcript, proof, controller permission, cleanup, evidence,
   rollback, and root disposition: exactly seven terminal-safe branches and
   one `LLDB_MAXIMUM_NOT_PROVED_IDENTITY_UNSAFE` diagnostic failure. The unsafe
   branch may have start present or absent but must claim no 150-second LLDB
   maximum, LLDB terminality, cleanup, rollback, deletion, or no-orphan state.
7. Confirm normal detach forwards no byte before EOF and exact whole-buffer
   equality, and requires exactly one accepted supervisor ETX/new C1003.
8. Confirm C847, C852, C1003, C1007, and C1010 are requested only as wholly
   new authority; no C196/C197 inheritance claim or hidden privilege/security/
   process authority may remain.
9. Audit credential minimization, mechanical network-attempt scan, durable
   evidence ordering/manifest, exact eight-hash frontend rollback, frontend
   cleanliness, derivative absence, and fixed-root deletion gates.
10. Confirm request/token wording is no broader than the exact rows and does
    not imply approval, execution, product remedy, acceptance, release,
    reliance, Git, Task Management, or foreign-loop authority.
11. Run static syntax, whitespace, diff, frontend cleanliness, fixed-root and
    durable-evidence-target absence checks. These checks are supporting
    evidence only; semantic defects still `BLOCK`.

## Return contract

Write one evidence-first return naming all recomputed hashes, row counts,
branch dispositions, checks, and every material finding with exact file/line
references. `PASS_FOR_OWNER_PRESENTATION_ONLY` means only that HELP_HUMAN may
present the prospective token for a new owner act; it authorizes no execution.
On any material mismatch return `BLOCK_PACKET_REPAIR_REQUIRED`; do not include
or restate a token on `BLOCK`.
