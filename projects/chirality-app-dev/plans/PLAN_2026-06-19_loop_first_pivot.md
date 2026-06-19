# Loop-First Pivot (D-APP-28) Plan

**Date:** 2026-06-19
**Status:** PROPOSAL (awaiting owner review)
**Governing ruling:** `execution/_Coordination/_DECISIONS/D-APP-28_RULING_2026-06-19.md` (Option B — full loop-first pivot)
**Packet:** `execution/_Coordination/_DECISIONS/D-APP-28_PACKET_2026-06-19.md`
**Active design:** `plans/DESIGN_2026-06-18_agent_orchestration_ui.md` (§3.1 primary loop, §3.2 sidebar, §3.3 tertiary screens, §5 build sequence; the D-APP-28 ruling/packet name the §5 "Transitional placement decision" bullet — DESIGN line 111 — as "§5.2", the transitional sidebar-left note)
**Working root:** `projects/chirality-app-dev/` (source under `frontend/`)
**Supersedes (as end-state):** D-APP-23 Option C hybrid

## 1. Purpose

D-APP-28 RULED Option B: the live loop becomes the primary surface app-wide, the route surfaces (portal `/`, `/workbench`, `/pipeline`, file tree) are demoted to sidebar-reachable tertiary forms, the multi-view sidebar moves to the right across the app, and matrix-cell launches boot a session in-place rather than `router.push`-ing to a route-as-main. This plan decomposes that pivot into bounded, individually reviewable tranches (`28a`…`28e`), each independently `npm run typecheck` + test-green with `next build` prerendering the affected routes, sequenced so the three working routes never break mid-flight. It is a routing/layout change only: the public UIEvent contract and permission plane stay untouched, in-flight turns survive every relayout, and no route or tertiary screen is deleted.

## 2. Current Substrate (verified live)

The shipped D-APP-23 Option C hybrid this pivot reworks (all paths under `frontend/`):

