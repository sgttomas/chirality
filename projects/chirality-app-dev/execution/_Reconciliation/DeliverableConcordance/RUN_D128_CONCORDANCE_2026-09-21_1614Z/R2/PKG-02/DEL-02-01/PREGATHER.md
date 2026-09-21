# PREGATHER — DEL-02-01 (Woven Dialogue Shell and Compatibility Navigation)

- Run: RUN_D128_CONCORDANCE_2026-09-21_1614Z, R2 PKG-02. Worker: TASK pre-gather (Type 2), read-only.
- Basis: frozen tree at `00115c719` (HEAD `00115c719`, 2026-09-21). No dispositions, verdicts or CauseTags below: evidence locations and reach facts only.
- Path abbreviations (all repo-relative): `FE/` = `projects/chirality-app-dev/frontend/`; `DEL/` = `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-01_Desktop_Shell_and_Matrix_Navigation/`; `DEC/` = `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/`; `REG` = `DEC/_REGISTER.md`.
- Units: 42 indexed (SEC-1..5, CLM-001..030, REM-1..7) from `R1_INVENTORY/CLAIM_INDEX.csv`; all 42 covered below in index order. (A 43rd CLAIM_INDEX row, `DEL-09-04#REM-2`, only names DEL-02-01-V3-04 in its gate and belongs to DEL-09-04.)
- Method:
  1. Read `DEL/ScopeOfWork.md` (full), `DEL/_STATUS.md` L1-70, `DEL/_CONTEXT.md` (grep), `DEL/_REFERENCES.md` (grep).
  2. Summarized `R1_INVENTORY/HINTS/DEL-02-01.csv` (537 data rows) per ClaimKey and path with python. Most hints hit tokens like `/pipeline`, `NORMATIVE` or `_CONTEXT.md` in scripts, Electron key storage or unrelated API tests; they were used only as leads.
  3. Read the product entries `FE/src/app/{page,chat/page,pipeline/page,pipeline/pipeline-client,workbench/page,workbench/workbench-client,not-found,layout}.tsx`. Followed the JSX render chain through `woven-dialogue-route.tsx` > `woven-dialogue-shell.tsx`. Grepped `<Component` render sites across `FE/src/{components,app,lib}`, excluding `__tests__`, for every legacy shell component.
  4. Looked up the reach of each module in `EVIDENCE_PACK/REACHABILITY.csv`. Checked `TOUCHED_PATHS.csv`: **no `FE/**` path is on the touched list**, so no TOUCHED marks apply below. Looked up `DECISION_HITS.csv` (DEL-02-01 rows), `REFERENCE_HASHES.csv` and `D-APP-127_APPLICATION_MAP.csv`, and matched decision IDs to `REG` rows.
  5. Listed test cases (grep of `it(`/`describe(`) in 20 candidate test files. Read-only git: `git -C <frozen> log -- FE/src/app/icon.svg` and `git show --stat b2b32669c`.
- Counts: 42/42 units covered. NO_CANDIDATES (code) for 17 documentary units: SEC-5, CLM-001, 002, 004, 006, 007, 008, 011, 013, 016, 018, 022, 023, 024, 027, 028, 030. REM units get gate-check locations. Test files cited: 29 distinct.

## Key reach facts (read before the units)

- **R1. Every page route renders only `WovenDialogueShell`.** `FE/src/app/page.tsx:8`, `chat/page.tsx:8`, `workbench/workbench-client.tsx:9` and `pipeline/pipeline-client.tsx:9` all render `<WovenDialogueRoute defaultSurface=… legacy={<PortalLoopShell/>|<LoopShell/>|<LoopTertiaryShell…/>}>`. `FE/src/components/woven-dialogue/woven-dialogue-route.tsx:18` does `void legacy;` and `:19` returns `<WovenDialogueShell defaultSurface={defaultSurface} />`. `WovenDialogueShell(_props)` (`woven-dialogue-shell.tsx:77`) does not read `defaultSurface`, and the workspace section carries a fixed `data-woven-surface="dialogue"` (`:822`).
- **R2. Legacy loop-first/matrix components are LIVE by import only.** Import-LIVE but not rendered from any product entry: `PortalLoopShell`, `LoopShell`, `LoopTertiaryShell`, `SidebarRightLoopLayout`, `createTertiarySidebarTabs` and the components it builds (`AgentMatrix`, `PipelineSurface`, `WorkbenchSurface`), and the `PersonaPicker` call sites inside the legacy shells. Searched `<PortalLoopShell|<LoopShell|<LoopTertiaryShell|<SidebarRightLoopLayout|<AgentMatrix|<PipelineSurface|<WorkbenchSurface`; the only render sites are inside those legacy shells or as the voided `legacy` prop. The only live render of `PersonaPicker` is the woven composer context line (`chat-panel.tsx:2124`).
- **R3. `ShellFrame` has two branches.** The woven shell renders it at `woven-dialogue-shell.tsx:812` with `variant="workspace"` and `renderWorkspaceContent`, which takes the headerless branch at `shell-frame.tsx:307-310` (`shell--stone`, `AccountPresentation` > `AccountRow`). The `<header>`/`<nav aria-label="Primary navigation">` branch with the PORTAL link and `shell-nav-link--active` (`shell-frame.tsx:314-364`, `NAVIGATION_ITEMS` at `:42-44`) is rendered live only via `AppShell` (`app-shell.tsx:316`) from `FE/src/app/not-found.tsx:6`. Otherwise it is reached only through the unrendered legacy shells.
- **R4. The "matrix" is now a role directory.** `FE/src/components/portal/agent-matrix.tsx:38` `AgentMatrix` renders `RoleDirectoryPanel` (`:9`), a list of direct-entry roles from `listRoles`. It has no 3x4 grid and no row or column vocabulary. `NORMATIVE|OPERATIVE|EVALUATIVE` occurs in non-test source only at `FE/src/components/workbench/workbench-surface.tsx:177` (`row` query default). `FE/src/lib/portal/agent-matrix-cells.ts` and `agent-matrix-launch.ts` are `REACH=TEST_ONLY`.
- **R5. The in-app icon was removed.** `git show --stat b2b32669c` (2026-09-10, "Use website artwork for macOS icon and remove in-app logo") deletes `FE/src/app/icon.svg` and `FE/public/chirality-app-icon.svg` and edits `FE/build/icon-macos.svg`, `FE/build/icon.icns`, `globals.css` and `shell-frame.tsx`. At `00115c719` neither `FE/src/app/icon.*` nor `FE/public/` exists. `FE/src/app/layout.tsx:57-60` `metadata` has only `title` and `description`.
- **R6. The composer context line (live).** `FE/src/components/shell/chat-panel.tsx:2121-2160`, woven presentation only, renders: "Working in"/"Start in", `FolderSelect` (`knownRoots`, `locked={Boolean(conversationBinding)}`), `PersonaPicker compact`, Interaction mode (Chat/Plan Mode), Permissions, Model and Reasoning. A grep for `rung|delegat` (case-insensitive) in `chat-panel.tsx` returns no hits.

