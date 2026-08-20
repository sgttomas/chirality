# Launch Brief — A2-PKG09-RUNATLOAD-REVIEW-01

- RequestedBy: `WI-PKG09-RUNATLOAD-01`
- RunID: `APPDEV_LAUNCHAGENT_RUNATLOAD_PROOF_2026-08-20`
- ParentInstanceID: `WI-PKG09-RUNATLOAD-01`
- ChildInstanceID: `A2-PKG09-RUNATLOAD-REVIEW-01`
- AgentType: `TASK` (Agent 2; fresh read-only reviewer; no delegation)
- TaskSkill: `software-code-review`
- ScopePath: this child instance directory.
- ApplyEdits: `false`
- PackageID: `PKG-09`
- DeliverableIDs: [`DEL-09-04`]
- Objective: independently review 100% of the frozen packaged LaunchAgent
  `RunAtLoad` implementation diff for correctness, safety, contract coverage,
  proof validity, and evidence sufficiency.
- ImplementationBrief: sibling
  `A2-PKG09-RUNATLOAD-IMPLEMENT-01/LAUNCH_BRIEF.md` and accepted return.
- AcceptedBasis: D-APP-97 C1; live DEL-09-04 SOW/status/dependencies; R6
  daemon-service record and real launchctl fixture; frozen parent work graph;
  current shared LaunchAgent/CLI implementation; software profile and App
  validation/release docs.
- DiffBasis: exact dirty-tree contents of the following four product/test paths,
  frozen after successful implementation checks:
  - `.github/workflows/desktop-release-template.yml` —
    `73a622dda27e1cf5fbcacbd2fc01ee23f97aec35dad82b8f893d2023277442e9`
  - `projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-runatload-proof.mjs` —
    `80dacae60a03ae79793062a4b68bf5fc057de81f2a3c675a9b10fdecc11421d1`
  - `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-runatload-proof.test.ts` —
    `4493cab4e4508d992ff020afb295ef5d21ac7b1065ac19e4ff7cadfa2a33a8cd`
  - `projects/chirality-app-dev/frontend/src/__tests__/scripts/desktop-release-workflow.test.ts` —
    `f25057563c5b6dc8d94b0589aafcf04b2dfbd2e450ed376c75c7ee70ded18563`
- DeclaredReads: all basis above; implementation source/tests/workflow; shared
  runtime LaunchAgent/CLI/config sources and relevant tests; implementer
  launch/return/run record/check JSON; related existing workflow/tests.
- AllowedTools: repository reads and read-only Git inspection plus the complete
  `software-code-review` deterministic allowlist. Do not run the real launchd
  proof or mutate any job/state.
- AllowedWriteTargets: none. The runtime-owned `LAUNCH_BRIEF.md`, `STATUS.json`,
  and `RETURN.md` under this instance are the durable managed read-only record.
- VerificationEvidence: implementer focused Vitest 16/16 PASS; typecheck PASS;
  `FRONTEND_TEST_HOST_FINAL.json` registered frontend suite PASS with 1,184
  passed / 4 skipped; harness self-check and APP-HOLD integrity PASS; explicit
  scope and diff checks PASS. PR-CI launchd proof remains intentionally owed.
- ReviewFocus:
  - actual current account `~/Library/LaunchAgents`, non-root/disposable CI
    posture, and no unsafe HOME/path substitution;
  - absence of any `kickstart` or equivalent manual launch hidden in the proof;
  - packaged CLI and executable identity binding, including real launchctl
    nested fields and process identity inspection;
  - fail-closed behavior across preflight, install/bootstrap, polling, partial
    failure, cleanup, and stale/previous evidence;
  - complete process/job/plist cleanup and default job/plist protection;
  - CI expression/YAML correctness, unique label safety, artifact retention,
    permissions, signing/notarization/distribution fences;
  - test realism, missed failure modes, redaction, timeouts, races, and any
    dependency/contract drift.
- AcceptanceCriteria: `PASS` with no actionable finding and a precise residual
  risk statement, or return every actionable finding with severity,
  file/best-effort line, concrete impact, evidence, and remediation direction.
- ExpectedReturn: review verdict, findings, scope/evidence audit, residual risks,
  and manager fan-in recommendation. Do not edit or fix.
- EXCLUSIONS: all writes/repairs; owner/default LaunchAgent mutation; local
  launchd proof; dependencies/lockfiles; commits/pushes/PRs; release/lifecycle/
  reliance acceptance.
