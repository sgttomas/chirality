# SHELL capability inventory — notes (R1b, run RUN_D128_CONCORDANCE_2026-09-21_1614Z)

Area: `projects/chirality-app-dev/frontend/src/components/shell/**` and `frontend/src/lib/shell/**` at frozen basis `00115c719`
(file list = `R1_INVENTORY/IMPLEMENTATION_SURFACES.csv` rows with `Area=SHELL`, 53 files).
Output: `SHELL_capabilities.csv`, 45 rows (`CAP-SHELL-001`…`045`). Validator: `RESULT PASS errors=0 warnings=0`.
No deliverable folders were read. Rows come from code, the evidence pack, a scratchpad import graph and test-import greps.

## 1. Census

`CENSUS rows=45 LIVE=44 LEGACY_ONLY=0 TEST_ONLY=1 UNREACHED=0 ENABLED=42 DISABLED=3`

- The evidence pack `REACHABILITY.csv` marks all 53 SHELL files `LIVE`. None are `LEGACY_ONLY` or `UNREACHED`.
- Static reach overstates what is rendered in this area (see §4). I recomputed reach with a scratchpad script, cutting the edges that the route wrapper discards. The results go into `STATE` and `Notes`, not into `REACH`, because the brief limits `REACH` to static reach.
- `TEST_ONLY` (CAP-SHELL-017): the renderer-storage snapshot and compare functions in `user-data-inventory.ts` have only test consumers. The module itself is LIVE through its `UPDATE_*` constants.
- `PostReleaseBasis` is `NO` on every row. `TOUCHED_PATHS.csv` has no path under `projects/chirality-app-dev/frontend/**`. The four commits touch only `exports/`, `docs/governance_harness/` and `projects/chirality-runtime/**`.

## 2. Granularity rationale

- Each row is one user-visible behaviour or contract surface. Helpers are folded into the behaviour they serve. For example, `ansi.ts` goes into markdown rendering, `activity-sentences.ts` into the stream views, and `native-progress.ts` into turn activity and event derivations.
- `chat-panel.tsx` (2178 lines) is split into 13 rows by operator-visible function. The splits cover:
  - session lifecycle, turn streaming, recovery/re-attach, Stop, steering receipts and turn phase;
  - the model/permissions/mode selectors, draft persistence, attachments and selected methods;
  - Plan Mode, new/resume chat, and transcript presentation.
  Each split is a plausible separate deliverable claim.
- `shell-frame.tsx` has two rows because its variants differ. The legacy default chrome renders only on the 404 route. The woven `workspace` variant is the live account and settings host.
- `document-view.tsx` has two rows. The woven UI uses the file previewer; the deliverable-roster viewer is legacy.
- Retired presentation code keeps its own rows (001, 002, 004–008, 044). Forward workers can then see that a claim anchored there is not rendered in the product.

## 3. Files covered versus total

`COVERAGE covered=53 total=53`

All 53 files are named in at least one row's `Paths`. The CSS module `account-controls.module.css` sits in the account-row row. No file is uncovered.

## 4. Dead, unreached, disabled or retired code observed

- **Route-level legacy shells are imported but never rendered.**
  - Every page passes its legacy shell as the `legacy` prop to `WovenDialogueRoute`: `app/chat/page.tsx` → `LoopShell`, `app/page.tsx` → `PortalLoopShell`, `app/pipeline/pipeline-client.tsx` and `app/workbench/workbench-client.tsx` → `LoopTertiaryShell`.
  - `components/woven-dialogue/woven-dialogue-route.tsx:18` discards the prop (`void legacy;`) and always renders `WovenDialogueShell`.
  - Tests assert this: `__tests__/components/woven-dialogue-route.test.tsx` and `loop-tertiary-routes.test.ts`.
  - The following are therefore `STATE=DISABLED`: `loop-shell.tsx`, `portal-loop-shell.tsx`, `loop-tertiary-shell.tsx`, `sidebar-right-loop-layout.tsx` and `tertiary-sidebar-tabs.tsx`.
  - The discarded shells also make `AgentMatrix`, `PipelineSurface` and `WorkbenchSurface` statically LIVE in the pack, though they are unrendered through this path. Those files belong to other areas.
- **Legacy AppShell cluster renders only on the 404 route.**
  - `app/not-found.tsx:6` mounts `AppShell`. That brings in `layout-state.ts`, `workspace-sidebar.tsx`, `session-list-view.tsx` and `operator-toolkit-panel.tsx`.
  - It also brings the default-variant `ShellFrame` chrome: Working Root path input, PORTAL nav, and the Runtime & credentials disclosure.
  - It also renders the deliverable-roster `LegacyDocumentView` and the non-woven branches of `ChatPanel`.
  - The woven shell reaches none of these. I recomputed reach with the `app-shell.tsx` and three loop-shell edges cut: these five files become unreachable.
  - They are tagged `STATE=ENABLED` because an unknown URL does render them. Every such row notes "404 only; retired presentation".