- **Two divergent shells.** `frontend/src/components/shell/app-shell.tsx` is a 5-column resizable grid (`shell-grid shell-grid--resizable`, :307): sidebar-LEFT (`fileTree` pane, ~:311-331) → handle (`renderResizeHandle('fileTree')`, :333) → main `children` (`panel--main`, ~:335-340) → handle (`renderResizeHandle('chat')`, :342) → chat-RIGHT (`shell-pane--chat`, ~:343-371). `frontend/src/components/shell/loop-shell.tsx` is a fixed 2-column grid (`loop-grid` class toggled at :32): loop-MAIN left (`loop-main`, :35) + sidebar-RIGHT (`shell-pane--sidebar loop-sidebar`, :57-78), persona picker in a `loop-persona-bar` (:36-37), no resize handles.
- **Shared chrome already extracted.** `frontend/src/components/shell/shell-frame.tsx` owns the header/nav/Working-Root bar/API-key settings and is wrapped by both shells. `NAVIGATION_ITEMS` (:19-22) lists `/`, `/pipeline`, `/workbench`; `/chat` is intentionally absent (comment :16-18).
- **Geometry state is AppShell-only.** `frontend/src/lib/shell/layout-state.ts` owns `ResizablePaneKey` (`fileTree`|`toolkit`|`chat`, :1), width/collapse persistence (`LAYOUT_STORAGE_KEY = 'chirality.layout.v1'`, :8), and clamping. `LoopShell` reuses none of it — it has local `sidebarTab`/`sidebarCollapsed` state only (loop-shell.tsx:21-22). `TOOLKIT_PANE_VISIBLE = false` (app-shell.tsx:56); the `toolkit` entries persist only to satisfy the frozen `Record<ResizablePaneKey,…>` type.
- **Drag direction is left/right-baked.** `DRAG_DIRECTION` (app-shell.tsx:48-52) is `fileTree: 1, chat: -1`; the delta is applied at app-shell.tsx:183 (`(event.clientX - dragState.startX) * DRAG_DIRECTION[dragState.pane]`). CSS grid order is in `frontend/src/app/globals.css` `.shell-grid` (sidebar-left, the `minmax(56px, var(--pane-file-tree-width))` first column) vs `.loop-grid` (sidebar-right, `minmax(0,1fr) minmax(56px,360px)`).
- **In-flight-turn survival mechanism.** `ChatPanel` (`frontend/src/components/shell/chat-panel.tsx`) holds streaming/message state in component state; both shells Suspense-wrap it (app-shell.tsx ~:355-368; loop-shell.tsx :40-53) and only hide chrome on collapse (CSS `.shell-pane--collapsed …{display:none}`, globals.css). The instance is never unmounted, so a turn survives relayout. This is load-bearing for the pivot.
- **Routes today.** `frontend/src/app/page.tsx` → `AppShell` + `AgentMatrix`; `frontend/src/app/workbench/page.tsx` → `WorkbenchClient` (Suspense); `frontend/src/app/pipeline/page.tsx` → `PipelineClient` (Suspense); `frontend/src/app/chat/page.tsx` → `LoopShell` (Suspense).
- **Matrix navigation = route-as-main.** `frontend/src/components/portal/agent-matrix.tsx` schedules navigation via `createNavigationIntentScheduler` (wired `router.push(target)` :13-21) — cells call `navigationScheduler.schedule(cell.target)` (:66). Targets are static in `frontend/src/lib/portal/agent-matrix-cells.ts`: NORMATIVE/EVALUATIVE → `/workbench?agent=…` (Type-0/Type-1); OPERATIVE → `/pipeline?category=…` (Type-2). Deliverable rows schedule `/pipeline?category=TASK&…&scopeKey=…` (agent-matrix.tsx:104).
- **Route-free in-place boot already exists.** `ChatPanel` resolves persona from `?agent=` and mode from pathname, and boots the session on first message via `createHarnessSession`/`bootHarnessSession` (POST `/api/harness/session/create`, D-APP-24 `assertDirectChatPersona` guard at agent-roster.ts:98). `buildDirectChatHref(persona)` (`frontend/src/lib/shell/loop-first.ts:19-24`) is the route-free href builder; `CHAT_ROUTE`/`CHAT_SECTION` at :11-12.
- **Test/build baseline.** `frontend/package.json`: `test` = `vitest run` (:14), `typecheck` = `tsc --noEmit --incremental false && tsc -p tsconfig.electron.json --noEmit --incremental false` (:15, next + electron). `frontend/next.config.mjs` is minimal (`reactStrictMode: true`), no prerender directives. DESIGN §5 records Tranche 5b at **477 tests** (line 122); the current suite baseline is **491** (Tranche 5c, DESIGN line 122; explorer test-surface map). **No test encodes DOM grid-column order, sidebar placement, or drag direction** — `frontend/src/__tests__/lib/layout-state.test.ts` is pure clamping/collapse math (placement-independent), `agent-matrix-cells.test.ts` asserts route targets + the Type-0/1 roster guard, `loop-first.test.ts` asserts href building, `navigation-intent.test.ts` asserts turn-boundary coalescing.

## 3. Gaps the Pivot Closes

| # | DESIGN §3.1 target IA | Today (hybrid) | Tranche |
|---:|---|---|---|
| G1 | Live loop primary on every surface | Loop primary only on `/chat`; `/`, `/workbench`, `/pipeline` keep `children` as main and the loop as a side panel | 28a, 28c, 28d |
| G2 | Sidebar on the RIGHT app-wide (the DESIGN line-111 "Transitional placement decision" — named §5.2 by the D-APP-28 ruling/packet — recorded sidebar-left as transitional) | Sidebar-right only in `LoopShell`; `AppShell` is sidebar-left (DESIGN line 111; app-shell.tsx ~:311-331) | 28a, 28b |
| G3 | Matrix-cell launch boots a session in-place | `AgentMatrix` schedules `router.push` to a route-as-main (agent-matrix.tsx:66; matrix-cells.ts targets) | 28c |
| G4 | Route screens are tertiary forms reached via the sidebar | `/workbench`/`/pipeline` are primary routes with their own `AppShell` | 28d |
| G5 | One sidebar-right relayout primitive, not two divergent shells | `AppShell` (resizable, sidebar-left) and `LoopShell` (fixed, sidebar-right) diverge | 28a |
| G6 | DESIGN §5 / the line-111 "§5.2" transitional note reflect loop-as-primary end-state | The line-111 note still names sidebar-left "transitional" pending exactly this decision | 28e |

