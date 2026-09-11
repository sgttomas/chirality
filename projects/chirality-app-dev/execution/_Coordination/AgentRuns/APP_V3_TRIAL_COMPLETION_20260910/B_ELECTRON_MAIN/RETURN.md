# RETURN — B_ELECTRON_MAIN (Type 2 / Author)

Worktree: `/Users/ryan/dev/chirality/.claude/worktrees/owner-alignment-inspection-db4335`
(branch `claude/chirality-v3-mvp-trial-ab05cb`). No commits, no stash, no
installs, no packaged build, no launchctl against real services.

## Design

### 1. Automatic runtime start (`electron/runtime-autostart.ts`, pure)

`ensureRuntimeDaemonAutostart(deps)` never throws and returns a discriminated
outcome. Decision matrix over `lifecycle.status()`:

| installed | loaded | plist program | action |
|---|---|---|---|
| no | – | – | `install(exe)` then `start()` -> `installed-and-started` |
| yes | no | = `app.getPath('exe')` | `start()` -> `started` |
| yes | yes | = exe | nothing -> `skipped/already-loaded` |
| yes | any | != exe | **refused** (`foreign-executable`), no install, no start |
| yes | any | unparseable / unreadable | `failed/inspect`, no install, no start |
| – | – | `status()`/`install()`/`start()` throws | `failed/<stage>`, logged |

Packaged-only (`packaged: app.isPackaged`); `CHIRALITY_SKIP_RUNTIME_AUTOSTART=1`
opts out (mirrors `CHIRALITY_SKIP_CLI_LAUNCHER` for verification runs).

Foreign-plist refusal: `@chirality/runtime-cli` `LaunchAgentManager.install()`
overwrites the plist unconditionally and has no foreign check of its own, so the
check is implemented here. `readLaunchAgentProgramPath(plist)` takes the first
`ProgramArguments` `<string>` (XML-unescaped) and compares `path.resolve` of
both sides. Autostart never calls `install()` for an already-installed job, so
it can never overwrite a plist.

Log events via `desktopLogger`: `runtime.autostart.status`,
`runtime.autostart.installed`, `runtime.autostart.started`,
`runtime.autostart.skipped`, `runtime.autostart.refused_foreign_executable`
(level `error`, carries `installedExecutable` and `desktopExecutable` for a
later UI surface), `runtime.autostart.failed` (level `error`, `{stage, error}`),
and `runtime.autostart.outcome` (the returned object).

Wiring in `electron/main.ts` `initializeGui()`: the lifecycle from
`createDesktopDaemonLifecycle()` is now created once (`daemonLifecycle`) right
after `await bindingSupervisor.start()`, autostart runs against it, and the same
instance is passed to `registerRuntimeControlHandlers` — so autostart and the
manual Settings controls address the same job with the same posture. When the
outcome is `installed-and-started` or `started`, `void bindingSupervisor.refreshNow()`
is fired. `readInstalledPlist` is `readFile(daemonLifecycle.plistPath)` with
errors mapped to `undefined`; `createDesktopDaemonLifecycle()`'s return type was
widened to `RuntimeDaemonLifecycle & { readonly plistPath: string }`
(`LaunchAgentManager` already exposes it).

Posture compatibility: the lifecycle is built by the unchanged
`createDesktopDaemonLifecycle()`, which reads
`resolveDesktopDaemonPosture(process.env, app.getPath('userData'))` — after
`applyUserDataOverride()` has applied `CHIRALITY_USER_DATA`. A trial run with
`CHIRALITY_USER_DATA` therefore installs the job for that userData with the
posture-pinned environment, and the label is `com.chirality.runtime` unless
`CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL` overrides it. The `~/.local/bin/chirality`
launcher (`cli-launcher.ts`) is untouched and still exports the same
`daemonPostureEnvironment(posture)` values, so `chirality daemon *` and autostart
render/address the identical job.

Manual IPC controls (`chirality:runtime-daemon-control` install/start/stop/
status/uninstall) are unchanged.

