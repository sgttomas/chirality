# Fresh static LLDB-script revalidation

Verdict: `PASS_STATIC_ONLY — EXECUTION FITNESS AND SYMBOL RESOLUTION UNKNOWN`

Historical script:
`execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt`.

Prepared self-contained copy: `prepared/lldb-signal-trace.txt`.

Both reproduce SHA-256
`720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8`.
The prepared copy is evidence convenience only. Preserved C196 names the
historical absolute path and must continue to use that exact path unless new
authority is granted.

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

Preserved C196 is exactly:

```text
/usr/bin/xcrun lldb --batch -p <EXACT_HELPER_PID> -s /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt
```

The PID must be the sealed numeric direct child captured by the approved
owner launch step, with no name search or alternate target. Preserved C197 is
only one ETX byte followed in that same existing LLDB PTY by exact debugger
bytes `process detach\nquit\n`. Attach-to-detach has an absolute 150-second
maximum. C196/C197 remain valid, exact, and unused; they grant no launch, PID
search, first signal, forwarding, watchdog, evidence, cleanup, or process
authority.

No LLDB/debugger command or target was invoked during this revalidation.
