# 02 — Current State of the Shell at `307addfc2`

All paths are relative to `projects/chirality-app-dev/frontend/` unless stated. Line counts and line numbers are from `origin/main` `307addfc2` (2026-09-04). Re-verify with the commands in §9 before relying on a number.

## 1. Routes

| Route | Renders | Notes |
|---|---|---|
| `/` | `WovenDialogueRoute` with `defaultSurface="dialogue"`, legacy fallback `PortalLoopShell` | `src/app/page.tsx` |
| `/chat` | `WovenDialogueRoute`, legacy fallback `LoopShell` | `src/app/chat/page.tsx` |
| `/workbench` | `WorkbenchClient` | Retired by SR-06; keep the route file |
| `/pipeline` | `PipelineClient` | Retired by SR-06; keep the route file |
| `?legacy=1` | Any woven route renders its legacy fallback inside `data-legacy="true"` | `src/components/woven-dialogue/woven-dialogue-route.tsx:22` |

Electron opens one `BrowserWindow` (`electron/main.ts:524`) at the packaged renderer server's URL or `ELECTRON_RENDERER_URL`. There is **no second-window facility today**; SR-05 pop-out needs one.

## 2. The woven shell, component by component

Folder `src/components/woven-dialogue/`, 1,812 lines total.

| File | Lines | What it does today | Bearing on the design |
|---|---|---|---|
| `woven-dialogue-shell.tsx` | 670 | Owns surface state, session list, replay loader, workspace state persistence, resize handles, and composes the four regions. | Central to every tranche. |
| `dialogue-viewport.tsx` | 60 | Keeps the primary `ChatPanel` mounted but sets `hidden` and `aria-hidden` when a replay lens or a focused surface (`workbench` / `pipeline`) is shown. | **Contradicts SR-01.** The dialogue is hidden, not merely de-emphasised. Tranche T1 removes the focused branch and stops replay from hiding the primary. |
| `navigator.tsx` | 327 | Left panel: three mode groups (`dialogue`, `workbench`, `pipeline`) each listing sessions attributed to that surface; `FileTreePanel` below; footer link to the legacy interface. Session labels are the persona string, not a title. | Mode groups and the file tree leave (SR-03, SR-04, SR-06). Session projection helper `buildNavigatorSessionGroups` is reusable for date grouping. |
| `coordination-panel.tsx` | 76 | Right panel with two tabs, Work and Agents. | Becomes the right-panel view switcher (SR-02). |
| `work-projection.tsx` | 99 | Renders `CoordinationWorkItem[]`. The shell passes a constant empty array (`woven-dialogue-shell.tsx:56`, `:620`), so it always shows "No structured plan recorded." | No data source exists. Drop from the switcher until one does (DEL-02-02-V3-01 / V3-02 are its future sources). |
| `agents-projection.tsx` | 220 | Recorded agent hierarchy from the session list, with parentage. | Becomes the "Who is working" view. |
| `activity-shelf.tsx` | 71 | Bottom region, resizable 120–480px, tabs Tools / Events / Children wrapping the three stream views. | Becomes a one-line strip; the three views move into the right panel's Activity view (SR-07). |
| `selected-session-replay-lens.tsx` | 258 | Read-only transcript of a recorded session with provenance block; shown in the centre instead of the dialogue. | Moves into the right panel as the Session view (SR-08). Loader and guard are unchanged. |
| `woven-dialogue-route.tsx` | 31 | Legacy switch. | Unchanged. |

Supporting library `src/lib/woven-dialogue/` (3,075 lines): `contracts.ts`, `guarded-session-selection.ts` (161), `operator-projection.ts` (198), `recorded-agent-hierarchy.ts` (332), `selected-session-replay.ts` (332), `woven-workspace-state.ts` (504).

## 3. Shell frame and header

`src/components/shell/shell-frame.tsx`. The header (`:170` onward) renders:

- `img src="/chirality-app-icon.svg"` at 26px with class `shell-brand-tile` (`:178`) — **removed by SR-11**.
- `<span className="shell-wordmark">Chira<em>lity</em></span>` (`:184`) — **replaced by SR-15** with a single-colour span.
- `shell-kicker` (section), `h1` (title), `shell-subtitle` — the woven shell passes `section="CHAT"`, `title="Woven Dialogue"`, and the sentence "A shared professional workspace where dialogue produces inspectable artifacts and governed work." — **all removed by SR-18**.
- Runtime connectivity chip (accessible reconnect action; DEL-02-01 2026-08-15) — chip **removed** with the header (SR-12); its reconnect action and `aria-label` move to the activity strip's status dot.
- A settings disclosure containing `RuntimeSettings` and `ApiKeySettings` (`:288-289`) and `ThemeControl` (`:318`) — **relocated** into the account popover and Settings view (SR-17).

