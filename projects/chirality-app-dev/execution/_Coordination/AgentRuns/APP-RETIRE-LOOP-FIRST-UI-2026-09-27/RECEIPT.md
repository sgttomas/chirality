# Receipt — APP-RETIRE-LOOP-FIRST-UI-2026-09-27

Derivative account of the SCA-APP-012 code change. SCA-APP-012 and the
sources below keep their authority.

**Status: checkpoint-group-3 candidate, awaiting the owner's acceptance.**
This is the code side of SCA-APP-012. The owner has accepted checkpoint
groups 1 and 2. Checkpoint group 3 is **not** accepted: it reviews this code
candidate together with the SCA-APP-012 scope-text candidate (choice Q-a).
After the owner accepts group 3, one PR lands both. Nothing here is pushed or
merged.

## Authority

**Scope-change amendment SCA-APP-012**
(`execution/_ScopeChange/SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/`):

- Checkpoint group 1, accepted by the owner on 2026-09-27 ("Accept SCA-APP-012
  group 1: R-b, W-b, P-keep (keeping the two pages, as recommended),
  defaults."): snapshot
  `execution/_ScopeChange/checkpoint_snapshots/SCA-APP-012_GROUP-1_2026-09-27/`
  (`DECISION.md` SHA-256
  `0bc055869d3b29f6fc719ad8eb376f580073eaabafd5f75faa1978d10cbc6abe`,
  `ACCEPTED_MANIFEST.csv` SHA-256
  `86b0f7cb87ba45c8a0655088864905e20467ed60442a13f4f267ed27a4387056`) and
  pointer `SCA-APP-012_GROUP-1_AUTHORIZED.md`. It accepted BASE, S, R-b, W-b,
  P-keep and the defaults L-lib, S-tool and E.
- Checkpoint group 2, accepted by the owner on 2026-09-27 ("Accept SCA-APP-012
  group 2: T-a, Q-a."): snapshot
  `execution/_ScopeChange/checkpoint_snapshots/SCA-APP-012_GROUP-2_2026-09-27/`
  (`DECISION.md` SHA-256
  `d828e975c3e0d313a49d0b65980462047b506342586c3260af860f4cc3d5d428`,
  `ACCEPTED_MANIFEST.csv` SHA-256
  `0574aca5909331732e5791eea8ef023cd6b2fb5f1a7f45f024acb8443cce6ac9`),
  recorded at commit `dad463311` on the scope-change branch, with pointer
  `SCA-APP-012_GROUP-2_AUTHORIZED.md`. This candidate was built from the
  revision-2 package at `a4295f9ed`, before that snapshot was written; the
  snapshot binds the same group-2 files.
- Code specification: `Propagation_Plan.md` §4, revision 2 at `a4295f9ed`
  (SHA-256 `d5a14d2bfbecf2cc2cc9d96223b780e21893d0751065b2f9979f378d789fea18`),
  with `Impact_Assessment.md` §3 and §15 (revision 4, SHA-256
  `894d04e598b20269e24bf6169ca97cfa2e3af8ffbcc9febeb203938920bd3225`). The
  exact scope text is `Amendment_Preview.md` (SHA-256
  `bb6c0b44ec91e00cd8afced23081a3e9eea27cd9be374946736583feaa281ce9`); the test
  paths its verification hooks name exist in this candidate.

The SCA-APP-012 supersession bindings (D-APP-74 lines 97-99 and 107 for the
loop-first UI and the two retired routes, the SCA-APP-011 DEL-07-02 follow-up
and D-APP-56 R4-P29) take effect only on group-3 acceptance.

## Result

Built from `origin/main` `974bf7da4`. Paths are under
`projects/chirality-app-dev/frontend/src/`.

- **Deleted (the 20 paths of §4).** The loop-first shell
  (`components/shell/loop-shell.tsx`, `portal-loop-shell.tsx`,
  `loop-tertiary-shell.tsx`, `sidebar-right-loop-layout.tsx`,
  `tertiary-sidebar-tabs.tsx`); the role-directory panel
  `components/portal/agent-matrix.tsx` and
  `__tests__/components/agent-matrix-panel.test.ts`; the portal helpers
  `lib/portal/agent-matrix-cells.ts` and `agent-matrix-launch.ts` with
  `__tests__/lib/agent-matrix-launch.test.ts` and
  `__tests__/lib/agent-matrix-cells.test.ts` (after porting its case 1);
  `components/workspace/deliverables-provider.tsx`;
  `app/api/working-root/scope/route.ts`; the unmounted
  `components/woven-dialogue/workflows-view.tsx` and `workflow-detail.tsx` with
  `__tests__/components/woven-workflows.test.tsx`; and
  `GET /api/working-root/workflow` (`route.ts`, `workflow-store.ts`,
  `workflow-read-contract.ts`) with `__tests__/api/working-root-workflow.test.ts`.
- **Legacy prop and link.** `WovenDialogueRoute` loses its discarded `legacy`
  prop; `app/page.tsx`, `app/chat/page.tsx`, `app/workbench/workbench-client.tsx`
  and `app/pipeline/pipeline-client.tsx` stop passing it and drop the shell
  imports. `legacyHref` and the `?legacy=1` link it built are removed from
  `woven-dialogue-shell.tsx`, the `Navigator` props and the `ShellFrame` props.
- **Provider mount and copy.** `app/layout.tsx` no longer imports or mounts
  `DeliverablesProvider`; its metadata description reads "Dialogue shell for
  local agent execution". The four page Suspense fallbacks read "Loading...".
- **Symbol residue.** `lib/shell/loop-first.ts` keeps only `CHAT_SECTION`
  (`buildPortalPersonaHref`, `buildDirectChatHref`, `PORTAL_ROUTE` and
  `CHAT_ROUTE` removed). `PersonaPicker` loses its `buildHref` prop.
  `WorkspaceSidebar` loses its `portalTab`/`workbenchTab`/`pipelineTab` props,
  the `PORTAL_TAB`/`WORKBENCH_TAB`/`PIPELINE_TAB` constants, their panel branches
  and the `'portal' | 'workbench' | 'pipeline'` members of `SidebarTabId`.
- **CSS.** `app/globals.css` loses the 11 legacy-only class tokens and the 11
  dead selector families of §4, including their responsive rules; `shell-pane*`,
  `persona-picker*` and `workbench-card` stay.
  `components/woven-dialogue/workflows.module.css` keeps only `header` and
  `tabs` (`right-panel.tsx`).

**Kept** (§4): the `/workbench` and `/pipeline` pages (P-keep);
`lib/woven-dialogue/woven-workspace-state.ts` with its `'workbench' | 'pipeline'`
surfaces and tolerant parsing; `chat-panel.tsx` unchanged, including
`<PersonaPicker compact disabled={isRunning} />`, `resolveMode` and the
WORKBENCH/PIPELINE session modes; `lib/shell/persona-resolution.ts`;
`lib/woven-dialogue/guarded-session-selection.ts`;
`lib/woven-dialogue/operator-projection.ts` (its own local
`DIRECT_ENTRY_ROLE_IDS`); `lib/workspace/task-scope.ts`,
`lib/pipeline/pipeline-dispatch-contract.ts`, `scanProjectScopes` and
`/api/project/deliverables`; `app/api/working-root/workflow-drafts/**`,
`method-library-view.tsx` and `right-panel.tsx`; the scaffold library.
`electron/renderer-window-policy.ts` is not edited and still hashes to
`e2d63d32423d1ef6b0a03259235676ac9cefadde00e4f067be4f13e5ed2cc3ed` (33544
bytes); its L13-14 comment on the "open legacy interface" link is the recorded
residual of `Propagation_Plan.md` §11. `electron/main.ts`,
`scripts/run-packaged-security-proof.mjs` and
`__tests__/contract-pins.manifest.ts` are unchanged.

## Tests

- **Ported.** `__tests__/lib/persona-resolution.test.ts` gains case 1 of the
  retired `agent-matrix-cells.test.ts`, "derives exactly the three direct-entry
  choices from the shared role registry": from `CHIRALITY_ROLES`
  (`@chirality/runtime-contracts/v3`) the direct-entry roles are HELP_HUMAN,
  HELPS_HUMANS and WORKING_ITEMS, HELP_HUMAN is the new-chat default and TASK is
  not direct-entry. Case 2 (`isRoleSelectionBlocked`, an identity helper with no
  product caller) is dropped.
- **Added (DEL-08-02-REQ-004).** In the same file, RECONCILING and the App
  TYPES §4 matrix labels (rows NORMATIVE, OPERATIVE, EVALUATIVE; columns
  GUIDING, APPLYING, JUDGING, REVIEWING), in upper and lower case, each resolve
  to HELP_HUMAN, and none is a `PERSONA_ALIASES` key.
- **Added (role-picker guard).**
  `__tests__/components/chat-panel-role-picker-guard.test.tsx` mounts the woven
  `ChatPanel` with the picker stubbed and reads the props `ChatPanel` passes:
  the compact picker is enabled with no turn running, disabled while a turn
  runs, and enabled again when it ends. Mutation check: with `disabled={isRunning}`
  removed from `chat-panel.tsx`, the running-turn case fails ("expected 'false'
  to be 'true'"); the file was restored and is unchanged in the diff.
- **Replaced.** `__tests__/components/workspace-sidebar.test.ts` had two cases,
  both on the retired props or `SidebarRightLoopLayout`. Its one case ("WorkspaceSidebar
  default tabs") renders `WorkspaceSidebar` with `activeTab: 'workflow'` and
  checks exactly eight `role="tab"` buttons (Files, Sessions, Transcript, Tools,
  Subagents, Document, Workflow, Tool Kit), Workflow alone selected, and no
  Portal, Workbench or Pipeline tab.
- **Trimmed.** `__tests__/lib/loop-first.test.ts` keeps one case, on
  `CHAT_SECTION`. `__tests__/lib/pkg08-compatibility-boundaries.test.ts` keeps
  the role-boundary case (the direct-entry roles now read from
  `CHIRALITY_ROLES`) and the dispatch case; the matrix-helper round trip is
  dropped. `__tests__/components/woven-dialogue-route.test.tsx` keeps its default
  and `/workbench`/`/pipeline` surface cases without a `legacy` prop and drops
  the legacy-prop case. `__tests__/components/woven-dialogue-shell.test.tsx`
  drops the "preserves the legacy compatibility link" case and the `legacyHref`
  of its `ShellFrame` mock. `woven-dialogue-navigator.test.tsx` and
  `historical-chat-reveal.test.tsx` drop the `legacyHref` prop.
- **Relabelled.** `__tests__/components/loop-tertiary-routes.test.ts` keeps its
  file name and both cases; its `describe` label is now "Workbench and Pipeline
  route clients".

Every test path the scope text cites keeps its path.

## Records

- MEMORY rows in DEL-02-01, DEL-02-02, DEL-02-03 and DEL-08-02.
- `loop/LOOP_RECEIPTS.md` entry for this candidate (numbered at integration).
- Tranche manifest
  `docs/governance_harness/tranche_manifests/APP-RETIRE-LOOP-FIRST-UI-20260927.yaml`.
- `exports/chirality-app/` regenerated with the export tooling.
- **Not written here.** The decomposition, the App PRD, SPEC and PLAN and the
  eight Scopes of Work that SCA-APP-012 amends are its scope-text side
  (`Propagation_Plan.md` §2, T-a). No `_CONTEXT.md`, `_STATUS.md`,
  `Dependencies.csv`, `_DEPENDENCIES.md`, `_LATEST.md`, companion register or
  Task Management row is changed.

## Checks (worktree candidate)

Run on this candidate, with results in the hand-off to the coordinating
session: a repository search for every removed module, symbol, route and CSS
class (no code reference remains; the remaining hits are historical records and
this candidate's own provenance comment); frontend and Electron typecheck; the
changed and new Vitest files, then the full suite (the known uid-0
`harness-attachment-resolver` failure is the only failure); the role-picker
guard mutation check; the production build (`next build` and the Electron
build; the two retired API routes are absent from the route table and
`/workbench` and `/pipeline` remain); the renderer-window-policy hash; this
ledger's validator; Root G0–G3 and G4; conflict-marker and run-record-leak
checks; the workflow index check; `git diff --check`;
`run_affected_tests.py`; and export regeneration.

## Limits

- Group 3 of SCA-APP-012 is not accepted. The candidate lands only with the
  scope text, in one PR, after the owner's group-3 acceptance, independent
  review and actual-candidate CI.
- The premerge harness gate (`harness:validate:premerge`) needs a running
  harness server and Codex and could not run in this environment (every case
  reported "fetch failed"). No packaged run. The removed modules were not
  mounted in the live App, and no live UI called the two removed routes.
- `?legacy=1` is now an ordinary unknown query parameter.
- No lifecycle transition, approval-SHA refresh, dependency-register change,
  Task Management edit, authority-corpus repin, release or issuance.

Execution: a Claude Code subagent (TASK-type executor, no delegation) in an
isolated worktree for the coordinating session. Model identifiers are withheld;
the commit's session trailer identifies the run.
