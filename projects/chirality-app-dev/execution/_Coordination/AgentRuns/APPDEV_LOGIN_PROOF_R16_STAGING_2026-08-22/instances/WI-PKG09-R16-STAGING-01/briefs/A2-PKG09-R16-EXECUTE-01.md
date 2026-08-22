# Sealed brief — A2-PKG09-R16-EXECUTE-01

## Identity and objective

- RequestedBy / ParentInstanceID: `WI-PKG09-R16-STAGING-01`
- RunID: `APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22`
- ChildInstanceID: `A2-PKG09-R16-EXECUTE-01`
- Agent type: fresh ephemeral generalist Agent 2; no delegation
- PackageID / DeliverableID: `PKG-09` / `DEL-09-04`
- Objective: independently rebuild the unsigned arm64 app from exact merged
  source and author a new R16/status staging package with complete read-only
  evidence and owner copy/paste procedure.

## Exact basis and identities

- Branch: `codex/app-login-proof-r16-staging`
- Required HEAD and origin/main:
  `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`
- Required app:
  `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app`
- `PROOF_REVISION=06f60e42e35ea5c39abf9e33c4d3e877d77c4497`
- `PROOF_ROOT=/private/tmp/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20`
- `PROOF_LABEL=com.chirality.ci.runatload.login.owner.macos26.00bc8f1a-0045-48a2-970f-be120cf7fc20`
- Public evidence destination:
  `/Users/ryan/Desktop/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20-public-evidence`

Fail closed before build if HEAD/origin/main differ, index is nonempty,
tracked files are dirty, scoped frontend porcelain is nonempty, or the proof
root/plist/exact proof job exists. Manager-created untracked files inside this
new run root are the sole expected post-activation exception.

## Declared reads

- Root `AGENTS.md`, current `AGENT_WORKING_ITEMS.md` and `AGENT_TASK.md`.
- App LOOP_INIT plus committed selected standing plan, Receipt 186, current
  DEL status, merged R14/R15, R13 only as command/procedure precedent,
  `software-workflow.json`, `docs/BUILD_AND_RELEASE.md`, tracked package and
  proof scripts, this run root, activation, and sealed brief.
- Read-only package/host/Git commands specified below.

Strict quarantine: do not read, list, hash, copy, cite for identity, or adopt
any byte or claim from
`/private/tmp/chirality-app-login-proof-r16-superseded-20260822/`. Do not
remove it; manager owns removal only after fresh review PASS.

## Allowed tools and writes

Allowed tools: shell; tracked Node/npm scripts; Git read-only commands;
`file`, `lipo`, `plutil`/`PlistBuddy`, `codesign` display/verify only,
`shasum`, and patch-based record writes.

Allowed writes:

1. ignored build/package and current-byte instruction-root outputs generated
   only by exact `npm run desktop:pack`;
2. new deliverable record
   `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/R16_MACOS26_LOGIN_PROOF_BUILD_AND_STAGING_2026-08-22.md`;
3. minimal amendment to that deliverable's `_STATUS.md`;
4. unique `executor/` evidence under this manager instance, including complete
   build/preflight/check logs and `RETURN.md`.

No product source/test/manifest/lockfile/dependency/provider, prior record,
receipt, shared completion surface, or path outside App may change.

## Execution requirements

1. Record exact initial HEAD/branch/origin, clean index/tracked/frontend state,
   root/plist absence, and a read-only exact-proof-label job absence check.
   Do not query or touch the default operator job, plist, or launcher.

2. From exact cwd `projects/chirality-app-dev/frontend`, preserve full combined
   output and exit status while running exactly:

   ```sh
   npm run desktop:pack
   ```

   The tracked command itself must run and pass embedded
   `desktop:verify-dependencies` and `instruction-root:integrity`. Do not
   substitute separate gates. If a sandbox/cache network failure occurs, stop
   and ask the manager; no update, alternate command, or provider expansion.