CSS for the header: `src/app/globals.css` `.shell-header` (`:247`), `.shell-brand-row` (`:269`), `.shell-brand-tile` (`:276`), `.shell-wordmark` (`:286`), `.shell-wordmark em` (`:294`), `.shell-kicker` (`:310`), `.shell-subtitle` (`:319`), `.shell-header--workspace` (`:2451`).

## 4. Dialogue

`src/components/shell/chat-panel.tsx` (681 lines). Already provides: streaming assistant text, interrupt with the "Turn interrupted by operator." terminal text, per-session drafts and attachments persisted by storage key, `UiAttachment { path, displayName, mimeType, clientType }` chips, `PermissionRequests` inline (`:538`), the persona from `PersonaPicker`, and four operator modes at `:52-57`:

| value | current label | target label (SR-18) |
|---|---|---|
| `readOnly` | Read-only | Read only |
| `ask` | Plan (ask) | Ask before changes |
| `workspaceWrite` | Gated-write | Approve each write |
| `bypass` | Autonomous | Run on its own |

Markdown: `chat-markdown.tsx` uses `react-markdown` with `remark-gfm`; links render as `<a target="_blank">` (`:25`). There is no path or identifier recognition today; SR-09 reference chips are a new component in this pipeline.

## 5. Documents and files

- `src/components/shell/document-view.tsx` (254 lines): fetches the deliverable roster (`/api/project/deliverables`), lets the user pick a deliverable and one of the control-plane files (`_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`, `MEMORY.md`, plus selected production documents), fetches content through `/api/working-root/deliverable/content`, renders with `ChatMarkdown`. Mounted **only** in the legacy `WorkspaceSidebar` ("Document" tab) and inside `WorkbenchSurface`. Not in the woven route.
- `src/components/shell/file-tree-panel.tsx` (258 lines): renders `/api/working-root/tree`. Directory rows have a toggle button; file rows are inert spans (`:34-60`). Nothing opens.
- **API gap.** `readDeliverableContent` (`src/lib/workspace/deliverable-contracts.ts`) reads only well-known documents inside a deliverable folder. There is no endpoint that returns the bytes of an arbitrary file under the working root. SR-04 needs a bounded read endpoint with the same containment rules as the tree (`docs/CONTRACT.md` K-PATH-2 and K-PATH-3; PRD NFR-006). See `04_IMPLEMENTATION_PLAN.md` T3.

## 5a. Working root is app-global today

`src/components/workspace/workspace-provider.tsx` holds one `projectRoot` for the whole app, persisted under `localStorage` key `chirality.projectRoot`, validated through `/api/working-root/validate`, set from the header chip. Every consumer reads it from `useWorkspace()`. Sessions are listed per root: `listHarnessSessions(projectRoot)` calls `/api/harness/session/list?projectRoot=` (`src/lib/harness/client.ts:170`). SR-21 makes the root a property of the chat and SR-20 lists chats across roots, so the provider becomes "root of the active chat" and the list must be assembled from a persisted set of known roots (see `03_TARGET_SPEC.md` §12 and `04_IMPLEMENTATION_PLAN.md` T6).

## 6. Activity streams

`src/lib/shell/harness-event-views.ts` projects harness events into `ToolActivityRow { key, toolName, status, source?, surface?, pathFields, lastEventType, timestamp, eventCount }`, `SubagentActivityRow`, and permission rows. Views: `tool-stream-view.tsx` (72), `transcript-stream-view.tsx`, `subagent-stream-view.tsx`. `pathFields` is the redacted path map the reference chips (SR-09) can open from.

## 7. Settings, account, runtime

| Component | Lines | Mounted where | Design placement |
|---|---|---|---|
| `settings/account-consent-settings.tsx` | 459 | **Not mounted.** Built for DEL-02-05-V3-02 against the fake `HostedEngineConsentPort`; live wiring is DEL-02-05-V3-03 and is `NOT_SELECTABLE_UNTIL` the Root contract routes to the App. | Popover "OpenAI" group and Settings → OpenAI account (SR-17). Keep every "for this root" phrase. |
| `settings/runtime-settings.tsx` | 385 | `shell-frame.tsx:288` settings disclosure | Popover "Local model" switch and Settings → Local model. Provides Install / Start / Stop / Uninstall / Refresh, residency line, oMLX model select, "Activate Explicitly". |
| `settings/api-key-settings.tsx` | 392 | `shell-frame.tsx:289` | Settings → Keys (Anthropic, oMLX). |
| `shell/theme-control.tsx` | — | `shell-frame.tsx:318`; stamps `data-theme` on `<html>`; `light` / `dark` / `system` | Popover "Appearance" and Settings → Appearance. |
| `portal/agent-matrix.tsx` | 265 | Legacy sidebar "Portal" tab only | Not part of the adopted design. The owner's "user portal" is the account popover, not this matrix. |

Consent vocabulary that the UI must render verbatim (`src/lib/consent/hosted-engine-consent-port.ts`): `Opt-in Preview`; the three command-network postures with labels "No command network (default)", "Ask per destination", "Command network on (`network_access = true`)"; the role labels including `role not mechanically enforced` and `instruction-asserted`. The mock abbreviates these to Off / Ask / On and Agent 0 / 1 / 2 for the segmented control; the full label must remain in the tooltip or the row beneath (see `03_TARGET_SPEC.md` §8.4).

