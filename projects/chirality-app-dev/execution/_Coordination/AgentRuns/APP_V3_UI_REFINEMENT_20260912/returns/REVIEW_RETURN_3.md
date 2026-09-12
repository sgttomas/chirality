# Third independent review return: frozen diff 19bca4930..07f222a41, then candidate 51faa0a12

Reviewer: fresh Fable 5.1 session (TASK, `software-code-review`), read-only, no authorship. Dispatched from `briefs/REVIEW_FROZEN_DIFF_3.md`. The initial report over 07f222a41 and the updated verdict over the test-only delta to 51faa0a12 are reproduced verbatim except for heading levels; the remediation record sits between them.

## Initial report (07f222a41)

### Verdict

FAIL for publication under the App AGENTS.md independent-review rule. One actionable finding (Low). Product source across the range, including both remediations in 07f222a41 and the Specialist collapse, was found correct; the finding concerns a regression test that does not exercise the failure condition it claims to pin.

### Findings (by severity)

Finding 1 (Low, test-coverage): the Finding 2 regression test passes on the pre-fix code.

- File: `projects/chirality-app-dev/frontend/src/__tests__/components/woven-dialogue-shell.test.tsx:716-742` ("does not attribute a document opened while no chat was active to the chat resumed afterwards"); fix under test at `src/components/woven-dialogue/woven-dialogue-shell.tsx:616-623`.
- Triggering condition: the chat resumed at the end of the test (`primary`) already has a remembered document (`docs/SPEC.md`, recorded at line 726). The defect fixed in 07f222a41 only manifests for a chat with no remembered document (or shows up as a transient write).
- Evidence (effect trace on the pre-fix record effect, `git show 07f222a41`: `if (!stateHydrated || !primarySessionId) return;` before the ref update, so the ref stayed `'primary'` through the no-chat interval): on resume, the restore effect (`documentSessionRef`, lines 598-607) queues `openDocumentPath = 'docs/SPEC.md'`; in the same commit the pre-fix record effect sees `sessionChanged === false` and queues `chatDocuments.primary = 'docs/TYPES.md'`. Next render `openDocumentPath` is `SPEC.md`, the record effect re-runs and overwrites the entry back to `SPEC.md`. The assertions at 739-740 read only the last `persist` call and `openDocumentPath`, both of which end as `SPEC.md` pre-fix. The wrong value exists only in an intermediate persisted write, which the test never inspects.
- Concrete impact: the fix is correct but unguarded; a future regression to the old ordering (ref updated after the `!primarySessionId` return) would not be caught. Not a runtime defect.
- Remediation direction: either resume a chat with no remembered document at the end (e.g. resume `recorded` after the no-chat interval and assert `chatDocuments` has no `recorded` key), or additionally assert that no persisted write ever mapped `primary` to `docs/TYPES.md` (`persist.mock.calls.every(...)`). I could not run the pre-fix code empirically under the no-write rule; the finding rests on the effect-ordering trace above, which I re-verified against the current file and the commit diff.

No other actionable findings. In particular, verified in 07f222a41:

- Finding 1 fix (cross-folder open routed through New chat): `openChatInFolder` guards `streaming || folderSelectionPending`; a locked binding (`Boolean(conversationBinding) || isRunning`, chat-panel.tsx:628-630) sets `pendingFolderChat.awaitingNewChat` and bumps `newChatRequest`; the panel's New chat effect reports `onNewChatSettled(false)` on running/pending or a declined confirm and `(true)` only after `resetConversationRef.current()`; `newChatSeen` initialised from the prop so a mount with a non-zero counter never fires; the pending effect ignores `awaitingNewChat`; `handleNewChatSettled(false)` drops pending and the notice, `(true)` calls `switchToFolderChat`. The three shell tests discriminate pre-fix behaviour (pre-fix: `newChatRequests` 0; `applyProjectRoot` called on decline; `folderLocked` stuck true on the not-listed branch). The chat-panel test pins declined to false with draft kept and accepted to true with draft cleared.
- Specialist collapse: `<details open={query ? true : undefined}>` (uncontrolled when idle, forced open during search), count in summary; test asserts `open` undefined with counts `['1','2']` then `[true]` after searching `pdf`. CSS hides the marker and adds the expand markers.

### Residual risks and missing verification (not defects)

- R-A: `globals.css:4605` `summary:focus-visible { outline: none }` leaves keyboard focus on Specialist category headers indicated by the h4 colour change only (line 4604); low-contrast focus indication.
- R-B: declining the New chat confirmation during a cross-folder open deletes any pre-existing notice for that folder (`handleNewChatSettled` deletes `folderNotices[expectedRoot]` on `!started`).
- R-C: an unbound chat with an unsent draft switches folders directly without a confirm (pre-existing draft semantics; not changed by this range).
- R-D: `appUpdateController` in `electron/main.ts` is assigned but never read after wiring (prior R-8 stands).
- R-E: tranche manifest `approved_source_sha` still pins the basis 19bca4930; its own note requires re-pinning to the reviewed candidate before merge.
- R-F: `verify-instruction-root-integrity.test.ts` timed out once under full-suite load (see checks); outside the diff.
- Prior residual risks R-1..R-7 from REVIEW_RETURN.md / REVIEW_RETURN_2.md stand where applicable; no live App verification was performed by this review (prohibited).

### Checks run