### 2. Folder picker (`SELECT_DIRECTORY_CHANNEL`)

`dialog.showOpenDialog({ title: 'Choose a project folder', buttonLabel: 'Use this folder',
message: 'Chirality will work in this folder and add a chirality.project.json file if one is missing.',
properties: ['openDirectory', 'createDirectory'] })`. Return shape unchanged
(`{cancelled:true, error?}` | `{cancelled:false, path}`).

### 3. Native attachment picker

- `electron/attachment-ipc-contract.ts`: `ATTACHMENT_SELECT_FILES_CHANNEL =
  'chirality:attachments-select-files'`, request/result types (shared by preload
  and main).
- `electron/attachment-picker.ts` (pure, electron-free):
  `attachmentDialogExtensions()` = `SUPPORTED_ATTACHMENT_EXTENSIONS` without
  dots (imported from `src/lib/harness/ui-attachments.ts`, not restated);
  `resolveAttachmentProjectRoot(input)` requires an absolute path with
  `path.resolve(root) === root`, no control chars, then `realpath` + `stat`
  directory; `resolveAttachmentSelections(canonicalRoot, selections)` resolves +
  realpaths each selection, canonical-prefix check via `path.relative`
  (symlink escapes rejected, the root itself rejected), `isSupportedAttachmentPath`,
  regular-file check, dedupe, order preserved — any offender fails the whole
  selection; `createAttachmentSelectionHandler({authorized, showOpenDialog})`
  is the `ipcMain.handle` body (authorized-sender check first, before any
  validation or dialog; non-`AttachmentPickerError` failures collapse to a
  generic message so nothing native leaks).
- `main.ts`: `registerAttachmentSelectionHandler(rendererOrigin)` defined next
  to `registerDirectorySelectionHandler`, registered in the origin-gated block
  (it needs `rendererOrigin`, which the directory handler does not), removed in
  `teardown()` next to `SELECT_DIRECTORY_CHANNEL`. Dialog options exactly:
  `{ title: 'Attach files', buttonLabel: 'Attach', defaultPath: <canonical projectRoot>,
  properties: ['openFile','multiSelections'],
  filters: [{ name: 'Supported files', extensions: ['png','jpg','jpeg','gif','webp','pdf','txt','md','csv'] }] }`.

### 4. Window title

