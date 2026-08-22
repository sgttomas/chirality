# A2-PKG09-LOGIN-PACK-01 return

- Verdict: `BLOCKED_CACHE_MISS_NETWORK_FORBIDDEN`
- Agent: ephemeral generalist Agent 2 `A2-PKG09-LOGIN-PACK-01`
- Parent: `WI-PKG09-LOGIN-STAGING-01`
- Accepted basis / build commit attempted: `1b375af4f1219ecfc00fc2755854aa7fd4220901`
- Branch: `codex/app-post-root-login-proof`
- Node: `v24.18.0`
- npm: `11.16.0`

## Outcome

The one authorized command was run exactly once from the required directory.
The Next and Electron/CLI compilation stages passed, but `electron-builder`
could not package because the required Electron distribution was not locally
cached. It attempted to resolve `github.com` and failed with
`getaddrinfo ENOTFOUND github.com`; the command exited `1`. The sealed brief
forbids network access and dependency install/update, so no escalation or retry
was attempted. No current package, current dependency-boundary verdict, or
current instruction-root-integrity verdict exists from this execution.

## Command evidence

- Command: `npm run desktop:pack`
- Working directory: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend`
- Started: `2026-08-22T03:18:07.539Z`
- Ended: `2026-08-22T03:18:58.307Z`
- Elapsed: `50.768` seconds
- Exit: `1`
- Transcript: `desktop-pack.log`
- Transcript SHA-256: `22defdaf3e9685e92514b7ffce5c4b2792b2475fc23224e289ba112b28d2ed87`

The command emitted `installing native dependencies` as the ordinary
`@electron/rebuild` packaging phase, but a post-run timestamp audit found no
`node_modules` file newer than command start and Git shows no package-lock or
tracked frontend change. No separate install or update command was run.

## Artifact identity and posture

The required absolute path is:

`/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app`

That path exists, but it is **not this run's output**. Its bundle mtime is
`2026-08-20T15:24:07-0600` and executable mtime is
`2026-08-20T15:23:50-0600`, both predating this run. It is therefore retained
only as a pre-existing stale observation and is not eligible for the requested
`PROOF_APP` staging.

Read-only metadata on that stale bundle: bundle identifier
`com.chirality.app`, name `Chirality`, version `2.0.0`, thin `arm64` Mach-O.
`codesign -dvvv` reports an ad-hoc linker signature with no TeamIdentifier;
strict deep verification reports `code has no resources but signature indicates
they must be present`. These observations do not describe a package built from
the current basis and make no signing, release, or reliance claim.

## Integrity evidence

Current source identity is independently observable:

- `agents/AGENT_HELP_HUMAN.md` SHA-256:
  `0285715cbe41ac2c8b7bfd8b6dbd56ad1f0cbb1a970a4f7afed290fc30d1e981`
- Git blob:
  `a9e538c0d9603e18d9884e9f60489be6df8ba1ff`

However, the packaging chain stopped before
`desktop:verify-dependencies` and `instruction-root:integrity`. The retained
`artifacts/harness/instruction-root-integrity/latest/summary.json` is stale:
it was generated `2026-08-20T21:24:08.233Z` for Git SHA
`89758a32634ee6cedbd1dbadf35e3728fb48d2eb` and records the prior
HELP_HUMAN SHA-256
`f0640b092c12f0f847e0d8df2786ca46bdf916f33e3330bdc54e202c788cbde3`.
It must not be represented as current-byte evidence.

## Git and frontend identity

Pre-command porcelain was:

```text
 M projects/chirality-app-dev/execution/_Coordination/_TaskManagement/DRAFT_NOTICE_ROOT_TM-APP-032_SUCCESSOR_IDENTITY_2026-08-02.md
 M projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv
?? projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_POST_ROOT_LOGIN_ENABLEMENT_2026-08-21/
```

Post-command porcelain additionally showed the concurrent Node 2 path
`projects/chirality-app-dev/execution/_Coordination/_TaskManagement/ROW_MAINTENANCE_TM-APP-032_RESCOPE_2026-08-21.md` as untracked. There was no
tracked frontend delta before or after the command, staged or unstaged.

The required proof command was run and produced no output:

```sh
git diff --stat 1b375af4f1219ecfc00fc2755854aa7fd4220901..HEAD -- projects/chirality-app-dev/frontend
```

HEAD remained exactly `1b375af4f1219ecfc00fc2755854aa7fd4220901`.
This proves current HEAD's frontend tree is identical to the attempted build
commit, but does not cure the failed package.

## Forbidden-target containment

Read-only before/after observations were identical:

- `gui/501/com.chirality.runtime`: loaded and running, PID `1301`, program
  `/Users/ryan/dev/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality`, argument
  `--runtime-daemon`.
- `/Users/ryan/Library/LaunchAgents/com.chirality.runtime.plist`: size `1207`,
  mtime `2026-07-24T21:57:59-0600`, SHA-256
  `2ebc556673d7dc1232a9e230a88a75355dec6916ad6c432f707a525b29a6c7bc`.
- `/Users/ryan/.local/bin/chirality`: size `1114`, mtime
  `2026-08-20T15:26:36-0600`, SHA-256
  `f16bc2ba9228b5321deb9c66ba9526aa60fbe3bb02179d32fd66ce1de208384a`.

No GUI launch, proof `prepare` or `capture`, bootstrap, kickstart, `launchctl`
mutation, operator plist/launcher write, proof label, artifact-proof label,
signing, notarization, distribution, staging, commit, push, or PR action
occurred.

## Writes and acceptance matrix

Persistent writes by this executor are contained to:

- `executor/desktop-pack.log`
- `executor/RETURN.md`

The failed command regenerated only ignored build content in `.next/`,
`dist-electron/`, and `dist-runtime/`. No file under `dist/` or `node_modules`
had a timestamp newer than command start. No tracked source path changed.

| Acceptance check | Result |
| --- | --- |
| Exact build commit / branch / versions captured | PASS |
| Pre/post Git status captured; no tracked frontend write | PASS |
| Forbidden operator targets unchanged | PASS |
| One exact authorized package command only | PASS |
| Current unsigned `Chirality.app` produced | **BLOCKED** — Electron distribution cache miss; network forbidden |
| Current dependency-boundary check | **NOT RUN** — command short-circuited |
| Current instruction-root integrity and HELP_HUMAN packaged hash | **NOT RUN** — command short-circuited |
| Frontend diff-stat proof empty | PASS |

## Required follow-on

Node 3 cannot stage `PROOF_APP`, `PROOF_REVISION`, `PROOF_ROOT`, or
`PROOF_LABEL` from this attempt. A fresh execution of the same package command
requires the Electron `43.2.0` arm64 distribution to be present in an approved
local cache, or separate owner authorization that changes the sealed no-network
boundary. This executor does not request or imply that authorization.
