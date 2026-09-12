# Update path: preservation of user work (acceptance checks)

Run: APP_V3_UI_REFINEMENT_20260912, item 17 of the appended brief.
Basis: the update feature delivered under TASK B (fail-closed feed checker,
Check for Updates…, Download opens the installer in the system browser).

## What the update path is

Chirality checks a release feed and, when a newer version is published,
offers a Download button that opens the installer in the browser. Chirality
does not download in the background, does not install, and does not relaunch.
The user quits Chirality, installs the downloaded build over the old one, and
reopens it. Because the application bundle is replaced and nothing else is,
preservation of user work means: nothing the user relies on lives inside the
bundle, and the new build reads the same stores the old one wrote.

The renderer describes this path in those words (Download button title, the
note under it in the About panel, and the About panel when nothing is
available) and never says or implies that the application has updated.

## Inventory of user work

The inventory is code: `src/lib/shell/user-data-inventory.ts`
(`USER_DATA_INVENTORY`). Each entry names the store, the location in the
user's terms, the renderer-storage key prefix where one applies, and the
observable that proves the entry survived.

| Entry | Store | Observable after reopening |
|---|---|---|
| Chats and their history | Runtime data (userData/runtime, per project) | Every chat listed before is listed after, with its transcript. |
| Unsent drafts and attachments | Renderer storage `chirality.chatDraft.v1:` | The draft is back in the composer of the same chat, with attachments and selected workflows. |
| Per-chat folder bindings | Renderer storage `chirality.wovenWorkspace.v1` | Each chat opens in its own folder; the navigator groups by folder as before. |
| Per-chat model, reasoning, role and permission settings | Renderer storage (draft record) and the chat record in the Runtime | Reopening a chat restores its own selections; new-chat defaults unchanged. |
| Plan revision execution records | Renderer storage `chirality.planExecutions.v1:` | An executed revision still reads as executed with its attempts. |
| Saved project workflows | `.chirality/workflows` in the project folder | Project Specific workflows listed unchanged. |
| Saved personal workflows | `.chirality/workflows` in the home folder | Personal workflows listed unchanged. |
| Application preferences | Renderer storage `chirality.` | Appearance, layout, pinned and grouped chats, folder for new chats as before. |
| Codex sign-in | Codex home, custodied by Codex | Account row reads Signed in without a new ceremony. |

## Automated checks (in the frontend suite)

1. `src/__tests__/contract-pins.test.ts` pins `electron/app-update.ts` to
   contain no Electron, filesystem, child-process, `autoUpdater`,
   `quitAndInstall`, `relaunch` or `userData` surface, and `electron/main.ts`
   to contain no `quitAndInstall` and no `app.relaunch(`. The update code
   therefore cannot replace, migrate or clear any store in the inventory.
2. `src/__tests__/lib/user-data-inventory.test.ts` keeps the inventory's
   renderer-storage prefixes aligned with the modules that write them
   (`chat-draft.ts`, `plan-executions.ts`, `woven-workspace-state.ts`), and
   checks the snapshot and comparison helpers used by the manual check below.
3. `src/__tests__/components/app-update-controls.test.tsx` pins the wording:
   availability is "available to download", the Download title and the About
   note say the user quits, installs and reopens, no state reads as
   "updated" or "installed", and a running-work warning appears while a turn
   is live in the window (`data-update-note="running-work"`).
4. `src/__tests__/electron/app-update.test.ts` (TASK B) covers the fail-closed
   checker: no request without a configured, allowlisted source; opening the
   download hands an https URL to the system browser and nothing else.

## Manual acceptance (owner, on a packaged candidate)

Preconditions: a signed candidate DMG of the newer version and the currently
installed build. No release source is configured today, so step 1 is
exercised through the About panel wording and steps 2 to 6 through a manual
install of the candidate over the installed build.

1. Open About Chirality. Confirm the text says the download opens an
   installer in the browser and that Chirality does not install updates. With
   no release source the panel says so; Check for Updates… ends in "No
   release source is configured for this build." and nothing else changes.
2. Before quitting: open two chats in two different folders, type a draft
   (with an attachment and a selected workflow) in one and leave it unsent,
   execute a plan revision in the other, pin a chat, set Appearance, and note
   the folder marked current. In the renderer console record
   `snapshotRendererUserData(localStorage)` from
   `src/lib/shell/user-data-inventory.ts` (a dev-tools call in the packaged
   build is not available; use the observables instead).
3. If a turn is running, confirm the About panel and the account menu show
   the running-work note under Download. Wait for the turn to finish or stop
   it: quitting stops running turns, and the update path says so.
4. Quit Chirality. Install the candidate over the installed build. Reopen.
5. Check every observable in the inventory table. Each must hold. In
   particular: the chat list is complete in both folders; the draft is back in
   its composer; the executed revision reads as executed with its attempt;
   the current folder is unchanged; the account row reads Signed in.
6. Record the outcome in RUN_LOG.md with the two version strings. Any
   observable that fails blocks the candidate.

## Not covered, by design

- No release source exists yet (TASK B return, missing infrastructure 1 to
  5). Until the owner supplies the feed, the checker fails closed and the
  Download button never appears in a shipped build; the checks above exercise
  the wording and the manual install path.
- The Runtime data schema is the Runtime loop's contract. A future Runtime
  change that migrates session records must carry its own preservation
  evidence; this checklist only requires that the App never touches the store
  on the update path.