## 8. Persisted workspace state

`src/lib/woven-dialogue/woven-workspace-state.ts`, schema string `chirality.woven-workspace/v1` (must **not** be bumped; the reader hard-rejects other schema strings, DEL-02-04 Remaining). Fields at `:62-105`: `theme`, `navigatorWidth`, `coordinationWidth`, `activityHeight`, `navigatorCollapsed`, `coordinationCollapsed`, `activityCollapsed`, `coordinationView`, `dialogueAnchorId`, `focusedArtifact`, `expandedObjectIds`, `selectedReplaySessionId`, `contextReferences`, `sessionSurfaces` (cap 500, first attribution wins), `navigatorExpandedSurfaces`, `migration`. New fields must be additive with sanitize-and-fallback readers, following the Stage A / B2 pattern in the R6 run record.

## 9. Tests that pin the current shell

Under `src/__tests__/components/`: `woven-dialogue-shell.test.tsx`, `woven-dialogue-viewport.test.tsx` (asserts the primary stays mounted while replay and **focused surfaces** change, and a "Return to primary dialogue" action for a focused surface), `woven-dialogue-navigator.test.tsx` (references Workbench/Pipeline groups), `woven-dialogue-controls.test.tsx`, `woven-dialogue-route.test.tsx`, `woven-dialogue-runtime-reconnect.test.tsx`, `woven-dialogue-work-projection.test.tsx`, `selected-session-replay-lens.test.tsx`, `shell-frame.test.tsx`, `shell-frame-runtime-connectivity.test.tsx`, `app-shell-resize.test.tsx`, `chat-panel-*.test.ts(x)`, `runtime-settings.test.ts`, `api-key-settings-storage-states.test.ts`, `account-consent-settings-states.test.ts`. 166 test files, run by `npm test` (`vitest run`); render tests use `react-test-renderer` per D-APP-36.

Verification commands (run from `frontend/`):

```bash
grep -n "hidden={!primaryVisible}" src/components/woven-dialogue/dialogue-viewport.tsx
grep -n "EMPTY_WORK_ITEMS" src/components/woven-dialogue/woven-dialogue-shell.tsx
grep -n "Chira<em>" src/components/shell/shell-frame.tsx
grep -rn "Workbench\|Pipeline" src/components/woven-dialogue/navigator.tsx | head
ls src/__tests__/components | grep -i "woven\|shell-frame\|replay"
```

## 10. Brand assets in the tree

| Path | Role today | Design |
|---|---|---|
| `public/chirality-app-icon.svg` | Header tile | Retired from the header (SR-11). Keep the file until nothing references it; `shell-frame.test.tsx` may assert it. |
| `src/app/icon.svg` | Next `metadata.icons` by file convention (DEL-02-01 record-only note) | Replace with the chalk mark as `src/app/icon.png` (Next accepts `icon.png`); delete `icon.svg` in the same change. |
| `build/icon-macos.svg`, `build/icon.icns` | Committed macOS icon; regenerated only by hand with `scripts/generate-macos-icon.mjs` (not in the build graph; requires transitive `sharp`) | Replace `icon.icns` with `assets/painted-field.icns`. The SVG source no longer applies because the mark is raster; see `05_LOGO_AND_BRAND.md` §4 for the reproducibility note the script header demands. |
| `artifacts/logos/` | Owner's source photographs and `generated/` outputs | **Git-ignored** (`.gitignore:53`, `**/frontend/artifacts/`). That is why this package carries copies under `assets/`. |

## 11. Contradictions between code and the adopted design, in one list

1. `DialogueViewport` hides the primary dialogue for replay and for focused surfaces (SR-01, SR-08).
2. Navigator lists sessions by mode group, including two retired surfaces, and hosts the file tree (SR-03, SR-04, SR-06).
3. Right panel is Coordination with an always-empty Work tab; no Files, no document viewer, no Activity, no Settings (SR-02, SR-04, SR-07, SR-17).
4. File tree rows cannot be opened (SR-04); no file read endpoint (SR-04).
5. A header row exists at all, showing the icon, a split italic wordmark, a kicker, a title, a subtitle, the root chip, the status chip, and a gear (SR-11, SR-12, SR-15, SR-18).
6. Settings live in a header disclosure; account and consent are unmounted; there is no account row (SR-17).
7. Activity is a resizable region that takes height from the dialogue (SR-07).
8. Assistant text carries no reference chips; the document viewer offers no Ask or Attach (SR-09).
9. Mode and persona labels use developer vocabulary (SR-18).
10. One Electron window; no pop-out (SR-05).
11. The working root is one app-global value chosen in the header, and sessions are listed for that root only (SR-20, SR-21).
12. Sign-in and consent are both presented as per root (SR-19).
