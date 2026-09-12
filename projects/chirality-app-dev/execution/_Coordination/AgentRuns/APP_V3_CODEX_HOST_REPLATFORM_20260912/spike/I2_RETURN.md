# I2 return: frontend CI fixture, integration tests and workflow alignment

Assignment: I2 of the D-GOV-43 (topology A2) integration, after W1 to W4 and concurrently with I1 (Runtime CLI cleanup). Executor: Fable 5.1 TASK instance, 2026-09-12. Basis: the worktree at branch `claude/chirality-codex-replatform-3999f1` (main `e83cb1f47`) with the W1 to W4 spike returns and I1's `packages/cli/src/cli.ts` cleanup in the working tree. No git write operations; the lead commits. Nothing under `projects/chirality-runtime` was edited (its packages were built with `tsc -b` into gitignored `dist/` for verification only). No installed App, `~/Library/Application Support/Chirality*`, LaunchAgent, `launchctl`, credential, Codex home or trial data was touched. Scratch files stayed under the session scratchpad, except the Unix sockets of the fixture smoke runs, which used `os.tmpdir()` because the scratchpad path exceeds the 103-byte socket limit (the existing integration tests use `os.tmpdir()` the same way).

Paths below are relative to `projects/chirality-app-dev/frontend` unless stated.

## 1. Files changed

