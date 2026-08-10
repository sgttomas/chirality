# D-APP-92 Attempt 8 R4 — v1.19 command approval request

Status: `PROPOSED — MANAGER FREEZE AND FRESH ADVERSARIAL VERIFIER REQUIRED BEFORE OWNER PRESENTATION`

V1.19 answers the fresh v1.18 verifier at SHA-256
`b2fce5f287c06fce400d60588fee70d4d40d6dbbfab87aa46f52be591f45fe70`.
V1.16-v1.18 and `proposed/attempt8-r3/**` remain unchanged rejected history.
No R4 proposal script or command was executed. The author intentionally did
not compute or state final R4 hashes; the manager must independently freeze
all final bytes before dispatching a genuinely fresh verifier.

The standalone register contains one literal, unique, contiguous R4 range
C531-C786 plus exact C196 and C197. It makes five terminal branches mutually
exclusive: pre-controller/no session B; controller but no LLDB spawn; LLDB
terminal before mechanically observed attach/start; normal exact detach; and
forced watchdog terminal. Every branch has honest receipts, evidence freeze,
independent rollback, exact eight-hash/status/absence assertions, and guarded
fixed-root removal without requiring artifacts from a nonexistent session.

Every controller child handle is assigned to the outer registry immediately
after spawn; its exit/error listener and bounded owned-handle watchdog are
installed before a write, wait, identity probe, or PID validation. Each child
settles independently. The LLDB deadline starts immediately before C196
spawn. Listeners and the +149.0-second watchdog precede every protocol write
and identity probe. C737 is the normal identity-guarded watchdog SIGKILL;
C738 is new, explicit, owner-gated direct-child-handle-only fail-safe authority
when the watchdog identity route itself fails. LLDB terminality is required by
spawn+149.9 seconds.

C197 accepts exactly one ETX/SIGINT. The supervisor buffers stdin through EOF,
requires byte equality with `process detach\nquit\n`, and forwards the whole
buffer once. It closes/rejects partial, arbitrary, overlong, duplicate, or
extra bytes without forwarding them.

The proof binds controller PID, supervisor PID, session ID, target PID, LLDB
PID and start identity, spawn-attempt/start hashes, exact input/stdout/stderr
hashes, exact exit, null supervisor error, and the exact target detach line.
Early and forced terminality remain separately and honestly labeled. Cleanup
permission is written only after the applicable complete binding passes.
Frozen deterministic scripts create the typed terminal receipt, exact
transcript copies/absence receipt, sorted durable evidence manifest, cleanup
verdict, network-scan proof, and rollback permission. No free-form base64 or
dynamic prose is accepted.

## Exact prospective owner token after manager freeze and verifier acceptance

> APPROVE D-APP-92 ATTEMPT 8 R4 COMMANDS C531-C786, INCLUDING EVERY SCRIPT-INTERNAL ACTION C637-C786, AND INVOCATION OF THE SEPARATELY PREVIOUSLY APPROVED EXACT C196-C197 — ONE HASH-FROZEN CANDIDATE RECONSTRUCTION AND PACKAGE; ONE TRACKED BOUNDED PUBLIC REGISTRATION CHILD; EXACT OWNED HELPER, GUI, REGISTRATION, SUPERVISOR, AND LLDB CHILD HANDLES WITH IMMEDIATE OUTER REGISTRATION, EXIT LISTENERS, INDEPENDENT SETTLEMENT, AND BOUNDED WATCHDOGS; FIVE MUTUALLY EXCLUSIVE PRE-CONTROLLER, NO-LLDB-SPAWN, LLDB-TERMINAL-BEFORE-ATTACH, NORMAL-EXACT-DETACH, AND FORCED-WATCHDOG-TERMINAL BRANCHES; EXACTLY ONE C734 LLDB SIGINT FOR THE ONE C197 ETX; C737 IDENTITY-GUARDED SIGKILL OF ONLY THE SUPERVISOR-OWNED LLDB CHILD AT SPAWN PLUS 149.0 SECONDS; NEW C738 OWNER-GATED DIRECT-CHILD-HANDLE-ONLY FAIL-SAFE SIGKILL OF THAT SAME LLDB CHILD IF ITS WATCHDOG IDENTITY PROBE OR TERMINAL-PATH SETUP FAILS; LLDB TERMINAL REQUIRED BY SPAWN PLUS 149.9 SECONDS; NO LLDB STDIN FORWARDING UNTIL EOF AND WHOLE-BUFFER BYTE EQUALITY WITH EXACT `process detach\nquit\n`; 28.0-SECOND GUI AND 102.0-SECOND FIRST-SIGTERM REPLAY; SAME-SESSION MACHINE-BOUND TERMINAL PROOF; DETERMINISTIC CREDENTIAL-FREE TRANSCRIPT, RECEIPT, AND SORTED DURABLE EVIDENCE-MANIFEST CREATION BEFORE TEMPORARY DELETION; AND INDEPENDENT EXACT D-APP-89 ROLLBACK WITH EIGHT LITERAL HASH COMPARISONS, EXACTLY EMPTY FRONTEND STATUS, DERIVATIVE ABSENCE, AND DELETE-PERMISSION GATE — NO NETWORK, CACHE SEED, STATIC-PID OR UNOWNED SIGNAL, ORPHAN, CREDENTIAL VALUE, MEMORY OR ENVIRONMENT DUMP, BROAD PROCESS CENSUS, OTHER DEBUGGER, PRIVILEGE, ENTITLEMENT, SECURITY, SIGNING, ADMIN, PRODUCT REMEDY, ACCEPTANCE, RELEASE, RELIANCE, GIT MUTATION, TASK MANAGEMENT, FOREIGN-LOOP, OR OTHER AUTHORITY

Fresh verifier acceptance and a subsequent owner act remain mandatory. This
request itself authorizes nothing. D-APP-88 and DEL-09-04 remain open;
TM-APP-036 remains unfired.
