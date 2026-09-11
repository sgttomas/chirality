# RETURN — C_RENDERER_SURFACES (Type 2 TASK, Author)

Worktree: `/Users/ryan/dev/chirality/.claude/worktrees/owner-alignment-inspection-db4335` (branch `claude/chirality-v3-mvp-trial-ab05cb`).
All paths below are relative to `projects/chirality-app-dev/frontend/`. Nothing committed, stashed, installed, or built.

## Criterion → change

### A. Window title
- `src/app/layout.tsx:57` — `metadata.title` `'Chirality Workflow Shell'` → `'Chirality'`.

### B. "Who is working" → "Agents"
- `src/components/woven-dialogue/right-panel.tsx:116` (session breadcrumb button) and `:126` (tab label). Tab `role`/`aria-controls`/`data-view="agents"` unchanged.
- Grep of `src/` and `electron/` shows no other user-visible occurrence. Tests: `woven-dialogue-shell.test.tsx:186-191`, `woven-right-panel.test.tsx:29,90`.

### C. User menu
- `src/components/shell/account-popover.tsx` — now renders exactly: account/sign-in group (`HostedBootstrapView compact` when hosted, `:28`; non-hosted OpenAI account group `:28-35`), then `Settings…` `:38`, `Appearance` `:39`, `About Chirality` `:40` (version only, "· Opt-in Preview" dropped). "Shared runtime" section, both `DaemonQuickControl` uses, and the non-hosted "Local model" section removed. Non-hosted "Preview account · simulated state" line removed (the "Account service unavailable in this build." fallback stays).
- `src/components/shell/account-settings-controls.tsx` — `DaemonQuickControl` deleted (its only consumer was the popover); `accountTitle` and `LocalModelStatus` (non-hosted row subtitle) kept.
- `runtime` prop kept on `AccountPopoverProps` (`:17`) because `AccountRow`/`ShellFrame` share one controller between popover and Settings; it is unused in the popover.

### D. Project access dropdown
- `src/components/shell/chat-panel.tsx` — both `<select>`s (non-woven header `Operator mode` label + woven context row) removed. `OPERATOR_MODES`, `DEFAULT_OPERATOR_MODE`, `PLAIN_MODE_LABELS`, `isSupportedOperatorMode` stay; `isSupportedOperatorMode` now reads `OPERATOR_MODES` (`:95`) so the registry remains the single source. `operatorMode` state is still sent per turn as `permissionMode`/`opts.mode` (unchanged lines ~644/785/805).
- Unsupported stored mode: two-paragraph alert → one line `:1232-1234`: `<p class="chat-runtime-error" role="alert">This recorded chat used {label}, which is no longer supported. [Continue with Project access]</p>`. The button sets `DEFAULT_OPERATOR_MODE`; Send stays disabled until then. No new permission modes.
- Interaction mode (Chat / Plan Mode) selector untouched `:1324-1326`.

### E. Redundant labels / banners / telemetry
1. `chat-panel.tsx:1325` — "Human trial — empirical qualification pending" span removed; "Plan Mode unavailable: {reason}" is now the `title` of the disabled `Plan Mode` option. No inline span remains.
2. `src/components/settings/hosted-bootstrap-view.tsx` — status line (`:42`) + single action per state kept. Explanations moved to `title` on the action (`:25-27,29-34` constants; `:44,46,48-49,51`): setup ("…one minimal chirality.project.json…"), consent ("Allow this project to contact…"), pending ("Complete sign-in with OpenAI…" on link and Cancel), signed-in readiness text on Sign out. Non-compact hint paragraph "Connect this project to Codex…" removed; `<h3>OpenAI account</h3>` kept as the Settings group heading. `role="alert"` lines kept (`:53,57`); "The previous sign-in was cancelled." kept (short state, `:54`). "Use this folder" button kept for the fallback path.
3. `src/components/shell/folder-select.tsx:38-45` — "Choose a folder before sending a message." paragraph dropped; `Choose folder…` is first and default-styled (hover title explains when the native picker is unavailable); Known folders select follows; manual path input + `Use folder` (`button-muted`) sit inside `<details class="chat-folder-path"><summary>Enter a path…</summary>`. Error `role="alert"` kept.
4. `src/components/settings/runtime-settings.tsx:42-65,76-78,176` — visible label is `Running` / `Installed and stopped` / …; PID and `startedAt` go into `title` on the `.runtime-status` span (`data-running` attr kept for existing CSS). Install/Start/Stop/Refresh/Uninstall row wrapped in `<details class="runtime-service">` (collapsed by default) whose summary reads `Runtime service · {status}`. Heading "Shared Runtime" → "Runtime". Non-desktop fallback still shows status + "Runtime controls are available only in Chirality Desktop.". Button labels unchanged. `settings-view.module.css` gained three small `.runtime-service` rules and lost the unused `.footer` rule.
5. `src/components/settings/settings-view.tsx` — footer paragraph removed; "Preview account · simulated state…" paragraph removed. Groups: account (`:29`), folder (non-hosted, `:30`), runtime (`:31`, disclosure inside), local-model (non-hosted, `:32`), api-keys (`:33`), appearance (`:34`).
6. `src/components/shell/shell-frame.tsx:250` — visible `runtime` key span removed (button already has `aria-label="… runtime connection; reported status: …"`); `:270` root chip key is now `visually-hidden` text "Working root" so the summary's accessible name still names the value; `title` unchanged.
7. `account-settings-controls.tsx` — "oMLX server status unknown." no longer renders anywhere in hosted builds (it lived only in the deleted `DaemonQuickControl`). Non-hosted Settings "Local model" group (`settings-view.tsx:32`) still shows it — non-hosted only, per the criterion.

