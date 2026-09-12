# I1 return: Runtime workspace integration cleanup

Assignment: I1 of the D-GOV-43 (topology A2) spike integration, executed as a bounded Type 2 TASK (Fable 5.1), 2026-09-12. Worktree `.claude/worktrees/project-first-impressions-06aed9`, branch `claude/chirality-codex-replatform-3999f1`, on top of the W1 and W2 working-tree returns. Paths below are relative to `projects/chirality-runtime` unless stated. No git write operations were performed; the lead commits. No credential, keychain, session or trial data was read; no live sign-in.

## 1. Outcome

- `npm run build` (`tsc -b`, all seven package references) passes from an empty `dist` (every `packages/*/dist` removed first, so no stale output of a deleted module survives).
- `npm test -- --maxWorkers=1`: 34 test files passed, 309 tests passed, 0 failed, 0 skipped (foreground run, 53.8 s). The same result was obtained on the preceding clean-rebuild run.
- Baseline before this assignment: `tsc -b` failed with exactly two errors, both the retired `@chirality/runtime-core/runtime-conformance-v2` import in `packages/cli/src/cli.ts:15` and `packages/cli/test/cli.test.ts:8`; contracts, core, client and daemon already built clean.

## 2. Files changed and deleted (mine)

Changed:
- `packages/cli/src/cli.ts`: rewritten to the retained v1 surface (section 3).
- `packages/cli/src/config.ts`: `CliRuntimePaths.launchAgentsDirectory` and the `CHIRALITY_LAUNCH_AGENTS_DIRECTORY` variable removed; socket, token file and user data resolution unchanged.
- `packages/cli/src/index.ts`: exports only `cli.js` and `config.js`.
- `packages/cli/test/cli.test.ts`: tests of the removed commands and modules deleted; retained tests kept verbatim; four small tests added (project register/list, `daemon status`, retired commands answer usage error 2 without contacting the client, `resolveCliRuntimePaths` shape). 13 tests.
- `packages/contracts/src/delegated.ts`: see section 4.
- `packages/client/src/client.ts`: see section 5.
- `packages/client/test/client.test.ts`: one test added asserting the retired methods are gone and the retained hosted-bootstrap and turn-registry methods exist. 9 tests.
- `packages/daemon/src/runtime-daemon.ts`: see section 6.
- `packages/daemon/src/hosted-paths.ts`: `resolveHostedBootstrapTokenFile` removed (no reference anywhere in the runtime workspace or the frontend). `HOSTED_BOOTSTRAP_CLIENT_ID` (used by `tests/bootstrap-api.test.ts`), `hostedProjectClientId` (used by the daemon's hosted project registration) and `resolveHostedProjectTokenFile` (imported by the frontend's `src/lib/runtime-client/runtime-daemon-harness-port.ts` through `@chirality/runtime-daemon/hosted-paths`) are kept.

Deleted:
- `packages/cli/src/launch-agent.ts` (`LaunchAgentManager`, `renderRuntimeLaunchAgent`, `resolveRuntimeLaunchAgentOptions`, `RUNTIME_LAUNCH_AGENT_LABEL`): the App-owned Runtime service is spawned and stopped by Electron (design section 1, "No LaunchAgent"); nothing else imported it.
- `packages/cli/src/runtime-jobs.ts` and `packages/cli/test/runtime-jobs.test.ts` (`renderRuntimeJobs`): render-only two-job daemon/supervisor plists for the retired supervisor role; nothing else imported it.

Not touched: `codex-*.ts`, `app-owned-composition.ts`, `standalone*.ts`, `turn-registry.ts`, `packages/core/**`, `packages/daemon/src/hosted.ts` (it only re-exports `hosted-paths.js`, still valid), root `package.json` and `tsconfig.json` (no package reference needed to change), `package-lock.json`, and nothing under `projects/chirality-app-dev` except this return.

## 3. CLI (`@chirality/runtime-cli`)

Removed, with the reason:
- `release measure-support` and `CliDependencies.measureRuntimeSupportProfile`: the only consumer of the retired `runtime-conformance-v2` module (the build blocker reported by W1 and W3).
- `daemon install|start|stop|uninstall`, `RuntimeLaunchAgent`, `CliDependencies.launchAgent` and `CliDependencies.executablePath`: LaunchAgent job management has no target in the A2 composition.
- `hosted-login start|status|cancel`, `delegated capabilities|turn|interrupt|consent|approvals|decide-approval`, `approvals list|decide`, the `--explicit-user-act` flag and the optional v2 methods on `RuntimeCliClient`: they addressed `/v2/projects/:id/login|delegated|approvals` routes that the daemon no longer serves (section 6).