---

## SEC-1 — SCA-APP-004 current responsibility (SoW L28)
- Gist: the shell composes a persistent transcript and composer, provenance-bearing artifact views, the Navigator, the Coordination Panel, the Activity Shelf, and compatibility navigation, with replay kept read-only.
- Candidate code:
  - `FE/src/components/woven-dialogue/woven-dialogue-shell.tsx:77 WovenDialogueShell`: REACH=LIVE; SYMBOL-REACH: rendered from all four page routes (R1).
  - `FE/src/components/shell/chat-panel.tsx:318 ChatPanel` (rendered at `woven-dialogue-shell.tsx:855`, `presentation="woven"`): REACH=LIVE; SYMBOL-REACH: rendered.
  - `FE/src/components/woven-dialogue/navigator.tsx:117 Navigator` (rendered `woven-dialogue-shell.tsx:894`): REACH=LIVE; SYMBOL-REACH: rendered.
  - `FE/src/components/woven-dialogue/coordination-panel.tsx` `CoordinationPanel` (rendered `woven-dialogue-shell.tsx:1019`) > `agents-projection.tsx:109 AgentsProjection` (rendered `coordination-panel.tsx:80`): REACH=LIVE; SYMBOL-REACH: rendered.
  - `FE/src/components/woven-dialogue/activity-shelf.tsx:109 ActivityStrip` (rendered `woven-dialogue-shell.tsx:1062`) and `:221 ActivityView` (rendered `right-panel.tsx:191`): REACH=LIVE; SYMBOL-REACH: rendered. `activity-shelf.tsx:28 ActivityShelf`: SYMBOL-REACH: no non-test `<ActivityShelf` render site found.
  - `FE/src/components/woven-dialogue/selected-session-replay-lens.tsx:328 SelectedSessionReplayLens` (rendered `woven-dialogue-shell.tsx:1024`): REACH=LIVE; SYMBOL-REACH: rendered.
  - `FE/src/lib/woven-dialogue/guarded-session-selection.ts:59 guardRecordedSessionSelection`, `:159 returnToPrimaryDialogue`: REACH=LIVE; SYMBOL-REACH: imported by the woven shell (`:22`); call sites not traced.
  - `FE/src/components/shell/document-view.tsx:446 DocumentView` (focused artifact/document view; imported by `right-panel.tsx:10`): REACH=LIVE; SYMBOL-REACH: not checked for the render branch.
  - `FE/src/components/woven-dialogue/work-projection.tsx`: REACH=TEST_ONLY (Work projection).
  - `FE/src/lib/woven-dialogue/contracts.ts`: REACH=UNREACHED (type-only imports).
- Candidate tests: `FE/src/__tests__/components/woven-dialogue-shell.test.tsx :: "preserves controller identity and focusable composer through replay, panel controls, resize, and return"`, `"continues a compatible v3 replay in the mounted primary dialogue and leaves legacy replay read-only"`. `selected-session-replay-lens.test.tsx :: "labels replay as read-only and renders exact provenance and attribution"`, `"exposes no historical mutation controls"`. `guarded-session-selection.test.ts :: "blocks replay selection while a live turn is active"`, `"allows the persistent return to primary even while a live turn is active"`. `activity-strip.test.tsx`, `native-coordination.test.tsx`, `woven-dialogue-work-projection.test.tsx`.
- Candidate decisions: D-APP-74 (REG L89; `DEC/D-APP-74_RULING_2026-07-23.md:81`, SCA-APP-004 Woven Dialogue); D-APP-108 (REG L123).

## SEC-2 — SCA-APP-004 current acceptance obligations 1-7 (SoW L52)
- Gist: preserve the four routes, deep links and query params; keep the loop-first/matrix UI reachable; keep the dialogue mounted; show artifact provenance; evidence-conditional projections; mid-turn guards; render/a11y evidence.
- Candidate code:
  - Routes: the four pages (R1). REACH=LIVE; SYMBOL-REACH: each renders `WovenDialogueShell`, and the legacy element is voided (R1).
  - Query preservation: `woven-dialogue-shell.tsx:384-388 legacyHref` copies all `searchParams` and sets `legacy=1`. It is passed to `Navigator`, where `navigator.tsx:119` does `void legacyHref;`. `woven-dialogue-shell.tsx:424-429` reads and sets `agent`. REACH=LIVE.
  - Obligation 2 (loop-first and matrix UI reachable): legacy shells and `AgentMatrix` are REACH=LIVE; SYMBOL-REACH: not rendered (R2, R4).
  - Obligation 3 (mounted dialogue): `woven-dialogue-shell.tsx:848` `<main className="woven-dialogue-region" aria-label="Primary Dialogue">`. REACH=LIVE.
  - Obligation 5: `agents-projection.tsx:109` REACH=LIVE; `work-projection.tsx` REACH=TEST_ONLY.
  - Obligation 6: `guarded-session-selection.ts:59` REACH=LIVE.
  - Obligation 7 (reduced motion): `FE/src/app/globals.css:3188, 3665` `@media (prefers-reduced-motion: reduce)`.
  - Electron probes: `FE/electron/main.ts:647 RENDERER_SECURITY_PROBE_ROUTES = ['/', '/chat', '/pipeline', '/workbench']`, REACH=LIVE.
- Candidate tests:
  - `woven-dialogue-route.test.tsx :: "renders Woven Dialogue by default"`, `"opens /%s in the continuing conversation surface"` (it.each workbench/pipeline), `"does not expose the retired execution surface through a legacy route prop"`. Mocks `WovenDialogueShell` (L6).
  - `loop-tertiary-routes.test.ts :: "opens the Workbench deep link in the continuing conversation"`, `"opens the Pipeline deep link…"`. Mocks `WovenDialogueShell` (L5-11).
  - `woven-dialogue-shell.test.tsx :: "only mounts Dialogue even with historical %s surface input"`, `"preserves the legacy compatibility link with the current query string"`, `"keeps collapse, detail return and expansion as distinct real controls without remounting primary"`, `"provides explicit desktop reopen glyphs and full accessible names across responsive states"`.
  - `woven-dialogue-controls.test.tsx :: "uses ordinary pressed buttons rather than incomplete ARIA tab widgets"`.
- Candidate decisions: D-APP-74; D-APP-36 (REG L51, render-test bar).

