# W3 return: Electron child lifecycle and packaging

Assignment: W3 of `SPIKE_DESIGN.md` section 12 (section 9, with the section 1 configuration schema). Executor: Fable 5.1 TASK instance, 2026-09-12. Basis: the worktree at branch `claude/chirality-codex-replatform-3999f1` on main `e83cb1f47` plus the lead's pre-authored contract seam. No git write operations were performed beyond `git rm` staging of retired files in the working tree; the lead commits. Nothing under `projects/chirality-runtime` was edited. The owner's Codex home, keychain, trial data, installed Apps, `~/Library/Application Support/Chirality*` and LaunchAgents were not read or touched. `desktop:dist` was not run.

All paths below are relative to `projects/chirality-app-dev/frontend` unless stated.

## 1. Files added

- `electron/runtime-service-host.ts`: the App-owned service host (no Electron import, so it is unit-testable with a fake child). Path resolution under `userData/runtime` with the 103-byte macOS socket limit check, the `chirality-app-owned/v1` config builder, private atomic config write (directory 0700, file 0600), ready-line parsing, spawn and ready wait (30 s), restart backoff 1, 2, 4, 8, 16, 30 s, give-up after 5 failures in 3 minutes, SIGTERM then SIGKILL after 5 s on stop, no restart during stop, stderr lines to the desktop log, state snapshots for the connectivity IPC.
- `electron/runtime-service-launcher.ts`: the Electron-side launcher, `utilityProcess.fork` with piped stdio and a `serviceName`, exit and kill adapters matching the host's child port.
- `electron/codex-executable.ts`: the pinned version constant (`0.154.0`), target triple resolution by platform and arch, development resolution from the installed `@openai/codex` platform package, packaged resolution from `resources/codex`, the signed-binary list.
- `electron/runtime-control-ipc-contract.ts`: the one remaining runtime control channel, `chirality:runtime-service-restart`, shared by preload and main.
- `scripts/pack-electron.mjs`: the plain pack (replaces `pack-electron-with-supply.mjs`).
- `scripts/verify-codex-pin.mjs`: `desktop:verify-codex-pin`.
- `src/__tests__/electron/fixtures/fake-runtime-service.mjs`: a fake service child driven by environment variables (ready, exit before ready, never ready, delayed exit, stderr lines, ignore SIGTERM).
- `src/__tests__/electron/runtime-service-host.test.ts` (12 tests), `src/__tests__/electron/codex-executable.test.ts`, `src/__tests__/scripts/pack-electron.test.ts`, `src/__tests__/scripts/verify-codex-pin.test.ts`.

## 2. Files changed

