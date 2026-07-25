# TRB-APPDEV-DAEMON-SERVICE-2026-07-25 — Daemon-as-Service + Packaged-App Fix Tranche (ADOPTED)

**Status:** ADOPTED by owner direction in-session 2026-07-25 ("draft the brief and proceed using the same subagent delegation model established in this session (Agent 0/1/2 as appropriate, `opus-5` models for Agent 1/2)").
**Agent 0:** HELP_HUMAN (session loop operator). **Agent 1:** opus validator / integration owner (WORKING_ITEMS posture). **Agent 2:** opus stage executors under sealed briefs.
**Branch:** `feat/daemon-service` from `origin/main` @ `e9068c87d76c75b133f3686db8bf453565ce8fa2`.
**Parent run:** APPDEV_WOVEN_REDESIGN_2026-07-24 (PR #330, merged). **Receipt:** Receipt-91 at closeout.

## Problem statement (owner-observed, diagnosed 2026-07-24/25)

Packaged Chirality.app fails every harness request with `ENGINE_UNAVAILABLE: Chirality runtime daemon client is not configured`, and the redesign's quincunx logo appears neither in-app nor as the macOS app icon. Owner verdict on interim workarounds (devtools rebind, manual kickstart): **not acceptable**. Owner design direction: the daemon should be a real machine-local service; the app should just work at every launch.

## Diagnosed root causes (evidence in session; file:line as of e9068c87d)

1. **GUI launch terminates a running daemon.** Daemon = same Electron binary/bundle relaunched with `--runtime-daemon` (`electron/main.ts:47,520-528`). Launching the GUI at 19:05:28 caused the daemon LaunchAgent job to exit cleanly (code 0) at 19:05. Mechanism unidentified: no `requestSingleInstanceLock`, no `LSMultipleInstancesProhibited`. Reverse order coexists (daemon started while GUI runs: verified 18:30–18:54 and again 19:0x).
2. **No self-healing.** LaunchAgent plist (`runtime/packages/cli/src/launch-agent.ts:38-70,147-177`) has no `KeepAlive`/`RunAtLoad`; a dead daemon stays dead.
3. **GUI binds once at startup and never retries.** `configureDesktopHarnessClient` failure is swallowed into a bare `console.warn` (`electron/main.ts:449-454`), invisible in a packaged app (no log file). Only rebind hook is `onDaemonAvailable` via the daemon-status IPC (`electron/runtime-control-ipc.ts:99-102`), which no renderer code calls.
4. **`public/` not packaged.** `build.files` in `frontend/package.json` omits `public/**/*`; asar contains no `chirality-app-icon.svg`; `shell-frame.tsx:95` `<img src="/chirality-app-icon.svg">` 404s in the packaged app (favicon route from `src/app/icon.svg` works — asymmetry confirmed).
5. **No `.icns`.** `build.mac` has no `icon` key, no `frontend/build/` dir; stock `electron.icns` ships (residual DEL-09-04). electron-builder's SVG/PNG conversion path downloads a toolset from GitHub — prohibited by offline packaging posture; a committed `.icns` bypasses it entirely (`iconConverter.js:189-193`).
6. **CLI userData mismatch.** `~/.local/bin/chirality` (rendered by `electron/cli-launcher.ts:16-37`) resolves userData to `~/Library/Application Support/Chirality` (`runtime/packages/cli/src/config.ts:17-20`) while the app uses `.../chirality-frontend`; documented commands fail without `CHIRALITY_USER_DATA`.

**Hard design constraint (verified):** daemon credentials use Electron `safeStorage` (`electron/api-key-storage.ts`, consumed by `runtime-host.ts`). `ELECTRON_RUN_AS_NODE` has no `safeStorage` ⇒ a plain-Node daemon is RULED OUT this tranche. The daemon remains an Electron process; it must shed its *app identity* instead (no Dock, no LaunchServices activation surface). If Stage A finds accessory/prohibited activation policy insufficient to stop the kill, the self-healing envelope (KeepAlive + auto-rebind) still delivers the owner-required behavior; a credential-port redesign is out of scope and would be escalated to the owner.

## Stages, scopes, and acceptance

### Stage A — daemon as a real service + self-healing client (Agent 2, opus)
- **A1 (investigate first, time-boxed):** reproduce and identify the GUI-launch→daemon-kill mechanism on this machine. Record the mechanism with evidence. If not definitively pinned within the box, record best-supported hypothesis and proceed — A2–A5 make the system robust regardless.
- **A2:** daemon process sheds app identity: in `--runtime-daemon` mode set activation policy accessory/prohibited before ready (and/or equivalent LS-registration suppression that safeStorage tolerates). safeStorage must remain functional (prove with a decrypt round-trip in verification).
- **A3:** LaunchAgent hardening: `LaunchAgentManager` gains parameterized `KeepAlive` (restart-on-exit), `RunAtLoad`, and explicit `EnvironmentVariables`/userData pinning. Keep the runtime package **generic** — new behavior is caller-configurable options, not frontend-specific constants. Frontend passes its values at `createDesktopDaemonLifecycle()`.
- **A4:** GUI becomes a resilient client: binding retry with backoff after startup failure, automatic rebind when the daemon reappears (poll or reuse status probe internally in main process — not dependent on renderer calls), and daemon-connectivity state pushed to the renderer so the top-bar status can reflect runtime connectivity (closes the "runtime-connectivity dot" residual; do not break existing working-root dot tests — extend deliberately).
- **A5:** durable diagnostics: binding/daemon lifecycle failures logged to a file under `userData/logs/` (e.g. `desktop-main.log`) with timestamps; replace the bare `console.warn`.
- **Write scope:** `frontend/electron/**`, `frontend/src/**` (connectivity surface + tests only), `runtime/packages/cli/src/**` (+ its tests), `frontend/src/__tests__/**`. Do NOT touch `frontend/package.json` `build` block (Stage B owns it) except `scripts` if a new electron entry needs wiring via `scripts/build-electron.mjs`.

### Stage B — packaging & branding fixes (Agent 2, opus)
- **B1:** add `"public/**/*"` to `build.files`.
- **B2:** macOS app icon: produce an icns-tuned variant of the quincunx artwork (inset ~10–18% margin on the 1024 canvas, stroke weight and corner geometry adjusted for macOS icon grid — NOT a naive 32→1024 upscale), rasterize offline with system tools (`sips`/`rsvg`/`sharp`-free preferred; `iconutil -c icns`), commit `frontend/build/icon.icns`, add `"icon": "build/icon.icns"` to `build.mac`. Keep any generation script out of the build graph (one-time tool under `frontend/scripts/`, documented, no new deps).
- **B3:** CLI launcher pins userData: `cli-launcher.ts` renders the launcher to export `CHIRALITY_USER_DATA` = the app's actual userData path, so documented `chirality` commands work as written. Do not change the generic CLI default in `runtime/packages/cli/src/config.ts`.
- **Write scope:** `frontend/package.json` (`build` block only), `frontend/build/**`, `frontend/scripts/**`, `frontend/electron/cli-launcher.ts` (+ tests), `frontend/public/**` (icns-variant source artwork only; do not alter the shipped 32-vb SVG used in-app).

### Stage V — packaged-app verification drills (Agent 2, opus; after integration)
- Build `desktop:pack` from the integrated branch. All drills run **isolated**: temp `CHIRALITY_USER_DATA`, distinct LaunchAgent label (e.g. `com.chirality.runtime.tranchetest`), never touching the owner's real `com.chirality.runtime` agent, real userData (`.../chirality-frontend`), or real registration. Register the real main-checkout manifest read-only into the isolated runtime dir if needed for binding drills; use the `stub` adapter for any turn-level proof.
- Drills (each evidenced with logs/screenshots/JSON): (1) daemon-first → GUI launch: daemon SURVIVES GUI launch (or is auto-restarted by KeepAlive) and GUI binds without manual action; (2) GUI-first → daemon starts later: GUI auto-rebinds, no restart; (3) kill daemon mid-session: launchd restarts it, GUI reconnects, connectivity indicator transitions observed; (4) in-app quincunx logo visible (screenshot); (5) Finder/Dock icon = quincunx (screenshot + `Info.plist` `CFBundleIconFile` check); (6) safeStorage round-trip in daemon mode; (7) launcher `chirality project status` works without manual `CHIRALITY_USER_DATA`.
- Full cleanup of isolated state at end (bootout test label, remove temp dirs).

### Records stage (Agent 2, opus; at closeout)
- DEL run records + `_STATUS.md` updates for affected deliverables (close residuals: packaged-desktop smoke evidence (DEL-02-01), runtime-connectivity dot, `.icns` DEL-09-04); `plans/PLAN_COMPLETION_LOG.md` entry; Receipt-91 appended to `LOOP_RECEIPTS.md` (validator-checked, full-SHA Examined-Through via `git rev-parse`).

### Agent 1 (opus) — validator / integration owner
Validates every return against its brief, owns integration commits and conflict serialization, runs the full gate set, remedies bounded defects itself (recording rounds under `instances/AGENT1-VALIDATOR/`), escalates consequential decisions to Agent 0.

## Gates (all green before PR)
`npm run typecheck`, `npm run test` (vitest), `npm run build`, `harness:validate:section9`, `validate:release-quality` (documented `--skip-premerge <reason>` only if evidence-skip needed), `desktop:pack` (CSC_IDENTITY_AUTO_DISCOVERY=false) + `desktop:verify-dependencies` + `instruction-root:integrity`, repo self-check (`tools/practitioner_harness/harness.py self-check`), corpus reconcile status if governed docs touched.

## Fences and cautions
- F-APP-1..5 hold: no provider/network expansion (icns generation strictly offline; never let electron-builder fetch its icons toolset), no signing/notarization claims, no `_DomainEngines`/piping writes, no issuance, single-surface rule.
- `runtime/packages/*` changes must stay generic and parameterized (D-GOV-20); project-specific values live in the frontend caller.
- Never commit incidental `package-lock.json` mutations from local `npm install` (`pi-lock-integrity` test will fail; `git checkout -- package-lock.json` if mutated).
- Owner's live machine state (real LaunchAgent, userData, registration, main-checkout dist app) is out of write scope for ALL stages incl. V (isolation mandatory). Deployment to the owner's machine happens post-merge under owner direction.
- Concurrent sibling writes disjoint per scopes above; overlaps resolve through Agent 1 as serialized integration owner.

## Decision gates returned to the owner
1. PR merge (owner-only, as before).
2. Any forced scope change: e.g. activation-policy approach fails AND self-healing envelope proves insufficient in drills; credential-port redesign; anything touching fences.
3. Post-merge deployment steps on the owner's machine (rebuild, LaunchAgent migration incl. removal/replacement of the existing agent).

## Explicitly out of scope (future tranches)
First-run registration/setup UI (D-GOV-20 opt-in flow); canonical daemon-side session mode metadata; replay-lens cosmetic residuals F-3/F-7; instruction-root divergence between packaged daemon (`process.resourcesPath`) and manifest-resolved roots — flagged 2026-07-24, assess separately.

## Corrections

Appended, not rewritten: the diagnosis text above is preserved as adopted. Each
entry records a factual error found during execution, the evidence, and what it
does (and does not) change.

### C-1 — 2026-07-25, Agent 1 validator (source: Stage A return §2, verified at integration)

**Corrects root cause #2 ("No self-healing"), which as written is factually wrong.**

Brief text: *"LaunchAgent plist (`runtime/packages/cli/src/launch-agent.ts:38-70,147-177`) has no `KeepAlive`/`RunAtLoad`; a dead daemon stays dead."*

Both halves of the premise are false, for the source and for the installed plist:

- `renderRuntimeLaunchAgent` at base `e9068c87d` emitted `RunAtLoad` → `<true/>`,
  `KeepAlive` → `{ SuccessfulExit: false }`, and `ThrottleInterval` → `10`.
  Confirmed against the pre-change source and against the installed
  `~/Library/LaunchAgents/com.chirality.runtime.plist` via `plutil -p`
  (read-only probe).
- The actual defect is **semantic, not missing**: `KeepAlive:{SuccessfulExit:false}`
  contractually forbids launchd from restarting a job that exited zero, and the
  observed termination *was* a clean `exit(0)`.
  `launchctl print gui/501/com.chirality.runtime` reported
  `state = not running`, `runs = 4`, `last exit code = 0`, and decisively
  `semaphores = { successful exit => 0 }` — launchd reporting that it was
  deliberately holding the job down. `daemon.stderr.log` was 0 bytes and
  `daemon.stdout.log` held exactly 4 startup banners with no shutdown trace,
  consistent with a silent clean-exit path.

**Restated root cause #2:** *the LaunchAgent's restart posture is blind to the
only failure mode actually observed — the plist carries
`KeepAlive:{SuccessfulExit:false}` and `RunAtLoad:true`, so a daemon that exits
cleanly (rather than crashing) is held down by launchd's successful-exit
semaphore and stays dead.*

**Impact on the tranche:** none on remediation or scope. A3's parameterized
`keepAlive` and the frontend caller's `keepAlive: 'always'` are the correct fix
for the corrected cause as well as the stated one; `runAtLoad` remains a
parameterized option whose default reproduces the historical plist byte-for-byte.
The correction matters for the *record*: it moves the defect from "an omission in
our plist renderer" to "a wrong restart contract", and it is the direct
justification for choosing `always` over `crash-only`, which the records stage
must carry rather than repeating the original wording.

**Consequence retained for owner decision gate 3:** because the corrected cause
lives in the *installed* plist, merging alone delivers no behaviour change. The
owner's existing agent keeps `SuccessfulExit:false` and carries no
`EnvironmentVariables` until `daemon install` is re-run from a rebuilt app.
