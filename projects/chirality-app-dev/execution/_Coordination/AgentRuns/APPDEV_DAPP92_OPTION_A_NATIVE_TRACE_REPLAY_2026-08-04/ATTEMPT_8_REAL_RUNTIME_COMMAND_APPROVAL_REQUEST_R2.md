# D-APP-92 Attempt 8 R2 — repaired real-runtime command approval request

Status: `DECISION-READY — FRESH VERIFICATION AND OWNER APPROVAL REQUIRED — NOT EXECUTED`

This v1.17 package preserves v1.16 and its request as rejected history and
repairs every blocker in verifier R2
`ebb81fb33524eb68ef0a3435d5e594a17f13044420330570cbcf9b114955a2d8`.

Frozen bytes:

- v1.17 amendment: `94309f250bc5a8489c34e5328c920ff66c19a89a9c08e5e348fce76335be39df`;
- controller R2: `6da4821fb04550af01e4deaf0c05c398f93267f1c75e7c764f660e50c8c02059`;
- sentinel R2: `30f8bd60858a4c86fb7cb8ca0a4350b41b8c69ac78116c1d9fbcb2768c726213`;
- cleanup verifier R2: `690b1b10d0afa48fc9963d4e4722121032880b15b8eb97c5f53a5be2a298ba26`.

The repair binds live PID, PPID, executable text, command, and start identity
immediately before C196 and every signal; uses only live controller-owned
ChildProcess handles for signals; exhaustively reaps stale, final-helper, and
GUI handles on every controller path; emits a pre-controller cleanup-safe
receipt if no controller record exists; and makes the former fallback a
no-signal receipt verifier. A five-poll contact window and absolute ready+
139.5-second replay and ready+148.0-second detach-terminal deadlines retain
the 28.0-second, 102.0-second, and 80×0.1-second bounds with strict slack
inside C196's 150-second maximum. Package output receives a mechanical
no-network-attempt scan before runtime. Cleanup receipts precede durable copy.
A mutation marker separates partial pre-mutation root cleanup from exact
post-mutation baseline rollback.

No proposed command or script has been run or syntax-checked. Fresh
adversarial verification of these bytes is required before owner reliance.
C196/C197 retain their exact separate prior approval.

## Exact owner token after fresh verifier acceptance

> APPROVE D-APP-92 ATTEMPT 8 R2 COMMANDS C336-C374 AND INVOCATION OF THE SEPARATELY PREVIOUSLY APPROVED C196-C197 — ONE HASH-BOUND CANDIDATE RECONSTRUCTION/PACKAGE, MECHANICAL NO-NETWORK-ATTEMPT SCAN, LIVE PID/PPID/EXECUTABLE/START-BOUND DIRECT-CHILD HELPER, CONTROLLER-OWNED-HANDLE SIGNALS ONLY, TWO-SESSION LLDB TRACE, PUBLIC AUTHENTICATED REGISTRATION, 28.0-SECOND/102.0-SECOND FIRST-SIGTERM REPLAY, 139.5-SECOND REPLAY AND 148.0-SECOND DETACH-TERMINAL DEADLINES, BOUNDED EVIDENCE FREEZE AFTER CLEANUP RECEIPTS, EXHAUSTIVE OWNED-CHILD REAP, AND BRANCHED EXACT D-APP-89 ROLLBACK — NO NETWORK, STATIC-PID SIGNAL, CREDENTIAL VALUE, MEMORY OR ENVIRONMENT DUMP, PROCESS CENSUS, OTHER DEBUGGER, PRIVILEGE, ENTITLEMENT, SECURITY, SIGNING, ADMIN, PRODUCT REMEDY, ACCEPTANCE, RELEASE, RELIANCE, GIT, TASK MANAGEMENT, FOREIGN-LOOP, OR OTHER AUTHORITY

Until fresh verifier acceptance and that token, this package has preparation
effect only. D-APP-88 and DEL-09-04 remain open; TM-APP-036 remains unfired.
