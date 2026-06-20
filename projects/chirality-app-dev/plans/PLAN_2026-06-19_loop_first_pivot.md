# Loop-First Pivot (D-APP-28) Plan

**Date:** 2026-06-19
**Status:** COMPLETE (28a, 28b, 28c, 28d, and 28e landed; SD-1/2/3 ruled — D-APP-30/31/32)
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
- **Shared chrome already extracted.** `frontend/src/components/shell/shell-frame.tsx` owns the header/nav/Working-Root bar/API-key settings and is wrapped by loop-first shells. After 28d, `NAVIGATION_ITEMS` exposes only `/` as primary navigation; `/workbench` and `/pipeline` remain route entry points but are tertiary sidebar forms.
- **Geometry state is AppShell-only.** `frontend/src/lib/shell/layout-state.ts` owns `ResizablePaneKey` (`fileTree`|`toolkit`|`chat`, :1), width/collapse persistence (`LAYOUT_STORAGE_KEY = 'chirality.layout.v1'`, :8), and clamping. `LoopShell` reuses none of it — it has local `sidebarTab`/`sidebarCollapsed` state only (loop-shell.tsx:21-22). `TOOLKIT_PANE_VISIBLE = false` (app-shell.tsx:56); the `toolkit` entries persist only to satisfy the frozen `Record<ResizablePaneKey,…>` type.
- **Drag direction is left/right-baked.** `DRAG_DIRECTION` (app-shell.tsx:48-52) is `fileTree: 1, chat: -1`; the delta is applied at app-shell.tsx:183 (`(event.clientX - dragState.startX) * DRAG_DIRECTION[dragState.pane]`). CSS grid order is in `frontend/src/app/globals.css` `.shell-grid` (sidebar-left, the `minmax(56px, var(--pane-file-tree-width))` first column) vs `.loop-grid` (sidebar-right, `minmax(0,1fr) minmax(56px,360px)`).
- **In-flight-turn survival mechanism.** `ChatPanel` (`frontend/src/components/shell/chat-panel.tsx`) holds streaming/message state in component state; both shells Suspense-wrap it (app-shell.tsx ~:355-368; loop-shell.tsx :40-53) and only hide chrome on collapse (CSS `.shell-pane--collapsed …{display:none}`, globals.css). The instance is never unmounted, so a turn survives relayout. This is load-bearing for the pivot.
- **Routes today.** `frontend/src/app/page.tsx` → `PortalLoopShell`; `frontend/src/app/workbench/page.tsx` → thin `WorkbenchClient` entry route that opens `WorkbenchSurface` in the right sidebar beside the live loop; `frontend/src/app/pipeline/page.tsx` → thin `PipelineClient` entry route that opens `PipelineSurface` in the right sidebar beside the live loop; `frontend/src/app/chat/page.tsx` → `LoopShell` (Suspense).
- **Matrix navigation after 28d.** `frontend/src/components/portal/agent-matrix.tsx` renders in the right sidebar Portal tab on `/` and every loop shell. NORMATIVE/EVALUATIVE cells swap `?agent=` on the mounted loop and focus the live prompt when idle; D-APP-30's mid-turn guard reuses `useHarnessStreaming`. OPERATIVE cells and deliverable rows now open the Pipeline tab in-place and fold Pipeline intent into the current URL query.
- **Route-free in-place boot exists on `/` and `/chat`.** `ChatPanel` resolves persona from `?agent=` and mode from pathname, and boots the session on first message via `createHarnessSession`/`bootHarnessSession` (POST `/api/harness/session/create`, D-APP-24 `assertDirectChatPersona` guard at agent-roster.ts:98). `buildDirectChatHref(persona)` drives `/chat`; `buildPortalPersonaHref(persona)` drives `/` without leaving the mounted portal loop.
- **Test/build baseline.** `frontend/package.json`: `test` = `vitest run` (:14), `typecheck` = `tsc --noEmit --incremental false && tsc -p tsconfig.electron.json --noEmit --incremental false` (:15, next + electron). `frontend/next.config.mjs` is minimal (`reactStrictMode: true`), no prerender directives. DESIGN §5 records Tranche 5b at **477 tests** (line 122); Tranche 5c established the pre-pivot **491-test** baseline. Tranche 28b raised the suite baseline to **492 tests**; Tranche 28c raised it to **496 tests**; Tranche 28d raised it to **499 tests** with tertiary-sidebar and in-place launch merge coverage.

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
| `28a` | **LANDED 2026-06-19.** Make the sidebar-right loop layout a reusable primitive | Added `SidebarRightLoopLayout` and rewired `LoopShell` to consume it; no route behavior change, no test edits, `AppShell` untouched | Passed `npm run typecheck`; `npx vitest run` (491 green); `npm run build` prerendered `/`, `/chat`, `/workbench`, `/pipeline`; browser `/chat` collapse check passed |
| `28b` | **LANDED 2026-06-19.** Flip the sidebar to the RIGHT app-wide + update geometry tests in the SAME tranche | Re-ordered `AppShell` grid (CSS `.shell-grid` + JSX children) to sidebar-right; moved drag-direction/grid-order constants into `layout-state.ts`; added stable `data-shell-slot` markers and layout-geometry assertions | Passed `npm run typecheck`; `npx vitest run` (492 green); `npm run build` prerendered `/`, `/chat`, `/workbench`, `/pipeline`; browser `/`, `/workbench`, `/pipeline` geometry/collapse/drag checks passed |
| `28c` | **LANDED 2026-06-19.** Portal `/` becomes a loop-first home with in-place matrix launch | `page.tsx` renders `PortalLoopShell`; `AgentMatrix` Type-0/Type-1 cells swap `?agent=` on the mounted loop and focus the prompt when idle; OPERATIVE cells/deliverables retain the staged `/pipeline` route hop until 28d | Passed `npm run typecheck`; `npx vitest run` (496 green); `npm run build`; browser desktop/mobile portal checks plus Type-1 focus and OPERATIVE `/pipeline` route-hop checks passed; `npm run harness:validate:premerge`; `npm run desktop:pack` |
| `28d` | **LANDED 2026-06-20.** Demote `/workbench` + `/pipeline` to sidebar-reachable tertiary forms (kept, not deleted) | `WorkbenchClient`/`PipelineClient` reachable as tertiary forms from the sidebar; routes remain and still render; nav reflects tertiary status; OPERATIVE/deliverable matrix launches open Pipeline in-place | Passed `npm run typecheck`; focused tests (13); `npm test` (499); browser desktop/mobile route and sidebar checks; `npm run harness:validate:premerge`; `npm run build`; `npm run desktop:pack` |
| `28e` | **LANDED 2026-06-20.** Closeout | DESIGN §5 + line-111 "§5.2" note update (loop-primary end-state; close the transitional sidebar-left note), resume prompt, `_REGISTER.md` annotation, plan completion record | Governance-only diff hygiene; runtime commands not rerun because no source changed after validated 28d |

