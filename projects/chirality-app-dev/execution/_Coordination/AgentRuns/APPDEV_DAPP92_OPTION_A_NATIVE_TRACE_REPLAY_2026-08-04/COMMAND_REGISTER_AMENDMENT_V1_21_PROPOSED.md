# Proposed command-register amendment v1.21 — Attempt-8 R6

Status: `PROPOSED — MANAGER FREEZE, FRESH VERIFIER, AND OWNER APPROVAL REQUIRED — NOT EXECUTED`

This standalone replacement answers exactly the four material findings in the
immutable v1.20 fresh-verifier return at accepted SHA-256
`47b57dae327e247c97a8957ad2cdf602b10ff64b94546babc3c5c1b8f5dbe655`.
V1.16-v1.20, R3-R5, and all prior proposal bytes remain byte-preserved rejected
history. No R6 script or runtime command has been invoked. The manager, not
the author, will independently hash and freeze the final proposal bytes.

`repo` is `/Users/ryan/.codex/worktrees/7388/chirality`; `frontend` is
`repo/projects/chirality-app-dev/frontend`; `root` is
`/private/tmp/chirality-dapp92-option-a-20260804`. C787-C1066 are one unique,
contiguous R6 owner-gated range. Historical C196/C197 remain unused context
only. C847, C848, and C853 are redesigned operations presented solely as new owner
authority and claim no inheritance from C196/C197.

The live R6 proposal contains ten `.mjs` files plus `README.md`, not eleven
`.mjs` files. The stale count in the immutable R7 handoff/validation is
historical and is not repeated as current fact here.

## External commands and controls

Every row is one command, one existing-session poll/control, or one exact
script invocation. A nonzero result stops forward execution and enters the
branch and rollback law below.

