# A2 Attempt-8 v1.19 fresh adversarial verifier brief

RequestedBy: `WORKING_ITEMS`

RunID: `APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04`

ParentInstanceID: `WI-DAPP92-A-ATTEMPT7-01`

ChildInstanceID: `A2-DAPP92-A-ATTEMPT8-V1-19-VERIFY-01`

PackageID: `PKG-09`

DeliverableID: `DEL-09-04`

Objective: independently determine whether manager-frozen v1.19 is
decision-ready for owner command approval. This is a read-only proposal
verification. Do not repair any file and do not execute any proposed script
or command.

## Freeze basis

Read `MANAGER_FREEZE_V1_19.md` SHA-256
`2bdc153c1550d20bc64dd14f53b6b0212c7c2fac020349e083ee2ee20f3dd001`
first. Before any substantive review, independently recompute every hash in
that manifest twice, separated by other read-only work, and confirm the author
instance is interrupted. Any mismatch or drift is an immediate critical
blocker. The frozen amendment/request/author-return hashes are respectively:

- `627d00ec7d520dab98e4cc9b9cf7d542ad64f5a723de4bab413b03800cecafa7`;
- `b67cf4563378fa212e6426fdbbaed41f04255c2e989ea2a578baddc519e1ad10`;
- `2fdc2c330875ead3b5223f886b78e96fbe2b9b9afc0841e792b935966a7a78a5`.

Accepted prior blocker: v1.18 verifier SHA-256
`b2fce5f287c06fce400d60588fee70d4d40d6dbbfab87aa46f52be591f45fe70`.

## Allowed reads and tools

Read D-APP-92 ruling/adoption; exact historical C196/C197 authority; Attempt-7
verifier and whitespace-repair backcheck; v1.18 verifier; v1.19 freeze,
amendment, request, author return, all ten `proposed/attempt8-r4/*.mjs` files,
the LLDB command file, and referenced source/baseline artifacts as necessary.

Allowed tools are read-only filesystem/Git inspection, static text parsing,
`/usr/bin/shasum -a 256`, `node --check` on the ten r4 scripts only,
candidate-whitespace, and `git diff --check`. No proposal script may be
invoked. No package, dependency, cache, network, helper, GUI, LLDB, attach,
signal, replay, credential, product mutation, release, Git write, Task
Management, or foreign-loop action is allowed.

## Allowed write target

Write exactly one return:

`reviews/A2_ATTEMPT8_V1_19_FRESH_ADVERSARIAL_VERIFIER_RETURN.md`

## Mandatory adversarial checks

1. Confirm freeze stability first and last; confirm C531's literal path order
   and eleven ordered hashes exactly match the manager freeze.
2. Prove C531-C786 is contiguous and unique and C196/C197 each appear once
   with exact inherited semantics. Reject aggregate imported ranges or one row
   that hides multiple materially distinct executable/signal/wait actions.
3. Enumerate and cross-check every external command/control and internal
   executable, spawn, signal, bounded wait, identity probe, branch selection,
   evidence write, cleanup step, and rollback assertion against its numeric
   row and the prospective owner token.
4. Path-analyze immediate child ownership: outer registry assignment, exit/
   error listener and watchdog installation must occur before any operation
   capable of throwing. Every stale/helper/GUI/registration child must reach
   independent bounded direct-handle settlement on every pre/post-controller
   failure path. No PID reuse/static-PID signal is allowed.
5. Path-analyze the LLDB supervisor from the instant before spawn through
   terminal receipt. Confirm the hard origin, listener/watchdog ordering,
   identity-guarded C737 and direct-child-handle-only C738 fail-safe, event-loop
   deadline semantics, and observed terminality by +149.9 seconds on every
   throwing/probe/failure path. Confirm no detached LLDB orphan is possible.
6. Prove exact C197 enforcement: one ETX only; buffer until EOF; reject
   partial/arbitrary/overlong/duplicate/post-EOF input without forwarding any
   byte; only the exact whole `process detach\nquit\n` buffer is forwarded once.
7. Verify five branches are mutually exclusive, mechanically selected, and
   executable: pre-controller/no session B; controller/no LLDB spawn; LLDB
   terminal before attach/start; normal exact detach; forced watchdog
   terminal. No branch may require an artifact/session that never existed.
8. Verify same-session proof binds controller/supervisor/session/target/LLDB
   PID and start, spawn-attempt/start hashes, exact input/stdout/stderr hashes,
   exact exit, null supervisor error, exact target-PID detach line or honest
   branch-specific terminal reason. Cleanup permission must be impossible
   before complete branch binding.
9. Verify deterministic transcript capture/no-session receipt, network status,
   cleanup verdict, protocol/runtime/package evidence freeze, and sorted
   durable hash manifest. No free-form operator-synthesized runtime bytes and
   no credential/raw registration stdout may enter durable evidence.
10. Verify every early-stop branch continues rollback independently, restores
    exact eight governed hashes, requires an actually empty scoped Git status,
    proves derivative/build/dependency absence, writes delete permission only
    after all assertions, and retains the temp baseline if any assertion fails.
11. Verify frontend is currently Git-clean, fixed temp and durable r4 target
    are absent, static parse/whitespace checks pass, and historical r3 bytes
    remain rejected history.
12. Search for network primitives, env/memory dumps, broad process census,
    unowned/static signals, extra debugger/privilege/security/signing/admin,
    release/reliance/Git mutation, or other unrequested authority.
13. Compare every actual operation and branch against the exact prospective
    token. Any false statement, omitted authority, discretionary substitution,
    or material ambiguity is blocking.

## Return contract

Return exactly one verdict:

- `PASS_FOR_OWNER_COMMAND_APPROVAL_PRESENTATION_ONLY — EXECUTION REMAINS OWNER_GATED`; or
- `BLOCK_PACKET_REPAIR_REQUIRED`.

Report hashes, stability observations, row counts, static checks, all blockers
with file/line/ID evidence, prior-blocker disposition, and explicit confirmation
that no proposed operation executed. A pass authorizes token presentation only,
not execution, acceptance, remedy, release, reliance, Git, Task Management, or
foreign-loop action.