## SEC-3 — SCA-APP-010 current responsibility (SoW L84)
- Gist: compose the transcript and composer with a context line (folder, agent, permissions, delegation, rung), a header-less three-panel frame, a chat navigator, per-chat folder selection, an account row host, and compatibility navigation.
- Candidate code:
  - Header-less frame: `shell-frame.tsx:307-310` workspace branch (R3). REACH=LIVE; SYMBOL-REACH: rendered from the woven shell `:812`.
  - Context line: `chat-panel.tsx:2121-2160` (R6). REACH=LIVE; SYMBOL-REACH: rendered (woven branch). No delegation or rung field (R6 grep).
  - `FE/src/components/shell/folder-select.tsx:15 FolderSelect`: REACH=LIVE; SYMBOL-REACH: rendered `chat-panel.tsx:2123`.
  - `FE/src/components/shell/persona-picker.tsx:25 PersonaPicker`: REACH=LIVE; SYMBOL-REACH: rendered `chat-panel.tsx:2124` (compact).
  - Navigator: `navigator.tsx:117`, REACH=LIVE, rendered.
  - Account row: `FE/src/components/shell/account-row.tsx:13 AccountRow` via `shell-frame.tsx:372 AccountPresentation` (`:403`). REACH=LIVE; SYMBOL-REACH: rendered in the workspace branch.
- Candidate tests: `woven-dialogue-shell.test.tsx :: "exposes collapsed search, guarded new-chat, expand, and account controls"`, `"opens Settings from the sole footer or collapsed account control without remounting the chat"`. `shell-frame.test.tsx :: "anchors the woven account popover outside its trigger…"`. `folder-select.test.tsx` (3 cases). `account-presentation.test.tsx`. `chat-panel-model-selectors.test.tsx`.
- Candidate decisions: D-APP-108 (REG L123; `DEC/D-APP-108_RULING_SCA_APP_010_SEATING_AND_SHELL_QUESTIONS_2026-09-04.md:56`); D-APP-120 (REG L139; `DEC/D-APP-120_RULING_PRESENTATION_SEAM_AND_NO_FOLDER_ROUTING_2026-09-06.md:15`); D-APP-122 (REG L143, account-row host); D-APP-127 (REG L152; ruling L118-122 keeps the DEL-02-01 account-row host selection "Not superseded"). `D-APP-127_APPLICATION_MAP.csv`: all five DEL-02-01 carriers are `NO`.

## SEC-4 — SCA-APP-010 acceptance obligations 1-6 (SoW L102)
- Gist: dialogue never hidden, no header row; context line from recorded state, with no-folder stated; folder fixed after the first message, validated by DEL-07-01 with native affordances; local-only chat organisation; compatibility routes unlisted; no pop-out; account row hosted here.
- Candidate code:
  1. Headerless: `shell-frame.tsx:307-310` (R3), REACH=LIVE, rendered.
  2. Context line: `chat-panel.tsx:2121-2160` (R6). No-folder label: `navigator.tsx:104` (`title=… || 'No folder'`). A grep for a no-folder string in `folder-select.tsx` and `chat-panel.tsx` found none.
  3. Folder lock: `chat-panel.tsx:2123` (`locked={Boolean(conversationBinding)}`). Validation: `FE/src/components/workspace/workspace-provider.tsx:36 validateProjectRoot` > `FE/src/app/api/working-root/validate/route.ts:9 POST` > `FE/src/lib/harness/session-manager.ts assertProjectRootAccessible`; all REACH=LIVE. Native picker: `folder-select.tsx:42` (`chooseProjectRoot`). Recent documents: `FE/electron/main.ts:103 registerRecentFolder` (`app.addRecentDocument`, `validateRevealRoot`), called from `chat-panel.tsx:764 registerRecent`. Reveal: `FE/electron/main.ts:987 shell.showItemInFolder`; `FE/electron/preload.ts:78` handoff `reveal`/`reveal-root`. Folder drop: `chat-panel.tsx:2035-2041 onDrop` > `preload.ts:49 webUtils.getPathForFile`; `main.ts:1129 app.on('open-file')` folder intent. All REACH=LIVE.
  4. Local organisation: `FE/src/lib/woven-dialogue/chat-organization.ts:136 visibleActiveChatSessions`, `:150 projectChatSections` (deleted/archived sets), `:60 deriveChatTitle` / `:65 redactConfiguredApiKeys`. `FE/src/lib/woven-dialogue/woven-workspace-state.ts`, storage key `chirality.wovenWorkspace.v1` (`:3`). REACH=LIVE.
  5. Routes unlisted: `navigator.tsx:119 void legacyHref`; the pages exist (R1).
  6. Pop-out: a grep for pop-out/new-window code was not run (NOT checked). Account row: see SEC-3.
- Candidate tests: `woven-dialogue-navigator.test.tsx :: "creates/moves groups, supports drag and collapse, and locally deletes while the original record remains recoverable"`, `"renders folder sections, derived title/time, folder basename/no-folder, …"`. `chat-organization.test.ts :: "redacts configured keys before trimming at a word boundary…"`, `"keeps archived and locally deleted sessions distinct and hides both from active chats"`. `woven-dialogue-shell.test.tsx :: "persists a redacted live title…"` and the `WovenDialogueShell per-chat folders` suite (5 cases L592-679). `chat-panel-folder-binding.test.tsx :: "blocks native folder intent while bound or pending and blocks Send during pending selection"`, `"rejects empty and multiple-file drops without invoking folder validation"`. `historical-chat-reveal.test.tsx` (11 cases). `FE/src/__tests__/electron/folder-conveniences.test.ts`. `FE/src/__tests__/lib/redaction-path-matrix.test.ts`.
- Candidate decisions: D-APP-108 (Q1, Q3, Q5, Q6, Q9); D-APP-120; D-APP-122; D-APP-127.

## SEC-5 — Seating and rulings (SoW L111)
- Gist: records that four V3 Remaining items were seated under D-APP-108, the ruled questions applied, the alignment writes, and that no lifecycle or release act is implied.
- Candidate code: NO_CANDIDATES (documentary). Searched: n/a (record of seating).
- Check against: `DEL/_STATUS.md` L27-58 (the four V3 items present) and L65 (2026-09-04 seating history); `DEL/Dependencies.csv` (15 lines; D-APP-108 hits L13-15; D-APP-109/110 L11).
- Candidate decisions: D-APP-108 (ruling L56); D-APP-109 (REG L124); D-APP-110 (REG L125; `DEC/D-APP-110_RULING_SCA_APP_010_SCC_DECOMPOSE_2026-09-05.md:50`).

## CLM-001 — Datasheet P40 note (SoW L123)
- Gist: REF-006 `docs/PRD.md` is MATCH under D-APP-38; older hash-mismatch wording is dated history.
- Candidate code: NO_CANDIDATES (documentary). Hint hits (`verify-version-identity.mjs`, `harness-section9-manifest.json`) are unrelated PRD mentions.
- Hash fact: `EVIDENCE_PACK/REFERENCE_HASHES.csv` DEL-02-01 PRD has RecordedVerdict `MATCH`, recorded `8649ccba…fa4`, recomputed `17ca3f3c…6054`, Match `NO`. CONTRACT and SPEC rows are also `NO`. Recorded line: `DEL/_REFERENCES.md:12`.
- Candidate decisions: D-APP-38 (REG L53); D-APP-56 (REG L71).

