# Proposed command-register amendment v1.17 — Attempt-8 R2 repair

Status: `PROPOSED — OWNER COMMAND APPROVAL REQUIRED — NOT EXECUTED`

This packet supersedes v1.16 for decision purposes without modifying its
rejected historical bytes. It answers fresh adversarial verifier R2 SHA-256
`ebb81fb33524eb68ef0a3435d5e594a17f13044420330570cbcf9b114955a2d8`.
Nothing in this packet was run or syntax-checked.

Frozen scripts:

- controller R2: `6da4821fb04550af01e4deaf0c05c398f93267f1c75e7c764f660e50c8c02059`;
- same-PID sentinel R2: `30f8bd60858a4c86fb7cb8ca0a4350b41b8c69ac78116c1d9fbcb2768c726213`;
- cleanup verifier R2: `690b1b10d0afa48fc9963d4e4722121032880b15b8eb97c5f53a5be2a298ba26`.

Unless a row says `frontend`, cwd is repo root
`/Users/ryan/.codex/worktrees/7388/chirality`. C196/C197 retain their exact
previously approved bytes and separate authority.

## Pre-mutation, reconstruction, and package

| ID | Exact command/control | Gate |
|---|---|---|
| C336 | `/usr/bin/shasum -a 256 projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/reviews/A2_ATTEMPT8_PACKET_FRESH_ADVERSARIAL_VERIFIER_RETURN_R2.md projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r2/real-runtime-controller-r2.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r2/real-second-session-sentinel-r2.mjs projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r2/real-runtime-cleanup-verifier-r2.mjs` | Require the four hashes above. |
| C337 | `/bin/test ! -e /private/tmp/chirality-dapp92-option-a-20260804` | Fixed root absent. |
| C338 | `/bin/mkdir -p /private/tmp/chirality-dapp92-option-a-20260804/home /private/tmp/chirality-dapp92-option-a-20260804/user /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-runtime /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests /private/tmp/chirality-dapp92-option-a-20260804/protocol` | Root creation only; no product mutation. |
| C339 | `/bin/cp -p projects/chirality-app-dev/frontend/electron/cli-launcher.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/cli-launcher.ts` | Baseline 1/7. |
| C340 | `/bin/cp -p projects/chirality-app-dev/frontend/electron/main.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/main.ts` | Baseline 2/7. |
| C341 | `/bin/cp -p projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/runtime-control-ipc.ts` | Baseline 3/7. |
| C342 | `/bin/cp -p projects/chirality-app-dev/frontend/package.json /private/tmp/chirality-dapp92-option-a-20260804/baseline/package.json` | Baseline 4/7. |
| C343 | `/bin/cp -p projects/chirality-app-dev/frontend/scripts/build-electron.mjs /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts/build-electron.mjs` | Baseline 5/7. |
| C344 | `/bin/cp -p projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/cli-launcher.test.ts` | Baseline 6/7. |
| C345 | `/bin/cp -p projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/runtime-control-ipc.test.ts` | Baseline 7/7. |
| C346 | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/cli-launcher.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/main.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/electron/runtime-control-ipc.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/package.json projects/chirality-app-dev/frontend/package-lock.json /private/tmp/chirality-dapp92-option-a-20260804/baseline/scripts/build-electron.mjs /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/cli-launcher.test.ts /private/tmp/chirality-dapp92-option-a-20260804/baseline/tests/runtime-control-ipc.test.ts` | Require all eight D-APP-89 hashes before mutation. |
| C347 | `/usr/bin/touch /private/tmp/chirality-dapp92-option-a-20260804/MUTATION_AUTHORIZED` | Mechanical branch marker; first product mutation follows. |
| C348 | Run, in listed order, the exact `cp -p` commands from v1.16 C261-C272 | Reconstruct all 12 hash-bound candidate files once; these command bytes are incorporated verbatim, not authorized by v1.16. |
| C349 | `/usr/bin/shasum -a 256 projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json projects/chirality-app-dev/frontend/electron/cli-launcher.ts projects/chirality-app-dev/frontend/electron/main.ts projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts projects/chirality-app-dev/frontend/electron/runtime-helper-entry.ts projects/chirality-app-dev/frontend/electron/runtime-helper-path.ts projects/chirality-app-dev/frontend/package.json projects/chirality-app-dev/frontend/scripts/build-electron.mjs projects/chirality-app-dev/frontend/scripts/embed-runtime-helper.mjs projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts projects/chirality-app-dev/frontend/package-lock.json` | Require R3 candidate hashes plus unchanged lock. |
| C350 | `/usr/bin/ditto /Users/ryan/dev/chirality/projects/chirality-app-dev/frontend/node_modules projects/chirality-app-dev/frontend/node_modules` | Local exact-lock dependency copy; no network/install. |
| C351 | Run, in listed order, exact v1.16 commands C275-C281 | Remove only six copied Root packages and install the six exact local symlinks. |
| C352 | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm test -- src/__tests__/electron/desktop-daemon-posture.test.ts src/__tests__/electron/runtime-control-ipc.test.ts src/__tests__/electron/cli-launcher.test.ts src/__tests__/electron/runtime-helper-packaging.test.ts src/__tests__/electron/desktop-cli-single-daemon-integration.test.ts` | `frontend`; local tests. |
| C353 | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run typecheck` | `frontend`. |
| C354 | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run build` | `frontend`. |
| C355 | Run, in listed order, exact v1.16 commands C286-C291 | Prepare and hash-check the local Electron archive and two-config overlay; no network/cache seed. |
| C356 | `/bin/sh -c 'exec /usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run desktop:pack > /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-package.stdout-stderr.txt 2>&1'` | `frontend`; sole package invocation. |
| C357 | `/usr/bin/grep -E -i 'https?://|download|fetch|network|ECONN|ENET|EAI_AGAIN|registry|proxy|TLS' /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-package.stdout-stderr.txt` | Must return status 1 and zero bytes. Status 0 or >1 blocks every runtime row. |
| C358 | Run, in listed order, exact v1.16 commands C293-C298 | Bind five package hashes, identities, relative symlinks, and embedded-helper equality. |

