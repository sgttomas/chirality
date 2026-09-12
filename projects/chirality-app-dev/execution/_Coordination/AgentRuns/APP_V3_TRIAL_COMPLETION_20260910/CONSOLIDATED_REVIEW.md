# CONSOLIDATED_REVIEW — APP_V3_TRIAL_COMPLETION_20260910

Independent Type 2 review of the complete uncommitted working tree on
`claude/chirality-v3-mvp-trial-ab05cb` (base `main` at `14a594b78`), worktree
`/Users/ryan/dev/chirality/.claude/worktrees/owner-alignment-inspection-db4335`.
Reviewer did not author any of the tranche. Paths below: `R` =
`projects/chirality-runtime`, `F` = `projects/chirality-app-dev/frontend`.
Product and test files were not modified by this review; this file is the only
file written.

## Verdict

**ACCEPT**

The tranche satisfies owner criteria (0)–(8) in code, not only in the authors'
RETURN documents. The trial blocker is closed at the App side (the Next-tier
hosted-bootstrap port now returns binding-only for initialize and status and no
non-test App path calls `RuntimeClient.hostedBootstrapStatus`) while the daemon
side is byte-unchanged (`R/packages/daemon/src/runtime-daemon.ts` has no diff;
`runHostedAccount` still requires `x-chirality-account-proof`). Autostart is
packaged-only, foreign-plist-refusing and never throws; the attachment picker
has sender authorization, realpath containment and the shared allow-list; model
selection is validated at every hop (App draft, Next route pass-through,
`RuntimeService`, adapter, `DelegatedRuntime`, supervisor) with explicit 400/503
`details.reason` and no silent substitution; the v2 configDigest recipe,
`EngineSelection`, `startManager` pinning and schema identifiers are unchanged.
All three typechecks pass; the full frontend suite passes (2214/2214); the full
runtime suite shows two failures that both pass in isolation (2/2 reruns), touch
files outside the diff, and are load-induced flakes rather than regressions.
No blocking findings. The non-blocking items below are recommended for a
follow-up tranche and do not gate the signed build or the human trial. Nothing
in this review authorizes publishing.

## Blocking findings

None.

## Non-blocking findings