## CLM-002 — Identification table (SoW L130)
- Gist: identification fields: SOFTWARE_DECOMP v3.2, PKG-02, DEL-02-01, name "Woven Dialogue Shell and Compatibility Navigation", ResponsibleParty TBD, UX_UI_SLICE, M, OPEN at P1/P2.
- Candidate code: NO_CANDIDATES (documentary; hint hits are generic field-name tokens in unrelated tests).
- Check against: `DEL/_CONTEXT.md:10-14` (PackageName matches; `ResponsibleParty | TBD` at L14); `DEL/_STATUS.md:3` (IN_PROGRESS).
- Candidate decisions: none specific; D-APP-19 (REG L34) for lifecycle basis.

## CLM-003 — Attributes (SoW L148)
- Gist: primary surface is the loop-first shell with PORTAL in the header and Workbench/Pipeline as right-sidebar tertiary tabs; 3x4 matrix with canonical rows and columns; row destinations; shell routes; active-route indication.
- Candidate code:
  - `shell-frame.tsx:42 NAVIGATION_ITEMS [{ href: '/', label: 'PORTAL' }]` and `:344-360` nav: REACH=LIVE; SYMBOL-REACH: the header branch is rendered only via `AppShell` from `not-found.tsx` (R3).
  - `FE/src/components/shell/tertiary-sidebar-tabs.tsx:7 createTertiarySidebarTabs` (portal/pipeline/workbench tabs), `FE/src/components/shell/workspace-sidebar.tsx:99 WorkspaceSidebar` (`portalTab`/`workbenchTab`/`pipelineTab` props L84-110): REACH=LIVE; SYMBOL-REACH: the tertiary tabs are not rendered. `WorkspaceSidebar` is rendered by `AppShell` (`app-shell.tsx:383`) with no tab props (R2).
  - `FE/src/components/portal/agent-matrix.tsx:38 AgentMatrix`: REACH=LIVE; SYMBOL-REACH: not rendered; the component is a role directory, not a 3x4 matrix (R4).
  - `FE/src/lib/portal/agent-matrix-launch.ts:10 mergeMatrixTargetIntoCurrentUrl`: REACH=TEST_ONLY.
- Candidate tests: `agent-matrix-panel.test.ts :: "renders the three direct-entry roles without ladder or workflow-rung controls"` (describe "legacy Portal role directory"). `workspace-sidebar.test.ts :: "renders Portal, Workbench, and Pipeline as sidebar tabs when provided"`. `shell-frame.test.tsx :: "renders the PORTAL header link with the active class"` (mocks `usePathname` to `/`).
- Candidate decisions: D-APP-28 (REG L43), D-APP-30 (L45), D-APP-31 (L46), D-APP-32 (L47), D-APP-36 (L51); later D-APP-74 (L89) and D-APP-108 (L123) change the target.

## CLM-004 — Conditions (SoW L166)
- Gist: covers SOW-001/005 and OBJ-001; includes UI and operator workflow; excludes runtime engine internals; PRD MATCH; dependency extraction deferred with no Dependencies.csv.
- Candidate code: NO_CANDIDATES (documentary).
- Check against: `DEL/Dependencies.csv` exists (15 lines, rows citing D-APP-108/109/110); `DEL/_STATUS.md:64` (D-APP-109 re-extraction); `REFERENCE_HASHES.csv` (see CLM-001).
- Candidate decisions: D-APP-56 (UPD-105); D-APP-109 (REG L124).

## CLM-005 — Construction (SoW L180)
- Gist: header exposes PORTAL and preserves the `/pipeline` and `/workbench` deep links; the matrix renders canonical rows and columns; cells route by row; the listed route-state keys; ADQ-13 tests.
- Candidate code:
  - `shell-frame.tsx:42, 344-360` (R3). REACH=LIVE; SYMBOL-REACH: header only via not-found.
  - `agent-matrix.tsx:38` (R4). REACH=LIVE; not rendered.
  - Route-state keys:
    - `agent`: `woven-dialogue-shell.tsx:424-429`, `chat-panel.tsx:403, 468`, `persona-picker.tsx:70, 85`; REACH=LIVE, rendered.
    - `row` default `NORMATIVE`: `FE/src/components/workbench/workbench-surface.tsx:177`; REACH=LIVE; SYMBOL-REACH: `WorkbenchSurface` not rendered (R2).
    - `taskScopeMode` and `pkg::deliverable`: `FE/src/lib/workspace/task-scope.ts:14 buildDeliverableCompositeKey`, `:18 normalizeTaskScopeMode`; REACH=LIVE via `deliverables-provider.tsx` (layout); SYMBOL-REACH: not checked.
- Candidate tests: `agent-matrix-launch.test.ts :: "keeps persona launches on the current loop shell route"`, `"opens Pipeline intent in place and clears stale Pipeline scope query"` (TEST_ONLY lib). `task-scope-selection.test.ts`. `loop-first.test.ts :: "pre-selects a persona via ?agent= and url-encodes it"`. ADQ-13 note: `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/Evidence_ADQ-13_UI_Specs_Render_Tests.md` (exists).
- Candidate decisions: D-APP-28/30/31/32/36.

## CLM-006 — References table (SoW L193)
- Gist: lists REF-004 TYPES §4, REF-006 PRD §§7.2/8.1/8.2, the decomposition v3.2, and local files as sources.
- Candidate code: NO_CANDIDATES (documentary).
- Check against: `DEL/_REFERENCES.md` (REF-006 row L12); `REFERENCE_HASHES.csv` (no TYPES row; PRD, CONTRACT and SPEC Match `NO`).
- Candidate decisions: D-APP-38.

## CLM-007 — D-APP-56 R5 P45 reconciliation, Ontology (SoW L205)
- Gist: UPD-105 says the extracted dependency register exists; UPD-106 says a governed PORTAL active-link render test implements it.
- Candidate code: NO_CANDIDATES for the register (documentary; `DEL/Dependencies.csv` exists).
- For UPD-106: `shell-frame.tsx:349-351` active-class logic, REACH=LIVE; SYMBOL-REACH: header branch only via not-found (R3).
- Candidate tests: `shell-frame.test.tsx :: "renders the PORTAL header link with the active class"`.
- Candidate decisions: D-APP-56 (REG L71; `DEC/D-APP-56_RULING_2026-07-12.md:78`).

## CLM-008 — Specification P40 note (SoW L213)
- Gist: same as CLM-001 (PRD MATCH under D-APP-38; the older mismatch is history).
- Candidate code: NO_CANDIDATES (documentary). See CLM-001 for hash facts.
- Candidate decisions: D-APP-38; D-APP-56.

