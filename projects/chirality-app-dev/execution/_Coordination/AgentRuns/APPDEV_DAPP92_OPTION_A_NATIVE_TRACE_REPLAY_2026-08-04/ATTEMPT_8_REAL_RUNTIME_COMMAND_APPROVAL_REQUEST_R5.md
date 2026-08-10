# D-APP-92 Attempt 8 R5 — v1.20 command approval request

Status: `PROPOSED — NOT PRESENTED — NOT ADOPTED — MANAGER FREEZE AND FRESH ADVERSARIAL VERIFIER REQUIRED`

This request implements the ruled D-APP-92 Option A planning baseline and is
bounded by Receipt 127, HANDOFF_STATE_R7, and the WORKING_ITEMS Brief
Amendments V2/V3. It answers only the rejected v1.19 verifier at SHA-256
`2c8f8a1db7e207783a556c4a2e5d5f6f676cb32f63ade9cc4b384f2dc7302e8b`
and the exact PACKET-06 synchronization blocker. It does not adopt, approve,
or execute any proposed byte.

The standalone v1.20 register enumerates every operation in one unique,
contiguous range C787-C1057: external commands and session controls C787-C900
and script-internal actions C901-C1057. There are no inherited command ranges,
aggregate “run prior rows” controls, or free-form substitutions. Historical
C196/C197 are unused context only and supply no authority to this packet.

The manager must independently insert and freeze all final R5 hashes, then
dispatch one genuinely fresh adversarial verifier. This request may be
presented to the owner only if that verifier accepts the exact frozen bytes.

## Authority newly requested

All C787-C1057 authority is requested as new authority. In particular:

- C847 newly authorizes the exact non-detached `/usr/bin/xcrun lldb --batch`
  attach to the controller-recorded direct-child helper PID and the frozen
  trace script only.
- C852 newly authorizes exactly one ETX to the supervisor followed by the
  exact bytes `process detach\nquit\n` and EOF. It is not historical C197.
- C1003 newly authorizes one live PID/PPID/start/text-identity-guarded `SIGINT`
  from the supervisor to its owned LLDB child in response to that one ETX.
- C1007 newly authorizes one whole-buffer LLDB-stdin write only after EOF,
  exact byte equality, and exactly one accepted C1003 event.
- C1010 newly authorizes one live PID/PPID/start/text-identity-guarded
  `SIGKILL` to the supervisor-owned LLDB child at spawn origin +149,000 ms.
  Failed identity proof issues no signal and enters the diagnostic failure
  branch.

No other attach, debugger, signal, stdin, process, privilege, credential, or
runtime authority is inferred from these operations.

## Exact branch and deadline disposition

Exactly one of eight mechanically selected branches applies:

1. `PRE_CONTROLLER_NO_SESSION_B`;
2. `CONTROLLER_NO_LLDB_SPAWN`;
3. `LLDB_TERMINAL_BEFORE_ATTACH`;
4. `NORMAL_EXACT_DETACH`;
5. `FORCED_WATCHDOG_TERMINAL`;
6. `WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL`;
7. `POST_START_ABNORMAL_LLDB_TERMINAL`; or
8. `UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE`.

The first seven are terminal-safe branches. Each requires its exact typed
receipt/proof and permits controller cleanup, credential-free durable evidence
freeze, independent exact rollback, and fixed-root deletion only after all
applicable gates pass. A watchdog identity proof at C1008-C1009 may truthfully
supply the C999 start receipt when the initial C997-C998 observation did not;
that receipt is written before C1010 and before classification fan-in.

For each first-seven observed-terminal branch, the terminal proof requires
`elapsedMs <= 150000` and records a 150-second-compliant observed-terminal
trace. The eighth branch is instead the explicit diagnostic result
`LLDB_MAXIMUM_NOT_PROVED_IDENTITY_UNSAFE`: it permits no signal after failed
identity proof, no cleanup permission, no durable-copy or rollback claim, no
temporary-root deletion, and no assertion of the LLDB 150-second maximum,
LLDB-child terminality, or no-orphan state. Its start receipt is truthfully
optional, and the fixed root is retained.

The controller independently settles registration and stale children on all
paths. It settles GUI and helper only after an exact terminal-safe permission
proof. The seven terminal-safe paths freeze evidence before rollback; the
identity-unsafe diagnostic path stops with its typed proof and retained root.

