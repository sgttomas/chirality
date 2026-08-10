# Proposed command-register amendment v1.18 — Attempt-8 R3

Status: `PROPOSED — FRESH VERIFIER AND OWNER APPROVAL REQUIRED — NOT EXECUTED`

This proposal adopts verifier return
`93d5e64db0017f14b61c327cae86a009a103a10be593514ea39314bedb312b4e`.
V1.16/v1.17 and their scripts remain unchanged rejected history. No proposed
script or command was executed. Read-only hashing and static parsing only are
permitted before fresh verification.

Script hashes:

- controller R3 `3bdcad4ff8136acbddab10b2e454ab05bf19a26baa85b2e19e9af3876ed2cc05`;
- sentinel R3 `36e7a99697d69d039c76893522e3a1e1ab8fb170ad42a843729f42d45678c43e`;
- LLDB supervisor R3 `da7034e4bc079c4e0c581f785bdb94fc2b27da0137350c69024166ef934062be`;
- LLDB observer R3 `f73b4aa52ed999e376d8c6b13cb091cb1b15715488e59f2ea91fbf619e783179`;
- cleanup verifier R3 `ec420d0de8b0c9aa62fc9a1358a9ff52ff4ffa6127c1074e01bafd373e5407ab`;
- network scan R3 `4456f35254a34e3c1e8e0680f0d9f4321f2a578d9cc6b13b3e3f768cd34d1285`.

`repo` means `/Users/ryan/.codex/worktrees/7388/chirality`; `frontend` means
`repo/projects/chirality-app-dev/frontend`. Every row is a distinct numeric
owner gate. Placeholders are substituted only from the named run-owned record.

## External orchestration rows