## CLM-009 — Scope (SoW L220)
- Gist: in scope are loop-first access to PORTAL/WORKBENCH/PIPELINE, the header PORTAL link, right-sidebar tertiary tabs, PORTAL 3x4 matrix, row routing, and tests. Out of scope are engine internals and Dependencies.csv creation.
- Candidate code: the same set as CLM-003 and CLM-005.
  - Legacy chain: `loop-tertiary-shell.tsx:21 LoopTertiaryShell` > `sidebar-right-loop-layout.tsx:19 SidebarRightLoopLayout` > `tertiary-sidebar-tabs.tsx:7`. All REACH=LIVE; SYMBOL-REACH: not rendered (R1, R2).
  - Live path: `WovenDialogueShell`, rendered.
  - `FE/src/components/pipeline/pipeline-surface.tsx:230 PipelineSurface`, `workbench-surface.tsx:173 WorkbenchSurface`: REACH=LIVE; not rendered.
- Candidate tests: `workspace-sidebar.test.ts :: "keeps the primary loop content mounted while a tertiary tab owns the right sidebar"`; `loop-tertiary-routes.test.ts` (2 cases, mocked shell); `woven-dialogue-shell.test.tsx :: "only mounts Dialogue even with historical %s surface input"`.
- Candidate decisions: D-APP-28/31/32; superseding target D-APP-74, D-APP-108.

## CLM-010 — Requirements REQ-001..011 (SoW L243)
- Gist: eleven requirements: tertiary surfaces reachable, header PORTAL, active indication, 3x4 matrix, row and column labels, NORMATIVE/EVALUATIVE to the loop persona, OPERATIVE to Pipeline, disabled variants visible, and stable route keys.
- Candidate code, per requirement:
  - REQ-001/002: legacy tertiary chain (not rendered) versus `WovenDialogueShell` (rendered; `defaultSurface` unused, R1).
  - REQ-003: `shell-frame.tsx:349-351` (not-found only).
  - REQ-004/005/006: `agent-matrix.tsx:9 RoleDirectoryPanel` (no grid, R4).
  - REQ-007/008: persona selection live via `persona-picker.tsx:25` in the context line. `FE/src/lib/portal/agent-matrix-cells.ts:8 isRoleSelectionBlocked` is REACH=TEST_ONLY.
  - REQ-009: `agent-matrix-launch.ts:10` is REACH=TEST_ONLY; `pipeline-client.tsx` renders the woven shell.
  - REQ-010: `pipeline-surface.tsx` / `workbench-surface.tsx` (not rendered). Whether any live surface shows "coming soon" was not checked.
  - REQ-011: see the CLM-005 keys.
  - `FE/src/lib/shell/loop-first.ts:10-32` (`PORTAL_ROUTE`, `CHAT_ROUTE`, `buildPortalPersonaHref`): REACH=LIVE; SYMBOL-REACH: `buildPortalPersonaHref` is used at `portal-loop-shell.tsx:30` (not rendered).
- Candidate tests: every test file named in CLM-012 exists at the frozen basis. `agent-matrix-cells.test.ts` (describe "retired matrix compatibility"): `"derives exactly the three direct-entry choices from the shared role registry"`, `"blocks role selection at an active execution boundary"`. `pipeline-surface.test.ts` (216 lines).
- Candidate decisions: D-APP-28/30/31/32/36; D-APP-74; D-APP-108.

## CLM-011 — Standards (SoW L262)
- Gist: lists PRD (MATCH), TYPES §4, CONTRACT K-ID-1/K-PATH-1/K-INVENT-1/K-CONFLICT-1, DIRECTIVE §4.1 and the decomposition as accessible standards.
- Candidate code: NO_CANDIDATES (documentary). See CLM-001 for hash facts.
- Candidate decisions: D-APP-38.

## CLM-012 — Verification mapping (SoW L275)
- Gist: maps REQ groups to named test files.
- Candidate tests (all exist; line counts in brackets):
  - `FE/src/__tests__/components/workspace-sidebar.test.ts` [49]: 2 cases; renders `WorkspaceSidebar` with tabs provided.
  - `components/loop-tertiary-routes.test.ts` [29]: 2 cases; mocks `WovenDialogueShell`.
  - `lib/agent-matrix-cells.test.ts` [16].
  - `lib/agent-matrix-launch.test.ts` [26].
  - `components/agent-matrix-panel.test.ts` [24]: "legacy Portal role directory".
  - `components/pipeline-surface.test.ts` [216].
  - `lib/task-scope-selection.test.ts` [120].
  - "Matrix UI test output" (REQ-004..006) is not a file path; `agent-matrix-panel.test.ts` is the nearest candidate.
- Candidate code: see CLM-010.
- Candidate decisions: D-APP-36.

## CLM-013 — Documentation (SoW L288)
- Gist: anticipated artifacts are navigation components, matrix tests, route query handling, key-name evidence notes, the ADQ-13 note, and a possible path-rename ruling.
- Candidate code: NO_CANDIDATES (documentary).
- Check against: `…/1_Working/Evidence_ADQ-13_UI_Specs_Render_Tests.md` exists; CONFLICT-001 path (see CLM-030).
- Candidate decisions: D-APP-36.

## CLM-014 — D-APP-56 R5 P45 reconciliation, Epistemology (SoW L303)
- Gist: UPD-105 says the register exists; UPD-106 says a `ShellFrame` render test asserts `shell-nav-link--active` on the PORTAL link.
- Candidate code: `shell-frame.tsx:349-351` (`shell-nav-link--active`). REACH=LIVE; SYMBOL-REACH: header branch only via not-found (R3). `FE/src/app/globals.css` (one `shell-nav-link--active` hit).
- Candidate tests: `shell-frame.test.tsx :: "renders the PORTAL header link with the active class"` (L69-77; `usePathname` mocked to `/`, L19). `shell-frame-runtime-connectivity.test.tsx` and `app-shell-resize.test.tsx` also render ShellFrame/AppShell (hint hits).
- Candidate decisions: D-APP-56.

## CLM-015 — D-APP-56 shell ownership amendment + AC-001 (SoW L310)
- Gist: R4-P29 assigns `/chat` and the portal persona-picker bar to DEL-02-01; DEL-08-02 owns alias ownership and the `isMatrixLaunchBlockedByStreaming` guard. AC-001 concerns SoW validity.
- Candidate code:
  - `FE/src/app/chat/page.tsx:8`: REACH=LIVE; renders the woven shell.
  - `persona-picker.tsx:25 PersonaPicker`: REACH=LIVE; SYMBOL-REACH: rendered only compact in the context line. The "portal persona-picker bar" call site `portal-loop-shell.tsx:30` is not rendered (R2).
  - `isMatrixLaunchBlockedByStreaming`: a grep of `FE/src` for the name found no hit in non-test code. The nearest symbol is `FE/src/lib/portal/agent-matrix-cells.ts:8 isRoleSelectionBlocked` (REACH=TEST_ONLY).
  - `FE/electron/renderer-window-policy.ts`: REACH=LIVE (hint hit for `/chat`; content not checked).
