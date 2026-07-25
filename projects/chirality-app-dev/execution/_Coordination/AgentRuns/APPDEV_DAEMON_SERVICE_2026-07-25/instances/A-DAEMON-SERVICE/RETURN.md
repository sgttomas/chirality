# A-DAEMON-SERVICE — RETURN (Stage A: A1–A6)

**Run:** TRB-APPDEV-DAEMON-SERVICE-2026-07-25 · **Agent 2 (opus)** · branch `feat/daemon-service` (base `main` @ `e9068c87d`)
**Authority:** `../../ADOPTED_BRIEF.md` · **Launch brief:** `LAUNCH_BRIEF.md` (verbatim)
**Status:** COMPLETE. No commits made, no branch operations, no `desktop:pack`, no GUI launched, no touch of the real LaunchAgent / real userData / real registration.

---

## 1. Files changed

### Modified

| Path | Why |
|---|---|
| `runtime/packages/cli/src/launch-agent.ts` | A3: `renderRuntimeLaunchAgent` / `LaunchAgentManager` gain generic `label`, `keepAlive`, `runAtLoad`, `throttleIntervalSeconds`, `environmentVariables` options; defaults reproduce the historical plist byte-for-byte. |
| `runtime/packages/cli/test/cli.test.ts` | 6 new tests: `KeepAlive=true` rendering, `KeepAlive` omission, env/RunAtLoad/Throttle pinning + XML escaping, default-preservation, isolated-label routing through plist path + `bootstrap`/`kickstart`/`bootout` service names. |
| `frontend/electron/main.ts` | A6 `CHIRALITY_USER_DATA` honoring before `ready`; A2 daemon activation policy; A4 supervised binding + connectivity IPC + broadcast; A5 file logging replacing the bare `console.warn`; A1 mitigation (daemon quit veto) and exit-path instrumentation. |
| `frontend/electron/runtime-control-ipc.ts` | A3 caller side: `createDesktopDaemonLifecycle()` passes `keepAlive:'always'`, `runAtLoad:true`, `environmentVariables.CHIRALITY_USER_DATA`, and an optional isolation label from `CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL`. Runtime package stays generic (D-GOV-20). |
| `frontend/electron/preload.ts` | A4: exposes `chirality.runtime.connectivity.get()` / `.subscribe()`. |
| `frontend/src/components/shell/shell-frame.tsx` | A4: runtime-connectivity chip in `.shell-header-controls`, a sibling of the working-root chip. |
| `frontend/src/types/chirality-window.d.ts` | Declares the connectivity bridge on `ChiralityBridge` (additive; other bridge surfaces still narrowed locally by their consumers). |
| `frontend/src/app/globals.css` | Appended a clearly-marked EOF section for the connectivity chip. Existing tokens only (`--sage*`, `--slate*`, `--danger*`, `--rule`, `--ground`, `--ink-*`); **no token changes**. |
| `frontend/src/__tests__/electron/runtime-control-ipc.test.ts` | 3 new tests for the lifecycle options and label-override handling (`afterEach` added to the vitest import). |

### New

| Path | Why |
|---|---|
| `frontend/electron/runtime-connectivity.ts` | A4: IPC channel contract + `createRuntimeBindingSupervisor` (bind/retry/probe/rebind state machine). `electron`-free, fully injectable → unit-testable under plain Node. |
| `frontend/electron/desktop-log.ts` | A5: dependency-free append-only timestamped logger with a single size-triggered rotation and a console mirror. |
| `frontend/electron/desktop-process-policy.ts` | Pure env decisions (`resolveUserDataOverride`, `resolveDaemonActivationPolicy`) extracted so the pre-`ready` rules in `main.ts` are testable. |
| `frontend/src/lib/shell/runtime-connectivity.ts` | Renderer-side snapshot guard + pure `deriveRuntimeConnectivityPresentation`. |
| `frontend/src/components/shell/use-runtime-connectivity.ts` | Push-driven hook (hydrate + subscribe, ordered so a late hydrate cannot overwrite a newer push). |
| `frontend/src/__tests__/electron/runtime-connectivity.test.ts` | 11 tests, deterministic timer queue. |
| `frontend/src/__tests__/electron/desktop-log.test.ts` | 8 tests. |
| `frontend/src/__tests__/electron/desktop-process-policy.test.ts` | 9 tests. |
| `frontend/src/__tests__/lib/shell-runtime-connectivity.test.ts` | 9 tests. |
| `frontend/src/__tests__/components/shell-frame-runtime-connectivity.test.tsx` | 8 tests. |

