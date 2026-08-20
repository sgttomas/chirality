# Launch Brief — A2-PKG09-RUNATLOAD-IMPLEMENT-01

- RequestedBy: `WI-PKG09-RUNATLOAD-01`
- RunID: `APPDEV_LAUNCHAGENT_RUNATLOAD_PROOF_2026-08-20`
- ParentInstanceID: `WI-PKG09-RUNATLOAD-01`
- ChildInstanceID: `A2-PKG09-RUNATLOAD-IMPLEMENT-01`
- AgentType: `TASK` (Agent 2; no delegation)
- TaskSkill: `software-bounded-implementation`
- PackageID: `PKG-09`
- DeliverableIDs: [`DEL-09-04`]
- ScopePath: this child instance directory.
- ApplyEdits: `true`
- Objective: implement the smallest reusable fail-closed proof that a freshly
  bootstrapped packaged Chirality LaunchAgent launches automatically through
  `RunAtLoad`, without `kickstart`, in a disposable macOS CI/host account's
  actual `~/Library/LaunchAgents`.
- AcceptedBasis: D-APP-97 C1; DEL-09-04 SOW/live Remaining/dependencies; R6
  daemon-service evidence; frozen parent work graph v1; current unsigned
  Desktop CI workflow and shared LaunchAgent implementation.
- Dependencies: none; APP-HOLD-1 dispatch preflight `ALLOW`.
- DeclaredReads: root/project/TASK instructions; complete bounded-implementation
  skill pack; software profile; decision/deliverable/validation docs; current
  workflow; frontend packaging/daemon/CLI scripts and tests; shared runtime
  LaunchAgent/CLI implementation and tests.
- AllowedTools: repository reads/edits plus the complete
  `software-bounded-implementation` tool allowlist; focused npm/Vitest and only
  registered profile checks authorized below.
- AllowedWriteTargets:
  - `projects/chirality-app-dev/frontend/scripts/**`
  - `projects/chirality-app-dev/frontend/src/__tests__/scripts/**`
  - `projects/chirality-app-dev/frontend/package.json`
  - `.github/workflows/desktop-release-template.yml`
  - this child instance directory, including `_run_records/**`
- Tasks:
  - add a reusable Node proof script with injectable/process-safe seams for
    focused tests;
  - integrate it into the existing unsigned Desktop macOS job after the staged
    app exists;
  - use a unique non-default label and the runner account's actual
    `~/Library/LaunchAgents`, failing if HOME does not resolve to that actual
    location;
  - install/bootstrap the packaged app job and prove launchd starts it from
    `RunAtLoad` without any `kickstart` command;
  - bind the loaded job/process to the staged packaged executable identity;
  - always clean the process, launchd job, and plist, and verify all three are
    gone; preserve/prove the default label and default plist path were not
    touched;
  - emit a retained redacted JSON summary suitable for CI artifact upload;
  - add focused tests for success/failure/cleanup/default-protection and update
    existing workflow contract coverage.
- AcceptanceCriteria: no default label/path reference in mutation commands;
  actual `~/Library/LaunchAgents` asserted; no `kickstart`; automatic process
  launch observed and executable identity matches the packaged app; cleanup is
  fail-closed and verified for job/process/plist; script rejects unsafe labels,
  paths, missing packaged app, ambiguous process identity, and incomplete
  cleanup; focused tests/typecheck and applicable registered checks pass.
- AuthorizedRegisteredChecks: `frontend-test`, `frontend-typecheck`,
  `frontend-build`, `harness-self-check`, `app-hold-integrity` plus focused
  Vitest. Do not run packaging or launchd host proof locally against the owner
  account; PR CI owns the disposable-account proof.
- ExpectedReturn: structured TASK return with exact changed paths, behavior,
  focused/registered checks, proof summary contract, scope validation, residual
  PR-CI command/job, and blockers/reruns.
- EXCLUSIONS: default `com.chirality.runtime` job/plist; owner machine/account
  LaunchAgent state; owner deployment; signing/notarization/publication/
  distribution/release/lifecycle/reliance; provider/network expansion;
  dependencies/lockfiles; runtime package writes; other projects; decision and
  shared closeout registers; commits, pushes, PRs.
- Escalation: stop and return before any unsafe/default target, owner-state
  access, dependency change, unregistered check, release contract, or scope
  expansion.
