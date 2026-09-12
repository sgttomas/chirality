# J_RUNTIME_LOGIN_REPAIR — RETURN

Type 2 TASK return. Worktree `owner-alignment-inspection-db4335`, branch
`claude/chirality-v3-mvp-trial-ab05cb`. Nothing committed. No daemon or app was
started or stopped. No authentication, admission, or containment check was
weakened.

## Files changed (working tree, `git diff --numstat`)

| File | + | − |
|---|---|---|
| `projects/chirality-runtime/packages/daemon/src/codex-login.ts` | 37 | 19 |
| `projects/chirality-runtime/packages/daemon/src/hosted-bootstrap.ts` | 42 | 18 |
| `projects/chirality-runtime/packages/daemon/src/host-account-client.ts` | 39 | 3 |
| `projects/chirality-runtime/packages/daemon/src/runtime-daemon.ts` | 37 | 9 |
| `projects/chirality-runtime/packages/daemon/src/hosted-private-entry.ts` | 8 | 3 |
| `projects/chirality-runtime/packages/daemon/src/hosted-private-composition.ts` | 2 | 1 |
| `projects/chirality-runtime/tests/codex-login.test.ts` | 28 | 1 |
| `projects/chirality-runtime/tests/hosted-bootstrap-integration.test.ts` | 44 | 1 |
| `projects/chirality-runtime/tests/host-account-lifecycle.test.ts` | 57 | 0 |

Total: 294 added, 55 removed, within the declared write scope. The same
worktree also carries unrelated in-flight modifications from another task
(`projects/chirality-app-dev/frontend/**`, `projects/chirality-runtime/tools/codex-supplier/**`,
`RUN_LOG.md`, `K_APP_LOGIN_REPAIR/`); those are not part of this return and
were not touched.

## A. Retry poison

### `codex-login.ts`
- New exported `createGroupedLoginRetirement({ retire, cleanup, retainedResources, pid? })`
  returning `{ close(), diagnostics() }`. It is the memoized grouped-login close
  used by the native (v2) launch path. Behaviour:
  - `retire()` rejects (retirement unproven) → `close()` rejects with the
    existing `RuntimeError(ENGINE_UNAVAILABLE, 503, { reason: "LOGIN_RETIREMENT_UNVERIFIED", retainedResources, pid })`
    — unchanged from before.
  - `retire()` resolves a verified outcome (leader exited, reaped, group retired)
    with non-empty `signalFailures` (for example the addon's `wait-unavailable`
    when the leader already exited) → **`close()` resolves**. The failures are
    retained as sanitized diagnostics `{ phase: "term" | "kill", message }`
    (control characters replaced, ≤200 chars).
  - `cleanup()` rejects → `close()` rejects with
    `RuntimeError(ENGINE_UNAVAILABLE, "Login containment cleanup failed; allocation retained", 503, { reason: "LOGIN_CLEANUP_FAILED", retainedResources, pid?, signalFailures: phases[] })`,
    `cause` = `AggregateError([cleanupError, ...signalCauses])`. Diagnostics
    remain readable. Resources are genuinely retained in that case, so it still
    rejects, as the brief allows.
- New `CodexLoginCloseDiagnostic` type and `CodexLoginTransport`
  (`CodexSessionTransport & { diagnostics?() }`); `launch()` returns that shape
  and `controlledForTests` accepts it.
- New accessor `CodexLogin.closeDiagnostics(): readonly CodexLoginCloseDiagnostic[]`
  (empty before close or when no signal failed).
- The v1 spawn path and the fixture path are unchanged.

### `hosted-bootstrap.ts`
- `TrustedHostedLoginCeremony` gains optional `closeDiagnostics?()`.
  `hosted-private-composition.ts` forwards `login.closeDiagnostics()`.
- New private `closeCeremony(projectId, ceremony, operation)` in
  `HostedBootstrapController`: awaits `ceremony.close()`, logs a rejection as
  `hosted.ceremony.close_failed`, logs non-empty diagnostics once per ceremony
  as `hosted.ceremony.close_diagnostics`, and rethrows the close failure.
