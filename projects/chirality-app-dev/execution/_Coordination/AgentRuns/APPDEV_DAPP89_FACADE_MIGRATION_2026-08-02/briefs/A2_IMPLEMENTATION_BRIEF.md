# A2 Implementation Brief — D-APP-89 Option B

RequestedBy: App `HELP_HUMAN` through `WORKING_ITEMS`

RunID: `APPDEV_DAPP89_FACADE_MIGRATION_2026-08-02`

ParentInstanceID: `WI-PKG03-DAPP89-B`

ChildInstanceID: `TASK-DAPP89-MIGRATION-01`

TaskSkill: `software-bounded-implementation`

PackageID: `PKG-03`

DeliverableIDs: `DEL-03-01`

ScopePath: `projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-01_AgentEnginePort_and_Engine_Conformance_Suite`

PROFILE_PATH: `projects/chirality-app-dev/software-workflow.json`

ApplyEdits: `true`

## Objective

Mechanically migrate every executable App importer and App build/config
dependency from `@chirality/harness-contract` to equivalent existing
`@chirality/runtime-contracts` root/subpath exports, while retaining
`frontend/packages/harness-contract/**` intact and tested as the rollback
compatibility package. Preserve runtime behavior and public contract shapes.

## Accepted basis

- Git base HEAD `97678a841ef58345c73d3470ed8de57c9b1405d2` on
  `codex/appdev-planning-gates-20260802`, plus the pre-existing uncommitted
  D-APP-86..89 planning/ruling/register tranche. Preserve those bytes.
- D-APP-89 packet SHA-256
  `7dc274ac9d8d081947420c2155954adef9e5f0d2987e8e0913c0b84f8eabb8dc`.
- D-APP-89 ruling SHA-256
  `5b651cb41c3e69e59d26d12c32331d4c6918cc77e590e228dd90fbd8d5da0f22`.
- DEL-03-01 pre-run `_STATUS.md` SHA-256
  `328dd412f829f1cea44913449fb05df52165dbcd2cf927827dff8bd4bab6270b`;
  lifecycle is `IN_PROGRESS` and Checking Approval SHA is
  `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`.
- `docs/SOFTWARE_WORKFLOW_PROFILE.md`, project-local
  `projects/chirality-app-dev/software-workflow.json`, and TASK skill
  `skills/software-bounded-implementation/`.

## Declared reads

- the exact App frontend consumers, manifests, config, validators, tests, and
  retained facade package;
- Root `runtime/package.json`, `runtime/packages/contracts/**`, and focused
  Root runtime contract tests as read-only evidence;
- D-APP-49/73/76/81/89 evidence and DEL-03-01 status/memory/ScopeOfWork only
  as needed to preserve boundaries;
- repository validation scripts and current Git diff/status as read-only
  evidence.

## Allowed tools

- repository-native read/search and patch/editor operations;
- `python3 tools/software_workflow/select_affected_checks.py`;
- `python3 tools/software_workflow/run_registered_checks.py`;
- `python3 tools/software_workflow/validate_change_scope.py`;
- `python3 tools/software_workflow/verify_generated_manifest.py`;
- `python3 tools/software_workflow/compare_structured.py`.

The project profile's registered checks may be run through
`run_registered_checks.py`. Ordinary managed execution under this sealed brief
is not an Agent-2 arbitrary Bash capability grant. If the runtime requires a
separate Bash grant to perform an operation, fail closed and return it.
Do not install, release, publish, access the network, or use destructive tools.

## Allowed write targets

- `projects/chirality-app-dev/frontend/src/**` only where mechanically
  required for executable import/reference migration;
- `projects/chirality-app-dev/frontend/package.json`;
- `projects/chirality-app-dev/frontend/package-lock.json`;
- `projects/chirality-app-dev/frontend/tsconfig.json`;
- `projects/chirality-app-dev/frontend/next.config.mjs`;
- relevant App contract-dependency validator/tests only when required to
  remove facade load-bearing wiring;
- `projects/chirality-app-dev/frontend/packages/harness-contract/**` only for
  rollback-package tests/docs/metadata needed to prove it remains buildable;
  preserve all compatibility exports;
- DEL-03-01 `_STATUS.md`, `MEMORY.md`, and
  `_run_records/APPDEV_DAPP89_FACADE_MIGRATION_2026-08-02/**`;
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP89_FACADE_MIGRATION_2026-08-02/**`.

Do not touch any other file. The parent is sole integration owner for any
needed shared synthesis after your return.

## Required tasks and outputs

1. Capture an execution-time before census of every exact
   `@chirality/harness-contract` string and categorize production, tests,
   config/scripts, lock/workspace, retained facade, and historical/docs.
2. Build a path-complete mapping from each used facade root/subpath export to
   the exact existing Root `@chirality/runtime-contracts` export/subpath.
   Stop on any missing or semantically non-equivalent export.
3. Apply the minimum coherent import/build-config migration without behavior
   change. Retain the facade and its compatibility exports.
4. Add or adjust dedicated rollback-package tests/documentation only as
   required to prove the facade still builds and resolves to the same Root
   contract identities.
5. Capture the after census proving zero executable App references outside
   the retained facade and its dedicated rollback tests. Precisely enumerate
   package/workspace/lock/historical strings that remain and explain why.
6. Record a complete before/after mapping, exact changed-path SHA-256 manifest,
   exact rollback sequencing/bytes boundary, affected-client statement, and
   release/no-reliance disposition under the run root and deliverable run
   record. Do not assert Root/Piping/PEC consumer state without evidence.
7. Run the D-APP-89 minimum validation. Use registered profile helpers where
   applicable. For required commands not registered in the App profile, run
   only if ordinary managed execution is available without a separate Bash
   capability grant; otherwise return the exact blocked command and reason.
   Required set: Root runtime build/typecheck; focused Root/App contract
   export/identity tests; App full tests, typecheck, contract-deps, build,
   desktop pack; zero-consumer assertion; receipt, corpus, practitioner,
   self-check, diff, and containment checks.
8. Update DEL-03-01 `_STATUS.md` and `MEMORY.md` only to record this bounded
   migration and the true residual: facade retirement remains a later owner
   gate. Preserve `IN_PROGRESS`, Checking Approval SHA, dependencies, and all
   unrelated history.
9. Return status, outputs, exact hashes, validation results, blockers/reruns,
   derivative status, and next owner. Do not commit, push, merge, close the
   deliverable, or claim retirement readiness.

## Exclusions

- facade deletion or removal of any facade export;
- DEL-03-01 lifecycle transition, dependency disposition, or closure;
- Root/runtime source writes or claims of generic runtime-contract
  implementation;
- Piping/PEC writes or consumer claims without evidence;
- PRD/authority corpus, decomposition, scope-change, Task Management,
  receipts, completion log, decision packets/register, and Git state;
- provider/network, sandbox/Bash, release, distribution, publication,
  professional reliance, or acceptance authority;
- the six D-APP-81 `HISTORICAL_RELATION_UNKNOWN` relations.

## Acceptance criteria

The parent can accept the return only if all nine gates in the frozen
orchestration plan are evidenced, all writes stay inside the whitelist, the
facade remains intact, the zero-consumer assertion is reproducible, and every
failed/unavailable required command is diagnosed without weakening the end
state.

## Expected return

A terminal structured return plus durable run records and evidence files
covering before/after census, complete export mapping, exact manifests and
hashes, rollback, affected clients, registered and direct validation results,
containment, preservation boundaries, residual risks, rerun triggers,
derivative status, and next owner.
