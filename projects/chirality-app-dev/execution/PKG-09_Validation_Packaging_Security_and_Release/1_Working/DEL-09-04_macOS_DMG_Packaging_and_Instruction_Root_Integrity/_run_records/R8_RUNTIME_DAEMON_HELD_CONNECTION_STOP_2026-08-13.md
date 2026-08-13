# R8 — runtime daemon held-connection graceful stop (2026-08-13)

Status: `SOURCE + REGRESSION READY FOR REVIEW`

## Built

- `runtime/packages/daemon/src/signal-shutdown.ts` adds a reusable one-shot
  `SIGINT`/`SIGTERM` binder. It awaits the existing bounded daemon stop,
  absorbs repeat signals during teardown, restores listeners, normalizes a
  synchronous failure, never calls `process.exit()`, and reports cleanup
  failure through a nonzero exit code.
- `frontend/electron/main.ts` installs the binder only after daemon-mode
  runtime-host start and delegates to the complete existing Electron shutdown
  funnel. GUI direct signal behavior remains conditional to GUI mode.
- `frontend/electron/runtime-shutdown-policy.ts` keeps native `before-quit`
  vetoed throughout in-flight teardown and releases only the final owned
  `app.exit()` after teardown completes.

## Regression

`runtime/tests/runtime-daemon-signal.test.ts` spawns a real child daemon. The
fixture writes complete HTTP headers with `Content-Length: 100` and only one
body byte, waits until the daemon's `request` event proves the message is
parsed while `complete=false` and `readableEnded=false`, sends OS `SIGTERM`,
and requires a natural code-0 exit in under four seconds. The observed run
completed in 2.146 s and verified both `control.sock` and its owner record
absent. Electron policy tests cover binder-first/native-quit ordering,
resource disappearance during teardown, final owned exit, and idle quit.

## Checks

- Runtime typecheck: PASS.
- Runtime full tests: PASS — 9 files, 76 tests.
- Frontend typecheck: PASS (application and Electron configurations).
- Frontend full tests: PASS — 143 files passed, 1 skipped; 1113 tests passed,
  6 skipped.
- Frontend production build: PASS — Next production build and Electron/runtime
  bundles completed in the disposable validation copy.
- Fresh terminal code review: `PASS_FOR_MANAGER_FAN_IN` after one review-found
  native-quit race was remediated and independently re-reviewed.

The complete managed evidence is under
`execution/_Coordination/AgentRuns/APPDEV_RUNTIME_DAEMON_HELD_CONNECTION_STOP_2026-08-13/`.
No app/package deployment or D-APP-93/D-APP-88 disposition, acceptance,
closure, lifecycle, or Checking Approval SHA act occurred.