- Candidate tests: `loop-first.test.ts :: "exposes the /chat route and CHAT section constants"`, `"builds the bare /chat href when no persona is given"`.
- Candidate decisions: D-APP-56 (R4-P29; ruling L78). AC-001 is documentary (SoW validation), with no code.

## CLM-016 — Procedure heading (SoW L320)
- Gist: heading only ("Procedure: DEL-02-01 Desktop Shell and Matrix Navigation"); no assertion beyond the title.
- Candidate code: NO_CANDIDATES (heading; no searchable assertion).

## CLM-017 — Procedure purpose (SoW L325)
- Gist: produce and verify the loop-first shell and matrix navigation, preserving PORTAL/WORKBENCH/PIPELINE access with the live loop primary.
- Candidate code: as CLM-009 (legacy chain not rendered; live woven shell rendered, R1/R2).
- Candidate tests: as CLM-012.
- Candidate decisions: D-APP-28; D-APP-74; D-APP-108.

## CLM-018 — Prerequisites (SoW L332)
- Gist: prerequisites are the sources, context, workspace, evidence slots, ResponsibleParty TBD, and deferred dependency extraction (do not create Dependencies.csv); upstream/downstream dependencies TBD.
- Candidate code: NO_CANDIDATES (documentary).
- Check against: `DEL/Dependencies.csv` exists (15 lines); `DEL/_DEPENDENCIES.md` (D-APP-109/110 hits L53-154); `DEL/_CONTEXT.md:14` (TBD).
- Candidate decisions: D-APP-109; D-APP-110; D-APP-56 (UPD-105).

## CLM-019 — Steps 1-14 (SoW L352)
- Gist: fourteen procedure steps: confirm identity and sources, preserve the three surfaces and deep links, header active state, render the matrix, route rows, keep disabled variants, add tests, keep engine internals out, record paths.
- Candidate code: as CLM-005, CLM-009 and CLM-010.
- Step 2 (the PRD mismatch treated as a warning) has no code candidate; see CLM-001.
- Candidate tests: as CLM-012.
- Candidate decisions: D-APP-28/30/31/32/36/38.

## CLM-020 — Verification checks (SoW L372)
- Gist: nine checks covering route reachability, active state, matrix shape and labels, loop-persona and Pipeline routing, unsupported variants, and scope discipline.
- Candidate code: as CLM-010 (per-REQ mapping).
- Candidate tests: as CLM-012, plus `woven-dialogue-route.test.tsx` (3 cases).
- Candidate decisions: D-APP-36.

## CLM-021 — Implementation Evidence Slots (SoW L389)
- Gist: names navigation component paths, matrix UI test paths and route-query test paths as evidence.
- Named navigation paths, all REACH=LIVE:
  - `FE/src/components/shell/shell-frame.tsx`: rendered, workspace branch.
  - `sidebar-right-loop-layout.tsx`: not rendered.
  - `loop-tertiary-shell.tsx`: not rendered.
  - `FE/src/app/workbench/workbench-client.tsx`: rendered; renders the woven shell.
  - `FE/src/app/pipeline/pipeline-client.tsx`: rendered; renders the woven shell.
- Named test paths exist: `agent-matrix-panel.test.ts`, `agent-matrix-cells.test.ts`, `loop-tertiary-routes.test.ts`, `agent-matrix-launch.test.ts`, `loop-first.test.ts`.
- Candidate decisions: D-APP-36.

## CLM-022 — Records (SoW L402)
- Gist: expected records are change notes, test results, query-key documentation, rulings on path/hash/source-pointer issues, and the kit plus TASK record.
- Candidate code: NO_CANDIDATES (documentary).
- Check against: `DEL/_run_records/` (24 files, e.g. `TASK_RUN_2026-05-20_*.md`, `TASK_RUN_2026-07-12_DAPP56_*.md`, `SHELL_CONVERGENCE_V5_2026-09-06.md`, `APP_V3_INTEGRATION_2026-09-06.md`).
- Candidate decisions: D-APP-38 (hash); D-APP-56.

## CLM-023 — D-APP-56 R5 P45 reconciliation, Praxeology + VER-001 (SoW L413)
- Gist: UPD-105 says the register exists; UPD-106 is "withheld for the final code tranche". This wording differs from CLM-007/014, which say UPD-106 is implemented. VER-001: validate the SoW candidate.
- Candidate code: NO_CANDIDATES (documentary). For UPD-106 see CLM-014.
- Check against: `DEL/_run_records/TASK_RUN_2026-07-12_DAPP56_FINAL_CODE.md`, `TASK_RUN_2026-07-12_DAPP56_R5_P45.md` (not read).
- Candidate decisions: D-APP-56.

## CLM-024 — Guidance P40 note (SoW L423)
- Gist: same as CLM-001 (PRD MATCH under D-APP-38).
- Candidate code: NO_CANDIDATES (documentary). See CLM-001 for hash facts.
- Candidate decisions: D-APP-38.

## CLM-025 — Guidance purpose (SoW L430)
- Gist: preserve the operator's movement through the loop-first shell: PORTAL for the matrix, WORKBENCH for contract review, PIPELINE for operative categories, with the live loop mounted.
- Candidate code: as CLM-009 (legacy surfaces not rendered; woven shell rendered).
- Candidate tests: as CLM-012.
- Candidate decisions: D-APP-28; D-APP-74; D-APP-108.

## CLM-026 — Principles (SoW L437)
- Gist: explicit PORTAL/PIPELINE/WORKBENCH surfaces; canonical matrix vocabulary; routing by row semantics; stable IDs and keys; visible unsupported variants; no engine behaviour in this slice.
- Candidate code:
  - Vocabulary: only at `workbench-surface.tsx:177` (not rendered). `agent-matrix.tsx` has no row or column labels (R4).
  - Keys: see CLM-005.
  - `FE/electron/main.ts`: 8 hint hits for `agent`/`row`/`column`, which are generic tokens (not checked as routing).
- Candidate tests: as CLM-012.
- Candidate decisions: D-APP-28/30/31.

## CLM-027 — Considerations (SoW L449)
- Gist: PRD is the main source (MATCH); PRD points to SPEC while concrete matrix semantics are in TYPES §4; DEL-08-02, DEL-02-02 and DEL-08-03 own adjacent concerns; query keys per ADQ-13.
- Candidate code: NO_CANDIDATES (documentary).
- Check against: `projects/chirality-app-dev/docs/PRD.md` §8.2 FR-008 and `docs/TYPES.md` §4 (not read); `REFERENCE_HASHES.csv` (PRD Match `NO`).
- Candidate decisions: D-APP-38; D-APP-56.

## CLM-028 — Trade-offs (SoW L460)
- Gist: prefer canonical vocabulary in tests and route state; keep runtime out; keep disabled options visible; treat implementation keys as evidence, not authority.
- Candidate code: NO_CANDIDATES (design rationale). Related code facts are in CLM-005 and CLM-026.
- Candidate decisions: none specific.

