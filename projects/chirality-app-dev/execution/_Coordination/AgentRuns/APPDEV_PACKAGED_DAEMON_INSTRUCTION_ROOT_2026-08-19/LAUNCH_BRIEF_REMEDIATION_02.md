# Sealed Agent 2 brief — D-APP-100 proof remediation 02

- RequestedBy: `WORKING_ITEMS`
- RunID: `APPDEV_PACKAGED_DAEMON_INSTRUCTION_ROOT_2026-08-19`
- ParentInstanceID: `AGENT1-PKG09-WORKING-ITEMS`
- ChildInstanceID: `A2-DAPP100-IMPLEMENT-02`
- PackageID: `PKG-09`
- DeliverableID: `DEL-09-04`
- TaskSkill: `software-bounded-implementation`
- ApplyEdits: `true`
- Objective: remediate exactly the four actionable findings in `REVIEW_RETURN_01.md` without expanding D-APP-100 product behavior.
- DeclaredReads: original implementation brief/return; review brief/return; complete proof script and its focused tests/callers.
- AllowedTools: read/search, `apply_patch`, proof-script syntax and focused tests. Do not run package/host proof; manager owns it after fresh review.
- AllowedWriteTargets: `projects/chirality-app-dev/frontend/scripts/run-packaged-daemon-instruction-root-proof.mjs`; proof-specific tests under `projects/chirality-app-dev/frontend/src/__tests__/scripts/**`; this run root `REMEDIATION_RETURN_02.md`.
- AcceptanceCriteria:
  1. Every spawned pack/CLI/Electron command has a deadline and terminal cleanup escalates SIGTERM to SIGKILL while awaiting confirmed exit.
  2. Proof freshness binds the exact tested app path to the exact current invocation's pack output/marker or captured content identity; `--app` and `--skip-pack` cannot falsely certify stale or unrelated bytes.
  3. Canonical summary is invalidated/replaced with `PENDING` before proof work and atomically becomes `FAIL` on every caught failure, so stale PASS cannot survive.
  4. Log offsets use one correct unit for non-ASCII text.
  5. New focused regression tests cover the failure modes and pass; syntax and diff hygiene pass.
- EXCLUSIONS: no production resolver/main/integration regression changes unless an actionable proof-test dependency makes them mechanically necessary and is escalated first; no runtime/manifest/dependency/lockfile/deliverable/receipt/decision/register/Git writes; all original release/security exclusions remain.
- ExpectedReturn: exact diff, tests, containment, residual risks, and fresh-review readiness.
