# Independent review return: frozen diff 19bca4930..02ffa62b0

Reviewer: fresh Fable 5.1 session (TASK, `software-code-review`), read-only, no authorship of the diff. Dispatched by HELP_HUMAN (this run) from `briefs/REVIEW_FROZEN_DIFF.md`. The report below is the reviewer's return, reproduced verbatim except for heading levels. The remediation record follows it.

## Reviewer report

### Verdict

FAIL for publication. One medium and two low actionable defects, all in product source added by this diff (`frontend/src/**`). Deterministic gates pass (typecheck clean; Vitest 2150 passed, 4 skipped), but the medium finding is not exercised by any test.

### Findings (by severity)

F-1 (Medium): runaway re-render loop between the shell and the chat panel whenever a Plan model exists and the file catalog is unavailable.
- `frontend/src/components/shell/chat-panel.tsx:1590-1599` (`planPanelModel` memoised over `fileCatalog`; effect publishes every new model via `onPlanPanelChange`), `src/components/woven-dialogue/woven-dialogue-shell.tsx:755,761` (`onPlanPanelChange={setPlanPanel}`, `fileCatalog={currentFileCatalog}`), contributing pre-existing cause `src/lib/workspace/use-conversation-file-catalog.ts:31` (`paths: catalog?.root === projectRoot ? catalog.paths : []` returns a fresh array on every render while the catalog is null or belongs to another root).
- Trigger: woven presentation; model non-null (Plan Mode selected, or any revision/clarification present); catalog null: on launch before `/api/working-root/tree` resolves, after every folder switch (including the new cross-folder chat open) until the new tree loads, and permanently when that fetch fails or reports a different root.
- Impact: new `[]` -> new model -> effect -> `setPlanPanel(newRef)` -> shell re-render -> `ChatPanel` (not memoised, rendered inline with fresh arrow props) re-renders -> new `[]` ... a continuous passive-effect update loop. Self-heals only when the catalog arrives; persists while the tree fetch fails. In dev React reports "Maximum update depth exceeded"; in production the renderer spins.
- Evidence: RUN_LOG 17:41Z records this exact class for the default params (hoisted to `NO_FILE_CATALOG`), but the shell's `[]` was not addressed. `woven-dialogue-shell.test.tsx` mocks `ChatPanel`; `chat-panel-*.test.tsx` never passes `fileCatalog`; no test covers the combination.
- Remediation: return a module-constant (or memoised) empty array from `useConversationFileCatalog`; additionally decouple `fileCatalog`/`onOpenFile` from the published model or compare before publishing. Add a host test that re-renders on `onPlanPanelChange` while passing a fresh array.

F-2 (Low): per-chat document context inherits whatever document is open when a chat with no remembered document is opened.
- `woven-dialogue-shell.tsx:578-596`.
- Trigger: document X open; select chat B with no `chatDocuments[B]`. Effect (a) restores nothing; effect (b) runs in the same commit with `openDocumentPath` still X and records `chatDocuments[B] = X`.
- Impact: B later restores X (and forces `rightPanelView: 'files'`) though the user never opened X in B; contradicts "document context per chat" (item 13). Test covers restore only.
- Remediation: record only on `openDocumentPath` transitions while `primarySessionId` is unchanged (ref-guard the session-change render), or clear the document when switching to a chat without a remembered one.

F-3 (Low): a running plan-execution record is settled as `unknown` when the resume attach never opens.
- `chat-panel.tsx:1147` (`settleRecoveredExecution(state.turnId, outcome.outcome ?? 'unknown')`); `observeTurn` returns `{ terminal: false, outcome: null, error }` when the first attach fails (chat-panel.tsx ~1003-1006) while the Runtime still owns the turn.
- Impact: the record leaves `running` permanently as `unknown`; the no-live-turn settle effect (chat-panel.tsx ~916-942) only touches `running` records, so the real outcome never reaches the Plan tab, and the tooltip claims "connection lost ... record does not show how this turn ended", which is false.
- Remediation: settle only when `outcome.terminal`; otherwise leave the record running for the log-based settle.

### Residual risks and missing verification (not confirmed defects)

Residual risks:
- R-1 `chat-panel.tsx:541` + `chat-draft.ts:114`: every session visited now persists a non-empty draft snapshot (permissionMode/interactionMode), one key per session, no eviction. Small (~150 B each) but not covered by the brief's "bounded growth" claim.
- R-2 `woven-dialogue-shell.tsx:532`: if the validated root differs from the indexed root (canonicalisation), the pending cross-folder open never resolves and the "Opening this chat..." note persists. Not observed; Runtime records `canonicalRoot` and the pre-existing canonicalTransition path suggests agreement.
- R-3 `woven-dialogue-shell.tsx:538`: a listing error in the target folder drops the pending open silently.
- R-4 Continuable running sessions: between resume and `getHarnessTurnState` resolving, Send is enabled. Runtime rejects a second turn with 409 `SESSION_TURN_IN_PROGRESS` (`chirality-runtime/packages/core/src/turn-coordinator.ts:113`, `daemon/src/turn-registry.ts:165`) and the panel restores the draft, so no double submission; the user would see an error instead of "Working".
- R-5 `chat-panel.tsx:1481`: the panel now re-renders on every harness event and derives activity per assistant message per render (bounded by `MAX_LIVE_HARNESS_EVENTS = 2000`).
- R-6 `woven-dialogue-shell.tsx:585`: restoring a remembered document forces the right panel to Files, leaving Plan/Activity.
- R-7 Governance: `ROOT-WORKFLOW-NAVIGATION-20260912.yaml` still pins `approved_source_sha` to the basis (re-pin before merge, as it says); WORK_GRAPH's contract text omits `group.order` (drift only). Diff is 89 files, brief says 90.
- R-8 `electron/main.ts:141` `appUpdateController` is assigned and cleared but never read.

