# WOVEN capability inventory — notes (R1b, area WOVEN)

Area: `projects/chirality-app-dev/frontend/src/components/woven-dialogue/**` and
`projects/chirality-app-dev/frontend/src/lib/woven-dialogue/**` at frozen basis `00115c719`.
The file list is the 23 `Area=WOVEN` rows of `R1_INVENTORY/IMPLEMENTATION_SURFACES.csv`.
Output: `WOVEN_capabilities.csv`, 43 rows (`CAP-WOVEN-001`…`043`). Validator: `RESULT PASS errors=0 warnings=0`.
No deliverable folders were read. Rows come from code read at the frozen tree, production and test import greps, and the R2 evidence pack.

## 1. Census

CENSUS rows=43 LIVE=41 LEGACY_ONLY=0 TEST_ONLY=2 UNREACHED=1 ENABLED=36 DISABLED=7

- `UNREACHED=1` is `CAP-WOVEN-043` (`lib/woven-dialogue/contracts.ts`). The pack marks it UNREACHED. Under the TYPE-ONLY rule the row is tagged `REACH=LIVE; TYPE-ONLY`: live code consumes it only through `import type`, including the shell, the replay lens, the coordination panel, `selected-session-replay.ts` and `components/shell/chat-panel.tsx`. The row names the pack status, so it counts as marked.
- TEST_ONLY rows:
  - 041: `work-projection.tsx`.
  - 042: `workflows-view.tsx` and `workflow-detail.tsx`.
- DISABLED rows:
  - 002: legacy link.
  - 031: Skills browsing.
  - 035: legacy ActivityShelf.
  - 039: surface attribution and mode groups.
  - 040: retired persisted fields.
  - 041: Work projection.
  - 042: plan file browser.
- `PostReleaseBasis` is `NO` on every row. `R2/_shared/EVIDENCE_PACK/TOUCHED_PATHS.csv` has no row under `projects/chirality-app-dev/frontend/**`, so no blame was needed.

## 2. Granularity rationale

- There is one row per behaviour a human or the system can observe. Helpers are folded into the behaviour they serve. For example, `chatFolderKey`, `folderSectionLabels` and `formatChatWhen` go into the Navigator chat list row.
- `woven-dialogue-shell.tsx` (1068 lines) is the orchestrator. It is split by behaviour into 15 rows:
  - layout;
  - pane sizing;
  - dialogue hosting;
  - folder lock;
  - session listing;
  - background attention;
  - new chat and Cmd/Ctrl+K;
  - cross-folder chats;
  - known folders;
  - last-chat restore;
  - replay loading;
  - continuation;
  - live turn-phase publication;
  - and its share of right-panel wiring.
- `right-panel.tsx` is split by tab: the frame, Files, Plan, the session menu and Workflows. Activity and Agents have their own rows because their content lives in other modules.
- `woven-workspace-state.ts` (758 lines) is split into five rows:
  - the persistence and migration contract;
  - the theme contract, which `app/layout.tsx` and `components/shell/theme-control.tsx` consume;
  - the chat index and known roots, folded into the cross-folder and known-folder rows;
  - surface attribution (disabled);
  - retired persisted fields (disabled).
- Retired or unmounted presentation kept in LIVE modules gets its own DISABLED row: legacy link, Skills, ActivityShelf and surface groups. A deliverable claiming these would otherwise map onto a live row by mistake.
- Rows 001–038 are live behaviour. Rows 039–042 are disabled or test-only. Row 043 is the type contract.

## 3. Files covered versus total

COVERAGE covered=23 total=23

- Every file in the Area list appears in at least one row's `Paths`.
- `workflows.module.css` appears in rows 026 and 042. It is LIVE through `right-panel.tsx`, which uses it for the header and tab styles, as well as through the test-only `workflows-view.tsx`.
- No file is uncovered.

## 4. Dead, unreached, disabled or retired code observed

- **The route's legacy element is never rendered.** `WovenDialogueRoute` voids `legacy` (`woven-dialogue-route.tsx:18`). All four pages still build `PortalLoopShell`, `LoopShell` or `LoopTertiaryShell` elements and pass them in. `WovenDialogueShell(_props)` (`woven-dialogue-shell.tsx:77`) ignores `defaultSurface`, so `/workbench` and `/pipeline` render the same dialogue surface as `/`. `woven-dialogue-route.test.tsx` and `loop-tertiary-routes.test.ts` assert this behaviour.
- **The legacy-interface link is dead.**
  - The shell builds `legacyHref` (`?legacy=1`) at `woven-dialogue-shell.tsx:384-388` and passes it on.
  - `navigator.tsx:119` voids it.
  - `ShellFrame` declares the prop (`shell-frame.tsx:56`) but never destructures it.
  - Nothing reads `?legacy`.
  - `electron/renderer-window-policy.ts:14` still names the navigator's "open legacy interface" link. That comment is stale.