Each tranche is independently typecheck- and test-green and leaves all three working routes operational.

## 5. Tranche Detail

### 28a — Reusable sidebar-right loop primitive

**Status: LANDED 2026-06-19.** `frontend/src/components/shell/sidebar-right-loop-layout.tsx`
now owns the reusable sidebar-right grid and collapse/tab state; `LoopShell` passes its
existing persona picker and Suspense-wrapped `ChatPanel` through unchanged. `AppShell`,
route behavior, the public `UIEvent` contract, and the permission plane were not touched.
Validation: `npm run typecheck`; `npx vitest run` (491 tests); `npm run build`
(`next build` prerendered `/`, `/chat`, `/workbench`, `/pipeline`); browser `/chat`
geometry/collapse check verified the sidebar remains right-side and collapse changes only
the sidebar width while the chat panel remains mounted.

- **Scope.** Extract the sidebar-right relayout structure currently hard-coded in `loop-shell.tsx` (:32-78: `loop-grid` + `loop-main` left + `shell-pane--sidebar loop-sidebar` right + collapse toggle) into a primitive that route surfaces can adopt. `LoopShell` and (later) the portal both consume it; `WorkspaceSidebar` and the Suspense-wrapped `ChatPanel` are passed through unchanged.
- **What changes.** A single sidebar-right layout component/structure plus its `.loop-grid`-family CSS becomes the shared substrate; `LoopShell` is rewired to consume it with identical visible behavior. No route page changes; `AppShell` is untouched in this tranche.
- **What stays.** `AppShell` (sidebar-left) and all three routes render exactly as today. `layout-state.ts` is untouched (still AppShell-only). `ShellFrame` chrome unchanged.
- **In-flight-turn survival.** The extracted primitive must preserve the collapse-without-unmount property: `ChatPanel` stays mounted (Suspense-wrapped, loop-shell.tsx:40-53) and the sidebar collapses by toggling the grid template only (current loop-shell.tsx:32 / globals.css `.loop-grid--sidebar-collapsed`). No change to `ChatPanel` state ownership.
- **Contract/permission untouched.** Pure layout extraction — no `/api/harness/*` call, no UIEvent emission, no permission-plane code is touched.
- **Nothing deleted.** `LoopShell` keeps its public shape; no route or screen removed.
- **Acceptance:** `npm run typecheck` clean; `npx vitest run` green with **zero test edits** (no test encodes this structure); `next build` prerenders `/`, `/chat`, `/workbench`, `/pipeline`; `/chat` is visually identical to pre-tranche.