## 4. Tranche Spine

| Tranche | Purpose | Primary scope | Minimum validation |
|---|---|---|---|
| `28a` | Make the sidebar-right loop layout a reusable primitive | Generalize the `loop-grid` sidebar-right structure (shared with `WorkspaceSidebar`/`ChatPanel`) so route surfaces can adopt it without forking `LoopShell`; no route behavior change yet | `npm run typecheck`; `npx vitest run` (491 green, no test edits); `next build` prerenders `/`, `/chat`, `/workbench`, `/pipeline` |
| `28b` | Flip the sidebar to the RIGHT app-wide + update geometry tests in the SAME tranche | Re-order `AppShell` grid (CSS `.shell-grid` + JSX children) to sidebar-right; invert `DRAG_DIRECTION`; fix collapsed-label/handle CSS; update/extend layout-geometry tests in the same commit | `npm run typecheck`; `npx vitest run` (geometry tests updated, suite green); `next build` prerenders affected routes |
| `28c` | Portal `/` becomes a loop-first home with in-place matrix launch | `page.tsx` renders the loop-first shell; `AgentMatrix` Type-0/Type-1 cells boot in-place via `buildDirectChatHref` (no `router.push`-to-route-as-main); OPERATIVE cells gated on a sub-decision (§8) | `npm run typecheck`; `npx vitest run` (matrix/route tests updated, suite green); `next build` prerenders `/` |
| `28d` | Demote `/workbench` + `/pipeline` to sidebar-reachable tertiary forms (kept, not deleted) | `WorkbenchClient`/`PipelineClient` reachable as tertiary forms from the sidebar; routes remain and still render; nav reflects tertiary status | `npm run typecheck`; `npx vitest run` (suite green); `next build` prerenders `/`, `/workbench`, `/pipeline`, `/chat` |
| `28e` | Closeout | DESIGN §5 + line-111 "§5.2" note update (loop-primary end-state; close the transitional sidebar-left note), resume prompt, `_REGISTER.md` annotation, plan completion record | Governance gate; runtime commands re-run if any source changed in this tranche |

Each tranche is independently typecheck- and test-green and leaves all three working routes operational.

## 5. Tranche Detail

### 28a — Reusable sidebar-right loop primitive

- **Scope.** Extract the sidebar-right relayout structure currently hard-coded in `loop-shell.tsx` (:32-78: `loop-grid` + `loop-main` left + `shell-pane--sidebar loop-sidebar` right + collapse toggle) into a primitive that route surfaces can adopt. `LoopShell` and (later) the portal both consume it; `WorkspaceSidebar` and the Suspense-wrapped `ChatPanel` are passed through unchanged.
- **What changes.** A single sidebar-right layout component/structure plus its `.loop-grid`-family CSS becomes the shared substrate; `LoopShell` is rewired to consume it with identical visible behavior. No route page changes; `AppShell` is untouched in this tranche.
- **What stays.** `AppShell` (sidebar-left) and all three routes render exactly as today. `layout-state.ts` is untouched (still AppShell-only). `ShellFrame` chrome unchanged.
- **In-flight-turn survival.** The extracted primitive must preserve the collapse-without-unmount property: `ChatPanel` stays mounted (Suspense-wrapped, loop-shell.tsx:40-53) and the sidebar collapses by toggling the grid template only (current loop-shell.tsx:32 / globals.css `.loop-grid--sidebar-collapsed`). No change to `ChatPanel` state ownership.
- **Contract/permission untouched.** Pure layout extraction — no `/api/harness/*` call, no UIEvent emission, no permission-plane code is touched.
- **Nothing deleted.** `LoopShell` keeps its public shape; no route or screen removed.
- **Acceptance:** `npm run typecheck` clean; `npx vitest run` green with **zero test edits** (no test encodes this structure); `next build` prerenders `/`, `/chat`, `/workbench`, `/pipeline`; `/chat` is visually identical to pre-tranche.

