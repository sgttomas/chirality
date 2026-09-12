# TASK B return: update discovery (Electron main, preload, renderer provider)

Role: TASK (Type 2). Engine/model: Claude Fable 5.1 via the Claude Code Agent tool. No delegation.
Basis: 19bca4930 on branch claude/chirality-ui-refinement-20260912 (worktree). No commit, stash, or branch switch was performed.
Status: COMPLETE with one external typecheck finding outside this brief's scope (see Checks).

## Files changed (all inside the brief's write scope, paths relative to projects/chirality-app-dev/frontend)

New:
- electron/app-update-ipc-contract.ts: the five channel constants and the AppUpdateState, AppUpdateFailureCode, AppUpdateAvailable and AppUpdateOpenDownloadResult types exactly as the brief fixed them.
- electron/app-update-source.ts: APP_UPDATE_ALLOWED_FEED_HOSTS (empty), resolveAppUpdateSource() returning null, describeAppUpdateSource(), isAllowlistedFeedHost(), and the user-facing UNCONFIGURED_RELEASE_SOURCE_DESCRIPTION ('No release source is configured for this build.').
- electron/app-update.ts: parseSemver/compareSemver (semver 2.0.0 precedence with prerelease ordering, build metadata ignored), parseAppUpdateFeed, evaluateAppUpdateSourcePolicy (the single policy gate), createPolicyGuardedFetch (production fetch guard), checkForAppUpdate, and createAppUpdateController. No electron import.
- electron/application-menu.ts: buildApplicationMenuTemplate({ onCheckForUpdates, onShowAbout }) extracted from main.ts; About Chirality is now a click item and Check for Updates... follows it; every other item is byte-identical to the previous inline template.
- src/components/shell/app-update-provider.tsx: AppUpdateProvider, useAppUpdate(), isAppUpdateState() and the duplicated renderer-side types. Not mounted anywhere; no other renderer file touched.
- src/__tests__/electron/app-update.test.ts, src/__tests__/electron/application-menu.test.ts, src/__tests__/components/app-update-provider.test.tsx.

Modified:
- electron/main.ts: imports; module state for the controller and its unsubscribe; broadcastAppUpdateState (mirrors broadcastRuntimeConnectivity); focusOrCreateMainWindow and sendAboutShowSignal (send only to a receiver whose loaded URL has the renderer origin, like the folder-intent path, and after did-finish-load when the window is still loading); in initializeGui the constant appVersion = app.getVersion(), app.setAboutPanelOptions({ applicationName: 'Chirality', applicationVersion: appVersion, version: appVersion }), controller creation with createPolicyGuardedFetch and shell.openExternal, the three ipcMain.handle registrations next to the other renderer-origin handlers (each checks isAuthorizedSender; denied get/check return null, denied openDownload returns { ok: false, error }), the menu built from buildApplicationMenuTemplate, and removal of the three handlers plus unsubscribe in teardown(). The menu's Check for Updates... focuses or creates a window before starting the check so the broadcast result has somewhere to land.
- electron/preload.ts: window.chirality.appUpdate with get, check, openDownload, subscribe (APP_UPDATE_CHANGED_CHANNEL) and onShowAbout (APP_ABOUT_SHOW_CHANNEL), each unsubscribe removing the exact listener.
- src/types/chirality-window.d.ts: AppUpdateStatePayload and the optional appUpdate bridge on ChiralityBridge. The diff was verified to contain only this hunk.
- src/__tests__/electron/folder-preload.test.ts: one added test covering the appUpdate bridge shape (channels, single-argument listener delivery, exact-listener removal). The existing tests are unchanged. The brief admits this file only when its bridge-shape assertion needs the new namespace; this addition is the bridge-shape assertion for the new namespace and the parent may drop it if that reading is too wide.

## State machine

AppUpdateState.status moves: idle -> checking -> one of up-to-date, update-available, failed. Any later check() returns to checking and then to a fresh terminal status. While checking, failure and available are cleared and the previous checkedAt is kept; every completed check sets checkedAt from now(). currentVersion and releaseSource never change after construction. Concurrent check() calls return the same in-flight promise; a check after settlement is a new one.