- `electron/main.ts`: one GUI path. Resolves the service paths (honouring a `CHIRALITY_RUNTIME_SOCKET_PATH` override), exports `CHIRALITY_RUNTIME_DIRECTORY`, `CHIRALITY_RUNTIME_SOCKET_PATH` and `CHIRALITY_RUNTIME_TOKEN_FILE` into `process.env` before the in-process Next server starts and removes `CHIRALITY_RUNTIME_BOOTSTRAP_TOKEN_FILE`, creates the main-process `RuntimeClient({socketPath, tokenFile})`, resolves the Codex executable and the service entry, writes the config, starts the host without awaiting readiness, keeps the connectivity supervisor and the socket watcher, broadcasts host state changes as `service` on the connectivity payload, registers the restart IPC, and tears down in the order renderer server then service child. `before-quit` waits for the teardown; window close on macOS stops nothing.
- `electron/preload.ts`: `runtime.daemon`, `runtime.models` and `runtime.hostedAccount` removed; `runtime.service.restart()` added.
- `electron/runtime-control-ipc.ts`: reduced to the restart handler with the same sender authorisation (`isAuthorizedSender(event, deps.rendererOrigin)`) and error redaction.
- `electron/desktop-log.ts`: account e-mail redaction at the writer (`[redacted-email]`), applied to every line including service stderr.
- `electron/desktop-process-policy.ts`: trimmed to the `userData` override helper.
- `src/types/chirality-window.d.ts`: hosted-account types and the `runtime.hostedAccount` block removed (retired IPC surface only).
- `scripts/build-electron.mjs`: native-admission, hosted, conformance and protected-CLI aliases removed; adds the runtime service bundle (`dist-runtime/runtime-service/standalone-bin.mjs` from `packages/daemon/src/standalone-bin.ts`) next to the runtime CLI bundle (`dist-runtime/runtime-cli/chirality-cli.mjs`), both ESM with a `createRequire` banner.
- `scripts/sign-electron-runtime-v2.mjs`: reduced to the App plus the two Codex binaries: hardened runtime everywhere, App entitlements for the bundle and helpers, `build/entitlements.mac.code-mode-host.plist` for `codex-code-mode-host` only, inherit entitlements for everything else; post-sign strict verification of the two binaries and the bundle.
- `scripts/finalize-electron-resources.mjs` (electron-builder `afterPack`): required and forbidden resource entries for the A2 layout, writes `packaged-resources-inventory.json`.
- `scripts/verify-packaged-dependency-boundary.mjs` (`desktop:verify-dependencies`): checks the staged Codex tree, forbids `@openai` and legacy runtime packages inside `app.asar`, proves from the source maps that the main bundle embeds the host and launcher and not the daemon, that the service bundle embeds `standalone-bin.ts`, `runtime-daemon.ts`, `runtime-service.ts`, `delegated-runtime.ts`, `codex-supervisor.ts` and `codex-app-server-client.ts`, and that the CLI bundle carries no server source.
- `package.json`: `@openai/codex` `0.154.0` (exact) added, `@chirality/native-admission` removed, `runtime:build` replaces `runtime:build-core`, `desktop:prepare`, `desktop:pack`, `desktop:dist` and `desktop:verify-codex-pin` as in the table below, `desktop:bind-payload` removed, `build.files` excludes `node_modules/@openai/**`, `extraResources` as in section 4, fuses unchanged (`runAsNode: false`).
- `package-lock.json`: the two dependency changes only; the Pi nested integrity fields were restored with `npm run pi:lock-integrity` (the diff moves the three fields inside their entries, it does not drop them).
- Tests updated: `runtime-control-ipc.test.ts`, `desktop-process-policy.test.ts`, `desktop-log.test.ts`, `folder-preload.test.ts`, `build-electron.test.ts`, `sign-electron-runtime-v2.test.ts`, `finalize-electron-resources.test.ts`, `verify-packaged-dependency-boundary.test.ts`, `dmg-packaging-policy.test.ts`, `desktop-release-workflow.test.ts` (the RunAtLoad proof assertions are removed because the proof script is retired; the workflow itself is out of scope, see section 7).
- Coordination records: `PACKAGING_PROCEDURE.md` step 1 (plain pack, `runtime:build`, the bundles, the check sequence), step 2 (two Codex binaries, identity selection, `utilityProcess` and the fuse) and step 4 (which comparison happens before and after signing); `NATIVE_CHECKLIST.md` item 2 names `desktop:verify-codex-pin -- --after-signing`. Both edits carry a note saying they were revised by W3 and why.

## 3. Files deleted

Electron: `runtime-host.ts`, `runtime-host-legacy.ts`, `runtime-autostart.ts`, `daemon-activate-policy.ts`, `desktop-daemon-posture.ts`, `host-account-connection.ts`, `host-account-ipc-contract.ts`, `host-account-ipc.ts`, `protected-runtime-cli.ts` (unused after the rewrite), `cli-launcher.ts` (depended on `desktop-daemon-posture.ts`, not independent), `desktop-entry-mode.ts`, `daemon-instruction-root.ts`, `desktop-project-client.ts`.

Scripts: `pack-electron-with-supply.mjs`, `run-packaged-launchagent-login-proof.mjs`, `run-packaged-launchagent-runatload-proof.mjs`, `run-packaged-daemon-instruction-root-proof.mjs`.

Tests: the electron tests of every module above (`cli-launcher`, `daemon-activate-policy`, `daemon-instruction-root`, `desktop-daemon-posture`, `desktop-entry-mode`, `desktop-project-client`, `host-account-connection`, `host-account-ipc-connection`, `host-account-ipc`, `hosted-account-sequence.integration`, `protected-runtime-cli`, `runtime-autostart`, `runtime-daemon-signal-integration`, `runtime-host-agent1-manager`, `runtime-host-socket-path`), the four script tests of the deleted scripts, and the fixture `launchctl-print-r19-never-exited.txt`.

## 4. Exact spawn and config