### 28b — Sidebar-right app-wide + geometry tests (same tranche)

- **Scope.** Flip `AppShell` from sidebar-left to sidebar-right: re-order `grid-template-columns` in `globals.css` `.shell-grid` (currently `minmax(56px,var(--pane-file-tree-width)) | handle | 1fr | handle | minmax(56px,var(--pane-chat-width))`) and the JSX grid children in app-shell.tsx (~:311-371) so the workspace sidebar is the right-most pane. Invert `DRAG_DIRECTION` (app-shell.tsx:48-52) for the moved panes and verify the delta sign at app-shell.tsx:183. Adjust the collapsed-label/handle CSS (`.shell-pane-collapsed-label`, the `.shell-pane--collapsed` toggle rules) for the right-edge placement.
- **Tests in the same commit.** No existing test breaks on the flip (the suite encodes no DOM order), but this tranche **adds** layout-geometry/route assertions so the right-placement is regression-guarded going forward, extending `frontend/src/__tests__/lib/layout-state.test.ts` (clamping is placement-independent and stays green; new assertions cover the pane ordering/drag-direction invariant the flip introduces). Bundling code + test in one commit satisfies the binding "each tranche independently typecheck + layout-geometry/route tests green."
- **What stays.** `layout-state.ts` math, `chirality.layout.v1` persistence, `TOOLKIT_PANE_VISIBLE = false`, and the two-pane clamp model all stay; only column order + drag sign change. Resizability is preserved.
- **In-flight-turn survival.** Chat stays mounted across the relayout — `ChatPanel` is not remounted by a CSS grid re-order; collapse semantics are unchanged.
- **Contract/permission untouched.** No engine/API/permission file touched.
- **Nothing deleted.** All panes and routes remain; sidebar merely moves right.
- **Acceptance:** `npm run typecheck` clean; `npx vitest run` green with the new geometry assertions; `next build` prerenders affected routes; manual visual/interaction check of grid order, drag direction, and collapsed-label centering (the maps flag these are not test-covered).

### 28c — Portal `/` loop-first home + in-place matrix launch

- **Scope.** Convert `frontend/src/app/page.tsx` so the portal is loop-first: the live loop is primary with the right sidebar (consuming the 28a primitive); `AgentMatrix` becomes a sidebar-reachable surface rather than the main `children`. Rewire `agent-matrix.tsx` so Type-0/Type-1 cells boot the session in-place: replace the `navigationScheduler.schedule(cell.target)` `router.push` path (:66) with the route-free path — set `?agent=` via `buildDirectChatHref(rawAgent)` and let `ChatPanel`'s existing route-free `resolvePersona` boot on next message (the picker/`ChatPanel` flow already supports this). The static targets in `agent-matrix-cells.ts` and the Type-0/1 roster guard (`agent-matrix-cells.test.ts`) are updated/retargeted in the same tranche so the mechanical guard still holds.
- **OPERATIVE cells (sub-decision, §8).** OPERATIVE cells route to `/pipeline?category=…` (Type-2 task work) and have no direct-chat parallel — Type-2 cannot boot at `/chat` (D-APP-24 server guard). Their in-place behavior (open the pipeline tertiary form in-place vs. retain a route hop) is a NEW UX sub-decision and is **flagged for its own packet (§8)**; this tranche does not assume it. Until ruled, OPERATIVE/deliverable cells keep their current `navigationScheduler.schedule` to the still-present `/pipeline` route (nothing deleted, route still works).
- **What stays.** `/workbench` and `/pipeline` routes still exist and render (demotion is 28d). `createNavigationIntentScheduler` turn-boundary coalescing (navigation-intent.test.ts) is preserved for any retained navigation.
- **In-flight-turn survival.** In-place launch reuses the mounted `ChatPanel` (session boots on first message, route-free) — no remount, so a prior in-flight turn is not interrupted by a cell click that only swaps `?agent=`.
- **Contract/permission untouched.** Session boot continues through the unchanged `/api/harness/session/create` with its `assertDirectChatPersona` D-APP-24 guard; no UIEvent or permission change.
- **Nothing deleted.** Matrix, deliverable rows, and all routes remain reachable.
- **Acceptance:** `npm run typecheck` clean; `npx vitest run` green with `agent-matrix-cells.test.ts` retargeted (Type-0/1 roster guard still asserts) and `loop-first`/`navigation-intent` tests green; `next build` prerenders `/`.

