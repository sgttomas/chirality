# Sealed brief — A2-PKG09-R18-EXECUTE-01

## Identity and objective

- RequestedBy / ParentInstanceID: `WI-PKG09-R18-STAGING-01`
- RunID: `APPDEV_LOGIN_PROOF_R18_STAGING_2026-08-22`
- ChildInstanceID: `A2-PKG09-R18-EXECUTE-01`
- Agent type: fresh ephemeral generalist Agent 2; no delegation
- PackageID / DeliverableID: `PKG-09` / `DEL-09-04`
- Objective: overwrite the ignored R16 package with an exact-merge offline
  unsigned arm64 build, prove its identity and R17 guard, and author R18 plus
  the minimal status update without executing the staged procedure.

## Exact basis and identities

- Branch: `codex/app-login-proof-r18-staging`
- Required HEAD and origin/main:
  `166efa82748133e90674be62304b81f8a0a8c1b4`
- App:
  `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app`
- `PROOF_REVISION=166efa82748133e90674be62304b81f8a0a8c1b4`
- `PROOF_ROOT=/private/tmp/ch-r18-91499728-51dd`
- `PROOF_LABEL=com.chirality.ci.runatload.login.owner.macos26.r18.1f16d830-4fd0-4647-a01b-a746e8a22cb4`
- `PROOF_PLIST=/Users/ryan/Library/LaunchAgents/com.chirality.ci.runatload.login.owner.macos26.r18.1f16d830-4fd0-4647-a01b-a746e8a22cb4.plist`
- `PROOF_SERVICE=gui/501/com.chirality.ci.runatload.login.owner.macos26.r18.1f16d830-4fd0-4647-a01b-a746e8a22cb4`
- `PUBLIC_EVIDENCE=/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r18-1f16d830-4fd0-4647-a01b-a746e8a22cb4-public-evidence`

Fail closed if HEAD/origin/main differ, index or tracked files are dirty,
frontend tracked/scoped porcelain is nonempty, or exact root/plist/public
destination exists or is a symlink, or exact service is anything other than
launchctl exit 113 with these two exact lines:

```text
Bad request.
Could not find service "com.chirality.ci.runatload.login.owner.macos26.r18.1f16d830-4fd0-4647-a01b-a746e8a22cb4" in domain for user gui: 501
```

Manager-created untracked files inside this new run root are the sole expected
repository exception.

## Declared reads

Read root `AGENTS.md`, `agents/AGENT_TASK.md`, this brief and run root, App
LOOP_INIT and committed selected plan, Receipt 188, current DEL status, R16 and
R17, R17 repair source/tests, R16 run-root evidence, `software-workflow.json`,
packaging docs, `frontend/package.json`, tracked build/integrity/proof scripts,
and the package/host/Git identities needed below.

Do not read, list, traverse, hash, copy, cite, or adopt the owner's Desktop R16
failed-evidence directory or private R16 proof root. Do not query or touch the
default operator job, plist, launcher, or `~/.local/bin/chirality`.

## Allowed tools and writes

Allowed: shell; tracked Node/npm scripts; Git read-only commands; `file`,
`lipo`, `plutil`/`PlistBuddy`, `codesign` display/verify only, `shasum`, and
patch-based record writes. Run packaging in the ordinary restricted sandbox;
do not request network escalation. `npm_config_offline=true` may be set as a
defense in depth, but the executed tracked command remains exactly
`npm run desktop:pack`.

Allowed writes:

1. ignored `frontend/dist` and current-byte instruction-root outputs generated
   only by the exact tracked package command;
2. new deliverable record `_run_records/R18_MACOS26_LOGIN_PROOF_BUILD_AND_STAGING_2026-08-22.md`;
3. minimal amendment to the same deliverable's `_STATUS.md`;
4. unique `instances/WI-PKG09-R18-STAGING-01/executor/` evidence and return.

No product source/test/manifest/lockfile/dependency/provider, receipt, prior
record, shared completion surface, or path outside App may change.

## Execution requirements

1. Record exact initial Git/basis/branch/clean-state evidence and exact
   root/plist/public-destination absence plus exact service exit/text. The
   untracked run root is expected; all other candidate paths must be clean.

