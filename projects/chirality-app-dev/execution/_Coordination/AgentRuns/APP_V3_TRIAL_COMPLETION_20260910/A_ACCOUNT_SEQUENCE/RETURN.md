# A_ACCOUNT_SEQUENCE — RETURN

Worktree: `/Users/ryan/dev/chirality/.claude/worktrees/owner-alignment-inspection-db4335`
(branch `claude/chirality-v3-mvp-trial-ab05cb`). Author role, Type 2. No commits,
no stash, no npm install, no packaged build, no Runtime (R) source edits, no
daemon guard weakened.

## 1. Diagnosis confirmation

Confirmed from source before any edit:

- `F/src/lib/runtime-client/runtime-daemon-harness-port.ts`:
  `RuntimeHostedBootstrapPort.initializeProject` registered, called
  `verifyAndBind`, then `registeredStatus`, which called
  `current.client.hostedBootstrapStatus(projectId)` on the ordinary
  project-scoped `RuntimeClient`. `getStatus` did the same via
  `resolveAndBind` -> `registeredStatus`.
- `R/packages/daemon/src/runtime-daemon.ts` `runHostedAccount`: when
  `options.accountHost` exists and the request lacks
  `x-chirality-account-proof`, it throws
  `RuntimeError("UNAUTHORIZED", "Complete App account host proof is required", 401)`
  before any effect. The ordinary `RuntimeClient` never sends that header, so
  "Use this folder" in the signed R3 trial failed exactly there.
- Every other account action (status / consent / login start / cancel / sign
  out) already went renderer -> preload `hostedAccount` -> `electron/host-account-ipc.ts`
  `performHostAccountOperation` -> verified `HostAccountClient` (signed proof
  headers). The Next status route (`/api/harness/hosted-bootstrap/status`) had
  no renderer caller in production (`getHostedBootstrapStatus` already uses IPC).

## 2. Design chosen

### Part 1 — repair

- `HostedBootstrapPort.initializeProject` now returns
  `HostedProjectInitializationResponse = Extract<HostedProjectBindingResponse, { registration: 'registered' }>`
  i.e. `{ registration: 'registered', projectId }` only. Defined in
  `daemon-harness-port.ts` and mirrored in `hosted-bootstrap-client.ts`.
  `HostedBootstrapStatusResponse` is removed from the server-side port module
  (the Next tier can no longer produce it); the renderer keeps its own
  `HostedBootstrapStatusResponse` for the IPC result.
- `registeredStatus` deleted. `verifyAndBind`, reservation
  (`reserveExplicitSelection` / `reserveHydration` / `reservationIsCurrent`),
  drift (`assertRegistration`, `revalidateBinding`) and cancellation handling
  are untouched.
- `getStatus`: option chosen = **binding-only** (remove the ordinary status
  call; the route returns `{ registration, projectId }`), not fail-closed.
  Reasons: (a) minimal — the port interface, fake port, and all existing
  callers/tests keep working; (b) safe — the route now carries the same data
  as the bind route, never account status, and the return type makes it
  impossible for a future renderer caller to expect `status` from Next;
  (c) the route has no production caller, so behaviour visible to users is
  unchanged. Doc comments on the port method and the route state that account
  status is served only through the Desktop account-host IPC.
- Renderer client: `initializeHostedBootstrapProject` returns the binding.
  The transient-retry ladder from `hydrateHostedBootstrapProject` is extracted
  into exported `getHostedBootstrapStatusWithRetry(projectRoot, signal)`
  (same `[250, 1000, 5000]` ms ladder, same transient predicate, same abort
  handling); `hydrate` now composes it.
- Controller (`hosted-bootstrap-controller.tsx`): shared `publishBinding(root,
  projectId)` applies the `${root}:${projectId}:registered` dedupe key that
  `load` used. A single `setup(root, signal, generation)` runs
  `initialize` -> guard (abort / generation / root) -> `publishBinding` ->
  `getHostedBootstrapStatusWithRetry` -> guard -> `setObserved`. `onSetup`
  calls `perform('setup', setup)`; `perform`'s abort/generation/root
  protections are unchanged. If the status read fails after a successful
  registration the binding stays published, the error surfaces, and the manual
  action remains (verified idempotent daemon-side: repeat initialize returns
  the same projectId — asserted in the integration test).

### Part 2 — native-picker integration hook