### 28d — Demote `/workbench` + `/pipeline` to sidebar-reachable tertiary forms

- **Scope.** Make `WorkbenchClient` (`frontend/src/app/workbench/workbench-client.tsx`) and `PipelineClient` (`frontend/src/app/pipeline/pipeline-client.tsx`) reachable as tertiary forms from the right sidebar across the app, per DESIGN §3.3 "tertiary screens." The `/workbench` and `/pipeline` routes are **kept** as thin entry points that render the same clients; `ShellFrame` `NAVIGATION_ITEMS` (shell-frame.tsx:19-22) is updated to reflect their tertiary status (reachable, not primary). The exact sidebar affordance (new tab vs. menu entry vs. overlay) is bounded by the §8 sub-decision if it changes `SidebarTabId` (`workspace-sidebar.tsx:11-18`).
- **What stays.** Both routes still resolve and render their clients (backward-compatible deep links, e.g. `/pipeline?category=TASK&scopeKey=…` from deliverable rows). `WorkbenchClient`/`PipelineClient` internals (contracts, DECOMP/PREP/TASK/AUDIT cards, scope selectors) are unchanged.
- **In-flight-turn survival.** Opening a tertiary form must not unmount the loop's `ChatPanel`; the form renders in the sidebar/tertiary region while the loop stays mounted (same primitive as 28a). If a tertiary form is reached by route navigation, that path is unchanged from today.
- **Contract/permission untouched.** No engine/API/permission change; only routing/IA and nav labels move.
- **Nothing deleted.** This is the binding "nothing is deleted" tranche: `/workbench`, `/pipeline`, the file tree, and the portal matrix all remain reachable via the sidebar.
- **Acceptance:** `npm run typecheck` clean; `npx vitest run` green; `next build` prerenders `/`, `/workbench`, `/pipeline`, `/chat`; every tertiary screen demonstrably reachable from the sidebar.

### 28e — Closeout

- **Scope.** Update DESIGN §5 and its line-111 "Transitional placement decision" bullet (named "§5.2" by the D-APP-28 ruling/packet) to record the loop-as-primary app-wide end-state and **close the transitional sidebar-left note** — sidebar is now right app-wide. Annotate `execution/_Coordination/_DECISIONS/_REGISTER.md` D-APP-28 row with the landed-tranche summary, write the resume/next-instance prompt, and add a plan completion record. No source change expected; if any is made, re-run the runtime gates.
- **What stays / nothing deleted / contract untouched.** Documentation-and-coordination only; no code, no route, no contract, no permission change.
- **Acceptance:** governance gate (diff hygiene, path checks); the line-111 transitional note closed; register + resume updated.

## 6. Sequencing

`28a → 28b → 28c → 28d → 28e`.

- `28a` **de-risks the rest**: extracting the sidebar-right primitive first means `28b` (AppShell flip) and `28c` (portal) consume a proven structure rather than each forking layout.
- `28b` must land before `28c`/`28d` so the app is already sidebar-right when route surfaces become loop-first.
- `28c ∥ 28d` are *logically* parallelizable (portal vs. workbench/pipeline are independent surfaces), but to keep review bounded and the IA coherent they land sequentially `28c → 28d`; either may be split further if a single diff grows too large to review.
- `28e` is strictly last (records the realized end-state).

## 7. Boundaries — Explicit Out of Scope (human-gated)

Restating D-APP-28's out-of-scope (ruling final paragraph): this plan does **not** approve deleting any route or tertiary screen (portal/workbench/pipeline/file tree all stay reachable), nor any engine / public-contract / permission-plane change. The public UIEvent type and the permission/hook/path/redaction plane are untouched — this is routing/layout only.

