# Proposed command-register amendment v1.20 — Attempt-8 R5

Status: `PROPOSED — MANAGER FREEZE, FRESH VERIFIER, AND OWNER APPROVAL REQUIRED — NOT EXECUTED`

This standalone replacement answers the v1.19 verifier return at the required
accepted identity
`2c8f8a1db7e207783a556c4a2e5d5f6f676cb32f63ade9cc4b384f2dc7302e8b`.
V1.16-v1.19 and `proposed/attempt8-r3/**` / `proposed/attempt8-r4/**` remain byte-preserved rejected
history. No R5 script or runtime command has been invoked. The manager, not
the author, will independently hash and freeze the final proposal bytes.

`repo` is `/Users/ryan/.codex/worktrees/7388/chirality`; `frontend` is
`repo/projects/chirality-app-dev/frontend`; `root` is
`/private/tmp/chirality-dapp92-option-a-20260804`. C787-C1057 are one unique,
contiguous R5 owner-gated range. Historical C196/C197 remain unused context
only. C847 and C852 are redesigned operations presented solely as new owner
authority and claim no inheritance from C196/C197.

The live R5 proposal contains ten `.mjs` files plus `README.md`, not eleven
`.mjs` files. The stale count in the immutable R7 handoff/validation is
historical and is not repeated as current fact here.

## External commands and controls

Every row is one command, one existing-session poll/control, or one exact
script invocation. A nonzero result stops forward execution and enters the
branch and rollback law below.

