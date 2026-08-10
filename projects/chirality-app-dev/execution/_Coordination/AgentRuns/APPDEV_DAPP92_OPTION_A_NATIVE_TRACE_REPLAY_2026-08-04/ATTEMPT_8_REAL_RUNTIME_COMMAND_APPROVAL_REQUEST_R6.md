# D-APP-92 Attempt 8 R6 — v1.21 command approval request

Status: `PROPOSED — NOT PRESENTED — NOT ADOPTED — MANAGER HASH/FREEZE AND FRESH ADVERSARIAL VERIFIER REQUIRED`

This derivative request answers only the four material findings in the
immutable v1.20 fresh-verifier return at SHA-256
`47b57dae327e247c97a8957ad2cdf602b10ff64b94546babc3c5c1b8f5dbe655`.
It preserves every v1.20/R5 byte as rejected history and adopts, approves, and
executes nothing.

The standalone v1.21 register enumerates every operation in one unique,
contiguous range C787-C1066: external commands/controls C787-C902 and
script-internal actions C903-C1066. Historical C196/C197 are unused context
only. The manager must independently hash, statically check, and freeze every
R6 byte, then dispatch one genuinely fresh read-only adversarial verifier.
This request may be presented only on that verifier's acceptance.

## Four bounded repairs

1. C847 immediately re-proves the controller's direct-child helper using
   exact PID, PPID, start identity, executable, accepted attach-intent, and
   controller bindings before C848 can spawn LLDB. Failure writes the typed
   `FAILED_CLOSED_NO_LLDB_SPAWN` receipt, exits 5, performs no attach or other
   target-affecting operation, and is proved only as
   `CONTROLLER_NO_LLDB_SPAWN`.
2. Every controller-owned child and LLDB records `error` independently from
   drained `close`. `error` alone never satisfies terminality, cancels a
   settlement deadline, authorizes cleanup, or supports an orphan-absence
   claim. Terminal-safe proofs require `observedEvent:close` and
   `streamsDrained:true`.
3. Accepted C1018 without observed drained LLDB `close` by spawn+149,900 ms is
   the exact `WATCHDOG_SIGNAL_ACCEPTED_NO_CLOSE_AT_DEADLINE` diagnostic branch.
   It retains the fixed root and claims neither the LLDB time cap, LLDB
   terminality, orphan absence, cleanup, rollback, nor deletion.
4. C1014 forwarding requires one accepted identity-guarded C1009 plus its
   typed C1010 receipt and exact whole-buffer equality. C1013 and C1015 trap
   `child.stdin` stream and completion-callback errors, preserve the exact
   input/evidence bytes, and cannot bypass settlement.

The 28.0-second GUI target, 102.0-second first-SIGTERM target, spawn+149,000 ms
watchdog, spawn+149,900 ms supervisor deadline, package/registration design,
credential minimization, evidence freeze, and exact rollback remain otherwise
unchanged.

## Authority newly requested

All C787-C1066 authority is requested as wholly new authority. In particular:

- C847 is the immediate exact target-identity guard and typed pass/fail receipt.
- C848 is the exact non-detached `/usr/bin/xcrun lldb --batch` attach to the
  guarded direct-child helper PID and frozen trace script only.
- C853 is exactly one supervisor ETX followed by exact bytes
  `process detach\nquit\n` and EOF; it is not historical C197.
- C1009 is one live-identity-guarded `SIGINT` from the supervisor to its owned
  LLDB child.
- C1014 is one exact whole-buffer LLDB-stdin write after the accepted C1009,
  its receipt, EOF, and byte equality.
- C1018 is one live-identity-guarded `SIGKILL` to the supervisor-owned LLDB
  child at spawn+149,000 ms. Failed identity proof issues no signal.

No other attach, debugger, signal, stdin, process, privilege, credential, or
runtime authority is inferred.

## Exact branch disposition

Seven terminal-safe branches require drained close and exact typed proof:
`PRE_CONTROLLER_NO_SESSION_B`, `CONTROLLER_NO_LLDB_SPAWN` (only the proved
C847 fail-closed state), `LLDB_TERMINAL_BEFORE_ATTACH`,
`NORMAL_EXACT_DETACH`, `FORCED_WATCHDOG_TERMINAL`,
`WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL`, and
`POST_START_ABNORMAL_LLDB_TERMINAL`.