| ID | Cwd | Exact command/control |
|---|---|---|
| C787 | repo | `/usr/bin/shasum -a 256 projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/reviews/A2_ATTEMPT8_V1_20_FRESH_ADVERSARIAL_VERIFIER_RETURN.md projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/real-runtime-controller-r6.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/real-second-session-sentinel-r6.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/lldb-session-supervisor-r6.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/session-terminal-receipt-r6.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/session-terminal-proof-r6.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/transcript-capture-r6.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/real-runtime-cleanup-verifier-r6.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/network-attempt-scan-r6.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/evidence-manifest-r6.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/rollback-verifier-r6.mjs` — require exactly these ordered SHA-256 values: `47b57dae327e247c97a8957ad2cdf602b10ff64b94546babc3c5c1b8f5dbe655`, `49cdc334388896fefd066e7e3d0405b870923a1e3ad81e3f41e8d2542c225722`, `bb6be369be35d8d73ac20fb244c0df844c0041ac87bfd33158ec8d19099fbce8`, `2137a72e0c53639319b3120cc65a27e58a66e900a5577b7747ff9bb4c55495a4`, `d6292506552630b3d8db0f21de7f93e6e37102663632db59a6e36d6d5b3a51ce`, `20c0e9477489e9b00b5cc4ccf3db85f79b59c1cb2d0807ceeafb66a253a5178d`, `8c3a4edcb32224091c9490034ef46f2e48c7dc0c291cdb486cb82aa4232d5edc`, `17d068b207dd277e257e1cc55f486b9a0ae29e06bd5a24e4e7a31fef15f5eacb`, `f03479d834868f7befd264eba03dbefdb61fdbe93fd942b1c34d69bda87e5453`, `c752f0b1bd33073e7aafa951e1fd51fb374ee18b393d1c025ef30416a6db0be5`, and `c06f58cabf2130518be19cc58d3a21901b674a0ca63ceeb1289b3a9a0621f4a3`. |
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
| C836 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/network-attempt-scan-r6.mjs` |
| C837 | repo | `/usr/bin/shasum -a 256 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service' 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Resources/app.asar' 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist' 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality' 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar'` |
| C838 | repo | `/usr/bin/plutil -p 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist'` |
| C839 | repo | `/usr/bin/plutil -p 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Info.plist'` |
| C840 | repo | `/usr/bin/find 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app' -type l -print` |
| C841 | repo | `/usr/bin/find 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app' -type l -exec /usr/bin/readlink '{}' ';'` |
| C842 | repo | `/usr/bin/diff -qr 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app' 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Library/LoginItems/Chirality Runtime Service.app'` |
| C843 | repo, session A | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/real-runtime-controller-r6.mjs` |
| C844 | repo | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/protocol/controller.json` |
| C845 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/real-second-session-sentinel-r6.mjs attach-intent <EXACT_HELPER_PID_FROM_C844>` |
| C846 | repo, session B | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/lldb-session-supervisor-r6.mjs <EXACT_HELPER_PID_FROM_C844>` |
| C847 | supervisor C992-C995, new authority | Immediately re-prove the controller direct-child helper with exact PID, PPID, start identity, executable, and byte-bound attach-intent/controller identities; exclusively write `target-identity-guard.json`. `FAILED_CLOSED_NO_LLDB_SPAWN` issues no C848 or other target-affecting operation. |
| C848 | supervisor C996, new authority | `/usr/bin/xcrun lldb --batch -p <EXACT_HELPER_PID> -s /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt` |
| C849 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/real-second-session-sentinel-r6.mjs trace-ready <EXACT_HELPER_PID_FROM_C844>` |
| C850 | session A | Poll with zero input until exact `SIGNAL_ARMED`, bounded by controller ready +128.6 seconds. |
| C851 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/real-second-session-sentinel-r6.mjs trace-live <EXACT_HELPER_PID_FROM_C844>` |
| C852 | session A | Poll with zero input until replay-terminal output, bounded by controller ready +139.5 seconds. |
| C853 | session B only, new authority | Send exactly one ETX to the supervisor; the supervisor performs newly requested identity-guarded C1009 `SIGINT` to LLDB, buffers exact bytes `process detach\nquit\n`, and at EOF performs newly requested whole-buffer C1014 stdin forwarding. No byte is forwarded before EOF and whole-buffer equality. This is not historical C197. |
| C854 | session B | Poll with zero additional input for supervisor terminal; hard bound is LLDB spawn origin +149.9 seconds. |
| C855 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/session-terminal-receipt-r6.mjs PRE_CONTROLLER_NO_SESSION_B NONE` |
| C856 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/session-terminal-receipt-r6.mjs CONTROLLER_NO_LLDB_SPAWN <EXACT_C846_EXIT>` — valid only for exact exit 5 and typed C847 fail-closed receipt. |
| C857 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/session-terminal-receipt-r6.mjs LLDB_TERMINAL_BEFORE_ATTACH <EXACT_C846_EXIT>` |
| C858 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/session-terminal-receipt-r6.mjs NORMAL_EXACT_DETACH <EXACT_C846_EXIT>` |
| C859 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/session-terminal-receipt-r6.mjs FORCED_WATCHDOG_TERMINAL <EXACT_C846_EXIT>` |
| C860 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/session-terminal-receipt-r6.mjs POST_START_ABNORMAL_LLDB_TERMINAL <EXACT_C846_EXIT>` |
| C861 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/session-terminal-receipt-r6.mjs UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE <EXACT_C846_EXIT>` |
| C862 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/session-terminal-receipt-r6.mjs WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL <EXACT_C846_EXIT>` |
| C863 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/session-terminal-receipt-r6.mjs WATCHDOG_SIGNAL_ACCEPTED_NO_CLOSE_AT_DEADLINE <EXACT_C846_EXIT>` |
| C864 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/transcript-capture-r6.mjs BOTH WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL` |
| C865 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/transcript-capture-r6.mjs BOTH POST_START_ABNORMAL_LLDB_TERMINAL` |
| C866 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/transcript-capture-r6.mjs BOTH UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE` |
| C867 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/session-terminal-proof-r6.mjs` |
| C868 | session A | Poll with zero input until controller terminal; bound is cleanup permission +24 seconds. |
| C869 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/real-runtime-cleanup-verifier-r6.mjs` |
| C870 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/transcript-capture-r6.mjs A PRE_CONTROLLER_NO_SESSION_B` |
| C871 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/transcript-capture-r6.mjs A CONTROLLER_NO_LLDB_SPAWN` |
| C872 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/transcript-capture-r6.mjs A LLDB_TERMINAL_BEFORE_ATTACH` |
| C873 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/transcript-capture-r6.mjs A NORMAL_EXACT_DETACH` |
| C874 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/transcript-capture-r6.mjs A FORCED_WATCHDOG_TERMINAL` |
| C875 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/transcript-capture-r6.mjs B PRE_CONTROLLER_NO_SESSION_B` |
| C876 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/transcript-capture-r6.mjs B CONTROLLER_NO_LLDB_SPAWN` |
| C877 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/transcript-capture-r6.mjs B LLDB_TERMINAL_BEFORE_ATTACH` |
| C878 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/transcript-capture-r6.mjs B NORMAL_EXACT_DETACH` |
| C879 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/transcript-capture-r6.mjs B FORCED_WATCHDOG_TERMINAL` |
| C880 | repo | `/bin/mkdir -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r6` |
| C881 | repo | `/bin/mkdir -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r6/runtime` |
| C882 | repo | `/usr/bin/ditto /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-runtime projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r6/runtime` |
| C883 | repo | `/bin/mkdir -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r6/protocol` |
| C884 | repo | `/usr/bin/ditto /private/tmp/chirality-dapp92-option-a-20260804/protocol projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r6/protocol` |
| C885 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-package.stdout-stderr.txt projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r6/attempt8-package.stdout-stderr.txt` |
| C886 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/evidence/network-scan.matches.txt projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r6/network-scan.matches.txt` |
| C887 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/evidence/network-scan.status.json projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r6/network-scan.status.json` |
| C888 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/evidence-manifest-r6.mjs` |
| C889 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/cli-launcher.ts projects/chirality-app-dev/frontend/electron/cli-launcher.ts` |
| C890 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/main.ts projects/chirality-app-dev/frontend/electron/main.ts` |
| C891 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/runtime-control-ipc.ts projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts` |
| C892 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/package.json projects/chirality-app-dev/frontend/package.json` |
| C893 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts/build-electron.mjs projects/chirality-app-dev/frontend/scripts/build-electron.mjs` |
| C894 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/cli-launcher.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts` |
| C895 | repo | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/runtime-control-ipc.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts` |
| C896 | repo | `/bin/rm -f projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts` |
| C897 | repo | `/bin/rm -rf projects/chirality-app-dev/frontend/node_modules projects/chirality-app-dev/frontend/dist projects/chirality-app-dev/frontend/dist-runtime-helper projects/chirality-app-dev/frontend/dist-electron projects/chirality-app-dev/frontend/dist-runtime projects/chirality-app-dev/frontend/.next` |
| C898 | repo | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r6/rollback-verifier-r6.mjs` |
| C899 | repo | `/bin/test -f /private/tmp/chirality-dapp92-option-a-20260804/TEMP_DELETE_ALLOWED` |
| C900 | repo | `/bin/rm -rf /private/tmp/chirality-dapp92-option-a-20260804` |
| C901 | repo | `/bin/test ! -e /private/tmp/chirality-dapp92-option-a-20260804` |
| C902 | repo | `/bin/test -f projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r6/EVIDENCE_MANIFEST.sha256` |