Deviation from section 9, recorded here with the reason: the design says `process.execPath` with `ELECTRON_RUN_AS_NODE=1`. The App's electron-builder fuses set `runAsNode: false` (and `enableNodeOptionsEnvironmentVariable: false`), which makes `ELECTRON_RUN_AS_NODE` inert in the packaged App; the child would start a second GUI instance. Rather than flip the fuse, the host starts the service through Electron's supported `utilityProcess.fork`, probed in a scratch script against Electron 43: the child sees `process.argv` as `[helper, entry, ...args]` so the service's `argv.slice(2)` contract holds, the environment and piped stdio behave as with `child_process`, `pid` is available after the `spawn` event, and signals are delivered with `process.kill(pid, signal)`. The Codex child is spawned by the service, not by the App.

Spawn (from `electron/runtime-service-launcher.ts`, invoked by the host):

```
utilityProcess.fork(
  <serviceEntry>,
  ['daemon', '--config', '<userData>/runtime/service-config.json'],
  { stdio: ['ignore', 'pipe', 'pipe'], env: <env>, serviceName: 'chirality-runtime-service' }
)
```

`<serviceEntry>` is `CHIRALITY_RUNTIME_SERVICE_ENTRY` when set, else `<resourcesPath>/runtime-service/standalone-bin.mjs` when packaged, else `../../chirality-runtime/packages/daemon/dist/standalone-bin.js` relative to `frontend/`. `<env>` is a copy of the App's `process.env` without `ELECTRON_RUN_AS_NODE` and `NODE_OPTIONS`; `CHIRALITY_RUNTIME_DIRECTORY`, `CHIRALITY_RUNTIME_SOCKET_PATH` and `CHIRALITY_RUNTIME_TOKEN_FILE` are already present because `main.ts` sets them before the launch. The host waits up to 30 s for a stdout line parsing as `{"ready":true,"role":"daemon","socketPath":...,"clientTokenFile":...}`; the paths in the ready line are logged and published in the host state, while the main-process client and the Next server use the config values (the host does not compare the two). Stop is SIGTERM, then SIGKILL after 5 s.

Config written to `<userData>/runtime/service-config.json` (mode 0600, directory 0700, written through a temporary file and rename):

```
{
  "schema": "chirality-app-owned/v1",
  "socketPath": "<userData>/runtime/control.sock",
  "runtimeDirectory": "<userData>/runtime",
  "instructionRoot": "<resourcesPath>/instruction-root" (packaged) | "<repository root>" (development),
  "clientTokenFile": "<userData>/runtime/client-token",
  "codex": {
    "executablePath": "<resourcesPath>/codex/bin/codex" (packaged) | "<frontend>/node_modules/@openai/codex-<platform>-<arch>/vendor/<triple>/bin/codex" (development),
    "userCodexHome": "$CODEX_HOME" | "~/.codex",
    "effectiveHome": "<userData>/runtime/codex-home",
    "expectedVersion": "0.154.0"
  }
}
```

`CHIRALITY_RUNTIME_SOCKET_PATH` in the App's environment overrides `socketPath` (the harness CI uses this); the 103-byte limit is asserted on the final value. The main-process client is `new RuntimeClient({ socketPath, tokenFile: clientTokenFile })`; token reads are the client's, the App never parses the token itself.

Host state exposed to the renderer through the existing connectivity broadcast as `service`: `status` (`idle`, `starting`, `ready`, `restarting`, `stopping`, `stopped`, `failed`), `pid`, `socketPath`, `clientTokenFile`, `restarts`, `recentFailures`, `lastExit`, `lastError`, `nextRestartAt`, `changedAt`. `failed` is the give-up state; the renderer's retry action calls `window.chirality.runtime.service.restart()`, which resets the failure window and starts again.

## 5. Packaging layout

`Chirality.app/Contents/Resources/`:

- `app.asar`: `dist-electron/main.js` and `preload.js` with maps, `.next`, `public`, `package.json`, `next.config.mjs`; no `node_modules/@chirality/**` and no `node_modules/@openai/**`.
- `codex/`: the whole `vendor/aarch64-apple-darwin` tree of the installed `@openai/codex-darwin-arm64` package: `bin/codex`, `bin/codex-code-mode-host`, `codex-path/rg`, `codex-resources/` (zsh), `codex-package.json`.
- `runtime-service/standalone-bin.mjs` and `.map`.
- `runtime-cli/chirality-cli.mjs` and `.map`.
- `instruction-root/` (from `node_modules/.cache/chirality-instruction-root`, with `instruction-bundle-manifest.json`).
- `packaged-resources-inventory.json` (written by the `afterPack` hook, schema `chirality-packaged-resources-inventory/v1`).

