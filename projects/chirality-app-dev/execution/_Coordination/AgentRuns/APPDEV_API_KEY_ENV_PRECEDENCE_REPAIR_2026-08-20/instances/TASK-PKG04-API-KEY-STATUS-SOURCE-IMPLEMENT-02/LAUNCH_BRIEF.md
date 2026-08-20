# TASK-PKG04-API-KEY-STATUS-SOURCE-IMPLEMENT-02 — sealed brief

- RequestedBy: `WI-PKG04-API-KEY-PRECEDENCE-01`
- RunID: `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
- ParentInstanceID: `WI-PKG04-API-KEY-PRECEDENCE-01`
- ChildInstanceID: `TASK-PKG04-API-KEY-STATUS-SOURCE-IMPLEMENT-02`
- Role: `TASK` Agent 2
- TaskSkill: `software-bounded-implementation`
- PackageID: `PKG-04`
- DeliverableIDs: `DEL-04-05`
- ScopePath: `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge`
- Objective: amend `SafeStorageCredentialStore.status` to expose a non-secret
  `ui | env | none` source discriminator that accurately reflects the same
  provider credential chosen by `get`, while preserving the accepted
  safeStorage > `ANTHROPIC_API_KEY` > `CHIRALITY_ANTHROPIC_API_KEY` order and
  all provider/get/set/remove behavior.
- AcceptedBasis: working candidate from accepted N1 v1 product identity
  (`api-key-storage.ts`
  `72e9cdb9fabb5beb77ba009933dbb8c1375f012ac0162e088d96a460fe5baaab`;
  focused test
  `56b36a5ed44885877d692ad6357b6ee209f96edb8844aec2f5781d6c0a5b4fe7`),
  plus frozen `ORCHESTRATION_PLAN_V2.md`, `WORK_GRAPH_V2.md`, N2 amendment
  v2, SPEC 12.3, PRD FR-030, and DEL-04-05 RQ-001/RQ-004/AC-001/VER-001.
- Dependencies: APP-HOLD amended dispatch preflight `ALLOW`.
- ApplyEdits: `true`
- AllowedWriteTargets:
  - `projects/chirality-app-dev/frontend/electron/api-key-storage.ts`
  - `projects/chirality-app-dev/frontend/src/__tests__/electron/api-key-storage.test.ts`
  - `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge/_run_records/`
  - this child instance's `STATUS.json` and `RETURN.md`
- PROFILE_PATH: `projects/chirality-app-dev/software-workflow.json`
- AuthorizedChecks: focused API-key-storage Vitest; registered frontend test,
  frontend/Electron typecheck, and build; exact-path scope/whitespace checks.
- AcceptanceCriteria:
  - status returns only `{ configured, source }`, never credential material;
  - persisted safeStorage reports `ui` even when one or both Anthropic
    environment values coexist;
  - canonical-only and compatibility-only Anthropic credentials report `env`;
  - oMLX persisted/environment/none states report `ui`/`env`/`none` without
    consulting Anthropic variables;
  - unsupported/unconfigured providers report non-secret none status;
  - accepted environment order and all get/set/remove behavior remain intact;
  - no root runtime contract, IPC, other package, dependency, or lockfile edit.
- EXCLUSIONS: IPC consumer/tests, root runtime contracts, lifecycle/status/
  memory/evidence calibration, other packages, shared fan-in/receipt/completion
  log, Git commit/push/PR, provider/storage/error redesign.
- ExpectedReturn: exact changed paths and API shape, focused/full check results,
  write-scope validation, residual risks, blockers, coordination notices.
- ModelAttribution: OpenAI Codex; exact model build not exposed.
