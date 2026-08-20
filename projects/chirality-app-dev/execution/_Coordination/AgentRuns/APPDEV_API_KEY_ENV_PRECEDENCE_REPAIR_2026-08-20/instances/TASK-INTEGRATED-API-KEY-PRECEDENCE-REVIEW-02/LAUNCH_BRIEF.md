# INIT-TASK — fresh integrated review 02

PURPOSE: Independently review the complete remediated cross-package candidate and backcheck Review 01 F1-F3.
RequestedBy: `WI-PKG09-API-KEY-PRECEDENCE-01`
RunID: `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
ParentInstanceID: `WI-PKG09-API-KEY-PRECEDENCE-01`
ChildInstanceID: `TASK-INTEGRATED-API-KEY-PRECEDENCE-REVIEW-02`
WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
ScopePath: `{WORKING_ROOT}`
TaskSkill: `software-code-review`
ImplementationBrief: `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/TASK-INTEGRATED-REMEDIATION-01/LAUNCH_BRIEF.md`
AcceptedBasis: `6710ee6354debc201f6a454e2802897026cd4b38`
DiffBasis: `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/FROZEN_CANDIDATE_MANIFEST_V2.md`
VerificationEvidence: complete 94-path candidate plus `/tmp/chirality-precedence-closure.pXvs6Z`
PROFILE_PATH: `{WORKING_ROOT}/software-workflow.json`
ApplyEdits: false
AllowedWriteTargets: []

Tasks:
  - Independently reconstruct exactly 94 paths and aggregate `eeda6c56d07326b0c30c186627d14a8319c3f8239b497b507f314724e544b788`, excluding only v2 manifest and this review's controls.
  - Review 100% of all 4 product/test and 90 evidence/state/control paths, including prior review and remediation controls; parse all JSON/NDJSON and verify complete untracked whitespace.
  - Backcheck Review 01 F1-F3: zero trailing blanks, factually exact REQ015 citations, and normalized PASS evidence for 350 harness tests plus self-check exit 0.
  - Reconfirm product correctness/security, predecessor identities, raw packaged artifact/credential/network/TCP/cleanup/secret proof, compact evidence, APP-HOLD, state calibration, Remaining boundaries, lifecycle/Checking SHA/dependency/release fences, and no protected-path drift.
  - Report any actionable finding immediately; terminal return must state PASS/PASS_WITH_FINDINGS/FAIL, exact 100% coverage, findings, residual risk, fan-in validity, and no-write/delegation confirmation. Fan-in requires PASS with zero actionable findings.

ExpectedReturn:
  - Exact v2 identity and coverage; F1-F3 backcheck; integrated correctness/evidence/state verdict; findings; fan-in recommendation.

CustomInstructions:
  - Read-only; do not repair, edit, stage, commit, push, publish, release, or delegate.
  - No product/host proof rerun is required; validate byte preservation and retained evidence.

EXCLUSIONS:
  - No lifecycle/release acceptance or remediation.
