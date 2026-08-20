# Sealed Agent 2 brief — DEL-09-05 unsigned Desktop CI artifact workflow

- RequestedBy: `HELP_HUMAN -> WORKING_ITEMS`
- RunID: `APPDEV_UNSIGNED_RELEASE_WORKFLOW_2026-08-19`
- ParentInstanceID: `WI-PKG09-DEL0905-01`
- ChildInstanceID: `A2-DEL0905-IMPLEMENT-01`
- PackageID: `PKG-09`
- DeliverableIDs: `DEL-09-05`
- ScopePath: `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-05_CI_Artifact_and_Release_Verification_Workflow`
- PROFILE_PATH: `{WORKING_ROOT}/software-workflow.json`
- TaskSkill: `software-bounded-implementation`
- ApplyEdits: `true`
- Objective: reactivate `.github/workflows/desktop-release-template.yml.disabled` as `.github/workflows/desktop-release-template.yml`, replacing its fenced release-publication design with the smallest coherent least-privilege GitHub Actions workflow that builds, verifies, and uploads unsigned macOS Desktop artifacts for CI-only use under D-APP-97 C1.
- AcceptedBasis: branch `codex/app-unsigned-release-workflow-20260819` at `57803893d1eb161f395e0574c256dd27920bf1d4`; exact D-APP-97 C1 ruling; DEL-09-05 live SOW/Remaining; frozen activation and work graph in this run root; APP-HOLD dispatch preflight is ALLOW.
- Dependencies: existing frontend/runtime lockfiles, build scripts, packaging configuration, instruction-root integrity and packaged-dependency verification; do not change dependency versions, locks, runtime contracts, or product/provider/network scope.
- DeclaredReads: root/project agent and TASK instructions; `skills/software-bounded-implementation/{SKILL.md,BRIEF_SCHEMA.md,TOOL_POLICY.md,QA_CHECKS.md}`; `docs/SOFTWARE_WORKFLOW_PROFILE.md`; project software profile, D-APP-97, DEL-09-05 SOW/status/memory/context/dependencies/references; current disabled template; related active workflows; frontend package/build config, scripts, tests, instruction-root/package-integrity proofs, and root/runtime package scripts needed to form an executable macOS job.
- AllowedTools: repository read/search; `apply_patch`; existing repository/package test, typecheck, build, workflow-static-validation, and registered software-workflow commands; no installs, release/publication actions, network expansion, or destructive commands.
- AllowedWriteTargets: `.github/workflows/desktop-release-template.yml`; deletion/retirement of `.github/workflows/desktop-release-template.yml.disabled`; narrowly necessary `projects/chirality-app-dev/frontend/scripts/**`; narrowly necessary `projects/chirality-app-dev/frontend/src/__tests__/**`; `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_UNSIGNED_RELEASE_WORKFLOW_2026-08-19/IMPLEMENTER_RETURN.md`.
- ExpectedOutputs: active unsigned macOS CI artifact workflow; deterministic/static regression proving the bounded triggers, least privilege, unsigned/unnotarized posture, required packaging/instruction-root evidence, CI artifact upload, and absence of release publication; any narrowly needed reusable artifact-verification script; concise return with exact files, commands/results, containment, residual risks, and the exact PR-CI proof still owed.
- AcceptanceCriteria:
  1. Triggers are bounded to PR/manual CI proof and cannot publish or respond to release tags; permissions are read-only/minimal and the job has a timeout/concurrency guard.
  2. Only the macOS 15+ Apple Silicon target is built; signing identity discovery and credential use are disabled; no signing, notarization, stapling, GitHub Release, Windows/Linux packaging, or distribution action is performed.
  3. Workflow explicitly verifies the produced app/DMG has no Developer ID authority and no notarized/accepted release posture, while tolerating the accepted unsigned/adhoc local-builder form; it fails closed if release signing/notarization posture appears.
  4. Existing build/package checks preserve packaged-dependency and instruction-root integrity evidence, with stable JSON evidence and the DMG/app artifact identity verified before upload.
  5. Upload uses only `actions/upload-artifact` for bounded CI artifacts and verification evidence, never GitHub Release APIs/actions; no secrets are requested or written.
  6. Deterministic tests/static validation would fail on the disabled predecessor's tag trigger, `contents: write`, signing-secret path, Windows job, or release-publication job.
  7. Applicable focused tests and proportional registered checks pass; actual macOS artifact execution is explicitly identified for PR CI.
  8. Exact changed paths remain inside AllowedWriteTargets.
- EXCLUSIONS: no signing, notarization, stapling, GitHub Release publication, external distribution, release-readiness/professional claims, provider/network expansion, dependency/lockfile change, lifecycle or Checking Approval SHA act, owner-machine deployment, deliverable state/evidence/receipt/decision/register/shared coordination write, commit, push, PR, or merge. Do not start another engineering node.
- Escalation: stop and return a precise blocker before any dependency/lockfile, runtime/root source, signing/notarization/publication, or additional-node need.
- ExpectedReturn: product-first summary, exact path list, commands/results, PR-CI proof command/check, containment, residual risks, and CHANGE-readiness recommendation without claiming acceptance.