Rows C855-C866 and C870-C879 are mutually exclusive branch-specific exact invocations. No
row permits a loop, another value, or free-form text.

## Script-internal actions

| ID | Exact independently gated operation |
|---|---|
| C903 | Create fixed evidence/protocol files and raw controller descriptors. |
| C904 | Spawn exact stale-helper `/usr/bin/env` child. |
| C905 | Install distinct stale-helper nonterminal `error` recorder and drained-`close` terminal observer; `error` alone never settles. |
| C906 | Install stale-helper 170,000 ms owned-handle watchdog. |
| C907 | Stale-helper 40 ms spawn-grace wait. |
| C908 | Stale-helper exact-PID `/bin/ps` identity probe. |
| C909 | Stale-helper exact-PID `/usr/sbin/lsof -d txt` probe. |
| C910 | Stale-helper bounded 80×100 ms readiness wait. |
| C911 | Pre-signal stale-helper exact-PID `/bin/ps` probe. |
| C912 | Pre-signal stale-helper exact-PID `/usr/sbin/lsof` probe. |
| C913 | Owned stale-helper `SIGKILL`. |
| C914 | Stale-helper 3,000 ms terminal wait. |
| C915 | Spawn exact final-helper `/usr/bin/env` child. |
| C916 | Install distinct final-helper nonterminal `error` recorder and drained-`close` terminal observer; `error` alone never settles. |
| C917 | Install final-helper 170,000 ms owned-handle watchdog. |
| C918 | Final-helper 40 ms spawn-grace wait. |
| C919 | Final-helper initial exact-PID `/bin/ps` probe. |
| C920 | Final-helper initial exact-PID `/usr/sbin/lsof` probe. |
| C921 | Final-helper bounded 80×100 ms readiness wait. |
| C922 | Atomic controller-record write. |
| C923 | Bounded trace-ready wait, 50 ms polls through ready+28,000 ms. |
| C924 | Spawn exact tracked registration child. |
| C925 | Install distinct registration nonterminal `error` recorder and drained-`close` terminal observer; `error` alone never settles. |
| C926 | Install registration 170,000 ms owned-handle watchdog. |
| C927 | Registration 40 ms spawn-grace wait. |
| C928 | Registration exact-PID `/bin/ps` probe. |
| C929 | Registration exact-PID `/usr/sbin/lsof` probe. |
| C930 | Registration stdout 1 MiB overflow monitor. |
| C931 | Registration stderr 1 MiB overflow monitor. |
| C932 | Registration 10,000 ms timeout arm. |
| C933 | Final-helper terminal-during-registration arm. |
| C934 | Registration race resolution over C925/C930-C933. |
| C935 | Bounded GUI-launch timer. |
| C936 | Spawn exact GUI `/usr/bin/env` child. |
| C937 | Install distinct GUI nonterminal `error` recorder and drained-`close` terminal observer; `error` alone never settles. |
| C938 | Install GUI 170,000 ms owned-handle watchdog. |
| C939 | GUI 40 ms spawn-grace wait. |
| C940 | GUI initial exact-PID `/bin/ps` probe. |
| C941 | GUI initial exact-PID `/usr/sbin/lsof` probe. |
| C942 | Bounded 5×100 ms authenticated-contact wait. |
| C943 | Exact helper/GUI `/bin/ps` snapshot. |
| C944 | Exact helper Unix `/usr/sbin/lsof` snapshot. |
| C945 | Exact helper TCP `/usr/sbin/lsof` snapshot. |
| C946 | `/usr/bin/stat` of the two exact control paths. |
| C947 | `/usr/bin/shasum` of the five exact package files. |
| C948 | Bounded signal-arm timer. |
| C949 | Bounded trace-live wait. |
| C950 | Bounded first-signal timer. |
| C951 | Immediate pre-SIGTERM helper `/bin/ps` probe. |
| C952 | Immediate pre-SIGTERM helper `/usr/sbin/lsof` probe. |
| C953 | First ordinary owned-helper `SIGTERM`. |
| C954 | Bounded 80×100 ms helper-terminal poll. |
| C955 | Bounded 3,040×50 ms cleanup-permission wait. |
| C956 | Registration cleanup `/bin/ps` probe. |
| C957 | Registration cleanup `/usr/sbin/lsof` probe. |
| C958 | Owned registration `SIGKILL`. |
| C959 | Registration 3,000 ms terminal wait. |
| C960 | Stale cleanup `/bin/ps` probe. |
| C961 | Stale cleanup `/usr/sbin/lsof` probe. |
| C962 | Owned stale cleanup `SIGKILL`. |
| C963 | Stale cleanup 3,000 ms terminal wait. |
| C964 | GUI cleanup pre-TERM `/bin/ps` probe. |
| C965 | GUI cleanup pre-TERM `/usr/sbin/lsof` probe. |
| C966 | Owned GUI `SIGTERM`. |
| C967 | GUI graceful 3,000 ms terminal wait. |
| C968 | GUI cleanup pre-KILL `/bin/ps` probe. |
| C969 | GUI cleanup pre-KILL `/usr/sbin/lsof` probe. |
| C970 | Identity-guarded owned GUI `SIGKILL`. |
| C971 | GUI forced 3,000 ms terminal wait. |
| C972 | Helper cleanup `/bin/ps` probe. |
| C973 | Helper cleanup `/usr/sbin/lsof` probe. |
| C974 | Owned helper cleanup `SIGKILL`. |
| C975 | Helper cleanup 3,000 ms terminal wait. |
| C976 | Independent registration settlement completion. |
| C977 | Independent stale settlement completion. |
| C978 | Independent GUI settlement completion. |
| C979 | Independent helper settlement completion. |
| C980 | Record absent or already-terminal settlement fast path for the applicable child. |
| C981 | Record applicable child's first identity/signal/wait-stage failure; issue no additional signal in this row. |
| C982 | Record applicable GUI forced-stage identity/signal/wait failure; issue no additional signal in this row. |
| C983 | Race the applicable observed child exit against its already-live 170,000 ms absolute settlement deadline; issue no signal in this row. |
| C984 | Record the applicable fallback as terminal or bounded `terminal:false, unsafeToSignal:true`; retain the root on the latter. |
| C985 | Record an independently trapped settlement exception before the applicable C976-C979 completion row. |
| C986 | Attach-intent helper `/bin/ps` probe. |
| C987 | Attach-intent helper `/usr/sbin/lsof` probe and typed write. |
| C988 | Trace-ready helper `/bin/ps` probe. |
| C989 | Trace-ready helper `/usr/sbin/lsof` probe and typed write. |
| C990 | Trace-live helper `/bin/ps` probe. |
| C991 | Trace-live helper `/usr/sbin/lsof` probe and typed write. |
| C992 | Bind exact controller and accepted attach-intent identities for immediate C847. |
| C993 | Immediate pre-C848 exact target-helper `/bin/ps` PID/PPID/start/executable probe. |
| C994 | Immediate pre-C848 exact target-helper `/usr/sbin/lsof -d txt` executable probe. |
| C995 | Exclusively write the typed C847 pass or fail-closed receipt; failure exits 5 without C848. |
| C996 | Spawn exact new-authority C848 with piped streams, `detached:false`, and spawn origin captured immediately before. |
| C997 | Install distinct callback-trapped LLDB nonterminal `error` recorder and drained stream-`close` terminal observer; `error` alone never settles or cancels a deadline. |
| C998 | Arm the spawn-origin+149,000 ms identity-guarded watchdog and independent spawn-origin+149,900 ms absolute supervisor deadline before any awaited probe. |
| C999 | Exclusively write the typed LLDB spawn-attempt receipt. |
| C1000 | Trap/capture each LLDB stdout callback; callback failure records error and destroys only that stream. |
| C1001 | Trap/capture each LLDB stderr callback; callback failure records error and destroys only that stream. |
| C1002 | LLDB 40 ms start-observation race against stream-`close`. |
| C1003 | Initial exact LLDB `/bin/ps` probe. |
| C1004 | Initial exact LLDB `/usr/sbin/lsof` probe. |
| C1005 | Exclusively write the mechanically observed LLDB-start receipt when still live, using either the initial C1003-C1004 identity proof or, if that initial observation did not produce a receipt, the later exact C1016-C1017 pre-signal watchdog identity proof before C1018. |
| C1006 | Trap exactly one newly authorized supervisor ETX/SIGINT event and reject duplicates. |
| C1007 | Immediate pre-new-SIGINT LLDB `/bin/ps` identity probe. |
| C1008 | Immediate pre-new-SIGINT LLDB `/usr/sbin/lsof` identity probe; this row carries no signal or fail-safe. |
| C1009 | Newly authorized identity-guarded LLDB-child `SIGINT`. |
| C1010 | Exclusively write the typed new-interrupt receipt. |
| C1011 | Trap and prefix/length-check newly authorized stdin data without forwarding. |
| C1012 | At EOF, require exact whole-buffer equality, one accepted C1009, and its typed C1010 receipt. |
| C1013 | Trap `child.stdin` stream errors as nonterminal failure evidence; never bypass settlement. |
| C1014 | Newly authorized one-time exact whole-buffer LLDB stdin write of `process detach\nquit\n`. |
| C1015 | Trap the C1014 completion callback and record completion/failure without bypassing settlement. |
| C1016 | At spawn+149,000 ms, exact LLDB `/bin/ps` identity probe. |
| C1017 | At spawn+149,000 ms, exact LLDB `/usr/sbin/lsof` identity probe. |
| C1018 | Wholly new owner authority: at the hard deadline, identity-guarded LLDB-child `SIGKILL`; if either probe fails, issue no signal, record `UNSAFE_TO_SIGNAL`, retain the root, and do not claim the 150-second maximum. |
| C1019 | Classify accepted C1018 with no drained LLDB `close` by +149,900 ms as `WATCHDOG_SIGNAL_ACCEPTED_NO_CLOSE_AT_DEADLINE`; retain root and make no terminality, orphan-absence, or 150-second claim. |
| C1020 | Parse one typed terminal branch and numeric-or-NONE exit. |
| C1021 | Evaluate controller/intent/spawn/start/terminal presence matrix. |
| C1022 | Read exact LLDB terminal receipt when present. |
| C1023 | Read/hash exact LLDB spawn-attempt receipt when present. |
| C1024 | Read/hash exact LLDB-start receipt only when present. |
| C1025 | Hash exact C853 input/stdout/stderr files. |
| C1026 | Bind exact supervisor/session/LLDB/target/exit fields. |
| C1027 | Exclusive typed session-terminal receipt write. |
| C1028 | Read/hash typed session-terminal receipt. |
| C1029 | Bind exact controller PID/target. |
| C1030 | Bind exact spawn-attempt session and hash. |
| C1031 | Bind exact optional LLDB-start session and hash. |
| C1032 | Recompute exact input/stdout/stderr hashes. |
| C1033 | Evaluate exact target detach, early drained close, forced drained close, watchdog-accepted race drained close, post-start abnormal drained close, accepted-watchdog/no-close failure, or identity-unsafe failure; accept optional start only for identity-unsafe. |
| C1034 | Exclusive session-terminal proof write. |
| C1035 | Cleanup-permission write only after C1028-C1034 pass. |
| C1036 | Parse typed transcript session/branch. |
| C1037 | Exact session-A stdout copy. |
| C1038 | Exact session-A stderr copy. |
| C1039 | Exact session-B C853 input copy when session exists. |
| C1040 | Exact session-B LLDB stdout copy when session exists. |
| C1041 | Exact session-B LLDB stderr copy when session exists. |
| C1042 | Typed no-session-B absence receipt for the two no-session branches only. |
| C1043 | Exact transcript hash/length manifest write. |
| C1044 | Read and schema-check controller cleanup receipt. |
| C1045 | Check registration/stale/GUI/helper terminal states independently. |
| C1046 | Bind exact branch proof and cleanup permission. |
| C1047 | Exclusive cleanup-verifier receipt write. |
| C1048 | Exact `/usr/bin/grep` network-attempt scan plus status/match writes. |
| C1049 | Recursively read only the fixed durable evidence root. |
| C1050 | Byte-sort exact relative evidence paths. |
| C1051 | Hash each sorted evidence file and exclusively write `EVIDENCE_MANIFEST.sha256`. |
| C1052 | Byte-equal manifest readback assertion. |
| C1053 | Compare all eight literal final frontend path/hash pairs. |
| C1054 | Spawn exact frontend-scoped `/usr/bin/git status --short --untracked-files=all`. |
| C1055 | Assert Git command success and exactly empty stdout. |
| C1056 | Assert five candidate additions absent. |
| C1057 | Assert six build/dependency derivative roots absent. |
| C1058 | Exclusively write `TEMP_DELETE_ALLOWED`. |
| C1059 | Require permission marker readback before external C899-C900. |
| C1060 | Remove the supervisor SIGINT and stdin data/end listeners and pause stdin before terminal receipt construction. |
| C1061 | Close the three exact LLDB evidence descriptors after the terminal/deadline race resolves. |
| C1062 | Exclusively write the LLDB terminal receipt with listener-teardown and final-exit action bindings. |
| C1063 | Attempt replay-terminal evidence write inside `finally`; record failure without bypassing child settlement. |
| C1064 | Write controller-cleanup evidence only after all applicable independent child settlements finish. |
| C1065 | Write final protocol-result evidence after controller cleanup evidence. |
| C1066 | Explicitly terminate the supervisor with exit 0 for exact detach, 4 for identity-unsafe diagnostic failure, or 1 for every other observed-terminal branch. |

