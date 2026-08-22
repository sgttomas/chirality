# Fresh review — A2-PKG09-R16-REVIEW-02

## Verdict

`PASS — COMPLETE 16-ITEM MATRIX PASSED; NO ACTIONABLE FINDINGS`

- Reviewer: fresh ephemeral generalist Agent 2; no delegation
- Parent: `WI-PKG09-R16-STAGING-01`
- Package / deliverable: `PKG-09` / `DEL-09-04`
- Accepted basis: `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`
- Branch: `codex/app-login-proof-r16-staging`
- Review posture: evidence-only; no reviewed byte repaired

The strict temporary-material quarantine was honored. The quarantined recovery
material was not read, listed, hashed, copied, cited, adopted, or removed.

## Complete matrix

1. **PASS — exact Git basis and containment.** Independent `git rev-parse`,
   branch, index, frontend-diff, frontend-porcelain, and status checks found
   branch `codex/app-login-proof-r16-staging`, `HEAD == origin/main ==
   06f60e42e35ea5c39abf9e33c4d3e877d77c4497`, an empty index, no tracked or
   untracked frontend change, and only the declared App status/R16/run-root
   paths dirty.

2. **PASS — exact build record.** Independent hashes match the failed first
   log (`827459042c5115f7b0e1ac14d9a25d9550bc48ddf1b1cf5442adafc4d1975ee5`),
   successful retry log
   (`67f9c2de21de732f819e59cad4f4b94429cd654c227fc27653ed676d9937ce62`),
   and successful exit file
   (`9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`).
   The first exit file contains `1`; the retry contains `0`. The first log
   records the pinned Electron `43.2.0` arm64 cache miss and sandbox DNS
   `ENOTFOUND github.com`. The complete successful log begins with the tracked
   `desktop:pack` script and ends after PASS from
   `desktop:verify-dependencies` and `instruction-root:integrity`: zero local
   package entries, no forbidden development package, all required packages,
   packaged desktop/CLI source proof PASS, no failures, integrity `pass`, 43
   checked files, and exact Git SHA. The recorded narrow retry is truthful.

3. **PASS — package and executable identity.** The exact app directory exists;
   its main executable is readable/executable. Independent PlistBuddy, `file`,
   `lipo`, and SHA-256 checks returned `com.chirality.app`, short/build versions
   `2.0.0`/`2.0.0`, executable `Chirality`, minimum macOS `15.0.0`, thin arm64
   Mach-O, and executable SHA-256
   `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`.

4. **PASS — packaged CLI identity.** The packaged
   `Contents/Resources/runtime-cli/chirality-cli.mjs` is present/readable and
   independently hashes to
   `0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989`.

5. **PASS — calibrated unsigned posture.** Read-only `codesign -dv
   --verbose=4` reports `adhoc,linker-signed`, `Signature=adhoc`, no Team ID,
   no sealed resources, and no internal requirements. Independent strict
   verification exits `1` only with `code has no resources but signature
   indicates they must be present`. The successful builder log records skipped
   application signing under `CSC_IDENTITY_AUTO_DISCOVERY=false`. R16 makes no
   signing, notarization, distribution, or release claim.

6. **PASS — instruction-root evidence.** Independent JSON parsing and hashes
   require summary `status: pass`, exact Git SHA, 43 comparisons/43 manifest
   files, and empty missing/mismatched/unexpected arrays. Summary SHA-256 is
   `89ba0e597190205fd50e1216e9efeb9f6ea9dd53e920a27f31251ad8cfb5b468`;
   manifest SHA-256 is
   `dfea68cf9b550848d5573a02c73b6647700e0543b6376bb61831c3d38d1c75d1`.
   The separate `sourceCompleteness.status: needs_remediation` and missing
   candidate `examples` asset remain explicitly calibrated and are not
   upgraded.

