# K_APP_LOGIN_REPAIR — RETURN

Type 2 TASK return. Worktree branch `claude/chirality-v3-mvp-trial-ab05cb`;
nothing committed. Write scope honoured: only
`projects/chirality-app-dev/frontend/electron/**` and
`projects/chirality-app-dev/frontend/src/**` (plus this file). No daemon, app,
or Electron process was started; nothing under `/private/tmp/chirality-*` or
`~/Library` was touched. No authentication, signed-IPC, or admission check was
weakened: sender-origin checks, request parsing, project canonicalisation, and
the transport-failure invalidate path are unchanged.

`F` = `projects/chirality-app-dev/frontend`.

## Files changed (`git diff --numstat`, new files by `wc -l`)

| File | + | − |
|---|---|---|
| `F/electron/host-account-ipc.ts` | 127 | 5 |
| `F/electron/host-account-ipc-contract.ts` | 15 | 1 |
| `F/electron/main.ts` | 16 | 2 |
| `F/electron/renderer-server-port.ts` | 12 | 2 |
| `F/electron/daemon-activate-policy.ts` (new) | 116 | 0 |
| `F/src/components/settings/hosted-bootstrap-controller.tsx` | 55 | 4 |
| `F/src/components/shell/account-row.tsx` | 6 | 1 |
| `F/src/__tests__/electron/host-account-ipc.test.ts` | 83 | 0 |
| `F/src/__tests__/electron/daemon-activate-policy.test.ts` (new) | 109 | 0 |
| `F/src/__tests__/components/hosted-bootstrap.test.tsx` | 109 | 2 |
| `F/src/__tests__/components/account-presentation.test.tsx` | 15 | 1 |

Untouched: `preload.ts`, `hosted-bootstrap-client.ts`,
`hosted-bootstrap-view.tsx`, `chirality-window.d.ts` (see "Deviations").

## 1. Main-process IPC: rejection vs transport failure

### Contract (`host-account-ipc-contract.ts`)

```ts
export const HOST_ACCOUNT_UNAVAILABLE = 'Hosted account service is unavailable.';

export type HostAccountDesktopResult =
  | { ok: true; value: HostAccountDesktopValue }
  | { ok: false; error: typeof HOST_ACCOUNT_UNAVAILABLE }          // transport/authority
  | { ok: false; error: string; reason?: string };                  // daemon rejection
```

### Behaviour (`host-account-ipc.ts`, `performHostAccountOperation`)

`parseOperationRejection(error)` (exported) accepts only an error whose
`details` is exactly the daemon contract: `kind === 'operation-rejected'`,
`operation: string`, `status: safe integer`, optional `daemonCode` (≤64,
`/^[A-Z_]+$/`), `reason` (≤64, `/^[A-Z0-9_]+$/`), `daemonMessage` (≤200).
Any deviation (missing `details`, other `kind`, malformed optional field,
plain `Error`) returns `undefined` and the failure is handled as transport.

- Rejection: the account client is **not** invalidated. Result is
  `{ ok: false, error: '<wording> (<reason>).', reason }` where
  `reason = details.reason ?? details.daemonCode` (the `reason` key and the
  parenthesised code are both omitted when neither is present). Wording per
  operation: `start-login` → "Sign-in could not start",
  `grant-provider-network-consent` → "Provider network consent could not be
  recorded", `cancel-login` → "Sign-in could not be cancelled", `sign-out` →
  "Sign-out could not complete", `status` → "Account status could not be read".
  Example: `Sign-in could not start (CODEX_REQUEST_REJECTED).`
- Transport/authority failure: unchanged — invalidate the selected client and
  return the generic `HOST_ACCOUNT_UNAVAILABLE`.

### Logging

New optional `log(level, event, detail)` option, wired in `main.ts` to
`desktopLogger.log` next to the existing `runtime.account_host.*` events.

| Event | Level | Detail |
|---|---|---|
| `runtime.account_host.operation_rejected` | warn | `operation, projectId, name, code, status, message, daemonOperation, daemonStatus, daemonCode?, reason?, daemonMessage?` |
| `runtime.account_host.operation_failed` | error | `operation?, projectId?, clientSelected, name?, code?, status?, message?` |
| `runtime.account_host.client_unavailable` | warn | `operation, projectId` (account host not yet connected; no invalidate) |

