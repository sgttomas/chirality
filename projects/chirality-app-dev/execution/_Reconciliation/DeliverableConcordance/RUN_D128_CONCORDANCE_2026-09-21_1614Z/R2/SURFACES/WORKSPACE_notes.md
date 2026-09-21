# WORKSPACE capability inventory — notes (R1b, area WORKSPACE)

Area: `projects/chirality-app-dev/frontend/src/components/{workspace,pipeline,workbench,portal}/**` and
`frontend/src/lib/{workspace,pipeline,portal}/**` at frozen basis `00115c719` (18 files per
`R1_INVENTORY/IMPLEMENTATION_SURFACES.csv`, Area=WORKSPACE).
Output: `WORKSPACE_capabilities.csv`, 39 rows (`CAP-WORKSPACE-001`…`039`). Validator: `RESULT PASS errors=0 warnings=0`.
No deliverable folders were read.

## 1. Census

`CENSUS rows=39 LIVE=35 LEGACY_ONLY=0 TEST_ONLY=4 UNREACHED=0 ENABLED=25 DISABLED=14`

- Each row's first `REACH=` tag is its primary reach. Six LIVE rows (009, 018, 020, 022, 023, 024) also name a secondary legacy consumer
  (`lib/harness/mcp/read-tools.ts`, REACH=LEGACY_ONLY); that is not counted as a LEGACY_ONLY row.
- The 14 DISABLED rows are: 6 retired presentation rows (`RETIRED-UNMOUNTED`, 030–035), 3 statically LIVE helper
  rows whose only consumers are the retired surfaces (025, 026, 029), the dual-format migration path with no
  production caller (015), and the 4 TEST_ONLY rows (036–039).
- `PostReleaseBasis` is `NO` on every row. `TOUCHED_PATHS.csv` has no path under `projects/chirality-app-dev/frontend/**`.

## 2. Granularity rationale

- One row per observable behavior or contract surface. Providers are split by what consumers can observe:
  - `workspace-provider.tsx` has three rows: root persistence, the native picker (platform-gated) and the explicit selection signal.
  - `toolkit-provider.tsx` has three rows: storage fallback, turn options (live through the chat panel) and preset editing (UI only on the 404 route).
- `lib/workspace/filesystem.ts` (1302 lines) is split by route-visible behavior:
  - root normalization and errors;
  - the tree;
  - deliverable discovery;
  - knowledge detection;
  - the contract scanner, split four ways: kit findings, format and SOW v1, migration, and memory. References are a fifth row;
  - the scope scan.
  The migration row is separate because its enabled state differs from the rest.
- `lib/workspace/deliverable-contracts.ts` has one row per route operation (status read, content read, transition, dependency read and write) and one row for shared path containment.
- Retired surfaces keep one row per panel a deliverable could own:
  - Pipeline: selectors, scaffold, contracts;
  - Workbench: context, contracts;
  - Portal: role directory.
  This keeps retirement visible at capability level instead of hiding it in a single row.
- Helpers are folded into the behavior they serve. For example, `task-scope.ts`'s `buildDeliverableCompositeKey` is in the deliverables provider row.

## 3. Files covered versus total

`COVERAGE covered=18 total=18`

There are no uncovered files. The area has no stylesheets, `.d.ts` files or config files.

## 4. Dead, unreached, disabled or retired code observed

- **RETIRED-UNMOUNTED Pipeline, Workbench and Portal surfaces** (`pipeline-surface.tsx`, `workbench-surface.tsx`, `agent-matrix.tsx`).
  - REACHABILITY marks them LIVE through the chain `app/chat/page.tsx > shell/loop-shell.tsx > shell/tertiary-sidebar-tabs.tsx`. In practice they are never rendered:
    - Their only mount is `createTertiarySidebarTabs` (`shell/tertiary-sidebar-tabs.tsx:13-15`).
    - That function is called only by `LoopShell`, `PortalLoopShell` and `LoopTertiaryShell`.
    - Every page (`app/page.tsx`, `app/chat/page.tsx`, `app/pipeline/pipeline-client.tsx`, `app/workbench/workbench-client.tsx`) passes those shells as the `legacy` prop of `WovenDialogueRoute`, which discards it (`woven-dialogue-route.tsx:18`, `void legacy`).
    - `WovenDialogueShell` ignores `defaultSurface` (`woven-dialogue-shell.tsx:77`, `_props`).
  - The 404 route (`app/not-found.tsx`) renders `AppShell` → `WorkspaceSidebar` without the `pipelineTab`, `portalTab` or `workbenchTab` props. The tertiary tabs therefore never appear there either (`workspace-sidebar.tsx:107-110`).
  - Tests confirm it:
    - `woven-dialogue-shell.test.tsx:156-165` asserts that neither surface is mounted for the `workbench` or `pipeline` input;
    - `woven-dialogue-route.test.tsx` asserts that the legacy prop is not exposed.
  - `RoleDirectoryPanel` and its deprecated alias `AgentMatrixPanel` have no other production importer.
