# Cleanup and containment

Verdict: `RUN-OWNED CLEANUP PASS / OWNER-STATE CONTAINMENT FAIL`

- GUI PID `67697` received Ctrl-C and logged `desktop.shutdown.completed` at
  `2026-08-20T21:27:17.682Z`.
- Daemon PID `67623` received Ctrl-C and logged
  `desktop.shutdown.completed` at `2026-08-20T21:27:25.303Z` through the
  accepted `runtime-daemon-signal` funnel.
- Subsequent exact PID checks returned `no such process`.
- The isolated runtime socket was absent.
- CDP port `127.0.0.1:52786` had no listener.
- `lsof +D /private/tmp/chirality-d86pkg02.VWKLGL` returned no holders.
- The exact disposable root `/private/tmp/chirality-d86pkg02.VWKLGL` was then
  removed and verified absent.
- No default LaunchAgent action was invoked.
- The unexpected owner launcher write is unresolved and deliberately untouched.
