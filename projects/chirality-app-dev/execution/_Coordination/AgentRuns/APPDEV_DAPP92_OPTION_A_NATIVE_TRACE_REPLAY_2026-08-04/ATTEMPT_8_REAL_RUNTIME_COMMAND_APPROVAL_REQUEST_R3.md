# D-APP-92 Attempt 8 R3 — v1.18 command approval request

Status: `PROPOSED — FRESH ADVERSARIAL VERIFIER REQUIRED BEFORE OWNER PRESENTATION`

V1.18 answers verifier
`93d5e64db0017f14b61c327cae86a009a103a10be593514ea39314bedb312b4e`
and preserves all v1.16/v1.17 bytes as rejected history. No proposed command
or script was executed. Static `node --check`, ID coverage, and read-only
SHA-256 checks are the only checks performed.

Frozen hashes:

- amendment v1.18: `f2aa50cb4dfc55a8f4d5c3c58e2d7a679081d66fd3978de696cee8ca5ff5fb39`;
- controller: `3bdcad4ff8136acbddab10b2e454ab05bf19a26baa85b2e19e9af3876ed2cc05`;
- same-PID sentinel: `36e7a99697d69d039c76893522e3a1e1ab8fb170ad42a843729f42d45678c43e`;
- LLDB supervisor: `da7034e4bc079c4e0c581f785bdb94fc2b27da0137350c69024166ef934062be`;
- LLDB terminal observer: `f73b4aa52ed999e376d8c6b13cb091cb1b15715488e59f2ea91fbf619e783179`;
- cleanup verifier: `ec420d0de8b0c9aa62fc9a1358a9ff52ff4ffa6127c1074e01bafd373e5407ab`;
- network scan: `4456f35254a34e3c1e8e0680f0d9f4321f2a578d9cc6b13b3e3f768cd34d1285`.

V1.18 contains every ID C375-C530 exactly once, plus C196/C197 exactly
once. C375-C466 and C525-C530 are individually enumerated external operations;
C467-C524 are separately gated script-internal executable/API operations.
There are no imported command ranges or aggregate “run prior rows” controls.

The registration CLI is a tracked direct child with bounded output, timeout,
exit race, and independent identity-guarded final settlement. Registration,
stale helper, GUI, and final helper settle independently, so one failure does
not skip another. Every signal has a live PID/PPID/start/command/text identity
proof; stale reaps are bounded.

The inherited C196 bytes are spawned by a dedicated supervisor into a separate
process group. Exactly one C197 ETX reaches the supervisor, which identity-
checks and forwards one C520 `SIGINT`; duplicate ETX fails closed. If C197 does
not terminate LLDB, new owner-gated C523 identity-checks and sends `SIGKILL` to
only that supervisor-owned LLDB child at 149.0 seconds, requiring its exit by
149.9 seconds. The observer accepts cleanup only after machine-readable PTY
terminal metadata hashes the C197 input, LLDB terminal receipt, and both raw
output streams. Normal C197 detach and forced watchdog terminality remain
distinct evidence states.

Durable evidence is copied before temporary deletion through individually
enumerated operations: runtime evidence and cleanup receipts, the complete
protocol tree, package transcript, network scan result/status, both PTY
transcripts and terminal metadata, binding/order/deviation logs, and final
hashes. Registration token/raw stdout and all credential values remain
excluded. Pre-mutation root cleanup and post-mutation exact rollback are
mechanically separate.

## Exact prospective owner token after fresh verifier acceptance

> APPROVE D-APP-92 ATTEMPT 8 R3 COMMANDS C375-C530, INCLUDING SCRIPT-INTERNAL ACTIONS C467-C524, AND INVOCATION OF THE SEPARATELY PREVIOUSLY APPROVED EXACT C196-C197 — ONE HASH-BOUND CANDIDATE RECONSTRUCTION AND PACKAGE, PUBLIC AUTHENTICATED REGISTRATION BY ONE TRACKED BOUNDED-REAPED DIRECT CHILD, MECHANICAL NO-NETWORK-ATTEMPT SCAN, LIVE PID/PPID/EXECUTABLE/START-BOUND OWNED CHILDREN, INDEPENDENT BEST-EFFORT SETTLEMENT, TWO-SESSION NATIVE TRACE, EXACTLY ONE C520 LLDB SIGINT FOR THE C197 ETX, AND C523 IDENTITY-GUARDED SIGKILL OF ONLY THE SUPERVISOR-OWNED LLDB CHILD AT 149.0 SECONDS IF STILL LIVE WITH TERMINAL REQUIRED BY 149.9 SECONDS, 28.0-SECOND/102.0-SECOND FIRST-SIGTERM REPLAY, MACHINE-BOUND TERMINAL/DETACH PROOF, INDIVIDUALLY ENUMERATED CREDENTIAL-FREE DURABLE EVIDENCE FREEZE, AND BRANCHED EXACT D-APP-89 ROLLBACK — NO NETWORK, CACHE SEED, STATIC-PID SIGNAL, OTHER PROCESS SIGNAL, CREDENTIAL VALUE, MEMORY OR ENVIRONMENT DUMP, PROCESS CENSUS, OTHER DEBUGGER, PRIVILEGE, ENTITLEMENT, SECURITY, SIGNING, ADMIN, PRODUCT REMEDY, ACCEPTANCE, RELEASE, RELIANCE, GIT, TASK MANAGEMENT, FOREIGN-LOOP, OR OTHER AUTHORITY

Fresh adversarial verifier acceptance remains mandatory before that token is
presented for owner reliance. D-APP-88 and DEL-09-04 remain open; TM-APP-036
remains unfired.