- `workspace-provider.tsx` exposes
  `lastSelection: { path: string; explicit: true; sequence: number } | null`.
  Set (sequence + 1) only in `applyProjectRoot` on successful validation —
  the path both the native picker (`chooseProjectRoot`) and manual entry use.
  Cleared by `clearProjectRoot`. The localStorage restore effect never sets it.
  Added `useWorkspaceSelection()` — a null-tolerant read (returns `null`
  outside a provider) so the controller does not need `shell-frame.tsx`
  changes (other worker's area) and hosts without a provider degrade to
  manual-only.
- Controller effect: when `lastSelection.path === projectRoot`, the sequence
  has not been consumed, hydration finished (`!loading`), no action is busy,
  and the snapshot is `registration: 'required'`, it consumes the sequence and
  runs `perform('setup', setup)` once. A failure surfaces the existing error
  with no automatic retry; re-selecting the folder increments the sequence and
  may run it again; restored roots never auto-initialize.

### Part 3 — complete-sequence integration test

`F/src/__tests__/electron/hosted-account-sequence.integration.test.ts`
(imports `performHostAccountOperation`, not `registerHostAccountHandler`;
`electron` is neither required nor mocked, following
`host-account-ipc-connection.test.ts`).

## 3. Files changed (all under F = `projects/chirality-app-dev/frontend`)

Production:
- `src/lib/runtime-client/daemon-harness-port.ts` (interface + types; required)
- `src/lib/runtime-client/runtime-daemon-harness-port.ts`
- `src/lib/harness/hosted-bootstrap-client.ts`
- `src/components/settings/hosted-bootstrap-controller.tsx`
- `src/components/workspace/workspace-provider.tsx`
- `src/app/api/harness/hosted-bootstrap/status/route.ts` (doc comment only)

Tests:
- `src/__tests__/lib/runtime-daemon-harness-port.test.ts`
- `src/__tests__/lib/hosted-bootstrap-client.test.ts`
- `src/__tests__/api/harness/hosted-bootstrap.test.ts`
- `src/__tests__/components/hosted-bootstrap.test.tsx` (this file is also being
  edited concurrently by the renderer-surfaces worker for view `title`/`<p>`
  assertions; my additions coexist with theirs)
- NEW `src/__tests__/electron/hosted-account-sequence.integration.test.ts`
- `src/__tests__/api/harness/fake-daemon-harness-port.ts`: reviewed, no change
  needed (its `getStatus` already returns `{ registration: 'required' }`).

Not touched: R sources, `electron/*`, `components/shell/*`,
`hosted-bootstrap-view.tsx`, `settings-view.tsx`, `runtime-settings*.tsx`,
`app/layout.tsx`.

## 4. Commands and results

Environment: `export PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin`, cwd = F.

```
node node_modules/vitest/vitest.mjs run \
  src/__tests__/lib/runtime-daemon-harness-port.test.ts \
  src/__tests__/lib/hosted-bootstrap-client.test.ts \
  src/__tests__/api/harness/hosted-bootstrap.test.ts \
  src/__tests__/components/hosted-bootstrap.test.tsx \
  src/__tests__/components/account-presentation.test.tsx \
  src/__tests__/components/runtime-reconnect-refresh.test.tsx \
  src/__tests__/electron/host-account-ipc.test.ts \
  src/__tests__/electron/host-account-ipc-connection.test.ts \
  src/__tests__/electron/host-account-connection.test.ts \
  src/__tests__/electron/hosted-account-sequence.integration.test.ts
=> Test Files 10 passed (10); Tests 106 passed (106)

node node_modules/vitest/vitest.mjs run src/__tests__/electron/hosted-account-sequence.integration.test.ts
=> 1 passed (1)   (final run after adding the repeat-initialize assertion)

node node_modules/typescript/bin/tsc --noEmit -p tsconfig.json
=> 1 error, not mine: src/__tests__/api/harness/turn-route-attachments.test.ts(128,33)
   TS2493 (untracked file from the attachment-path worker). No errors in any
   file I changed or created.

node node_modules/typescript/bin/tsc --noEmit -p tsconfig.electron.json
=> clean
```

Guard evidence: `grep -rn hostedBootstrapStatus src electron --include='*.ts' --include='*.tsx' | grep -v __tests__` => none.

Note on a transient failure during the run: one intermediate run of
`hosted-bootstrap.test.tsx` failed on the other worker's `<p>` assertion
(`'Sign-in pending'` vs `'[object Object]'`, line ~102) while their view edit
was mid-flight; it passed in the final run without any change from me.

## 5. What the integration test proves

Against a real controlled daemon (`startControlledHostedBootstrapRuntimeHostForTests`)
whose bindings supply a real `HostAccountAuthority` (`createAccountHost`), a
controlled login ceremony, admission/materialization, and project-local
sign-out, using a real signed `HostAccountClient` (`createHostAccountClient`)
whose provisioning ceremony goes through an in-process seam that forwards the
exact challenge / host nonce / proof / bearer bytes (nothing fabricated):

1. `hydrateHostedBootstrapProject` (renderer) -> `fetch` routed to the
   production `bind` route handler -> `RuntimeHostedBootstrapPort` created by
   `createRuntimeHostedBootstrapPortFromEnvironment` from the Desktop env vars
   -> daemon: `{ registration: 'required' }`; status via the bridge
   (`performHostAccountOperation` -> `HostAccountClient`): required.
2. `initializeHostedBootstrapProject` -> `initialize` route -> port
   (`verifyAndBind`, `installBoundDaemonHarnessPort`) -> daemon: returns
   `{ registration: 'registered', projectId }` with no `status`; the bound
   normal daemon port serves `listRoles(projectRoot)`; repeat initialize
   returns the same projectId.
3. The daemon's account-proof check is exercised for real: the project-scoped
   ordinary client (the exact client the old port used) and the bootstrap
   client both get `UNAUTHORIZED` / 401 / "Complete App account host proof is
   required" for status, and 401 for consent. The Next `status` route returns
   only the binding.
4. Status after setup through `getHostedBootstrapStatusWithRetry` -> bridge ->
   `performHostAccountOperation` -> signed client -> daemon: `consent-required`.
5. Re-hydration revalidates the cached binding (`onBound` fired) and reads
   status the same way.
6. Consent -> `ready-to-start`; start login -> `{ loginId, authUrl }`; status
   `pending`; cancel -> `cancelled`; status `cancelled`.
7. Second login; ceremony completed through the controlled seam; status
   `signed-in` / admission `ready` (engine materialized).
8. Sign out -> `consent-required`; supplier sign-out and admission retirement
   observed; status `consent-required` / `unavailable`; ordinary path still 401.

Every status/consent/login/cancel/sign-out call in the sequence is accepted by
the authority's proof verification, counter/replay guard, and scope check on
the daemon side.

### What remains native-only

- The Electron IPC transport itself (`ipcRenderer.invoke` / `contextBridge` /
  `ipcMain.handle` + `isAuthorizedSender`). The test calls
  `performHostAccountOperation` directly and replicates preload's
  `invokeHostAccount` unwrap verbatim.
- The Next HTTP server between renderer `fetch` and the route handlers (the
  handlers themselves run).
- The XPC transport and codesign peer verification that
  `createVerifiedHostAccountClient` / `createVerifiedHostAccountAuthority`
  (`host-account-release.ts`) add on top of the same `MainHostAccountClient`
  and `HostAccountAuthority` classes used here; that needs a signed packaged
  bundle and its release basis. The signing predicate used in the test is the
  controlled one from `R/tests/host-account-lifecycle.test.ts`.

## 6. Open risks

- Concurrent edits: `hosted-bootstrap.test.tsx` is shared with the
  renderer-surfaces worker; if their view change lands after mine, the file
  should be re-run once. `turn-route-attachments.test.ts` (attachment-path
  worker) currently fails the app typecheck; unrelated to this tranche.
- `getStatus` on the port is now binding-only and functionally overlaps
  `bindProject` (the latter revalidates a cached binding; the former does not).
  Leaving both is deliberate to keep the route surface and fake port stable;
  a later cleanup could collapse the status route onto bind.
- Auto-setup consumes one sequence per explicit selection. If the hosted
  account service is down at selection time the automatic setup fails once
  and shows the error; the user then uses the manual action. This is the
  specified behaviour but means a slow account-host start could surface an
  error the manual retry immediately clears (the retry ladder covers up to
  ~6.25 s of transient unavailability).
- The controller reads the selection via `useWorkspaceSelection()`; hosts
  that mount the controller outside `WorkspaceProvider` (none in production
  today) silently get manual-only behaviour.
- The integration test uses `/tmp/app-account-sequence-*` (not the reserved
  `/private/tmp/chirality-*` prefix) and the repo root as the daemon
  instruction root; it took ~0.2 s locally with a 20 s timeout.