- `startLogin` catch now **detaches first**:
  `if (state.ceremony === ceremony) { state.ceremony = undefined; state.ceremonyState = "failed"; }`
  then `await closeCeremony(...).catch(() => {})` then rethrows the original
  start error. A rejected (memoized) close therefore can never be re-encountered
  by the next `startLogin`, by `invalidateState`, or by `close()` at daemon
  stop. The `state.ceremony === ceremony` guard also stops a superseded start
  from clobbering a newer ceremony (the old code cleared unconditionally).
  The two pre-start close sites (`operation.check()` failure and "superseded
  before start") also go through `closeCeremony(...).catch(() => {})`.
- `signOut` and `close()` were changed to the same detach-then-close pattern
  (`const ceremony = state.ceremony; state.ceremony = undefined;` before
  awaiting `cancel`/`close`). `invalidateState` already detached first; it now
  routes through `closeCeremony` for logging. `cancelLogin` uses
  `invalidateState` and needed no change. Rethrow semantics of
  `invalidateState`/`signOut`/`close()` are otherwise unchanged.
- `startBootstrap`, `startHostedBootstrapRuntimeHost(input, bindings?, logger?)`
  and `startControlledHostedBootstrapRuntimeHostForTests(input, bindings, qualification?, logger?)`
  accept an optional logger and pass it to both the controller and the daemon.

## B. Client `details` contract (`host-account-client.ts`)

Exact shape attached as `RuntimeError.details` for every HTTP ≥ 400 daemon
response (`RuntimeError.code` stays `"ENGINE_UNAVAILABLE"`, `message` stays
`"Account operation was rejected"`, `status` stays the HTTP status):

```ts
export interface HostAccountOperationRejection {
  readonly kind: "operation-rejected";
  readonly operation: HostAccountOperation;   // "status" | "grant-provider-network-consent" | "start-login" | "cancel-login" | "sign-out"
  readonly status: number;                    // HTTP status (503 when the socket reported none)
  readonly daemonCode?: string;               // daemon error.code, only if ≤64 chars matching /^[A-Z_]+$/
  readonly reason?: string;                   // daemon error.details.reason, only if ≤64 chars matching /^[A-Z0-9_]+$/
  readonly daemonMessage?: string;            // daemon error.message, control chars (\x00-\x1f, \x7f) stripped, cut to 200 chars; omitted if empty
}
```

Parsing (`hostAccountOperationRejection(operation, status, body)`, exported):
- Rejection bodies are buffered to at most 16 KiB; anything larger is
  discarded and yields only `kind/operation/status`.
- Accepts the daemon envelope `{ error: { code, message, details? } }` (or a
  bare `{ code, message, details? }`); `code` and `message` must be strings.
  Non-JSON, arrays, wrong types → only `kind/operation/status`.
- Transport failures (socket errors such as `ENOENT`, aborts, timeouts) and the
  "authority revoked during request" rejection carry **no** `details`
  (verified by test). Success responses keep the previous 1 MiB limit and
  parsing.
- `RuntimeError` in `packages/contracts/src/errors.ts` already had
  `details?: Readonly<Record<string, unknown>>`; it was not changed.

## C. Daemon-side logging

- `runtime-daemon.ts` had no logger. Added a minimal optional one:
  ```ts
  export interface RuntimeDaemonLogger {
    warn(event: string, fields?: Readonly<Record<string, unknown>>): void;
    error(event: string, fields?: Readonly<Record<string, unknown>>): void;
  }
  export const NOOP_RUNTIME_DAEMON_LOGGER  // default
  export function describeRuntimeFailure(error): { code, status, reason?, message, cause? | causes? }
  export function safeDiagnosticText(value, limit = 200)
  ```
  `RuntimeDaemonOptions.logger?: RuntimeDaemonLogger`, no-op default. The
  interface maps 1:1 onto the App's `desktopLogger.warn/error(event, detail)`.
- `runHostedAccount` (covers all `/v3/projects/:id/hosted-bootstrap/*` routes,
  including authorization failures) now logs every failure as
  `runtime.daemon.hosted_account.failed` with
  `{ operation, projectId, code, status, reason?, message, cause?|causes? }`.
  `code`/`status`/`reason` come from the `RuntimeError` (non-RuntimeErrors log
  `code: "UNEXPECTED", status: 500`); `reason` is only `details.reason` when it
  is a string; messages are control-character-free and ≤200 chars; details are
  never copied wholesale. Auth URL, bearer, proof, counters and generation are
  never read for logging.
- Ceremony diagnostics from A are logged by the controller through the same
  logger: `hosted.ceremony.close_failed` (error) and
  `hosted.ceremony.close_diagnostics` (warn, `{ operation, projectId, diagnostics: [{ phase, message }] }`).
- Wiring for the App: `HostedPrivateBootstrapHostInput.logger?: RuntimeDaemonLogger`
  (`hosted-private-entry.ts`), passed through `compose` →
  `startHostedBootstrapRuntimeHost(input, bindings, logger)`. The logger is only
  forwarded when supplied so the existing adapter call-shape tests still pass.
  It is deliberately a separate top-level field, not part of `bootstrap`,
  because `readHostedPrivateBootstrapConfiguration` `structuredClone`s the
  bootstrap block (functions would throw). **The App main process
  (`frontend/electron/main.ts`, out of scope here) must pass
  `logger: desktopLogger` in its `startHostedPrivateBootstrapRuntimeHost` call
  for these events to reach the desktop log; until then the default is no-op.**

## D. Observer coverage — NOT changed (by design)

`account-free-login-observation.ts` `"bounded-protocol-purpose"` still lists
`account/login/start` only as a `laterPurposeMethods` entry. Sending it is not
cheap/safe under the current evidence contract:
- The observation record asserts `accountUsed: false`,
  `networkTriggeringRpcUsed: false`, and `protocolMethods` must equal exactly
  `["initialize","initialized","config/read"]` (`OBSERVATION_PROTOCOL_INVALID`
  otherwise); `account/login/start` starts the supplier's login flow (local
  callback server + provider auth URL) and would falsify those facts.
