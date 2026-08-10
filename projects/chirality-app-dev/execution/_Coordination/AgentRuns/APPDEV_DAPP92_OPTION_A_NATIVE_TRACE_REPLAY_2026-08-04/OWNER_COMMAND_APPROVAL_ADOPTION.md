# Owner command approval adoption — D-APP-92 Option A

Status: `ADOPTED — C196/C197 ONLY`

Owner direction received in the HELP_HUMAN coordination session on
2026-08-04, adopted verbatim:

> APPROVE D-APP-92 COMMAND C196 AND C197 — LLDB ATTACH TO THE SEALED DIRECT-CHILD HELPER PID ONLY, 150-SECOND MAXIMUM, ENUMERATED BREAKPOINT/BACKTRACE CAPTURE, THEN DETACH — NO OTHER DEBUGGER, PRIVILEGE, ENTITLEMENT, SECURITY, SIGNING, ADMIN, MEMORY, ENVIRONMENT, CREDENTIAL, OR PROCESS AUTHORITY

This approval changes only the state of C196 and C197 from `HELD` to
`OWNER_APPROVED`. It does not approve C052, C053, another debugger, another
PID, a PID search, a persistent security or entitlement change, credential
access, source instrumentation, product work, release work, Git effects, or
foreign-loop work.

C196 remains exactly:

```text
/usr/bin/xcrun lldb --batch -p <EXACT_HELPER_PID> -s /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt
```

The numeric replacement must be frozen before invocation and must be the
direct child returned by the sealed helper-launch wrapper. C197 remains only
the interrupt byte, `process detach`, and `quit` in that same LLDB session.
The absolute attach-to-detach bound is 150 seconds.
