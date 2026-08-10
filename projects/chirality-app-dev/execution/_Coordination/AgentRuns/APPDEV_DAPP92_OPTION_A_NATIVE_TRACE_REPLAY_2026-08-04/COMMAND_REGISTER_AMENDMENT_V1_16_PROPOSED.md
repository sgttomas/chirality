# Proposed command-register amendment v1.16 — Attempt-8 real runtime

Status: `PROPOSED — OWNER COMMAND APPROVAL REQUIRED — NOT EXECUTED`

Attempt 7 passed only the mock two-session protocol. Fresh verifier SHA-256
`1546dc33b24bbbd86d43d6b547b404113267e594b4eb6f0247c59455ad13ce6f`
permits preparation of this separately owner-gated packet and no runtime act.
C196/C197 remain separately owner-approved and unused; their exact bytes and
150-second/one-direct-child constraints are preserved below. This proposal
does not infer that their prior approval authorizes any new command.

The proposed scripts were created as packet bytes only and were neither run
nor syntax-checked:

- `proposed/attempt8/real-runtime-controller.mjs` — SHA-256
  `11a97d620e7f742e04d91418a1bbbeec2d1ef20b43e48596b75900c8cba4bd2f`;
- `proposed/attempt8/real-second-session-sentinel.mjs` — SHA-256
  `a75b91299cb20f7daa2154a2ba9b36e4f71235ed634bfe81f80d16d7874d4242`;
- `proposed/attempt8/real-runtime-fallback-cleanup.mjs` — SHA-256
  `ed577526d8d1122c24b96db1f62e4e796341bce27878145498288f94a1c19fec`.

Unless a row says `frontend`, cwd is repo root
`/Users/ryan/.codex/worktrees/7388/chirality`. Every new row is held for one
Attempt-8 invocation. Any drift, nonzero result outside an explicitly allowed
existence probe, unexpected output, network attempt, special-authority prompt
beyond C196/C197, PID/schema/state/timing mismatch, or cleanup failure stops
the success path and enters the ordered detach/quiescence/rollback graph.

## Basis, one reconstruction, and one package invocation