| # | Location | Observation | Suggested follow-up | Criterion |
|---|---|---|---|---|
| N1 | `R/tests/supervisor.test.ts` ("bounds worker lifetime and kills stubborn children during retirement"), `R/tests/hosted-private-composition.test.ts:303` | Fail under full-suite load (`supervisor request rejected`; `Test timed out in 5000ms`), pass 2/2 when run alone. Neither test nor `packages/core/src/supervisor.ts` is in the diff. | Raise the per-test timeout on the composition test or serialise the two process-heavy files in the vitest config so CI (`harness-premerge`) does not flake. | 7 / CI parity |
| N2 | `R/packages/core/src/runtime-service.ts:70`, `R/packages/daemon/src/codex-supervisor.ts:143,242-243`, `R/packages/core/src/delegated-runtime.ts` (`resolveTurnAttribution`) | The `[\x21-\x7e]{1,128}` / `{1,64}` regexes are re-typed inline instead of importing `HOSTED_MODEL_ID_PATTERN` / `HOSTED_REASONING_EFFORT_PATTERN` from `R/packages/contracts/src/delegated.ts:175-176`. `validateModelSelection` also duplicates the shape check inside `resolveHostedModelSelection` (`delegated.ts:205-212`). | Import the constants; keep `validateModelSelection` only as the pre-catalog gate. Behaviour is identical today so this is drift risk, not a defect. | 6 |
| N3 | `F/src/lib/harness/error-display.ts:153-160` | `modelNotInCatalogUiError` renders "This chat used X, which your Codex account no longer offers. Start a new chat." for every `MODEL_NOT_IN_CATALOG`, including the session-create 400 raised when the renderer's catalog snapshot is stale (the chat has not started, so "this chat used" is misleading). | Branch on whether a booted session exists: for the create path say "Model X is no longer offered; refresh your account status and choose again." | 6 |
| N4 | `F/electron/runtime-autostart.ts:150-158` | If the installed plist names a stale copy of the same app (e.g. app moved from `~/Downloads` to `/Applications`), the executable differs and autostart is `refused` forever; the user must reinstall through Settings. Correct per the "foreign plist refusal" requirement, but a moved app is a likely trial scenario. | Log the refusal at warn level and surface a one-line hint in Settings > Runtime ("installed service points at another copy"). | 1 |
| N5 | `F/electron/main.ts:839-848` | `ensureRuntimeDaemonAutostart` is awaited before the renderer server starts, so a slow `launchctl bootstrap` delays first paint. Bounded (launchctl typically returns in <1 s) and never throws, but not time-boxed. | Wrap in a `Promise.race` with a short timeout that resolves to `{action:'failed', stage:'start'}`. | 1 |
| N6 | `F/electron/attachment-picker.ts:63-66` | `within()` treats any `relative.startsWith('..')` as an escape, so a legitimately in-root file named `..notes.md` is rejected. Harmless (user sees "Unable to attach the selected files."). | Use `relative === '..' \|\| relative.startsWith('..' + path.sep)`. | 5 |
| N7 | `F/electron/attachment-picker.ts` | Containment is project-root prefix only; the picker does not exclude the instruction root or `.chirality/` internals. Same posture as the existing `ui-attachments.ts` renderer path, so no regression. | Consider aligning with any future protected-path list. | 5 |
| N8 | `F/src/lib/runtime-client/daemon-harness-port.ts` and `F/src/lib/harness/hosted-bootstrap-client.ts` | `HostedProjectInitializationResponse` (`Extract<..., {registration:'registered'}>`) is declared twice. | Export once from the port and import in the client. | 0 |
| N9 | `F/src/components/shell/account-popover.tsx` | `runtime` and `legacyHref` props are kept on `AccountPopoverProps` but only consumed via `void legacyHref; void runtime;`. | Drop the props from the interface and the call site in `shell-frame.tsx:417`. | 2 |
| N10 | `F/src/__tests__/electron/hosted-account-sequence.integration.test.ts` | The controlled `materializeAdmission` returns no catalog, so the catalog-bearing `ready` status is never observed through `HostAccountClient` → `performHostAccountOperation` in this test; that path is covered only by unit tests with hand-built statuses (`host-account-ipc.test.ts`, `hosted-bootstrap-client.test.ts`). | Add a catalog to the sequence test's fixture engine so `models`/`selection` are asserted across the real proof-bearing path. | 6 / 7 |
| N11 | `R/packages/daemon/src/hosted-private-composition.ts:518-520` | The catalog is read only when `context.v2`; v1/standalone admissions keep `resolveDefaultModel` and never expose `models`, so the App never sends `modelSelection` and any client that does gets 400 `MODEL_SELECTION_UNSUPPORTED`. Correct (no silent default) and documented by F, recorded here so trial testers on a v1 basis are not surprised by absent selectors. | None. | 6 |

## Criterion-by-criterion verification