| ID | Cwd | Exact command/control |
|---|---|---|
| C787 | repo | `/usr/bin/shasum -a 256 projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/reviews/A2_ATTEMPT8_V1_19_FRESH_ADVERSARIAL_VERIFIER_RETURN.md projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/real-runtime-controller-r5.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/real-second-session-sentinel-r5.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/lldb-session-supervisor-r5.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/session-terminal-receipt-r5.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/session-terminal-proof-r5.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/transcript-capture-r5.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/real-runtime-cleanup-verifier-r5.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/network-attempt-scan-r5.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/evidence-manifest-r5.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/rollback-verifier-r5.mjs` — require exactly these ordered SHA-256 values: `2c8f8a1db7e207783a556c4a2e5d5f6f676cb32f63ade9cc4b384f2dc7302e8b`, `7ddac5f585e00b12a9806db73351654234776e5324d1d2bdbbaecbe5a82da945`, `e42616c3a3015e9c25b4b717ab90b669a38ed055f0809207bc61997e7c44868e`, `49ee82b38e3a29b64c81d24b795c6b5fd462db2de936fa15f82e865705e32b90`, `73ed3a89b6304107462d9e6f04ea8f6252def2b387829dec3ce5d20fa922ca1b`, `711c90244444508cfb08db6e05d76371c8ed424fc1f8ed0bc5652722d12e75c9`, `7d36bdf05ef607bf3feca49e3242529dcd7b9d6b0d58a8ac27878619c7c6eaa1`, `e42d04822c5c94e220482928d6496e890ea7a91dbc9a7e6217c77b3845b39714`, `1c24cfc932a8410ce7938d5274585e26174e265bea0f29650905abaa370571e4`, `7f9939d4eeaac0796900ac4f6ccd4d234820949c47e7c7c131c39ea795984dae`, and `5938e1afcf12ceddf5bddf73efe1bf4e44abe909d5178635e600f1062c97d53c`. |
| C788 | repo | `/bin/test ! -e /private/tmp/chirality-dapp92-option-a-20260804` |
| C789 | repo | `/bin/mkdir -p /private/tmp/chirality-dapp92-option-a-20260804/home /private/tmp/chirality-dapp92-option-a-20260804/user /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-runtime /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests /private/tmp/chirality-dapp92-option-a-20260804/protocol` |
| C790 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/electron/cli-launcher.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/cli-launcher.ts` |
| C791 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/electron/main.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/main.ts` |
| C792 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/runtime-control-ipc.ts` |
| C793 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/package.json /private/tmp/chirality-dapp92-option-a-20260804/baseline/package.json` |
| C794 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/scripts/build-electron.mjs /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts/build-electron.mjs` |
| C795 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/cli-launcher.test.ts` |
| C796 | repo | `/bin/cp -p projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/runtime-control-ipc.test.ts` |
| C797 | repo | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/cli-launcher.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/main.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/runtime-control-ipc.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/package.json projects/chirality-app-dev/frontend/package-lock.json /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts/build-electron.mjs /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/cli-launcher.test.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/runtime-control-ipc.test.ts` — require, in order, the exact eight hashes in “Rollback constants”. |
| C798 | repo | `/bin/test ! -e projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json` |
| C799 | repo | `/bin/test ! -e projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts` |
| C800 | repo | `/bin/test ! -e projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts` |
| C801 | repo | `/bin/test ! -e projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs` |
| C802 | repo | `/bin/test ! -e projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts` |
| C803 | repo | `/usr/bin/touch /private/tmp/chirality-dapp92-option-a-20260804/MUTATION_AUTHORIZED` |
| C804 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron-builder.runtime-helper.json projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json` |
| C805 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/cli-launcher.ts projects/chirality-app-dev/frontend/electron/cli-launcher.ts` |
| C806 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/main.ts projects/chirality-app-dev/frontend/electron/main.ts` |
| C807 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/runtime-control-ipc.ts projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts` |
| C808 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/runtime-helper-entry.ts projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts` |
| C809 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/runtime-helper-path.ts projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts` |
| C810 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/package.json projects/chirality-app-dev/frontend/package.json` |
| C811 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/scripts/build-electron.mjs projects/chirality-app-dev/frontend/scripts/build-electron.mjs` |
| C812 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/scripts/embed-runtime-helper.mjs projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs` |
| C813 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/cli-launcher.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts` |
| C814 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/runtime-control-ipc.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts` |
| C815 | repo | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/runtime-helper-packaging.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts` |
| C816 | repo | `/usr/bin/shasum -a 256 projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json projects/chirality-app-dev/frontend/electron/cli-launcher.ts projects/chirality-app-dev/frontend/electron/main.ts projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts projects/chirality-app-dev/frontend/package.json projects/chirality-app-dev/frontend/scripts/build-electron.mjs projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts projects/chirality-app-dev/frontend/package-lock.json` |
| C817 | repo | `/usr/bin/ditto /Users/ryan/dev/chirality/projects/chirality-app-dev/frontend/node_modules projects/chirality-app-dev/frontend/node_modules` |
| C818 | repo | `/bin/rm -rf projects/chirality-app-dev/frontend/node_modules/@chirality/engine-pi-omlx projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-cli projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-client projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-contracts projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-core projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-daemon` |
| C819 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/engine-pi-omlx projects/chirality-app-dev/frontend/node_modules/@chirality/engine-pi-omlx` |
| C820 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/cli projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-cli` |
| C821 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/client projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-client` |
| C822 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/contracts projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-contracts` |
| C823 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/core projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-core` |
| C824 | repo | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/daemon projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-daemon` |
| C825 | repo | `/bin/ls -ld projects/chirality-app-dev/frontend/node_modules/@chirality/engine-pi-omlx projects/chirality-app-dev/frontend/node_modules/@chirality/harness-contract projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-cli projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-client projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-contracts projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-core projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-daemon` |
| C826 | frontend | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm test -- src/__tests__/electron/desktop-daemon-posture.test.ts src/__tests__/electron/runtime-control-ipc.test.ts src/__tests__/electron/cli-launcher.test.ts src/__tests__/electron/runtime-helper-packaging.test.ts src/__tests__/electron/desktop-cli-single-daemon-integration.test.ts` |
| C827 | frontend | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run typecheck` |
| C828 | frontend | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run build` |
| C829 | repo | `/bin/mkdir -p /private/tmp/chirality-dapp92-option-a-20260804/electron-dist` |
| C830 | repo | `/bin/cp -p /Users/ryan/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip /private/tmp/chirality-dapp92-option-a-20260804/electron-dist/electron-v43.2.0-darwin-arm64.zip` |
| C831 | repo | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/electron-dist/electron-v43.2.0-darwin-arm64.zip` |
| C832 | frontend | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt5/apply-local-electron-dist-overlay.mjs` |
| C833 | frontend | `/usr/bin/shasum -a 256 electron-builder.runtime-helper.json package.json` |
| C834 | frontend | `/usr/bin/grep -n electronDist electron-builder.runtime-helper.json package.json` |
| C835 | frontend | `/bin/sh -c 'exec /usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run desktop:pack > /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-package.stdout-stderr.txt 2>&1'` |
| C836 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/network-attempt-scan-r5.mjs` |
| C837 | repo | `/usr/bin/shasum -a 256 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service' 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Resources/app.asar' 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist' 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality' 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar'` |
| C838 | repo | `/usr/bin/plutil -p 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist'` |
| C839 | repo | `/usr/bin/plutil -p 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Info.plist'` |
| C840 | repo | `/usr/bin/find 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app' -type l -print` |
| C841 | repo | `/usr/bin/find 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app' -type l -exec /usr/bin/readlink '{}' ';'` |
| C842 | repo | `/usr/bin/diff -qr 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app' 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Library/LoginItems/Chirality Runtime Service.app'` |
| C843 | repo, session A | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/real-runtime-controller-r5.mjs` |
| C844 | repo | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/protocol/controller.json` |
| C845 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/real-second-session-sentinel-r5.mjs attach-intent <EXACT_HELPER_PID_FROM_C844>` |
| C846 | repo, session B | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/lldb-session-supervisor-r5.mjs <EXACT_HELPER_PID_FROM_C844>` |
| C847 | supervisor C990, new authority | `/usr/bin/xcrun lldb --batch -p <EXACT_HELPER_PID> -s /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt` |
| C848 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/real-second-session-sentinel-r5.mjs trace-ready <EXACT_HELPER_PID_FROM_C844>` |
| C849 | session A | Poll with zero input until exact `SIGNAL_ARMED`, bounded by controller ready +128.6 seconds. |
| C850 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/real-second-session-sentinel-r5.mjs trace-live <EXACT_HELPER_PID_FROM_C844>` |
| C851 | session A | Poll with zero input until replay-terminal output, bounded by controller ready +139.5 seconds. |
| C852 | session B only, new authority | Send exactly one ETX to the supervisor; the supervisor performs newly requested identity-guarded C1003 `SIGINT` to LLDB, buffers exact bytes `process detach\nquit\n`, and at EOF performs newly requested whole-buffer C1007 stdin forwarding. No byte is forwarded before EOF and whole-buffer equality. This is not historical C197. |
| C853 | session B | Poll with zero additional input for supervisor terminal; hard bound is LLDB spawn origin +149.9 seconds. |
| C854 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/session-terminal-receipt-r5.mjs PRE_CONTROLLER_NO_SESSION_B NONE` |
| C855 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/session-terminal-receipt-r5.mjs CONTROLLER_NO_LLDB_SPAWN NONE` |
| C856 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/session-terminal-receipt-r5.mjs LLDB_TERMINAL_BEFORE_ATTACH <EXACT_C846_EXIT>` |
| C857 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/session-terminal-receipt-r5.mjs NORMAL_EXACT_DETACH <EXACT_C846_EXIT>` |
| C858 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/session-terminal-receipt-r5.mjs FORCED_WATCHDOG_TERMINAL <EXACT_C846_EXIT>` |
| C859 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/session-terminal-receipt-r5.mjs POST_START_ABNORMAL_LLDB_TERMINAL <EXACT_C846_EXIT>` |
| C860 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/session-terminal-receipt-r5.mjs UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE <EXACT_C846_EXIT>` |
| C861 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/session-terminal-receipt-r5.mjs WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL <EXACT_C846_EXIT>` |
| C862 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/transcript-capture-r5.mjs BOTH WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL` |
| C863 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/transcript-capture-r5.mjs BOTH POST_START_ABNORMAL_LLDB_TERMINAL` |
| C864 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/transcript-capture-r5.mjs BOTH UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE` |
| C865 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/session-terminal-proof-r5.mjs` |
| C866 | session A | Poll with zero input until controller terminal; bound is cleanup permission +24 seconds. |
| C867 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/real-runtime-cleanup-verifier-r5.mjs` |
| C868 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/transcript-capture-r5.mjs A PRE_CONTROLLER_NO_SESSION_B` |
| C869 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/transcript-capture-r5.mjs A CONTROLLER_NO_LLDB_SPAWN` |
| C870 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/transcript-capture-r5.mjs A LLDB_TERMINAL_BEFORE_ATTACH` |
| C871 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/transcript-capture-r5.mjs A NORMAL_EXACT_DETACH` |
| C872 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/transcript-capture-r5.mjs A FORCED_WATCHDOG_TERMINAL` |
| C873 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/transcript-capture-r5.mjs B PRE_CONTROLLER_NO_SESSION_B` |
| C874 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/transcript-capture-r5.mjs B CONTROLLER_NO_LLDB_SPAWN` |
| C875 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/transcript-capture-r5.mjs B LLDB_TERMINAL_BEFORE_ATTACH` |
| C876 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/transcript-capture-r5.mjs B NORMAL_EXACT_DETACH` |
| C877 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/transcript-capture-r5.mjs B FORCED_WATCHDOG_TERMINAL` |
| C878 | repo | `/bin/mkdir -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r5` |
| C879 | repo | `/bin/mkdir -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r5/runtime` |
| C880 | repo | `/usr/bin/ditto /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-runtime projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r5/runtime` |
| C881 | repo | `/bin/mkdir -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r5/protocol` |
| C882 | repo | `/usr/bin/ditto /private/tmp/chirality-dapp92-option-a-20260804/protocol projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r5/protocol` |
| C883 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-package.stdout-stderr.txt projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r5/attempt8-package.stdout-stderr.txt` |
| C884 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/evidence/network-scan.matches.txt projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r5/network-scan.matches.txt` |
| C885 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/evidence/network-scan.status.json projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r5/network-scan.status.json` |
| C886 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/evidence-manifest-r5.mjs` |
| C887 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/cli-launcher.ts projects/chirality-app-dev/frontend/electron/cli-launcher.ts` |
| C888 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/main.ts projects/chirality-app-dev/frontend/electron/main.ts` |
| C889 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/runtime-control-ipc.ts projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts` |
| C890 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/package.json projects/chirality-app-dev/frontend/package.json` |
| C891 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts/build-electron.mjs projects/chirality-app-dev/frontend/scripts/build-electron.mjs` |
| C892 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/cli-launcher.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts` |
| C893 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/runtime-control-ipc.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts` |
| C894 | repo | `/bin/rm -f projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts` |
| C895 | repo | `/bin/rm -rf projects/chirality-app-dev/frontend/node_modules projects/chirality-app-dev/frontend/dist projects/chirality-app-dev/frontend/dist-runtime-helper projects/chirality-app-dev/frontend/dist-electron projects/chirality-app-dev/frontend/dist-runtime projects/chirality-app-dev/frontend/.next` |
| C896 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r5/rollback-verifier-r5.mjs` |
| C897 | repo | `/bin/test -f /private/tmp/chirality-dapp92-option-a-20260804/TEMP_DELETE_ALLOWED` |
| C898 | repo | `/bin/rm -rf /private/tmp/chirality-dapp92-option-a-20260804` |
| C899 | repo | `/bin/test ! -e /private/tmp/chirality-dapp92-option-a-20260804` |
| C900 | repo | `/bin/test -f projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r5/EVIDENCE_MANIFEST.sha256` |

Rows C854-C864 and C868-C877 are mutually exclusive branch-specific exact invocations. No
row permits a loop, another value, or free-form text.

## Script-internal actions

| ID | Exact independently gated operation |
|---|---|
| C901 | Create fixed evidence/protocol files and raw controller descriptors. |
| C902 | Spawn exact stale-helper `/usr/bin/env` child. |
| C903 | Install stale-helper error/exit settlement observer. |
| C904 | Install stale-helper 170,000 ms owned-handle watchdog. |
| C905 | Stale-helper 40 ms spawn-grace wait. |
| C906 | Stale-helper exact-PID `/bin/ps` identity probe. |
| C907 | Stale-helper exact-PID `/usr/sbin/lsof -d txt` probe. |
| C908 | Stale-helper bounded 80×100 ms readiness wait. |
| C909 | Pre-signal stale-helper exact-PID `/bin/ps` probe. |
| C910 | Pre-signal stale-helper exact-PID `/usr/sbin/lsof` probe. |
| C911 | Owned stale-helper `SIGKILL`. |
| C912 | Stale-helper 3,000 ms terminal wait. |
| C913 | Spawn exact final-helper `/usr/bin/env` child. |
| C914 | Install final-helper error/exit observer. |
| C915 | Install final-helper 170,000 ms owned-handle watchdog. |
| C916 | Final-helper 40 ms spawn-grace wait. |
| C917 | Final-helper initial exact-PID `/bin/ps` probe. |
| C918 | Final-helper initial exact-PID `/usr/sbin/lsof` probe. |
| C919 | Final-helper bounded 80×100 ms readiness wait. |
| C920 | Atomic controller-record write. |
| C921 | Bounded trace-ready wait, 50 ms polls through ready+28,000 ms. |
| C922 | Spawn exact tracked registration child. |
| C923 | Install registration error/exit observer. |
| C924 | Install registration 170,000 ms owned-handle watchdog. |
| C925 | Registration 40 ms spawn-grace wait. |
| C926 | Registration exact-PID `/bin/ps` probe. |
| C927 | Registration exact-PID `/usr/sbin/lsof` probe. |
| C928 | Registration stdout 1 MiB overflow monitor. |
| C929 | Registration stderr 1 MiB overflow monitor. |
| C930 | Registration 10,000 ms timeout arm. |
| C931 | Final-helper terminal-during-registration arm. |
| C932 | Registration race resolution over C923/C928-C931. |
| C933 | Bounded GUI-launch timer. |
| C934 | Spawn exact GUI `/usr/bin/env` child. |
| C935 | Install GUI error/exit observer. |
| C936 | Install GUI 170,000 ms owned-handle watchdog. |
| C937 | GUI 40 ms spawn-grace wait. |
| C938 | GUI initial exact-PID `/bin/ps` probe. |
| C939 | GUI initial exact-PID `/usr/sbin/lsof` probe. |
| C940 | Bounded 5×100 ms authenticated-contact wait. |
| C941 | Exact helper/GUI `/bin/ps` snapshot. |
| C942 | Exact helper Unix `/usr/sbin/lsof` snapshot. |
| C943 | Exact helper TCP `/usr/sbin/lsof` snapshot. |
| C944 | `/usr/bin/stat` of the two exact control paths. |
| C945 | `/usr/bin/shasum` of the five exact package files. |
| C946 | Bounded signal-arm timer. |
| C947 | Bounded trace-live wait. |
| C948 | Bounded first-signal timer. |
| C949 | Immediate pre-SIGTERM helper `/bin/ps` probe. |
| C950 | Immediate pre-SIGTERM helper `/usr/sbin/lsof` probe. |
| C951 | First ordinary owned-helper `SIGTERM`. |
| C952 | Bounded 80×100 ms helper-terminal poll. |
| C953 | Bounded 3,040×50 ms cleanup-permission wait. |
| C954 | Registration cleanup `/bin/ps` probe. |
| C955 | Registration cleanup `/usr/sbin/lsof` probe. |
| C956 | Owned registration `SIGKILL`. |
| C957 | Registration 3,000 ms terminal wait. |
| C958 | Stale cleanup `/bin/ps` probe. |
| C959 | Stale cleanup `/usr/sbin/lsof` probe. |
| C960 | Owned stale cleanup `SIGKILL`. |
| C961 | Stale cleanup 3,000 ms terminal wait. |
| C962 | GUI cleanup pre-TERM `/bin/ps` probe. |
| C963 | GUI cleanup pre-TERM `/usr/sbin/lsof` probe. |
| C964 | Owned GUI `SIGTERM`. |
| C965 | GUI graceful 3,000 ms terminal wait. |
| C966 | GUI cleanup pre-KILL `/bin/ps` probe. |
| C967 | GUI cleanup pre-KILL `/usr/sbin/lsof` probe. |
| C968 | Identity-guarded owned GUI `SIGKILL`. |
| C969 | GUI forced 3,000 ms terminal wait. |
| C970 | Helper cleanup `/bin/ps` probe. |
| C971 | Helper cleanup `/usr/sbin/lsof` probe. |
| C972 | Owned helper cleanup `SIGKILL`. |
| C973 | Helper cleanup 3,000 ms terminal wait. |
| C974 | Independent registration settlement completion. |
| C975 | Independent stale settlement completion. |
| C976 | Independent GUI settlement completion. |
| C977 | Independent helper settlement completion. |
| C978 | Record absent or already-terminal settlement fast path for the applicable child. |
| C979 | Record applicable child's first identity/signal/wait-stage failure; issue no additional signal in this row. |
| C980 | Record applicable GUI forced-stage identity/signal/wait failure; issue no additional signal in this row. |
| C981 | Race the applicable observed child exit against its already-live 170,000 ms absolute settlement deadline; issue no signal in this row. |
| C982 | Record the applicable fallback as terminal or bounded `terminal:false, unsafeToSignal:true`; retain the root on the latter. |
| C983 | Record an independently trapped settlement exception before the applicable C974-C977 completion row. |
| C984 | Attach-intent helper `/bin/ps` probe. |
| C985 | Attach-intent helper `/usr/sbin/lsof` probe and typed write. |
| C986 | Trace-ready helper `/bin/ps` probe. |
| C987 | Trace-ready helper `/usr/sbin/lsof` probe and typed write. |
| C988 | Trace-live helper `/bin/ps` probe. |
| C989 | Trace-live helper `/usr/sbin/lsof` probe and typed write. |
| C990 | Spawn exact new-authority C847 with piped streams, `detached:false`, and spawn origin captured immediately before. |
| C991 | Install callback-trapped LLDB error and stream-`close` observers; every callback error enters supervisor state. |
| C992 | Arm the spawn-origin+149,000 ms identity-guarded watchdog and independent spawn-origin+149,900 ms absolute supervisor deadline before any awaited probe. |
| C993 | Exclusively write the typed LLDB spawn-attempt receipt. |
| C994 | Trap/capture each LLDB stdout callback; callback failure records error and destroys only that stream. |
| C995 | Trap/capture each LLDB stderr callback; callback failure records error and destroys only that stream. |
| C996 | LLDB 40 ms start-observation race against stream-`close`. |
| C997 | Initial exact LLDB `/bin/ps` probe. |
| C998 | Initial exact LLDB `/usr/sbin/lsof` probe. |
| C999 | Exclusively write the mechanically observed LLDB-start receipt when still live, using either the initial C997-C998 identity proof or, if that initial observation did not produce a receipt, the later exact C1008-C1009 pre-signal watchdog identity proof before C1010. |
| C1000 | Trap exactly one newly authorized supervisor ETX/SIGINT event and reject duplicates. |
| C1001 | Immediate pre-new-SIGINT LLDB `/bin/ps` identity probe. |
| C1002 | Immediate pre-new-SIGINT LLDB `/usr/sbin/lsof` identity probe; this row carries no signal or fail-safe. |
| C1003 | Newly authorized identity-guarded LLDB-child `SIGINT`. |
| C1004 | Exclusively write the typed new-interrupt receipt. |
| C1005 | Trap and prefix/length-check newly authorized stdin data without forwarding. |
| C1006 | At EOF, require exact whole-buffer equality and exactly one C1003 event. |
| C1007 | Newly authorized one-time exact whole-buffer LLDB stdin write of `process detach\nquit\n`. |
| C1008 | At spawn+149,000 ms, exact LLDB `/bin/ps` identity probe. |
| C1009 | At spawn+149,000 ms, exact LLDB `/usr/sbin/lsof` identity probe. |
| C1010 | Wholly new owner authority: at the hard deadline, identity-guarded LLDB-child `SIGKILL`; if either probe fails, issue no signal, record `UNSAFE_TO_SIGNAL`, retain the root, and do not claim the 150-second maximum. |
| C1011 | Parse one typed terminal branch and numeric-or-NONE exit. |
| C1012 | Evaluate controller/intent/spawn/start/terminal presence matrix. |
| C1013 | Read exact LLDB terminal receipt when present. |
| C1014 | Read/hash exact LLDB spawn-attempt receipt when present. |
| C1015 | Read/hash exact LLDB-start receipt only when present. |
| C1016 | Hash exact C852 input/stdout/stderr files. |
| C1017 | Bind exact supervisor/session/LLDB/target/exit fields. |
| C1018 | Exclusive typed session-terminal receipt write. |
| C1019 | Read/hash typed session-terminal receipt. |
| C1020 | Bind exact controller PID/target. |
| C1021 | Bind exact spawn-attempt session and hash. |
| C1022 | Bind exact optional LLDB-start session and hash. |
| C1023 | Recompute exact input/stdout/stderr hashes. |
| C1024 | Evaluate exact target detach, early terminal, forced terminal, watchdog-accepted race terminal, post-start abnormal terminal, or identity-unsafe diagnostic failure; accept optional start only for the unsafe branch. |
| C1025 | Exclusive session-terminal proof write. |
| C1026 | Cleanup-permission write only after C1019-C1025 pass. |
| C1027 | Parse typed transcript session/branch. |
| C1028 | Exact session-A stdout copy. |
| C1029 | Exact session-A stderr copy. |
| C1030 | Exact session-B C852 input copy when session exists. |
| C1031 | Exact session-B LLDB stdout copy when session exists. |
| C1032 | Exact session-B LLDB stderr copy when session exists. |
| C1033 | Typed no-session-B absence receipt for the two no-session branches only. |
| C1034 | Exact transcript hash/length manifest write. |
| C1035 | Read and schema-check controller cleanup receipt. |
| C1036 | Check registration/stale/GUI/helper terminal states independently. |
| C1037 | Bind exact branch proof and cleanup permission. |
| C1038 | Exclusive cleanup-verifier receipt write. |
| C1039 | Exact `/usr/bin/grep` network-attempt scan plus status/match writes. |
| C1040 | Recursively read only the fixed durable evidence root. |
| C1041 | Byte-sort exact relative evidence paths. |
| C1042 | Hash each sorted evidence file and exclusively write `EVIDENCE_MANIFEST.sha256`. |
| C1043 | Byte-equal manifest readback assertion. |
| C1044 | Compare all eight literal final frontend path/hash pairs. |
| C1045 | Spawn exact frontend-scoped `/usr/bin/git status --short --untracked-files=all`. |
| C1046 | Assert Git command success and exactly empty stdout. |
| C1047 | Assert five candidate additions absent. |
| C1048 | Assert six build/dependency derivative roots absent. |
| C1049 | Exclusively write `TEMP_DELETE_ALLOWED`. |
| C1050 | Require permission marker readback before external C897-C898. |
| C1051 | Remove the supervisor SIGINT and stdin data/end listeners and pause stdin before terminal receipt construction. |
| C1052 | Close the three exact LLDB evidence descriptors after the terminal/deadline race resolves. |
| C1053 | Exclusively write the LLDB terminal receipt with listener-teardown and final-exit action bindings. |
| C1054 | Attempt replay-terminal evidence write inside `finally`; record failure without bypassing child settlement. |
| C1055 | Write controller-cleanup evidence only after all applicable independent child settlements finish. |
| C1056 | Write final protocol-result evidence after controller cleanup evidence. |
| C1057 | Explicitly terminate the supervisor with exit 0 for exact detach, 4 for identity-unsafe diagnostic failure, or 1 for every other observed-terminal branch. |

## Mutually exclusive branch law

Exactly one branch is selected from observed artifacts; no branch requires a
file from a session that did not exist.

| Branch | Required | Forbidden | Exact path to evidence/rollback |
|---|---|---|---|
| `PRE_CONTROLLER_NO_SESSION_B` | replay terminal and controller cleanup record; no controller record | controller, attach-intent, LLDB spawn/start/terminal | C854, C865-C868, C873, C878-C900 |
| `CONTROLLER_NO_LLDB_SPAWN` | controller record; optionally attach-intent; no spawn attempt | LLDB spawn/start/terminal | C855, C865-C867, C869, C874, C878-C900 |
| `LLDB_TERMINAL_BEFORE_ATTACH` | controller, attach-intent, spawn-attempt, terminal | lldb-start | C856, C865-C867, C870, C875, C878-C900 |
| `NORMAL_EXACT_DETACH` | all same-session start/terminal bindings, exact one ETX, exact buffered detach/quit input, exit 0, exact `Process <TARGET_PID> detached` | watchdog/fail-safe terminal | C857, C865-C867, C871, C876, C878-C900 |
| `FORCED_WATCHDOG_TERMINAL` | all same-session start/terminal bindings, observed stream-`close`, and exact identity-guarded C1010 `SIGKILL` terminal | normal-detach or unsafe-to-signal claim | C858, C865-C867, C872, C877, C878-C900 |
| `WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL` | all same-session start/terminal bindings, observed stream-`close`, exact identity-guarded C1010 `SIGKILL` accepted, and a terminal signal other than `SIGKILL` from the concurrent terminal race | forced-watchdog, normal-detach, or unsafe-to-signal claim | C861-C862, C865-C867, C878-C900 |
| `POST_START_ABNORMAL_LLDB_TERMINAL` | controller, attach-intent, same-session spawn/start/terminal, observed stream-`close`, and any non-normal/non-watchdog terminal state | normal-detach or watchdog-success claim | C859, C863, C865-C867, C878-C900 |
| `UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE` | controller, attach-intent, same-session spawn/terminal receipt, optional same-session start receipt, `terminalObserved:false`, and watchdog `UNSAFE_TO_SIGNAL` | any LLDB-child-terminal, cleanup-permission, cleanup-complete, rollback, temporary-root-deletion, 150-second-maximum, or no-orphan claim | C860, C864-C865 only; C865 writes `LLDB_MAXIMUM_NOT_PROVED_IDENTITY_UNSAFE`, exits nonzero after proof, controller records incomplete cleanup, and the fixed root remains |

C865 alone may create cleanup permission, and only after the applicable row's
complete binding passes, and it never creates cleanup permission for
`UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE`. Each controller child is
outer-registered immediately after spawn; callback-trapped exit/error listeners
and an absolute 170,000 ms settlement deadline are installed before a wait or
identity probe. Registration, stale helper, GUI, and helper settlement continue
independently after failures. A throwing identity probe never causes a signal:
settlement remains bounded by the already-live deadline, records
`terminal:false, unsafeToSignal:true`, and retains the root without claiming
child terminality.

LLDB's deadline begins at the instant immediately before C990. C991-C992 are
installed before any awaited identity operation. C1008-C1010 run at +149,000
ms; C1010 signals only after both live-identity probes pass. If the initial
C997-C998 observation did not produce a start receipt, the same C1008-C1009
pre-signal proof truthfully supplies the C999 start receipt before C1010, so a
watchdog-accepted concurrent terminal is classified before the early-terminal
fallback and remains consumable by the unchanged receipt/proof scripts. The independent
absolute race resolves at observed stream-`close` or +149,900 ms. If identity
cannot be proved and no `close` is observed, the supervisor writes
`UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE`, exits boundedly, makes no LLDB-child
terminal or no-orphan claim, withholds cleanup permission, and retains the fixed
root. All callback errors are trapped into supervisor state. Any observed
post-start terminal that is neither exact normal detach nor watchdog terminal is
mechanically classified `POST_START_ABNORMAL_LLDB_TERMINAL` and still permits
independent cleanup because LLDB stream-`close` was observed. Arbitrary,
partial, overlong, non-prefix, duplicate, or post-EOF stdin is rejected/closed
without forwarding. Only one EOF-complete byte-equal C852 buffer is forwarded
once, entirely under newly requested authority.

## Durable evidence and rollback law

C878-C886 finish before any rollback or fixed-root deletion on the seven
terminal-safe branches. They retain the
actual branch receipt, raw controller streams, exact C852 input, LLDB raw
stdout/stderr if session B existed, typed session-B absence if it did not,
spawn/start/terminal/session proof, package transcript, network-scan result,
action/deviation logs, cleanup receipts, and a deterministically sorted durable
hash manifest. Credential/token bytes and raw registration stdout are never
retained. The unsafe-to-signal branch stops after its typed proof: no cleanup,
durable-copy, rollback, permission marker, or fixed-root deletion is claimed.

C887-C895 are attempted independently in order even if a prior rollback step
fails. C896 then compares the exact final eight hashes, requires an exactly
empty frontend status, and requires all named candidate/build/dependency
derivatives absent. Only C896 may create `TEMP_DELETE_ALLOWED`; C897 must see
it before C898. If any restore or validation fails, C898-C899 are forbidden:
the baseline and fixed root remain for diagnosis and the failure is reported.
C900 proves the durable manifest exists after deletion.

Rollback constants, in C797/C1044 order:

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