7. **PASS — exact source proof.** Both the exact
   `git diff --stat 06f60e42e35ea5c39abf9e33c4d3e877d77c4497..HEAD --
   projects/chirality-app-dev/frontend` and scoped frontend porcelain are
   empty. The index is empty. No tracked source, test, manifest, lockfile,
   dependency, Electron, or package file changed.

8. **PASS — live optionless read-only preflight and uniqueness.** Independent
   checks found the exact proposed proof root and plist absent before and after
   preflight. The committed optionless command exited `0` with schema v1,
   `PASS`, `READ_ONLY_PREFLIGHT`, all five validation booleans true,
   `mutationsPerformed: false`, `sessionRootCreated: false`, and
   `serviceOrJobInspection: false`; it emitted no username or session handle.
   The exact proof-service-only `launchctl print` exited `113` and returned
   exactly `Bad request.` plus the exact label-not-found line for `gui: 501`.
   No default operator identity was queried.

9. **PASS — R16 direction fidelity.** Line-by-line review against the owner
   transcription found the exact build cwd/command/outcomes/log, app and
   revision, package/CLI/integrity/Git/preflight identities, absent proof
   root/plist/job, current-only derivative status, concrete procedure, and all
   hard fences. No prepare, capture, GUI launch, logout/login, bootstrap,
   kickstart, deployment, signing, notarization, distribution, publication,
   issuance, reliance, or release act is claimed.

10. **PASS — supersession disclosure.** R16 explicitly discloses the earlier
    approximately `12:50` rebuild and material as prior-authorized, unadopted,
    and superseded. It attributes or adopts no byte or identity from that
    material.

11. **PASS — copy-paste and syntax.** All 11 `sh` fences independently pass
    `/bin/zsh -n`. Each of the seven owner-execution blocks starts at the exact
    repository cwd and contains `set -euo pipefail`; concrete app, revision,
    root, label, and Desktop evidence paths contain no placeholder or
    continue-after-error route.

12. **PASS — Step 0 and post-commit portability.** Static review proves Step 0
    checks repository toplevel, executable presence/mode/hash, empty exact
    frontend diff, root absence before and after, exact plist absence, exact
    proof-service exit `113` plus exact two-line not-found output, and
    optionless preflight before its final PASS. It contains no assertion that
    live `HEAD` equals `PROOF_REVISION`, no manual-open route, and no default
    operator surface. Independently, a temporary isolated clone created
    distinct synthetic commit `c44aca59c562dbf81b94466b8c83699080008abe`
    with exact parent/build revision and only
    `projects/chirality-app-dev/execution/_Coordination/R16_REVIEW2_SYNTHETIC_DOC_ONLY.md`
    changed. Its build-revision-to-later-HEAD frontend diff was empty and the
    staged toplevel/frontend source gate printed
    `PASS_SOURCE_GATE_DISTINCT_LATER_DOCS_ONLY_HEAD`. No preflight ran in that
    scratch proof; the live branch/ref/index were unchanged, and the scratch
    clone was removed.

13. **PASS — prepare/capture sequence.** The exact prepare block is followed by
    a direct `PREPARED`, `proofClaimed === false`, and exact-revision check.
    Only after both pass does the record direct the owner to ordinary
    logout/login; the later capture block and direct summary/evidence PASS plus
    revision check are exact. Prominent instructions forbid manual app open,
    bootstrap/kickstart, and continuation after any failure.

14. **PASS — public preservation and handoff.** Preservation refuses an
    existing concrete Desktop destination, creates it mode 0700, installs
    exactly `prepared.json`, `summary.json`, and `evidence-package.json` mode
    0600, checks every mode, hashes all three, and verifies the hashes. Private
    capture/runtime/plist state is expressly excluded. Owner handoff
    revalidates PASS/revision and prints the exact revision, label, absolute
    evidence path, `STATUS=PASS`, and three exact hash lines for verbatim
    return.

15. **PASS — minimal truthful status amendment.** The status diff changes only
    the now-merged/rebuilt R15 paragraph and adds one R16 history entry. It
    retains `IN_PROGRESS`, unproved status, open owner acts/residuals, all
    fences, and unchanged Checking Approval SHA
    `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`.