3. Require the exact app and readable/executable main binary. Record via
   independent read-only checks:

   - bundle identifier, short version, bundle version, executable name, and
     minimum macOS;
   - `file` and `lipo -archs`, requiring thin arm64;
   - exact main executable SHA-256;
   - `codesign -dv --verbose=4` and verification output showing only
     ad-hoc/linker identity, no team/Developer ID, with no signing action;
   - packaged
     `Contents/Resources/runtime-cli/chirality-cli.mjs` exists and is readable;
   - instruction-root latest summary/manifest hashes, PASS status, exact Git
     SHA, counts, and embedded dependency-boundary PASS in the full build log.

4. After build, require no output from:

   ```sh
   git diff --stat 06f60e42e35ea5c39abf9e33c4d3e877d77c4497..HEAD -- projects/chirality-app-dev/frontend
   git status --porcelain=v1 --untracked-files=all -- projects/chirality-app-dev/frontend
   ```

   Also require empty index, unchanged HEAD, and no tracked source/manifest/
   lockfile/dependency change.

5. Confirm proposed root absent, run only the committed optionless read-only
   `preflight`, save its exact output, require exit zero and PASS with
   `READ_ONLY_PREFLIGHT`, no mutations/root creation/service-job inspection,
   then reconfirm root absent. Confirm only the exact proof plist/job absent
   read-only. Do not run `prepare` or `capture`.

6. Write a NEW R16 entirely from current evidence. Do not use quarantined
   prior bytes or claims. R16 must disclose: an earlier approximately `12:50`
   local rebuild and superseded R16 material occurred under prior
   authorization, remained unadopted, and are superseded by this exact-merge
   rebuild and new record. Do not cite identities from that prior material.

7. R16 must record exact command/cwd/exit/log, app/revision/package/CLI/
   integrity/preflight identities and hashes, root/plist/job absence,
   frontend-diff/porcelain proof, derivative status, and fences. It must stage
   independently copy-pasteable documentation-only blocks:

   - **Step 0:** exact repo-root `cd`; `set -euo pipefail`; define all concrete
     values; require exact current HEAD; require app executable and exact
     recorded SHA-256; run and require empty exact frontend diff; require root
     absent; run optionless preflight and require it exits zero; require root
     remains absent. Print a clear PASS only after all gates.
   - **Step 1:** exact prepare command using concrete app/root/label/revision.
   - **Prepared check:** parse `prepared.json`, require `status === 'PREPARED'`
     and `proofClaimed === false`, then print the exact accepted state.
   - **Owner act:** only after Step 1 and the prepared check both exit zero,
     instruct one ordinary logout and later login on the same GUI account.
     State that manually opening `Chirality.app` is forbidden and not part of
     RunAtLoad proof.
   - **Capture:** exact capture command after login.
   - **PASS/revision check:** require both `summary.json` and
     `evidence-package.json` status PASS and exact source revision.
   - **Preservation/hashes:** refuse an existing concrete Desktop destination;
     create it mode 0700; copy only `prepared.json`, `summary.json`, and
     `evidence-package.json` mode 0600; generate and verify SHA-256 for exactly
     those three. Never copy/publish private capture-state files.
   - **Owner handoff:** generate and display exact plain text naming revision,
     label, public-evidence absolute path, PASS status, and the three exact
     file hash lines; tell the owner to paste the complete displayed handoff
     back verbatim.

   Immediately before the procedure, state prominently: do not manually open
   the app, bootstrap/kickstart, or continue after any error. Every block must
   be shell-safe, independently copy-pasteable, and contain no placeholder for
   any required value.

8. Update `_STATUS.md` minimally: point to R16 and exact rebuilt/staged values,
   retain `IN_PROGRESS` and unproved, keep actual owner logout/login/capture
   and proof acceptance open, and retain all release/operator fences.

9. Run `git diff --check`, App-only containment, exact changed-path, hash, and
   empty-index checks. Return PASS/fail, exact hashes, paths, reruns, blockers,
   derivative status, and fresh-review requirement.

## Hard exclusions

No prior-temp read/adoption; GUI/open app; prepare/capture/logout/login;
proof-root creation; bootstrap/kickstart; default operator job/plist/launcher
query or mutation; signing/notarization/deployment/release/distribution;
dependency/provider expansion; stage/commit/push/merge/PR/receipt; delegation.