### 28b — Sidebar-right app-wide + geometry tests (same tranche)

**Status: LANDED 2026-06-19.** `AppShell` now renders main → chat handle →
chat → workspace handle → workspace sidebar, with the workspace sidebar right-most
on route surfaces. The shared grid template, rendered slot order, and drag-direction
signs live in `layout-state.ts`; `AppShell` consumes the grid template and marks
rendered panes/handles with `data-shell-slot` for browser-verifiable geometry. The
workspace resize sign is inverted for the right-edge placement. Validation:
`npm run typecheck`; `npx vitest run` (492 tests); `npm run build` (`next build`
prerendered `/`, `/chat`, `/workbench`, `/pipeline`); browser route checks verified
the slot order on `/`, `/workbench`, and `/pipeline`, workspace collapse to 56px
with centered label, and left-drag growth from 280px to 360px.

- **Scope.** Flip `AppShell` from sidebar-left to sidebar-right: re-order `grid-template-columns` in `globals.css` `.shell-grid` (currently `minmax(56px,var(--pane-file-tree-width)) | handle | 1fr | handle | minmax(56px,var(--pane-chat-width))`) and the JSX grid children in app-shell.tsx (~:311-371) so the workspace sidebar is the right-most pane. Invert `DRAG_DIRECTION` (app-shell.tsx:48-52) for the moved panes and verify the delta sign at app-shell.tsx:183. Adjust the collapsed-label/handle CSS (`.shell-pane-collapsed-label`, the `.shell-pane--collapsed` toggle rules) for the right-edge placement.
- **Tests in the same commit.** No existing test breaks on the flip (the suite encodes no DOM order), but this tranche **adds** layout-geometry/route assertions so the right-placement is regression-guarded going forward, extending `frontend/src/__tests__/lib/layout-state.test.ts` (clamping is placement-independent and stays green; new assertions cover the pane ordering/drag-direction invariant the flip introduces). Bundling code + test in one commit satisfies the binding "each tranche independently typecheck + layout-geometry/route tests green."
- **What stays.** `layout-state.ts` math, `chirality.layout.v1` persistence, `TOOLKIT_PANE_VISIBLE = false`, and the two-pane clamp model all stay; only column order + drag sign change. Resizability is preserved.
- **In-flight-turn survival.** Chat stays mounted across the relayout — `ChatPanel` is not remounted by a CSS grid re-order; collapse semantics are unchanged.
- **Contract/permission untouched.** No engine/API/permission file touched.
- **Nothing deleted.** All panes and routes remain; sidebar merely moves right.
- **Acceptance:** `npm run typecheck` clean; `npx vitest run` green with the new geometry assertions; `next build` prerenders affected routes; manual visual/interaction check of grid order, drag direction, and collapsed-label centering (the maps flag these are not test-covered).

### 28c — Portal `/` loop-first home + in-place matrix launch