## Runtime, trace, evidence, and rollback

| ID | Exact command/control | Gate |
|---|---|---|
| C359 | Start session A: `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r2/real-runtime-controller-r2.mjs` | Retain PTY. Controller hash exact. |
| C360 | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/protocol/controller.json` | Bind direct-child PID, live identity, ready time, replay deadline, detach deadline. |
| C361 | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r2/real-second-session-sentinel-r2.mjs attach-started <EXACT_HELPER_PID>` | Immediately before C196; mechanically re-proves PID, PPID, executable text, command, and start identity. |
| C196 | `/usr/bin/xcrun lldb --batch -p <EXACT_HELPER_PID> -s /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt` | Inherited prior approval exactly; one bound direct-child PID, 150-second maximum. |
| C362 | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r2/real-second-session-sentinel-r2.mjs trace-ready <EXACT_HELPER_PID>` | Only after LLDB breakpoints loaded and resumed; repeats live identity. |
| C363 | Poll only session A without bytes until exact `SIGNAL_ARMED`; absolute deadline from controller record | The contact window is five 0.1-second polls. |
| C364 | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r2/real-second-session-sentinel-r2.mjs trace-live <EXACT_HELPER_PID>` | Only while C196 PTY is live; repeats identity immediately before first SIGTERM. |
| C365 | Poll session A without bytes to replay terminal; require ready+139.5 seconds maximum | Preserves 28.0 seconds, 102.0 seconds, and 80×0.1 seconds. |
| C197 | On only the existing C196 PTY: send interrupt byte `\u0003`, then exact debugger commands `process detach\nquit\n` | Inherited prior approval exactly. |
| C366 | Poll C196 PTY without bytes until terminal; require terminal before controller ready+148.0 seconds | Strictly inside the 150-second inherited cap with at least 2.0 seconds slack from earliest possible attach. |
| C367 | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r2/real-second-session-sentinel-r2.mjs detached <EXACT_HELPER_PID>` | Only after C366. If C196 never started, `no-attach-terminal` is allowed only when attach-started is absent. |
| C368 | Poll session A without bytes until terminal; require cleanup status `ALL_CONTROLLER_CHILDREN_REAPED` | No static-PID cleanup follows. |
| C369 | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt8-r2/real-runtime-cleanup-verifier-r2.mjs` | Receipt verification only; performs no signal, PID probe, or process inspection. |
| C370 | `/bin/mkdir -p /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r2` | Durable evidence target after cleanup receipts exist. |
| C371 | `/usr/bin/ditto /private/tmp/chirality-dapp92-option-a-20260804/evidence/attempt8-runtime /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r2` | Copy all evidence including controller cleanup and cleanup-verifier receipts. |
| C372 | If `MUTATION_AUTHORIZED` exists, run exact v1.16 C320-C332; otherwise run no product restore/removal command | Post-mutation exact baseline rollback versus pre-mutation root-only branch. |
| C373 | `/bin/rm -rf /private/tmp/chirality-dapp92-option-a-20260804` | After C368-C372 only. On any C338-C346 stop, this is the sole cleanup command and is valid without baseline files. |
| C374 | `/bin/test ! -e /private/tmp/chirality-dapp92-option-a-20260804` | Prove fixed-root removal. |