- **`LocalModelStatus` is disabled** (CAP-SHELL-013). `account-row.tsx:68` shows it only when `props.hosted` is falsy, and the only production caller, `shell-frame.tsx:403`, always passes `hosted`.
- **Dead exports (no production consumer):**
  - `useWorkspaceSidebarActions` (`workspace-sidebar.tsx:60`);
  - `buildDirectChatHref` (`loop-first.ts`); `buildPortalPersonaHref` is used only by the disabled `PortalLoopShell`;
  - `ServerRequests` (`request-card.tsx:209`);
  - `TURN_CONTINUATION_NOTE` (`turn-phase.ts:68`);
  - `snapshotRendererUserData` and `rendererUserDataPreserved` (`user-data-inventory.ts`), which have test consumers only.
- **Duplicate surfaces:**
  - `SessionListView` (404 sidebar) duplicates the woven navigator's session list.
  - `TranscriptStreamView`, `ToolStreamView` and `SubagentStreamView` are mounted both by the woven activity shelf and by the 404 sidebar.
- **Desktop-only gates (tagged ENABLED):**
  - App update: `app-update-provider.tsx:110` is a no-op without the bridge.
  - Runtime connectivity: `use-runtime-connectivity.ts` returns null without the preload bridge.
  - Native document handoff: `document-view.tsx:268` throws without the bridge.
  - Native attachment and folder pickers fall back to the in-app `FilePicker` and the typed path when the bridge is absent (`chat-panel.tsx:1855`).
- **`tool.permission` approval cards are live under Codex.** I checked this because the name suggests legacy. The Runtime core adapter (`projects/chirality-runtime/packages/core/src/delegated-engine-adapter.ts:298,310`) maps Codex approvals to `tool.permission`.
  - By contrast, the `subagent.*` lifecycle branch of `deriveSubagentActivity` serves legacy SDK-engine events. It is kept alongside the native child-thread path.
- **No direct unit test:**
  - `steering-receipts.ts`, `turn-phase.ts`, `activity-sentences.ts`, `native-attachments.ts` and `turn-activity.tsx` are covered only through chat-panel or activity tests.
  - `operator-toolkit-panel.tsx`, `file-picker.tsx`, `account-icon.tsx` and `use-runtime-connectivity.ts` have no test that imports them by path. `file-picker` is mocked in the chat-panel tests.

## 5. Method friction with §5.2, with proposed revision

- **Static `REACH` cannot express "imported, never rendered".** For this area the pack marks everything LIVE, yet the three route shells and their sub-tree are discarded at render time. I encoded this in `STATE=DISABLED` plus a gate citation, as the brief directs.
  - Proposal: add an optional `REACH=LIVE(static-only)` qualifier, or a `RENDER=MOUNTED|UNMOUNTED|ERROR_ROUTE_ONLY` token in `Notes`. The pack's reachability script could also accept a cut list of known prop-discarding wrappers (`woven-dialogue-route.tsx`) and emit a second `RenderReach` column.
- **ENABLED/DISABLED is binary.** The 404-only AppShell cluster is technically mounted, but only on an error route. I used `ENABLED` plus a note.
  - Proposal: allow `STATE=ENABLED(error-route-only)`, or an equivalent qualifier.
- **Test coverage by import path over-counts mocks.** Many chat-panel tests `vi.mock` `file-picker`, `persona-picker` or `permission-requests`, so an import-string match does not mean coverage. I listed only tests that exercise the behaviour, and marked the rest `(indirect)`.
  - Proposal: the evidence pack could carry a `TEST_IMPORTS.csv` that separates `import` from `vi.mock`.
- **A capability can mix reach within one module** (CAP-SHELL-017, `user-data-inventory.ts`). The "tag by live path" rule does not fit when the capability's own functions are test-only but the file is LIVE. I tagged it `TEST_ONLY` and explained why in `Notes`.

## 6. Effort

- About 25 SHELL files inspected by export and comment greps; about 8 read in line ranges (`chat-panel.tsx`, `shell-frame.tsx`, `app-shell.tsx`, `document-view.tsx`, `account-row.tsx`, `app-update-provider.tsx`, `workspace-sidebar.tsx`, `tertiary-sidebar-tabs.tsx`).
- Also read: the route pages, `woven-dialogue-route.tsx`, and targeted slices of `woven-dialogue-shell.tsx` and `right-panel.tsx`, plus one Runtime core grep.
- The import graph and render-reach recomputation were done with a scratchpad script.
- Context was comfortable, not tight.
