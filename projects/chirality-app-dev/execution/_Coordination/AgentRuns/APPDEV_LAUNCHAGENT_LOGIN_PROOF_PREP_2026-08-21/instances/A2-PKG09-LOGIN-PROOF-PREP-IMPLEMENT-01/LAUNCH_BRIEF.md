# TASK launch brief — login proof preparation implementation

- RequestedBy: `WI-PKG09-LOGIN-PROOF-PREP-01`
- RunID: `APPDEV_LAUNCHAGENT_LOGIN_PROOF_PREP_2026-08-21`
- ParentInstanceID: `WI-PKG09-LOGIN-PROOF-PREP-01`
- ChildInstanceID: `A2-PKG09-LOGIN-PROOF-PREP-IMPLEMENT-01`
- WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
- ScopePath: `{REPO_ROOT}/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`
- PackageID: `PKG-09`
- DeliverableIDs: [`DEL-09-04`]
- TaskSkill: `software-bounded-implementation`
- ApplyEdits: `true`
- PROFILE_PATH: `{REPO_ROOT}/projects/chirality-app-dev/software-workflow.json`
- Objective: implement the smallest reusable, fail-closed App-local harness
  required to prepare and later capture proof that launchd discovered and
  auto-started a packaged Chirality LaunchAgent during an actual owner login
  session, without explicit bootstrap/kickstart in the proof path.
- AcceptedBasis: owner 2026-08-21 `PREPARE-THEN-OWNER` ruling; D-APP-97 C1;
  DEL-09-04 live kit/state/dependencies; R10/R11 D-APP-97 proof records; existing
  `frontend/scripts/run-packaged-launchagent-runatload-proof.mjs` and tests.
- Dependencies: none beyond the accepted packaged-app/CLI posture already
  represented by the existing proof harness.
- DeclaredReads: root/App AGENTS, AGENT_TASK, selected committed App workplan,
  software workflow profile, DEL-09-04 kit/state/evidence, existing proof
  scripts/tests/package manifest.
- AllowedWriteTargets:
  - `{REPO_ROOT}/projects/chirality-app-dev/frontend/scripts/**`
  - `{REPO_ROOT}/projects/chirality-app-dev/frontend/src/__tests__/scripts/**`
  - `{REPO_ROOT}/projects/chirality-app-dev/frontend/package.json` only if an
    npm script is essential
  - `{ScopePath}/_run_records/**`
  - this child instance `RETURN.md` / `STATUS.json`
- AllowedTools: repository reads/search, `apply_patch`, focused npm/Vitest,
  and the software-workflow tools allowed by the selected skill.
- ExpectedOutputs: product harness source, focused tests, a completed TASK run
  record, exact changed-path list, focused/registered check evidence, and
  residual risks.
- AcceptanceCriteria:
  1. Preparation installs only a unique non-default proof plist in the current
     GUI user's canonical `~/Library/LaunchAgents`, using the packaged CLI,
     with `RunAtLoad=true`, exact packaged daemon argv, persistent proof-only
     runtime data, and launcher rewrite disabled.
  2. Preparation refuses a pre-existing proof plist/job and does not invoke
     `launchctl bootstrap` or `kickstart`.
  3. One later capture invocation proves the prepared job was discovered and
     running after login, binds exact job argv/process/executable identity and
     source/session identity, packages redacted evidence, and then performs
     bounded fail-closed cleanup of proof-only process/job/plist/runtime state.
  4. Default label/plist are excluded and their pre/post posture is recorded;
     unsafe, stale, ambiguous, or incomplete evidence fails closed.
  5. The harness never performs logout/login and never claims proof during
     preparation; focused tests explicitly assert these boundaries.
- EXCLUSIONS: no logout/login execution; no action against
  `com.chirality.runtime`; no launcher mutation; no root/piping writes; no
  provider/network change; no signing/notarization/distribution/release claim;
  no workflow/CI expansion unless strictly necessary and explicitly escalated.
- Escalation: stop and return if the safe prepare/capture lifecycle cannot be
  implemented within these paths or requires owner-environment action now.
- ExpectedReturn: implementation summary, exact paths, check results, scope
  validation, limitations, and explicit statement that actual login proof is
  unexecuted and owner-gated.
