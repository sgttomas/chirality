# D-APP-93 R4.4.6 successor return-namespace decision request

Status: `OWNER DECISION REQUIRED — RECOMMEND SIBLING SUCCESSOR NAMESPACE`

## Accepted state

- R4.4.5 execution intake is frozen at
  `intake_r4_4_5/INTAKE_FREEZE.md`, SHA-256
  `012ce18778b90798624a3491657e80d5238c7e04d984c6994c46364c0bcd0d91`,
  with verdict `STOP_INCOMPLETE`.
- The accepted `returned/` directory contains exactly 28 immutable objects
  and must not be moved, deleted, overwritten, or reused.
- The D-APP-93 overlay repair exists only as an unfrozen static draft. Its
  overlay SHA-256 is
  `5ae3d79bdb711153c315920ac4f4d584f6bab2d8d9d17fa2f08c31ed9242c7b7`;
  its expected post-overlay configuration hashes are
  `1cb9e4c7325166f69139eeba3a0bdfcfa1d4f871e03acf4af1809aa88fa02a36`
  and
  `b53a867e8aa7d8874cf7ce2417691a05d449babaa9bf0b905c550deb13b3ac6d`.

## Recommended decision

Authorize a mechanical successor rebind from the occupied live destination

`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_OPTION_A_OWNER_OPERATED_PREPARATION_2026-08-06/returned`

to the unoccupied sibling

`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_OPTION_A_OWNER_OPERATED_PREPARATION_2026-08-06/returned_r4_4_6`.

The rebind applies to every live successor absence gate, producer destination,
copy, transcript export, form path, hash-sidecar path, runbook instruction,
evidence-return reference, ingestion expectation, token, index, command
inventory, backcheck, and freeze cross-reference. It does not alter the
accepted `returned/` bytes or intake identities.

A read-only blast-radius audit found exactly 89 occurrences of the full live
destination pathname, all in `prepared/COMMAND_AUTHORITY_LEDGER.md`. Other
prepared surfaces refer to the destination semantically rather than embedding
that full pathname; they change only where the new successor namespace must be
named or hash-bound. Historical freezes, returned evidence, intake records,
and predecessor control records retain their original `returned/` references.

The exact fixed temporary root remains
`/private/tmp/chirality-dapp93-owner-operated-20260807`, which is presently
absent. The new D-APP-93-owned overlay continues to bind its Electron archive
under that root. C196/C197, the original SHA-720AD198 LLDB script, all
non-return-path command bytes, ordinary C1145→C1144→C1130 order,
terminal cut, raw packet semantics, failure routes, and all unrelated prepared
bytes remain unchanged.

After the mechanical rebind, WORKING_ITEMS must freeze a successor, stop for
HELP_HUMAN acceptance, and then dispatch exactly one genuinely fresh read-only
verifier whose checks include:

1. accepted `returned/` remains byte-identical with exactly 28 objects;
2. `returned_r4_4_6/` is absent before any future execution;
3. every live successor returned-path literal uses only `returned_r4_4_6`;
4. every live temp/archive/config literal uses the D-APP-93 fixed root;
5. zero operational D-APP-92 temp-root references remain;
6. preserved D-APP-92 C196/LLDB-script provenance remains exact; and
7. no other command, route, runtime, product, release, reliance, Git, task-
   management, or foreign-loop effect occurred.

## Exact requested authority

`AUTHORIZE D-APP-93 R4.4.6 SUCCESSOR RETURN-NAMESPACE REBIND ONLY — PRESERVE THE ACCEPTED 28-OBJECT returned/ SNAPSHOT BYTE-EXACT AND REBIND EVERY LIVE SUCCESSOR RETURN DESTINATION, ABSENCE GATE, COPY, EXPORT, FORM, SIDECAR, RUNBOOK, EVIDENCE, INGESTION, TOKEN, INDEX, INVENTORY, BACKCHECK, FREEZE, AND NECESSARY SAME-RUN CROSS-REFERENCE TO THE SIBLING returned_r4_4_6/ NAMESPACE; KEEP /private/tmp/chirality-dapp93-owner-operated-20260807 AND THE D-APP-93-OWNED OVERLAY AS DRAFTED; PRESERVE C196/C197, THE ORIGINAL SHA-720AD198 LLDB SCRIPT, EVERY NON-RETURN-PATH COMMAND BYTE, THE ORDINARY C1145→C1144→C1130 ORDER, THE TERMINAL CUT, RAW PACKET SEMANTICS, FAILURE ROUTES, AND ALL UNAFFECTED BYTES; THEN FREEZE THE SUCCESSOR AND DISPATCH ONE GENUINELY FRESH READ-ONLY VERIFIER WITH EXPLICIT ACCEPTED-SNAPSHOT, SUCCESSOR-NAMESPACE-ABSENCE, RUN-ROOT-CURRENCY, AND STALE-ROOT CHECKS — NO MOVE, DELETE, OVERWRITE, RUNTIME, DEBUGGER, PACKAGE, HELPER OR GUI, SIGNAL, CREDENTIAL, PRODUCT, RELEASE, RELIANCE, GIT, TASK MANAGEMENT, FOREIGN-LOOP, OR OTHER AUTHORITY`

Without that decision, no valid next-attempt token can be frozen: the current
successor preflight would stop immediately on the accepted occupied
`returned/` destination.
