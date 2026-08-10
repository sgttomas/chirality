# Proposed command-register amendment v1.19 — Attempt-8 R4

Status: `PROPOSED — MANAGER FREEZE, FRESH VERIFIER, AND OWNER APPROVAL REQUIRED — NOT EXECUTED`

This standalone replacement answers verifier return
`b2fce5f287c06fce400d60588fee70d4d40d6dbbfab87aa46f52be591f45fe70`.
V1.16-v1.18 and `proposed/attempt8-r3/**` remain byte-preserved rejected
history. No R4 script or runtime command has been invoked. The manager, not
the author, will independently hash and freeze the final proposal bytes.

`repo` is `/Users/ryan/.codex/worktrees/7388/chirality`; `frontend` is
`repo/projects/chirality-app-dev/frontend`; `root` is
`/private/tmp/chirality-dapp92-option-a-20260804`. C531-C786 are one unique,
contiguous R4 owner-gated range. C196 and C197 retain their separate prior
approval and exact v1.9 bytes.

## External commands and controls

Every row is one command, one existing-session poll/control, or one exact
script invocation. A nonzero result stops forward execution and enters the
branch and rollback law below.

| ID | Cwd | Exact command/control |
|---|---|---|
| C531 | repo | `/usr/bin/shasum -a 256 projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/reviews/A2_ATTEMPT8_V1_18_FRESH_ADVERSARIAL_VERIFIER_RETURN.md projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/real-runtime-controller-r4.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/real-second-session-sentinel-r4.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/lldb-session-supervisor-r4.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/session-terminal-receipt-r4.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/session-terminal-proof-r4.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/transcript-capture-r4.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/real-runtime-cleanup-verifier-r4.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/network-attempt-scan-r4.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/evidence-manifest-r4.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/rollback-verifier-r4.mjs` — require exactly these ordered SHA-256 values: `b2fce5f287c06fce400d60588fee70d4d40d6dbbfab87aa46f52be591f45fe70`, `856a2fc990cac99f9aacfee2c6393e637d16a2d165707178000e5de7db9c1786`, `1007d9f29cb50b2d1b26f854ab94ecbd92f019a14c9b1000311c51d9759f8a33`, `2c3d738831860f2b292e9822933a454e38ec311982ce2394059bf86596a8b611`, `09caaa917046c762fff0f73aa55bf263af3128a4d808bb39b4d338f9abc918b4`, `89bf3f3a884170ffe2b4f09f9808c5ec7da4de7207c946fd593d398bfe6b2ead`, `f739c663095423bd4844c4896ee75526227e9f8192211d287dfc3c19b2448e62`, `fedb6530585e38ceb8aa7d4412a0d32c6712cc5e6971ffe48d18196bbb768628`, `9e2244f29ff597c58b0e9808c62dddaf0cee0701d78d65bdf282f60a1cd74903`, `b190ec40d3511cc23bc17a936c101cbb36f25032662124f30de8c4466e3ff27b`, and `09181ceab9e4c0e180cabc47a12660cae400141229bcba6cc055d28dd6200650`. |
| C532 | repo | `/bin/test ! -e /private/tmp/chirality-dapp92-option-a-20260804` |
| C533 | repo | `/bin/mkdir -p /private/tmp/chirality-dapp92-option-a-20260804/home /private/tmp/chirality-dapp92-option-a-20260804/user /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-runtime /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests /private/tmp/chirality-dapp92-option-a-20260804/protocol` |
| C534 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/electron/cli-launcher.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/cli-launcher.ts` |
| C535 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/electron/main.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/main.ts` |
| C536 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/runtime-control-ipc.ts` |
| C537 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/package.json /private/tmp/chirality-dapp92-option-a-20260804/baseline/package.json` |
| C538 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/scripts/build-electron.mjs /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts/build-electron.mjs` |
| C539 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/cli-launcher.test.ts` |
| C540 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/runtime-control-ipc.test.ts` |
| C541 | repo | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/cli-launcher.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/main.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/runtime-control-ipc.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/package.json projects/chirality-app-dev/frontend/package-lock.json /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts/build-electron.mjs /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/cli-launcher.test.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/runtime-control-ipc.test.ts` — require, in order, the exact eight hashes in “Rollback constants”. |
| C542 | repo | `/bin/test ! -e projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json` |
| C543 | repo | `/bin/test ! -e projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts` |
| C544 | repo | `/bin/test ! -e projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts` |
| C545 | repo | `/bin/test ! -e projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs` |
| C546 | repo | `/bin/test ! -e projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts` |
| C547 | repo | `/usr/bin/touch /private/tmp/chirality-dapp92-option-a-20260804/MUTATION_AUTHORIZED` |
| C548 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron-builder.runtime-helper.json projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json` |
| C549 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/cli-launcher.ts projects/chirality-app-dev/frontend/electron/cli-launcher.ts` |
| C550 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/main.ts projects/chirality-app-dev/frontend/electron/main.ts` |
| C551 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/runtime-control-ipc.ts projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts` |
| C552 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/runtime-helper-entry.ts projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts` |
| C553 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/runtime-helper-path.ts projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts` |
| C554 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/package.json projects/chirality-app-dev/frontend/package.json` |
| C555 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/scripts/build-electron.mjs projects/chirality-app-dev/frontend/scripts/build-electron.mjs` |
| C556 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/scripts/embed-runtime-helper.mjs projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs` |
| C557 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/cli-launcher.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts` |
| C558 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/runtime-control-ipc.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts` |
| C559 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/runtime-helper-packaging.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts` |
| C560 | repo | `/usr/bin/shasum -a 256 projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json projects/chirality-app-dev/frontend/electron/cli-launcher.ts projects/chirality-app-dev/frontend/electron/main.ts projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts projects/chirality-app-dev/frontend/package.json projects/chirality-app-dev/frontend/scripts/build-electron.mjs projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts projects/chirality-app-dev/frontend/package-lock.json` |
| C561 | repo | `/usr/bin/ditto /Users/ryan/dev/chirality/projects/chirality-app-dev/frontend/node_modules projects/chirality-app-dev/frontend/node_modules` |
| C562 | repo | `/bin/rm -rf projects/chirality-app-dev/frontend/node_modules/@chirality/engine-pi-omlx projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-cli projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-client projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-contracts projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-core projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-daemon` |
| C563 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/engine-pi-omlx projects/chirality-app-dev/frontend/node_modules/@chirality/engine-pi-omlx` |
| C564 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/cli projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-cli` |
| C565 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/client projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-client` |
| C566 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/contracts projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-contracts` |
| C567 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/core projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-core` |
| C568 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/daemon projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-daemon` |
| C569 | repo | `/bin/ls -ld projects/chirality-app-dev/frontend/node_modules/@chirality/engine-pi-omlx projects/chirality-app-dev/frontend/node_modules/@chirality/harness-contract projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-cli projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-client projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-contracts projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-core projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-daemon` |
| C570 | frontend | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm test -- src/__tests__/electron/desktop-daemon-posture.test.ts src/__tests__/electron/runtime-control-ipc.test.ts src/__tests__/electron/cli-launcher.test.ts src/__tests__/electron/runtime-helper-packaging.test.ts src/__tests__/electron/desktop-cli-single-daemon-integration.test.ts` |
| C571 | frontend | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run typecheck` |
| C572 | frontend | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run build` |
| C573 | repo | `/bin/mkdir -p /private/tmp/chirality-dapp92-option-a-20260804/electron-dist` |
| C574 | repo | `/bin/cp -p /Users/ryan/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip /private/tmp/chirality-dapp92-option-a-20260804/electron-dist/electron-v43.2.0-darwin-arm64.zip` |
| C575 | repo | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/electron-dist/electron-v43.2.0-darwin-arm64.zip` |
| C576 | frontend | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt5/apply-local-electron-dist-overlay.mjs` |
| C577 | frontend | `/usr/bin/shasum -a 256 electron-builder.runtime-helper.json package.json` |
| C578 | frontend | `/usr/bin/grep -n electronDist electron-builder.runtime-helper.json package.json` |
| C579 | frontend | `/bin/sh -c 'exec /usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run desktop:pack > /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-package.stdout-stderr.txt 2>&1'` |
| C580 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/network-attempt-scan-r4.mjs` |
| C581 | repo | `/usr/bin/shasum -a 256 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service' 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Resources/app.asar' 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist' 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality' 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar'` |
| C582 | repo | `/usr/bin/plutil -p 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist'` |
| C583 | repo | `/usr/bin/plutil -p 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Info.plist'` |
| C584 | repo | `/usr/bin/find 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app' -type l -print` |
| C585 | repo | `/usr/bin/find 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app' -type l -exec /usr/bin/readlink '{}' ';'` |
| C586 | repo | `/usr/bin/diff -qr 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app' 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Library/LoginItems/Chirality Runtime Service.app'` |
| C587 | repo, session A | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/real-runtime-controller-r4.mjs` |
| C588 | repo | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/protocol/controller.json` |
| C589 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/real-second-session-sentinel-r4.mjs attach-intent <EXACT_HELPER_PID_FROM_C588>` |
| C590 | repo, session B | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/lldb-session-supervisor-r4.mjs <EXACT_HELPER_PID_FROM_C588>` |
| C196 | supervisor C726 | `/usr/bin/xcrun lldb --batch -p <EXACT_HELPER_PID> -s /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt` |
| C591 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/real-second-session-sentinel-r4.mjs trace-ready <EXACT_HELPER_PID_FROM_C588>` |
| C592 | session A | Poll with zero input until exact `SIGNAL_ARMED`, bounded by controller ready +128.6 seconds. |
| C593 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/real-second-session-sentinel-r4.mjs trace-live <EXACT_HELPER_PID_FROM_C588>` |
| C594 | session A | Poll with zero input until replay-terminal output, bounded by controller ready +139.5 seconds. |
| C197 | session B only | Send exactly one ETX (one supervisor `SIGINT`), then buffer exact bytes `process detach\nquit\n`, then EOF. No byte is forwarded to LLDB until EOF and whole-buffer equality pass. |
| C595 | session B | Poll with zero additional input for supervisor terminal; hard bound is LLDB spawn origin +149.9 seconds. |
| C596 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/session-terminal-receipt-r4.mjs PRE_CONTROLLER_NO_SESSION_B NONE` |
| C597 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/session-terminal-receipt-r4.mjs CONTROLLER_NO_LLDB_SPAWN NONE` |
| C598 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/session-terminal-receipt-r4.mjs LLDB_TERMINAL_BEFORE_ATTACH <EXACT_C590_EXIT>` |
| C599 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/session-terminal-receipt-r4.mjs NORMAL_EXACT_DETACH <EXACT_C590_EXIT>` |
| C600 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/session-terminal-receipt-r4.mjs FORCED_WATCHDOG_TERMINAL <EXACT_C590_EXIT>` |
| C601 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/session-terminal-proof-r4.mjs` |
| C602 | session A | Poll with zero input until controller terminal; bound is cleanup permission +24 seconds. |
| C603 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/real-runtime-cleanup-verifier-r4.mjs` |
| C604 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/transcript-capture-r4.mjs A PRE_CONTROLLER_NO_SESSION_B` |
| C605 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/transcript-capture-r4.mjs A CONTROLLER_NO_LLDB_SPAWN` |
| C606 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/transcript-capture-r4.mjs A LLDB_TERMINAL_BEFORE_ATTACH` |
| C607 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/transcript-capture-r4.mjs A NORMAL_EXACT_DETACH` |
| C608 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/transcript-capture-r4.mjs A FORCED_WATCHDOG_TERMINAL` |
| C609 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/transcript-capture-r4.mjs B PRE_CONTROLLER_NO_SESSION_B` |
| C610 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/transcript-capture-r4.mjs B CONTROLLER_NO_LLDB_SPAWN` |
| C611 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/transcript-capture-r4.mjs B LLDB_TERMINAL_BEFORE_ATTACH` |
| C612 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/transcript-capture-r4.mjs B NORMAL_EXACT_DETACH` |
| C613 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/transcript-capture-r4.mjs B FORCED_WATCHDOG_TERMINAL` |
| C614 | repo | `/bin/mkdir -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r4` |
| C615 | repo | `/bin/mkdir -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r4/runtime` |
| C616 | repo | `/usr/bin/ditto /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-runtime projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r4/runtime` |
| C617 | repo | `/bin/mkdir -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r4/protocol` |
| C618 | repo | `/usr/bin/ditto /private/tmp/chirality-dapp92-option-a-20260804/protocol projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r4/protocol` |
| C619 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-package.stdout-stderr.txt projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r4/attempt8-package.stdout-stderr.txt` |
| C620 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/evidence/network-scan.matches.txt projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r4/network-scan.matches.txt` |
| C621 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/evidence/network-scan.status.json projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r4/network-scan.status.json` |
| C622 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/evidence-manifest-r4.mjs` |
| C623 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/cli-launcher.ts projects/chirality-app-dev/frontend/electron/cli-launcher.ts` |
| C624 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/main.ts projects/chirality-app-dev/frontend/electron/main.ts` |
| C625 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/runtime-control-ipc.ts projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts` |
| C626 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/package.json projects/chirality-app-dev/frontend/package.json` |
| C627 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts/build-electron.mjs projects/chirality-app-dev/frontend/scripts/build-electron.mjs` |
| C628 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/cli-launcher.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts` |
| C629 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/runtime-control-ipc.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts` |
| C630 | repo | `/bin/rm -f projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts` |
| C631 | repo | `/bin/rm -rf projects/chirality-app-dev/frontend/node_modules projects/chirality-app-dev/frontend/dist projects/chirality-app-dev/frontend/dist-runtime-helper projects/chirality-app-dev/frontend/dist-electron projects/chirality-app-dev/frontend/dist-runtime projects/chirality-app-dev/frontend/.next` |
| C632 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r4/rollback-verifier-r4.mjs` |
| C633 | repo | `/bin/test -f /private/tmp/chirality-dapp92-option-a-20260804/TEMP_DELETE_ALLOWED` |
| C634 | repo | `/bin/rm -rf /private/tmp/chirality-dapp92-option-a-20260804` |
| C635 | repo | `/bin/test ! -e /private/tmp/chirality-dapp92-option-a-20260804` |
| C636 | repo | `/bin/test -f projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r4/EVIDENCE_MANIFEST.sha256` |

Rows C604-C613 are mutually exclusive branch-specific exact invocations. No
row permits a loop, another value, or free-form text.

## Script-internal actions

| ID | Exact independently gated operation |
|---|---|
| C637 | Create fixed evidence/protocol files and raw controller descriptors. |
| C638 | Spawn exact stale-helper `/usr/bin/env` child. |
| C639 | Install stale-helper error/exit settlement observer. |
| C640 | Install stale-helper 170,000 ms owned-handle watchdog. |
| C641 | Stale-helper 40 ms spawn-grace wait. |
| C642 | Stale-helper exact-PID `/bin/ps` identity probe. |
| C643 | Stale-helper exact-PID `/usr/sbin/lsof -d txt` probe. |
| C644 | Stale-helper bounded 80×100 ms readiness wait. |
| C645 | Pre-signal stale-helper exact-PID `/bin/ps` probe. |
| C646 | Pre-signal stale-helper exact-PID `/usr/sbin/lsof` probe. |
| C647 | Owned stale-helper `SIGKILL`. |
| C648 | Stale-helper 3,000 ms terminal wait. |
| C649 | Spawn exact final-helper `/usr/bin/env` child. |
| C650 | Install final-helper error/exit observer. |
| C651 | Install final-helper 170,000 ms owned-handle watchdog. |
| C652 | Final-helper 40 ms spawn-grace wait. |
| C653 | Final-helper initial exact-PID `/bin/ps` probe. |
| C654 | Final-helper initial exact-PID `/usr/sbin/lsof` probe. |
| C655 | Final-helper bounded 80×100 ms readiness wait. |
| C656 | Atomic controller-record write. |
| C657 | Bounded trace-ready wait, 50 ms polls through ready+28,000 ms. |
| C658 | Spawn exact tracked registration child. |
| C659 | Install registration error/exit observer. |
| C660 | Install registration 170,000 ms owned-handle watchdog. |
| C661 | Registration 40 ms spawn-grace wait. |
| C662 | Registration exact-PID `/bin/ps` probe. |
| C663 | Registration exact-PID `/usr/sbin/lsof` probe. |
| C664 | Registration stdout 1 MiB overflow monitor. |
| C665 | Registration stderr 1 MiB overflow monitor. |
| C666 | Registration 10,000 ms timeout arm. |
| C667 | Final-helper terminal-during-registration arm. |
| C668 | Registration race resolution over C659/C664-C667. |
| C669 | Bounded GUI-launch timer. |
| C670 | Spawn exact GUI `/usr/bin/env` child. |
| C671 | Install GUI error/exit observer. |
| C672 | Install GUI 170,000 ms owned-handle watchdog. |
| C673 | GUI 40 ms spawn-grace wait. |
| C674 | GUI initial exact-PID `/bin/ps` probe. |
| C675 | GUI initial exact-PID `/usr/sbin/lsof` probe. |
| C676 | Bounded 5×100 ms authenticated-contact wait. |
| C677 | Exact helper/GUI `/bin/ps` snapshot. |
| C678 | Exact helper Unix `/usr/sbin/lsof` snapshot. |
| C679 | Exact helper TCP `/usr/sbin/lsof` snapshot. |
| C680 | `/usr/bin/stat` of the two exact control paths. |
| C681 | `/usr/bin/shasum` of the five exact package files. |
| C682 | Bounded signal-arm timer. |
| C683 | Bounded trace-live wait. |
| C684 | Bounded first-signal timer. |
| C685 | Immediate pre-SIGTERM helper `/bin/ps` probe. |
| C686 | Immediate pre-SIGTERM helper `/usr/sbin/lsof` probe. |
| C687 | First ordinary owned-helper `SIGTERM`. |
| C688 | Bounded 80×100 ms helper-terminal poll. |
| C689 | Bounded 3,040×50 ms cleanup-permission wait. |
| C690 | Registration cleanup `/bin/ps` probe. |
| C691 | Registration cleanup `/usr/sbin/lsof` probe. |
| C692 | Owned registration `SIGKILL`. |
| C693 | Registration 3,000 ms terminal wait. |
| C694 | Registration direct-child-handle fail-safe `SIGKILL`. |
| C695 | Registration fail-safe 3,000 ms terminal wait. |
| C696 | Stale cleanup `/bin/ps` probe. |
| C697 | Stale cleanup `/usr/sbin/lsof` probe. |
| C698 | Owned stale cleanup `SIGKILL`. |
| C699 | Stale cleanup 3,000 ms terminal wait. |
| C700 | Stale direct-child-handle fail-safe `SIGKILL`. |
| C701 | Stale fail-safe 3,000 ms terminal wait. |
| C702 | GUI cleanup pre-TERM `/bin/ps` probe. |
| C703 | GUI cleanup pre-TERM `/usr/sbin/lsof` probe. |
| C704 | Owned GUI `SIGTERM`. |
| C705 | GUI graceful 3,000 ms terminal wait. |
| C706 | GUI cleanup pre-KILL `/bin/ps` probe. |
| C707 | GUI cleanup pre-KILL `/usr/sbin/lsof` probe. |
| C708 | Owned GUI `SIGKILL` or same-handle fail-safe after probe failure. |
| C709 | GUI forced 3,000 ms terminal wait. |
| C710 | Independent registration settlement completion. |
| C711 | Independent stale settlement completion. |
| C712 | Independent GUI settlement completion. |
| C713 | Helper cleanup `/bin/ps` probe. |
| C714 | Helper cleanup `/usr/sbin/lsof` probe. |
| C715 | Owned helper cleanup `SIGKILL`. |
| C716 | Helper cleanup 3,000 ms terminal wait. |
| C717 | Helper direct-child-handle fail-safe `SIGKILL`. |
| C718 | Helper fail-safe 3,000 ms terminal wait. |
| C719 | Independent helper settlement completion. |
| C720 | Attach-intent helper `/bin/ps` probe. |
| C721 | Attach-intent helper `/usr/sbin/lsof` probe and typed write. |
| C722 | Trace-ready helper `/bin/ps` probe. |
| C723 | Trace-ready helper `/usr/sbin/lsof` probe and typed write. |
| C724 | Trace-live helper `/bin/ps` probe. |
| C725 | Trace-live helper `/usr/sbin/lsof` probe and typed write. |
| C726 | Spawn exact C196 with piped streams and separate process group; capture spawn origin immediately before. |
| C727 | Assign LLDB handle to outer registry and install error/exit observers immediately. |
| C728 | Install absolute spawn-origin+149,000 ms watchdog before any write/probe. |
| C729 | Validate stored owned LLDB handle/PID. |
| C730 | Initial exact LLDB `/bin/ps` probe. |
| C731 | Initial exact LLDB `/usr/sbin/lsof` probe. |
| C732 | Pre-C197 LLDB `/bin/ps` probe. |
| C733 | Pre-C197 LLDB `/usr/sbin/lsof` probe. |
| C734 | Exactly one owned LLDB-child `SIGINT`; reject duplicates. |
| C735 | Watchdog LLDB `/bin/ps` probe. |
| C736 | Watchdog LLDB `/usr/sbin/lsof` probe. |
| C737 | Identity-guarded owned LLDB `SIGKILL` at spawn+149,000 ms. |
| C738 | Owner-gated direct-child-handle-only LLDB `SIGKILL` fail-safe after probe/setup failure. |
| C739 | LLDB 40 ms start-observation wait. |
| C740 | Atomic LLDB spawn-attempt receipt. |
| C741 | Atomic mechanically observed LLDB-start receipt. |
| C742 | C197 prefix/length/EOF input validation; close/reject invalid bytes. |
| C743 | One exact whole-buffer write of `process detach\nquit\n`. |
| C744 | LLDB terminal wait. |
| C745 | Remaining absolute terminal wait through spawn+149,900 ms. |
| C746 | LLDB terminal receipt write with all session/PID/hash/exit/error/detach fields. |
| C747 | Parse one typed terminal branch and numeric-or-NONE exit. |
| C748 | Evaluate controller/intent/spawn/start/terminal presence matrix. |
| C749 | Read exact LLDB terminal receipt when present. |
| C750 | Read/hash exact LLDB spawn-attempt receipt when present. |
| C751 | Read/hash exact LLDB-start receipt only when present. |
| C752 | Hash exact C197 input/stdout/stderr files. |
| C753 | Bind exact supervisor/session/LLDB/target/exit fields. |
| C754 | Exclusive typed session-terminal receipt write. |
| C755 | Read/hash typed session-terminal receipt. |
| C756 | Bind exact controller PID/target. |
| C757 | Bind exact spawn-attempt session and hash. |
| C758 | Bind exact optional LLDB-start session and hash. |
| C759 | Recompute exact input/stdout/stderr hashes. |
| C760 | Evaluate exact target detach, honest early terminal, or honest forced terminal. |
| C761 | Exclusive session-terminal proof write. |
| C762 | Cleanup-permission write only after C755-C761 pass. |
| C763 | Parse typed transcript session/branch. |
| C764 | Exact session-A stdout copy. |
| C765 | Exact session-A stderr copy. |
| C766 | Exact session-B C197 input copy when session exists. |
| C767 | Exact session-B LLDB stdout copy when session exists. |
| C768 | Exact session-B LLDB stderr copy when session exists. |
| C769 | Typed no-session-B absence receipt for the two no-session branches only. |
| C770 | Exact transcript hash/length manifest write. |
| C771 | Read and schema-check controller cleanup receipt. |
| C772 | Check registration/stale/GUI/helper terminal states independently. |
| C773 | Bind exact branch proof and cleanup permission. |
| C774 | Exclusive cleanup-verifier receipt write. |
| C775 | Exact `/usr/bin/grep` network-attempt scan plus status/match writes. |
| C776 | Recursively read only the fixed durable evidence root. |
| C777 | Byte-sort exact relative evidence paths. |
| C778 | Hash each sorted evidence file and exclusively write `EVIDENCE_MANIFEST.sha256`. |
| C779 | Byte-equal manifest readback assertion. |
| C780 | Compare all eight literal final frontend path/hash pairs. |
| C781 | Spawn exact frontend-scoped `/usr/bin/git status --short --untracked-files=all`. |
| C782 | Assert Git command success and exactly empty stdout. |
| C783 | Assert five candidate additions absent. |
| C784 | Assert six build/dependency derivative roots absent. |
| C785 | Exclusively write `TEMP_DELETE_ALLOWED`. |
| C786 | Require permission marker readback before external C633-C634. |

## Mutually exclusive branch law

Exactly one branch is selected from observed artifacts; no branch requires a
file from a session that did not exist.

| Branch | Required | Forbidden | Exact path to evidence/rollback |
|---|---|---|---|
| `PRE_CONTROLLER_NO_SESSION_B` | replay terminal and controller cleanup record; no controller record | controller, attach-intent, LLDB spawn/start/terminal | C596, C601-C604, C609, C614-C636 |
| `CONTROLLER_NO_LLDB_SPAWN` | controller record; optionally attach-intent; no spawn attempt | LLDB spawn/start/terminal | C597, C601-C603, C605, C610, C614-C636 |
| `LLDB_TERMINAL_BEFORE_ATTACH` | controller, attach-intent, spawn-attempt, terminal | lldb-start | C598, C601-C603, C606, C611, C614-C636 |
| `NORMAL_EXACT_DETACH` | all same-session start/terminal bindings, exact one ETX, exact buffered detach/quit input, exit 0, exact `Process <TARGET_PID> detached` | watchdog/fail-safe terminal | C599, C601-C603, C607, C612, C614-C636 |
| `FORCED_WATCHDOG_TERMINAL` | all same-session start/terminal bindings and exact C737 or C738 forced terminal | normal-detach claim | C600, C601-C603, C608, C613, C614-C636 |

C601 alone may create cleanup permission, and only after the applicable row's
complete binding passes. Each controller child is outer-registered immediately
after spawn; exit/error listeners and an absolute settlement watchdog are
installed before a file write, wait, PID validation, identity probe, or other
throwing operation. Registration, stale helper, GUI, and helper settlement
continue independently after failures. Every spawned child has a bounded
direct-handle terminal fail-safe; a failed settlement retains the root and is
reported, never silently declared clean.

LLDB's deadline begins at the instant immediately before C726. C727-C728 are
installed before C740 or any identity operation. C737 runs at +149,000 ms;
C738 is the separately enumerated owner-gated escape hatch when the watchdog
identity probe itself fails; C745 requires observed LLDB terminality no later
than +149,900 ms. There is no path that intentionally leaves the owned LLDB
child live. Arbitrary, partial, overlong, non-prefix, duplicate, or post-EOF
stdin is rejected/closed without forwarding. Only one EOF-complete byte-equal
C197 buffer is forwarded once.

## Durable evidence and rollback law

C614-C622 finish before any rollback or fixed-root deletion. They retain the
actual branch receipt, raw controller streams, exact C197 input, LLDB raw
stdout/stderr if session B existed, typed session-B absence if it did not,
spawn/start/terminal/session proof, package transcript, network-scan result,
action/deviation logs, cleanup receipts, and a deterministically sorted durable
hash manifest. Credential/token bytes and raw registration stdout are never
retained.

C623-C631 are attempted independently in order even if a prior rollback step
fails. C632 then compares the exact final eight hashes, requires an exactly
empty frontend status, and requires all named candidate/build/dependency
derivatives absent. Only C632 may create `TEMP_DELETE_ALLOWED`; C633 must see
it before C634. If any restore or validation fails, C634-C635 are forbidden:
the baseline and fixed root remain for diagnosis and the failure is reported.
C636 proves the durable manifest exists after deletion.

Rollback constants, in C541/C780 order:

1. `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b`
2. `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f`
3. `5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a`
4. `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53`
5. `5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56`
6. `a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558`
7. `1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9`
8. `f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6`

No network, credential value, environment/memory dump, broad process census,
cache seed, unowned/static-PID signal, other debugger, product remedy,
acceptance, release, reliance, Git mutation, Task Management, or foreign-loop
authority is present.