**Status: LANDED 2026-06-19.** `/` now renders `PortalLoopShell`: the live
loop is the primary pane, the right sidebar opens on a Portal tab, and the
Agent Matrix is sidebar-reachable instead of the route-as-main body. Type-0 and
Type-1 matrix cells now update `?agent=` on `/` and reuse the mounted
`ChatPanel`; when the prompt is enabled, the launch focuses the prompt. The
mid-turn guard uses the existing shared streaming flag. OPERATIVE cells and
deliverable rows retain their interim `/pipeline` route hop, per D-APP-31's
28d staging. Validation: `npm run typecheck`; `npx vitest run` (496 tests);
`npm run build`; browser checks at desktop and 390px mobile; `npm run
harness:validate:premerge` (rerun passed Section 8 8/8 and Section 9 report-only
13/13 after an initial dev-server/build race); `npm run desktop:pack`.

- **Scope.** Convert `frontend/src/app/page.tsx` so the portal is loop-first: the live loop is primary with the right sidebar (consuming the 28a primitive); `AgentMatrix` becomes a sidebar-reachable surface rather than the main `children`. Rewire `agent-matrix.tsx` so Type-0/Type-1 cells boot the session in-place: replace the `navigationScheduler.schedule(cell.target)` `router.push` path (:66) with the route-free path — set `?agent=` on `/` via `buildPortalPersonaHref(rawAgent)` and let `ChatPanel`'s existing route-free `resolvePersona` boot on next message (the picker/`ChatPanel` flow already supports this). The static targets in `agent-matrix-cells.ts` and the Type-0/1 roster guard (`agent-matrix-cells.test.ts`) are updated/retargeted in the same tranche so the mechanical guard still holds.
- **OPERATIVE cells (sub-decision, §8).** OPERATIVE cells route to `/pipeline?category=…` (Type-2 task work) and have no direct-chat parallel — Type-2 cannot boot at `/chat` (D-APP-24 server guard). Their in-place behavior (open the pipeline tertiary form in-place vs. retain a route hop) is a NEW UX sub-decision and is **flagged for its own packet (§8)**; this tranche does not assume it. Until ruled, OPERATIVE/deliverable cells keep their current `navigationScheduler.schedule` to the still-present `/pipeline` route (nothing deleted, route still works).
- **What stays.** `/workbench` and `/pipeline` routes still exist and render (demotion is 28d). `createNavigationIntentScheduler` turn-boundary coalescing (navigation-intent.test.ts) is preserved for any retained navigation.
- **In-flight-turn survival.** In-place launch reuses the mounted `ChatPanel` (session boots on first message, route-free) — no remount, so a prior in-flight turn is not interrupted by a cell click that only swaps `?agent=`.
- **Contract/permission untouched.** Session boot continues through the unchanged `/api/harness/session/create` with its `assertDirectChatPersona` D-APP-24 guard; no UIEvent or permission change.
- **Nothing deleted.** Matrix, deliverable rows, and all routes remain reachable.
- **Acceptance:** `npm run typecheck` clean; `npx vitest run` green with `agent-matrix-cells.test.ts` retargeted (Type-0/1 roster guard still asserts) and `loop-first`/`navigation-intent` tests green; `next build` prerenders `/`.

### 28d — Demote `/workbench` + `/pipeline` to sidebar-reachable tertiary forms

**Status: LANDED 2026-06-20.** `WorkbenchSurface` and `PipelineSurface` now live
under `frontend/src/components/workbench/` and `frontend/src/components/pipeline/`.
`/workbench` and `/pipeline` remain thin route entry points, but both render the
live loop as primary and open the corresponding tertiary form in the right
sidebar through `LoopTertiaryShell`. `WorkspaceSidebar` has D-APP-32 tabs for
Portal, Workbench, and Pipeline when those surfaces are supplied, and `ShellFrame`
top navigation exposes only Portal as the primary route. D-APP-31 is implemented:
OPERATIVE matrix cells and deliverable rows open Pipeline in-place and merge the
Pipeline intent into the current URL query while keeping the live loop mounted.
Validation: `npm run typecheck`; focused tests (13); `npm test` (71 files,
499 tests); browser desktop/mobile checks for sidebar reachability, in-place
Pipeline launches, direct `/workbench` and `/pipeline` entry routes, and no
horizontal overflow; `npm run harness:validate:premerge` (Section 8 8/8,
Section 9 report-only 13/13); `npm run build`; `npm run desktop:pack`.