- **Statically LIVE helpers used only by retired UI:**
  - `lib/workspace/deliverable-api.ts` (all of it);
  - `task-scope.ts`'s `normalizeTaskScopeMode` and `sanitizeTaskSelection`.
- **Dead work at runtime:** `DeliverablesProvider` is mounted in `app/layout.tsx` and fetches `/api/project/deliverables` on every root change. Its only consumer, `useDeliverables`, is in the retired `PipelineSurface`, so the result is never read. The live `document-view.tsx` runs its own fetch of the same route.
- **Route-served but with no live UI caller:**
  - `/api/working-root/scope` (`scanProjectScopes`), `deliverable/status`, `status/transition` and `deliverable/dependencies` (GET and PUT).
  - Their callers are the retired surfaces and the legacy MCP tools in `lib/harness/mcp/read-tools.ts`.
  - The scope scan has no test.
- **Disabled path:** the `MIGRATION_DUAL` activation (`ScopeOfWorkMigrationActivation`) is supplied only by tests. The deliverables route calls `scanProjectDeliverables(projectRoot)` without options (`route.ts:13`), and a test asserts that a normal scan never infers migration.
- **TEST_ONLY modules** (confirmed: no importer in `src/`, `electron/` or `scripts/` outside `__tests__`; the grep hits in consent code are prose only):
  - `lib/pipeline/pipeline-dispatch-contract.ts`;
  - `lib/portal/agent-matrix-cells.ts` and `lib/portal/agent-matrix-launch.ts`;
  - `lib/workspace/governed-workflow.ts`;
  - `lib/workspace/navigation-intent.ts`.
- **Duplicates:**
  - `buildDeliverableCompositeKey` is defined in both `task-scope.ts` and `filesystem.ts`.
  - The Pipeline option tables are hard-coded in `pipeline-surface.tsx` and again in `pipeline-dispatch-contract.ts`.
  - Lifecycle gating rules are mirrored client-side in `deliverable-api.ts`.
- **Toolkit editor reach:** `OperatorToolkitPanel` is mounted only through `WorkspaceSidebar`. That sidebar is reachable only from the `app/not-found.tsx` `AppShell` and from the discarded loop shells. Toolkit values still reach live turns through `chat-panel.tsx` (`optsPayload`).

## 5. Method friction with §5.2

- **One STATE per row versus static LIVE reach.** Retired code is statically LIVE but never rendered. `REACH=LIVE` plus `STATE=DISABLED` plus `RETIRED-UNMOUNTED` expresses this, but a reader must know that REACHABILITY is module-level.
  - Proposal: add a `REACH=LIVE(static-only)` qualifier, or a Notes token `RENDER=NEVER`, so forward workers do not count these rows as live App behavior.
- **"Served but uncalled" routes.** A route handler is LIVE and ENABLED by definition, even when no live UI calls it. I used Notes text for this.
  - Proposal: a standard Notes token such as `NO-LIVE-CALLER`.
- **Mocked providers.** Nearly every component test mocks the workspace providers (checked with `vi.mock` counts). Importing a module in a test is therefore weak coverage evidence. Only `hosted-bootstrap.test.tsx` renders the real `WorkspaceProvider`.
  - Proposal: state in §5.2 that `CoveringTests` must exclude test files that only mock the module.
- **Rows that span two areas.** Some behaviors split across areas: toolkit logic is in `lib/harness/toolkit.ts`, the event bound in `lib/shell/harness-event-buffer.ts`, and transition rules in `lib/lifecycle`. I kept `Paths` inside the area and named the other files in Notes.

## 6. Effort

- About 25 files were touched by grep or line-range reads:
  - all 18 area files, 5 fully and the rest in ranges;
  - pages, the woven route and shell, tertiary tabs, the workspace sidebar, the app shell, document-view and the routes;
  - about 12 test headers.
- Test and consumer maps came from greps, not full reads.
- Context was comfortable, not tight.