- `scripts/controlled-ci-runtime.ts` (rewritten): still a stub-engine `RuntimeDaemon` over `RuntimeService` for the release-quality wrapper (no Codex, no sign-in, no App-owned composition). `RuntimeService`'s constructor and `ResidencyCoordinator` are unchanged in W2's core, so the composition is the same as before; the daemon is bound without a turn registry, requests port, delegated runtime or hosted bootstrap (all optional in `RuntimeDaemonOptions`). New: the entry takes `--manifest <absolute path>` (the only accepted argument; anything else is refused with a usage error), registers that manifest itself through `service.registerProject(manifest, "github-actions", "harness-premerge-ci")`, and prints exactly one ready line (section 2). Exports `CONTROLLED_CI_PURPOSE`, `CONTROLLED_CI_APPROVED_BY`, `CONTROLLED_CI_APPROVAL_REFERENCE`, `ControlledCiRuntimeReady`, `parseControlledCiReadyLine`, `parseControlledCiArguments`, `startControlledCiRuntime`. The `CHIRALITY_CONTROLLED_CI_RUNTIME` purpose guard is unchanged.
- `scripts/build-controlled-ci-runtime.mjs`: bundles only the fixture (the separate `chirality-cli.mjs` bundle is dropped; nothing consumed it once the workflow stopped registering through the CLI, and dropping it removes the fixture build's dependency on the CLI package). `@chirality/runtime-daemon` resolves to `packages/daemon/src/runtime-daemon.ts` directly so the package index (which re-exports the Codex client, supervisor and App-owned composition) never enters the graph. Forbidden fragments now: `/electron/main.ts`, `/electron/runtime-service-host`, `/electron/runtime-service-launcher`, `/engine-pi-omlx/`, `/engine-claude/`, `/daemon/src/app-owned-composition`, `/daemon/src/standalone`, `/daemon/src/hosted-bootstrap`, `/hosted-private-`, `/native-admission/`, `/codex-`, `/packages/cli/`. Required fragments: `scripts/controlled-ci-runtime.ts`, `daemon/src/runtime-daemon.ts`, `daemon/src/turn-registry.ts`, `core/src/runtime-service.ts`, `core/src/project-registry.ts`, `src/lib/harness/agent-sdk-manager.ts`. The built graph has 131 inputs; from the daemon package only `runtime-daemon.ts`, `turn-registry.ts` and `hosted-paths.ts`.
- `scripts/verify-packaged-dependency-boundary.mjs`: removed the deleted sources from the forbidden lists (`chirality-runtime/packages/cli/src/launch-agent.ts` and `chirality-runtime/packages/native-admission/src/index.ts` in both the desktop and the service lists) and the "native admission" wording in the header comment. The rest of W3's rewrite is untouched (the large diff against `HEAD` is W3's).
- `scripts/verify-electron-dist.mjs`: inspected, no reference to LaunchAgent, supplier or native admission; unchanged.
- `src/__tests__/scripts/verify-packaged-dependency-boundary.test.ts`: the "fails closed" case now uses `electron/runtime-autostart.ts` as the retired desktop source instead of the native-admission entry.
- `src/__tests__/integration/controlled-ci-runtime.integration.test.ts`: builds the fixture, asserts the controlled graph (now also `project-registry.ts` present and no `app-owned-composition`, `runtime-service-host` or `packages/cli/`), asserts the purpose-guard refusal and the missing `--manifest` refusal, spawns the fixture with `--manifest`, parses the ready line, checks the token file name (`project-<uuid>.token` under `<runtime>/auth/tokens`), the canonical `projectRoot`, the registry record's `approval.approvedBy === "github-actions"`, then drives a stub turn over the socket with the project token. Turn frames now carry W2's `seq`, so the event assertions use `objectContaining` and additionally assert `seq` is 1..n.
- `src/__tests__/integration/runtime-canonical-replay-restart.integration.test.ts`: kept (it tests retained behaviour: canonical replay across a daemon restart, Desktop port and CLI replay equal). The `CliDependencies` literal is trimmed to I1's `{ client, paths, readTextFile }`; `paths` no longer has `launchAgentsDirectory`.
- `src/__tests__/integration/runtime-successor-adapters.integration.test.ts`: unchanged; passes against current exports.
- `src/components/settings/runtime-status.tsx` (W4's file, untracked): adds the "Restart Runtime" action. `RuntimeStatusView` takes an optional `restart` port; the button renders only in the Stopped state and only when the preload bridge is present, shows "Restarting Runtime" while pending and the returned `error` when `ok: false`. `RuntimeStatus` resolves the port from `window.chirality.runtime.service.restart`. The Running state still renders no `<button>` (asserted by `runtime-settings.test.ts`).
- `src/types/chirality-window.d.ts`: declares `runtime.service.restart(): Promise<RuntimeServiceControlResultPayload>` with `RuntimeServiceStatePayload` mirroring `electron/runtime-service-host.ts`'s `RuntimeServiceState` and `electron/runtime-control-ipc-contract.ts`'s result union. No `electron/**` change was needed: W3's preload already exposes `runtime.service.restart()`.
- Root `.github/workflows/harness-premerge.yml` and `.github/workflows/desktop-release-template.yml`: section 2.

## 2. Files deleted

- `src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts`: retired. It exercised the shared per-user daemon composed with `@chirality/engine-pi-omlx` and the retired `electron/daemon-instruction-root`; under A2 there is no shared daemon and the Pi engine is not composed on the App path, so nothing it proved survives to re-point.

## 3. New CI step shape

`harness-premerge.yml`: the "Start shared runtime daemon" and "Register app-dev with shared runtime" steps are replaced by one "Start controlled CI runtime" step; `CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE` is dropped from "Initialize runner paths"; every other step is unchanged. The step runs

```
CHIRALITY_CONTROLLED_CI_RUNTIME=chirality-controlled-ci-runtime/v1 \
  node out/controlled-ci/controlled-runtime.mjs \
    --manifest "${GITHUB_WORKSPACE}/projects/chirality-app-dev/chirality.project.json"
```

in the background, polls its log for the ready line (up to 90 s, failing early if the process exits), and validates it with `node -e`. The ready line is exactly one JSON object:

```
{"status":"ready","purpose":"chirality-controlled-ci-runtime/v1","socketPath":"<CHIRALITY_RUNTIME_SOCKET_PATH>","tokenFile":"<runtime>/auth/tokens/project-<uuid>.token","projectId":"chirality-app-dev","projectRoot":"<realpath of projects/chirality-app-dev>"}
```

The step requires `status`, `purpose`, `socketPath` equal to `CHIRALITY_RUNTIME_SOCKET_PATH`, `projectId === "chirality-app-dev"`, `projectRoot` equal to the realpath of `${GITHUB_WORKSPACE}/projects/chirality-app-dev`, and a non-empty `tokenFile`, then exports `CHIRALITY_RUNTIME_TOKEN_FILE=<tokenFile>`, `CHIRALITY_RUNTIME_PROJECT_ID=chirality-app-dev`, `CHIRALITY_RUNTIME_PROJECT_ROOT=${GITHUB_WORKSPACE}/projects/chirality-app-dev` and `HARNESS_PROJECT_ROOT=${GITHUB_WORKSPACE}/projects/chirality-app-dev`. The App's `createRuntimeDaemonHarnessPortFromEnvironment` still requires a `project-*.token` file, `CHIRALITY_RUNTIME_PROJECT_ID === "chirality-app-dev"` and a project root, so all three variables stay. The "Build controlled CI runtime", "Start frontend server", readiness, wrapper, summary, log and stop steps are unchanged (the stop step still kills the daemon pid). `src/__tests__/contract-pins.manifest.ts` pins three strings of this workflow (`--manifest "${GITHUB_WORKSPACE}/projects/chirality-app-dev/chirality.project.json"`, `echo "CHIRALITY_RUNTIME_TOKEN_FILE=${project_token}"`, `echo "HARNESS_PROJECT_ROOT=${GITHUB_WORKSPACE}/projects/chirality-app-dev"`); the new step satisfies them as written, so the manifest (outside my scope) needed no edit.

The step was executed locally by extracting its `run:` block from the YAML and running it with `GITHUB_WORKSPACE` at the repository root and `GITHUB_ENV` at a scratch file: exit 0, and the four variables above were appended with the project token path. A separate smoke run of the built fixture against the real `chirality.project.json` registered `chirality-app-dev`, served a stub turn (`harness:event, session:init, chat:delta, chat:delta, chat:complete, session:complete, harness:event, process:exit`) and stopped cleanly on SIGTERM. Note for the runner: the manifest's `legacySessionRoots` entry `frontend/.chirality/sessions` must exist at registration; the existing "Initialize runner paths" step still creates it.

`desktop-release-template.yml`: removed `src/__tests__/scripts/run-packaged-launchagent-runatload-proof.test.ts` from the policy-test invocation, the "Prove packaged LaunchAgent RunAtLoad" step and its "Upload packaged LaunchAgent RunAtLoad proof evidence" step. The workflow carried no supplier or native-admission staging step. Everything else (S0 block, unsigned posture check, `desktop:dist`, artifact verification with `verify-packaged-dependency-boundary.mjs`, packaged Agent SDK proofs, DMG mount checks, upload) is unchanged. Both workflows parse with `python3 -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]))"`.

## 4. Tests retired

- `runtime-desktop-cli-shared-daemon.integration.test.ts`: shared per-user daemon with the Pi engine and the retired daemon instruction root; nothing to re-point (section 2).

Not retired: `runtime-canonical-replay-restart` (retained behaviour, repaired) and `runtime-successor-adapters` (passes unchanged).

## 5. Counts

All in `projects/chirality-app-dev/frontend`, after every edit above and after I1's CLI change (`packages/cli` rebuilt with `tsc -b`):

- `npx tsc --noEmit --incremental false`: 0 errors.
- `npx tsc -p tsconfig.electron.json --noEmit --incremental false`: 0 errors.
- `npm run build:electron`: exit 0; `dist-electron/main.js`, `dist-electron/preload.js`, `dist-runtime/runtime-service/standalone-bin.mjs` (738 KB), `dist-runtime/runtime-cli/chirality-cli.mjs` (78 KB). Before I1's change the CLI bundle failed on the conformance import, as W3 reported; it built once `cli.ts` no longer imported it.
- `node scripts/build-controlled-ci-runtime.mjs`: exit 0, graph assertion passes.
- `npm test` (vitest, full suite): Test Files 202 passed, 1 skipped (203); Tests 2066 passed, 4 skipped (2070); 0 failed. The skipped file is `src/__tests__/integration/pec-bridge.integration.test.ts`, an intentional `it.skip` gated on `PEC_BRIDGE_IT=1` that predates this work.
- Subsets: `src/__tests__/integration` 5 files passed, 1 skipped (19 tests passed, 4 skipped); `src/__tests__/integration src/__tests__/scripts src/__tests__/electron` 41 files passed, 1 skipped (477 passed, 4 skipped) before the last two fixture edits, then re-run green with `contract-pins.test.ts` (6 files, 39 tests).

## 6. Needed outside the I2 scope

- Coordinator's point (2), `consent-required` in `HostedBootstrapStatus`: the controlled CI fixture never emits hosted bootstrap status (it composes no hosted bootstrap controller). The frontend emitters are `src/__tests__/fixtures/controlled-v3-runtime.mjs` (line 68, the v3 proxy fixture's initial hosted status), `src/__tests__/components/chat-panel-model-selectors.test.tsx` (line 127) and `src/__tests__/components/runtime-reconnect-refresh.test.tsx` (line 263). None is in my write scope. If those three are changed to another ceremony value, the contracts can drop `consent-required`.
- No component test covers the new "Restart Runtime" button (`src/__tests__/components/**` is outside my scope); the existing `runtime-settings.test.ts` and `settings-view-codex.test.tsx` still pass. A small case rendering `RuntimeStatusView` with `snapshot.state = 'disconnected'` and a fake `restart` would close that.
- `docs/harness/README.md` and related harness docs may still describe the operator-token registration step of the old workflow; not checked in detail and outside scope.
- The runtime workspace `tsconfig.json` still references `packages/engine-claude` and `packages/engine-pi-omlx`; they build, and `runtime-successor-adapters` still imports the App-side legacy adapters. Whether those adapters and packages stay is a lead decision, not an I2 defect.