Deferrals **not reopened** by this plan: **D-APP-26** (editable document screen / content-WRITE — RULED Option C defer), **D-APP-27** (Type-2 task agents remain excluded from direct chat — RULED Option C; `assertDirectChatPersona` stands), **D-APP-29** (SECONDARY task-management/Workflow phase — RULED Option A defer). The Workflow sidebar view stays a thin peek (`workspace-sidebar.tsx:152-155`); no Type-2 direct-entry brief is introduced.

## 8. Required Human Rulings

D-APP-28 is **already RULED** (Option B, `D-APP-28_RULING_2026-06-19.md`) — this plan does not re-litigate it. Tranches surface the following NEW sub-decisions, each **flagged for its own packet; approval is not assumed**:

- **SD-1 — Exact in-place launch UX (28c).** The ruling mandates "boot a session in-place" but not the interaction (cell click swaps `?agent=` on the mounted loop; whether a prior in-flight turn is preserved-and-queued vs. confirmed-before-switch; what visual transition signals the boot). Needs a packet before 28c finalizes the UX.
- **SD-2 — OPERATIVE/Type-2 pipeline cells (28c).** OPERATIVE cells (and deliverable rows) target `/pipeline` Type-2 work that cannot boot at `/chat` (D-APP-24 guard). Whether they (a) keep a route hop to the retained `/pipeline`, (b) open the pipeline tertiary form in-place, or (c) require a brief, intersects the excluded D-APP-27 INIT-TASK question and needs its own packet. Until ruled, 28c leaves OPERATIVE cells on their current `navigationScheduler.schedule` (route still present, nothing deleted).
- **SD-3 — Tertiary-form affordance + sidebar tab surface (28d).** Whether demoted `/workbench`/`/pipeline` get new `SidebarTabId` entries (`workspace-sidebar.tsx:11-18`), a menu, or an overlay — an IA detail that changes the sidebar's public tab set. If it expands `SidebarTabId`, packet it before 28d.

## 9. Validation Policy

Per-tranche gates (binding):

- `npm run typecheck` — `tsc --noEmit` for both the Next and electron configs (`frontend/package.json` `typecheck`, :15); must be clean.
- `npx vitest run` — full suite green against the **491-test baseline** (DESIGN §5 records 477 at Tranche 5b line 122; the current baseline at Tranche 5c is 491). `28b` updates/extends layout-geometry tests **in the same commit**; `28c` retargets `agent-matrix-cells.test.ts` while preserving its Type-0/Type-1 roster guard; `loop-first.test.ts` and `navigation-intent.test.ts` stay green. New layout-geometry/route assertions are expected in `28b`/`28c`.
- `next build` — must prerender the affected routes (`/`, `/chat`, `/workbench`, `/pipeline`). `frontend/next.config.mjs` needs no prerender-directive change (the pivot is grid/routing, not a render-mode change).
- Manual visual/interaction check is required where no test covers DOM structure: grid column order, resize-handle drag direction, and collapsed-label placement after the `28b` flip.

## 10. Acceptance Criteria

End-state checks (all must hold at 28e):

1. The multi-view sidebar is on the **RIGHT** on every surface (`/`, `/chat`, `/workbench`, `/pipeline`); the DESIGN line-111 transitional sidebar-left note (named "§5.2" by the D-APP-28 ruling/packet) is closed.
2. The live loop is the **primary** surface on every route, not a side panel.
3. Matrix Type-0/Type-1 launches **boot a session in-place** (route-free `?agent=` on the mounted loop), not `router.push` to a route-as-main; OPERATIVE-cell behavior is whatever SD-2 rules.
4. Every tertiary screen — portal matrix, `/workbench`, `/pipeline`, file tree — is **reachable via the sidebar**; the routes still resolve and render.
5. **Nothing is deleted.**
6. The public **UIEvent contract and permission plane are unchanged** (no diff under the engine/permission paths).
7. **In-flight turns survive** every relayout (`ChatPanel` never unmounted across sidebar flip, in-place launch, or tertiary-form open).
8. `npm run typecheck` + `npx vitest run` (491 baseline) green and `next build` prerenders the affected routes at each landed tranche.