Missing verification:
- No test of shell + real `ChatPanel` plan-model publication with the shell's `fileCatalog` (F-1).
- No component test that a resumed session restores unsent permission/interaction mode from the draft store and that a new chat resets to defaults (only the chat-draft round-trip is tested).
- No test for `settleRecoveredExecution` or the no-live-turn settle effect.
- No test for streaming follow / Jump to latest (`chat-jump-to-latest`, `onTranscriptScroll`, ResizeObserver); RUN_LOG says "covered by ... its tests" but none exists in the diff.
- No test for the account-row update dot / "update available" accessible name.
- No test of `TurnActivityDisclosure` rendered from live events inside `ChatPanel` (only the pure derivation and message placement).
- `main.ts` wiring (IPC registration, `sendAboutShowSignal`, `focusOrCreateMainWindow`, `resolveAppVersion`) untested beyond contract pins (consistent with prior practice).
- Sign-in ceremony not exercised live (owner constraint, recorded).

Security/privacy and contracts checked and found sound: fail-closed feed checker (no fetch without configured allowlisted https source, redirects refused, URL/credential scrubbing, no install/relaunch/fs/userData surface, contract pins present); IPC handlers keep `isAuthorizedSender`; sign-in opens through the existing window-open policy to `shell.openExternal`; wovenWorkspace v1 additions additive and tolerant, chat index and chat documents bounded at 500; draft key format unchanged; catalog partition verified 71 workflows = 9 core / 59 specialist / 3 superseded, `legacy` only on the three superseded, no skill carries navigation, six central unchanged. No credentials, tokens or e-mail addresses appear in UI strings or logs added by the diff.

### Checks run
- `npm run typecheck` (frontend): PASS (renderer and electron projects).
- `npx vitest run` (frontend, full): 212 files passed, 1 skipped; 2150 tests passed, 4 skipped; exit 0.
- Structural read of `workflows/index.json` (python): counts above.
- `git log/diff/show` over the frozen range; greps of Runtime turn guard, window-open policy, root validation, event buffer cap, test coverage.

### Coverage
Read the complete `git diff 19bca4930..02ffa62b0` for all 89 files (electron, src, tests, runtime, tools, workflows, docs/governance). Beyond the diff, read in full: `chat-panel.tsx` lines 1-1575 (the render region 1576-1969 read as diff hunks only), `chat-draft.ts`, the workspace-provider apply/choose functions, `use-conversation-file-catalog.ts`. For the other modified product files (`woven-dialogue-shell.tsx`, `navigator.tsx`, `right-panel.tsx`, `method-library-view.tsx`, `activity-shelf.tsx`, `hosted-bootstrap-controller/view.tsx`) I read the diff hunks with their context, not the unchanged remainder. `workflows/index.json` and `workflows/catalog.yaml` were verified structurally rather than line by line. No file was written; no userData, Codex home, identity or log file was opened.

## Remediation record (HELP_HUMAN, this run)

All three findings accepted and fixed; one further defect found while writing the F-2 test.

- F-1: `use-conversation-file-catalog.ts` returns a module-constant empty array (`NO_PATHS`) whenever no catalog for the current root exists, so the chat panel's memoised plan model and its publication are stable while the tree is loading or unavailable. Test: `conversation-file-navigation.test.tsx` asserts one identical empty catalog across re-renders and a root change while the tree fetch fails.
- F-2: `woven-dialogue-shell.tsx` records a document for a chat only when the open document changes while that chat stays active (a ref marks the render in which the primary session changed, and that render records nothing). A chat with no remembered document no longer inherits the document on screen. Test: `woven-dialogue-shell.test.tsx` "does not hand an open document to a chat that never had one, and records only documents opened in that chat".
- F-3: `chat-panel.tsx` calls `settleRecoveredExecution` only when the observation reached a terminal event. When the attach never opens, the record stays running and the no-live-turn effect settles it from the log later. Test: `chat-panel-turn-attach.test.tsx` "leaves a recovered plan execution running when the attach never opens, instead of settling it as unknown".
- Additional (found by the F-2 test): the launch-time last-chat restore effect returned early while a chat was already open without ever marking the restore as done, so `lastActiveChat` was never recorded for the rest of that window whenever a chat existed before the folder listing settled. The effect now marks the restore done when a chat is already open (there is nothing to restore over it) and recording begins. The new shell test asserts the open chat is recorded before and after continuing another chat.
- The shell test's `ChatPanel` mock now reports the resumed session through `onActiveSessionChange`, as the real panel does.

Residual risks R-1 to R-8 are noted, not acted on in this tranche: R-7's file count is corrected in the brief; the `approved_source_sha` re-pin happens before merge as planned; R-8 (unused `appUpdateController` in `main.ts`) is left for a later cleanup rather than widening the Electron diff.

Gates after remediation: `npm run typecheck` clean; `npx vitest run` 212 files passed, 1 skipped; 2153 tests passed, 4 skipped. A second fresh reviewer is dispatched over the new frozen range, since product source changed (see `briefs/REVIEW_FROZEN_DIFF_2.md` and `returns/REVIEW_RETURN_2.md`).
