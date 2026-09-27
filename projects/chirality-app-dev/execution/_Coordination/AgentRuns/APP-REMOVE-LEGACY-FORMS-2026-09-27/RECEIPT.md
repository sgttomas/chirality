# Receipt — APP-REMOVE-LEGACY-FORMS-2026-09-27

Derivative account. The [work graph](../../WorkGraphs/app-lifecycle-deps-2026-09-26/WORK_GRAPH.md)
(row FU3) records the withdrawal, and the sources below keep their authority.

## Owner direction

CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING. Ryan Tufts, 2026-09-27, Claude Code
conversation:

> We don't need to carry the Workbench or Pipeline forms any longer. They are obsolete.

As the parent session relayed it, this run removes the Workbench and Pipeline
form surfaces and the code, CSS and tests only they used. It keeps the
deliverable HTTP API routes, the client fetch functions that call them,
`deliverable-contracts.ts`, `lib/lifecycle/*`, `lib/dependencies/*` and the MCP
tools. Whether the deliverable routes are still needed is being asked of the
owner separately.

## Result

- **Removed product source.**
  `frontend/src/components/workbench/workbench-surface.tsx`,
  `frontend/src/components/pipeline/pipeline-surface.tsx` and
  `frontend/src/components/pipeline/lifecycle-gate-fields.tsx`. Both component
  folders are now empty and gone.
- **Removed tests.** `frontend/src/__tests__/components/workbench-surface.test.ts`,
  `pipeline-surface.test.ts` and `lifecycle-transition-gates.test.tsx`.
- **Tab entries.** `createTertiarySidebarTabs` (`components/shell/tertiary-sidebar-tabs.tsx`)
  now returns only the Portal tab.
- **Client helpers.** `frontend/src/lib/workspace/deliverable-api.ts` keeps
  `WorkspaceApiClientError`, the request helper, the snapshot, result and input
  types, and the three fetch functions. It loses the helpers only the forms
  used: `workspaceApiErrorMessage`, `currentIsoDate`, `nextLifecycleTargets`,
  `requiresApprovalShaForTarget`, `lifecycleTransitionTargets`,
  `lifecycleTransitionEvidence` (with its kind, field and evidence types),
  `lifecycleTransitionTargetLabel`, `lifecycleTransitionErrorMessage` and its
  refusal hints, `canAgentTransitionLifecycle`, `isExecutionBlockerSubsetRow`,
  `summarizeDependencyRows` and `DependencyRowSummary`, `NO_METRIC`,
  `formatBlockingUpstreamMetric`, `DECLARED_READINESS_CAVEAT` and
  `formatBlockingUpstreamNote`, with their private constants. Each was checked
  by search: no other product module imports it.
- **Client tests.** `__tests__/lib/workspace-deliverable-api.test.ts` keeps the
  fetch-function tests. The test that posts a reopening now checks the thrown
  `WorkspaceApiClientError` (status, code, message and the checker's
  `refusalCode` in `details`) instead of the removed message formatter. The
  tests of the removed helpers go with them.
- **CSS.** `frontend/src/app/globals.css` drops the rules for classes only the
  forms used (`pipeline-layout`, `pipeline-grid`, `pipeline-card*`,
  `pipeline-summary`, `pipeline-note`, `pipeline-contract*`,
  `pipeline-transition-*`, `workbench-layout`, and the whole
  `workbench-documents-block` section, formerly C5). `workbench-card` stays,
  because `app/not-found.tsx` uses it.
- **Woven tests.** `woven-dialogue-shell.test.tsx` and
  `woven-dialogue-runtime-reconnect.test.tsx` drop their mocks of the two
  removed modules. The shell test drops its two assertions that the rendered
  dialogue contains no Workbench or Pipeline marker: those markers came only
  from the removed mocks. A comment now gives the actual reason
  `DocumentView` is mocked (the navigator and right panel import it).
- **Kept after a check.** `lib/workspace/task-scope.ts` and its test stay. The
  Pipeline form was their only product consumer, but DEL-08-03 owns
  dynamic task-scope semantics and names `task-scope-selection.test.ts` as a
  verification hook. `DeliverablesProvider` stays mounted in `app/layout.tsx`
  (see the dead-code list below).
- **Records.**
  - App SPEC §5.2 no longer names the Workbench and Pipeline contract panels as
    dependency readers, or the client-side `activeUpstreamBlockerCandidates`
    count and panel caveat; the API and MCP rules are unchanged. §17.3 item 6
    no longer lists Workbench and Pipeline among the re-hosted controls and says
    the forms were removed on this date. §4.3 had no form wording.
  - Work-graph FU3: WITHDRAWN by owner direction; the D-APP-36 render-evidence
    item is closed as moot. FU4 notes the hook change.
  - DEL-07-04 CLM-003 (FU4 hooks): the removed form test is replaced by the
    MCP tool test `chirality-mutating-mcp.test.ts`, which covers the same
    reversal and reopening gates. CLM-008 cited no form test and is unchanged.
    DEL-07-04 is IN_PROGRESS.
  - DEL-02-02 CLM-012 (IN_PROGRESS): the verification hooks for REQ-004, 005,
    006 and 011 no longer name removed tests and say what remains.
  - DEL-08-03 CLM-005 and CLM-006 (IN_PROGRESS): the sentences naming the
    retained Pipeline component and its tests as compatibility evidence now say
    they were removed.
  - The APP-TRANSITION-FORMS receipt has a dated note; its `render/` evidence is
    unchanged.
  - MEMORY rows for DEL-07-04, DEL-02-02 and DEL-08-03; `loop/LOOP_RECEIPTS.md`
    Receipt-269; tranche manifest
    `docs/governance_harness/tranche_manifests/APP-REMOVE-LEGACY-FORMS-20260927.yaml`.