Failure codes, in the order the checker evaluates them, none of which issues a request until the last two:
- no-release-source: source is null (the shipped build; the production fetch is never called).
- policy: source present but its feed URL is unparseable, not https, or its host is not in the allowlist (empty today).
- invalid-feed (pre-fetch): the installed version is not a valid semver, so no comparison is possible.
- network: fetchImpl rejected, or answered non-2xx. Messages are scrubbed of URLs and credential-shaped fragments.
- invalid-feed: body is not JSON, not an object, lacks a semver version, lacks an https downloadUrl, or carries a non-https releaseNotesUrl or non-string publishedAt.
- update-available when the feed semver is greater than currentVersion (3.0.0-rc.1 < 3.0.0; rc.1 < rc.2; rc.9 < rc.10; alpha < alpha.1 < beta; numeric identifiers precede alphanumeric); otherwise up-to-date.

openDownload(): { ok: false } when nothing is available or the downloadUrl is not https (nothing is opened); otherwise shell.openExternal(url) and { ok: true }, with a rejection mapped to { ok: false, error } (scrubbed).

Production fetch guard (createPolicyGuardedFetch): rejects with a refusal error unless a source is configured and allowlisted and the requested URL is exactly the configured feed; only then delegates to globalThis.fetch with redirect: 'error' and cache: 'no-store'. With app-update-source.ts unconfigured this build never fetches. The checker reports such a rejection as network, as the brief specifies.

Logging: app_update.check.started, app_update.check.completed (status, failureCode, availableVersion), app_update.open_download.opened/refused/failed, app_update.listener_failed. Detail objects carry no URL; error text has URLs replaced with [url] before it reaches state or log, and the test asserts the serialized log contains neither http nor an at-sign.

## Tests (all with a fake fetchImpl; no test issues a network request)

src/__tests__/electron/app-update.test.ts (23 tests): channel names; shipped source resolves null with an empty allowlist; policy gate for missing, non-https, malformed and non-allowlisted sources and case-insensitive host match; semver parsing and precedence; feed parsing accept/reject matrix; checkForAppUpdate for no-release-source (no fetch), policy (no fetch, both explicit and shipped allowlist), network (rejection with URL and query scrubbed from the message; HTTP 404), invalid-feed (three malformed bodies; unparseable installed version without fetch), update-available (exactly one fetch of the configured URL, all four feed fields carried), up-to-date (equal, older prerelease, older beta, older release, and a release current against a newer-looking rc); createPolicyGuardedFetch refusing without delegating, refusing a different URL, delegating when configured and allowlisted, and surfacing through the checker as network with the shipped source; controller initial state, checking -> failed/no-release-source transitions with checkedAt, shared in-flight check followed by a fresh one, stale outcome cleared while checking, openDownload for none/https/rejecting openExternal, and log hygiene plus unsubscribe.

src/__tests__/electron/application-menu.test.ts (3 tests): About is a click item with no role that calls onShowAbout, Check for Updates... follows it and calls onCheckForUpdates; the remainder of the Chirality submenu, the File menu, and the editMenu/viewMenu/windowMenu roles equal the previous inline template exactly; no install, restart or download item exists.

src/__tests__/components/app-update-provider.test.tsx (6 tests): isAppUpdateState accept/reject; no bridge gives bridgeAvailable false and state null with no-op actions; no provider gives the same fallback; hydration via get(), pushed transitions, a late hydrate never overwriting a push, malformed pushes ignored, and both listeners removed on unmount; check() invoking the bridge and adopting the settled state (a null answer leaves state as is), openDownload() invoking the bridge and a rejection swallowed; aboutRequests incrementing once per About signal and not after unmount.

src/__tests__/electron/folder-preload.test.ts (+1 test): the appUpdate bridge shape described above.

## Checks (run from projects/chirality-app-dev/frontend)

1. npm run typecheck: FAIL (exit 2), for reasons outside this brief's scope. The electron project passes on its own: npx tsc -p tsconfig.electron.json --noEmit --incremental false exits 0. The renderer project reports exactly two errors, both in files the parent is editing in parallel (they are dirty in git status and are not in this brief's write scope):
   - src/components/shell/chat-panel.tsx(41,37): error TS2307: Cannot find module './conversation-message' or its corresponding type declarations.
   - src/__tests__/components/account-presentation.test.tsx(22,7): error TS2741: Property 'onReopenLogin' is missing in type ... but required in type 'HostedBootstrapController'.
   No error is reported in any file this task wrote or modified. Not fixed, staged, or interpreted, per the external-state rule in projects/chirality-app-dev/AGENTS.md.