`message` is logged only when the error's `name === 'RuntimeError'` (runtime
composes those strings itself); for any other error only `name`/`code` are
logged, so a transport-layer error that echoes request headers (bearer, proof,
counter) never reaches the log. The auth URL is never a failure payload and is
never logged. Tests assert the log output contains none of
`authUrl|Bearer|proof|counter|https?:` and none of the raw messages.

### Renderer receipt of the reason

`preload.ts` already throws `new Error(result.error)`; that message now
carries the reason code, and `isTransientHostAccountError` (exact match on the
generic string) is unchanged, so rejections are never walked up the retry
ladder. See "Deviations" for why the structured `reason` field stops at the
main/preload boundary.

## 2. Renderer controller and popover

`hosted-bootstrap-controller.tsx`:

- `reconcile(root, generation, signal, clearError)` re-reads status through
  `getHostedBootstrapStatusWithRetry` and adopts it if still current; failures
  are swallowed so the action's own error stays.
- `withReconcile(...)` wraps the consent, start-login, and cancel requests: if
  the request itself throws, status is re-read first, then the error is
  rethrown so `perform` sets it. Sign-out keeps its bespoke reconciliation
  (admission forced to `unavailable`), now via the retry path instead of the
  single-shot `getHostedBootstrapStatus`.
- New `onRefresh` on `HostedBootstrapController`: re-reads status and clears a
  stale error on success. Skipped while hydrating, while an action is busy, or
  while the pending/establishing poll owns the reads.
- Reconnect: the controller reads `useRuntimeConnectivitySnapshot()` and calls
  `refresh()` on an `isRuntimeReconnect(previous, next)` transition — the same
  predicate the provider uses for its epoch. The epoch itself was not used
  because the controller's own `onBindingChanged` bumps it, which would have
  caused a self-triggered extra read after every binding publish.
- `account-row.tsx`: the trigger calls `props.hosted?.onRefresh()` on open
  only (not on close).
- `hosted-bootstrap-view.tsx`: no change. The existing `{error ? <p role="alert">…}`
  line renders the string from main, e.g. "Sign-in could not start
  (CODEX_REQUEST_REJECTED).". No new banner or panel.

## 3. Daemon `activate` guard

### How "GUI alive" is determined

The daemon has no view of the account-host lease (`HostAccountAuthority` is
internal to Runtime and not exposed on `HostedBootstrapRuntimeHost`), and a
control-socket client cannot be told apart from a CLI one. What it does share
with the GUI is `app.getPath('userData')` (both apply the same
`CHIRALITY_USER_DATA` override), where the packaged GUI persists
`renderer-port.json` (`renderer-server-port.ts`) and holds that loopback port
for its whole lifetime. So the evidence is: **read the saved renderer port
record with the GUI's own validating reader, then attempt one TCP connect to
`127.0.0.1:<port>` (no bytes sent, ≤500 ms)**. "Listening" is exactly the fact
the doomed second GUI would otherwise discover as "Saved renderer port … is
already occupied".

`daemon-activate-policy.ts` (pure, no `electron` import, same shape as
`runtime-autostart.ts`):

```ts
type RendererPortEvidence =
  | { kind: 'absent' } | { kind: 'unreadable'; error } | { kind: 'listening'; port }
  | { kind: 'closed'; port; error } | { kind: 'unknown'; port };
decideDaemonActivate(evidence): { action: 'ignore'; reason: 'gui-running'; port } | { action: 'spawn'; evidence }
observeRendererPortEvidence({ userDataDirectory, readRecord?, probe? })   // never throws
probeLoopbackPort(port, timeoutMs)                                       // 'listening' | 'closed' | 'unknown'
```

Only `listening` blocks. `absent` (development, or no GUI has ever run),
`closed` (GUI gone), `unreadable` (record fails validation) and `unknown`
(probe did not settle) all keep the existing V-D4 spawn so a genuine launch is
never swallowed by a stale or damaged file; the evidence is logged as
`runtime.daemon.gui_liveness` before spawning. This is the conservative side
for "do not kill a running GUI's runtime" on every positive observation, and
for "do not make the app look dead" on every uncertain one.