## Mutually exclusive branch law

Exactly one branch is selected from observed artifacts; no branch requires a
file from a session that did not exist.

| Branch | Required | Forbidden | Exact path to evidence/rollback |
|---|---|---|---|
| `PRE_CONTROLLER_NO_SESSION_B` | replay terminal and controller cleanup record; no controller record | controller, attach-intent, LLDB spawn/start/terminal | C855, C867-C870, C875, C880-C902 |
| `CONTROLLER_NO_LLDB_SPAWN` | controller, attach-intent, exact C847 fail-closed receipt, C846 exit 5; no spawn attempt | LLDB spawn/start/terminal or any target-affecting operation | C856, C867-C869, C871, C876, C880-C902 |
| `LLDB_TERMINAL_BEFORE_ATTACH` | controller, attach-intent, spawn-attempt, terminal | lldb-start | C857, C867-C869, C872, C877, C880-C902 |
| `NORMAL_EXACT_DETACH` | all same-session start/terminal bindings, exact one ETX, exact buffered detach/quit input, exit 0, exact `Process <TARGET_PID> detached` | watchdog/fail-safe terminal | C858, C867-C869, C873, C878, C880-C902 |
| `FORCED_WATCHDOG_TERMINAL` | all same-session start/terminal bindings, observed stream-`close`, and exact identity-guarded C1018 `SIGKILL` terminal | normal-detach or unsafe-to-signal claim | C859, C867-C869, C874, C879, C880-C902 |
| `WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL` | all same-session start/terminal bindings, observed stream-`close`, exact identity-guarded C1018 `SIGKILL` accepted, and a terminal signal other than `SIGKILL` from the concurrent terminal race | forced-watchdog, normal-detach, or unsafe-to-signal claim | C862-C864, C867-C869, C880-C902 |
| `WATCHDOG_SIGNAL_ACCEPTED_NO_CLOSE_AT_DEADLINE` | passed C847, same-session spawn/start/terminal receipt, accepted C1018, and `terminalObserved:false` at +149,900 ms | any LLDB-terminal, orphan-absence, cleanup, rollback, deletion, or 150-second claim | C863, C867 only; typed diagnostic proof, nonzero exit, retained root |
| `POST_START_ABNORMAL_LLDB_TERMINAL` | controller, attach-intent, same-session spawn/start/terminal, observed stream-`close`, and any non-normal/non-watchdog terminal state | normal-detach or watchdog-success claim | C860, C865, C867-C869, C880-C902 |
| `UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE` | controller, attach-intent, same-session spawn/terminal receipt, optional same-session start receipt, `terminalObserved:false`, and watchdog `UNSAFE_TO_SIGNAL` | any LLDB-child-terminal, cleanup-permission, cleanup-complete, rollback, temporary-root-deletion, 150-second-maximum, or no-orphan claim | C861, C866-C867 only; C867 writes `LLDB_MAXIMUM_NOT_PROVED_IDENTITY_UNSAFE`, exits nonzero after proof, controller records incomplete cleanup, and the fixed root remains |

