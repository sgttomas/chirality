# Update path: preservation of user work (acceptance checks)

Run: APP_V3_UI_REFINEMENT_20260912, item 17 of the appended brief.
Current basis: PR #776, source `26657ff9080efbba7ec1e71e6f1d08731462de0f`.
Public release discovery and user-selected browser downloads; earlier TASK B
checks and the original no-feed behavior remain recorded in the run log.

## What the update path is

Chirality checks the public `sgttomas/chirality-app` GitHub releases and, when a
newer stable version is published,
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
| Shared agent instructions | App-owned `instructions/AGENTS.md`, outside the bundle | Settings opens the same customization after an update; Restore default retains a backup. |

The last entry is covered by the dedicated product-instructions store tests;
it is not part of the renderer-storage snapshot. The earlier A2 build predates
that feature, so the first upgrade seeds the product default when no copy exists.

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
3. `src/__tests__/components/app-update-controls.test.tsx` checks the manual path:
   availability is "available to download", the Download title and the About
   note say the user quits, installs and reopens, no state reads as
   "updated" or "installed", and a running-work warning appears while a turn
   is live in the window (`data-update-note="running-work"`).
4. `src/__tests__/electron/app-update.test.ts` covers the fixed public source,
   release identity, version ordering, bounded failures and destination
   validation. Checking does not open a browser; the explicit Download action
   does. No comment wording is a merge condition.
5. `src/__tests__/electron/product-instructions.test.ts` covers seeding once,
   preserving edits through a new default version, safe restoration with a
   backup, and source/package path selection with distinct product fixtures.

## Manual acceptance (owner, on a packaged candidate)

Preconditions: both candidate DMGs are preserved. The old A2 source is
`388de6973`, installer
`/Users/ryan/.claude/chirality-build-a2-out/Chirality-3.0.0-rc.1-arm64.dmg`.
The replacement source is `26657ff90`, installer
`/Users/ryan/.claude/chirality-build-ui-recovery-20260912-out/Chirality-3.0.0-rc.1-arm64.dmg`.
The replacement build is complete and signed. Its pre-staple DMG SHA-256 is
`d3d32be65e515d48035fd923b08870a30f3cde2f42d5c04558e2153746408caf`;
Gatekeeper remains pending owner notarization/stapling.
Both use version `3.0.0-rc.1`, so record their source and artifact hashes too.
This is a manual install-over comparison, not a public release or an offered
version upgrade. Owner notarization/stapling and guarded agent-assisted launch
restrictions remain in force. Do not use the R17 installation or profile.

1. In the old A2 installation, note About Chirality and its version. That build
   has no release source. After installing the replacement, Check for Updates
   should consult the public release page and report the result without
   installing anything. At source verification, public v2.0.0 was older than
   this candidate, so Up to date was the expected result.
2. Before quitting: open two chats in two different folders, type a draft
   (with an attachment and a selected workflow) in one and leave it unsent,
   execute a plan revision in the other, pin a chat, set Appearance, and note
   the folder marked current. In the renderer console record
   `snapshotRendererUserData(localStorage)` from
   `src/lib/shell/user-data-inventory.ts` (a dev-tools call in the packaged
   build is not available; use the observables instead).
3. If Download is offered, confirm the running-work note appears while a turn
   is live. With no offered download, leave that branch unverified. Finish or
   explicitly stop work before quitting; window closure and application quit
   have different effects.
4. Quit Chirality. Install the replacement over the A2 application and reopen
   with the same A2 profile. A fresh profile does not test preservation. Do not
   inspect or copy credentials.
5. Check every observable in the inventory table. Each must hold. In
   particular: the chat list is complete in both folders; the draft is back in
   its composer; the executed revision reads as executed with its attempt;
   the current folder is unchanged; the account row reads Signed in.
6. Record the outcome in RUN_LOG.md with both source revisions, artifact hashes
   and version strings. Any
   observable that fails blocks the candidate.

## Not covered, by design

- The public source now exists. A download is offered only for a newer stable
  release; no release was created to manufacture that branch of the test.
- Same-build restart evidence is not evidence of install-over preservation.
- No owner observations have yet completed this manual checklist.
- The Runtime data schema is the Runtime loop's contract. A future Runtime
  change that migrates session records must carry its own preservation
  evidence; this checklist only requires that the App never touches the store
  on the update path.
