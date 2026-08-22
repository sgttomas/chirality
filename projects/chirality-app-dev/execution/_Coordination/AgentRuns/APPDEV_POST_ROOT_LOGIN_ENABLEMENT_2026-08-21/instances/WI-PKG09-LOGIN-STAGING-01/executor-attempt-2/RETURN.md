# A2-PKG09-LOGIN-PACK-02 return

- Verdict: `PASS`
- Agent: fresh ephemeral generalist Agent 2 `A2-PKG09-LOGIN-PACK-02`
- Parent: `WI-PKG09-LOGIN-STAGING-01`
- Accepted basis / exact build commit:
  `1b375af4f1219ecfc00fc2755854aa7fd4220901`
- Branch: `codex/app-post-root-login-proof`
- Node: `v24.18.0`
- npm: `11.16.0`

## Outcome

The exact authorized command `npm run desktop:pack` ran from
`/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend`
with narrowly escalated network access for Electron Builder's locked Electron
`43.2.0` arm64 artifact. It exited `0`. The package is current, the packaged
dependency boundary reports `PASS`, and instruction-root integrity reports
`pass` for the exact build commit and current post-#602 HELP_HUMAN bytes.

No install or alternate package command ran. No package, dependency, lockfile,
or tracked frontend byte changed. The only network use observed in the command
transcript was Electron Builder downloading and extracting the pinned Electron
artifact.

## Command evidence

- Command: `npm run desktop:pack`
- Exit: `0`
- Tool-reported wall time: approximately `58.016` seconds across the initial
  execution yield and completion wait.
- Completion anchor: instruction-root summary `generatedAt`
  `2026-08-22T03:25:09.387Z`.
- Transcript: `desktop-pack.log` (a faithful stage/verdict/path rendering; the
  non-fatal, very long duplicate-dependency diagnostic list is explicitly
  summarized rather than reproduced).
- Transcript SHA-256:
  `21c5c0ed2f1aeb077169837bc246ea0f311b5fc33952f71ce89fc82845e528e5`.
- Electron Builder: `26.15.3`; target Electron: `43.2.0`; platform/architecture:
  `darwin` / `arm64`; output mode: app directory, publishing disabled.
- Builder explicitly emitted `downloaded label=electron progress=100%`,
  successful extraction to `dist/mac-arm64`, and skipped macOS application
  code signing because `CSC_IDENTITY_AUTO_DISCOVERY=false`.

The ordinary `@electron/rebuild` phase emitted `installing native
dependencies`; no separate dependency installation command was run. Manifest
identity was unchanged before/after:

| File | SHA-256 before | SHA-256 after |
| --- | --- | --- |
| `frontend/package.json` | `25dcd056cf72dc807b65fb33dabaa4a03b5ea13f66dcb6779f51d3969cc2a1d8` | same |
| `frontend/package-lock.json` | `717d541fe6ee090aae79d4a386bbde1c8ff6ee136a50242d956500d76e80a458` | same |

## Current app identity and posture

Absolute app path:

`/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app`

The command replaced the prior package observation with current output: app
bundle mtime `2026-08-21 21:25:08 -0600`; main executable mtime
`2026-08-21 21:24:52 -0600`.

Read-only metadata:

- `CFBundleIdentifier`: `com.chirality.app`
- `CFBundleDisplayName` / `CFBundleName`: `Chirality`
- `CFBundleShortVersionString` / `CFBundleVersion`: `2.0.0`
- `LSMinimumSystemVersion`: `15.0.0`
- Main executable: thin `Mach-O 64-bit executable arm64`; `lipo -archs`
  reports only `arm64`.
- Electron Builder skipped application signing. Read-only `codesign -dvvv`
  identifies the main executable's linker-produced ad-hoc signature
  (`flags=adhoc,linker-signed`, `Signature=adhoc`, no `TeamIdentifier`). Strict
  deep bundle verification returns `code has no resources but signature
  indicates they must be present`. This is recorded as the expected local
  unsigned/adhoc posture, not a signing, distribution, release, or reliance
  claim.

## Packaged dependency boundary

`desktop:verify-dependencies` returned `PASS`:

- app.asar:
  `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar`
- monorepo-local package entries: `0`
- forbidden development packages: none
- required packages present: `@anthropic-ai/claude-agent-sdk`,
  `@earendil-works/pi-coding-agent`, `next`
- packaged runtime source proof: `PASS` (`184` desktop sources, `15` CLI
  sources, all enumerated required desktop and CLI sources present)
- failures: none

## Current instruction-root identity

Summary:

`/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`

- Summary SHA-256:
  `1028e49effe50da36cef27e7d2e05a5fcf1dc0369bc418f3c05e683c4d61cd82`
- Summary `generatedAt`: `2026-08-22T03:25:09.387Z`
- Summary `status`: `pass`
- Summary `gitSha`: `1b375af4f1219ecfc00fc2755854aa7fd4220901`
- Checked files: `43`
- Missing, mismatched, and unexpected bundle-agent files: none
- Manifest SHA-256:
  `d3ce01d5172ce1c0dbe23ff091ce74f397bef9b87da887361e615a06b3762d45`