- **Surface attribution is written but never shown.** `recordWovenSessionSurface` still runs (`woven-dialogue-shell.tsx:228-235`), but `navigator.tsx:118` voids `sessionSurfaces`. These have tests but no production caller:
  - `buildNavigatorSessionGroups`;
  - `NAVIGATOR_RECENT_SESSION_LIMIT`;
  - `toggleWovenNavigatorExpandedSurface`;
  - `readWovenWorkspaceSurface`;
  - the `navigatorExpandedSurfaces` field.
- **Skills browsing is disabled.**
  - `'skills'` is still a `WovenRightPanelView`.
  - `resolveRightPanelView` maps it to `workflows` (`woven-workspace-state.ts:67-68`).
  - The right panel has no Skills tab.
  - `MethodLibraryView` accepts a `view` prop but ignores it and keeps only `kind==='workflow'` (`method-library-view.tsx:112`).
  - This matches the Root AGENTS note that the App hides skill browsing for v3.0.0.
- **The legacy `ActivityShelf` is unmounted.** It is exported from the LIVE module `activity-shelf.tsx`, but only `woven-dialogue-controls.test.tsx` renders it. The live surfaces are `ActivityStrip` and `ActivityView`.
- **The CoordinationPanel header is unmounted.** Its standalone header, with the Session/Agents tabs, renders only when `embedded=false`, and the shell always passes `embedded` (`woven-dialogue-shell.tsx:1019`).
- **Retired persisted fields.** These are still sanitized and written, but no production component reads them:
  - `coordinationView` (`work|agents`); the shell keeps its own `session|agents` state and resets it to `agents` on load, per the comment at `:201`;
  - `activityHeight` and `activityCollapsed`;
  - `dialogueAnchorId`, `focusedArtifact`, `expandedObjectIds` and `contextReferences`;
  - `chatRung`.
- **TEST_ONLY modules:**
  - `work-projection.tsx`, the retired Work view. Its `contracts.ts` types `CoordinationWorkItem` and `CoordinationWorkClass` serve only this module.
  - `workflows-view.tsx` and `workflow-detail.tsx`, a plan-file browser over `/api/working-root/workflow`. That route stays live, but no UI consumes it.
- **Exported helpers with no production caller (tests only):**
  - `acceptGuardedReplayProjection`, `rejectGuardedReplayProjection`, and the lib `returnToPrimaryDialogue` in `guarded-session-selection.ts`. The shell defines its own `returnToPrimaryDialogue`.
  - `buildOperatorSessionProjection`; production uses `projectOperatorSession`.
  - `loadRecordedFirstOperatorMessages` and `searchRecordedSessionMessages`; production uses `createChatReplayReader` directly.

## 5. Method friction with §5.2

- **Module-level REACH is too coarse for UI components.** Several DISABLED rows sit in LIVE modules: the unmounted `ActivityShelf`, the CoordinationPanel header branch, and voided props. I tagged them `REACH=LIVE (module); STATE=DISABLED` and gave the evidence.
  - Proposal: allow `REACH=LIVE_MODULE_UNMOUNTED`, or state explicitly that `STATE=DISABLED` carries "imported but not rendered".
- **The TYPE-ONLY rule conflicts with the UNREACHED census field.** The census asks for a count of rows marked UNREACHED, but the TYPE-ONLY rule rewrites the pack's UNREACHED as `REACH=LIVE`. I counted the row because its Notes cite the pack status.
  - Proposal: have the census count `TYPE-ONLY` separately and keep `UNREACHED` for rows tagged `REACH=LEGACY_ONLY` under Addendum 1 item 4.
- **Shared test files.** `woven-dialogue-shell.test.tsx` covers most shell behaviours, so it appears on many rows. The CSV does not show which assertion covers which row.
  - Proposal: allow an optional `path#test-name` suffix in `CoveringTests`.
- **Cross-area entry points.** Some consumers sit outside the area: `app/layout.tsx`, `components/shell/theme-control.tsx`, `components/shell/chat-panel.tsx` and `components/shell/app-update-summary.tsx`. I put them in `EntryPoints`, mixed with symbols. The friction noted in R0 still applies.
- **PostReleaseBasis precheck.** A per-area "no touched ranges" flag in the pack would save every worker the same lookup.

## 6. Effort

- Files read:
  - all 23 area files, fully or in line ranges; the shell was read in full;
  - about 8 consumer files: the four pages, `layout.tsx`, the `shell-frame.tsx` props, the `renderer-window-policy.ts` header and `theme-control.tsx` by grep;
  - about 10 test files by targeted grep.
- The test map and coverage were computed with read-only greps and a scratchpad script.
- The context budget was comfortable, not tight.
