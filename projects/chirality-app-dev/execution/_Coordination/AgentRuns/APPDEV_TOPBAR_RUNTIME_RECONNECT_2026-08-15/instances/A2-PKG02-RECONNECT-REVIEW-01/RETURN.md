# Fresh review return

`BLOCK`

## Blocking finding

`frontend/src/components/shell/shell-frame.tsx` treated every `{ ok: true }` daemon-status response as a successful connection check. Production returns `{ ok: true, daemon: { running: false } }` when launch-agent status is readable but the daemon is unreachable (`electron/runtime-control-ipc.ts` `daemonSnapshot`). A stale connected snapshot could therefore remain visually connected while the secondary feedback reported success after the status check had proved the daemon unreachable. The test stub omitted the production daemon payload and missed this case.

Required repair: keep snapshot-derived visual state, but treat `daemon.running === false` as secondary check failure and add a component test using the real response shape.

## Other review results

- Exact scope: four `frontend/src/**` files; PASS.
- Desktop-only presence and existing `runtime.daemon.status()` path: PASS.
- Reachable status invokes `onDaemonAvailable`; production binds it to `bindingSupervisor.refreshNow()`: PASS.
- Accessibility, native keyboard behavior, reentrancy, and D-APP-64 fences otherwise PASS.
- Residual risk: late completion after unmount calls state setters; React isolates the disposed instance, so this is non-blocking.

Required after repair: focused component/IPC tests, clean full `frontend-test` and `frontend-typecheck`, and a new independent `COMMIT-SAFE`/`BLOCK` verdict. No files were written by the reviewer.