Two diagnostic no-close branches retain the root and permit no cleanup,
durable-copy, rollback, deletion, terminality, orphan-absence, or 150-second
claim: `UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE` and
`WATCHDOG_SIGNAL_ACCEPTED_NO_CLOSE_AT_DEADLINE`.

## Exact prospective owner token

The following token is derivative packet text only. It is unpresented,
unadopted, and non-authorizing unless manager freeze, fresh-verifier acceptance,
and a later independent owner act all occur:

> APPROVE D-APP-92 ATTEMPT 8 R6 COMMANDS C787-C1066, INCLUDING EVERY SCRIPT-INTERNAL ACTION C903-C1066 — ALL AUTHORITY IS WHOLLY NEW; ONE HASH-FROZEN CANDIDATE RECONSTRUCTION AND PACKAGE; ONE MECHANICAL NO-NETWORK-ATTEMPT SCAN; ONE TRACKED BOUNDED PUBLIC REGISTRATION CHILD; ONE CONTROLLER-RECORDED DIRECT-CHILD HELPER, ONE BOUNDED GUI CHILD, AND ONE NON-DETACHED SUPERVISOR-OWNED LLDB CHILD; NEW C847 IMMEDIATE EXACT PID/PPID/START/EXECUTABLE/ATTACH-INTENT/CONTROLLER TARGET GUARD WITH TYPED FAIL-CLOSED NO-LLDB-SPAWN RECEIPT; NEW C848 EXACT LLDB ATTACH TO THAT GUARDED HELPER PID AND THE FROZEN TRACE SCRIPT ONLY; NEW C853 EXACTLY ONE SUPERVISOR ETX FOLLOWED BY EXACT BYTES `process detach\nquit\n` AND EOF; NEW C1009 LIVE-IDENTITY-GUARDED LLDB-CHILD SIGINT; NEW C1014 ONE WHOLE-BUFFER LLDB-STDIN WRITE ONLY AFTER EOF, BYTE EQUALITY, ACCEPTED C1009, AND ITS RECEIPT, WITH C1013/C1015 STREAM/CALLBACK ERROR CONTAINMENT; NEW C1018 LIVE-IDENTITY-GUARDED LLDB-CHILD SIGKILL AT SPAWN PLUS 149.0 SECONDS; SEVEN DRAINED-CLOSE TERMINAL-SAFE BRANCHES; TWO SEPARATE RETAINED-ROOT DIAGNOSTIC BRANCHES FOR IDENTITY-UNSAFE NO-SIGNAL AND ACCEPTED-SIGKILL-WITHOUT-DRAINED-CLOSE, EACH MAKING NO 150-SECOND-MAXIMUM, LLDB-TERMINAL, ORPHAN-ABSENCE, CLEANUP, ROLLBACK, TEMPORARY-DELETION, RELEASE, OR RELIANCE CLAIM; 28.0-SECOND GUI LAUNCH AND 102.0-SECOND FIRST-SIGTERM REPLAY; SAME-SESSION MACHINE-BOUND RECEIPTS AND PROOFS; CREDENTIAL-FREE TRANSCRIPT AND DETERMINISTIC SORTED DURABLE EVIDENCE FREEZE ON TERMINAL-SAFE BRANCHES; AND INDEPENDENT EXACT D-APP-89 ROLLBACK WITH EIGHT LITERAL HASH COMPARISONS, EXACTLY EMPTY FRONTEND STATUS, DERIVATIVE ABSENCE, AND DELETE-PERMISSION GATE — NO HISTORICAL C196/C197 INHERITANCE, NETWORK, CACHE SEED, STATIC-PID OR UNOWNED SIGNAL, CREDENTIAL VALUE, MEMORY OR ENVIRONMENT DUMP, BROAD PROCESS CENSUS, OTHER DEBUGGER, PRIVILEGE, ENTITLEMENT, SECURITY, SIGNING, ADMIN, PRODUCT REMEDY, ACCEPTANCE, RELEASE, RELIANCE, GIT MUTATION, TASK MANAGEMENT, FOREIGN-LOOP, OR OTHER AUTHORITY

## Gate state

No owner token exists. D-APP-88 and DEL-09-04 remain open; TM-APP-036 remains
unfired. No proposed command or generated script was executed while authoring.