## CLM-029 — Examples (SoW L472)
- Gist: examples: NORMATIVE cell to mounted loop persona; OPERATIVE cell to PIPELINE in the sidebar; `/pipeline` opens the loop-first shell with the Pipeline tab selected.
- Candidate code:
  - `FE/src/app/pipeline/pipeline-client.tsx:9-19`: REACH=LIVE; renders `WovenDialogueShell` with `defaultSurface="pipeline"`, which the shell does not read (R1). The `LoopTertiaryShell defaultSidebarTab="pipeline"` element is voided.
  - Matrix cells: `agent-matrix.tsx` (no cells, R4).
- Candidate tests: `loop-tertiary-routes.test.ts :: "opens the Pipeline deep link in the continuing conversation"` (mocked shell). `woven-dialogue-shell.test.tsx :: "only mounts Dialogue even with historical %s surface input"`. `pipeline-surface.test.ts`.
- Candidate decisions: D-APP-31; D-APP-74; D-APP-108 (Q3).

## CLM-030 — Conflict Table CONFLICT-001..003 (SoW L483)
- Gist: three recorded conflicts: dispatch package path versus folder name; PRD expected versus actual SHA (now MATCH); PRD FR-008 SPEC pointer versus TYPES §4.
- Candidate code: NO_CANDIDATES (documentary).
- Check against: folder name `…/PKG-02_Desktop_Shell_Navigation_and_Operator_State/` (exists; a grep for `PKG-02_Desktop_UI_and_Local_Experience` was not run); `REFERENCE_HASHES.csv`; `docs/PRD.md`, `docs/SPEC.md`, `docs/TYPES.md` (not read).
- Candidate decisions: D-APP-38 (CONFLICT-002 "reconciled under D-APP-38"); none found for CONFLICT-001/003 in DECISION_HITS.

## REM-1 — Record-only `metadata.icons` note (_STATUS L12)
- Gist: no code owed; Next `metadata.icons` is satisfied via the `src/app/icon.svg` file convention.
- Gate suffix: none (no `NOT_SELECTABLE_UNTIL`).
- Candidate code:
  - `FE/src/app/layout.tsx:57-60 metadata`: REACH=LIVE; no `icons` field.
  - `FE/src/app/icon.svg`: absent at `00115c719`; deleted by `b2b32669c` (2026-09-10) along with `FE/public/chirality-app-icon.svg` (R5).
- Where to check: `DEL/_STATUS.md` L12-14 (still carries the note); `git -C <frozen> show --stat b2b32669c`.
- Candidate decisions: none specific.

## REM-2 — Cross-reference to DEL-09-04: Finder/Dock daemon bounce (_STATUS L15)
- Gist: launching from Finder or the Dock while the daemon runs briefly bounces the runtime; the causal fix, a helper bundle, is escalated to the owner.
- Gate suffix: none (cross-reference, "owned by DEL-09-04").
- Candidate code: not searched in depth. Possibly relevant, REACH=LIVE, content not checked: `FE/electron/desktop-process-policy.ts`, `runtime-service-host.ts`, `runtime-service-launcher.ts`.
- Where to check: `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md`. A grep for `bounce|helper bundle|LaunchServices` there found no hits. `DEL-02-02 _STATUS.md:22` mentions "distinct-helper implementation lands, rerun the D-APP-86 packaged parity", and `DEL-08-02 _STATUS.md:24` mentions the same rerun. The runtime is now App-owned per D-APP-127.
- Candidate decisions: D-APP-127 (context).

## REM-3 — Cross-reference to DEL-02-02 / DEL-08-02: packaged evidence (_STATUS L21)
- Gist: packaged Desktop evidence for the Workbench/Pipeline surfaces and the navigator recorded-session selection path is still owed.
- Gate suffix: none (cross-reference).
- Candidate code: Workbench/Pipeline surfaces not rendered (R2). Navigator selection path `navigator.tsx:117` > `guarded-session-selection.ts:59` (REACH=LIVE).
- Where to check:
  - `…/DEL-02-02_Workbench_and_Pipeline_Selection_UX/_STATUS.md`: L64-74 (2026-08-03 D-APP-86 packaged Workbench/Pipeline evidence; "residual was removed", L69); L54 (T1 "Work/Workbench/Pipeline mounts retired, legacy URLs retained").
  - `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-02_Persona_Alias_and_Agent_Matrix_Routing_Contract/_STATUS.md` L10-30 (Remaining; L24, L47 packaged items).
- Candidate decisions: D-APP-86 (cited in DEL-02-02 status; not in DEL-02-01 DECISION_HITS).

## REM-4 — DEL-02-01-V3-01 (_STATUS L27)
- Gist: header removal, Stone tokens, composer context line with folder select, and the plain-language copy pass (T2).
- Gate suffix (verbatim): `NOT_SELECTABLE_UNTIL: DEL-02-02-V3-03 landed`.
- Gate status check: `…/DEL-02-02_Workbench_and_Pipeline_Selection_UX/_STATUS.md:52` ("2026-09-06 - Ordinary factual T1 closeout: DEL-02-02-V3-03 removed from Remaining after PR733 merge 8e649ea…"). DEL-02-02 Remaining L10-50 no longer lists V3-03.
- Candidate code (the write locus):
  - `shell-frame.tsx:307-310` headerless branch (rendered).
  - `FE/src/app/globals.css:4007` "SCA-APP-010 Stone presentation" token block, `:4341 .shell--stone`.
  - `chat-panel.tsx:2121-2160` context line (R6, no delegation or rung).
  - `folder-select.tsx:15`, `persona-picker.tsx:25`.
  - `FE/electron/main.ts:103 registerRecentFolder`, `:987` reveal, `:1129 open-file`; `FE/electron/preload.ts:49, 78`.
  - `woven-dialogue-shell.tsx`, `navigator.tsx`, `activity-shelf.tsx`.
  - All REACH=LIVE.
- Candidate tests: `folder-select.test.tsx`, `chat-panel-folder-binding.test.tsx`, `historical-chat-reveal.test.tsx`, `FE/src/__tests__/electron/folder-conveniences.test.ts`, `shell-frame.test.tsx`, `woven-dialogue-shell.test.tsx`.
- Where to check item progress: `DEL/_STATUS.md` History L61-63 (2026-09-06 integration: "does not close whole T2"; "Finder-drop, Dock behavior, full multi-root behavior, no-folder execution and PDF remain unproven"); `DEL/_run_records/SHELL_CONVERGENCE_V5_2026-09-06.md`, `APP_V3_INTEGRATION_2026-09-06.md`.
- Candidate decisions: D-APP-108 (Q9), D-APP-120 (A1 seam / no-folder), D-APP-98 (Electron authority), D-APP-127.

