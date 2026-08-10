# A2 Attempt-8 v1.18 fresh adversarial verifier brief

RequestedBy: `WORKING_ITEMS`

RunID: `APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04`

ParentInstanceID: `WI-DAPP92-A-ATTEMPT7-01`

ChildInstanceID: `A2-DAPP92-A-ATTEMPT8-V1-18-VERIFY-01`

PackageID: `PKG-09`

DeliverableID: `DEL-09-04`

Objective: independently and adversarially determine whether frozen Attempt-8
v1.18 is decision-ready for owner command approval. This is a read-only
proposal verification. Do not repair any file and do not execute any proposed
script or command.

## Accepted basis

- D-APP-92 Option A ruling and exact prior C196/C197 owner approvals.
- Attempt-7 fresh verifier SHA-256
  `1546dc33b24bbbd86d43d6b547b404113267e594b4eb6f0247c59455ad13ce6f`.
- v1.17 fresh blocker SHA-256
  `93d5e64db0017f14b61c327cae86a009a103a10be593514ea39314bedb312b4e`.
- v1.18 amendment claimed SHA-256
  `f2aa50cb4dfc55a8f4d5c3c58e2d7a679081d66fd3978de696cee8ca5ff5fb39`.
- v1.18 request claimed SHA-256
  `49630578673d138e0cb08ac27ec8e9ec7dab227f632dedb24d599088202ed49c`.
- packet-author return claimed SHA-256
  `a19de2274632c1ec4c1d563ffd6094ba6a4ebd51cc215070fc2c9478b9ef49dc`.

## Declared reads

Read the ruling/adoption, C196/C197 historical command authority, Attempt-7
evidence/verifier, v1.17 verifier, v1.18 amendment/request/packet return, all
six `proposed/attempt8-r3/*.mjs` files, the referenced LLDB command file, and
the exact source commands/files imported by literal path. Read other run-local
evidence only as necessary to verify claims.

## Allowed tools

- read-only filesystem and Git inspection;
- `/usr/bin/shasum -a 256`;
- static text search and parsing;
- `node --check` only for the six proposal scripts;
- candidate-whitespace and `git diff --check` read-only checks.

No proposed script may be invoked. No package, dependency, cache, network,
helper, GUI, LLDB, attach, signal, replay, credential, product mutation,
release, Git write, Task Management, or foreign-loop action is allowed.

## Allowed write target

Write exactly one return:

`reviews/A2_ATTEMPT8_V1_18_FRESH_ADVERSARIAL_VERIFIER_RETURN.md`

Do not modify proposal bytes.

## Mandatory adversarial checks

1. Recompute every claimed hash and Node-parse every proposal script without
   invoking it.
2. Prove C375-C530 is contiguous and each ID occurs exactly once, and C196 and
   C197 each occur exactly once with byte-exact inherited semantics.
3. Reject every aggregate cross-reference. Each formerly hidden shell command
   and every controller/sentinel/supervisor internal executable, spawn,
   ChildProcess signal, bounded wait, overflow/timeout cleanup action, and
   observer action must be a unique separately owner-gated row with exact
   executable/API semantics. Runtime placeholders must be narrowly typed and
   mechanically sourced; free-form runtime byte generation is not exact
   enumeration.
4. Verify registration is a tracked direct child, its exact node-mode
   environment and piped bounded public output are correct, no credential
   value/raw stdout survives, and every timeout/overflow/parse/helper-exit
   path reaches bounded identity-guarded settlement.
5. Exhaustively path-analyze stale/helper/GUI/registration cleanup. One
   failure must not skip another child. Reaps must be bounded. No signal may
   use a static/reused PID or occur without immediate PID/PPID/start/command/
   executable-text and live-handle guards.
6. Verify the inherited 150-second LLDB maximum mechanically on every path.
   Confirm exact C196 invocation, exact C197 input, one-and-only-one interrupt
   delivery, separate-process-group semantics, the new C520/C523 authority,
   watchdog start point and deadline arithmetic, and terminal confirmation by
   149.9 seconds. Identify any exception path that can orphan LLDB or escape
   the watchdog.
7. Verify detach/terminality is mechanically observable, fail-closed, and
   cannot be created by an assertion. The tool/session return must be bound to
   the same supervisor session, exact C197 input, stdout/stderr, LLDB identity
   and actual terminal result. Specifically test whether a merely nonempty or
   self-authored JSON object, an arbitrary integer exit code, a stale file, or
   a supervisor error can unlock cleanup.
8. Analyze every early-stop branch. In particular distinguish: C431 fails
   before controller record; controller exits before C434; C433 attach-intent
   exists but C434 fails before `lldb-start.json`; LLDB starts but attach
   fails; normal detach; watchdog-forced terminal. Each branch must have an
   executable, non-contradictory route to child cleanup, evidence freeze,
   exact rollback, fixed-root removal, and no unrelated-process signal. A
   branch must not require evidence from a session that never existed.
9. Verify durable evidence is frozen before temp deletion: complete protocol
   tree, package transcript, network scan status and result, both raw PTY
   transcripts/input/terminal metadata, cleanup receipts, action/order/
   binding/deviation evidence, and final hashes. Dynamic transcript/freezing
   controls must use exact templates and mechanical sources, not discretionary
   prose. Credentials must remain excluded.
10. Verify pre-mutation cleanup and every post-mutation/early-failure rollback
    path are literal, complete, and byte-restore the eight governed files while
    removing only the enumerated derivative paths. Verify frontend current
    state is clean and fixed temp/durable targets do not already exist.
11. Search scripts and commands for network primitives, environment/memory
    dumps, broad process census, static-PID signaling, extra debugger,
    privilege, entitlement, security, signing, admin, release, reliance, Git
    mutation, or other authority.
12. Compare the exact prospective owner token against every operation. Any
    operation not expressly covered, any false claim, or any ambiguity capable
    of broadening authority is blocking.

## Return contract

Return one of:

- `PASS_FOR_OWNER_COMMAND_APPROVAL_PRESENTATION_ONLY — EXECUTION REMAINS OWNER_GATED`; or
- `BLOCK_PACKET_REPAIR_REQUIRED`.

Report all blocking findings with file/line/ID evidence, frozen hashes,
enumeration results, prior-blocker disposition, static-check results, and an
explicit statement that no proposed operation executed. Verification evidence
does not authorize runtime execution, acceptance, remedy, release, reliance,
Git, Task Management, or foreign-loop action.
