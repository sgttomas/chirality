# Exact command-level approval request — D-APP-92 Option A

Status: `OWNER APPROVAL REQUIRED BEFORE INVOCATION`

## Requested command

Approve only:

```text
/usr/bin/xcrun lldb --batch -p <EXACT_HELPER_PID> -s /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt
```

`<EXACT_HELPER_PID>` is constrained to the direct child PID returned by the
future sealed launch of the hash-bound Electron 43.2.0 runtime-helper package.
The expanded numeric PID is frozen in the command ledger before invocation.
No process-name search or other target is authorized.

Also approve only the cleanup control for that existing LLDB session: interrupt
byte `\u0003`, then `process detach` and `quit`, after first-signal settlement
or at the 150-second absolute trace bound.

## Why separate approval is required

LLDB `lldb-2100.0.17.203` uses macOS task attachment. Even for a same-user,
run-owned process, this crosses the D-APP-92 command-level debugger privilege/
Developer Tools authorization or entitlement boundary. No generic debugger,
shell, admin, SIP/security, signing, or persistent entitlement grant is sought.

## Scope, capture, redaction, and cleanup

- One run-owned helper PID only, from ready through first-SIGTERM settlement.
- Maximum trace duration: 150 seconds.
- Captures timestamped breakpoint names and at most 16 native stack frames at
  native signal trampoline, libuv handler, Node SignalWrap, Electron Browser
  quit, and AppKit terminate seams.
- Existing redacted App logs supply teardown/Root-stop observables.
- Captures no memory dump/read, expression, environment, token, keychain item,
  credential, secret, owner HOME, GUI contents, network content, or unrelated
  process state.
- LLDB detaches; all run-owned helper/GUI processes, sockets/owners, packages,
  source reconstruction, dependency projection, and isolated runtime paths are
  then removed/restored under separately enumerated unprivileged commands.

## Exact owner return token

`APPROVE D-APP-92 COMMAND C196 AND C197 — LLDB ATTACH TO THE SEALED DIRECT-CHILD HELPER PID ONLY, 150-SECOND MAXIMUM, ENUMERATED BREAKPOINT/BACKTRACE CAPTURE, THEN DETACH — NO OTHER DEBUGGER, PRIVILEGE, ENTITLEMENT, SECURITY, SIGNING, ADMIN, MEMORY, ENVIRONMENT, CREDENTIAL, OR PROCESS AUTHORITY`