## REM-5 — DEL-02-01-V3-02 (_STATUS L35)
- Gist: left-panel chat organisation: search, titles, pins, groups, archive and the context menu (T6 part), with delete as a local hide and redacted titles.
- Gate suffix (verbatim): `NOT_SELECTABLE_UNTIL: DEL-02-01-V3-01 landed`.
- Gate status check: `DEL/_STATUS.md` Remaining L27 (V3-01 still listed at the frozen basis).
- Candidate code:
  - `navigator.tsx:117 Navigator` (props include `chatTitles`, `chatPins`, `chatArchived`, `chatDeleted`, `chatGroups`, `searchMessages`).
  - `chat-organization.ts:60 deriveChatTitle` (`redactConfiguredApiKeys` at `:65`, from `FE/src/lib/harness/run-logger.ts`), `:136`, `:150`, `:268 createChatReplayReader`.
  - `woven-workspace-state.ts:279 indexWovenChats`.
  - All REACH=LIVE; SYMBOL-REACH: Navigator rendered; the others are imported by the woven shell (`:21`).
- Candidate tests: `woven-dialogue-navigator.test.tsx` (13 cases, including search, the context menu with rename/pin/unpin/archive, groups, and local delete with the recoverable record); `chat-organization.test.ts` (11 cases); `woven-dialogue-shell.test.tsx :: "persists a redacted live title…"`, `"owns Cmd-K while collapsed…"`; `redaction-path-matrix.test.ts`.
- Candidate decisions: D-APP-108 (Q1, Q6).

## REM-6 — DEL-02-01-V3-03 (_STATUS L43)
- Gist: folder per chat: `knownRoots`, multi-root session listing, a folder line per chat, and a provider root derived from the active session (T6 part).
- Gate suffix (verbatim): `NOT_SELECTABLE_UNTIL: DEL-02-01-V3-01 landed`.
- Gate status check: `DEL/_STATUS.md` Remaining L27 (V3-01 listed).
- Candidate code:
  - `chat-panel.tsx:2123` (`knownRoots` to `FolderSelect`).
  - `navigator.tsx:104` (folder line, "No folder").
  - `chat-organization.ts:103 chatFolderKey`, `:111 folderSectionLabels`.
  - `woven-dialogue-shell.tsx:112` (`folderNotices`), `:450 navigatorSessions`.
  - `woven-workspace-state.ts` known roots (test "validates ISO root instants, deduplicates newest, sorts and caps roots").
  - All REACH=LIVE. `FE/src/lib/runtime-client/**` multi-root reads: NOT checked.
- Candidate tests: the `woven-dialogue-shell.test.tsx` "WovenDialogueShell per-chat folders" suite (L578-679); `woven-dialogue-navigator.test.tsx :: "collapses folder sections through the organisation patch and shows recovery actions for an unavailable folder"`; `chat-organization.test.ts :: "groups chats by recorded folder…"`; `woven-workspace-state.test.ts` "additive shell convenience fields" suite.
- Candidate decisions: D-APP-108; D-APP-120 (no-folder routing).

## REM-7 — DEL-02-01-V3-04 (_STATUS L51)
- Gist: app icon replacement (T7 renderer part) through the Next metadata path and public asset; the pop-out window is deferred (Q5).
- Gate suffix (verbatim): `NOT_SELECTABLE_UNTIL: DEL-02-05-V3-05 landed`.
- Gate status check: `…/DEL-02-05_API_Key_UI_and_Runtime_Feedback/_STATUS.md:23` ("2026-09-07 - Removed DEL-02-05-V3-05 after PR745 merged as `8275b4a7…`"). The dependent item is `DEL-09-04 _STATUS.md:114` DEL-09-04-V3-02 (`NOT_SELECTABLE_UNTIL: DEL-02-01-V3-04 selected`).
- Candidate code (the write locus):
  - `FE/src/app/icon.svg` and `FE/public/chirality-app-icon.svg`: absent (deleted by `b2b32669c`, R5).
  - `FE/build/icon-macos.svg` and `FE/build/icon.icns`: present, both changed by `b2b32669c` ("Use website artwork for macOS icon").
  - `FE/scripts/generate-macos-icon.mjs` (hint hit; not in the reach map).
- Where to check: `DEL/_STATUS.md` L51-58 (still in Remaining at the frozen basis).
- Candidate decisions: D-APP-108 (Q5).

---

## Cross-cutting

- Recurring modules and reach:

  | Module | Reach | Units |
  |---|---|---|
  | `FE/src/components/woven-dialogue/woven-dialogue-shell.tsx` | LIVE, rendered | ~16 |
  | `FE/src/components/shell/shell-frame.tsx` | LIVE; workspace branch rendered, header/nav branch only via not-found | ~12 |
  | `FE/src/components/shell/chat-panel.tsx` | LIVE, rendered (woven context line) | ~8 |
  | `FE/src/components/portal/agent-matrix.tsx` | LIVE by import, not rendered; role directory, not a matrix | ~10 |
  | `FE/src/components/woven-dialogue/navigator.tsx` | LIVE, rendered | ~8 |
  | legacy chain `portal-loop-shell` / `loop-shell` / `loop-tertiary-shell` / `sidebar-right-loop-layout` / `tertiary-sidebar-tabs` / `pipeline-surface` / `workbench-surface` | LIVE by import, not rendered | ~12 |
  | `FE/src/lib/woven-dialogue/chat-organization.ts` | LIVE | 3 |
  | `FE/src/lib/portal/agent-matrix-{cells,launch}.ts` | TEST_ONLY | 4 |

- Live versus legacy (reach facts only):
  - No DEL-02-01 code path is `REACH=LEGACY_ONLY`.
  - The whole loop-first/PORTAL/matrix generation of the shell (CLM-003..030 subject matter) is import-LIVE and render-dead: the page routes pass it as a `legacy` prop that `WovenDialogueRoute` discards (R1).
  - The SCA-APP-004/010 subject matter (SEC-1..4, REM-4..6) sits on rendered code.
  - Tests for the legacy generation still exist and pass by construction. `workspace-sidebar.test.ts` supplies tab props directly; `loop-tertiary-routes.test.ts` and `woven-dialogue-route.test.tsx` mock `WovenDialogueShell`; `shell-frame.test.tsx` renders the default (header) variant with `usePathname` mocked to `/`.
- Touched paths: none under `FE/**` (`TOUCHED_PATHS.csv` covers runtime packages, runtime execution files and export files only), so PostReleaseBasis blame is expected to be unnecessary for DEL-02-01 code citations.
- Hash facts: all three `REFERENCE_HASHES.csv` rows for DEL-02-01 (CONTRACT, PRD, SPEC) have recorded `MATCH` and recomputed Match `NO`. The D-APP-127 application map shows all five carriers `NO` / `NONE_FOUND`.
- SoW-internal differences that may matter to the forward workers:
  - CLM-007/014 say UPD-106 is implemented; CLM-023 says it is withheld.
  - CLM-004/009/018 say dependency extraction is deferred with no Dependencies.csv, but `DEL/Dependencies.csv` exists.
#END