| Criterion | Verdict | Evidence (file:line) |
|---|---|---|
| (0) Trial blocker: init does not request hosted status via ordinary client; status only via signed Desktop IPC; daemon auth unchanged; no non-test App caller of `hostedBootstrapStatus` | PASS | `git diff -- R/packages/daemon/src/runtime-daemon.ts` empty; proof gate `runtime-daemon.ts:806-809`; `F/src/lib/runtime-client/runtime-daemon-harness-port.ts:637,655,678` return `{registration:'registered', projectId}` only; `registeredStatus` deleted; `grep -rn hostedBootstrapStatus F/src F/electron` excluding `__tests__` returns nothing; renderer status via bridge `F/src/lib/harness/hosted-bootstrap-client.ts:132` (`getHostedBootstrapStatusWithRetry`) → `window.chirality.runtime.hostedAccount` → `F/electron/host-account-ipc.ts:108-116`; tests `F/src/__tests__/api/harness/hosted-bootstrap.test.ts` ("never carries hosted account status through the Next status route"), `runtime-daemon-harness-port.test.ts` (`hostedBootstrapStatus` `not.toHaveBeenCalled`), sequence test asserts 401 for scoped/bootstrap clients |
| (1) Daemon autostart in packaged use; posture consistent; foreign plist refused; packaged-only; never throws; ProgramArguments[0] is the executable | PASS (N4, N5) | `F/electron/runtime-autostart.ts:30` opt-out env, `:51-52` packaged flag, `:110` unpackaged skip, `:119-169` every stage wrapped in try/catch → `failed`, `:155` refused foreign executable, `:158` already-loaded skip, `:162` install+start; `F/electron/main.ts:839-848` wiring after `bindingSupervisor.start()`, `refreshNow()` on start; same `createDesktopDaemonLifecycle()` (`F/electron/runtime-control-ipc.ts`) used for Settings controls, posture from `F/electron/desktop-daemon-posture.ts:57-64`; plist `R/packages/cli/src/launch-agent.ts:251-253` `<string>${xml(resolve(input.executablePath))}</string>` then `--runtime-daemon`; `LaunchAgentManager.start` `launch-agent.ts:381-401` tolerates already-loaded then `kickstart -k`; 9 tests `F/src/__tests__/electron/runtime-autostart.test.ts` use real `renderRuntimeLaunchAgent` |
| (2) User menu only sign-in/account, Settings, Appearance, About | PASS (N9) | `F/src/components/shell/account-popover.tsx:24-40`; `DaemonQuickControl` removed from `account-settings-controls.tsx`; test `account-popover` suite updated to assert absence of Shared Runtime controls |
| (3) Redundant labels/banners removed; explanations in title/hover; accessible names preserved | PASS | `F/src/components/shell/shell-frame.tsx:271` `visually-hidden` "Working root"; `shell-runtime-chip-key` span removed (tests now expect `connected`/`connecting`); `F/src/components/settings/runtime-settings.tsx:62` PID/startedAt in `title`, `:76` `<details className="runtime-service">`; `hosted-bootstrap-view.tsx` explanations as `title` constants, `role="alert"` retained; chat-panel "Human trial" span removed; selects keep `aria-label` |
| (4) "Project access" dropdown removed; `workspaceWrite` still sent per turn; no new modes | PASS | `F/src/components/shell/chat-panel.tsx:92-104` single `OPERATOR_MODES` entry; `permissionMode` sent at `:691,:840,:859`; `opts.mode` at `:860`; unsupported-continuation recovery `:1290`; no `<select>` for mode remains |
| (5) Native attachment picker with sender auth, canonical containment incl. symlinks, allow-list identical to `ui-attachments.ts`, no native error leakage; "Who is working" → "Agents" | PASS (N6, N7) | `F/electron/attachment-picker.ts:19-20` imports `SUPPORTED_ATTACHMENT_EXTENSIONS`/`isSupportedAttachmentPath` from `src/lib/harness/ui-attachments.ts`; `:89,:121` realpath root and each selection; `:63` `within()`; `:130` allow-list; `:152-171` unauthorized → fixed string, non-picker error → "Unable to attach the selected files."; `F/electron/main.ts:529` handler uses `isAuthorizedSender(event, rendererOrigin)`; `F/electron/preload.ts:71-72` forwards only `projectRoot`; `F/electron/attachment-ipc-contract.ts:6` channel; 12 tests in `attachment-picker.test.ts` with real tmp dirs incl. symlink escape; `F/src/components/woven-dialogue/right-panel.tsx:116,126` "Agents"; `layout` fallback to in-app picker `chat-panel.tsx:1134` |
| (6) Model/reasoning selectors from authenticated catalog wired through Runtime; persistence; history; no silent substitution; Plan Mode separate; configDigest/launcher recipes/login method list unchanged; `startManager` pinned; `EngineSelection` unchanged; no schema bump | PASS (N2, N3, N10, N11) | Contracts `R/packages/contracts/src/delegated.ts:175-176,205-219,236-254`; daemon `codex-login.ts:269-272` `resolveDefaultModel` derives from `resolveModelCatalog`; `hosted-private-composition.ts:518-520` `selected = catalog.default`, `:523` configDigest recipe untouched (guarded by `d36-v2-connected.test.ts` `recordKey` equality), `:586` `modelCatalog` passed to `admitHosted`; `hosted-bootstrap.ts:226-230` status carries `models`/`selection` only when ready, `:345` cleared on retire; core `runtime-service.ts:66-71,154-182` (`MODEL_SELECTION_INVALID`, `MODEL_SELECTION_UNSUPPORTED`), boot rewrite spreads `...session` so `reasoningEffort` persists; `delegated-engine-adapter.ts:60-64,167` 503 reasons; `delegated-runtime.ts:212-222`; `codex-supervisor.ts:144-145,240-245,368,474-476` `assertCatalogChoice` before `thread/start`, `startManager` (`:320`) not in diff; `git diff R/packages/contracts` shows no schema-string change, no `EngineSelection` change; App `hosted-bootstrap-context.tsx:26-50`, `chat-panel.tsx:696` `modelSelection` on create, `:1385,:1399` selects, `chat-draft.ts:1,42-46` pair persistence with contract patterns, `error-display.ts:138-160`; toolkit `opts.model` removed (`harness-toolkit.test.ts`); history via `RuntimeSessionRecord.reasoningEffort` in operator projection and replay lens tests |
| (7) Sequence tested through production code | PASS (see coverage assessment) | `F/src/__tests__/electron/hosted-account-sequence.integration.test.ts`; `R/tests/hosted-bootstrap-integration.test.ts` (new catalog case); `R/tests/codex-primary-chat-integration.test.ts` (new catalog case asserting `thread/start.params.model` and `turn/start ... reasoning_effort`) |
| (8) Window title "Chirality" | PASS | `F/electron/main.ts:621` `title: 'Chirality'`; `F/src/app/layout.tsx:57` `title: 'Chirality'` (only title metadata under `src/app`) |
| Visual direction preserved | PASS | CSS diff limited to `settings-view.module.css` (+3 `.runtime-service` rules, −`.footer`) and existing `chat-mode-selector` class reuse; no palette/typography changes |
| Cross-cutting: effect loops / double setup | PASS | `F/src/components/settings/hosted-bootstrap-controller.tsx:195-207` one run per `lastSelection.sequence`, snapshot null on root change, `perform` (`:168`) generation+abort guards; `workspace-provider.tsx` sets sequence only in `applyProjectRoot` |
| Cross-cutting: secret logging | PASS | autostart logs executable paths and outcome only; attachment errors carry basename only; no token/proof values logged |
| Cross-cutting: weakened tests | PASS | Removed assertions all correspond to intentionally removed UI/fields and are replaced by stronger negatives; no `.skip/.only/.todo` added in either test diff |
| Cross-cutting: CI parity | PASS | Frontend consumes runtime via `file:` deps; runtime `build`/`typecheck` are `tsc -b` with cli in references; both pass here |

