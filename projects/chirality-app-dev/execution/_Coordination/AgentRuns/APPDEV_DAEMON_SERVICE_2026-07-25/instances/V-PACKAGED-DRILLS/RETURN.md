# V-PACKAGED-DRILLS — RETURN (Stage V: packaged-app verification drills)

**Run:** TRB-APPDEV-DAEMON-SERVICE-2026-07-25 · **Agent 2 (opus)** · branch `feat/daemon-service` @ `071bebf9e`
**Authority:** `../../ADOPTED_BRIEF.md` (Stage V + fences) · **Launch brief:** `LAUNCH_BRIEF.md` (verbatim, written before any drill)
**App under test:** `projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app` (Agent 1's integrated pack, 2026-07-24 19:55)
**Window:** 2026-07-25 02:08Z–02:37Z. **Status:** COMPLETE. All 10 drills executed, isolation held, cleanup verified byte-for-byte.
**Escalation triggers:** V0 isolation — NOT triggered. V2 safeStorage double-failure — NOT triggered.
**New material findings requiring Agent 0/1 disposition: 6 (V-D1 … V-D6). Two of them (V-D1, V-D2) contradict accepted claims in `../AGENT1-VALIDATOR/ROUND1_REVIEW.md` and change the owner deployment story.**

---

## 1. Verdict table

| Drill | Scope | Verdict | One-line evidence pointer |
|---|---|---|---|
| **V0** | A6 isolation proof (direct GUI exec, absolute `CHIRALITY_USER_DATA`) | **PASS** | `evidence/v0/summary.json`; helper `--user-data-dir=<temp>` in `ps`, `<temp>/logs/desktop-main.log` created, owner userData mtime unchanged |
| **V1** | daemon install + start under isolated label | **PASS** | `evidence/v1/plist-parsed.txt` (KeepAlive=true, RunAtLoad, env pinned), `launchctl-after.txt` (state=running, runs=2), `desktop-daemon.log` (`activationPolicy":"prohibited"`) |
| **V2** | safeStorage round-trip in daemon mode under `prohibited` | **PASS** | `evidence/v2/status-after.json` + 4 negative controls; blob prefix `v10`, 67 bytes, no plaintext |
| **V3** | worktree registration + GUI auto-binding | **PASS** | `evidence/v3/summary.json`; bound in **18 ms**, `failedAttempts:0`, screenshots `v3-topbar-connected.png` |
| **V4** | launch-order matrix (a: daemon-first incl. LaunchServices; b: GUI-first) | **PASS** (+ material residual) | `evidence/v4/summary.json`, `open-no-n.out`, `bootout-veto-observation.txt` |
| **V5** | kill drills (SIGKILL restart, bootout stop-and-stay) | **PASS** (+ defect in *how* it stops) | `evidence/v5/sigkill-timeline.txt` (98 ms), `bootout-timeline.txt` (5.083 s) |
| **V6** | quit veto | **PASS** on the veto / **FAIL** on the documented stop contract | `evidence/v6/summary.json`, `sigterm-timeline.txt` |
| **V7** | icons (Dock, Finder, in-app, `.icns`) | **PASS** | `evidence/v7/v7-dock-tile.png`, `v7-finder-window.png`, `icns-sha.txt`, `icon.iconset/icon_256x256.png` |
| **V8** | CLI launcher | **PASS** (+ isolation hazard V-D2) | `evidence/v8/launcher-rendered.sh`, `project-status.json` (exit 0, clean env) |
| **V9** | stub-adapter end-to-end turn through the GUI harness HTTP surface | **PASS** | `evidence/v9/turn-sse.txt` (`process:exit {"exitCode":0}`), `session-create.json` |
| **CLEANUP** | bootout, rm plist, rm temp, owner-state re-verify | **VERIFIED** | `evidence/cleanup/owner-state-diff.txt` (differs only in the capture-timestamp line) |

---

## 2. A1-outcome classification (the question Stage A and Agent 1 both put to Stage V)

**Answer: outcome (b) — `activate_received` but survived. The A1 hypothesis is CONFIRMED as the mechanism and is NOT neutralized at the cause.**

Two distinct paths, and the distinction is the whole point:

| Launch path | LaunchServices involved? | GUI starts? | Daemon | Log signature |
|---|---|---|---|---|
| `Contents/MacOS/Chirality` direct exec | no | yes, binds in 18–30 ms | untouched (`runs` unchanged) | none |
| `open -n --env … <app>` | yes, forced new instance | yes, binds in 30 ms | untouched (`runs=2`) | none |
| **`open <app>` / `open -b com.chirality.app`** (no `-n`) | **yes, resolution** | **NO — nothing starts, no window** | **survives untouched** | **`runtime.daemon.activate_received`** |

Reproduced **3/3** trials (02:19:23.322, 02:19:51.170, 02:19:54.226, all pid 92414). macOS printed
`Application …/Chirality.app was already running and so the additional environment variables could not be set.`

`app.setActivationPolicy('prohibited')` demonstrably does **not** remove the daemon as a LaunchServices resolution target:
`lsappinfo` still lists it (`ASN:0x0-0x42fc2f8`, `bundleID="com.chirality.app"`), merely reclassified `type="UIElement"`, and it is still AppleEvent-addressable (V6.1 quit reached it). It has no Dock tile and no windows (`evidence/v1/windowlist-daemon.txt` empty) — those parts of A2 worked.

**Two consequences the record must carry:**

1. **The daemon-death half of the defect IS fixed.** No `open`, Dock, Finder, AppleEvent quit, or SIGTERM ended the daemon in any drill. Measures 2+3 hold.
2. **The operator-visible symptom is NOT fixed.** While the daemon runs, double-clicking Chirality in Finder or clicking its Dock icon still does nothing at all. That is the *same* user-facing experience the owner reported, arrived at by a different route. See **V-D4**.
3. **The veto's stated trigger was never observed.** In all three `open` trials the daemon received `activate` and *no* quit event. The quit AppleEvent that measure 2 was built to refuse did not occur; the only quits in the whole run were ones I sent deliberately. The veto is therefore currently paying the full cost of **V-D1** for a trigger this run could not reproduce.

---

## 3. safeStorage verdict

**PASS under `CHIRALITY_DAEMON_ACTIVATION_POLICY` default = `prohibited`. The `accessory` fallback was NOT needed. Owner decision gate 2 is NOT triggered.**

Route: `POST/GET /v1/credentials/anthropic` over the isolated UDS → `SafeStorageCredentialStore` → Electron `safeStorage`.

| Step | Result |
|---|---|
| status before | `configured: false` |
| store dummy (`encryptString` + write) | `configured: true` |
| status after (`readFile` + `decryptString`) | `configured: true` |
| blob | `<userData>/credentials/api-key.enc`, 67 bytes, prefix `76 31 30` = `v10` (Chromium macOS os_crypt), plaintext (60 chars) absent |
| **negative control** flip byte @40 (mid block) | `configured: true` — AES-CBC is unauthenticated, padding survived, `decryptString` returned garbage. *Inconclusive alone; recorded for honesty.* |
| **negative control** flip byte @60 (last block) | **`configured: false`** — padding invalid, `decryptString` threw |
| **negative control** 64 random bytes after `v10` | **`configured: false`** |
| restore original blob | `configured: true` |
| **fresh daemon process** (pid 94611 decrypting a blob written by pid 92414) | `configured: true` |

The launchd job environment is `PATH` + `CHIRALITY_USER_DATA` only (`evidence/v1/launchctl-after.txt`), so no env credential can produce `configured:true`. `configured` therefore flips exactly with decryptability. **`encryptString` and `decryptString` both work in a `prohibited`-policy Electron daemon, across process boundaries, with no Keychain prompt and no blocking call.** Stage A's doc-based reasoning (macOS availability gated on Keychain, not on activation) is empirically confirmed.

The dummy credential was **removed** before V9 (`evidence/v9/cred-remove.json`) and the temp tree deleted at cleanup.

---

## 4. Timing numbers

| Measurement | Value | Note |
|---|---|---|
| `LaunchAgentManager.start()` (bootstrap + `kickstart -k`) | **10.07 s** | ThrottleInterval-gated; see **V-D6** |
| **SIGKILL → launchd restart** (`runs` 1→2) | **0.098 s** | 50 ms polling, `evidence/v5/sigkill-timeline.txt` |
| **`launchctl bootout` → process actually dead** | **5.083 s** | `bootout` itself returns in 5 ms; death is launchd's SIGKILL escalation at the job's `exit timeout = 5`. **R-2 datum.** |
| GUI cold bind, daemon already up | **18 ms** / **30 ms** | `failedAttempts:0` both times |
| **GUI rebind after outage** (daemon-ready → `connectivity.bound`) | **288 ms** / **869 ms** | `priorFailedAttempts` 10 and 6; worst case bounded by the 10 s steady backoff |
| GUI notices daemon loss (probe granularity) | **12.66 s** | death ≈02:25:05.39 → `runtime.connectivity.lost` 02:25:18.046 |
| Backoff ladder, measured in the real process | **1.003 / 2.001 / 5.003 / 10.002 s** then steady 10 s | `evidence/v0/desktop-main.log` — matches the designed 1→2→5→10 exactly |
| SIGKILL mid-session, GUI impact | **zero observed downtime** | the 98 ms restart fell inside the 10 s probe interval; the GUI logged no transition and kept serving |

Connectivity chip transitions observed and screenshotted: **offline** (`v0-topbar-offline.png`) → **connected** (`v3-topbar-connected.png`) → **offline** mid-session (`v5-topbar-error.png`) → **connected** (`v5-topbar-reconnected.png`), with no GUI restart, no devtools, no manual action. The `pending` (slate) tone was never visible — binding either succeeds in tens of ms or fails immediately. Not a defect; noted because Stage A §7.4 predicted `pending → error → ready`.

`launchctl print` `runs` / `last exit code` were captured at every boundary (`evidence/v1,v3,v5/*.txt`). Across the run: `runs` 2 → 2 → 1 → 2 → 3 → 1, `last exit code` never non-zero, **R-1 restart-loop never occurred** (no failing-startup daemon).

---

## 5. Findings requiring disposition

### V-D1 — the quit veto swallows SIGTERM; `ROUND1_REVIEW.md` §3 paths 1 and 3 are factually wrong · **HIGH**

**Observed** (`evidence/v6/sigterm-timeline.txt`, `summary.json`):

| Stimulus | Result |
|---|---|
| AppleEvent quit (`osascript … to quit`) | `runtime.daemon.quit_request_vetoed`, daemon survives — **as designed, PASS** |
| **single SIGTERM** | `runtime.daemon.quit_request_vetoed`, **process still alive after 30.022 s of 50 ms polling** |
| second SIGTERM | dies immediately, **no shutdown log**, launchd restarts it |
| SIGKILL | dies immediately (uncatchable) |
| `launchctl bootout` | dies at **+5.083 s** by launchd's SIGKILL escalation, **no shutdown log** |

ROUND1_REVIEW §3 states: *"`launchctl bootout` → SIGTERM. `process.once('SIGTERM')` sets `shutdownAuthorized = true`, then `shutdown(0, 'signal:SIGTERM')` → `app.exit(0)`"* and *"A second SIGTERM. `process.once` removes the listener after it fires…"*.

**The JS `process.once('SIGTERM')` handler never runs in the packaged Electron main process.** Chromium's own native SIGTERM handler intercepts the signal and calls `app.quit()` → `before-quit` → our veto → `preventDefault()`. `shutdownAuthorized` is never set and `shutdown()` is never called, so the first SIGTERM is consumed with no effect beyond a log line. The second SIGTERM terminates the process by default disposition (consistent with a one-shot native handler) — again without `shutdown()`. Corroborating evidence from GUI mode in V0: a GUI SIGTERM logged `reason:"before-quit"`, **not** `"signal:SIGTERM"` — the same ordering, benign there because GUI mode does not veto.

**Consequences.** Nothing is brickable (SIGKILL and bootout both work), so R-1/R-2 are not safety issues. But:
- **No daemon exit in the entire drill set produced `desktop.shutdown.started` / `.exiting`.** `runtimeHost.stop()` never runs on any stop path; every stop is a forced kill. `control.sock` is left behind as a stale socket file (harmless in practice — the next daemon rebound fine).
- The veto's own hint text is wrong: *"use launchctl bootout/kickstart, or SIGTERM"* — SIGTERM does not stop it, and bootout only does so by forced kill 5 s later.
- R-3's operator guidance ("use `launchctl bootout`") needs the 5 s / unclean caveat.
- The veto log is not even guaranteed: the cleanup bootout produced no `quit_request_vetoed` line at all (SIGTERM presumably arrived alongside the kill), so the diagnostics are not a reliable stop-path record.

**Recommendation for Agent 1 / Agent 0.** Given §2 point 3 — the quit AppleEvent the veto exists to refuse was **never observed** in three `open` trials, only `activate` — the cheapest correct move is to narrow or drop measure 2 and keep measures 3+4 (KeepAlive + supervised rebind), which are what actually carried every drill. If the veto is kept it must not intercept a signal-induced quit; a graceful `stop` route on the daemon control API (which the CLI could call before `bootout`) would give a real clean-shutdown path that today does not exist.

### V-D2 — the bundled CLI cannot address the isolated label, addresses the OWNER's label, and does not deliver the tranche's plist fix · **HIGH, affects owner decision gate 3**

`createDefaultCliDependencies()` (`runtime/packages/cli/src/cli.ts:462`) constructs `LaunchAgentManager` with **no options** — no `label`, no `keepAlive`, no `environmentVariables`. The A3 plumbing is reachable **only** through the GUI's `createDesktopDaemonLifecycle()`.

1. **Stage V could not use the bundled CLI for install/start/stop as the launch brief assumed.** Proven live: `chirality daemon status` run from the *fully isolated* environment (own `HOME`, own `CHIRALITY_USER_DATA`) reported **the owner's job** `gui/501/com.chirality.runtime`, `path = ~/Library/LaunchAgents/com.chirality.runtime.plist`, `program = /Users/ryan/dev/chirality/projects/chirality-app-dev/frontend/…` (`evidence/v8/daemon-status.json`). `daemon stop` would have booted out the operator's real agent; `uninstall` would have deleted its plist. I therefore drove install/start/stop through `evidence/la-driver.mjs`, which instantiates `LaunchAgentManager` from `runtime/packages/cli/dist` with **exactly** the frontend caller's options (`keepAlive:'always'`, `runAtLoad:true`, `environmentVariables.CHIRALITY_USER_DATA`) plus the test label and a test-home LaunchAgents directory. The rendered plist is therefore the real shipped posture (`evidence/v1/plist.xml`, `plutil -lint` OK).
2. **The corrected root cause #2 is not fixed on the CLI path.** A rebuilt app's documented `chirality daemon install` still renders `KeepAlive = {SuccessfulExit: false}` and **no** `EnvironmentVariables`. The tranche's headline behaviour change is delivered only by installing from the in-app runtime panel. **Deployment instructions written against `chirality daemon install` would silently reinstate the exact defect C-1 corrects.**

### V-D3 — packaged GUI launch unconditionally rewrites `~/.local/bin/chirality`, with no override · **MEDIUM**

`installBundledCliLauncher()` (`electron/cli-launcher.ts:51`) defaults to `os.homedir()/.local/bin/chirality` and `initializeGui()` calls it with no argument whenever `app.isPackaged`. There is no env override. Every packaged launch — including a verification run — rewrites that file to point at whatever bundle just started.

Isolation required an external guard: for V0 I `chmod 0500 ~/.local/bin` (restored 0755; owner file sha256 unchanged throughout), which produced positive evidence of the write attempt: `desktop.cli_launcher.install_failed {"error":"EACCES … /Users/ryan/.local/bin/.chirality.92162.mrzqhio8.tmp"}`. For all later drills I redirected `HOME` to the test home, which *is* the only available targeting mechanism (`os.homedir()` honours `$HOME`) and is what V8 exercised. A `CHIRALITY_CLI_LAUNCHER_PATH`-style override would make this testable without either trick.

### V-D4 — `prohibited` does not stop LaunchServices resolution: the GUI still cannot be opened from Finder/Dock while the daemon runs · **MEDIUM, owner-visible**

See §2. 3/3 reproduction, `evidence/v4/open-no-n.out`. The daemon survives, so the tranche's stated acceptance ("daemon SURVIVES GUI launch and GUI binds without manual action") is met on the direct-exec and `open -n` paths — but an owner double-clicking the app icon gets nothing. Options worth costing: `LSMultipleInstancesProhibited`-adjacent handling, a separate helper bundle id for the daemon, or having the daemon's `activate` handler re-launch the GUI with `open -n`.

### V-D5 — no graceful daemon shutdown exists on any path · **MEDIUM** (consequence of V-D1, listed separately because it is the operational fact)

`runtimeHost.stop()` never ran once in 6 daemon lifetimes. Stale `control.sock` observed after every death. Not fatal in these drills; relevant to any future work assuming clean teardown (durable resume, session finalisation).

### V-D6 — `daemon start` costs a full `ThrottleInterval` · **LOW**

`start()` does `bootstrap` (which `RunAtLoad:true` immediately honours → run 1) then `kickstart -k` (→ run 2). The kickstart is throttled, so the call blocks **10.07 s** and the job's launch count doubles per start. Stage A anticipated the redundancy as "harmless"; it is, but it is also a 10 s stall on an operator action and a misleading `runs` count. Skipping `kickstart` when `bootstrap` already started the job would remove both.

### Minor / cosmetic

- `chirality:provider-api-key-status` rejects into an unhandled `Error occurred in handler for …: ENOENT … operator.token` on the renderer channel whenever the daemon is down (`evidence/v0/gui-stderr.log`). The connectivity chip already communicates the state; the raw throw is noise.
- V9 session state lives entirely daemon-side under `<userData>/runtime/projects/<id>/sessions/` — **no writes into the registered worktree root at all** during a turn. Worth knowing for the isolation model: registering a project root does not by itself make the runtime write there.

---

## 6. Owner live-state: before / after

Snapshots: `evidence/owner-state-before.txt` (02:12:02Z) vs `evidence/owner-state-after.txt` (02:37:23Z). Diff: `evidence/cleanup/owner-state-diff.txt`.

| Artifact | Baseline | Final | Verdict |
|---|---|---|---|
| `~/Library/LaunchAgents/com.chirality.runtime.plist` | mtime 1784939440, 924 B, sha256 `6446817153f0a19003e3e494015652e1884546b74347e5c0316eeb7e733fe9a1` | identical mtime, size, sha256 | **unchanged** |
| `~/Library/LaunchAgents/` listing | 1 file, dir mtime Jul 24 18:30 | identical | **unchanged — the test plist was never written here** |
| `gui/501/com.chirality.runtime` | `state = not running`, `runs = 4`, `last exit code = 0` | identical | **untouched; the one authorized restorative `kickstart` was never needed** |
| `~/.local/bin/chirality` | mtime 1784941528, 703 B, sha256 `2c0120079831c1d2637e462304ac596044026d551c8d3ae89985da1506838b0d` | identical | **unchanged** |
| `~/.local/bin` perms | `drwxr-xr-x` | `drwxr-xr-x` | restored after the V0/V4 guard |
| `~/Library/Application Support/chirality-frontend` | mtime 1784942107 + full 2-level mtime inventory | identical, every entry | **unchanged** |
| Chirality processes | none | none | clean |
| `/Users/ryan/dev/chirality` (owner main checkout) | 5 pre-existing modified/untracked paths, newest mtime 1784944583 | identical; all mtimes predate the 02:08Z run start | **not written** |

The isolated triple used: `CHIRALITY_USER_DATA=$HOME/.chirality-tranchetest-v/userdata`, `HOME=$HOME/.chirality-tranchetest-v/home` (which relocated the LaunchAgents dir, the CLI launcher, and Chromium caches), label `com.chirality.runtime.tranchetest`. The plist path was **verified before bootstrap** (`la-driver.mjs plistpath`, with an explicit abort guard on the owner path). The registered manifest was the **worktree** one (`canonicalRoot` = worktree, `manifestHash 5a797770…`). All screenshots were window-scoped (`screencapture -l <CGWindowID>`) or ≤58×58 pt / ≤110 px-tall crops; no full-desktop capture was taken or retained.

---

## 7. Cleanup verification

1. `launchctl bootout gui/501/com.chirality.runtime.tranchetest` → rc 0; subsequent `launchctl print` → *Could not find service … in domain for user gui: 501*.
2. Test daemon process dead (via the 5 s SIGKILL escalation — no shutdown log, per V-D1).
3. Test GUI pid 93675 SIGTERMed; `pgrep -fl Chirality` → none.
4. `$TESTHOME/Library/LaunchAgents/com.chirality.runtime.tranchetest.plist` removed; directory empty.
5. `rm -rf ~/.chirality-tranchetest-v` (3.4 MB) — path absent.
6. `~/.local/bin` perms restored.
7. Final owner-state snapshot **differs from baseline only in the capture-timestamp line**.

Logs, the rendered plist, the launcher, the session record, and all screenshots are preserved under `evidence/`. Two helper scripts are retained as part of the method record: `evidence/la-driver.mjs` (isolated LaunchAgent driver) and `evidence/rt-driver.mjs` (isolated runtime-client driver), plus `evidence/winlist.swift` (window-ID lookup for scoped screenshots).

---

## 8. Residuals and handoff

**For Agent 1 (validation / possible round 2)**
1. **V-D1 and V-D2 contradict accepted §3 / §5 claims in `ROUND1_REVIEW.md`.** Both need a correction entry in the same appended-not-rewritten style as C-1. V-D2 in particular changes what "deployment" means.
2. **V-D2 is a code gap, not just a record gap.** If the CLI is meant to be the deployment surface, `createDefaultCliDependencies()` needs the same options the frontend caller passes (and a label/LaunchAgents-dir override would have made this stage's isolation trivial and safe). That is a bounded change in `runtime/packages/cli` — Agent 1's call whether it belongs in this tranche.
3. **V-D1's cheapest fix may be to remove code, not add it** (§2 point 3): the veto's trigger was unobservable in three reproductions, while measures 3+4 carried every drill unaided.
4. No gate re-runs were performed by me (none in scope). Nothing in the packed tree was modified; the only writes were under `instances/V-PACKAGED-DRILLS/`.

**For Agent 0 / owner decision gates**
5. **Gate 2 (forced scope change): NOT triggered by safeStorage** — `prohibited` works, no credential-port redesign needed. **But V-D4 is a partial failure of the A2 objective** ("daemon sheds its LaunchServices activation surface") and the owner should decide whether "the app still won't open from the Dock while the daemon runs" is acceptable for merge or is its own tranche.
6. **Gate 3 (deployment) must be rewritten around V-D2.** Re-running `chirality daemon install` from a rebuilt app does **not** deliver `KeepAlive:true` or the pinned `CHIRALITY_USER_DATA`. Only the in-app runtime-panel install does. Add: the daemon cannot be quit from Dock/Cmd-Q/AppleEvent/single-SIGTERM (R-3), `launchctl bootout` is the stop verb and takes ~5 s ending in a forced kill, and every packaged launch rewrites `~/.local/bin/chirality` (V-D3).
7. **What the tranche unambiguously delivers, proven on the packed app:** the `ENGINE_UNAVAILABLE` failure is gone (V9 end-to-end turn, `process:exit 0`); the GUI binds with no manual action and self-heals across daemon loss (18–30 ms cold, 288–869 ms rebind, 98 ms launchd restart); the daemon survives every launch path and every polite quit; safeStorage works headless; the quincunx ships as the Dock icon, the Finder icon, and the in-app logo; and the CLI launcher works from a clean environment.

**Not attempted / out of scope**
8. `CHIRALITY_DAEMON_ACTIVATION_POLICY=accessory` comparison — designed as the V2 fallback, unnecessary since `prohibited` passed. If V-D4 is pursued, an `accessory` comparison run is the natural first probe.
9. Instruction-root divergence between the packaged daemon (`process.resourcesPath`) and manifest-resolved roots — still open, still unpinned, as the brief intends.
10. Login-time auto-start behaviour: the test plist deliberately lived outside `~/Library/LaunchAgents`, so `RunAtLoad`-at-login was not exercised (only `RunAtLoad`-at-bootstrap, which worked: `runs=1` immediately on every `bootstrap`).