| ID | Cwd | Complete exact command/control bytes |
|---|---|---|
| C375 | repo | `/usr/bin/shasum -a 256 projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/reviews/A2_ATTEMPT8_V1_17_FRESH_ADVERSARIAL_VERIFIER_RETURN.md projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r3/real-runtime-controller-r3.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r3/real-second-session-sentinel-r3.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r3/lldb-session-supervisor-r3.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r3/lldb-terminal-observer-r3.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r3/real-runtime-cleanup-verifier-r3.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r3/network-attempt-scan-r3.mjs` |
| C376 | repo | `/bin/test ! -e /private/tmp/chirality-dapp92-option-a-20260804` |
| C377 | repo | `/bin/mkdir -p /private/tmp/chirality-dapp92-option-a-20260804/home /private/tmp/chirality-dapp92-option-a-20260804/user /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-runtime /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests /private/tmp/chirality-dapp92-option-a-20260804/protocol` |
| C378 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/electron/cli-launcher.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/cli-launcher.ts` |
| C379 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/electron/main.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/main.ts` |
| C380 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/runtime-control-ipc.ts` |
| C381 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/package.json /private/tmp/chirality-dapp92-option-a-20260804/baseline/package.json` |
| C382 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/scripts/build-electron.mjs /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts/build-electron.mjs` |
| C383 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/cli-launcher.test.ts` |
| C384 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/runtime-control-ipc.test.ts` |
| C385 | repo | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/cli-launcher.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/main.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/runtime-control-ipc.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/package.json projects/chirality-app-dev/frontend/package-lock.json /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts/build-electron.mjs /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/cli-launcher.test.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/runtime-control-ipc.test.ts` |
| C386 | repo | `/bin/test ! -e projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json` |
| C387 | repo | `/bin/test ! -e projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts` |
| C388 | repo | `/bin/test ! -e projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts` |
| C389 | repo | `/bin/test ! -e projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs` |
| C390 | repo | `/bin/test ! -e projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts` |
| C391 | repo | `/usr/bin/touch /private/tmp/chirality-dapp92-option-a-20260804/MUTATION_AUTHORIZED` |
| C392 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron-builder.runtime-helper.json projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json` |
| C393 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/cli-launcher.ts projects/chirality-app-dev/frontend/electron/cli-launcher.ts` |
| C394 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/main.ts projects/chirality-app-dev/frontend/electron/main.ts` |
| C395 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/runtime-control-ipc.ts projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts` |
| C396 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/runtime-helper-entry.ts projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts` |
| C397 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/runtime-helper-path.ts projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts` |
| C398 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/package.json projects/chirality-app-dev/frontend/package.json` |
| C399 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/scripts/build-electron.mjs projects/chirality-app-dev/frontend/scripts/build-electron.mjs` |
| C400 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/scripts/embed-runtime-helper.mjs projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs` |
| C401 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/cli-launcher.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts` |
| C402 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/runtime-control-ipc.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts` |
| C403 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/runtime-helper-packaging.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts` |
| C404 | repo | `/usr/bin/shasum -a 256 projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json projects/chirality-app-dev/frontend/electron/cli-launcher.ts projects/chirality-app-dev/frontend/electron/main.ts projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts projects/chirality-app-dev/frontend/package.json projects/chirality-app-dev/frontend/scripts/build-electron.mjs projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts projects/chirality-app-dev/frontend/package-lock.json` |
| C405 | repo | `/usr/bin/ditto /Users/ryan/dev/chirality/projects/chirality-app-dev/frontend/node_modules projects/chirality-app-dev/frontend/node_modules` |
| C406 | repo | `/bin/rm -rf projects/chirality-app-dev/frontend/node_modules/@chirality/engine-pi-omlx projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-cli projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-client projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-contracts projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-core projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-daemon` |
| C407 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/engine-pi-omlx projects/chirality-app-dev/frontend/node_modules/@chirality/engine-pi-omlx` |
| C408 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/cli projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-cli` |
| C409 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/client projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-client` |
| C410 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/contracts projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-contracts` |
| C411 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/core projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-core` |
| C412 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/daemon projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-daemon` |
| C413 | repo | `/bin/ls -ld projects/chirality-app-dev/frontend/node_modules/@chirality/engine-pi-omlx projects/chirality-app-dev/frontend/node_modules/@chirality/harness-contract projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-cli projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-client projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-contracts projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-core projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-daemon` |
| C414 | frontend | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm test -- src/__tests__/electron/desktop-daemon-posture.test.ts src/__tests__/electron/runtime-control-ipc.test.ts src/__tests__/electron/cli-launcher.test.ts src/__tests__/electron/runtime-helper-packaging.test.ts src/__tests__/electron/desktop-cli-single-daemon-integration.test.ts` |
| C415 | frontend | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run typecheck` |
| C416 | frontend | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run build` |
| C417 | repo | `/bin/mkdir -p /private/tmp/chirality-dapp92-option-a-20260804/electron-dist` |
| C418 | repo | `/bin/cp -p /Users/ryan/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip /private/tmp/chirality-dapp92-option-a-20260804/electron-dist/electron-v43.2.0-darwin-arm64.zip` |
| C419 | repo | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/electron-dist/electron-v43.2.0-darwin-arm64.zip` |
| C420 | frontend | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt5/apply-local-electron-dist-overlay.mjs` |
| C421 | frontend | `/usr/bin/shasum -a 256 electron-builder.runtime-helper.json package.json` |
| C422 | frontend | `/usr/bin/grep -n electronDist electron-builder.runtime-helper.json package.json` |
| C423 | frontend | `/bin/sh -c 'exec /usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run desktop:pack > /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-package.stdout-stderr.txt 2>&1'` |
| C424 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r3/network-attempt-scan-r3.mjs` |
| C425 | repo | `/usr/bin/shasum -a 256 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service' 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Resources/app.asar' 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist' 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality' 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar'` |
| C426 | repo | `/usr/bin/plutil -p 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist'` |
| C427 | repo | `/usr/bin/plutil -p 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Info.plist'` |
| C428 | repo | `/usr/bin/find 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app' -type l -print` |
| C429 | repo | `/usr/bin/find 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app' -type l -exec /usr/bin/readlink '{}' ';'` |
| C430 | repo | `/usr/bin/diff -qr 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app' 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Library/LoginItems/Chirality Runtime Service.app'` |
| C431 | repo, PTY A | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r3/real-runtime-controller-r3.mjs` |
| C432 | repo | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/protocol/controller.json` |
| C433 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r3/real-second-session-sentinel-r3.mjs attach-started <EXACT_HELPER_PID_FROM_C432>` |
| C434 | repo, PTY B | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r3/lldb-session-supervisor-r3.mjs <EXACT_HELPER_PID_FROM_C432>` |
| C196 | supervisor internal C515 | `/usr/bin/xcrun lldb --batch -p <EXACT_HELPER_PID> -s /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt` |
| C435 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r3/real-second-session-sentinel-r3.mjs trace-ready <EXACT_HELPER_PID_FROM_C432>` |
| C436 | PTY A | Poll without input until exact `SIGNAL_ARMED`; absolute bound is controller ready + 128.6 seconds. |
| C437 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r3/real-second-session-sentinel-r3.mjs trace-live <EXACT_HELPER_PID_FROM_C432>` |
| C438 | PTY A | Poll without input until replay-terminal output; absolute bound is controller ready + 139.5 seconds. |
| C197 | PTY B only | Send exact interrupt byte `\u0003`, then exact bytes `process detach\nquit\n`. |
| C439 | PTY B | Poll without input until the C434 supervisor returns terminal; C523 fires at LLDB-child +149.0 seconds and terminal return is required by +149.9 seconds. |
| C440 | repo | Start `/usr/bin/base64 -D -o /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-runtime/session-b-terminal-return.json`; send base64 of one exact machine JSON object with schema `chirality-dapp92-session-terminal-return-r3/v1`, `sessionRole=LLDB_SUPERVISOR`, `terminal=true`, integer tool exit code, and SHA-256 fields for `lldb-terminal.json`, C197 input, stdout, and stderr, derived only after observable C439 terminal return; send EOF. |
| C441 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r3/lldb-terminal-observer-r3.mjs` |
| C442 | repo | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/protocol/lldb-start.json /private/tmp/chirality-dapp92-option-a-20260804/protocol/lldb-terminal.json /private/tmp/chirality-dapp92-option-a-20260804/protocol/detached.json /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-runtime/session-b-terminal-return.json` |
| C443 | PTY A | Poll without input until terminal and exact cleanup status `ALL_CONTROLLER_CHILDREN_REAPED`. |
| C444 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r3/real-runtime-cleanup-verifier-r3.mjs` |
| C445 | repo | Start `/usr/bin/base64 -D -o /private/tmp/chirality-dapp92-option-a-20260804/evidence/session-a-pty.txt`; send base64 of byte-exact C431 PTY output plus terminal-return metadata, then EOF. |
| C446 | repo | Start `/usr/bin/base64 -D -o /private/tmp/chirality-dapp92-option-a-20260804/evidence/session-b-pty.txt`; send base64 of byte-exact C434/C197 PTY input/output plus terminal-return metadata, then EOF. |
| C447 | repo | `/bin/mkdir -p /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r3` |
| C448 | repo | `/bin/mkdir -p /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r3/runtime` |
| C449 | repo | `/usr/bin/ditto /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-runtime /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r3/runtime` |
| C450 | repo | `/bin/mkdir -p /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r3/protocol` |
| C451 | repo | `/usr/bin/ditto /private/tmp/chirality-dapp92-option-a-20260804/protocol /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r3/protocol` |
| C452 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-package.stdout-stderr.txt /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r3/attempt8-package.stdout-stderr.txt` |
| C453 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/evidence/network-scan.matches.txt /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r3/network-scan.matches.txt` |
| C454 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/evidence/network-scan.status.json /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r3/network-scan.status.json` |
| C455 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/evidence/session-a-pty.txt /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r3/session-a-pty.txt` |
| C456 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/evidence/session-b-pty.txt /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r3/session-b-pty.txt` |
| C457 | repo | `/usr/bin/find /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r3 -type f -exec /usr/bin/shasum -a 256 '{}' ';'` |
| C458 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/cli-launcher.ts projects/chirality-app-dev/frontend/electron/cli-launcher.ts` |
| C459 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/main.ts projects/chirality-app-dev/frontend/electron/main.ts` |
| C460 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/runtime-control-ipc.ts projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts` |
| C461 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/package.json projects/chirality-app-dev/frontend/package.json` |
| C462 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts/build-electron.mjs projects/chirality-app-dev/frontend/scripts/build-electron.mjs` |
| C463 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/cli-launcher.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts` |
| C464 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/runtime-control-ipc.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts` |
| C465 | repo | `/bin/rm -f projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts` |
| C466 | repo | `/bin/rm -rf projects/chirality-app-dev/frontend/node_modules projects/chirality-app-dev/frontend/dist projects/chirality-app-dev/frontend/dist-runtime-helper projects/chirality-app-dev/frontend/dist-electron projects/chirality-app-dev/frontend/dist-runtime projects/chirality-app-dev/frontend/.next` |

## Script-internal operation rows

All paths/cwd are exact: controller/sentinel cwd `repo`; LLDB supervisor cwd
`repo`; placeholders are the one recorded owned-child PID for the named row.

| ID | Owner | Complete exact executable/API action |
|---|---|---|
| C467 | controller | `spawn('/usr/bin/env',['-i','PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin','HOME=/private/tmp/chirality-dapp92-option-a-20260804/home','CHIRALITY_USER_DATA=/private/tmp/chirality-dapp92-option-a-20260804/user','CHIRALITY_SKIP_CLI_LAUNCHER=1','/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service','--runtime-daemon'])` for stale helper only. |
| C468 | controller | `spawn('/usr/bin/env',['-i','PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin','HOME=/private/tmp/chirality-dapp92-option-a-20260804/home','CHIRALITY_USER_DATA=/private/tmp/chirality-dapp92-option-a-20260804/user','CHIRALITY_SKIP_CLI_LAUNCHER=1','/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service','--runtime-daemon'])` for final helper only. |
| C469 | controller | `spawn('/usr/bin/env',['-i','PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin','HOME=/private/tmp/chirality-dapp92-option-a-20260804/home','CHIRALITY_USER_DATA=/private/tmp/chirality-dapp92-option-a-20260804/user','CHIRALITY_SKIP_CLI_LAUNCHER=1','/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality','--user-data-dir=/private/tmp/chirality-dapp92-option-a-20260804/user'])`. |
| C470 | controller | `spawn('/usr/bin/env',['-i','PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin','HOME=/private/tmp/chirality-dapp92-option-a-20260804/home','CHIRALITY_USER_DATA=/private/tmp/chirality-dapp92-option-a-20260804/user','ELECTRON_RUN_AS_NODE=1','/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality','/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/runtime-cli/chirality-cli.mjs','project','register','/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/chirality.project.json','--approved-by','D-APP-92','--approval-reference','D-APP-92-OPTION-A','--json'])`, piped stdout/stderr, tracked direct child. |
| C471 | controller | Registration outcome race: exact child exit vs 1 MiB stdout overflow vs 1 MiB stderr overflow vs 10,000 ms timeout vs final-helper exit; no signal in callback. |
| C472 | controller | `staleHelperChildProcess.kill('SIGKILL')` after C490/C491. |
| C473 | controller | `finalHelperChildProcess.kill('SIGTERM')` after C492/C493; first ordinary replay signal. |
| C474 | controller | `registrationChildProcess.kill('SIGKILL')` only if still live in finalizer, after C494/C495. |
| C475 | controller | `guiChildProcess.kill('SIGTERM')` only if still live, after C496/C497. |
| C476 | controller | `guiChildProcess.kill('SIGKILL')` only after C475's 3,000 ms reap bound fails and C498/C499 pass. |
| C477 | controller | `finalHelperChildProcess.kill('SIGKILL')` only in terminal-proofed cleanup if still live, after C500/C501. |
| C478 | controller | `staleHelperChildProcess.kill('SIGKILL')` only if still live, after C502/C503. |
| C479 | controller | Registration child exit observer and result capture; child handle retained through independent final settlement. |
| C480 | controller | Stale success-path exit race against exactly 3,000 ms; timeout enters independent final settlement. |
| C481 | controller | Each registration/stale/GUI/helper settlement independently races its own exit against 3,000 ms and cannot skip later children. |
| C482 | controller stale initial | `/bin/ps -o pid= -o ppid= -o lstart= -o comm= -p <STALE_PID>` |
| C483 | controller stale initial | `/usr/sbin/lsof -a -p <STALE_PID> -d txt -Fn` |
| C484 | controller helper initial | `/bin/ps -o pid= -o ppid= -o lstart= -o comm= -p <HELPER_PID>` |
| C485 | controller helper initial | `/usr/sbin/lsof -a -p <HELPER_PID> -d txt -Fn` |
| C486 | controller GUI initial | `/bin/ps -o pid= -o ppid= -o lstart= -o comm= -p <GUI_PID>` |
| C487 | controller GUI initial | `/usr/sbin/lsof -a -p <GUI_PID> -d txt -Fn` |
| C488 | controller registration initial | `/bin/ps -o pid= -o ppid= -o lstart= -o comm= -p <REGISTRATION_PID>` |
| C489 | controller registration initial | `/usr/sbin/lsof -a -p <REGISTRATION_PID> -d txt -Fn` |
| C490 | before C472 | `/bin/ps -o pid= -o ppid= -o lstart= -o comm= -p <STALE_PID>` |
| C491 | before C472 | `/usr/sbin/lsof -a -p <STALE_PID> -d txt -Fn` |
| C492 | before C473 | `/bin/ps -o pid= -o ppid= -o lstart= -o comm= -p <HELPER_PID>` |
| C493 | before C473 | `/usr/sbin/lsof -a -p <HELPER_PID> -d txt -Fn` |
| C494 | before C474 | `/bin/ps -o pid= -o ppid= -o lstart= -o comm= -p <REGISTRATION_PID>` |
| C495 | before C474 | `/usr/sbin/lsof -a -p <REGISTRATION_PID> -d txt -Fn` |
| C496 | before C475 | `/bin/ps -o pid= -o ppid= -o lstart= -o comm= -p <GUI_PID>` |
| C497 | before C475 | `/usr/sbin/lsof -a -p <GUI_PID> -d txt -Fn` |
| C498 | before C476 | `/bin/ps -o pid= -o ppid= -o lstart= -o comm= -p <GUI_PID>` |
| C499 | before C476 | `/usr/sbin/lsof -a -p <GUI_PID> -d txt -Fn` |
| C500 | before C477 | `/bin/ps -o pid= -o ppid= -o lstart= -o comm= -p <HELPER_PID>` |
| C501 | before C477 | `/usr/sbin/lsof -a -p <HELPER_PID> -d txt -Fn` |
| C502 | before C478 | `/bin/ps -o pid= -o ppid= -o lstart= -o comm= -p <STALE_PID>` |
| C503 | before C478 | `/usr/sbin/lsof -a -p <STALE_PID> -d txt -Fn` |
| C504 | controller snapshot | `/bin/ps -o pid=,ppid=,pgid=,state=,etime= -p <HELPER_PID>,<GUI_PID>` |
| C505 | controller snapshot | `/usr/sbin/lsof -nP -p <HELPER_PID> -a -U` |
| C506 | controller snapshot | `/usr/sbin/lsof -nP -p <HELPER_PID> -a -iTCP` |
| C507 | controller snapshot | `/usr/bin/stat -f %N|%i|%p|%u|%g|%z /private/tmp/chirality-dapp92-option-a-20260804/user/runtime/control.sock /private/tmp/chirality-dapp92-option-a-20260804/user/runtime/control.sock.owner.json` |
| C508 | controller snapshot | `/usr/bin/shasum -a 256 '/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service' '/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Resources/app.asar' '/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist' '/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality' '/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar'` |
| C509 | attach sentinel | `/bin/ps -o pid= -o ppid= -o lstart= -o comm= -p <HELPER_PID>` |
| C510 | attach sentinel | `/usr/sbin/lsof -a -p <HELPER_PID> -d txt -Fn` |
| C511 | trace-ready sentinel | `/bin/ps -o pid= -o ppid= -o lstart= -o comm= -p <HELPER_PID>` |
| C512 | trace-ready sentinel | `/usr/sbin/lsof -a -p <HELPER_PID> -d txt -Fn` |
| C513 | trace-live sentinel | `/bin/ps -o pid= -o ppid= -o lstart= -o comm= -p <HELPER_PID>` |
| C514 | trace-live sentinel | `/usr/sbin/lsof -a -p <HELPER_PID> -d txt -Fn` |
| C515 | supervisor | Node `spawn` C196 with `stdio=['pipe','pipe','pipe']` and `detached=true`, creating a separate LLDB process group so PTY ETX reaches supervisor only. |
| C516 | supervisor initial | `/bin/ps -o pid= -o ppid= -o lstart= -o comm= -p <LLDB_PID>` |
| C517 | supervisor initial | `/usr/sbin/lsof -a -p <LLDB_PID> -d txt -Fn` |
| C518 | before C520 | `/bin/ps -o pid= -o ppid= -o lstart= -o comm= -p <LLDB_PID>` |
| C519 | before C520 | `/usr/sbin/lsof -a -p <LLDB_PID> -d txt -Fn` |
| C520 | supervisor C197 interrupt | On exactly one supervisor `SIGINT` caused by C197 ETX, `lldbChildProcess.kill('SIGINT')`; duplicate interrupt is rejected. |
| C521 | before C523 | `/bin/ps -o pid= -o ppid= -o lstart= -o comm= -p <LLDB_PID>` |
| C522 | before C523 | `/usr/sbin/lsof -a -p <LLDB_PID> -d txt -Fn` |
| C523 | supervisor watchdog | At LLDB-child +149,000 ms only if still live, `lldbChildProcess.kill('SIGKILL')`; require exit event by +149,900 ms. This is new debugger-process termination authority. |
| C524 | network scan script | `/usr/bin/grep -E -i 'https?://|download|fetch|network|ECONN|ENET|EAI_AGAIN|registry|proxy|TLS' /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-package.stdout-stderr.txt`; require status 1 and zero stdout. |

## Remaining rollback rows and branch law

| ID | Cwd | Complete exact command |
|---|---|---|
| C525 | repo | `/usr/bin/shasum -a 256 projects/chirality-app-dev/frontend/electron/cli-launcher.ts projects/chirality-app-dev/frontend/electron/main.ts projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts projects/chirality-app-dev/frontend/package.json projects/chirality-app-dev/frontend/package-lock.json projects/chirality-app-dev/frontend/scripts/build-electron.mjs projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts` |
| C526 | repo | `/usr/bin/git status --short --untracked-files=all -- projects/chirality-app-dev/frontend` |
| C527 | repo | `/bin/test ! -e projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json` |
| C528 | repo | `/bin/test ! -e projects/chirality-app-dev/frontend/node_modules` |
| C529 | repo | `/bin/rm -rf /private/tmp/chirality-dapp92-option-a-20260804` |
| C530 | repo | `/bin/test ! -e /private/tmp/chirality-dapp92-option-a-20260804` |

If C377-C390 stops, only C529-C530 run: product mutation has not begun. Any
C391-or-later stop runs C458-C466 and C525-C530. Any C431-or-later stop also
requires C439-C457 before rollback; cleanup cannot start until C441 creates
the machine-bound `detached.json`. Credential/token bytes and raw registration
stdout are never retained. No environment/memory dump or process census is
authorized. C196/C197 exact bytes remain separately previously approved; all
new watchdog, transcript, proof, internal spawn, identity, and signal actions
are separately owner-gated here.