16. **PASS — hashes, whitespace, containment, and prohibited-action audit.**
    Independent SHA-256 checks match R16
    `348397ce3f7a217492017f187c7068b7b41cd9ea0e279f8b4bf86c1daaf9108e`,
    final executor return
    `f24635a2392e6c5bc716a35dbf87615dbfaaa2a52e48c845b60d21558df07e88`,
    unchanged status
    `4f9e04a3d229b9d64c83a038ba980518709684b3ed36fbb5e1d96172653b21a6`,
    and every other hash claimed in R16/return. `git diff --check --
    projects/chirality-app-dev` passes. The index is empty and all dirty paths
    are App-contained. Review found no prohibited execution or claim.

## Independent evidence summary

- `git rev-parse`, `git branch --show-current`, scoped `git diff`/`status`,
  cached diff, and whitespace check: PASS.
- `PlistBuddy`, `file`, `lipo`, executable/CLI SHA-256: PASS.
- `codesign` display and calibrated strict verification: PASS.
- Summary/manifest JSON parse and SHA-256: PASS.
- Build/evidence/R16/status/return SHA-256 matrix: PASS.
- Live root/plist absence, exact proof-service classification, optionless
  preflight, and post-preflight absence: PASS.
- Eleven extracted shell fences under `/bin/zsh -n`: PASS.
- Independent distinct later docs-only synthetic-HEAD source gate: PASS.
- Final containment and empty-index recheck: PASS.

## Exact changed-path inventory at verdict

The only dirty product/deliverable paths are:

```text
projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md
projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/R16_MACOS26_LOGIN_PROOF_BUILD_AND_STAGING_2026-08-22.md
```

The only other dirty paths are the following new derivative run package:

```text
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/CHAT_TRANSCRIPTION.md
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/ORCHESTRATION_PLAN.md
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/WORK_GRAPH.json
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/ACTIVATION_AND_WORK_GRAPH.md
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/RUNTIME_EVENTS.jsonl
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/briefs/A2-PKG09-R16-EXECUTE-01.md
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/briefs/A2-PKG09-R16-REVIEW-01.md
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/briefs/A2-PKG09-R16-REVIEW-02.md
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/briefs/AMENDMENT_01_LOCKED_ELECTRON_RETRIEVAL.md
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/briefs/AMENDMENT_02_POST_COMMIT_STEP0_PORTABILITY.md
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor/desktop-pack.exit-status.txt
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor/desktop-pack.log
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor/initial-gate.log
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/RETURN.md
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/amendment-02-exact-absence-gate.log
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/amendment-02-final-qa.log
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/codesign-executable.log
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/desktop-pack.exit-status.txt
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/desktop-pack.log
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/evidence-index-pre-record.log
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/final-checks.log
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/integrity-evidence.log
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/package-identity.log
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/post-build-git.log
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/post-commit-portability-setup-failure.txt
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/post-commit-portability.log
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/preflight-boundaries-after.log
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/preflight-boundaries-before.log
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/preflight.exit-status.txt
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/preflight.log
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/review/REVIEW.md
```

All paths are beneath `projects/chirality-app-dev/`; the index remains empty.

## Derivative and handoff status

R16, the ignored unsigned package, generated integrity files, live preflight
output, build logs, and this review are derivative evidence bound to accepted
source snapshot `06f60e42e35ea5c39abf9e33c4d3e877d77c4497` and do not replace source
truth. DEL-09-04 remains `IN_PROGRESS` and unproved. Actual prepare, owner
logout/login, capture, public-evidence return, and owner proof acceptance remain
owner acts. Rebuild/restage is required if the frontend tree or executable
identity changes; fresh values are required if the root, plist, or label ceases
to be uniquely absent. No signing, notarization, deployment, distribution,
publication, issuance, certification, reliance, or release-readiness claim is
made.

## Findings

None.
