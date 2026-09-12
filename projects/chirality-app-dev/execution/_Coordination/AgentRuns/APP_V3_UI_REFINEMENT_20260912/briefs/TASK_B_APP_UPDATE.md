# Launch brief — TASK B: update discovery (Electron main, preload, renderer provider)

Role: TASK (Type 2). Engine/model: Claude Fable 5.1 (Claude Code Agent tool). No delegation.
Parent: implementing session for APP_V3_UI_REFINEMENT_20260912. Basis: 19bca4930.
Repository: /Users/ryan/dev/chirality/.claude/worktrees/project-first-impressions-06aed9 (git worktree; branch claude/chirality-ui-refinement-20260912; do not switch branches, do not commit, do not stash). Work in projects/chirality-app-dev/frontend.

## Purpose

Add "Check for Updates…" to the macOS Chirality application menu and a bridge so the renderer's account menu and an About dialog can check for updates, show checking / up-to-date / update-available / failed states, and open the download in the system browser. Checking and access to the download only: no automatic download, install or restart.

## Hard constraints (read before editing)

- `src/__tests__/contract-pins.manifest.ts` pins `electron/main.ts`: it must not match `\bautoUpdater\b` and must not contain `releases/latest` or `api.github.com/repos`, and every existing `contains` pin must survive. Run `npx vitest run src/__tests__/contract-pins.test.ts` before you finish.
- `projects/chirality-app-dev/docs/CONTRACT.md` K-NET-1: outbound network is deny-by-default. There is no release feed today (`gh release list` on sgttomas/chirality is empty; `scripts/pack-electron.mjs` passes `--publish never`; BUILD_AND_RELEASE.md §9/§10 leave publication as an open owner decision). Therefore: the release source module ships **unconfigured** and the checker **fails closed** with `failure.code = 'no-release-source'`. Never fetch anything in this build. Do not add `electron-updater` or any dependency.
- Design the checker so that configuring a source later still fails closed on policy: `electron/app-update-source.ts` exports `APP_UPDATE_ALLOWED_FEED_HOSTS: readonly string[]` (empty today) and `resolveAppUpdateSource()` returning `null`. `checkForAppUpdate({ source, currentVersion, fetchImpl, now })` returns `failed/policy` when a source host is not allowlisted, `failed/network` on fetch rejection, `failed/invalid-feed` on a malformed feed, `update-available` when the feed's semver (with prerelease ordering, e.g. 3.0.0-rc.1 < 3.0.0) is greater than `currentVersion`, else `up-to-date`. Feed shape: `{ version: string; downloadUrl: string (https only); releaseNotesUrl?: string; publishedAt?: string }`. Unit-test all branches with a fake `fetchImpl`; the production wiring passes a `fetchImpl` that throws `network` unless a source is configured AND allowlisted.
- `openDownload` opens `available.downloadUrl` with `shell.openExternal` only when it is `https:`; otherwise returns `{ ok: false, error }`.
- Every IPC handler checks `isAuthorizedSender` from `electron/ipc-sender-policy.ts` like the existing handlers; register channels in the same place as the others and remove them in `teardown()` (see `main.ts` around lines 885-895).

## Contract (fixed; the renderer UI is being coded against it in parallel)

`electron/app-update-ipc-contract.ts`:
```ts
export const APP_UPDATE_GET_CHANNEL = 'chirality:app-update-get';
export const APP_UPDATE_CHECK_CHANNEL = 'chirality:app-update-check';
export const APP_UPDATE_OPEN_DOWNLOAD_CHANNEL = 'chirality:app-update-open-download';
export const APP_UPDATE_CHANGED_CHANNEL = 'chirality:app-update-changed';
export const APP_ABOUT_SHOW_CHANNEL = 'chirality:app-about-show';
export type AppUpdateFailureCode = 'no-release-source' | 'policy' | 'network' | 'invalid-feed';
export type AppUpdateState = {
  currentVersion: string;           // app.getVersion() in main; name the constant `appVersion` so scripts/verify-version-identity.mjs sees it
  status: 'idle' | 'checking' | 'up-to-date' | 'update-available' | 'failed';
  checkedAt?: string;               // ISO, set after any completed check
  failure?: { code: AppUpdateFailureCode; message: string };
  available?: { version: string; downloadUrl: string; releaseNotesUrl?: string; publishedAt?: string };
  releaseSource: { configured: boolean; description: string }; // description is user-facing, e.g. 'No release source is configured for this build.'
};
```
Preload bridge under the existing `window.chirality` object (see `electron/preload.ts` `runtime.connectivity` for the invoke + subscribe pattern):
```ts
appUpdate: {
  get(): Promise<AppUpdateState>;
  check(): Promise<AppUpdateState>;
  openDownload(): Promise<{ ok: boolean; error?: string }>;
  subscribe(listener: (state: AppUpdateState) => void): () => void;   // APP_UPDATE_CHANGED_CHANNEL
  onShowAbout(listener: () => void): () => void;                       // APP_ABOUT_SHOW_CHANNEL
}
```
Add the same shape to `src/types/chirality-window.d.ts`.

