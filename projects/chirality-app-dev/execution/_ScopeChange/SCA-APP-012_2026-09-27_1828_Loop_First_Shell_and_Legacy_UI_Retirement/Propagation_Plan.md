---
amendment_id: SCA-APP-012
doc_kind: scope_change.propagation_plan
decomp_variant: SOFTWARE
checkpoint_group: 2
created: 2026-09-27
status: awaiting_checkpoint_2_acceptance
revision: 2 (independent review of 4c572475f: N1-N9)
basis_commit: 830913331 (package basis; branch rebased onto 974bf7da4, which changed only PEC files)
accepted_group1_snapshot: execution/_ScopeChange/checkpoint_snapshots/SCA-APP-012_GROUP-1_2026-09-27/
workflow: scope-change (bundled)
---

# SCA-APP-012 — Checkpoint group 2: exact amendment and propagation plan

> **Status: PROPOSED, revision 2, awaiting the owner's checkpoint-group-2
> act.** Revision 2 applies the independent review of `4c572475f` (no blocking
> finding; nine corrections, §12). Nothing here is applied. This plan consumes
> the accepted group-1 snapshot
> `checkpoint_snapshots/SCA-APP-012_GROUP-1_2026-09-27/`
> (`DECISION.md` SHA-256 `0bc055869d3b29f6fc719ad8eb376f580073eaabafd5f75faa1978d10cbc6abe`,
> `ACCEPTED_MANIFEST.csv` SHA-256 `86b0f7cb87ba45c8a0655088864905e20467ed60442a13f4f267ed27a4387056`).
> It proposes exactly what was accepted there:
> - BASE and S;
> - R-b, W-b and P-keep;
> - the defaults L-lib, S-tool and E (no CONTRACT change);
> - the KG-033 acknowledgment, unchanged.

---

## Checkpoint group 2 — what you are asked to decide

### What accepting group 2 authorizes

Group 2 fixes the exact change. Accepting it authorizes checkpoint-group-3
preparation only:

1. **Scope text.** Writing the **80 exact text edits** in
   `Amendment_Preview.md` to **12 files** (the decomposition, the PRD, SPEC
   and PLAN, and eight Scopes of Work) as the group-3 candidate. 79 are
   written before group 3 for review. One, E26 (the decomposition revision
   and date), waits for your group-3 acceptance (§6).
2. **Action register.** Accepting `Amendment_Actions.csv`: **24 rows, 23
   MODIFY and 1 ADD** (DEC-027), the rows you selected at group 1.
   `ScopeChanging` is YES on 15 rows.
3. **Supersession bindings.** Accepting the **22 rows** of
   `Supersession_Delta.csv`. They supersede D-APP-74's compatibility clause
   (lines 97-99) for the loop-first UI and the two retired routes, D-APP-74's
   old-UI retirement clause (line 107) for the loop-first UI, the accepted
   SCA-APP-011 DEL-07-02 scaffold follow-up, and the D-APP-56 R4-P29 launcher
   confirmation.
4. **Code change.** Preparing the code change specified in §4 for review at
   group 3, together with the scope text.
5. **Handoffs.** The downstream handoffs in §8: incremental `project-setup`,
   `dependency-extract` against DX-01, DX-02, DX-03 and DX-05, the audits,
   and the TM-APP-051 note.

Nothing is applied or merged before you accept group 3. `_LATEST.md` stays on
SCA-APP-011 until then.

### Points to note before you decide

None of these changes what you accepted at group 1. They are listed so that
your group-2 act covers them knowingly.