Kept, unchanged in behaviour and output conventions: `daemon status` (now prints the `RuntimeClient.daemonStatus()` response directly, without the former `launchAgent` wrapper key), `project register|list|status`, `models list|activate`, `session create|list|replay|turn|interrupt`, `run`, `--json` single-line output and NDJSON event streams, `--request-file` and standard-input prompts, the exit-code mapping (2 usage, 1 runtime or transport error, 130 interrupted, the turn's `process:exit` code) and the machine-readable stderr envelope for `RUNTIME_COMPATIBILITY_MISMATCH` and `--json` errors (`RUNTIME_COMPATIBILITY_MISMATCH` is still an error code in contracts and core). Usage text rewritten to list only these commands and to say the App starts and stops the service. `session get` was never a CLI command (the client has `getSession`); it was not added, per "do not add features". `CliDependencies` is now `{ client, paths, readTextFile }`.

## 4. Contracts (`packages/contracts/src/delegated.ts`)

- `DelegatedTurnRequest`: `compatibility` and `preflight` are optional (documented as historical v2 admission fields the App-owned Runtime ignores); added optional `developerInstructions?: string` and `contextUpdate?: string`. These are the names W1 uses in `core/delegated-runtime.ts` (`DelegatedTurnInput`, envelope allow-list, size checks) and `core/delegated-engine-adapter.ts` (`thread/start` and `thread/resume` `developerInstructions`, the `contextUpdate` input item). W1's `DelegatedTurnInput` still compiles unchanged against the new shape.
- Removed as unreferenced across `projects/chirality-runtime` and `projects/chirality-app-dev/frontend/src` after the CLI and client cleanup (verified by grep before each deletion): `CommandNetworkPosture`, `HostedConsent`, `DestinationApproval`, `HostedEngineConsentPort`, `DelegatedCapabilities`, `DelegatedApprovalDecisionRequest`, `HostedAccountBinding`, `HostedManagedAuth`, `HostedLoginStatus`, `validateHostedAccountBinding`, `validateHostedManagedAuth`, `validateHostedLoginStatus`, `NetworkApprovalChoice`, `NetworkApprovalPrompt`, `SupervisorNetworkApprovalPort`, `SupervisorApprovalDescription`, `SupervisorApprovalDescriptionPort`. The frontend's `HostedEngineConsentPort` and `CommandNetworkPosture` are its own definitions in `src/lib/consent/hosted-engine-consent-port.ts`, not contract imports; the frontend's actual contract imports (`HostedBootstrapStatus`, `HostedBootstrapLoginStartResponse`, `HostedBootstrapProjectRegistrationResponse`, `HostedModelCatalogEntry`, `HostedModelSelection`, `SessionTurnState`, `SessionRequestsResponse`, `AnswerSessionRequestResponse`, `ServerRequestAnswer`, the patterns, and the session, event and v3 types) are all retained.
- Kept although only the optional fields reference them: `RuntimeCompatibilityIdentity` and `DelegatedPreflight`. Removing them requires removing `compatibility`/`preflight` from `DelegatedTurnRequest`, which W1's `DelegatedTurnInput` (`Pick<DelegatedTurnRequest, "compatibility" | "preflight">` in `packages/core/src/delegated-runtime.ts:73-74`) would not compile against; that is a core edit outside my scope (section 8).
- `HostedBootstrapStatus` values left unchanged: `admission: "establishing"` is still produced by W1's `packages/daemon/src/hosted-bootstrap.ts:47` (signed in, catalog not yet read) and exercised by `tests/helpers.ts` and `tests/hosted-model-selection-contracts.test.ts`. `ceremony: "consent-required"` is not produced by core or daemon any more, but the frontend still emits and renders it (`src/__tests__/fixtures/controlled-v3-runtime.mjs`, `chat-panel-model-selectors.test.tsx`, `runtime-reconnect-refresh.test.tsx`), and the frontend reads status through `RuntimeClient.hostedBootstrapStatus`, which applies `validateHostedBootstrapStatus`; removing the value now would break I2's concurrent fixture work. Left in place and reported (section 8). `tests/bootstrap-api.test.ts` also stubs `consent-required` and passes as is.
- `WorkerContinuity`, `DelegatedHarnessProcessSupervisorPort`, retirement types, `DelegatedTurnResponse`, `DelegatedRoleEvidence`, the hosted model catalog and selection helpers, `HostedProviderNetworkConsentRequest` (used by the daemon consent route), the native Plan, runtime tool, progress, request and policy seams are unchanged.

## 5. Client (`packages/client/src/client.ts`)

Removed, together with their inline `/v2/...` paths (there were no `RUNTIME_ROUTES` constants for them): `startHostedLogin`, `hostedLoginStatus`, `cancelHostedLogin`, `runDelegatedTurn`, `interruptDelegatedTurn`, `delegatedCapabilities`, `delegatedPreflight`, the private `delegatedAdmission`, `grantDelegatedConsent`, `pendingDelegatedApprovals`, `decideDelegatedApproval`, `pendingRuntimeApprovals`, `decideRuntimeApproval`, and the now-unused contract imports. None of these names occurs anywhere under `projects/chirality-app-dev/frontend/src`, `electron` or `scripts`. Everything the frontend uses is kept: the v1 project, session, boot, replay, context, methods, native Plan, turn, permission, interrupt, agents, scaffold, models and credential methods, the v3 hosted-bootstrap methods (`registerHostedBootstrapProject`, `initializeHostedBootstrapProject`, `hostedBootstrapStatus`, `grantHostedProviderNetworkConsent`, `startHostedBootstrapLogin`, `cancelHostedBootstrapLogin`, `signOutHostedProject`) and W2's `attachSessionTurn`, `sessionTurnState`, `listSessionRequests`, `answerSessionRequest`. `sse.ts` is W2's and untouched.

## 6. Daemon (`packages/daemon/src/runtime-daemon.ts`, `index.ts`, `hosted-paths.ts`)

- `RuntimeDaemonOptions`: removed `login`, `loginProjectId` and `approvals`; `RuntimeApprovalControl` and the private `approvalControl()` helper are gone. `DelegatedControlPort` is reduced to `startGeneration(daemonId?)` and `close()`, which is exactly what `app-owned-composition.ts` passes (`delegated: DelegatedRuntime`); `requests: DelegatedRequestPort`, `turnRegistry`, `hostedBootstrap`, `sseKeepaliveMs` and `logger` are unchanged.
- Routes removed: `GET/POST /v2/projects/:id/login/{status,start,cancel}`, `GET/POST /v2/projects/:id/approvals/{pending,capabilities,preflight,decision}`, `GET/POST /v2/projects/:id/delegated/{capabilities,approvals,preflight,consent,approval-decision,interrupt,turn}`. They now fall through to the existing `NOT_FOUND` (404) for any non-`v1` prefix other than the retained `v3` hosted-bootstrap routes. Nothing in the composition, the frontend or the tests addressed them (the composition never supplied the legacy operations, so they answered 503 before).
- Kept: all v1 session routes, `POST .../turn`, `GET .../turn/stream`, `GET .../turn/state`, `.../interrupt`, `.../permission`, `GET .../requests`, `POST .../requests/:id/answer`, the v3 hosted-bootstrap project registration and per-project status/consent/login/logout routes, health, daemon status, projects, models, credentials, roles, methods, agents, scaffold, runs, replay, context and native Plan routes.
- `stop()` and `stopLogin()` no longer reference the removed `login` option; the hosted-bootstrap cancel-on-stop path and the 2 s grace are unchanged.
- `index.ts` already exported `./turn-registry.js` (W1 added it), so no change.

## 7. Tests

`npm test -- --maxWorkers=1` in `projects/chirality-runtime`: 34 files, 309 tests, all passing. In-scope files: `packages/cli/test/cli.test.ts` 13, `packages/client/test/client.test.ts` 9. Unchanged files retained their counts (`daemon.test.ts` 20, `runtime-v3-api.test.ts` 33, `turn-registry.test.ts` 7, `v2-contracts.test.ts` 18, `bootstrap-api.test.ts`, `hosted-model-selection-contracts.test.ts` 4, W1's composition, client, effective-home, supervisor, delegated-runtime and standalone files). No test outside `packages/cli/test` and `packages/client/test` needed editing.

## 8. Needed outside scope

1. Frontend (I2): `projects/chirality-app-dev/frontend/src/__tests__/integration/runtime-canonical-replay-restart.integration.test.ts` builds a `CliDependencies` literal with `launchAgent`, `executablePath`, `measureRuntimeSupportProfile` and `paths.launchAgentsDirectory` (lines 156-178). These fields no longer exist; the literal should be `{ client, paths: { userData, runtimeDirectory, socketPath, tokenFile }, readTextFile }`. Vitest strips the types so the test still runs, but the frontend `typecheck` will flag the excess properties if that file is in its program.
2. Frontend (I2, later): once `controlled-v3-runtime.mjs` and the two component tests stop emitting `ceremony: "consent-required"`, drop that value from `HostedBootstrapStatus` and `validateHostedBootstrapStatus` in `packages/contracts/src/delegated.ts` (one line each) and the stub in `tests/bootstrap-api.test.ts`. `admission: "establishing"` stays while `hosted-bootstrap.ts` produces it.
3. Core (W1 owner): to retire `RuntimeCompatibilityIdentity` and `DelegatedPreflight` completely, change `DelegatedTurnInput` in `packages/core/src/delegated-runtime.ts:73-75` to `DelegatedTurnRequest` (the request type now carries `developerInstructions` and `contextUpdate` itself), then delete the two optional fields and the two interfaces from contracts.
4. `packages/cli/package.json` still lists `@chirality/runtime-core` as a dependency although the CLI no longer imports it (its tsconfig references only contracts and client). Dropping it touches `package-lock.json`, which is outside my write scope; harmless as is.
5. `packages/daemon/src/hosted.ts` (W1) re-exports `hosted-paths.js`; still valid, no action.

## 9. Notes

- The CLI remains a compatibility surface on the App path ("CLI compatibility unverified"): it was made smaller and honest about what the service serves, not extended.
- No em-dashes were introduced. No payload that can carry account data is logged or printed by the changed code beyond what the retained commands already printed.