- `npm run typecheck` (frontend): PASS.
- `npx vitest run` (frontend, full): 2157 passed, 4 skipped, 1 failure: `src/__tests__/scripts/verify-instruction-root-integrity.test.ts` timed out at 5000 ms while typecheck ran concurrently; rerun alone: 8 passed in 885 ms (load flake, file not in the diff).
- Structural check of `workflows/index.json` (python, read-only): 71 workflows, 8 skills; categories core 9 / specialist 59 / superseded 3; every workflow carries `navigation`, no skill does; `legacy` exactly on the three superseded; `supersededBy` targets exist and are non-superseded; core order 0-8 with the three display names; eight specialist groups with contiguous 0-based orders; `centralWorkflowNames` unchanged.
- `git show 07f222a41`, `git diff 19bca4930..07f222a41` (per file), `git log`: read-only.

### Coverage

I read the whole diff: every product-source file under `frontend/src/**` (outside `__tests__`) and `frontend/electron/**` in full, every changed test file, the Runtime contract/core/test files, `tools/validation/build_workflow_index.py` and `test_workflow_catalog.py`, `workflows/catalog.schema.json`, and all governance/docs records (RUN_LOG, WORK_GRAPH, UPDATE_PRESERVATION_ACCEPTANCE, PROMOTED_WORKFLOW_ASSUMPTIONS, tranche manifest, both notices, TASK_A/TASK_B briefs and returns, REVIEW_FROZEN_DIFF(_2/_3), REVIEW_RETURN(_2)); docs were found consistent with the code (counts, test totals, fix descriptions). Files not read line by line: `workflows/index.json` and `workflows/catalog.yaml` (generated/data; verified structurally as above instead). No files were written; no repository-writing commands were run; nothing under userData, Codex home, or runtime session directories was read; no e-mail address appears in this return.

## Remediation record (HELP_HUMAN, this run)

Finding 1 (Low) accepted: commit 51faa0a12 adds to the test the assertion that no persisted write ever mapped `primary` to `docs/TYPES.md`, so the transient pre-fix write fails it. No product source changed (`git diff 07f222a41..51faa0a12 --stat`: the test file and the third brief). The same reviewer session, which had no authorship of the change, was asked to verify the delta against its own effect trace and return a verdict for the candidate.

## Updated verdict (candidate 51faa0a12, `git diff 19bca4930..51faa0a12`)

### Verdict

PASS for publication under the App AGENTS.md independent-review rule. No actionable finding remains. Coverage: my full-range read of `19bca4930..07f222a41` (95 files, reported above) plus the delta `07f222a41..51faa0a12` verified below covers the candidate.

### Findings

None.

Delta verification:

- `git show 51faa0a12 --stat` and `git diff 07f222a41..51faa0a12 --stat`: exactly two files, 47 insertions, 0 deletions: `src/__tests__/components/woven-dialogue-shell.test.tsx` (+2 lines) and `briefs/REVIEW_FROZEN_DIFF_3.md` (new, record only). `git log 07f222a41..51faa0a12` shows the single commit. No product source changed.
- The added assertion (`persist.mock.calls.every(call => (JSON.parse(call[1]).chatDocuments ?? {}).primary !== 'docs/TYPES.md')`) discriminates the pre-fix ordering per my effect trace: pre-fix, the resume render commits `openDocumentPath = 'docs/SPEC.md'` (restore effect) together with `chatDocuments.primary = 'docs/TYPES.md'` (record effect, ref still `'primary'`); the persist effect at `woven-dialogue-shell.tsx:187-192` runs on every committed `workspaceState` change with no debounce (and the test stubs `requestAnimationFrame` as synchronous), so that intermediate state reaches `persist` as a call whose `chatDocuments.primary` is `'docs/TYPES.md'`, making `every(...)` false. With the fix the ref follows the chat through the no-chat interval, `sessionChanged` is true on the resume render, no such write occurs, and the assertion holds. Finding 1 of my previous return is therefore remediated.

### Residual risks and missing verification (unchanged from the previous return)

- R-A: `globals.css:4605` `summary:focus-visible { outline: none }` leaves keyboard focus on Specialist category headers indicated by colour change only.
- R-B: declining the New chat confirmation during a cross-folder open removes any pre-existing notice for that folder.
- R-C: an unbound chat with an unsent draft switches folders without a confirm (pre-existing semantics).
- R-D: `appUpdateController` in `electron/main.ts` assigned but never read (prior R-8).
- R-E: tranche manifest `approved_source_sha` still pins the basis; its own note requires re-pinning to the reviewed candidate (now 51faa0a12) before merge.
- R-F: `verify-instruction-root-integrity.test.ts` timed out once under full-suite load; passes alone; outside the diff.
- Prior R-1..R-7 stand where applicable; no live App verification was performed by this review.

### Checks run

- `git show 51faa0a12`, `git diff 07f222a41..51faa0a12 --stat`, `git log 07f222a41..51faa0a12`: read-only; two files as stated.
- `npx vitest run src/__tests__/components/woven-dialogue-shell.test.tsx` (frontend, on 51faa0a12): 28 passed in 797 ms.
- Previously on 07f222a41 (product source identical to 51faa0a12): `npm run typecheck` PASS; full `npx vitest run` 2157 passed, 4 skipped, 1 load-induced timeout (`verify-instruction-root-integrity`, 8 passed on isolated rerun); structural check of `workflows/index.json` (71/9/59/3, legacy only on the three superseded, contiguous orders, skills without navigation).

### Coverage

Whole diff read: every product-source file under `frontend/src/**` (outside `__tests__`) and `frontend/electron/**` in full, every changed test file including the two-line delta, the Runtime contract/core/test files, the validation tooling and catalog schema, and all governance and docs records including the new `REVIEW_FROZEN_DIFF_3.md`. Not read line by line: `workflows/index.json` and `workflows/catalog.yaml` (generated/data, verified structurally). No files written; no repository-writing commands; nothing under userData, Codex home, or runtime session directories read; no e-mail address appears in this return.