## Exact internal executable/API inventory

C359's frozen controller invokes only: `/usr/bin/env -i PATH=<exact NODE_PATH>
HOME=<fixed HOME> CHIRALITY_USER_DATA=<fixed USER_DATA>
CHIRALITY_SKIP_CLI_LAUNCHER=1 <HELPER> --runtime-daemon` exactly twice;
the same `/usr/bin/env -i ... <GUI> --user-data-dir=<fixed USER_DATA>` once;
`/usr/bin/env -i PATH=<exact NODE_PATH> HOME=<fixed HOME>
CHIRALITY_USER_DATA=<fixed USER_DATA> ELECTRON_RUN_AS_NODE=1 <GUI> <CLI>
project register <MANIFEST> --approved-by D-APP-92 --approval-reference
D-APP-92-OPTION-A --json` once; exact-PID `/bin/ps -o pid= -p <PID>`,
`ppid=`, `lstart=`, and `comm=` plus `/usr/sbin/lsof -a -p <PID> -d txt
-Fn` for identity; the bounded snapshot commands `/bin/ps -o
pid=,ppid=,pgid=,state=,etime= -p <HELPER_PID>,<GUI_PID>`,
`/usr/sbin/lsof -nP -p <HELPER_PID> -a -U`, `/usr/sbin/lsof -nP -p
<HELPER_PID> -a -iTCP`, `/usr/bin/stat -f %N|%i|%p|%u|%g|%z <SOCKET>
<OWNER>`, and `/usr/bin/shasum -a 256 <five exact package paths>`.

Signals are only controller-owned Node `ChildProcess.kill`: stale-helper
`SIGKILL`, final-helper first `SIGTERM`, GUI cleanup first `SIGTERM`, and
bounded still-live owned-handle cleanup `SIGKILL`. Every call is preceded
immediately by PID/PPID/start/comm/lsof-text identity and live exit guards.
The controller races unexpected child exit against every readiness, sentinel,
timer, registration, and contact wait. C361/C362/C364 invoke only the same
five exact-PID identity commands. C369 invokes no executable or child process.

No network, credential value, memory/environment dump, broad process census,
static-PID signal, other debugger/privilege/security/signing/admin, product
remedy, acceptance, release, reliance, Git, Task Management, foreign-loop, or
other authority is proposed.