- **Scope.** Make `WorkbenchClient` (`frontend/src/app/workbench/workbench-client.tsx`) and `PipelineClient` (`frontend/src/app/pipeline/pipeline-client.tsx`) reachable as tertiary forms from the right sidebar across the app, per DESIGN §3.3 "tertiary screens." The `/workbench` and `/pipeline` routes are **kept** as thin entry points that render the same clients; `ShellFrame` `NAVIGATION_ITEMS` (shell-frame.tsx:19-22) is updated to reflect their tertiary status (reachable, not primary). The exact sidebar affordance (new tab vs. menu entry vs. overlay) is bounded by the §8 sub-decision if it changes `SidebarTabId` (`workspace-sidebar.tsx:11-18`).
- **What stays.** Both routes still resolve and render their clients (backward-compatible deep links, e.g. `/pipeline?category=TASK&scopeKey=…` from deliverable rows). `WorkbenchClient`/`PipelineClient` internals (contracts, DECOMP/PREP/TASK/AUDIT cards, scope selectors) are unchanged.
- **In-flight-turn survival.** Opening a tertiary form must not unmount the loop's `ChatPanel`; the form renders in the sidebar/tertiary region while the loop stays mounted (same primitive as 28a). If a tertiary form is reached by route navigation, that path is unchanged from today.
- **Contract/permission untouched.** No engine/API/permission change; only routing/IA and nav labels move.
- **Nothing deleted.** This is the binding "nothing is deleted" tranche: `/workbench`, `/pipeline`, the file tree, and the portal matrix all remain reachable via the sidebar.
- **Acceptance:** `npm run typecheck` clean; `npx vitest run` green; `next build` prerenders `/`, `/workbench`, `/pipeline`, `/chat`; every tertiary screen demonstrably reachable from the sidebar.

### 28e — Closeout

**Status: LANDED 2026-06-20.** DESIGN §5 now records that the earlier
sidebar-left placement was transitional and closed by D-APP-28: the live loop is
primary app-wide, the multi-view sidebar is right-side app-wide, and
Portal/Workbench/Pipeline are sidebar-reachable tertiary forms with routes
preserved. The D-APP-28 register row records that 28a-28e landed. Resume and
coordination surfaces now state that the active loop-first pivot queue has no
remaining unstarted tranche, while D-APP-18 remains separately awaiting ruling
for any default-provider cutover. Validation: governance diff hygiene and stale
handoff scan; runtime commands were not rerun because 28e changed docs and
coordination only after the validated 28d source tranche.

- **Scope.** Update DESIGN §5 and its line-111 "Transitional placement decision" bullet (named "§5.2" by the D-APP-28 ruling/packet) to record the loop-as-primary app-wide end-state and **close the transitional sidebar-left note** — sidebar is now right app-wide. Annotate `execution/_Coordination/_DECISIONS/_REGISTER.md` D-APP-28 row with the landed-tranche summary, write the resume/next-instance prompt, and add a plan completion record. No source change expected; if any is made, re-run the runtime gates.
- **What stays / nothing deleted / contract untouched.** Documentation-and-coordination only; no code, no route, no contract, no permission change.
- **Acceptance:** governance gate (diff hygiene, path checks); the line-111 transitional note closed; register + resume updated.

## 6. Sequencing

`28a LANDED → 28b LANDED → 28c LANDED → 28d LANDED → 28e LANDED`.

- `28a` landed the sidebar-right primitive, so `28b` (AppShell flip) and `28c` (portal) can consume a proven structure rather than each forking layout.
- `28b` landed the AppShell sidebar-right flip, so `28c`/`28d` start from an app-wide right-sidebar geometry.
- `28c` landed the portal loop-first home and in-place Type-0/Type-1 matrix launch.
- `28d` consumed D-APP-31/D-APP-32, demoting `/workbench` and `/pipeline` into sidebar-reachable tertiary forms and opening OPERATIVE/deliverable Pipeline intent in-place.
- `28e` recorded the realized end-state and closed the transitional DESIGN note.

## 7. Boundaries — Explicit Out of Scope (human-gated)

Restating D-APP-28's out-of-scope (ruling final paragraph): this plan does **not** approve deleting any route or tertiary screen (portal/workbench/pipeline/file tree all stay reachable), nor any engine / public-contract / permission-plane change. The public UIEvent type and the permission/hook/path/redaction plane are untouched — this is routing/layout only.

