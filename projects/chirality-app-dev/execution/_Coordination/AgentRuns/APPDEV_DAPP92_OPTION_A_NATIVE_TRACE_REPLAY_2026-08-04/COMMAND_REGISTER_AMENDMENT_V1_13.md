# Command-register amendment v1.13 — direct local electronDist

Status: `OWNER APPROVED — FROZEN BEFORE ATTEMPT-5 C096`

This immutable adopted copy is byte-for-byte equivalent in operative command
scope to `COMMAND_REGISTER_AMENDMENT_V1_13_PROPOSED.md`. The exact owner token
is transcribed in `OWNER_ATTEMPT5_COMMAND_APPROVAL_ADOPTION.md`.

Attempt 4 consumed its sole C198 retry and terminated. This amendment does not
erase or override that stop and authorizes no cache placement or further C198
invocation.

Attempt 5 executes only:

1. existing C096-C105 and C152-C177;
2. new C210-C215 below;
3. one C198-equivalent package invocation as new C216;
4. existing C179-C184 only if C216 passes with no network attempt; and
5. mandatory existing C185-C195 plus C199-C200 on every terminal path.

Execution cwd is repo root except C213-C216, whose exact cwd is
`projects/chirality-app-dev/frontend`.

| ID | Class | Adopted state | Exact tool/command | Purpose / stop condition |
|---|---|---|---|---|
| C210 | temporary product reconstruction/runtime | OWNER_APPROVED | `/bin/mkdir -p /private/tmp/chirality-dapp92-option-a-20260804/electron-dist` | Create only the run-owned direct-distribution directory. |
| C211 | temporary product reconstruction/runtime | OWNER_APPROVED | `/bin/cp -p /Users/ryan/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip /private/tmp/chirality-dapp92-option-a-20260804/electron-dist/electron-v43.2.0-darwin-arm64.zip` | Copy only the already-local public Electron archive to the exact direct path. |
| C212 | read-only/unprivileged | OWNER_APPROVED | `/usr/bin/shasum -a 256 /private/tmp/chirality-dapp92-option-a-20260804/electron-dist/electron-v43.2.0-darwin-arm64.zip` | Must reproduce `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`; otherwise stop and roll back. |
| C213 | temporary product reconstruction/runtime | OWNER_APPROVED | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/node /Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/proposed/attempt5/apply-local-electron-dist-overlay.mjs` | From exact frontend cwd, apply only the two temporary hash-bound `electronDist` keys. Script SHA-256 `ba5142bfd3e4ee62a48a1acf663862a357b4790b48f66a33e8bd807148ab208b`; it fails closed on either pre/post hash mismatch. |
| C214 | read-only/unprivileged | OWNER_APPROVED | `/usr/bin/shasum -a 256 electron-builder.runtime-helper.json package.json` | From exact frontend cwd, must reproduce overlay hashes `0822414929eed5ebd6c87d21db8c8c55abd991f1b946c009e64de0467c5583af` and `01e93e41dd8c7d90a8308e5a347d6779093f15d9fd2ae02aa4f9743159ad89ea`; otherwise stop and roll back. |
| C215 | read-only/unprivileged | OWNER_APPROVED | `/usr/bin/grep -n 'electronDist' electron-builder.runtime-helper.json package.json` | From exact frontend cwd, bind exactly the two proposed local-path keys; any other match stops execution. |
| C216 | temporary product reconstruction/runtime | OWNER_APPROVED FOR ONE INVOCATION | `/usr/bin/env -i PATH=/Users/ryan/.local/share/mise/installs/node/24/bin:/usr/bin:/bin:/usr/sbin:/sbin HOME=/private/tmp/chirality-dapp92-option-a-20260804/home /Users/ryan/.local/share/mise/installs/node/24/bin/npm run desktop:pack` | One final package invocation only, from exact frontend cwd. No network authority. Stop and roll back on any failure or network attempt. |

The two overlay targets are temporary reconstructed candidate config, not an
accepted product remedy. Their pre-overlay hashes are the exact C165 candidate
hashes; C185-C193 restores/removes all config and generated state on every
path. This amendment adds no cache seed, network, helper/GUI launch, process,
debugger, signal, replay, credential, environment dump, release, Git, Task
Management, foreign-loop, or other authority. C196/C197 remains separate and
unused.
