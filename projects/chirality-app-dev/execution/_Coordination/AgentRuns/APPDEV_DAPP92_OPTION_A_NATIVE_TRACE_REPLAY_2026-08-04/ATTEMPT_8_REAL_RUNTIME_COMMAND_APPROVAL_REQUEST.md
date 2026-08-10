# D-APP-92 Attempt 8 — real-runtime command approval request

Status: `DECISION-READY — OWNER COMMAND APPROVAL REQUIRED — NOT EXECUTED`

Attempt 7's fresh verifier accepted the mock two-session protocol under
SHA-256 `1546dc33b24bbbd86d43d6b547b404113267e594b4eb6f0247c59455ad13ce6f`.
That finding permits this packet to issue; it does not authorize Attempt 8.

## Proposed packet

- command-register amendment v1.16: SHA-256
  `6ddf4b0fca2556b27f05fffd0a20cfe29aeb713520909da93c631b3148ebc073`;
- `proposed/attempt8/real-runtime-controller.mjs`: SHA-256
  `11a97d620e7f742e04d91418a1bbbeec2d1ef20b43e48596b75900c8cba4bd2f`;
- `proposed/attempt8/real-second-session-sentinel.mjs`: SHA-256
  `a75b91299cb20f7daa2154a2ba9b36e4f71235ed634bfe81f80d16d7874d4242`;
- `proposed/attempt8/real-runtime-fallback-cleanup.mjs`: SHA-256
  `ed577526d8d1122c24b96db1f62e4e796341bce27878145498288f94a1c19fec`.

The proposed scripts were prepared as immutable packet bytes only. They have
not been run or syntax-checked. Commands C245-C335 likewise have not run.
C196/C197 are preserved byte-for-byte from their separate prior owner
approval and may be invoked only at the exact direct-child PID produced by
this packet.

The packet performs one complete hash-bound candidate reconstruction and one
`desktop:pack`, launches a sealed stale owner and then the final direct-child
helper, authenticates through the packaged public CLI without retaining token
bytes, launches the GUI at helper-ready + 28.0 seconds, and sends the first
ordinary SIGTERM at authenticated-contact + 102.0 seconds. LLDB is bounded to
the inherited C196/C197, one direct-child PID, enumerated breakpoints and
backtraces, and 150 seconds. At most 80 exact-PID existence polls separated by
0.1 seconds follow the signal.

The new pre-attach sentinel makes detach terminality mechanical even when
C196 begins but fails before trace-ready. Evidence freeze, fallback cleanup,
product rollback, and removal of the fixed runtime root are all ordered after
both sessions are terminal. Any drift, unexpected output, network attempt,
PID/schema/timing mismatch, or missing detach proof stops the success path.

## Owner decision token

Approve exactly:

> APPROVE D-APP-92 ATTEMPT 8 COMMANDS C245-C335 AND INVOCATION OF THE SEPARATELY PREVIOUSLY APPROVED C196-C197 — ONE HASH-BOUND CANDIDATE RECONSTRUCTION/PACKAGE, SEALED STALE-OWNER RECOVERY, DIRECT-CHILD HELPER, TWO-SESSION LLDB TRACE, PUBLIC AUTHENTICATED REGISTRATION, 28.0-SECOND/102.0-SECOND FIRST-SIGTERM REPLAY, BOUNDED EVIDENCE FREEZE, DETACH, QUIESCENCE, CLEANUP, AND EXACT D-APP-89 ROLLBACK — NO NETWORK, CREDENTIAL VALUE, MEMORY OR ENVIRONMENT DUMP, PROCESS CENSUS, OTHER DEBUGGER, PRIVILEGE, ENTITLEMENT, SECURITY, SIGNING, ADMIN, PRODUCT REMEDY, ACCEPTANCE, RELEASE, RELIANCE, GIT, TASK MANAGEMENT, FOREIGN-LOOP, OR OTHER AUTHORITY

Until that token is received, this packet has no execution, product, release,
reliance, Git, Task Management, or acceptance effect. D-APP-88 and DEL-09-04
remain open; TM-APP-036 remains unfired.