Deferrals **not reopened** by this plan: **D-APP-26** (editable document screen / content-WRITE — RULED Option C defer), **D-APP-27** (Type-2 task agents remain excluded from direct chat — RULED Option C; `assertDirectChatPersona` stands), **D-APP-29** (SECONDARY task-management/Workflow phase — RULED Option A defer). The Workflow sidebar view stays a thin peek (`workspace-sidebar.tsx:152-155`); no Type-2 direct-entry brief is introduced.

## 8. Required Human Rulings

D-APP-28 is **already RULED** (Option B, `D-APP-28_RULING_2026-06-19.md`) — this plan does not re-litigate it. The sub-decisions the tranches surfaced were packeted and **ruled 2026-06-19**:

- **SD-1 — In-place launch UX (28c) → D-APP-30 RULED Option B.** A Type-0/Type-1 cell click swaps `?agent=` on the mounted loop immediately when idle, and is **guarded mid-turn** by reusing the Tranche-5c `streaming` / `useHarnessStreaming` flag so an in-flight turn is never clobbered; a brief loop focus/transition signals the boot.
- **SD-2 — OPERATIVE/Type-2 pipeline cells (28c) → D-APP-31 RULED Option B (staged with 28d).** OPERATIVE cells (and deliverable rows) open the governed `/pipeline` form as an **in-place tertiary form**, landing once the 28d / D-APP-32 affordance exists; the **interim through 28c is the retained `/pipeline` route hop** (nothing deleted). D-APP-27 is not reopened.
- **SD-3 — Tertiary-form affordance + sidebar tab surface (28d) → D-APP-32 RULED Option A.** Demoted screens get **new `SidebarTabId` tabs** (`workspace-sidebar.tsx:11-18`), each opening its full-screen tertiary form. Chat history stays on the right as the existing `Sessions` tab (Tranche 5c) — no left rail (owner directive, 2026-06-19).

## 9. Validation Policy

Per-tranche gates (binding):

- `npm run typecheck` — `tsc --noEmit` for both the Next and electron configs (`frontend/package.json` `typecheck`, :15); must be clean.
- `npx vitest run` — full suite green against the current **499-test baseline** after 28d (DESIGN §5 records 477 at Tranche 5b line 122; Tranche 5c established 491; 28b added one layout-geometry guard; 28c added portal-loop/matrix coverage; 28d added tertiary-sidebar/in-place launch coverage).
- `next build` — must prerender the affected routes (`/`, `/chat`, `/workbench`, `/pipeline`). `frontend/next.config.mjs` needs no prerender-directive change (the pivot is grid/routing, not a render-mode change).
- Manual visual/interaction check is required where no test covers DOM structure: grid column order, resize-handle drag direction, and collapsed-label placement after the `28b` flip.

## 10. Acceptance Criteria

End-state checks (all hold after 28e):

1. The multi-view sidebar is on the **RIGHT** on every surface (`/`, `/chat`, `/workbench`, `/pipeline`); the DESIGN line-111 transitional sidebar-left note (named "§5.2" by the D-APP-28 ruling/packet) is closed.
2. The live loop is the **primary** surface on every route, not a side panel.
3. Matrix Type-0/Type-1 launches **boot a session in-place** (route-free `?agent=` on the mounted loop), not `router.push` to a route-as-main; OPERATIVE-cell behavior is whatever SD-2 rules.
4. Every tertiary screen — portal matrix, `/workbench`, `/pipeline`, file tree — is **reachable via the sidebar**; the routes still resolve and render.
5. **Nothing is deleted.**
6. The public **UIEvent contract and permission plane are unchanged** (no diff under the engine/permission paths).
7. **In-flight turns survive** every relayout (`ChatPanel` never unmounted across sidebar flip, in-place launch, or tertiary-form open).
8. `npm run typecheck` + `npx vitest run` (current 499 baseline after 28d) green and `next build` prerenders the affected routes at each landed tranche.

## 11. Evidence Basis

