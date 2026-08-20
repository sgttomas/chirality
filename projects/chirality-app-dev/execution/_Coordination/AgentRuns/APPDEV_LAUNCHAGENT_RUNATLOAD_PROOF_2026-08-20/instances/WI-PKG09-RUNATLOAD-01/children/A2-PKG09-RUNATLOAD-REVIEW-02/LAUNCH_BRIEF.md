# Launch Brief — A2-PKG09-RUNATLOAD-REVIEW-02

- RequestedBy: `WI-PKG09-RUNATLOAD-01`
- RunID: `APPDEV_LAUNCHAGENT_RUNATLOAD_PROOF_2026-08-20`
- ParentInstanceID: `WI-PKG09-RUNATLOAD-01`
- ChildInstanceID: `A2-PKG09-RUNATLOAD-REVIEW-02`
- AgentType: `TASK` (Agent 2; fresh read-only reviewer; no delegation)
- TaskSkill: `software-code-review`
- ScopePath: this child instance directory.
- ApplyEdits: `false`
- PackageID: `PKG-09`
- DeliverableIDs: [`DEL-09-04`]
- Objective: independently review 100% of the amended and upstream-integrated
  packaged LaunchAgent `RunAtLoad` diff for correctness, fail-closed safety,
  contract coverage, and evidence sufficiency.
- ImplementationBrief: sibling `A2-PKG09-RUNATLOAD-IMPLEMENT-01` launch brief,
  `AMENDMENT_01.md`, final `RETURN.md`, status, run records, and check JSON.
- AcceptedBasis: D-APP-97 C1; live DEL-09-04 truth/dependencies; R6 evidence and
  real launchctl fixtures; frozen parent graph; shared LaunchAgent/CLI sources;
  software profile and validation docs; upstream PR #590 intent at
  `origin/main@7584de0a8`.
- DiffBasis: exact contents below, frozen after amendment checks:
  - `.github/workflows/desktop-release-template.yml` —
    `3642152e730e3b6c59d48d860cbf1fd49a5c999d25d505deba4112dde62db2dc`
  - `projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-runatload-proof.mjs` —
    `042e5545f18d031f30fe4200fabcd02f62bef5a02137d18914908b7e82756813`
  - `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-runatload-proof.test.ts` —
    `6b5aa9c3aa9f46541b3e23c21b93f46617ca5754d2a229dcf2ba0f382aab4d8e`
  - `projects/chirality-app-dev/frontend/src/__tests__/scripts/desktop-release-workflow.test.ts` —
    `1137dbf12f76649e7744695e9962e7a26ae34e4549b7fdf02ab64f7c3d9dea6a`
- DiffComparison: evaluate tracked workflow/test changes against
  `origin/main@7584de0a8`, not the older local HEAD, so PR #590 is basis rather
  than authored delta. New script/test are whole-file review surfaces.
- DeclaredReads: all basis/implementation/evidence above, relevant runtime
  callers/tests, workflow and GitHub Actions context, real R6 launchctl outputs,
  and review v1 return with six findings.
- AllowedTools: repository reads and read-only Git inspection plus the complete
  `software-code-review` deterministic allowlist. Do not run launchd or mutate.
- AllowedWriteTargets: none. Runtime-owned brief/status/return records under
  this instance are the only durable read-only record.
- VerificationEvidence: focused Vitest 26/26 PASS; registered full frontend
  test 1,194 passed / 4 skipped; typecheck/build/harness self-check/APP-HOLD
  integrity PASS; syntax/diff/upstream-intent/scope checks PASS; evidence hash
  `772403d0c496313e0d510557900f3bcd214b74835a22f5177ae2d37518378506`.
- MandatoryReview:
  - re-evaluate every v1 finding: exact launchctl absence classification, stale
    evidence for every parse/preflight failure, symlink-safe output, exact plist
    and loaded argv, failure-evidence retention, and unknown-PID cleanup;
  - actual account `~/Library/LaunchAgents`, unique/default protection, no
    `kickstart`, packaged identity, partial/timed-out install/bootstrap, cleanup
    races, redaction and stale evidence;
  - PR #590 event types and `artifact-proof` gate preserved exactly, workflow
    expressions/YAML correct, `if: always()` upload does not weaken the strict
    successful artifact gate, and release/signing fences remain unchanged;
  - realistic tests and gaps that could cause the `macos-15` host proof to fail
    or claim PASS incorrectly.
- AcceptanceCriteria: `PASS` with no actionable finding and explicit residual
  risks, or every actionable finding with severity, path/line, impact, evidence,
  and remediation. Do not edit.
- ExpectedReturn: terminal verdict, per-v1-finding audit, any new findings,
  scope/evidence audit, residual risk, and fan-in recommendation.
- EXCLUSIONS: all writes/repairs; local launchd/default/owner state; dependency/
  lockfile change; commits/pushes/PRs; release/lifecycle/reliance acceptance.