## 11. Evidence Basis

- Shells: `frontend/src/components/shell/app-shell.tsx` (5-col grid `:307`, `DRAG_DIRECTION` :48-52, delta apply :183, grid children ~:311-371, `TOOLKIT_PANE_VISIBLE` :56), `frontend/src/components/shell/loop-shell.tsx` (`loop-grid` class :32, sidebar-right :57-78, Suspense-wrapped ChatPanel :40-53), `frontend/src/components/shell/shell-frame.tsx` (`NAVIGATION_ITEMS` :19-22, `/chat`-absent note :16-18), `frontend/src/components/shell/workspace-sidebar.tsx` (`SidebarTabId` :11-18, Workflow peek :152-155), `frontend/src/components/shell/chat-panel.tsx` (route-free boot + in-flight state).
- Geometry/CSS: `frontend/src/lib/shell/layout-state.ts` (`ResizablePaneKey` :1, `LAYOUT_STORAGE_KEY` :8); `frontend/src/app/globals.css` (`.shell-grid`, `.loop-grid`, `.shell-pane--collapsed`, `.shell-pane-collapsed-label`).
- Routing/matrix: `frontend/src/app/page.tsx`, `frontend/src/app/workbench/page.tsx` + `workbench-client.tsx`, `frontend/src/app/pipeline/page.tsx` + `pipeline-client.tsx`, `frontend/src/app/chat/page.tsx`; `frontend/src/components/portal/agent-matrix.tsx` (scheduler+`router.push` :13-21, `schedule(cell.target)` :66, deliverable rows :104); `frontend/src/lib/portal/agent-matrix-cells.ts`; `frontend/src/lib/shell/loop-first.ts` (`buildDirectChatHref` :19-24, `CHAT_ROUTE`/`CHAT_SECTION` :11-12).
- Session boot/guard: `frontend/src/app/api/harness/session/create/route.ts`; `assertDirectChatPersona` (`frontend/src/lib/harness/agent-roster.ts:98`, D-APP-24).
- Tests/build: `frontend/src/__tests__/lib/layout-state.test.ts` (pure clamping/collapse), `agent-matrix-cells.test.ts` (route + Type-0/1 roster guard), `loop-first.test.ts`, `navigation-intent.test.ts`; `frontend/package.json` (:14-15); `frontend/next.config.mjs`.
- Decision substrate: `execution/_Coordination/_DECISIONS/D-APP-28_PACKET_2026-06-19.md`, `execution/_Coordination/_DECISIONS/D-APP-28_RULING_2026-06-19.md`, `execution/_Coordination/_DECISIONS/_REGISTER.md` (D-APP-28 row: RULED Option B); D-APP-23/24 rows; D-APP-26 (Option C defer), D-APP-27 (Option C exclude), D-APP-29 (Option A defer) rulings.
- Design: `plans/DESIGN_2026-06-18_agent_orchestration_ui.md` §3.1 (line 52), §3.2 (line 58), §3.3 (line 70), §5 (line 106); the "Transitional placement decision" bullet at line 111 (the transitional sidebar-left note the D-APP-28 ruling/packet call "§5.2"); Tranche 5b 477-test record and Tranche 5c 491-test record at line 122.

## 12. Finalization Rule

The plan is complete when `28a`–`28d` have landed, each typecheck- + vitest-green (491 baseline) with `next build` prerendering the affected routes, and the §10 acceptance checks all hold. Closeout is recorded in `28e`: update DESIGN §5 and the line-111 "Transitional placement decision" bullet (named "§5.2" by the D-APP-28 ruling/packet) to declare the loop-primary, sidebar-right app-wide end-state and close the transitional sidebar-left note; annotate the D-APP-28 row in `execution/_Coordination/_DECISIONS/_REGISTER.md` with the landed-tranche summary; write the resume / next-instance prompt; and add a plan completion record. Any sub-decision (SD-1/SD-2/SD-3) that arises is packeted under `execution/_Coordination/_DECISIONS/` and ruled before the dependent tranche finalizes — they are not assumed approved by D-APP-28.