`main.ts`: `spawnGuiFromDaemon` is now async; order is spawn-disabled check →
liveness probe → (`runtime.daemon.activate_ignored_gui_running { port }` and
return) → throttle → spawn → retire. The throttle timestamp is not touched when
the activation is ignored. `renderer-server-port.ts` exports
`readRendererPortRecord`, `rendererPortRecordPath`, and the
`RendererPortRecord` type (previously module-private; no behaviour change).

## Tests

Commands run from `F`:

- `npm run typecheck` — exit 0 (both `tsc` passes).
- `npm test` (whole frontend suite) — **210 files passed, 1 skipped; 2241
  tests passed, 4 skipped; 0 failures** (9.5 s). The skipped file is the
  pre-existing `src/__tests__/integration/pec-bridge.integration.test.ts`
  (`skipIf`). One stdout line `{"status":"FAIL","summaryPath":…}` is printed
  by `src/__tests__/scripts/run-packaged-daemon-instruction-root-proof.test.ts`,
  which deliberately drives a failing proof run; it is not a test failure and
  that file was not touched.
- `hosted-account-sequence.integration.test.ts` (real daemon, real signed
  client through `performHostAccountOperation`) — green, unchanged.

New/extended coverage:

- `host-account-ipc.test.ts` (+4): rejection keeps the client, returns the
  reason, logs without request material; daemonCode fallback and per-operation
  wording; five malformed/transport cases each invalidate and log without the
  raw message; invalid request and missing client log without retiring.
- `daemon-activate-policy.test.ts` (new, 10): decision table; real record
  reader + real loopback server for `listening` and `closed`; absent and
  invalid records never probe; `unknown` spawns; probe sends no bytes.
- `hosted-bootstrap.test.tsx` (+5, 1 adjusted): status re-read after a
  rejected login with reason on the existing alert line (exactly one extra
  `<p role="alert">`); `consent-required` rendered from the re-read;
  action error kept when the re-read fails; `onRefresh` re-reads and drops a
  stale error but is skipped while busy or polling; reconnect re-reads once and
  not on repeated connected or a drop. "resumes pending status polling after
  cancellation fails" now feeds one extra `pending` status for the re-read that
  follows the failed cancel; its intent (poll resumes) is unchanged.
- `account-presentation.test.tsx` (+1): `AccountRow` calls `onRefresh` on each
  open, never on close; `hostedBase` fixture gained `onRefresh: noop`.

## Deviations and why

- **`reason` is not a separate field on the renderer side.** `preload.ts` and
  `hosted-bootstrap-client.ts` were left unchanged: a rejected promise crossing
  `contextBridge` keeps only the Error `message`, so a structured field would
  not survive the bridge without changing the bridge's return shape for all
  five operations. The reason therefore travels inside the message
  (`… (CODE).`), which is exactly what the view renders; the structured
  `reason` exists on `HostAccountDesktopResult` for main-process and preload
  consumers and tests.
- **Setup failures do not trigger a re-read.** The brief lists
  login/consent/cancel/logout; the existing test "sets up an explicitly
  selected folder once and reports a failure without retrying" pins one status
  read for that path, and setup has no daemon-side state to reconcile.
- **Reconnect uses the connectivity snapshot, not `useRuntimeEpoch`** (see §2).
- **The sign-out path** already reconciled; it was moved to the retry-ladder
  read rather than duplicated with `withReconcile`.
- **Guard evidence is the renderer port, not a lease** — the lease is not
  observable from the daemon without a Runtime package change (out of scope).

## Not done / caveats

- Not exercised on a packaged build or a real `activate` delivery; the guard
  is verified only through the pure module and a real loopback socket. On a
  packaged build the liveness probe adds at most one 500 ms wait before a
  legitimate spawn.
- The daemon-side `details` contract is coded against the shape given in the
  brief; if the other agent's `host-account-client` lands with a different
  field set, rejections will fall through to the (unchanged) transport path
  rather than misparse — nothing regresses, but the reason will not surface
  until the shapes agree.