- **Other App docs.** `frontend/docs`, `docs/`, `README.md` and
  `frontend/docs/harness/TRACEABILITY.md` name none of the removed components.
  Historical plans and run records that name them are unchanged.

## Deliverable map and open scope conflict

No ISSUED deliverable names the removed components; the App has no deliverable
in `2_Checking` or `3_Issued`. Three IN_PROGRESS deliverables did, and only
their verification hooks were changed, as directed. Accepted scope text still
says the forms' code and tests are retained or required:

- **DEL-02-02** (`Workbench and Pipeline Selection UX`): the controlling
  SCA-APP-010 Gate-5 acceptance obligation 1 says Workbench and Pipeline are
  unmounted "with code, routes, and tests retained". Its requirements REQ-001
  to REQ-011 and CLM-014 describe the Workbench and Pipeline forms, and REQ-004
  names the removed `canAgentTransitionLifecycle`. Its `_STATUS.md` history
  records D-APP-86 packaged evidence of the re-hosted Workbench and Pipeline.
- **DEL-08-03**: obligation 2 and the applied row note say the Pipeline
  presentation is retired "(code retained)"; the applied row outputs include
  "Pipeline selector tests".
- **Accepted decomposition** v3.2 (applied by SCA-APP-010) says "Workbench,
  Pipeline, and the Work projection are unmounted, not deleted", and the
  SCA-APP-010 brief lists "Deletion of Workbench, Pipeline, or Work-projection
  code, routes, or tests" as an exclusion of that amendment.
- **App PRD §8.2** FR-010 to FR-012 still require WORKBENCH contract checks and
  PIPELINE category and TASK selectors. App `docs/PLAN.md` §1 and §13 and PRD
  §2, §6, §7, §15 (KG-033) and §16 describe Workbench and Pipeline as surfaces.

These texts were not edited. Changing them changes accepted scope or product
requirements. That needs an owning record: a scope-change amendment for the
decomposition note and the deliverable obligations, or an owner ruling that
names what this direction supersedes. **This candidate should not merge until
the owner chooses that route.** The routes `/workbench` and `/pipeline` still
resolve (D-APP-108 Q3 is unaffected).

## Legacy shell: what remains dead (not removed)

Every route renders `WovenDialogueRoute`, which discards its `legacy` prop. By
import reachability from the App's page, layout, route and Electron entry
points, these modules are reachable only through that discarded prop:
`components/shell/loop-shell.tsx`, `portal-loop-shell.tsx`,
`loop-tertiary-shell.tsx`, `sidebar-right-loop-layout.tsx`,
`tertiary-sidebar-tabs.tsx` and `components/portal/agent-matrix.tsx`. Also dead
now:

- the `workbenchTab` and `pipelineTab` props, `WORKBENCH_TAB`/`PIPELINE_TAB` and
  the `'workbench'`/`'pipeline'` tab ids in `workspace-sidebar.tsx` and
  `sidebar-right-loop-layout.tsx` (no caller supplies them);
  `workspace-sidebar.test.ts` still exercises the slots with placeholders;
- `defaultSidebarTab="workbench"`/`"pipeline"` and the form subtitles in
  `app/workbench/workbench-client.tsx` and `app/pipeline/pipeline-client.tsx`,
  and the `LoopTertiaryShell` comment that a route form opens in the sidebar;
- `DeliverablesProvider` in `app/layout.tsx`: `useDeliverables` has no consumer,
  yet the provider still fetches `/api/project/deliverables` when the working
  root changes;
- `/api/working-root/scope` (its only caller was the Workbench form) and the
  `scaffoldHarnessExecutionRoot` client, whose only App caller was the Pipeline
  form (the `/api/harness/scaffold` route is kept);
- `task-scope.ts` `normalizeTaskScopeMode` and `sanitizeTaskSelection`: tests
  only (kept for DEL-08-03, above);
- the CSS rule `.woven-focused-surface > .panel`, which no component renders
  (it was already dead).

`lib/pipeline/pipeline-dispatch-contract.ts` and the `lib/portal/agent-matrix-*`
helpers were already without a product importer before this run.

## Client fetch functions now unused

`fetchDeliverableStatus`, `fetchDeliverableDependencies` and
`transitionDeliverableStatus` in `lib/workspace/deliverable-api.ts` (with
`WorkspaceApiClientError` and the snapshot, result and input types) have no
product caller; only their tests use them. They are kept pending the owner's
answer on the deliverable routes. The server-side
`transitionDeliverableStatus` in `deliverable-contracts.ts`, used by the
transition route and the MCP tools, is a different function and is in use.

## Checks (worktree candidate)

Recorded in the hand-off to the parent session, with exit codes: typecheck;
full Vitest (the known uid-0 `harness-attachment-resolver` failure is the only
failure); the Root validators G0–G3, receipt, tranche-manifest, conflict-marker,
run-record-leak and whitespace checks; the practitioner-harness self-check;
export regeneration; the APP-HOLD dispatch check for DEL-07-04, DEL-02-02 and
DEL-08-03 (ALLOW) and the APP-HOLD scan. The App has no lint script.

## Limits

- The open scope conflict above blocks merge until the owner chooses the route.
- No build or packaged run; the removed modules were not mounted in the live
  App, so no rendered behaviour changes. No D-APP-36 render evidence is needed
  for a removal of unmounted forms.
- The App authority corpus already drifted for the App SPEC; the drift is
  retained, not repinned.
- No lifecycle transition, approval-SHA refresh, dependency change, Runtime
  change, route removal, release or issuance.

Execution: a Claude Code subagent (TASK-type executor, no delegation) in an
isolated worktree for the parent session. Model identifiers are withheld at the
dispatching session's instruction; the commit's session trailer identifies the
run.