### F. Native attachment picker
- New `src/lib/shell/native-attachments.ts` — `getNativeAttachmentBridge()` returns `{ selectFiles }` only when `typeof window.chirality?.attachments?.selectFiles === 'function'` (cast-based, so it does not depend on the concurrently edited `src/types/chirality-window.d.ts`, whose new `attachments` declaration matches this shape).
- `chat-panel.tsx:20` import; `:317` `attachmentPickPending` state; `:1072-1088` `pickAttachments()`: bridge present → `selectFiles({ projectRoot })`, `{cancelled:false}` → `paths.map(buildUiAttachment)` merged with `mergeAttachments`; `{cancelled:true, error}` → `setNativeFolderError(error)` (existing `role="alert"` at `:1328`); plain cancel → silent; thrown error → alert; bridge absent → `setPickerOpen(true)` (existing in-app `FilePicker`). Attach button `:1299` calls it and is disabled while a pick is pending.

## Deliberately kept
- `OPERATOR_MODES`/`DEFAULT_OPERATOR_MODE`/`isSupportedOperatorMode`/`PLAIN_MODE_LABELS` (owner instruction; labels feed the one-line error).
- `runtime` prop on `AccountPopoverProps` (shared controller with Settings; removing it would ripple into `account-row.tsx`/`shell-frame.tsx` for no user-visible gain).
- `LocalModelStatus` "Local model · unknown" in the non-hosted account row and the non-hosted Settings "Local model" group (criterion scoped E7 to hosted builds).
- Non-hosted "Account service unavailable in this build." and "The previous sign-in was cancelled." (short state text, not banners).
- All `role="alert"` errors; folder-select `Known folders` select.
- `src/app/globals.css` untouched (not in write scope; only module CSS next to components changed).

## Tests
Command prefix: `export PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin; cd $F` with `F=…/projects/chirality-app-dev/frontend`.

- Touched/added files, run together:
  `node node_modules/vitest/vitest.mjs run src/__tests__/components/account-presentation.test.tsx src/__tests__/components/hosted-bootstrap.test.tsx src/__tests__/components/runtime-settings.test.ts src/__tests__/components/shell-frame-runtime-connectivity.test.tsx src/__tests__/components/shell-frame.test.tsx src/__tests__/components/chat-panel-folder-binding.test.tsx src/__tests__/components/chat-panel-native-attachments.test.tsx src/__tests__/components/folder-select.test.tsx src/__tests__/components/woven-dialogue-shell.test.tsx src/__tests__/components/woven-right-panel.test.tsx`
  → 10 files, 139 tests passed.
- Full component suite: `node node_modules/vitest/vitest.mjs run src/__tests__/components` → **45 files passed, 410 tests passed**.
- Typecheck: `node node_modules/typescript/bin/tsc --noEmit -p tsconfig.json` → one error, not in my scope: `src/__tests__/api/harness/turn-route-attachments.test.ts(128,33) TS2493` (untracked file from the attachment-IPC worker). Earlier in the run a `hosted-bootstrap-controller.tsx(176)` error appeared and then cleared as that worker progressed. Everything in my write scope typechecks.

Test changes:
- New: `chat-panel-native-attachments.test.tsx` (3 tests: native bridge path scoped to projectRoot + merge; error/cancel/throw handling; fallback to in-app FilePicker when bridge absent), `folder-select.test.tsx` (2 tests: ordering/disclosure/actions; disabled-picker hover + alert).
- Updated: `account-presentation.test.tsx` (popover contents exactly account/Settings/Appearance/About; Runtime heading + disclosure in hosted Settings; no daemon switch in popover), `hosted-bootstrap.test.tsx` (explanations asserted on `title`, no paragraphs besides the status line), `runtime-settings.test.ts` (PID only in `title`, collapsed `runtime-service`), `shell-frame-runtime-connectivity.test.tsx` (chip text without `runtime` key), `chat-panel-folder-binding.test.tsx` (no operator select; one-line alert + "Continue with Project access"; no "Human trial" text), `woven-dialogue-shell.test.tsx` / `woven-right-panel.test.tsx` ("Agents" label).
- `shell-frame.test.tsx` and `runtime-reconnect-refresh.test.tsx`: added `useWorkspaceSelection: () => null` to the `workspace-provider` mock — required because the concurrently edited `hosted-bootstrap-controller.tsx` now calls that hook; without it those two files fail for reasons outside this task.

## Not done / caveats
- No browser/screenshot pass (no dev server or build permitted here); acceptance is by render tests only. Recommend a quick visual check of: the `Runtime service ·` summary spacing, the `Enter a path…` nested disclosure inside `.chat-folder-menu`, and the one-line permission alert wrapping with its inline button.
- `hosted-bootstrap.test.tsx` was being edited concurrently by the controller worker; my edits are targeted string replacements and coexisted with theirs at the time of the final green run, but that file should be re-run after they finish.
- `src/types/chirality-window.d.ts` was not touched (other worker); the accessor casts instead.