- The limb facts are hashed into `evidenceSha256` values that are published,
  consumed by `inspectCodexLoginPurposeReleaseRecord` / the v2 release basis,
  and asserted by `tests/account-free-login-observation.test.ts`,
  `hosted-packaged-release.test.ts`, `hosted-release-provisioner.test.ts`,
  `runtime-conformance-v2-admission.test.ts`, `d36-v2-connected.test.ts`.
What would be needed: a new evidence schema version (e.g.
`chirality-account-free-login-observation/v2` or a separate
`login-start-probe` record) with an explicit `networkTriggeringRpcUsed: true`
/ `accountUsed: false` semantics, an explicit consent gate for the probe, a
recorder that keeps only `loginId` presence and the auth URL **host**, and
matching updates to the release-record inspector and the consuming tests.
That is a governed evidence change, not a small observer edit.

## Tests

Added:
- `tests/codex-login.test.ts` — "grouped login retirement diagnostics" (2 tests):
  verified retirement with signal failures resolves `close()` twice, runs
  cleanup once, and `login.closeDiagnostics()` exposes sanitized entries
  (a `\u0007` in the cause becomes a space); unproven retirement and failed
  cleanup still reject with `LOGIN_RETIREMENT_UNVERIFIED` /
  `LOGIN_CLEANUP_FAILED` + `retainedResources`, memoized, with diagnostics retained.
- `tests/hosted-bootstrap-integration.test.ts` — "hosted bootstrap login retry
  after a failed start" (1 test, real daemon + `RuntimeClient` over the socket):
  first ceremony's `start()` rejects and its `close()` rejects; status shows
  `failed`/`canStartLogin: true`; second `startLogin` creates a new ceremony
  and returns `login-1`; logger received `runtime.daemon.hosted_account.failed`
  (operation, projectId, code, status 503, reason `CONTROLLED_START`, message),
  `hosted.ceremony.close_failed`, `hosted.ceremony.close_diagnostics`; no auth
  URL host in any event; `host.stop()` resolves afterwards.
- `tests/host-account-lifecycle.test.ts` — "host account client rejection
  details" (2 tests): unit coverage of `hostAccountOperationRejection`
  (sanitized fields, bad code/reason dropped, message cut to 200, non-JSON /
  array / wrong types / >16 KiB / absent body → bare details); end-to-end
  `MainHostAccountClient` against a local unix-socket HTTP server: 503 JSON
  body → full `operation-rejected` details; 20 KiB body → bare details;
  non-JSON 400 → bare details; a 200 status still validates; a missing socket
  yields an `ENOENT` error with `details === undefined`.

Results (`projects/chirality-runtime`, after `npm run build`):
- `npm run typecheck` — clean.
- `npm test` (vitest) — **Test Files 81 passed | 1 skipped (82); Tests 1078 passed | 14 skipped (1092)**, 25.1 s. The skipped file/tests are pre-existing
  platform/fixture gates, not caused by this change. No failures.
- Targeted: `codex-login.test.ts` 14/14, `host-account-lifecycle.test.ts`,
  `hosted-bootstrap-integration.test.ts` 7/7, `hosted-private-entry.test.ts` — all pass.

## Deviations from the brief and why

- **Start-failure error precedence**: after a failed `ceremony.start()` the
  controller rethrows the *original* start error and only records the close
  failure through the logger, rather than wrapping both in an `AggregateError`.
  Wrapping would make the daemon respond `INTERNAL_FAILURE 500 "Unexpected
  runtime failure"` and lose the actual `RuntimeError` code/reason that B now
  carries to the App. The close failure is fully recorded
  (`hosted.ceremony.close_failed` with reason/retainedResources when present).
- **Diagnostics exposure**: implemented as `closeDiagnostics()` accessor plus an
  exported helper, not a logger option on `CodexLoginOptions` (none existed);
  logging happens one level up in the controller through the daemon logger,
  which is the single mechanism requested in C.
- **Logger placement**: added on `RuntimeDaemonOptions` (no-op default) and
  plumbed via `HostedPrivateBootstrapHostInput.logger`, as the brief allowed.
  Not wired in the App (out of write scope).
- **D not implemented**, per the brief's own condition; rationale above.

## Not done / follow-ups for the lead

- App main process: pass `logger: desktopLogger` (or an adapter) into
  `startHostedPrivateBootstrapRuntimeHost({ bootstrap, privateComposition, logger })`
  so the daemon process's hosted-account failures and ceremony diagnostics land
  in the desktop log; and read `error.details` (`kind === "operation-rejected"`)
  from `HostAccountClient` rejections in `host-account-ipc.ts`.
- The root cause of the R4 sign-in failure itself is still undiagnosed; this
  change makes the next attempt report `daemonCode`/`reason`/`daemonMessage`
  to the App and log the daemon-side failure and any retirement diagnostics.
