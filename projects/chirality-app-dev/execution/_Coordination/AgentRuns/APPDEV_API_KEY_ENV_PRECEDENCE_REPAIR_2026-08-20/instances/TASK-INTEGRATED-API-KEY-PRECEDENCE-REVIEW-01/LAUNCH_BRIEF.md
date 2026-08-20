# INIT-TASK — fresh integrated cross-package review

PURPOSE: Independently review the complete frozen API-key precedence repair and packaged-security closure candidate.
RequestedBy: `WI-PKG09-API-KEY-PRECEDENCE-01`
RunID: `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
ParentInstanceID: `WI-PKG09-API-KEY-PRECEDENCE-01`
ChildInstanceID: `TASK-INTEGRATED-API-KEY-PRECEDENCE-REVIEW-01`
WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
ScopePath: `{WORKING_ROOT}`
TaskSkill: `software-code-review`
ImplementationBrief: `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/WI-PKG09-API-KEY-PRECEDENCE-01/LAUNCH_BRIEF.md`
AcceptedBasis: `6710ee6354debc201f6a454e2802897026cd4b38`
DiffBasis: `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/FROZEN_CANDIDATE_MANIFEST.md`
VerificationEvidence: complete frozen candidate plus `/tmp/chirality-precedence-closure.pXvs6Z`
PROFILE_PATH: `{WORKING_ROOT}/software-workflow.json`
ApplyEdits: false
AllowedWriteTargets: []

Tasks:
  - Independently reconstruct exactly 86 frozen candidate paths and aggregate SHA-256 `ee2623a620af684ed6b67a678466d46db186b4e590c9dd606f61542ff322acec`, excluding only the manifest and this review's own control records.
  - Read all four product/test paths in full and trace credential status serialization through the daemon/client/IPC/settings consumers.
  - Inspect every frozen evidence/state/control path, parse all JSON/NDJSON, and verify package write containment, candidate-wide whitespace including untracked files, protected-path exclusions, and predecessor identities.
  - Review the fixed safeStorage > canonical env > compatibility env behavior, non-secret source discriminator, IPC fail-closed validation, provider isolation, error/unavailable compatibility, security, and regression tests.
  - Backcheck compact N3 evidence against the raw host summary, logs, TCP snapshots, cleanup evidence, artifact hashes, exact commands, and secret scan under `/tmp/chirality-precedence-closure.pXvs6Z`.
  - Verify the fresh artifact actually contains the accepted fixed product behavior and the packaged proof supports every calibrated assessment/status claim.
  - Verify only DEL-09-06's named D-APP-97 packaged-security Remaining item and DEL-09-04's coordinated REQ-009/R4-P49 item were removed; lifecycle, Checking Approval SHA, dependencies, RunAtLoad, owner-machine deployment, and all release fences remain unchanged.
  - Return PASS, PASS_WITH_FINDINGS, or FAIL with exact locations, impact, evidence, remediation, 100% coverage, residual risk, and confirmation of no writes/delegation. Fan-in requires PASS with zero actionable findings.

ExpectedReturn:
  - Frozen identity and 100% coverage; product correctness/security verdict; proof/evidence integrity; state/claim calibration; exact findings; fan-in recommendation; no-write confirmation.

CustomInstructions:
  - Read-only. Do not edit, stage, commit, push, open PRs, run release actions, or delegate.
  - The first sandbox registered-check failure is accepted only as execution-surface calibration if exact host/mise reruns are independently supported.
  - Compact evidence is derivative and must match raw proof; it does not substitute for SOW or product truth.

EXCLUSIONS:
  - No lifecycle/release acceptance or product remediation.
