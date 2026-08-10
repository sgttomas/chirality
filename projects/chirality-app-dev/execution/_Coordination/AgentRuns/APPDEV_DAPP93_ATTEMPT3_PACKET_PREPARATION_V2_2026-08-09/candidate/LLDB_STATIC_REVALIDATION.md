# Attempt-3 v2 static LLDB-script revalidation

Verdict: `PASS_STATIC_ONLY — EXECUTION FITNESS AND SYMBOL RESOLUTION UNKNOWN`

Historical drafting source:
`execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt`.

Packet-local adapted object: `candidate/lldb-signal-trace-attempt3-v2.txt`,
SHA-256 `21beaaff1356a7069d3498403ae0a6ea8871504d28465bb9e3c24c6fdaf579c9`.
The historical source remains SHA-256
`720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8`.
The sole byte adaptation is one leading `#` comment identifying the new v2
packet-local object; the 34 historical LLDB command lines follow byte-for-byte.
This is a new v2 object and neither inherits nor continues C196/C197 authority.

Static parsing finds:

1. `auto-confirm` enabled and stop disassembly hidden;
2. `SIGTERM` configured to stop=`false`, notify=`true`, pass=`true`;
3. five enumerated breakpoint intents: `__sigtramp`,
   `uv__signal_handler`, regex `SignalWrap.*OnSignal`, regex
   `electron::Browser::Quit|Browser::Quit`, and
   `-[NSApplication terminate:]`;
4. each numbered breakpoint has one command block that emits a UTC
   `TRACE_EVENT`, captures `thread backtrace -c 16`, and continues; and
5. the final command is `process continue`.

This bounds each captured backtrace to 16 frames and reads no memory,
environment, credential, or process census. Static review cannot establish
that Electron 43.2.0 exports or resolves any breakpoint, that assigned
breakpoint numbers remain 1–5 after unexpected LLDB state, that attach is
permitted, or that an event will fire. Every `breakpoint set` and
`breakpoint command add` must visibly succeed before the owner treats the
target as resumed; an unresolved mandatory breakpoint or unexpected numbering
is a stop and deviation, not an interactive repair.

The future v2 attach row must name only this packet-local script:

```text
/usr/bin/xcrun lldb --batch -p <EXACT_HELPER_PID> -s /Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_ATTEMPT3_PACKET_PREPARATION_V2_2026-08-09/candidate/lldb-signal-trace-attempt3-v2.txt
```

The PID must be the sealed numeric direct child captured by the approved
owner launch step, with no name search or alternate target. The future v2
detach row is only one ETX byte followed in that same existing LLDB PTY by
exact debugger bytes `process detach\nquit\n`. Attach-to-detach has an absolute
150-second maximum. Both operations require new, individually approved v2
ledger authority; the historical C196/C197 cells grant none.

No LLDB/debugger command or target was invoked during this revalidation.
