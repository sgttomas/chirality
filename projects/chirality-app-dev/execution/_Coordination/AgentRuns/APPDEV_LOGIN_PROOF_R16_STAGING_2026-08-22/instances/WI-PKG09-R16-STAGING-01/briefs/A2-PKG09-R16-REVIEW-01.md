# Sealed brief — A2-PKG09-R16-REVIEW-01

## Identity and objective

- RequestedBy / ParentInstanceID: `WI-PKG09-R16-STAGING-01`
- RunID: `APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22`
- ChildInstanceID: `A2-PKG09-R16-REVIEW-01`
- Agent type: fresh ephemeral generalist Agent 2 reviewer; no delegation
- PackageID / DeliverableID: `PKG-09` / `DEL-09-04`
- Objective: independently re-run and review 100% of the exact-merge package,
  preflight, R16 procedure, status, hashes, and containment evidence.

## Accepted review inputs

- Exact branch / HEAD / origin/main:
  `codex/app-login-proof-r16-staging` /
  `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`.
- Run root, owner transcription, frozen plan/graph, executor brief/amendment,
  full executor evidence, executor return.
- New R16:
  `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/R16_MACOS26_LOGIN_PROOF_BUILD_AND_STAGING_2026-08-22.md`.
- Current DEL `_STATUS.md`, R13/R14/R15, Receipt 186, package scripts and
  current generated package/instruction-root outputs.

Strict quarantine: do not read, list, hash, copy, cite, adopt, or remove
`/private/tmp/chirality-app-login-proof-r16-superseded-20260822/`.

## Allowed tools and writes

Read-only shell/Git/package commands, Node optionless preflight, `file`,
`lipo`, `plutil`/`PlistBuddy`, `codesign` display/verify only, `shasum`, JSON
parsing, and shell syntax checks. Write only:

`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/review/REVIEW.md`

No repair authority. Do not rebuild, prepare, capture, launch/open the app,
logout/login, create the root, bootstrap/kickstart, query/touch default
operator surfaces, sign/notarize/deploy/release, stage/commit/push/merge, or
delegate.

## Mandatory full matrix

1. Require exact branch, HEAD, and origin/main; empty index; no tracked
   frontend change; only declared App documentation/run-root paths dirty.
2. Verify first/successful build logs and exit files by hash. Confirm the
   successful log is complete, comes from exact `npm run desktop:pack`, and
   contains passing embedded `desktop:verify-dependencies` and
   `instruction-root:integrity` output at exact Git SHA. Confirm the failed
   first attempt and narrow exact retry are honestly recorded.
3. Require exact app and readable/executable main binary. Independently record
   bundle identifier, short/build versions, minimum macOS and executable name;
   require thin arm64 via `file` and `lipo`; require executable SHA-256
   `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`.
4. Independently require packaged
   `Contents/Resources/runtime-cli/chirality-cli.mjs` present/readable and hash
   matches the record.
5. Re-run only read-only signature display/verification and ensure R16's
   ad-hoc/linker-only, no-team, unsealed/local-unsigned posture is exact and
   makes no signing/notarization/distribution claim.
6. Parse current instruction-root summary/manifest; require PASS, exact Git
   SHA, 43-file identity and recorded hashes. Confirm calibrated
   source-completeness residual is not upgraded.
7. Require empty output from exact frontend commit-to-HEAD diff and scoped
   frontend porcelain, plus empty index and no tracked source/manifest/
   lockfile/dependency change.
8. With proposed root absent, run only committed optionless preflight; require
   exit zero, PASS, READ_ONLY_PREFLIGHT, all consistency checks true, no
   mutation/root creation/service-job inspection, no raw username/handle;
   reconfirm root absent. Confirm only exact proof plist/job absent read-only.
   Do not query default operator identity.
9. Review R16 line-by-line against the transcribed owner direction. Require
   exact new-build command/cwd/exit/log, app/revision/package/CLI/integrity/
   Git/preflight identities, root/plist/job absence, current-only derivative
   status, and all fences.
10. Require R16's prior approximately `12:50` disclosure to say prior-authorized
    material was unadopted and superseded, with no identity attributed to or
    adopted from it.
11. Review every staged owner block as an independently copy-pasteable zsh
    sequence; extract and run `/bin/zsh -n` over each. Require no placeholder,
    exact repo cwd/app/root/label/revision/Desktop path, `set -euo pipefail`,
    and no continue-after-error path.
12. Require Step 0 to verify repository toplevel, executable presence/hash,
    empty exact frontend diff, root absence before and after, exact proof
    plist/job absence with unambiguous not-found classification, and optionless
    preflight success before printing PASS. It must not require live `HEAD` to
    equal `PROOF_REVISION`, manually open the app, or touch a default operator
    job/plist/launcher. Independently test or simulate Step 0 from a later
    docs-only HEAD whose frontend tree is identical to the build revision and
    prove the staged source gate remains executable and passing.
13. Require exact prepare block, direct PREPARED + `proofClaimed === false` +
    revision check, explicit owner logout/login only after both pass, exact
    capture block, and direct summary/evidence PASS + revision check. Confirm
    prominent no-manual-open, no-bootstrap/kickstart, stop-on-error warnings.
14. Require preservation to refuse existing concrete Desktop destination,
    create it 0700, copy exactly the three public JSON files 0600, hash and
    verify them, and exclude private state. Require owner handoff to revalidate
    PASS/revision and display revision, label, absolute evidence path, PASS and
    three exact file hash lines for verbatim return.
15. Review `_STATUS.md` diff as minimal and truthful: exact R16 pointer/current
    package, `IN_PROGRESS` and unproved, owner acts/residuals/fences retained,
    Checking Approval SHA unchanged.
16. Independently verify every R16/status/return/evidence hash claimed, run
    `git diff --check -- projects/chirality-app-dev`, require exact App-only
    containment and empty index, and confirm no prohibited action/claim.

## Verdict and return

Write `REVIEW.md` with a numbered 16-item PASS/fail matrix, independent command
evidence, hashes, exact changed paths, fence/derivative status, and either:

- `PASS` with no actionable findings; or
- `FINDINGS` with each defect stated precisely and no repair.