Forbidden and checked absent: `supplier`, `native`, `runtime-governance`, any admission addon, any LaunchAgent plist. The two Codex binaries are signed with the App identity and the hardened runtime; only `codex-code-mode-host` receives the JIT entitlement.

## 6. Scripts

| Script | Command | Purpose |
|---|---|---|
| `runtime:build` | `npm --prefix ../../chirality-runtime run build` | Builds the Runtime workspace (replaces `runtime:build-core`). |
| `build:electron` | `node ./scripts/build-electron.mjs` | Main and preload bundles plus the service and CLI ESM bundles under `dist-runtime/`. |
| `desktop:prepare` | `instruction-root:prepare`, `runtime:build`, `build`, `pack-electron.mjs` | Full unsigned directory build from source. |
| `desktop:pack` | `pack-electron.mjs`, `desktop:verify-dependencies`, `desktop:verify-codex-pin`, `instruction-root:integrity` | Unsigned candidate with the pre-signing digest comparison. |
| `desktop:dist` | `pack-electron.mjs --target dmg`, `desktop:verify-dependencies`, `desktop:verify-codex-pin -- --after-signing`, `instruction-root:integrity` | Signed DMG (identity through `CHIRALITY_SIGNING_IDENTITY_SHA1`; not run by W3). |
| `desktop:verify-dependencies` | `verify-packaged-dependency-boundary.mjs` | Codex tree, asar contents, source-map proofs for the three bundles. |
| `desktop:verify-codex-pin` | `verify-codex-pin.mjs [--after-signing]` | `package.json` pin, lockfile umbrella and platform package, packaged `codex --version`, staged `codex-package.json`, sha256 of both binaries against the installed package (digest failures are informational after signing). |
| `electron:supply-chain` | `verify-electron-dist.mjs` | Unchanged: verifies the Electron distribution zip against the pinned digest. |

`scripts/pack-electron.mjs` accepts `--target dir|dmg`, honours `CHIRALITY_ELECTRON_OUTPUT_DIRECTORY`, passes a single `-c.electronDist=` argument without a shell, sets `CSC_IDENTITY_AUTO_DISCOVERY=false` unless the identity SHA-1 is given, and refuses to run when a build input is missing, the Codex binary is not executable, or the pin is not exact.

## 7. Tests and checks run

- `npx vitest run src/__tests__/electron src/__tests__/scripts`: 37 files passed, 459 tests passed, 0 failed (final run after all edits).
- `npx tsc -p tsconfig.electron.json --noEmit`: clean.
- `npx tsc --noEmit` (root project): errors only in two out-of-scope integration tests, `src/__tests__/integration/runtime-canonical-replay-restart.integration.test.ts` (cannot find the `@chirality/runtime-cli` types until the Runtime workspace is built) and `src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts` (imports the retired `electron/daemon-instruction-root`).
- `node ./scripts/build-electron.mjs`: `dist-electron/main.js` (177 KB), `preload.js` and `dist-runtime/runtime-service/standalone-bin.mjs` (746 KB) build. The CLI bundle fails on `packages/cli/src/cli.ts:15` importing `@chirality/runtime-core/runtime-conformance-v2`, which W1 removed; the CLI package is outside every W scope.
- `npm run pi:lock-integrity`: PASS; `src/__tests__/scripts/pi-lock-integrity.test.ts` passes.
- `npm install --save-exact @openai/codex@0.154.0` and `npm uninstall @chirality/native-admission` were the only installs; the lockfile accepted both. The installed `codex --version` prints `codex-cli 0.154.0`.

Not run: `desktop:dist`, `desktop:pack` (needs the CLI bundle and the Runtime build), the full frontend `npm test` (W4 is editing `src/**` concurrently; the subset above is the W3 gate).

## 8. Needed outside the W3 scope

Root `.github/workflows/harness-premerge.yml` (root workflows are outside scope):

