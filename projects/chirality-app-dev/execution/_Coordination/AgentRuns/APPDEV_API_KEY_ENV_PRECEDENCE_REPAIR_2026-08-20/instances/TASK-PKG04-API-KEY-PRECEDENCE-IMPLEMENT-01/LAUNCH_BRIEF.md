# TASK-PKG04-API-KEY-PRECEDENCE-IMPLEMENT-01 — sealed brief

- RequestedBy: `WI-PKG04-API-KEY-PRECEDENCE-01`
- RunID: `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
- ParentInstanceID: `WI-PKG04-API-KEY-PRECEDENCE-01`
- ChildInstanceID: `TASK-PKG04-API-KEY-PRECEDENCE-IMPLEMENT-01`
- Role: `TASK` Agent 2
- TaskSkill: `software-bounded-implementation`
- PackageID: `PKG-04`
- DeliverableIDs: `DEL-04-05`
- ScopePath: `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge`
- Objective: implement the minimum production/test repair so Anthropic key
  resolution is UI safeStorage first, `ANTHROPIC_API_KEY` second, and
  `CHIRALITY_ANTHROPIC_API_KEY` third; replace the self-expiring expected-fail
  test with positive regression coverage for all relevant precedence cases.
- AcceptedBasis: branch base
  `6710ee6354debc201f6a454e2802897026cd4b38`; accepted
  `docs/SPEC.md` Section 12.3; `docs/PRD.md` FR-030;
  `DEL-04-05-RQ-001`, `AC-001`, and `VER-001`; Receipt-180 blocker; owner
  authorization recorded in the run orchestration plan.
- Dependencies: APP-HOLD dispatch preflight `ALLOW`.
- ApplyEdits: `true`
- AllowedWriteTargets:
  - `projects/chirality-app-dev/frontend/electron/api-key-storage.ts`
  - `projects/chirality-app-dev/frontend/src/__tests__/electron/api-key-storage.test.ts`
  - `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge/_run_records/`
  - this child instance's `STATUS.json` and `RETURN.md`
- AllowedTools: repository reads and patch edits; focused Vitest and only the
  brief-authorized registered software-workflow checks; scope/whitespace/diff
  inspection. No installs, network, release, destructive, or Git publication
  actions.
- PROFILE_PATH: `projects/chirality-app-dev/software-workflow.json`
- AuthorizedChecks: focused API-key-storage Vitest; registered
  `frontend-test`, `frontend-typecheck`, and `frontend-build` if time permits;
  `validate_change_scope.py` before return.
- AcceptanceCriteria:
  - persisted UI credential wins over both environment variables;
  - with no stored UI credential, `ANTHROPIC_API_KEY` wins when both are set;
  - each environment variable works alone and whitespace-only values fall
    through truthfully;
  - oMLX/provider isolation is unchanged;
  - expected-failure is replaced by ordinary positive tests;
  - no provider, storage, persistence, error, public-contract, dependency, or
    lockfile expansion;
  - all changed paths remain inside the declared fence.
- EXCLUSIONS: DEL-04-05 lifecycle/status/memory/evidence calibration; other
  packages; shared run fan-in; receipt/completion log; Git commit/push/PR.
- ExpectedReturn: exact changed paths and behavior, check commands/results,
  scope validation, residual risks, blockers, and coordination notices.
- ModelAttribution: OpenAI Codex; exact model build not exposed.