1. **Basis refresh G1B-01.** Main moved to `830913331` (PRs #1015 and #1016)
   after your group-1 act. Every file this amendment edits, and every input
   the accepted brief hashed, is byte-identical. Main changed one dependency
   row the baseline lists (DEP-02-01-006, now `UPSTREAM`/`INTERFACE` under
   your HGD-1 ruling), outside every edit. Recorded in `Decision_Log.md`.
2. **Sweep additions within accepted rows.** The residual sweep (§9, check 6)
   found wording that the group-1 line lists did not name but that carries
   the same retired obligation. It is edited under the same rows: DEL-02-03
   CLM-012, CLM-019, CLM-020 and CLM-030 (route consumers, row 22), and
   DEL-07-02 CLM-010 (`ProjectScaffoldPort`, row 19). No new row is added.
3. **Controlling sections.** DEL-02-01, DEL-02-03 and DEL-08-02 each gain a
   `## SCA-APP-012 Current Contract (Controlling)` section, following the
   SCA-APP-010 and SCA-APP-011 pattern. Earlier clauses stay as dated history.
4. **Two test names fixed here.** The new role-picker guard test is
   `frontend/src/__tests__/components/chat-panel-role-picker-guard.test.tsx`.
   `loop-tertiary-routes.test.ts` keeps its file name (only its `describe`
   label changes), because it already checks that `/workbench` and
   `/pipeline` open the dialogue shell.
5. **A superseded SCA-APP-011 text.** Row 19 replaces accepted SCA-APP-011
   wording in DEL-07-02 ("the Runtime loop … decides on it" and the
   follow-up). That is why it has a supersession row (D-019).

### The change in one screen

**Removed (code, after group 3):**

| Code | Files (under `frontend/src/`) |
|---|---|
| Loop-first shell | `components/shell/loop-shell.tsx`, `portal-loop-shell.tsx`, `loop-tertiary-shell.tsx`, `sidebar-right-loop-layout.tsx`, `tertiary-sidebar-tabs.tsx` |
| Role-directory panel | `components/portal/agent-matrix.tsx` |
| Discarded `legacy` prop and `?legacy=1` link | `WovenDialogueRoute` prop and its four callers; `legacyHref` in the dialogue shell, navigator and shell frame |
| Portal helpers (L-lib) | `lib/portal/agent-matrix-cells.ts`, `lib/portal/agent-matrix-launch.ts` |
| Unconsumed provider | `components/workspace/deliverables-provider.tsx` and its mount |
| Scope route | `app/api/working-root/scope/route.ts` |
| Flat-file workflow list (W-b) | `components/woven-dialogue/workflows-view.tsx`, `workflow-detail.tsx`; `app/api/working-root/workflow/` (route, store, contract) |
| Dead CSS | 11 legacy-only class tokens, 11 dead selector families, 8 view-only workflow classes |

**Kept:**
- the `/workbench` and `/pipeline` pages (P-keep), rendering the dialogue
  shell;
- `scanProjectScopes` and `/api/project/deliverables`;
- `lib/workspace/task-scope.ts` and the dispatch contract;
- the lifecycle, dependency and scaffold libraries and `scaffold_preview`;
- `/api/working-root/workflow-drafts` and the method-library view;
- `electron/renderer-window-policy.ts`, unchanged (D-APP-121 frozen).

**Tests.** Registry case 1 of `agent-matrix-cells.test.ts` moves to
`persona-resolution.test.ts`. A new test guards the role picker while a turn
runs. The dropped cases test code no product path reaches (§4).

**Scope text.**
- DEL-02-01: the loop-first UI is retired; routes, queries and aliases stay.
- DEL-02-03: the scope route and REQ-009 are retired, and REQ-010 is restated
  (status read-only, no transition control).
- DEL-08-02: hooks name where the alias and guard semantics now live.
- DEL-07-03 and DEL-08-03: the retired route is no longer named as a scan
  surface.
- DEL-07-02 and DEL-06-03: no App-side scaffold entry, and no write-capable
  scaffold tool, is planned.
- DEL-02-02: one line records the removed workflow list.
- PRD, SPEC, PLAN and the decomposition: every compatibility clause records
  this amendment as the separate owner decision on the loop-first UI; the
  two routes join the route carve-outs; DEC-027 is added.

**Unchanged:** topology (10 packages, 52 deliverables, 84 scope items, 10
objectives), scope-item mappings, context envelopes, lifecycle states,
CONTRACT, DIRECTIVE and TYPES. No dependency register is written by this
amendment; re-extraction is a downstream handoff (§8).

### Choices that remain

| # | Choice | Options | Recommendation |
|---|---|---|---|
| **T** | Who writes the Scope of Work, PRD, SPEC and PLAN text | **T-a:** this amendment writes the exact text at group-3 preparation. The write boundary names all 12 files (§2). **T-b:** this amendment writes only the decomposition; the eight Scopes of Work go to `project-setup` INCREMENTAL (`scope-of-work` REVISE) with the same text, and the PRD, SPEC and PLAN to a separate owner-approved change. | **T-a.** The exact text is ready and validated (§9); one audited poststate is simpler, and T-b would re-derive the same text. SCA-APP-011 did the same (its W-a). |
| **Q** | Sequencing of scope text and code | **Q-a:** group 3 reviews the written scope-text candidate together with the code candidate (§4); after your group-3 acceptance one PR lands both. **Q-b:** the scope-text PR lands first and the code PR after it; for a short time the texts would name a test file (`chat-panel-role-picker-guard.test.tsx`) that does not exist yet. | **Q-a.** It keeps text and code in step, as SCA-APP-011 did. |

Everything else is fixed by your group-1 acceptance.

**A short answer is enough**, for example:

> "Accept SCA-APP-012 group 2: T-a, Q-a."

I then record your words verbatim in the group-2 decision snapshot and
prepare group 3.

---

## 1. Basis consumed

| Input | Identity |
|---|---|
| Accepted group-1 snapshot | `checkpoint_snapshots/SCA-APP-012_GROUP-1_2026-09-27/` (hashes above); pointer `SCA-APP-012_GROUP-1_AUTHORIZED.md` |
| Accepted impact assessment | `Impact_Assessment.md` revision 4, SHA-256 `894d04e598b20269e24bf6169ca97cfa2e3af8ffbcc9febeb203938920bd3225` |
| Accepted intake | `Intake_Actions.csv` revision 4, SHA-256 `d2ae9c44e78457c7767b699390df5109d5d1f00ff1ccc7e751db4b9d0f9ec4c9`; rows 1–22 and 26–27 |
| Preimages | Every edited file's SHA-256 is recorded in `Evidence/Group2/PREIMAGE_POSTIMAGE.csv`. All equal the hashes in the accepted `Brief.md` (for example decomposition `cf6e56eb…d2321876`, PRD `95245121…1249997`, SPEC `5a6fcf15…946e017f`, PLAN `e5e3045b…c093`) |
| Package basis | `origin/main` `830913331` (basis refresh G1B-01; `Decision_Log.md`). The branch was then rebased onto `974bf7da4` (PR #1014), which changed only PEC files: no App file, no edited file and no hashed input moved (`Decision_Log.md` G1-NOTE-1) |
| Active pointer | `_LATEST.md` → SCA-APP-011 (SHA-256 `904c1bd6…62185637`); group-3 posture `ACCEPTED_PREDECESSOR` |

## 2. Write boundary (T-a)

The group-3 preparation writes **only** these files, and only the edits in
`Amendment_Preview.md`:

| File | Package role | Edits |
|---|---|---|
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Working surface | E20-E26 (E26 acceptance-conditional) |
| `docs/PRD.md` | Authoritative carrier (product requirements) | E27-E40, E60-E63 |
| `docs/SPEC.md` | Authoritative carrier (physical/API contract) | E41-E45, E59 |
| `docs/PLAN.md` | Authoritative carrier (roadmap) | E46-E53 |
| DEL-02-01 `ScopeOfWork.md` | Production contract | E01-E03 |
| DEL-02-02 `ScopeOfWork.md` | Production contract | E79, E80 |
| DEL-02-03 `ScopeOfWork.md` | Production contract | E04-E07, E64-E78 |
| DEL-06-03 `ScopeOfWork.md` | Production contract | E58 |
| DEL-07-02 `ScopeOfWork.md` | Production contract | E54-E57 |
| DEL-07-03 `ScopeOfWork.md` | Production contract | E08-E10 |
| DEL-08-02 `ScopeOfWork.md` | Production contract | E11-E18 |
| DEL-08-03 `ScopeOfWork.md` | Production contract | E19 |

The application also writes these snapshot and handoff artifacts under
`_ScopeChange/`:
- the group-2 and group-3 decision snapshots and their `_AUTHORIZED` pointers;
- the candidate snapshot files (`Supersession_Map.csv`,
  `Post_Change_Coverage.json`, `RUN_SUMMARY.md`, `Handoff_State.md`);
- after group-3 acceptance, `_LATEST.md` (§6).

It does **not** write:
- `docs/CONTRACT.md` or the companion register (E: no change);
- `docs/TYPES.md` or `docs/DIRECTIVE.md` (NO_CHANGE under P-keep, Impact
  Assessment §3.4 and §9);
- any `_CONTEXT.md` (none names a retired item; §9 check 6);
- any `_STATUS.md`, `Dependencies.csv`, `_DEPENDENCIES.md` or the Task
  Management register;
- any other deliverable.

No lifecycle state changes. No `ISSUED` or `CHECKING` deliverable is touched;
all eight are `IN_PROGRESS`, so no reopening is involved and
`write_status.sh` is not used.

Under T-b the table shrinks to the decomposition. The eight SOW rows become
`project-setup` INCREMENTAL handoffs carrying the same exact text, and the
PRD, SPEC and PLAN edits go to a separate owner-approved documentation change.

## 3. Register and exact text

`Amendment_Actions.csv` is the proposed authoritative register. Rows 1–22 are
intake rows 1–22; row 23 is intake row 26 (W-b, DEL-02-02) and row 24 is
intake row 27 (W-b, the read-route carve-outs). Each row names its exact
edits. Row 24 has no edit of its own: its text is carried by edits listed
under rows 8, 12, 13, 17 and 18, which name both retired routes together.
`AffectedFiles` names only files this amendment writes (contract L43, L377).

`Evidence/Group2/amendment_edits.py` holds every edit as data (exact `old`
and `new` bytes). `Evidence/Group2/build_amendment_preview.py` renders the
preview and records, per file, the preimage hash, the candidate hash (every
edit except E26) and the final hash where it does not depend on the date
(`Evidence/Group2/PREIMAGE_POSTIMAGE.csv`). Its modes:

- default: render `Amendment_Preview.md` and the CSV;
- `--check`: write nothing; fail if a preimage drifted, if the CSV differs
  from what the edit data produces, if `Amendment_Preview.md` differs from
  the rendering of the edit data, or if `Amendment_Actions.csv` breaks its
  schema;
- `--candidate`: group-3 preparation (§6 step 3). It refuses any root inside a
  git work tree (this checkout, another checkout, or a directory inside one)
  unless that root holds `SCA-APP-012_GROUP-2_AUTHORIZED.md`; only a scratch
  copy outside every git work tree is written without the pointer;
- `--finalize`: after group-3 acceptance only; refused without an accepted
  `SCA-APP-012_GROUP-3_{date}/DECISION.md` of the same date (§6).

Wording rules applied throughout:

- **Non-destructive.** Retired requirements and clauses are marked
  `[RETIRED — SCA-APP-012]` and kept as dated history. DEL-02-01, DEL-02-03
  and DEL-08-02 gain a controlling `## SCA-APP-012 Current Contract
  (Controlling)` section.
- **Owner words.** The only owner words quoted in scope text are the
  direction "Scaffolding through the agent is enough." (DEC-027, DEL-07-02,
  DEL-06-03).
- **Scope decisions, not code history.** The text states scope decisions
  ("retired by SCA-APP-012"). It does not claim that code has already been
  deleted. Verification hooks name the exact test files the code change in §4
  keeps or creates.
- **Dates.** Every date in the candidate text is the owner-direction date,
  2026-09-27, except the E26 slot (§6).

## 4. Code change specification (for the responsible current role)

The code change is repository work by the App loop under standing Git
authority. It is not an SCA write. It starts from current `main` (there is no
earlier candidate) and must end in exactly this state. Paths are under
`projects/chirality-app-dev/frontend/src/` unless stated.

**Delete:**

| Path | Why |
|---|---|
| `components/shell/loop-shell.tsx`, `components/shell/portal-loop-shell.tsx`, `components/shell/loop-tertiary-shell.tsx`, `components/shell/sidebar-right-loop-layout.tsx`, `components/shell/tertiary-sidebar-tabs.tsx` | The five loop-first shell modules; reachable only as the discarded `legacy` element (Impact Assessment §3.1 S1) |
| `components/portal/agent-matrix.tsx` | Role-directory panel; imported only by `tertiary-sidebar-tabs.tsx` |
| `__tests__/components/agent-matrix-panel.test.ts` | Test of the panel |
| `lib/portal/agent-matrix-cells.ts`, `lib/portal/agent-matrix-launch.ts` | L-lib: no product importer |
| `__tests__/lib/agent-matrix-launch.test.ts` | Test of the launch helper |
| `__tests__/lib/agent-matrix-cells.test.ts` | After porting case 1 (below); case 2 (`isRoleSelectionBlocked`, an identity helper with no product caller) is dropped |
| `components/workspace/deliverables-provider.tsx` | No `useDeliverables` consumer |
| `app/api/working-root/scope/route.ts` | No caller in the App, Electron, scripts or Runtime, and no test. Its client (the Workbench form's fetch) was already removed by SCA-APP-011 (commit `5ba17042b`); confirm with a grep that no caller remains |
| `components/woven-dialogue/workflows-view.tsx`, `components/woven-dialogue/workflow-detail.tsx` | W-b: no product importer since commit `9b005c23a` |
| `__tests__/components/woven-workflows.test.tsx` | Test of the view |
| `app/api/working-root/workflow/route.ts`, `app/api/working-root/workflow/workflow-store.ts`, `app/api/working-root/workflow/workflow-read-contract.ts` | W-b: `GET /api/working-root/workflow`; its only caller was `workflows-view.tsx`; the store and contract have no other user |
| `__tests__/api/working-root-workflow.test.ts` | Test of the read route |

**Modify:**

| Path | Change |
|---|---|
| `components/woven-dialogue/woven-dialogue-route.tsx` | Remove the `legacy` prop (`void legacy`) |
| `app/page.tsx`, `app/chat/page.tsx`, `app/workbench/workbench-client.tsx`, `app/pipeline/pipeline-client.tsx` | Stop passing `legacy`; drop the shell imports. Both page routes stay (P-keep) |
| `components/woven-dialogue/woven-dialogue-shell.tsx` (L384-388), `components/woven-dialogue/navigator.tsx` (L119), `components/shell/shell-frame.tsx` (L56) | Remove `legacyHref` and the `?legacy=1` link it built |
| `app/layout.tsx` | Remove the `DeliverablesProvider` import and mount (L7, L104-108). Restate the metadata description ("PORTAL, PIPELINE, and WORKBENCH shell for local agent execution", L59) to describe the dialogue shell |
| `app/page.tsx`, `app/chat/page.tsx`, `app/workbench/page.tsx`, `app/pipeline/page.tsx` | Restate the Suspense fallbacks ("Loading live loop portal...", "Loading direct chat...", "Loading workbench...", "Loading pipeline...") to neutral loading copy |
| `lib/shell/loop-first.ts` | Remove `buildPortalPersonaHref`, `buildDirectChatHref`, `PORTAL_ROUTE` and `CHAT_ROUTE` (no product user outside the retired shells); keep `CHAT_SECTION` (`chat-panel.tsx` uses it) |
| `components/shell/persona-picker.tsx` | Remove the `buildHref` prop (its only caller was `portal-loop-shell.tsx`) |
| `components/shell/workspace-sidebar.tsx` | Remove the `portalTab`/`workbenchTab`/`pipelineTab` props, the `PORTAL_TAB`/`WORKBENCH_TAB`/`PIPELINE_TAB` constants, their panel branches, and the `'portal' \| 'workbench' \| 'pipeline'` members of `SidebarTabId`. `AppShell` (used by `not-found.tsx`) passes none of these props and holds the sidebar tab in `useState` (default `'files'`); the sidebar tab is not persisted, so no stored value needs tolerant parsing |
| `lib/woven-dialogue/woven-workspace-state.ts` | No change. Its persisted `WovenWorkspaceSurface` keeps the `'workbench' \| 'pipeline'` members and tolerant parsing (SPEC §17.8), because the two page routes stay (P-keep) |
| `app/globals.css` | Remove the 11 legacy-only class tokens (`loop-chat-host`, `loop-grid`, `loop-grid--sidebar-collapsed`, `loop-main`, `loop-persona-bar`, `loop-sidebar`, `portal-launch-notice`, `portal-matrix`, `portal-matrix--sidebar`, `portal-matrix-header`, `portal-matrix-heading`) and the 11 dead selector families (`matrix-grid`, `matrix-cell`, `matrix-header-cell`, `matrix-row-group`, `matrix-row-label`, `portal-start-session`, `portal-deliverables`, `portal-deliverable-grid`, `portal-deliverable-row`, `portal-deliverable-name`, `portal-deliverable-key`). Keep `shell-pane*` (`AppShell` uses it) |
| `components/woven-dialogue/workflows.module.css` | Remove the 8 classes only the retired view used (`caption`, `file`, `foot`, `list`, `markdown`, `notice`, `provenance`, `view`); keep `header` and `tabs` (`right-panel.tsx`) |
| `__tests__/lib/persona-resolution.test.ts` | Add ported case 1 of `agent-matrix-cells.test.ts`: TASK is not a direct-entry role and HELP_HUMAN is the new-chat default, read from `CHIRALITY_ROLES` (`@chirality/runtime-contracts`). Add a DEL-08-02-REQ-004 case: the historical `RECONCILING` label and the TYPES §4 matrix labels (rows `NORMATIVE`, `OPERATIVE`, `EVALUATIVE`; columns `GUIDING`, `APPLYING`, `JUDGING`, `REVIEWING`) each resolve to `HELP_HUMAN` and none is a key of `PERSONA_ALIASES`. `resolvePersona` accepts only the three direct-entry roles and the `HELP`/`AGENTS` aliases, so every other label falls back to the default; the existing negative case covers only `TASK`, `ORCHESTRATE`, `RESEARCH` and `CHANGE` |
| `__tests__/lib/pkg08-compatibility-boundaries.test.ts` | Keep the role-boundary case (read the three direct-entry roles from `CHIRALITY_ROLES`) and the dispatch case; drop the matrix-helper round trip |
| `__tests__/components/workspace-sidebar.test.ts` | Both current cases exercise only the retired props or `SidebarRightLoopLayout`; dropping them would leave an empty suite, which vitest fails. Replace them with one default-tabs case for what `AppShell` renders: `WorkspaceSidebar` with `activeTab: 'workflow'` renders exactly the eight tabs Files, Sessions, Transcript, Tools, Subagents, Document, Workflow and Tool Kit as `role="tab"`, marks Workflow selected, and renders no Portal, Workbench or Pipeline tab. Rename the `describe` label accordingly |
| `__tests__/components/woven-dialogue-route.test.tsx` | Drop the `legacy` prop cases; keep the surface cases |
| `__tests__/components/loop-tertiary-routes.test.ts` | Keep the file and its two cases (`/workbench` and `/pipeline` open the dialogue shell); rename its `describe` label, which names `LoopTertiaryShell` |
| `__tests__/lib/loop-first.test.ts` | Trim case 1 (L12-14) to the `CHAT_SECTION` assertion only, since `PORTAL_ROUTE` and `CHAT_ROUTE` are removed, and update its import; drop cases 2-4 (`buildDirectChatHref`, `buildPortalPersonaHref`) |
| `__tests__/components/woven-dialogue-shell.test.tsx` | Delete the "preserves the legacy compatibility link with the current query string" case (L433-440) and the `legacyHref` in its `ShellFrame` mock |
| `__tests__/components/woven-dialogue-navigator.test.tsx`, `__tests__/components/historical-chat-reveal.test.tsx` | Drop the `legacyHref` prop |

**Add:**

- `__tests__/components/chat-panel-role-picker-guard.test.tsx`: the role
  picker in `components/shell/chat-panel.tsx` (L2124,
  `<PersonaPicker compact disabled={isRunning} />`) is disabled while a turn
  runs and enabled otherwise. No test covers it today.

**Keep unchanged:**
- `app/workbench/page.tsx` and `app/pipeline/page.tsx` routes (P-keep), the
  Electron renderer-security probe (`electron/main.ts` L647), the packaged
  security proof (`scripts/run-packaged-security-proof.mjs` L49) and
  `__tests__/contract-pins.manifest.ts` (L260, L384);
- `chat-panel.tsx` `resolveMode` and the `WORKBENCH`/`PIPELINE` session
  modes, drafts and session reuse;
- `electron/renderer-window-policy.ts`: **no edit**. It is a D-APP-121 frozen
  source identity; `scripts/run-packaged-security-proof.mjs` L55 pins its
  SHA-256 `e2d63d32423d1ef6b0a03259235676ac9cefadde00e4f067be4f13e5ed2cc3ed`.
  Its L13-14 comment still names the navigator's "open legacy interface"
  link; correct it the next time the file changes under D-APP-121;
- `lib/workspace/task-scope.ts`, `lib/pipeline/pipeline-dispatch-contract.ts`,
  `scanProjectScopes` and the `scope_scan` tool, `/api/project/deliverables`;
- `lib/shell/persona-resolution.ts`, `lib/woven-dialogue/guarded-session-selection.ts`,
  `lib/woven-dialogue/operator-projection.ts` (its own local
  `DIRECT_ENTRY_ROLE_IDS`);
- `app/api/working-root/workflow-drafts/**`, `method-library-view.tsx` and
  `right-panel.tsx`;
- the scaffold library and `scaffold_preview`.

**Records.**
- Run receipt and loop receipt for the code change (LOOP_INIT §5), citing the
  SCA-APP-012 group-2 and group-3 snapshots.
- MEMORY rows for DEL-02-01, DEL-02-02, DEL-02-03 and DEL-08-02 pointing to
  SCA-APP-012.
- A tranche manifest, if the App loop records one for the change.
- Regenerate `exports/chirality-app/` with the export tooling.

**Checks on the actual candidate:**
- frontend typecheck;
- the full frontend test suite and the registered harness checks;
- the build and premerge gates;
- a grep proving that no product import of the deleted modules, and no
  caller of the two retired routes, remains;
- `renderer-window-policy.ts` still hashes to `e2d63d32…`;
- `git diff --check` and Root G0–G4;
- a fresh read-only `software-code-review` of the product source.

## 5. Supersession bindings

`Supersession_Delta.csv` has 22 `SUPERSESSION` rows for the 14 register rows
marked `SupersessionBindingPresent = YES`:

| Superseded fact | Fact key | Register rows |
|---|---|---|
| D-APP-74 lines 97-99, "current UI remain compatibility surfaces until separately retired", for the loop-first UI | `loop_first_ui_compatibility` | 1, 7, 12, 13, 16, 17, 18 |
| D-APP-74 line 107, "Old-UI retirement requires separate owner acceptance …", for the loop-first UI | `loop_first_ui_retirement` | 1, 7, 12, 13, 16, 17, 18 |
| D-APP-74 lines 97-99 for `GET /api/working-root/scope` | `working_root_scope_route_compatibility` | 2, 8, 14, 15, 17 |
| D-APP-74 lines 97-99 for `GET /api/working-root/workflow` | `working_root_workflow_route_compatibility` | 24 |
| Accepted SCA-APP-011 DEL-07-02 text (lines 24-25: the Runtime loop decides on its scaffold API; a later App-side entry) | `del_07_02_runtime_scaffold_api_and_follow_up` | 19 |
| D-APP-56 R4-P29 (line 71): the launcher sits under DEL-02-03 REQ-009 | `del_02_03_req_009_launcher_ownership` | 22 |

**Line 107 and SCA-APP-010 D-015.** SCA-APP-010's map row D-015
(`workbench_pipeline_active_shell_retirement`) superseded line 107 for
Workbench and Pipeline only. SCA-APP-011 kept line 107 in force for the
loop-first shell. These rows bind line 107 under a different fact key, for the
loop-first UI only, so they do not compete with D-015. Line 107 stays in force
for any other old UI.

A dry run of `tools/coordination/accumulate_supersession_map.py` with the
SCA-APP-011 map as prior produces 85 rows (63 prior + 22) with 0 findings. At
group 3 the same command writes the candidate `Supersession_Map.csv`.

## 6. Acceptance-conditional edits and group-3 procedure

| Item | Rule |
|---|---|
| E26 `{APPLICATION_DATE}` | The decomposition Coverage and Telemetry `Revision` ("amended by SCA-APP-012") and `Date`. Not written into the candidate. After acceptance it is filled with the date of the group-3 decision folder `checkpoint_snapshots/SCA-APP-012_GROUP-3_{YYYY-MM-DD}/`, whose `DECISION.md` first line is `# SCA-APP-012 checkpoint group 3 — accepted …`; `--finalize` refuses any other date. It is the only slot: every file's candidate hash, and every final hash except the decomposition's, is fixed in `Evidence/Group2/PREIMAGE_POSTIMAGE.csv` |
| `_LATEST.md` | Moved to the accepted SCA-APP-012 snapshot folder only after group-3 acceptance; the SCA-APP-011 entry becomes the historical predecessor. The new pointer records SCA-APP-011's Runtime scaffold-API item (its L37) as closed by the Runtime loop in PR #1012. Its exact post-image is drafted in the group-3 package |
| `checkpoint_snapshots/SCA-APP-012_GROUP-2_{date}/` and `SCA-APP-012_GROUP-2_AUTHORIZED.md` | Written from your group-2 act |
| `checkpoint_snapshots/SCA-APP-012_GROUP-3_{date}/` | Written from your group-3 act |

No Runtime notice is needed: this amendment changes no Runtime surface, and
the Runtime loop already sent its own notice on the scaffold API.

Group-3 preparation, in order:

1. Resolve the group-2 decision snapshot and verify it binds this
   `Amendment_Actions.csv` by hash.
2. Run `build_amendment_preview.py --check`. No drift is allowed; if main has
   changed an edited file outside every edit, record a basis refresh with the
   new preimage and candidate hashes, as SCA-APP-011 did (G3B-01).
3. Write the candidate: `build_amendment_preview.py --candidate`. In this
   checkout, or any other git work tree, it needs the group-2 pointer
   `SCA-APP-012_GROUP-2_AUTHORIZED.md` in that root. It rechecks every
   preimage hash, writes every edit except E26, and verifies each written file
   against its recorded candidate hash.
4. Generate `Supersession_Map.csv` (accumulator) and `Post_Change_Coverage.json`
   (the baseline builder, rerun at the candidate).
5. Run `validate_postimage.py` and the SOW validator on the written files.
6. Run a fresh `audit-decomp`, or the equivalent deterministic baseline with
   disclosure.
7. Obtain an independent review of the written candidate together with the
   §4 code candidate (Q-a).
8. Present raw and adjusted `AuditState`, the closure verdict and the
   acceptance-conditional list.

After group-3 acceptance only: `build_amendment_preview.py --finalize --date
YYYY-MM-DD --group3-decision <path>` rechecks the candidate hashes and applies
E26; the pointer move follows, then the post-acceptance record under
`_PostAcceptanceValidation/`.

## 7. Deliverable propagation

| Deliverable | Lifecycle | Scope text | `_CONTEXT.md` | Dependencies |
|---|---|---|---|---|
| DEL-02-01 | IN_PROGRESS | MODIFY (row 1) | none | No change expected under P-keep (DEP-02-01-006 and -008 unchanged) |
| DEL-02-02 | IN_PROGRESS | MODIFY (row 23, a note) | none | No change expected |
| DEL-02-03 | IN_PROGRESS | MODIFY (rows 2, 3, 22) | none | DX-01 (DEP-02-03-009 retired), DX-02 (DEP-02-03-004 quote) |
| DEL-06-03 | IN_PROGRESS | MODIFY (row 20) | none | No change expected |
| DEL-07-02 | IN_PROGRESS | MODIFY (row 19) | none | No change expected |
| DEL-07-03 | IN_PROGRESS | MODIFY (row 4) | none | No change expected |
| DEL-08-02 | IN_PROGRESS | MODIFY (row 5) | none | No change expected under P-keep (DEP-08-02-013 unchanged; DX-04 does not apply) |
| DEL-08-03 | IN_PROGRESS | MODIFY (row 6, a label) | none | DX-03 (DEP-08-03-007 label); DEP-02-03-009 is its inbound edge |

For every deliverable: no `_STATUS.md` change, no reopening, no `CHECKING`
hold, and a MEMORY entry through the loop closeout.

## 8. Downstream reruns and handoffs (not executed by this workflow)

1. **`project-setup` in `INCREMENTAL` mode.** No additions to scaffold and no
   retirements to record. Under T-a the eight contracts are already written,
   so it refreshes the coordination records of the eight deliverables and
   their neighbours. Under T-b it carries the `scope-of-work` REVISE text.
2. **`dependency-extract`.** Run for DEL-02-03 and DEL-08-03, then
   `analyze_dep_closure.py`. Expected outcomes (checkable; the extraction run
   records them in an expected-outcome file, as SCA-APP-011 did with
   `DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.md`):

   | DX | Register row | Expected outcome | Check |
   |---|---|---|---|
   | DX-01 | DEP-02-03-009 (DEL-02-03 → DEL-08-03, `DOWNSTREAM`/`INTERFACE`, routing/preselection; `ACTIVE` with the DX-15 tension note) | `Status=RETIRED`, `SatisfactionStatus=NOT_APPLICABLE`, prior values kept in Notes, citing SCA-APP-012 (R-b) | Field values; ID kept; no row deleted |
   | DX-02 | DEP-02-03-004 (DEL-02-03 → REF-003 SPEC §17.2, `ACTIVE`) | `ACTIVE`; relationship unchanged; `EvidenceQuote` taken from the restated CLM-003 and no longer containing `/api/working-root/scope`; prior quote in Notes | `EvidenceQuote` has no `/api/working-root/scope`; Notes cite SCA-APP-012 |
   | DX-03 | DEP-08-03-007 (DEL-08-03 → REF-003, TargetName "docs/SPEC.md Section 17.2 working-root scope API", `ACTIVE`) | `ACTIVE`; `TargetName` names the `/api/project/deliverables` scan surface; prior label in Notes | `TargetName` has no "working-root scope API"; DEL-08-03 `_DEPENDENCIES.md` no longer reports `SOURCE_ENDPOINT_LABEL_CONFLICT` |
   | DX-04 | DEP-08-02-013 | **Does not apply** (P-keep): unchanged | — |
   | DX-05 | All registers | No `ACTIVE` row names `/api/working-root/scope`, `/api/working-root/workflow`, the loop-first shell modules, `DeliverablesProvider` or `ProjectScaffoldPort` | Screen, as SCA-APP-011's DX-16 |

   Only edges are retired or relabelled and no edge is added, so no cycle can
   form. DEP-02-01-006 (now `UPSTREAM`/`INTERFACE`, G1B-01) and DEP-02-02-020
   are unchanged under P-keep.
3. **Audits.** `audit-decomp` (post-change baseline) at group 3, then
   `audit-scope-closure` after the setup and code change.
4. **Code change** (§4) through the App loop, landed with the scope text under
   Q-a.
5. **Task Management TM-APP-051** ("Assign scope scan and route consumers",
   `DEFERRED`; APP-R024; DEL-02-03). Proposed disposition note for the row's
   owner (this workflow does not edit Task Management):

   | Consumer | After SCA-APP-012 |
   |---|---|
   | Route | Retired with DEL-02-03-REQ-009 (R-b) |
   | Scope scan | `/api/project/deliverables`; `/api/working-root/scope` retired |
   | Status | Restated read-only by DEL-02-03-REQ-010 from `/api/project/deliverables` |
   | Summary widget | Still unimplemented; stays with DEL-02-03 |

   The row then stays open only for the summary/status widget; this amendment
   does not close it.
6. **Export projection.** `exports/chirality-app/` is regenerated with the code
   change.
7. **`_LATEST.md` note.** At group 3 the new pointer records SCA-APP-011's
   Runtime scaffold-API item as closed by the Runtime loop (PR #1012).

## 9. Validation performed for this package

Run on the revision-2 package tree at `974bf7da4` (the package basis `830913331`
plus PR #1014, which changed only PEC files). No scope file, code or accepted
group-1 record changed.

| Check | Result |
|---|---|
| `build_amendment_preview.py` | 80 edits in 12 files. Every `old` passage occurs exactly once, in sequence; candidate and final images dry-run |
| `build_amendment_preview.py --check` | OK: all 12 preimages match `PREIMAGE_POSTIMAGE.csv`; the CSV equals what the edit data produces; `Amendment_Preview.md` equals the rendering of the edit data; `Amendment_Actions.csv` passes the schema check (10 contract columns, no surrounding whitespace, sequential `ActionSeq`, YES/NO flags). A test append to the preview made it FAIL, as intended |
| `check_candidate_mode.py` (scratch copies) | 22/22 PASS. The scratch root is outside every git work tree. `--candidate` is refused, and nothing is written, for this checkout (default root, `--root` naming it, `--root REPO/.`, a directory inside it), for another git checkout without the group-2 pointer (a `git init` scratch copy), and for a missing root. The other git checkout with a test pointer is written and matches every candidate hash. The scratch `--candidate` wrote 12 files, each matching its candidate hash, with E26 not applied and DEC-027 present; a rerun is refused on preimage drift. `--finalize` is refused for a draft heading, a date that differs from the decision folder and a wrong path; one `--finalize` with a test decision fills E26 only; a rerun is refused. This checkout is unchanged |
| `validate_postimage.py` | PASS (`Evidence/Group2/POSTIMAGE_VALIDATION.md`): 17 edited table rows keep their column count; all 8 edited Scopes of Work validate (exit 0 before and after); every edited unit naming a retired item carries an SCA-APP-012 marker; all 19 retired items are named with a marker; the two retired routes are gone from the PRD §9.2 and SPEC §17.2 tables; every register row has edits or is carried; the sweep of 114 files (every deliverable `ScopeOfWork.md` and `_CONTEXT.md`, the decomposition, PRD, SPEC, PLAN, DIRECTIVE and TYPES) finds 0 uncovered mentions after the edits (39 before), with 3 listed historical passages |
| `accumulate_supersession_map.py` dry run | 85 rows, 0 findings. A second run with `--check-map` against the first output: 0 findings, exit 0 (deterministic) |
| Group-1 baseline builder rerun (at `830913331`) | Differs from the accepted `Pre_Change_Coverage.json` only in the three G1B-01 values; the accepted file was restored unchanged (SHA-256 `c470779a…0cc0b2`) |
| Root G0–G3 (`validate_root_materialization_fence.py`, `validate_root_harness_adapter.py`, `validate_root_surface_ownership.py`, `validate_root_work_graph_dispatch.py`) | G0, G1, G2 and G3 PASS |
| G4 (`validate_instruction_tranche_manifest.py --base 974bf7da4 --head HEAD --added-manifests-only`) | Exit 0; 0 changed paths on the instruction surface |
| `validate_conflict_markers.py`, `validate_run_record_leaks.py` (base `974bf7da4`) | PASS; PASS (0 run-record files, 0 possible credentials) |
| `build_workflow_index.py --check` | PASS (78 methods) |
| `git diff --check` (base `974bf7da4`) | PASS |
| `exports/chirality-app/export_public.py`, run twice | No tracked change (export projection fresh); staging removed |

## 10. State fields and derivative surfaces

| Field | Value now | After group-3 acceptance (expected) |
|---|---|---|
| `DecompositionTruthState` | `NOT_STARTED` | `COMPLETE` |
| `DerivativePackageState` | `INCOMPLETE` | `INCOMPLETE` until dependency re-extraction and audits |
| `ContentRemediationState` | `NOT_REQUIRED` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `FROZEN` | `IN_PROGRESS` |
| `MetadataAlignmentState` | `NOT_REQUIRED` | `NOT_REQUIRED` |
| `AuditState` | `NOT_RUN` | Set by the group-3 audit |
| `ReadyForNextPhase` | `NOT_APPLICABLE` | `NOT_APPLICABLE` |

| Derivative surface | Classification | Owner |
|---|---|---|
| `_Evaluation/DecompCoverage` | STALE_REBUILD_REQUIRED | audit-decomp |
| `_Evaluation/ScopeClosureAudit` | STALE_REBUILD_REQUIRED | audit-scope-closure |
| `_Evaluation/DepClosure` | STALE_REBUILD_REQUIRED | analyze_dep_closure |
| DEL-02-03 and DEL-08-03 dependency registers | STALE_REBUILD_REQUIRED | dependency-extract (DX-01 to DX-03, DX-05) |
| `exports/chirality-app` | STALE_REBUILD_REQUIRED | export tooling, with the code change |
| Companion register | NO_CHANGE (E) | — |
| `_SEMANTIC_LENSING.md` and `_run_records/` files naming the scope route | Historical derived records; not rewritten | — |

## 11. Residuals (recorded, not proposed)

- `electron/renderer-window-policy.ts` L13-14 still names the "open legacy
  interface" link; corrected the next time the file changes under D-APP-121.
- The `/pipeline` dispatch query keys (`category`, `taskScopeMode`,
  `scopeKey`, `targetDeliverableKey`) keep no live consumer; they stay
  round-trippable under SPEC §17.9 (P-keep).
- DEL-02-03's summary/status widget stays unimplemented (TM-APP-051).
- The 49 other product modules without a product importer (Impact Assessment
  §10.3) are not legacy loop-first UI and are not proposed.

## 12. Revision 2: independent review of `4c572475f`

The review found no blocking issue. Its nine corrections are applied:

| # | Correction | Where |
|---|---|---|
| N1 | DEL-08-02-REQ-004 verification (E14) names the negative-alias test in `persona-resolution.test.ts`, which covered only TASK, ORCHESTRATE, RESEARCH and CHANGE. The code specification now adds a case for `RECONCILING` and the TYPES §4 matrix labels; E14 is unchanged | §4 |
| N2 | `workspace-sidebar.test.ts` would become an empty suite. It is replaced by one default-tabs case for what `AppShell` renders | §4 |
| N3 | The `'portal' \| 'workbench' \| 'pipeline'` members of `SidebarTabId` are removed; the sidebar tab is not persisted. Tolerant parsing applies to the persisted `WovenWorkspaceSurface`, which is unchanged | §4 |
| N4 | `PORTAL_ROUTE` and `CHAT_ROUTE` are removed, and case 1 of `loop-first.test.ts` is trimmed to `CHAT_SECTION` | §4 |
| N5 | `--candidate` now refuses any root inside a git work tree without the group-2 pointer, not only this checkout; `check_candidate_mode.py` tests it | §3, §6, §9; `Evidence/Group2/build_amendment_preview.py`, `check_candidate_mode.py` |
| N6 | The group-1 snapshot cites commits that are no longer ancestors after the rebase. The snapshot is immutable (method.md), so `Decision_Log.md` G1-NOTE-1 records the current commit; the manifest's content hashes are unchanged | `Decision_Log.md` |
| N7 | The rebase onto `974bf7da4` (PEC files only) is noted here and in `Decision_Log.md` G1-NOTE-1 | front matter, §1, §9 |
| N8 | The dependency-closure surface is `_Evaluation/DepClosure` | §10 |
| N9 | E05 now says which DEL-02-03 verification rows change (REQ-009, REQ-010, REQ-013) instead of "the verification hooks are unchanged" | `Amendment_Preview.md` E05 |

Only E05 changes in the exact text; the edit count, files, register and supersession delta are unchanged.

## Evidence basis for this package

| Artifact | SHA-256 |
|---|---|
| `Amendment_Actions.csv` | `a9ff78f2be8356b7727d7bb853bd758a55cb6a976b42dc2fc8dc1d1365e114ad` |
| `Supersession_Delta.csv` | `f6239eaef9777bd13af88cfb32ac69cc6ff04ef09d7bcda10bb126f2525de899` |
| `Amendment_Preview.md` | `bb6c0b44ec91e00cd8afced23081a3e9eea27cd9be374946736583feaa281ce9` |
| `Evidence/Group2/amendment_edits.py` | `a7595b05a4bbf74460a0929e72d4bc0a893dae67dec6e5503481ce457559687a` |
| `Evidence/Group2/build_amendment_preview.py` | `0d5995343332d0169b062d91217f51b9cdf98fa45ad4769876465cca1c9ece85` |
| `Evidence/Group2/validate_postimage.py` | `f6a2de1cc57e785c44b5a73abeb42699715c4b278c14a15003bfdfd50ffba76b` |
| `Evidence/Group2/check_candidate_mode.py` | `74fe97782378e10863aaaf33f3dad61391585e859efe46b4665cd249c3a99291` |
| `Evidence/Group2/PREIMAGE_POSTIMAGE.csv` | `76d26f6725c8010c5918d65e1330d979c96bfab3abfebb4f5b3f315485fcc70c` |
| `Evidence/Group2/POSTIMAGE_VALIDATION.md` | `8ac9784a2a08129c3e1e89e47a36fd8b2731b688a09c21e96f4131276fa9ab26` |