2. From exact cwd `projects/chirality-app-dev/frontend`, preserve full combined
   output and exit status for exactly `npm run desktop:pack`. Overwrite, do not
   adopt, the prior ignored package. Use no network and no escalation. The
   pinned Electron 43.2.0 cache must satisfy the build; any cache miss/download
   attempt fails this node. Require embedded `desktop:verify-dependencies` and
   `instruction-root:integrity` to pass in the full log.

3. Require the exact app/main executable and independently record bundle ID,
   short/bundle version, minimum macOS, executable name, `file`, `lipo -archs`
   thin arm64, codesign display/verify ad-hoc/linker-only/no-team posture, main
   SHA-256, and packaged runtime-cli presence/readability/SHA-256/arm64.
   Record instruction-root summary/manifest identities and exact commit.

4. Prove the packaged runtime contains the committed R17 runtime-host
   over-long-socket guard via deterministic source/build/package string or
   module evidence, including the 103-byte maximum and measured/max diagnostic,
   without executing the GUI or daemon.

5. Immediately after build require unchanged HEAD, empty index, no tracked
   changes, empty
   `git diff --stat 166efa82748133e90674be62304b81f8a0a8c1b4..HEAD -- projects/chirality-app-dev/frontend`,
   and empty scoped frontend porcelain. Generated ignored output is expected.

6. Reconfirm exact root/plist/public destination absent/non-symlink and exact
   service exit 113/text. Run only the committed optionless read-only
   `preflight`; require PASS/`READ_ONLY_PREFLIGHT`, no root creation, and all
   exact absences unchanged. Do not run prepare/capture or mutate launchd.

7. Write new R18 from current evidence. Record exact build command/cwd/exit/log,
   cache/no-network posture, package/CLI/integrity/guard/preflight identities,
   hashes, 67-byte socket path, frontend identity, derivative status, and all
   fences. Do not adopt identities from R16 package bytes.

8. Stage documentation-only blocks. State that every block starts with
   `cd /Users/ryan/.codex/worktrees/ef5e/chirality`, then `set -euo pipefail`,
   and runs in a fresh Terminal tab with no inherited variables. Each block
   must actually repeat those lines and define every value it uses.

   - Step 0: exact app/revision/root/label/plist/service/public path; require
     exact main hash; require empty frontend diff from revision to later HEAD
     without requiring HEAD equality; root/plist/public path absent and not
     symlinks; exact service exit 113 and exact two-line message; compute and
     print exact control socket UTF-8 bytes, require `67` and `<=103`; run
     optionless read-only preflight; recheck all absences and service text.
   - Prepare: exact command with app/root/label/revision.
   - Prepared check: require `PREPARED` and `proofClaimed === false`.
   - Owner act: only after both prior blocks pass, one ordinary logout then
     login on the same GUI account; never manually open the app.
   - Capture: exact capture command after login.
   - PASS/revision: require summary and evidence-package PASS plus exact source
     revision.
   - Preservation: refuse existing/symlink public destination, create it mode
     0700, copy exactly prepared/summary/evidence-package mode 0600, verify
     exactly three regular files and print SHA-256 lines; no private files.
   - Handoff: independently print exact revision/label/public path/PASS and the
     three hashes plus an owner message that proof remains unaccepted until
     separately accepted. No placeholder values.

   Prominently prohibit manual app open, bootstrap/kickstart, and continuing
   after any error. The procedure remains portable after later docs-only
   commit/merge because frontend-diff identity, not HEAD equality, is its gate.

9. Update `_STATUS.md` minimally to point to R18 and exact staged identities,
   retain `IN_PROGRESS` and unproved, leave owner logout/login/capture and
   acceptance open, and retain every release/operator fence.

10. Run proportional syntax/structured-command safety, focused/full/typecheck,
    package/integrity checks, APP-HOLD, repository self-check, practitioner
    suite, prior-ledger receipt validator, App-only containment, candidate/new
    file whitespace, `git diff --check`, exact changed paths, hashes, and empty
    index. Return PASS/fail, reruns, blockers, derivative status, and changed
    paths. Do not write Receipt 189.

## Hard exclusions

No network or escalation; Desktop R16 failed-evidence/private-root read;
default operator query/mutation; GUI/open app; prepare/capture/logout/login;
root/plist/job/public-directory creation; bootstrap/kickstart; signing,
notarization, deployment, distribution, release/reliance/proof-acceptance;
dependency/provider expansion; receipt; stage/commit/push/PR/merge; delegation.