Main process:
- `electron/app-update.ts`: a small state owner (`createAppUpdateController({ appVersion, source, fetchImpl, openExternal, now, log })` with `getState()`, `check()`, `openDownload()`, `subscribe()`), pure and unit-testable without Electron (mirror `electron/runtime-connectivity.ts` style). Concurrent `check()` calls share the in-flight check. Broadcast state changes to all windows on `APP_UPDATE_CHANGED_CHANNEL` (mirror `broadcastRuntimeConnectivity`).
- `electron/application-menu.ts`: extract the existing macOS menu template from `main.ts` into `buildApplicationMenuTemplate({ onCheckForUpdates, onShowAbout })` (pure, testable). Replace `{ role: 'about', label: 'About Chirality' }` with a click item that sends `APP_ABOUT_SHOW_CHANNEL` to the focused window (creating/focusing it if needed the way other main→renderer sends do), and add `{ label: 'Check for Updates…', click: onCheckForUpdates }` after it. Keep every other menu item exactly as it is. Also call `app.setAboutPanelOptions({ applicationName: 'Chirality', applicationVersion: appVersion, version: appVersion })` so any native panel reads Chirality, not the package name.
- Log with the existing desktop logger, never log URLs with query strings or anything containing `@`.

Renderer provider: `src/components/shell/app-update-provider.tsx` exporting `AppUpdateProvider` and `useAppUpdate(): { state: AppUpdateState | null; bridgeAvailable: boolean; check: () => Promise<void>; openDownload: () => Promise<void>; aboutRequests: number }` where `aboutRequests` increments on each `onShowAbout` signal. When `window.chirality.appUpdate` is absent (web dev, tests), `bridgeAvailable` is false and `state` is `null`. Do NOT mount it in `layout.tsx` and do not touch any other renderer file; the parent wires the UI.

## Write scope (exact)

- electron/app-update-ipc-contract.ts, electron/app-update-source.ts, electron/app-update.ts, electron/application-menu.ts (new)
- electron/main.ts (menu extraction, controller creation, IPC registration and teardown, about panel options), electron/preload.ts
- src/types/chirality-window.d.ts
- src/components/shell/app-update-provider.tsx (new)
- src/__tests__/electron/app-update.test.ts, src/__tests__/electron/application-menu.test.ts (new), src/__tests__/electron/folder-preload.test.ts only if its bridge-shape assertion needs the new namespace, src/__tests__/components/app-update-provider.test.tsx (new)

Nothing else. No git commits.

## Checks to run and report (exact commands and results), from projects/chirality-app-dev/frontend

- `npm run typecheck`
- `npx vitest run src/__tests__/electron src/__tests__/contract-pins.test.ts src/__tests__/components/app-update-provider.test.tsx`
- `npm run build:electron`
- `npm run verify:version-identity -- --expect 3.0.0-rc.1` (report whether the new `appVersion` surface is now scanned)
- `python3 ../../../tools/validation/validate_candidate_whitespace.py --base-ref 19bca4930`

## Return

Write projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_UI_REFINEMENT_20260912/returns/TASK_B_RETURN.md: files changed, the state machine and its tests, commands with results, and a precise list of the missing release infrastructure a future owner decision must supply (feed location and publication step, K-NET-1 amendment naming the feed host, the contract pins, checksum or signature verification of the feed). No em-dashes in prose.