2. npx vitest run src/__tests__/electron src/__tests__/contract-pins.test.ts src/__tests__/components/app-update-provider.test.tsx: PASS. Test Files 20 passed (20); Tests 366 passed (366). contract-pins.test.ts passed, so electron/main.ts still matches no \bautoUpdater\b, contains neither releases/latest nor api.github.com/repos, and keeps every existing contains pin.
3. npm run build:electron: PASS (exit 0). dist-electron/main.js 183.4kb, dist-electron/preload.js 6.9kb, runtime-service and runtime-cli bundles built.
4. npm run verify:version-identity -- --expect 3.0.0-rc.1: PASS (exit 0; 0 mismatching, 3 absent/not-inspected/unchecked). The new surface is now scanned: row 10 (source:version-reporting) changed from ABSENT to PRESENT_UNCHECKED and lists electron/app-update-ipc-contract.ts [electron-app-getVersion], electron/app-update.ts [product-version-token], electron/main.ts [electron-app-getVersion], electron/main.ts [product-version-token]. The value is read from app.getVersion() at runtime, so the script's "verify its rendered value manually on the staged bytes" note applies to a staged .app, not to source.
5. python3 ../../../tools/validation/validate_candidate_whitespace.py --base-ref 19bca4930: PASS ("candidate whitespace is clean").

Two iterations were needed before the vitest run went green: the provider needed an explicit React default import (this tree uses jsx: preserve with the classic transform under vitest), and the provider test had to wrap unmount() in act() so React 18 flushes passive-effect cleanup before the listener counts are asserted. Both were in files this task owns.

One note for the parent: src/__tests__/electron/app-update.test.ts line 342 contains a synthetic address-shaped string (user at example.test) used solely as a redaction fixture; the assertion on line 349 proves that no log line carries an at-sign. No log, record, or return carries one.

## Missing release infrastructure (a future owner decision must supply all of these before a source can be configured)

1. Feed location and publication step. There is no release feed: gh release list on sgttomas/chirality is empty, scripts/pack-electron.mjs passes --publish never, and BUILD_AND_RELEASE.md sections 9 and 10 leave publication open. The owner must choose an https host and path for a JSON document of shape { version, downloadUrl (https), releaseNotesUrl?, publishedAt? } and a publication step that writes it from the signed candidate (desktop:dist output), with the DMG at downloadUrl. Then electron/app-update-source.ts gains a resolveAppUpdateSource() that returns { feedUrl, description }.
2. K-NET-1 amendment naming the feed host. projects/chirality-app-dev/docs/CONTRACT.md K-NET-1 is deny-by-default; the feed host must be named there, and only then added to APP_UPDATE_ALLOWED_FEED_HOSTS in electron/app-update-source.ts. Until both happen a configured source fails closed with policy. The main-process fetch runs outside the renderer egress interception in main.ts, so the allowlist in app-update-source.ts is the enforcement point for this path and the amendment should say so.
3. Contract pins. src/__tests__/contract-pins.manifest.ts pins electron/main.ts against \bautoUpdater\b, releases/latest and api.github.com/repos. The current design honours all three and needs no change, but a GitHub Releases feed would collide with the last two if its URL were ever placed in main.ts; the decision should either keep the URL confined to app-update-source.ts (not pinned) or amend the manifest deliberately, and should consider adding pins that keep APP_UPDATE_ALLOWED_FEED_HOSTS and resolveAppUpdateSource() aligned with the K-NET-1 text.
4. Checksum or signature verification of the feed. checkForAppUpdate trusts the JSON it fetches over https with redirects refused; nothing verifies a detached signature or a checksum of the feed or the DMG. Because this build only opens the download in the browser, the Apple signature and notarization on the DMG remain the install-time trust anchor, but the owner decision should state whether the feed itself must be signed (for example a detached signature verified against a key embedded in electron/app-update-source.ts) and whether downloadUrl must carry a checksum for the renderer to display, before update-available is treated as more than a pointer.
5. Not required today but implied by the above: a documented version-identity check on the staged .app (verify-version-identity.mjs --app-path) so the appVersion the checker compares is the bundle's CFBundleShortVersionString, and a decision on whether pre-release identities (3.0.0-rc.N) should ever be offered as updates to release identities (the checker's semver precedence already says no).