## Test-coverage assessment for criterion 7

Proven through production code in this working tree:

- **App sequence** (`F/src/__tests__/electron/hosted-account-sequence.integration.test.ts`, 1 test, 20 s budget): a real controlled daemon (`startControlledHostedBootstrapRuntimeHostForTests`), real `HostAccountAuthority` and `createHostAccountClient` over an in-process XPC seam, the production Next route handlers invoked via `routeFetch()`, and `performHostAccountOperation` from `F/electron/host-account-ipc.ts`. It asserts 401 for scoped and bootstrap `RuntimeClient`s, that the Next status route returns binding-only, and the full consent → login → cancel → login → signed-in/ready → sign-out sequence. Ceremony and engine are controlled fixtures; no catalog is produced (N10).
- **Runtime bootstrap composition** (`R/tests/hosted-bootstrap-integration.test.ts`): real `HostedBootstrapService` with a catalog-bearing materialization; asserts catalog exposure while admitted, per-session fixed choice, and refusal of an out-of-catalog model.
- **Runtime primary chat** (`R/tests/codex-primary-chat-integration.test.ts`): real `DelegatedRuntime` + `CodexSupervisor` against a scripted app-server; asserts 400 `MODEL_NOT_IN_CATALOG` with `available`, `thread/start.params.model === 'gpt-alt'`, `turn/start` `collaborationMode.settings.reasoning_effort === 'low'`, the default path, and that the on-disk session record and replay carry the choice.
- **D36 v2 connected** (`R/tests/d36-v2-connected.test.ts`): asserts the retained catalog equals the same `model/list` read and pins the v2 `configDigest` via `recordKey` equality (regression guard for "recipes byte-unchanged").
- **Unit seams**: `host-account-ipc.test.ts` (ready status with catalog forwarded verbatim), `hosted-bootstrap-client.test.ts` (bridge retry ladder, no fetch), `runtime-autostart.test.ts` (9 cases, real plist renderer), `attachment-picker.test.ts` (12 cases, real filesystem with symlinks), `chat-panel-model-selectors.test.tsx` (9), `chat-panel-native-attachments.test.tsx` (3), `folder-select.test.tsx` (2), `turn-route-attachments.test.ts` (3), `hosted-model-selection-contracts.test.ts` (4), `attachment-content-path.test.ts` (3).