`new BrowserWindow({ title: 'Chirality', ... })` in `createMainWindow`. (The
renderer `<title>` still wins once the page loads — another worker's job.)

## Exact preload contract

```ts
window.chirality.attachments.selectFiles(
  { projectRoot: string }
): Promise<{ cancelled: true; error?: string } | { cancelled: false; paths: string[] }>
```

Preload forwards only `{ projectRoot }` (extra fields dropped) on channel
`chirality:attachments-select-files`. `paths` are canonical absolute paths
inside the canonical project root. Declared for the renderer in
`src/types/chirality-window.d.ts` as `attachments?: { selectFiles(...) }` plus
`AttachmentSelectionResult`. The concurrently authored consumer
`src/lib/shell/native-attachments.ts` (not mine) declares the identical shape.

## Files changed

Modified
- `projects/chirality-app-dev/frontend/electron/main.ts`
- `projects/chirality-app-dev/frontend/electron/preload.ts`
- `projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts` (return type of `createDesktopDaemonLifecycle` only)
- `projects/chirality-app-dev/frontend/src/types/chirality-window.d.ts` (renderer-side `window.chirality` declaration — the path asked for)
- `projects/chirality-app-dev/frontend/src/__tests__/electron/folder-preload.test.ts` (+1 test)

New
- `projects/chirality-app-dev/frontend/electron/runtime-autostart.ts`
- `projects/chirality-app-dev/frontend/electron/attachment-ipc-contract.ts`
- `projects/chirality-app-dev/frontend/electron/attachment-picker.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-autostart.test.ts` (9 tests)
- `projects/chirality-app-dev/frontend/src/__tests__/electron/attachment-picker.test.ts` (12 tests, real tmp dir with symlinks)

## Test commands and results

```
export PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin
cd /Users/ryan/dev/chirality/.claude/worktrees/owner-alignment-inspection-db4335/projects/chirality-app-dev/frontend

node node_modules/vitest/vitest.mjs run \
  src/__tests__/electron/runtime-autostart.test.ts \
  src/__tests__/electron/attachment-picker.test.ts \
  src/__tests__/electron/folder-preload.test.ts \
  src/__tests__/electron/runtime-daemon-signal-integration.test.ts \
  src/__tests__/electron/runtime-control-ipc.test.ts \
  src/__tests__/electron/folder-conveniences.test.ts
# Test Files 6 passed (6); Tests 46 passed (46)

node node_modules/vitest/vitest.mjs run src/__tests__/electron
# Test Files 27 passed (27); Tests 399 passed (399)

node node_modules/typescript/bin/tsc --noEmit -p tsconfig.electron.json
# exit 0

node node_modules/typescript/bin/tsc --noEmit -p tsconfig.json
# exit 1 — single error, NOT in my scope:
#   src/__tests__/components/account-presentation.test.tsx(9,10): TS2305
#   '../../components/shell/account-settings-controls' has no exported member 'DaemonQuickControl'
#   (both files are being modified by the concurrent renderer worker; no error in chirality-window.d.ts)
```

`runtime-daemon-signal-integration.test.ts` substring assertions on `main.ts`
remain true (verified by the run above).

## Risks and native-only verification

1. **LaunchAgent behaviour is only provable natively.** Unit tests cover the
   decision matrix with a fake lifecycle; `launchctl bootstrap` / `print`
   semantics, `ThrottleInterval`, and the plist write to
   `~/Library/LaunchAgents` need a packaged run (owner/R3 trial). Suggested
   native checks: fresh userData -> plist appears with `ProgramArguments[0]` =
   bundle exe and `CHIRALITY_USER_DATA` pinned, `launchctl print gui/$UID/<label>`
   succeeds, `desktop-main.log` shows `runtime.autostart.outcome {"action":"installed-and-started"}`;
   relaunch -> `already-loaded`; `launchctl bootout` then relaunch -> `started`.
2. **Stale-executable plist after the bundle moves** (e.g. app moved from
   `~/Downloads` to `/Applications`, or an upgrade in a different path). The
   installed plist names the old path, so autostart refuses
   (`refused_foreign_executable`) on every launch and the daemon never starts
   automatically. This is the conservative reading of "never overwrite a plist
   whose ProgramArguments name a different executable". Recovery is the manual
   Settings `install` (which does overwrite) or `chirality daemon install`. A
   follow-up could treat "named executable no longer exists" as reinstallable;
   left out to keep the change minimal and refusal-only.
3. **Trial vs. real job coexistence.** A trial run that uses the default label
   `com.chirality.runtime` with a different bundle path will see the owner's
   real plist as foreign (and vice versa) and refuse — correct, but the trial
   must set `CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL` (as the R3 launcher already
   does per posture) or set `CHIRALITY_SKIP_RUNTIME_AUTOSTART=1` to keep
   autostart out of an isolated drill.
4. **Startup latency.** Autostart awaits `launchctl print` (+ `bootstrap` when
   needed) before the renderer server starts; expected well under a second. It
   sits after the supervisor's first bind, so the window timing when the daemon
   is already up is unchanged.
5. **`already loaded` bootstrap race.** If the daemon is loaded between
   `status()` and `start()`, `LaunchAgentManager.start()` treats the
   `already loaded` bootstrap result as success and issues `kickstart -k`
   (a restart). Benign but visible as a daemon bounce; the supervisor rebinds.
6. **Attachment picker containment is by canonical prefix only**; it does not
   additionally exclude the instruction root (the folder picker's
   `validateRevealRoot` does that at project-selection time).
7. **Window title**: Electron replaces the BrowserWindow title with the page
   `<title>` on load unless `page-title-updated` is prevented; the renderer
   `<title>` change is owned by another worker.