- Shells: `frontend/src/components/shell/app-shell.tsx` (5-col grid `:307`, `DRAG_DIRECTION` :48-52, delta apply :183, grid children ~:311-371, `TOOLKIT_PANE_VISIBLE` :56), `frontend/src/components/shell/loop-shell.tsx` (`loop-grid` class :32, sidebar-right :57-78, Suspense-wrapped ChatPanel :40-53), `frontend/src/components/shell/shell-frame.tsx` (`NAVIGATION_ITEMS` :19-22, `/chat`-absent note :16-18), `frontend/src/components/shell/workspace-sidebar.tsx` (`SidebarTabId` :11-18, Workflow peek :152-155), `frontend/src/components/shell/chat-panel.tsx` (route-free boot + in-flight state).
- Geometry/CSS: `frontend/src/lib/shell/layout-state.ts` (`ResizablePaneKey` :1, `LAYOUT_STORAGE_KEY` :8); `frontend/src/app/globals.css` (`.shell-grid`, `.loop-grid`, `.shell-pane--collapsed`, `.shell-pane-collapsed-label`).
- Routing/matrix: `frontend/src/app/page.tsx`, `frontend/src/app/workbench/page.tsx` + `workbench-client.tsx`, `frontend/src/app/pipeline/page.tsx` + `pipeline-client.tsx`, `frontend/src/app/chat/page.tsx`; `frontend/src/components/shell/portal-loop-shell.tsx`; `frontend/src/components/portal/agent-matrix.tsx`; `frontend/src/lib/portal/agent-matrix-cells.ts`; `frontend/src/lib/shell/loop-first.ts` (`buildDirectChatHref`, `buildPortalPersonaHref`, `CHAT_ROUTE`/`CHAT_SECTION`).
- Session boot/guard: `frontend/src/app/api/harness/session/create/route.ts`; `assertDirectChatPersona` (`frontend/src/lib/harness/agent-roster.ts:98`, D-APP-24).
- Tests/build: `frontend/src/__tests__/lib/layout-state.test.ts` (clamping/collapse plus 28b AppShell right-sidebar grid-order/drag-sign guard), `agent-matrix-cells.test.ts` (route + Type-0/1 roster guard), `agent-matrix-launch.test.ts` (route-preserving query merge), `workspace-sidebar.test.ts` (tertiary tab rendering), `loop-first.test.ts`, `navigation-intent.test.ts`; `frontend/package.json` (:14-15); `frontend/next.config.mjs`.
- Decision substrate: `execution/_Coordination/_DECISIONS/D-APP-28_PACKET_2026-06-19.md`, `execution/_Coordination/_DECISIONS/D-APP-28_RULING_2026-06-19.md`, `execution/_Coordination/_DECISIONS/_REGISTER.md` (D-APP-28 row: RULED Option B); D-APP-23/24 rows; D-APP-26 (Option C defer), D-APP-27 (Option C exclude), D-APP-29 (Option A defer) rulings; D-APP-30 (Option B guard mid-turn), D-APP-31 (Option B in-place form, staged with 28d), D-APP-32 (Option A new sidebar tabs) rulings (SD-1/2/3).
- Design: `plans/DESIGN_2026-06-18_agent_orchestration_ui.md` §3.1 (line 52), §3.2 (line 58), §3.3 (line 70), §5 (line 106); the "Transitional placement decision" bullet at line 111 (the transitional sidebar-left note the D-APP-28 ruling/packet call "§5.2"); Tranche 5b 477-test record and Tranche 5c 491-test record at line 122; Tranche 28b raised the suite baseline to 492, Tranche 28c raised it to 496, and Tranche 28d raised it to 499.

## 12. Finalization Rule

This plan is complete: `28a`–`28e` have landed, source/layout tranches were typecheck- + vitest-green (current 499 baseline after 28d) with `next build` prerendering the affected routes, and the §10 acceptance checks hold. DESIGN §5 and the line-111 "Transitional placement decision" bullet (named "§5.2" by the D-APP-28 ruling/packet) now declare the loop-primary, sidebar-right app-wide end-state and close the transitional sidebar-left note; the D-APP-28 row in `execution/_Coordination/_DECISIONS/_REGISTER.md` records that 28a-28e landed; resume / next-instance prompts and the plan completion record are updated. SD-1/SD-2/SD-3 were ruled 2026-06-19 (D-APP-30/31/32). D-APP-18 remains separately awaiting ruling and continues to block only default-provider cutover.
