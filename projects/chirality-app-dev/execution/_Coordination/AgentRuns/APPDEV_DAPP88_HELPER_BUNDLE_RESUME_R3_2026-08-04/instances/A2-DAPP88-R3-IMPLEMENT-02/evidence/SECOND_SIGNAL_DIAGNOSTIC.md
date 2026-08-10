# Post-GUI second-SIGTERM cleanup diagnostic

Status: `DIAGNOSTIC ONLY — NO ACCEPTANCE CREDIT`

A fresh helper/GUI pair was started on the same isolated run store after the terminal first-signal evidence was frozen:

- helper PID `68575`; runtime started `2026-08-04T17:36:55.522Z`;
- GUI PID `68601`; authenticated contact returned `Unknown project: chirality-app-dev` at `2026-08-04T17:37:04.972Z`.

```text
diagnostic_first_signal_time=2026-08-04T11:37:23-06:00
diagnostic_first_command=/bin/kill -TERM 68575
diagnostic_after_first_3s=ALIVE
diagnostic_socket_after_first=PRESENT

diagnostic_second_signal_time=2026-08-04T11:37:26-06:00
diagnostic_second_command=/bin/kill -TERM 68575
diagnostic_after_second_polls=1 (0.1 seconds)
diagnostic_after_second=ABSENT
diagnostic_socket_after_second=PRESENT
diagnostic_owner_after_second=PRESENT
```

No `desktop.shutdown.started` or `desktop.shutdown.completed` line appeared for either signal. The second signal terminated the Electron helper immediately without Root cleanup. The GUI then exited gracefully on its own first cleanup `SIGTERM`.

This characterizes the seam: the first helper `SIGTERM` is absorbed before the App teardown funnel; the second uses Electron/native termination and bypasses Root stop, leaving stale socket/owner state. It does not support acceptance or a new generic Root semantic.