| ID | Exact command/control | Cwd and binding / stop condition |
|---|---|---|
| C245 | `/usr/bin/shasum -a 256 projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-92_PACKET_NATIVE_SIGNAL_TRACE_AND_REPLAY_2026-08-04.md projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-92_RULING_BOUNDED_NATIVE_SIGNAL_TRACE_AND_SEALED_REPLAY_2026-08-04.md projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_RESUME_R3_2026-08-04/instances/A2-DAPP88-R3-VERIFY-02/RETURN.md projects/chirality-app-dev/chirality.project.json projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt5/apply-local-electron-dist-overlay.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8/real-runtime-controller.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8/real-second-session-sentinel.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8/real-runtime-fallback-cleanup.mjs` | Must reproduce the packet/ruling/R3, manifest `5a797770…fdc04`, LLDB `720ad198…45f8`, overlay `ba5142bf…208b`, and three hashes above. |
| C246 | `/bin/test ! -e /private/tmp/chirality-dapp92-option-a-20260804` | Fixed root must be absent. |
| C247 | `/bin/mkdir -p /private/tmp/chirality-dapp92-option-a-20260804/home /private/tmp/chirality-dapp92-option-a-20260804/user /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-runtime /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests /private/tmp/chirality-dapp92-option-a-20260804/protocol` | Create only fixed run-owned paths. |
| C248 | `/bin/cp -p projects/chirality-app-dev/frontend/electron/cli-launcher.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/cli-launcher.ts` | Freeze baseline byte. |
| C249 | `/bin/cp -p projects/chirality-app-dev/frontend/electron/main.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/main.ts` | Freeze baseline byte. |
| C250 | `/bin/cp -p projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/runtime-control-ipc.ts` | Freeze baseline byte. |
| C251 | `/bin/cp -p projects/chirality-app-dev/frontend/package.json /private/tmp/chirality-dapp92-option-a-20260804/baseline/package.json` | Freeze baseline byte. |
| C252 | `/bin/cp -p projects/chirality-app-dev/frontend/scripts/build-electron.mjs /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts/build-electron.mjs` | Freeze baseline byte. |
| C253 | `/bin/cp -p projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/cli-launcher.test.ts` | Freeze baseline byte. |
| C254 | `/bin/cp -p projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/runtime-control-ipc.test.ts` | Freeze baseline byte. |
| C255 | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/cli-launcher.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/main.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/runtime-control-ipc.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/package.json projects/chirality-app-dev/frontend/package-lock.json /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts/build-electron.mjs /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/cli-launcher.test.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/runtime-control-ipc.test.ts` | Must reproduce all eight D-APP-89 hashes in `SOURCE_MANIFEST.md`. |
| C256 | `/bin/test ! -e projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json` | Addition absent. |
| C257 | `/bin/test ! -e projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts` | Addition absent. |
| C258 | `/bin/test ! -e projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts` | Addition absent. |
| C259 | `/bin/test ! -e projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs` | Addition absent. |
| C260 | `/bin/test ! -e projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts` | Addition absent. |
| C261 | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron-builder.runtime-helper.json projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json` | Exact candidate byte. |
| C262 | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/cli-launcher.ts projects/chirality-app-dev/frontend/electron/cli-launcher.ts` | Exact candidate byte. |
| C263 | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/main.ts projects/chirality-app-dev/frontend/electron/main.ts` | Exact uninstrumented candidate byte. |
| C264 | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/runtime-control-ipc.ts projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts` | Exact candidate byte. |
| C265 | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/runtime-helper-entry.ts projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts` | Exact candidate byte. |
| C266 | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/electron/runtime-helper-path.ts projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts` | Exact candidate byte. |
| C267 | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/package.json projects/chirality-app-dev/frontend/package.json` | Exact candidate byte; lockfile unchanged. |
| C268 | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/scripts/build-electron.mjs projects/chirality-app-dev/frontend/scripts/build-electron.mjs` | Exact candidate byte. |
| C269 | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/scripts/embed-runtime-helper.mjs projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs` | Exact candidate byte. |
| C270 | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/cli-launcher.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts` | Exact candidate test. |
| C271 | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/runtime-control-ipc.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts` | Exact candidate test. |
| C272 | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/runtime-helper-packaging.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts` | Exact candidate test. |
| C273 | `/usr/bin/shasum -a 256 projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json projects/chirality-app-dev/frontend/electron/cli-launcher.ts projects/chirality-app-dev/frontend/electron/main.ts projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts projects/chirality-app-dev/frontend/package.json projects/chirality-app-dev/frontend/scripts/build-electron.mjs projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts projects/chirality-app-dev/frontend/package-lock.json` | Must reproduce all 12 R3 candidate hashes plus lockfile. |
| C274 | `/usr/bin/ditto /Users/ryan/dev/chirality/projects/chirality-app-dev/frontend/node_modules projects/chirality-app-dev/frontend/node_modules` | Exact-lock local dependency copy; no install/network. |
| C275 | `/bin/rm -rf projects/chirality-app-dev/frontend/node_modules/@chirality/engine-pi-omlx projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-cli projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-client projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-contracts projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-core projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-daemon` | Remove only six copied Root-owned entries. |
| C276 | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/engine-pi-omlx projects/chirality-app-dev/frontend/node_modules/@chirality/engine-pi-omlx` | Exact R3 projection. |
| C277 | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/cli projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-cli` | Exact R3 projection. |
| C278 | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/client projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-client` | Exact R3 projection. |
| C279 | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/contracts projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-contracts` | Exact R3 projection. |
| C280 | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/core projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-core` | Exact R3 projection. |
| C281 | `/bin/ln -s /Users/ryan/dev/chirality/runtime/packages/daemon projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-daemon` | Exact R3 projection. |
| C282 | `/bin/ls -ld projects/chirality-app-dev/frontend/node_modules/@chirality/engine-pi-omlx projects/chirality-app-dev/frontend/node_modules/@chirality/harness-contract projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-cli projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-client projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-contracts projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-core projects/chirality-app-dev/frontend/node_modules/@chirality/runtime-daemon` | Bind six symlinks plus copied facade. |
| C283 | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm test -- src/__tests__/electron/desktop-daemon-posture.test.ts src/__tests__/electron/runtime-control-ipc.test.ts src/__tests__/electron/cli-launcher.test.ts src/__tests__/electron/runtime-helper-packaging.test.ts src/__tests__/electron/desktop-cli-single-daemon-integration.test.ts` | `frontend`; expected actual 4 files/30 tests, not historical 5/32. |
| C284 | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run typecheck` | `frontend`. |
| C285 | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run build` | `frontend`. |
| C286 | `/bin/mkdir -p /private/tmp/chirality-dapp92-option-a-20260804/electron-dist` | Exact local distribution directory. |
| C287 | `/bin/cp -p /Users/ryan/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip /private/tmp/chirality-dapp92-option-a-20260804/electron-dist/electron-v43.2.0-darwin-arm64.zip` | Copy only accepted public archive. |
| C288 | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/electron-dist/electron-v43.2.0-darwin-arm64.zip` | Must equal `ad4a0ae3…fe28`. |
| C289 | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt5/apply-local-electron-dist-overlay.mjs` | `frontend`; exact script hash and pre/post hashes gate two temporary keys. |
| C290 | `/usr/bin/shasum -a 256 electron-builder.runtime-helper.json package.json` | `frontend`; require `08224149…83af` and `01e93e41…89ea`. |
| C291 | `/usr/bin/grep -n electronDist electron-builder.runtime-helper.json package.json` | `frontend`; exactly two matches. |
| C292 | `/bin/sh -c 'exec /usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run desktop:pack > /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-package.stdout-stderr.txt 2>&1'` | `frontend`; sole `desktop:pack` invocation. Stop on failure or any network-attempt text. |
| C293 | `/usr/bin/shasum -a 256 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service' 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Resources/app.asar' 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist' 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality' 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar'` | Bind package hashes before use; expected Attempt-5 identities. |
| C294 | `/usr/bin/plutil -p 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist'` | Require helper identity and `LSUIElement=true`. |
| C295 | `/usr/bin/plutil -p 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Info.plist'` | Require GUI identity. |
| C296 | `/usr/bin/find 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app' -type l -print` | Bind helper symlink paths. |
| C297 | `/usr/bin/find 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app' -type l -exec /usr/bin/readlink '{}' ';'` | Require 14 relative targets. |
| C298 | `/usr/bin/diff -qr 'projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app' 'projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Library/LoginItems/Chirality Runtime Service.app'` | Require exit 0; documented loop diagnostics only. |

