# WORKING_ITEMS activation — unsigned Desktop CI artifact workflow

- RunID: `APPDEV_UNSIGNED_RELEASE_WORKFLOW_2026-08-19`
- InstanceID: `WI-PKG09-DEL0905-01`
- PackageID: `PKG-09`
- SelectedDeliverables: `DEL-09-05` only
- Objective: apply D-APP-97 C1 by reactivating the Desktop release template as a least-privilege unsigned macOS CI artifact and release-verification workflow, without signing, notarization, GitHub Release publication, or external distribution.
- Selection authority: HELP_HUMAN frozen Agent-0 graph v1 and exact owner ruling D-APP-97 C1.
- Accepted basis: `origin/main` / local `HEAD` `57803893d1eb161f395e0574c256dd27920bf1d4` on `codex/app-unsigned-release-workflow-20260819`.
- Deliverable representation: `SOW_V1`; lifecycle and Checking Approval SHA are unchanged.
- Software profile: `software-workflow.json` under `docs/SOFTWARE_WORKFLOW_PROFILE.md`.
- APP-HOLD-1: dispatch preflight `ALLOW` for `DEL-09-05`; register SHA-256 prefix `e7408516`; scan fingerprint prefix `3e0e6d` (full values remain in the supervising preflight evidence).
- Declared reads: repo-wide governing, project, deliverable, product, test, workflow, build, packaging, and proof surfaces needed for this node.
- Product/build write boundary: `.github/workflows/desktop-release-template.yml`; retirement of `.github/workflows/desktop-release-template.yml.disabled`; and narrowly necessary `projects/chirality-app-dev/frontend/**` build/packaging scripts, tests, or config.
- Manager closeout writes: DEL-09-05 `_STATUS.md`, `MEMORY.md`, one bounded `_run_records/**` record, `plans/PLAN_COMPLETION_LOG.md`, and this RunID root.
- Exclusions: signing, notarization, GitHub Release publication, distribution, release-readiness claims, provider/network expansion, dependency/lockfile changes without escalation, lifecycle transition, owner-machine deployment, unrelated nodes/surfaces, decisions/registers, `LOOP_RECEIPTS.md`, commit, push, PR, or merge.
- Proof surfaces: deterministic/static/workflow and applicable project gates in-session; actual macOS unsigned artifact workflow on PR CI.
- Return contract: exact changed files and evidence, fresh independent read-only 100%-diff review PASS, blocker/PR-CI-rerun statement, derivative disposition, and CHANGE-ready status.