C867 alone may create cleanup permission, and only after the applicable row's
complete binding passes, and it never creates cleanup permission for either
no-close diagnostic branch. Each controller child is outer-registered
immediately after spawn; distinct nonterminal-`error` and drained-`close` listeners
and an absolute 170,000 ms settlement deadline are installed before a wait or
identity probe. Registration, stale helper, GUI, and helper settlement continue
independently after failures. A throwing identity probe never causes a signal:
settlement remains bounded by the already-live deadline, records
`terminal:false, unsafeToSignal:true`, and retains the root without claiming
child terminality.

LLDB's deadline begins at the instant immediately before C996. C997-C998 are
installed before any awaited identity operation. C1016-C1018 run at +149,000
ms; C1018 signals only after both live-identity probes pass. If the initial
C1003-C1004 observation did not produce a start receipt, the same C1016-C1017
pre-signal proof truthfully supplies the C1005 start receipt before C1018, so a
watchdog-accepted concurrent terminal is classified before the early-terminal
fallback and remains consumable by the unchanged receipt/proof scripts. The independent
absolute race resolves at observed drained stream-`close` or +149,900 ms. If
identity cannot be proved, the supervisor writes
`UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE`; if C1018 was accepted but no drained
`close` is observed, it writes `WATCHDOG_SIGNAL_ACCEPTED_NO_CLOSE_AT_DEADLINE`.
Both exit boundedly, make no LLDB-terminal, no-orphan, or 150-second claim,
withhold cleanup permission, and retain the fixed root. Any observed
post-start terminal that is neither exact normal detach nor watchdog terminal is
mechanically classified `POST_START_ABNORMAL_LLDB_TERMINAL` and still permits
independent cleanup because LLDB stream-`close` was observed. Arbitrary,
partial, overlong, non-prefix, duplicate, or post-EOF stdin is rejected/closed
without forwarding. Only one EOF-complete byte-equal C853 buffer is forwarded
once, after accepted C1009 plus its receipt; C1013/C1015 trap stream and
completion-callback errors without satisfying terminality or bypassing settlement.

## Durable evidence and rollback law

C880-C888 finish before any rollback or fixed-root deletion on the seven
terminal-safe branches. They retain the
actual branch receipt, raw controller streams, exact C853 input, LLDB raw
stdout/stderr if session B existed, typed session-B absence if it did not,
spawn/start/terminal/session proof, package transcript, network-scan result,
action/deviation logs, cleanup receipts, and a deterministically sorted durable
hash manifest. Credential/token bytes and raw registration stdout are never
retained. Either no-close diagnostic branch stops after its typed proof: no cleanup,
durable-copy, rollback, permission marker, or fixed-root deletion is claimed.

C889-C897 are attempted independently in order even if a prior rollback step
fails. C898 then compares the exact final eight hashes, requires an exactly
empty frontend status, and requires all named candidate/build/dependency
derivatives absent. Only C898 may create `TEMP_DELETE_ALLOWED`; C899 must see
it before C900. If any restore or validation fails, C900-C901 are forbidden:
the baseline and fixed root remain for diagnosis and the failure is reported.
C902 proves the durable manifest exists after deletion.

Rollback constants, in C797/C1053 order:

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