## Two-session runtime, inherited LLDB, replay, and evidence

| ID | Exact command/control | Binding / stop condition |
|---|---|---|
| C299 | Start PTY/session A: `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8/real-runtime-controller.mjs` | Controller hash must match. It alone creates the stale helper, exact final direct-child helper, public readiness/recovery evidence, public registration, GUI, 28.0/102.0 timers, snapshots, first `/bin/kill -TERM`, 80×0.1-second polls, and owned-process cleanup. Retain session A. |
| C300 | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/protocol/controller.json` | Session B, only after C299 emits exact `ATTACH_READY`; bind positive `<EXACT_HELPER_PID>` and controller-record hash. No PID search. |
| C335 | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8/real-second-session-sentinel.mjs attach-started <EXACT_HELPER_PID>` | Immediately before C196, using only the PID bound by C300. This closes the pre-trace-ready detach race: after this sentinel exists, session A cannot clean up until the same-PID detached terminal sentinel exists. |
| C196 | `/usr/bin/xcrun lldb --batch -p <EXACT_HELPER_PID> -s /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt` | **Inherited prior approval exactly.** Start PTY/session B with the numeric direct-child PID from C299/C300 only. One PID, enumerated breakpoints/backtraces, 150-second absolute maximum. No other debugger authority. |
| C301 | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8/real-second-session-sentinel.mjs trace-ready <EXACT_HELPER_PID>` | Only after C196 output proves all enumerated breakpoint commands loaded and target resumed; exact PID substitution from C300. |
| C302 | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/protocol/trace-ready.json` | Bind sentinel before GUI. |
| C303 | Poll only existing C299 session A without bytes until it emits exact `SIGNAL_ARMED`, with deadline 132 seconds after its `ATTACH_READY` output | No input/interrupt; stop on unexpected output or early terminal state. |
| C304 | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/protocol/signal-armed.json` | Bind exact helper PID and signal target. |
| C305 | Poll only existing C196 PTY/session B without bytes; require it remains live, attached to the same PID, and has emitted no unexpected debugger/security/credential output | Immediately before trace-live acknowledgment; no bytes. |
| C306 | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8/real-second-session-sentinel.mjs trace-live <EXACT_HELPER_PID>` | Same PID; only after C305 and C304. |
| C307 | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/protocol/trace-live.json` | Bind pre-signal tracer-live sentinel. |
| C308 | Poll only existing C299 session A without bytes until it emits the exact replay-terminal line, maximum 12 seconds after the signal target | Require one SIGTERM, contact-to-signal scheduler value in `[102000,102100)` ms, and at most 80 recorded 0.1-second polls. No bytes. |
| C309 | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/protocol/replay-terminal.json` | Bind replay result before detach. |
| C197 | On only the existing C196 PTY: send interrupt byte `\u0003`, then exact debugger commands `process detach\nquit\n` | **Inherited prior approval exactly.** Invoke after C308 or on any post-C196 stop, and before the 150-second C196 bound. No kill/security change. |
| C310 | Poll only the existing C196 PTY/session B without further bytes until terminal; hard deadline is 150 seconds after C196 started | Require terminal state before detach sentinel or cleanup. |
| C311 | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8/real-second-session-sentinel.mjs detached <EXACT_HELPER_PID>` | Only after C310. If C196 never began, substitute phase `no-attach-terminal` only after recording that fact and session A's exact PID record. |
| C312 | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/protocol/detached.json` | Bind detach/quiescence signal. |
| C313 | Poll only existing C299 session A without bytes until terminal, maximum 30 seconds after C311 | Require terminal controller state; no cleanup may race it. |
| C314 | Start `/usr/bin/base64 -D -o /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-runtime/lldb-transcript.txt`; send exactly `<BASE64_OF_BYTE_EXACT_C196_C197_PTY_OUTPUT>` followed by EOF | Dynamic placeholder may be derived only from the complete C196/C197 tool-return bytes, with no edit/summary. No target memory/environment/credential bytes are permitted. |
| C315 | `/bin/mkdir -p /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime` | Create only durable run-local evidence directory after both sessions terminal. |
| C316 | `/usr/bin/ditto /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-runtime /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime` | Copy only sanitized/raw approved trace/runtime evidence after quiescence. |
| C317 | `/usr/bin/find /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime -type f -exec /usr/bin/shasum -a 256 '{}' ';'` | Bind every durable evidence file. |
| C318 | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8/real-runtime-fallback-cleanup.mjs` | Mandatory idempotent exact-PID backstop only after C310 and C313. It reads only controller/replay public PID records; no process census. |
| C319 | `/usr/bin/find /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-runtime -type f -name '*cleanup.json' -exec /usr/bin/shasum -a 256 '{}' ';'` | Bind exactly the cleanup files that exist; require at least one cleanup receipt and record any missing expected receipt without inventing a file. |

The controller's internal commands are part of C299's frozen hash and separately
owner-gated by this packet: two `/usr/bin/env -i ... <HELPER> --runtime-daemon`
direct-child launches (one stale setup, one traced final helper); one exact
stale-helper `/bin/kill -KILL`; one `/usr/bin/env -i ... <GUI>
--user-data-dir=<isolated-user>` launch; one newly sealed public CLI command
using the packaged GUI executable and `Contents/Resources/runtime-cli/
chirality-cli.mjs` with `ELECTRON_RUN_AS_NODE=1`, `project register`, the exact
manifest, `--approved-by D-APP-92 --approval-reference D-APP-92-OPTION-A
--json`; exact-PID `ps` without command/environment, `lsof`, `stat`, and
`shasum`; one `/bin/kill -TERM <EXACT_HELPER_PID>`; up to 80 `/bin/kill -0`
polls separated by 0.1 seconds; and exact-PID GUI/helper cleanup. Registration
stdout is parsed in memory and only `projectId`, `clientId`, `manifestHash`, and
exit status are retained; `tokenFile` and raw stdout are discarded. This
command is source-derived and newly sealed, not claimed as byte-complete
historical command recovery.

## Mandatory product/runtime rollback

Rows C320-C334 run after any C247-or-later terminal path, subject to C310/C313
quiescence whenever C196/C299 began. Evidence is copied before removal when
safe; an unproved live debugger/controller blocks C318 and C333 rather than
racing cleanup.

| ID | Exact command | Stop condition |
|---|---|---|
| C320 | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/cli-launcher.ts projects/chirality-app-dev/frontend/electron/cli-launcher.ts` | Restore baseline. |
| C321 | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/main.ts projects/chirality-app-dev/frontend/electron/main.ts` | Restore baseline. |
| C322 | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/runtime-control-ipc.ts projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts` | Restore baseline. |
| C323 | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/package.json projects/chirality-app-dev/frontend/package.json` | Restore baseline. |
| C324 | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts/build-electron.mjs projects/chirality-app-dev/frontend/scripts/build-electron.mjs` | Restore baseline. |
| C325 | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/cli-launcher.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts` | Restore baseline. |
| C326 | `/bin/cp -p /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/runtime-control-ipc.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts` | Restore baseline. |
| C327 | `/bin/rm -f projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts` | Remove five candidate additions. |
| C328 | `/bin/rm -rf projects/chirality-app-dev/frontend/node_modules projects/chirality-app-dev/frontend/dist projects/chirality-app-dev/frontend/dist-runtime-helper projects/chirality-app-dev/frontend/dist-electron projects/chirality-app-dev/frontend/dist-runtime projects/chirality-app-dev/frontend/.next` | Remove named dependency/build derivatives. |
| C329 | `/usr/bin/shasum -a 256 projects/chirality-app-dev/frontend/electron/cli-launcher.ts projects/chirality-app-dev/frontend/electron/main.ts projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts projects/chirality-app-dev/frontend/package.json projects/chirality-app-dev/frontend/package-lock.json projects/chirality-app-dev/frontend/scripts/build-electron.mjs projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts` | Must reproduce eight governed baseline/lock hashes. |
| C330 | `/usr/bin/git status --short --untracked-files=all -- projects/chirality-app-dev/frontend` | Must emit zero bytes. |
| C331 | `/bin/test ! -e projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json` | Prove addition absent. |
| C332 | `/bin/test ! -e projects/chirality-app-dev/frontend/node_modules` | Prove dependency projection absent. |
| C333 | `/bin/rm -rf /private/tmp/chirality-dapp92-option-a-20260804` | Only after evidence freeze and proven C310/C313 quiescence; remove exact fixed root. |
| C334 | `/bin/test ! -e /private/tmp/chirality-dapp92-option-a-20260804` | Prove runtime-root removal. |

## Exact timing and causal fences

- Final-helper ready is the first bounded poll observing both `control.sock`
  and `control.sock.owner.json` with exact owner schema and direct-child PID.
- GUI spawn is scheduled at ready-monotonic + `28000` ms and fails closed
  unless observed in `[28000,28100)` ms.
- Authenticated contact is the timestamped `runtime.connectivity.bound` event
  after public registration; first SIGTERM is scheduled at contact-monotonic +
  `102000` ms and fails closed if the trace-live sentinel misses the deadline.
- The first ordinary SIGTERM is sent once. The credited window contains at
  most 80 exact existence polls separated by 0.1 seconds and stops early only
  on exit. No second signal receives acceptance credit.
- C196 must be attached and resumed before the trace-ready sentinel and still
  live immediately before trace-live. C197 and both-session terminal proof
  precede evidence copy, fallback cleanup, product rollback, and root removal.
- Any unresolved symbol remains `UNKNOWN`; missing breakpoint output is not a
  zero inference. A diagnostic result cannot itself select or implement a
  remedy or accept D-APP-88.

## Exclusions

No network, cache seed, owner-HOME/keychain read, token/credential value,
memory or environment dump, broad process census, other debugger, DTrace,
`fs_usage`, privilege/entitlement/security/signing/admin change, product
remedy, release, reliance, Git mutation, Task Management, foreign-loop, or
other authority is proposed. Generated packages are diagnostic derivatives
and must be removed. D-APP-88 and DEL-09-04 remain open; TM-APP-036 remains
unfired.