Remains native-only (not exercised by any automated test here):

- Electron IPC transport itself (`ipcMain.handle`/`ipcRenderer.invoke`), `contextBridge` exposure, and `dialog.showOpenDialog`.
- The real Next HTTP server and the packaged renderer origin check.
- Real XPC / codesign-backed `HostAccountAuthority` proof issuance.
- Real Codex app-server `model/list`, `thread/start`, `turn/start` semantics (scripted in tests).
- `launchctl bootstrap/kickstart/print` behaviour, `ThrottleInterval`, and the moved-app plist scenario (N4).
- Catalog-bearing `ready` status crossing the proof-bearing `HostAccountClient` path end-to-end (N10).

## Commands run and exact results

Environment: `PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin` (Node 24.18.0). No `npm install/ci`, no packaged build, no `launchctl`, no writes outside this file and the session scratchpad.

| Command (cwd) | Result |
|---|---|
| `git status --short` / `git diff --stat` (worktree root) | 71 modified tracked files, `+1642 −365`; 15 untracked product/test files plus the run directory (all read) |
| `git diff -- projects/chirality-runtime/packages/daemon/src/runtime-daemon.ts` | empty |
| `git diff --stat -- projects/chirality-runtime/packages/core/src/supervisor.ts projects/chirality-runtime/tests/supervisor.test.ts` | empty |
| `npm run typecheck` (R) → `tsc -b --pretty false` | exit 0, no diagnostics |
| `node node_modules/typescript/bin/tsc --noEmit -p tsconfig.json` (F) | exit 0 |
| `node node_modules/typescript/bin/tsc --noEmit -p tsconfig.electron.json` (F) | exit 0 |
| `node node_modules/vitest/vitest.mjs run` (R, full suite) | `Test Files  2 failed \| 79 passed \| 1 skipped (82)`; `Tests  2 failed \| 1071 passed \| 14 skipped (1087)`; Duration 22.22s; exit 1 |
| — failure 1 (verbatim) | `FAIL  tests/hosted-private-composition.test.ts > hosted private production composition boundary > connects public bootstrap through real same-actor admission to retained and fresh controlled candidates` / `Error: Test timed out in 5000ms.` (at `tests/hosted-private-composition.test.ts:303:3`) |
| — failure 2 (verbatim) | `FAIL  tests/supervisor.test.ts > private process supervisor > bounds worker lifetime and kills stubborn children during retirement` / `Error: supervisor request rejected` (at `packages/daemon/src/supervisor-server.ts:240:314`) |
| `node node_modules/vitest/vitest.mjs run tests/supervisor.test.ts tests/hosted-private-composition.test.ts` (R, run twice) | run 1: `Test Files  2 passed (2)` / `Tests  22 passed (22)`; run 2: `Test Files  2 passed (2)` / `Tests  22 passed (22)` |
| `node node_modules/vitest/vitest.mjs run` (F, full suite) | `Test Files  209 passed \| 1 skipped (210)`; `Tests  2214 passed \| 4 skipped (2218)`; Duration 7.93s; exit 0. (A stdout line `{"status":"FAIL","summaryPath":".../chirality-daemon-proof-test-KX97CK/evidence/summary.json"}` is printed by a script under test, not a vitest failure.) |

Classification of the two runtime failures: load-induced flakes. Both pass
deterministically in isolation, neither file is touched by the tranche, and the
composition timeout is documented by author F as pre-existing. They do not
change the verdict but are recorded as N1 for CI hardening.