- The "Initialize runner paths" step exports `CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE=.../runtime/auth/tokens/operator.token`; the "Register app-dev with shared runtime" step waits for that file, registers the project through `out/controlled-ci/chirality-cli.mjs` and exports `CHIRALITY_RUNTIME_TOKEN_FILE`, `CHIRALITY_RUNTIME_PROJECT_ID` and `CHIRALITY_RUNTIME_PROJECT_ROOT`. Under A2 the App sets `CHIRALITY_RUNTIME_TOKEN_FILE` to `<userData>/runtime/client-token` and no project token is minted; the recommended change is to start the built service directly (`node projects/chirality-app-dev/frontend/dist-runtime/runtime-service/standalone-bin.mjs daemon --config <file>` with a CI-written `chirality-app-owned/v1` config, or the Runtime workspace's own built `standalone-bin.js`), wait for the ready line or the socket plus `client-token`, and export `CHIRALITY_RUNTIME_TOKEN_FILE` to the client token file. Drop the operator token variable, the `project register` step and the two project variables unless W4 keeps a project registration route.
- The "Build controlled CI runtime" step runs `scripts/build-controlled-ci-runtime.mjs`, which bundles `scripts/controlled-ci-runtime.ts`. That file (in my scope) imports `ResidencyCoordinator`, `RuntimeService`, `OmlxControlPort` and `RuntimeDaemon` composition pieces that W1 has removed from `@chirality/runtime-core`; I did not rewrite it because its replacement depends on W1's final composition entry (`app-owned-composition.ts`). Recommendation: retire `controlled-ci-runtime.ts` and `build-controlled-ci-runtime.mjs` and use the service bundle above; if a controlled stub engine is still wanted for CI, it should be an option of the App-owned composition, not a separate composition.
- `.github/workflows/desktop-release-template.yml` lines 84 to 103 reference `run-packaged-launchagent-runatload-proof.test.ts`, run `scripts/run-packaged-launchagent-runatload-proof.mjs` and upload its summary. All three are deleted; remove the vitest include, the proof step and the artifact upload. `npm run desktop:dist` remains the packaging entry. `src/__tests__/scripts/desktop-release-workflow.test.ts` no longer asserts those steps.

W4 (`frontend/src/**`):

- `src/lib/harness/hosted-bootstrap-client.ts` (or its successor) must stop calling `window.chirality.runtime.hostedAccount.*`; the bridge is gone from preload and from `chirality-window.d.ts`.
- `src/lib/shell/shell-frame.tsx` and any renderer code using `window.chirality.runtime.daemon.*` or `runtime.models.*` must move to the connectivity payload and `runtime.service.restart()`.
- The connectivity payload now carries `service: RuntimeServiceState | null` (the shape is in `electron/runtime-service-host.ts`); the renderer's `RuntimeConnectivitySnapshot` type in `src/**` and the "Runtime stopped" state with its retry action need that field.
- The Next harness runtime client should read `CHIRALITY_RUNTIME_TOKEN_FILE` (the client token) and stop expecting `CHIRALITY_RUNTIME_PROJECT_ID` and `CHIRALITY_RUNTIME_PROJECT_ROOT`, which the App no longer sets.
- `src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts` imports the retired `electron/daemon-instruction-root`; retire or rewrite it against the service config.

Runtime workspace (W1 or lead): `packages/cli/src/cli.ts` still imports `@chirality/runtime-core/runtime-conformance-v2`; until that import goes, `build:electron` cannot produce the CLI bundle and `desktop:pack` will refuse to run. The service bundle also depends on W1's `standalone-bin.ts` printing the ready line with `socketPath` and `clientTokenFile` equal to the config values and honouring `--config`; the host was tested only against the fake child.

## 9. Open risks

- `utilityProcess` instead of `ELECTRON_RUN_AS_NODE`: exit reporting gives an exit code but no signal name, and the child runs with Electron's Node, not a standalone Node; the service must not rely on `process.execPath` being usable to spawn further Node children (the Codex child is a native binary, so this does not affect A2). If the lead prefers the literal design, the fuse `runAsNode` must be flipped to `true`, which widens the packaged App's attack surface and is why I did not do it.
- First start is not awaited: the window opens while the service is `starting`; the renderer must show that state from the `service` field rather than a generic disconnect.
- `packaged-resources-inventory.json` and the `afterPack` checks have been exercised only through unit tests with fixture trees; a real `desktop:pack` run is pending the Runtime build and CLI fix.
- `verify-codex-pin` reads the umbrella and platform entries from the lockfile and requires the platform package to be installed; a CI runner on another platform or arch needs the matching optional package present.
- `scripts/controlled-ci-runtime.ts` is currently broken against W1's core and remains in the tree pending the decision in section 8.
- The contract-pins manifest still pins the Pi and Agent SDK scripts and the `desktop:*` script contents; those pins were kept satisfied, but any later rename of `pack-electron.mjs` must keep `desktop:verify-dependencies` inside `desktop:pack` and `desktop:dist`.
