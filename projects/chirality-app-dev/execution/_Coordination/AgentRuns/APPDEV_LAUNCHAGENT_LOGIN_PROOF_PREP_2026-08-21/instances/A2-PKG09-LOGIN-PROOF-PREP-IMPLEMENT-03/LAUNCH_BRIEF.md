# TASK launch brief — login proof preparation implementation retry 2

- RequestedBy: `WI-PKG09-LOGIN-PROOF-PREP-02`
- RunID: `APPDEV_LAUNCHAGENT_LOGIN_PROOF_PREP_2026-08-21`
- ParentInstanceID: `WI-PKG09-LOGIN-PROOF-PREP-02`
- ChildInstanceID: `A2-PKG09-LOGIN-PROOF-PREP-IMPLEMENT-03`
- WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
- ScopePath: `{REPO_ROOT}/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`
- PackageID: `PKG-09`
- DeliverableIDs: [`DEL-09-04`]
- TaskSkill: `software-bounded-implementation`
- ApplyEdits: `true`
- PROFILE_PATH: `{REPO_ROOT}/projects/chirality-app-dev/software-workflow.json`
- Objective: inspect, repair or replace, and validate the smallest reusable,
  fail-closed App-local harness that prepares and later captures proof that
  launchd discovered and auto-started packaged Chirality during an actual
  owner login session, without explicit bootstrap/kickstart in the proof path.
- Starting candidate: unvalidated recovery bytes at
  `frontend/scripts/run-packaged-launchagent-login-proof.mjs` and
  `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`.
  Treat them as untrusted input and assume sole write ownership while active.
- AcceptedBasis: owner 2026-08-21 `PREPARE-THEN-OWNER` ruling; D-APP-97 C1;
  DEL-09-04 live kit/state/dependencies; R10/R11 D-APP-97 proof records; existing
  packaged RunAtLoad proof script/tests; manager takeover and work-graph
  amendment 02.
- Dependencies: N1 attempt 1 and N1-R1 attempt 2 are interrupted and provide
  no accepted return. APP-HOLD dispatch preflight is `ALLOW` at
  `b1876a5e0f0083e10c0c18255cd92ed0079b63a2`.
- DeclaredReads: root/App AGENTS, AGENT_TASK, selected committed App workplan,
  software workflow profile, software-bounded-implementation skill and
  companions, DEL-09-04 kit/state/evidence, existing RunAtLoad and candidate
  proof scripts/tests, package manifest.
- AllowedWriteTargets:
  - `{REPO_ROOT}/projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs`
  - `{REPO_ROOT}/projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`
  - `{ScopePath}/_run_records/TASK_RUN_2026-08-20_2206.md`
  - this child instance `RETURN.md` / `STATUS.json`
- AllowedTools: repository reads/search and patch editing; focused Vitest; and
  the deterministic tools permitted by the selected skill. Do not invoke the
  prepare/capture harness against the live host.
- ExpectedOutputs: corrected product harness source, focused tests, finalized
  TASK run record, exact changed-path list, focused check and scope evidence,
  and residual risks.
- AcceptanceCriteria:
  1. `prepare` uses only a unique non-default label/plist in the current GUI
     user's canonical `~/Library/LaunchAgents`, invokes the packaged CLI, sets
     `RunAtLoad=true`, exact packaged daemon argv, persistent proof-only data,
     and disables launcher rewrite.
  2. `prepare` refuses a pre-existing proof job/plist and does not bootstrap or
     kickstart anything.
  3. One later `capture` invocation requires evidence of login discovery and a
     running process, binds exact job argv/process/executable/session/source
     identity, emits redacted evidence, and boundedly cleans only proof-owned
     job/plist/runtime state.
  4. Default label/plist pre/post posture is recorded without mutation. Stale,
     ambiguous, unsafe, or incomplete evidence fails closed.
  5. The harness never performs logout/login and preparation never claims the
     proof. Focused tests explicitly assert owner-act, no-bootstrap,
     no-default, and no-launcher boundaries.
  6. Focused tests pass and all changed product/test paths remain in scope.
- EXCLUSIONS: no logout/login execution; no action against
  `com.chirality.runtime`; no launcher mutation; no root/piping writes; no
  provider/network change; no signing/notarization/distribution/release claim;
  no workflow/CI expansion; no Git action.
- Escalation: stop and return if the safe lifecycle cannot be completed in the
  two product/test paths or needs owner-environment action now.
- ExpectedReturn: implementation summary, exact paths, check results, scope
  validation, residual limitations, and explicit statement that actual login
  proof remains unexecuted and owner-gated.