HELP_HUMAN identity:

| Surface | SHA-256 | Size |
| --- | --- | ---: |
| Source `agents/AGENT_HELP_HUMAN.md` | `0285715cbe41ac2c8b7bfd8b6dbd56ad1f0cbb1a970a4f7afed290fc30d1e981` | 10,073 bytes |
| Bundle `Contents/Resources/agents/AGENT_HELP_HUMAN.md` | `0285715cbe41ac2c8b7bfd8b6dbd56ad1f0cbb1a970a4f7afed290fc30d1e981` | 10,073 bytes |

The summary records `match: true`, and an independent byte comparison returned
exit `0`.

The summary also retains the separately modeled `sourceCompleteness.status` of
`needs_remediation` because the candidate `examples` source asset is absent;
the required instruction-root comparison row itself is `satisfied`. This does
not alter the command's explicit instruction-root `status: pass`, but it is
surfaced without promotion or release inference.

## Exact commit and frontend-tree proof

HEAD remained the exact 40-character build commit:

`1b375af4f1219ecfc00fc2755854aa7fd4220901`

The required command returned no output:

```sh
git diff --stat 1b375af4f1219ecfc00fc2755854aa7fd4220901..HEAD -- projects/chirality-app-dev/frontend
```

Therefore the current HEAD frontend tree is identical to the app's build
commit. In addition, unstaged and staged frontend diff-stat checks and scoped
frontend porcelain were all empty. Generated `.next`, `dist-electron`,
`dist-runtime`, `dist`, and `artifacts` outputs are ignored by their applicable
Git ignore rules.

## Git status observations

Pre-command porcelain (concurrent owner-node work, all outside frontend):

```text
 M projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/MEMORY.md
 M projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/_STATUS.md
 M projects/chirality-app-dev/execution/_Coordination/_TaskManagement/DRAFT_NOTICE_ROOT_TM-APP-032_SUCCESSOR_IDENTITY_2026-08-02.md
 M projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv
?? projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/_run_records/POST_ROOT_AGENT0_A2_INTEGRATION_2026-08-21.md
?? projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_POST_ROOT_LOGIN_ENABLEMENT_2026-08-21/
?? projects/chirality-app-dev/execution/_Coordination/_TaskManagement/ROW_MAINTENANCE_TM-APP-032_RESCOPE_2026-08-21.md
```

Post-command porcelain was the same at path granularity. This executor added
only the two attempt-2 files below the already-untracked run root. No frontend
path appeared in porcelain before or after.

## Forbidden-target containment

Read-only before/after observations were identical:

- `gui/501/com.chirality.runtime`: loaded and running, PID `1301`, program
  `/Users/ryan/dev/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality`, argument
  `--runtime-daemon`, one run, never exited.
- `/Users/ryan/Library/LaunchAgents/com.chirality.runtime.plist`: size `1207`,
  mtime `2026-07-24 21:57:59 -0600`, SHA-256
  `2ebc556673d7dc1232a9e230a88a75355dec6916ad6c432f707a525b29a6c7bc`.
- `/Users/ryan/.local/bin/chirality`: size `1114`, mtime
  `2026-08-20 15:26:36 -0600`, SHA-256
  `f16bc2ba9228b5321deb9c66ba9526aa60fbe3bb02179d32fd66ce1de208384a`.

The packaged app was not launched, so the accepted future first-GUI-launch
launcher rewrite effect did not occur. No proof `prepare` or `capture`, proof
label selection, bootstrap, kickstart, logout/login, `launchctl` mutation,
operator plist/launcher write, signing, notarization, distribution, provider
expansion, staging, commit, push, or PR action occurred.

## Writes and acceptance matrix

Persistent writes by this executor are contained to:

- documented ignored packaging outputs in `frontend/.next`,
  `frontend/dist-electron`, `frontend/dist-runtime`, `frontend/dist`, and
  `frontend/artifacts`; and
- `executor-attempt-2/desktop-pack.log`
- `executor-attempt-2/RETURN.md`

| Acceptance check | Result |
| --- | --- |
| Exact commit / branch / Node / npm / pre-post status | PASS |
| Exact authorized package command; no alternate command/install | PASS |
| Current arm64 app directory produced | PASS |
| Packaged dependency boundary | PASS |
| Current instruction-root status/build SHA | PASS |
| Current HELP_HUMAN source/bundle hash and byte match | PASS |
| Frontend commit-to-HEAD diff-stat empty | PASS |
| No tracked frontend/manifest/lockfile mutation | PASS |
| Forbidden operator targets unchanged | PASS |
| GUI/proof/service/release hard fences preserved | PASS |

## Calibrated handoff

Packaging retry is `PASS`; there is no executor blocker. The parent may use the
absolute app path and exact build commit above to stage the still-unexecuted R12
owner procedure. Actual `prepare`, logout/login, capture, and any operator
deployment remain owner acts; DEL-09-04 remains `IN_PROGRESS` and no proof,
release-readiness, issuance, publication, signing, notarization, or
distribution claim is made here.