**Out-of-scope paths untouched** (Stage B's, confirmed via `git status`): `frontend/package.json`, `frontend/public/**`, `frontend/build/**`, `frontend/electron/cli-launcher.ts`, `frontend/scripts/**`, `src/__tests__/electron/cli-launcher.test.ts`, `.gitignore`. No `package-lock.json` mutation. `frontend/scripts/build-electron.mjs` needed **no** change — `main.ts`/`preload.ts` are esbuild entry points and bundle new siblings automatically (verified by running `node ./scripts/build-electron.mjs`).

---

## 2. A1 — GUI-launch → daemon-kill mechanism (desk analysis; hypothesis + evidence)

Live reproduction deliberately deferred to Stage V. All probes below were non-disruptive and read-only (`plutil`, `launchctl print`, `ls`, `ps`, `lsappinfo`, reading log files).

### New evidence gathered this stage

1. **The installed plist already had `RunAtLoad` and `KeepAlive`.** `plutil -p ~/Library/LaunchAgents/com.chirality.runtime.plist` → `KeepAlive => { SuccessfulExit => false }`, `RunAtLoad => true`, `ThrottleInterval => 10`. The brief's root cause #2 ("no `KeepAlive`/`RunAtLoad`") is **inaccurate as stated**; source at `launch-agent.ts:54-62` matched. The real defect is semantic, see (2).
2. **launchd is deliberately holding the job down.** `launchctl print gui/501/com.chirality.runtime` → `state = not running`, `runs = 4`, `last exit code = 0`, and decisively **`semaphores = { successful exit => 0 }`**. That is launchd reporting the `SuccessfulExit:false` KeepAlive condition as unsatisfied: the daemon exited *successfully*, so KeepAlive is contractually forbidden from restarting it. The existing restart posture is by construction blind to the actual failure mode.
3. **The daemon exits through a silent clean path.** `daemon.stderr.log` is 0 bytes; `daemon.stdout.log` holds exactly 4 successful startup banners (matching `runs = 4`) and no error, warning, or shutdown trace. The only code paths producing exit 0 with zero output are `before-quit → shutdown()` and `SIGTERM → shutdown(0)`.
4. **No Chromium process-singleton is involved.** `ls -la "~/Library/Application Support/chirality-frontend"` shows **no `SingletonLock`/`SingletonSocket`/`SingletonCookie`** — consistent with the source never calling `app.requestSingleInstanceLock()` (Electron creates `ProcessSingleton` only on that call; the userData folder is the singleton criterion). Shared-userData lock contention is therefore **ruled out** as the kill mechanism.
5. **The daemon runs as an ordinary foreground application.** `Chirality.app/Contents/Info.plist` has **no** `LSUIElement`, **no** `LSBackgroundOnly`, **no** `LSMultipleInstancesProhibited`, and `CFBundleIdentifier = com.chirality.app` (also confirms Stage B's residual: `CFBundleIconFile = electron.icns`).

### Best-supported mechanism hypothesis

**LaunchServices instance-resolution against a foreground-registered daemon, followed by an operator-visible quit that launchd was configured not to undo.**

- launchd starts the daemon by `exec`ing the Mach-O directly. That **bypasses LaunchServices' launch path**, so it always produces a new process — which is exactly why the *reverse* order always coexists (daemon started while the GUI runs: verified 18:30–18:54 and 19:0x). This asymmetry is the discriminating observation, and only a LaunchServices-side mechanism explains it.
- Because the bundle sets no `LSUIElement` and the code never called `setActivationPolicy`, that daemon process nevertheless comes up as a **full `NSApplication`**: Dock tile, menu bar, and a LaunchServices-visible, *activatable* instance of `com.chirality.app`.
- A Finder/Dock/`open` launch **does** go through LaunchServices, which by default does not start a second instance of an already-running bundle — it resolves the launch against the existing instance (activate / `kAEReopenApplication`). That instance is the headless daemon, which registers no `activate` handler in daemon mode and has no window, so **nothing visibly opens**.
- Any operator response to "the app didn't open" — Quit from the Dock tile, ⌘Q, force-quit, or an AppleEvent quit accompanying the launch — reaches Electron as `before-quit`, which the old handler serviced with `shutdown()` → `app.exit(0)`: a **clean, silent exit 0**. `KeepAlive:{SuccessfulExit:false}` then refuses to restart it (evidence 2), and the next launch produces a fresh process that becomes the GUI. Net operator-visible effect: *"launching the GUI killed the daemon."*

Confidence: **high** on the LaunchServices-resolution asymmetry and on the KeepAlive-blindness (both directly evidenced); **medium** on the precise quit trigger (operator-mediated ⌘Q/Dock-Quit vs. an OS-delivered quit AppleEvent) — the two are indistinguishable from the surviving artefacts because nothing logged the exit reason. That gap is now closed by instrumentation (below), and Stage V can settle it.

### Neutralization measures shipped (each independently sufficient or additive)

| # | Measure | What it removes |
|---|---|---|
| 1 | `app.setActivationPolicy('prohibited')` + `app.dock?.hide()` in daemon mode, at module scope **and** re-asserted after `ready` | Removes the daemon as a Dock/menu-bar presence and as an *activatable* target ("may not create windows or be activated"), so a Finder launch has no headless instance to resolve against. Attacks the cause. |
| 2 | `before-quit` **veto** in daemon mode unless the exit was authorized by our own signal handling | A service must not be quittable by the window server. Any ⌘Q / Dock-Quit / quit-AppleEvent is refused and logged instead of ending the daemon. launchd retains full control: `bootout`/`kickstart -k` operate by signal, and `SIGKILL` stays uncatchable. |
| 3 | `keepAlive: 'always'` in the desktop LaunchAgent | Even if 1 and 2 are both circumvented, launchd restarts the daemon after *any* exit — including the clean `exit(0)` the previous posture ignored — within `ThrottleInterval` (10s). |
| 4 | Supervised GUI binding with 1s/2s/5s→10s backoff and steady 10s liveness probing | The GUI binds as soon as the daemon exists or returns, with no manual action and no renderer involvement. Covers the ≤10s launchd restart window. |
| 5 | Exit-path + `activate`/`open-file`/`open-url`/`second-instance` instrumentation in daemon mode | Makes the hypothesis falsifiable. `runtime.daemon.activate_received` in the daemon log **is** the signature of macOS resolving a bundle launch against the daemon; `desktop.shutdown.started {reason}` records exactly why any exit happened. |

Measures 3+4 are the self-healing envelope the brief names as the guaranteed fallback: they deliver the owner-required "just works" behavior **even if the activation-policy approach turns out not to stop the resolution**, without a credential-port redesign.

---

## 3. safeStorage / activation-policy findings (with citations)

**Finding: `'prohibited'` activation policy does not endanger safeStorage on macOS.**

- Electron `safeStorage` docs, `isEncryptionAvailable()`: *"On MacOS, returns true if Keychain is available."* Contrast the other platforms in the same doc — *"On Linux, returns true if the app has emitted the `ready` event and the secret key is available"*, *"On Windows, returns true once the app has emitted the `ready` event."* macOS availability is gated on **Keychain access only** — not on `ready`, not on NSApplication activation, not on a Dock tile, not on a window.
  Source: <https://github.com/electron/electron/blob/main/docs/api/safe-storage.md> (also <https://www.electronjs.org/docs/latest/api/safe-storage>).
- Same doc: *"Note that on macOS, access to the system Keychain is required and these calls can block the current thread to collect user input."* The Keychain prompt is presented by the system security agent, not by this process's `NSApplication`, so a non-activatable app can still complete it. **This is the one point Stage V must empirically confirm** (drill 6).
- `app.setActivationPolicy(policy)` (macOS): *"'regular' — The application is an ordinary app that appears in the Dock and may have a user interface. 'accessory' — The application doesn't appear in the Dock and doesn't have a menu bar, but it may be activated programmatically or by clicking on one of its windows. 'prohibited' — The application doesn't appear in the Dock and may not create windows or be activated."*
  Source: <https://www.electronjs.org/docs/latest/api/app>.
  → **`'prohibited'` chosen as the default**: it is the only policy that removes *activatability*, which is precisely the hypothesised mechanism, and it is safe here because the daemon never creates a `BrowserWindow`. `'accessory'` still leaves the process programmatically activatable and present in `NSRunningApplication`.
- The docs state no before/after-`ready` requirement for `setActivationPolicy`. It is therefore called at module scope (avoiding a Dock flash during launch) inside `try/catch`, and **re-asserted** inside `initializeDaemon()` after `ready`. Both calls are non-fatal on failure.
- Escape hatch: `CHIRALITY_DAEMON_ACTIVATION_POLICY` accepts `regular|accessory|prohibited` (unknown values fall back to the default rather than failing startup), so Stage V can compare postures without a rebuild.
- Related known Electron issue reviewed and **not applicable**: `safeStorage.isEncryptionAvailable()` called *before* `ready` creates a `Chromium Safe Storage` Keychain entry instead of `{app.name} Safe Storage` (electron/electron#45328, fixed by electron/electron#48206). The daemon touches safeStorage only via `SafeStorageCredentialStore` inside `startRuntimeHost()`, i.e. strictly after `ready`, and nothing added here calls safeStorage earlier. **Do not** move any safeStorage call earlier without revisiting this.

---

## 4. KeepAlive semantics chosen, and why

**Chosen: `KeepAlive: true` (restart after any exit) for the desktop caller. Generic default remains `KeepAlive: {SuccessfulExit: false}`.**

`LaunchAgentKeepAlivePolicy = 'always' | 'crash-only' | 'never'`:

- `'crash-only'` → `{SuccessfulExit: false}` — **the historical value and the still-current default**, so existing generic callers are byte-identical.
- `'always'` → `true` — what the frontend now passes. Justification: the observed termination is a *clean* `exit(0)` (§2 evidence 2–3). `{SuccessfulExit:false}` explicitly instructs launchd **not** to restart after a successful exit, and `launchctl print` shows the `successful exit` semaphore doing exactly that. The previous posture was therefore blind to the only failure mode actually observed. Crash-only restart is the wrong contract for a service whose failure mode is an externally induced graceful shutdown.
- `'never'` → omit the key.

Interactions documented in code (`launch-agent.ts` doc comment on the policy type, and `runtime-control-ipc.ts` on the caller):

- **`bootout` still stops the daemon under `'always'`.** `bootout` *unloads* the job from the domain, taking the KeepAlive contract with it. Operator stop semantics via `LaunchAgentManager.stop()` are unchanged. (`launchctl stop` *would* be immediately undone by `KeepAlive:true` — this module deliberately never uses `stop`.)
- **`kickstart -k` remains correct but is now redundant-but-harmless.** Under `'always'` launchd would relaunch the killed instance anyway; `-k` just makes the restart immediate and deterministic. `ThrottleInterval` (10s, still parameterized) bounds relaunch rate and also bounds worst-case recovery latency.
- `EnvironmentVariables` is pinned because launchd jobs inherit almost nothing (`launchctl print` shows `default environment = { PATH => /usr/bin:/bin:/usr/sbin:/sbin }` and a single inherited `SSH_AUTH_SOCK`). `CHIRALITY_USER_DATA` is pinned to `app.getPath('userData')` so the daemon, the app, and every `chirality` CLI invocation agree on one runtime directory — closing the CLI/app userData mismatch from the app side (Stage B owns the launcher side).
- Rendered plist validated with `plutil -lint` (→ `OK`) and `plutil -p` (→ intended structure, `KeepAlive => true`, `EnvironmentVariables` dict with a space-containing path correctly escaped/parsed). Performed against a scratchpad file; nothing on the operator's machine was written.

**Isolation affordance added for Stage V:** `label` is now a `LaunchAgentManager` option (governing the plist filename, the `gui/<uid>/<label>` service name, and the plist `Label`), surfaced to the frontend through `CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL`. Combined with `CHIRALITY_USER_DATA`, Stage V can install/start/stop a fully parallel job without ever naming `com.chirality.runtime`. Test coverage asserts `bootstrap`/`kickstart`/`bootout` all address the isolated service.

---

## 5. Connectivity surface design

**Main process owns connectivity; the renderer only mirrors it.**

`createRuntimeBindingSupervisor` ( `electron/runtime-connectivity.ts` ):

- States `connecting → connected | disconnected`, snapshot `{ state, failedAttempts, lastError, changedAt }`.
- `start()` returns a promise settling after the **first** cycle, so startup still awaits an initial bind attempt (no regression versus the old awaited one-shot) while every later cycle is timer-driven and never blocks.
- Bind failure ladder **1s → 2s → 5s → 10s steady**, forever. While `connected`, a cheap `daemonStatus()` probe every 10s; a failed/throwing probe publishes `disconnected` and attempts an immediate rebind in the same cycle.
- `refreshNow()` cancels pending backoff — wired to the existing `onDaemonAvailable` hook so an operator starting the daemon from the runtime panel does not wait out the ladder.
- Reasons are redacted through the same credential-shaped pattern used by `runtime-control-ipc`, so no token text can reach the renderer or the log.
- Identical consecutive failures publish **one** transition (no renderer spam); a changed reason does publish.
- Deliberate: a failing rebind clears `CHIRALITY_RUNTIME_TOKEN_FILE`/`_PROJECT_ROOT` via `prepareDesktopHarnessEnvironment`. Only reachable after a probe already proved the daemon unreachable, so it fails closed rather than serving a stale binding.

**IPC:** `chirality:runtime-connectivity-query` (invoke, hydration) + `chirality:runtime-connectivity-changed` (main→renderer push to every live window). Preload exposes `chirality.runtime.connectivity.get()` / `.subscribe(listener) → unsubscribe`.

**Top bar:** `useRuntimeConnectivity()` → `deriveRuntimeConnectivityPresentation()` → a chip rendered as a sibling **before** the working-root disclosure in `.shell-header-controls`. Tones: `ready` (sage) / `pending` (slate) / `error` (danger). Returns `null` — chip entirely absent — when there is no bridge (SSR, browser, older preload); a web render must not claim a runtime state it cannot observe.

**Existing tests preserved by design, not by luck:** `shell-frame.test.tsx` locates the root dot with `tree.root.find(n => className.startsWith('shell-root-dot'))`, and `find` throws on multiple matches. New classes are therefore on the disjoint `shell-runtime-*` prefix. A regression test (`leaves the working-root chip and its dot untouched`) asserts exactly one `shell-root-dot*` node remains while a runtime chip is present.

**Logging (A5):** `<userData>/logs/desktop-main.log` (GUI) and `desktop-daemon.log` (daemon). Synchronous `appendFileSync` — ordering-preserving and survives `app.exit()`, which matters because the most valuable events are the ones emitted around shutdown. Mode `0600`, one rotation at 2 MiB, console mirror retained, never throws. Replaces the `console.warn` at the old `main.ts:449-454`. Logged: GUI/daemon start, activation policy in effect, CLI-launcher failure, supervisor start, each bind attempt/failure (escalating to `error` once past the ladder), bind success with prior attempt count, connectivity loss, probe failure, every state transition, daemon quit-veto, `activate`/`open-file`/`open-url`/`second-instance` in daemon mode, and `desktop.shutdown.started {reason, exitCode}` / `.exiting`.

**Tests added: 54 total** (48 frontend + 6 runtime CLI) across 5 new frontend files plus additions to 2 existing files. Node environment, no CSS assertions, deterministic (injected timer queue / injected clock — nothing sleeps).

---

## 6. Validation output (exact)

```
frontend $ npm run typecheck
> tsc --noEmit --incremental false && tsc -p tsconfig.electron.json --noEmit --incremental false
(clean — no diagnostics)

frontend $ npx vitest run
 Test Files  135 passed | 1 skipped (136)
      Tests  1038 passed | 4 skipped (1042)
   Duration  10.71s

runtime/packages/cli $ npm test
 ✓ test/cli.test.ts (14 tests) 18ms
 Test Files  1 passed (1)
      Tests  14 passed (14)

frontend $ node ./scripts/build-electron.mjs
 dist-electron/main.js 1.3mb · dist-electron/preload.js 3.5kb · dist-runtime/chirality-cli.mjs 70.0kb  (all OK)

$ git status --short -- '*package-lock.json'
(empty)
```

Baseline was `130 passed | 1 skipped (131)` files / `988 passed | 4 skipped (992)` tests. Delta `+5` files / `+50` tests = **+48 from Stage A** and `+2` from Stage B's concurrent `cli-launcher.test.ts` edits (present in this shared worktree; that file is out of my write scope and untouched by me).

**Environment-only action:** `runtime/packages/cli` had a stale `dist/`, so the root `tsconfig.json` (which lacks the `@chirality/*` path aliases and resolves through `node_modules` → `dist/src/*.d.ts`) reported `TS2554` on the new 4-argument constructor. Ran `npx tsc -b` in `runtime/packages/cli`. `dist/` is gitignored (`.gitignore:42 **/dist/`) — no tracked artifact was created or committed. **Agent 1 should be aware the frontend typecheck gate depends on runtime workspace `dist/` freshness.**

Not run (Agent 1 owns): `npm run build`, `harness:validate:section9`, `validate:release-quality`, `desktop:pack`, `desktop:verify-dependencies`, `instruction-root:integrity`, repo self-check.

---

## 7. Residuals and risks

### For Agent 1

1. **Brief correction to carry into records.** Root cause #2 as written ("LaunchAgent plist has no `KeepAlive`/`RunAtLoad`") is factually wrong for both source and installed plist. The true defect is `KeepAlive:{SuccessfulExit:false}` being semantically blind to a clean `exit(0)`, evidenced by `semaphores = { successful exit => 0 }`. The remediation is unchanged; the *record* should be corrected.
2. **Post-merge deployment requires re-installing the LaunchAgent.** The owner's existing plist will keep `SuccessfulExit:false` and carry no `EnvironmentVariables` until `install` is re-run from a rebuilt app. Behaviour change is not delivered by the merge alone — this belongs in owner decision gate 3.
3. **Serialization:** my only overlap surface with Stage B is `src/__tests__/electron/` (different files) — no shared-file read-modify-write occurred. `frontend/package.json` untouched by me; the new electron modules need no `build` block change.
4. **`preload.js` grew 2.0→3.5 kb** because it imports the channel constants from `runtime-connectivity.ts` and esbuild bundles the (pure, node-free) supervisor with them. Harmless; splitting the constants into a separate module would trim it if anyone objects.
5. **Behaviour change to note in review:** the daemon now vetoes external quit requests. Anyone used to quitting the daemon from the Dock must use `launchctl bootout` / `kickstart -k` / SIGTERM. The veto is logged with that hint.

### For Stage V — what the isolated drills MUST settle

1. **safeStorage under `'prohibited'` (highest-priority unknown).** Prove `isEncryptionAvailable() === true` **and** a full `encryptString`/`decryptString` round-trip in daemon mode. If a Keychain prompt cannot be completed by a non-activatable process, re-run with `CHIRALITY_DAEMON_ACTIVATION_POLICY=accessory` and report; that is the designed fallback and needs no code change. A failure of *both* is the escalation trigger in owner decision gate 2.
2. **Does `'prohibited'` actually stop the LaunchServices resolution?** Daemon-first, then launch the GUI. Check the isolated `desktop-daemon.log` for `runtime.daemon.activate_received` and `runtime.daemon.quit_request_vetoed`, and `launchctl print` for `runs`/`last exit code`. Three distinguishable outcomes: (a) GUI opens and daemon survives untouched → measure 1 worked; (b) daemon logs `activate_received` but survives → resolution still happens, measures 2+3 carried it; (c) daemon exits → measure 3 must have restarted it within ≤10s, and the log records the reason. **Any of the three satisfies the owner requirement; only (a) confirms the A1 hypothesis was fully neutralized at the cause.** Report which.
3. **`CHIRALITY_USER_DATA` isolation is now load-bearing for V's own safety.** Verify the app honors it (A6) *before* relying on it: launch the packaged app with `CHIRALITY_USER_DATA=<temp>` and confirm `<temp>/logs/desktop-main.log` and `<temp>/runtime/` appear and that `~/Library/Application Support/chirality-frontend` is not written. Combine with `CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL=com.chirality.runtime.tranchetest`. A relative value is *ignored* (logged) — pass an absolute path.
4. **Backoff and rebind timing in the real process.** GUI-first then daemon: confirm binding within ~1–5s with no restart, and that the top-bar chip transitions `pending → error → ready` (screenshot each). Kill the daemon mid-session: confirm launchd restart, chip going `error` then `ready`, and `runtime.connectivity.lost` / `.bound` in the log.
5. **Cleanup** must `bootout` the test label, delete the temp userData, and remove the temp plist. Assert afterwards that `~/Library/LaunchAgents/com.chirality.runtime.plist` and `.../chirality-frontend/` are byte-unchanged.

### Known limits of Stage A

- **Not fixed (out of scope, still open):** instruction-root divergence between the packaged daemon (`process.resourcesPath`) and manifest-resolved roots — flagged 2026-07-24 in the brief, deliberately not addressed. The daemon's `CHIRALITY_INSTRUCTION_ROOT` is still resolved per-process and is *not* pinned through the new `EnvironmentVariables` channel; pinning it would silently change instruction-root resolution semantics and needs its own decision.
- `main.ts` itself remains untested (it self-executes `app.whenReady()` on import). Its pre-`ready` decision rules were extracted to `desktop-process-policy.ts` and are covered; the side effects are Stage V's to prove.
- The connectivity chip has no manual "reconnect now" affordance. The `refreshNow()` plumbing exists and is reachable through the existing runtime-panel daemon actions; a top-bar click target was not in scope.