## Exact prospective owner token

The following token is prospective only. It is included for decision review,
has not been presented, is not adopted, and authorizes nothing unless the
manager freeze and fresh verifier first accept these exact bytes and the owner
then issues the token as a new act:

> APPROVE D-APP-92 ATTEMPT 8 R5 COMMANDS C787-C1057, INCLUDING EVERY SCRIPT-INTERNAL ACTION C901-C1057 — ALL AUTHORITY IS WHOLLY NEW; ONE HASH-FROZEN CANDIDATE RECONSTRUCTION AND PACKAGE; ONE MECHANICAL NO-NETWORK-ATTEMPT SCAN; ONE TRACKED BOUNDED PUBLIC REGISTRATION CHILD; ONE CONTROLLER-RECORDED DIRECT-CHILD HELPER, ONE BOUNDED GUI CHILD, AND ONE NON-DETACHED SUPERVISOR-OWNED LLDB CHILD; NEW C847 EXACT LLDB ATTACH TO THAT HELPER PID AND THE FROZEN TRACE SCRIPT ONLY; NEW C852 EXACTLY ONE SUPERVISOR ETX FOLLOWED BY EXACT BYTES `process detach\nquit\n` AND EOF; NEW C1003 LIVE-IDENTITY-GUARDED LLDB-CHILD SIGINT; NEW C1007 ONE WHOLE-BUFFER LLDB-STDIN WRITE ONLY AFTER EOF, BYTE EQUALITY, AND EXACTLY ONE C1003; NEW C1010 LIVE-IDENTITY-GUARDED LLDB-CHILD SIGKILL AT SPAWN PLUS 149.0 SECONDS; SEVEN TERMINAL-SAFE PRE-CONTROLLER, NO-LLDB-SPAWN, LLDB-TERMINAL-BEFORE-ATTACH, NORMAL-EXACT-DETACH, FORCED-WATCHDOG-TERMINAL, WATCHDOG-SIGNAL-ACCEPTED-RACE-TERMINAL, AND POST-START-ABNORMAL-LLDB-TERMINAL BRANCHES WITH OBSERVED TERMINALITY PROVED WITHIN 150 SECONDS; ONE SEPARATE `LLDB_MAXIMUM_NOT_PROVED_IDENTITY_UNSAFE` BRANCH THAT ISSUES NO UNPROVED SIGNAL, RETAINS THE FIXED ROOT, AND MAKES NO 150-SECOND-MAXIMUM, LLDB-TERMINAL, CLEANUP, ROLLBACK, TEMPORARY-DELETION, OR NO-ORPHAN CLAIM; 28.0-SECOND GUI LAUNCH AND 102.0-SECOND FIRST-SIGTERM REPLAY; SAME-SESSION MACHINE-BOUND RECEIPTS AND PROOFS; CREDENTIAL-FREE TRANSCRIPT AND DETERMINISTIC SORTED DURABLE EVIDENCE FREEZE ON TERMINAL-SAFE BRANCHES; AND INDEPENDENT EXACT D-APP-89 ROLLBACK WITH EIGHT LITERAL HASH COMPARISONS, EXACTLY EMPTY FRONTEND STATUS, DERIVATIVE ABSENCE, AND DELETE-PERMISSION GATE — NO HISTORICAL C196/C197 INHERITANCE, NETWORK, CACHE SEED, STATIC-PID OR UNOWNED SIGNAL, CREDENTIAL VALUE, MEMORY OR ENVIRONMENT DUMP, BROAD PROCESS CENSUS, OTHER DEBUGGER, PRIVILEGE, ENTITLEMENT, SECURITY, SIGNING, ADMIN, PRODUCT REMEDY, ACCEPTANCE, RELEASE, RELIANCE, GIT MUTATION, TASK MANAGEMENT, FOREIGN-LOOP, OR OTHER AUTHORITY

## Gate state

This document is `PROPOSED`, `NOT PRESENTED`, and `NOT ADOPTED`. No owner token
exists unless and until the owner independently issues it after the required
freeze and verifier acceptance. D-APP-88 and DEL-09-04 remain open;
TM-APP-036 remains unfired.
