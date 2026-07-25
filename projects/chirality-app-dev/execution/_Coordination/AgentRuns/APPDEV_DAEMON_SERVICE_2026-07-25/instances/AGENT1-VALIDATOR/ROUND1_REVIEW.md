# AGENT1-VALIDATOR — ROUND 1 REVIEW

**Run:** TRB-APPDEV-DAEMON-SERVICE-2026-07-25 · **Agent 1 (opus)**, validator and serialized integration owner
**Branch:** `feat/daemon-service` · base `main` @ `e9068c87d76c75b133f3686db8bf453565ce8fa2`
**Authority:** `../../ADOPTED_BRIEF.md` (incl. Correction C-1, appended this round)
**Inputs validated:** `../A-DAEMON-SERVICE/RETURN.md`, `../B-PACKAGING/RETURN.md`
**Round outcome:** both stages **ACCEPTED**. Full gate set green (one documented premerge skip). Integrated in 4 commits. No push, no PR — Agent 0 owns that after Stage V.

---

## 1. Per-stage verdicts

### Stage A — A-DAEMON-SERVICE: **ACCEPTED**

Scope conformance verified file-by-file against the declared write scope
(`frontend/electron/**`, `frontend/src/**` connectivity surface + tests,
`runtime/packages/cli/src/**` + tests):

| Declared boundary | Actual | Verdict |
|---|---|---|
| `runtime/packages/cli/src/**` + tests | `src/launch-agent.ts`, `test/cli.test.ts` | in scope |
| `frontend/electron/**` | `main.ts`, `preload.ts`, `runtime-control-ipc.ts` + 3 new (`runtime-connectivity.ts`, `desktop-log.ts`, `desktop-process-policy.ts`) | in scope |
| `frontend/src/**` connectivity surface | `components/shell/shell-frame.tsx`, `components/shell/use-runtime-connectivity.ts`, `lib/shell/runtime-connectivity.ts`, `types/chirality-window.d.ts`, `app/globals.css` | in scope |
| `frontend/src/__tests__/**` | 5 new files + `runtime-control-ipc.test.ts` | in scope |
| `frontend/package.json` (Stage B's) | untouched by A | respected |
| `frontend/electron/cli-launcher.ts` (Stage B's) | untouched by A | respected |

D-GOV-20 genericity **holds**. `runtime/packages/cli` gained only
caller-configurable options (`label`, `keepAlive`, `runAtLoad`,
`throttleIntervalSeconds`, `environmentVariables`) whose defaults reproduce the
historical plist byte-for-byte (`crash-only` → `{SuccessfulExit:false}`,
`runAtLoad:true`, `ThrottleInterval:10`). Every project-specific value —
`keepAlive:'always'`, the pinned `CHIRALITY_USER_DATA`, the isolation label — is
chosen in the frontend caller `createDesktopDaemonLifecycle()`. No frontend
constant leaked into the runtime package.

`globals.css` reviewed line-by-line: appended block only, exclusively new
`.shell-runtime-*` rules, **zero token definitions changed**. All 13 referenced
custom properties resolve; `var(--font-mono, ui-monospace, …)` matches the
existing idiom used at 11 other sites in the same file (`--font-mono` is supplied
by `next/font` on `<html>`, never declared in CSS — confirmed against
`globals.css:25`).

Quality notes worth carrying: the supervisor is deliberately `electron`-free and
fully injectable (timer queue, clock), which is why its 11 tests are
deterministic rather than sleep-based; the logger is `appendFileSync` for a
stated reason (ordering + survives `app.exit()`, which is exactly when the
load-bearing events are emitted); failure reasons are redacted through a
credential-shaped pattern before they can reach a renderer or the log.

**A1 note.** Live reproduction was deferred to Stage V, as the brief permits
("If not definitively pinned within the box, record best-supported hypothesis and
proceed"). The desk analysis is genuinely evidenced (the LaunchServices
launch-path asymmetry is the discriminating observation, and the
`semaphores = { successful exit => 0 }` reading is decisive for the restart
blindness), and the shipped instrumentation makes the hypothesis falsifiable in
drill 2. Accepted as scoped.

### Stage B — B-PACKAGING: **ACCEPTED** (one declared deviation, ratified below)

| Declared boundary | Actual | Verdict |
|---|---|---|
| `frontend/package.json` `build` block only | `build.files` += `public/**/*`; `build.mac.icon` = `build/icon.icns` | in scope; diff touches nothing outside `build` |
| `frontend/build/**` | `icon-macos.svg`, `icon.icns` | in scope |
| `frontend/scripts/**` | `generate-macos-icon.mjs` | in scope, and confirmed absent from the build graph |
| `frontend/electron/cli-launcher.ts` + tests | both | in scope |
| `frontend/public/**` (icns-variant artwork permitted) | **not written** | see credit below |
| `frontend/.gitignore` | modified | declared deviation → ratified, §2a |

**Credit — a latent defect avoided.** The brief permitted the icns-variant source
artwork under `frontend/public/**`. Stage B instead placed `icon-macos.svg` in
`frontend/build/`. Taking the permission literally would have been a real defect:
B1 adds `public/**/*` to `build.files`, so a 1024-canvas variant living in
`public/` would have shipped inside the asar as dead payload. The narrower
placement is correct and is confirmed clean — see the asar leak check in §5.

B2's geometry claims were re-derived independently and hold: every quincunx
element is the 32-unit source composition under one affine map (×`824/32 = 25.75`,
`+100`) — `4.6→218.45`, `12.3→416.73`, `20→615`, `7.4→190.55`, `1.5→38.63`,
pivots `8.3→313.73`, `16→512`, `23.7→710.28`, rotations and all six colours
unchanged. The tile alone is *not* a scale of the source (drawn at `104,816²`
with an 8px centred stroke so the outer silhouette lands on the 824 content box)
— a deliberate, documented departure implementing the macOS icon-grid inset, not
an arithmetic slip.

`sharp` reliance is regeneration-only and correctly kept out of
`dependencies`/`devDependencies`; the icns is a committed deterministic artifact,
so the build needs no rasteriser. electron-builder's SVG→icns path (which fetches
a toolset from GitHub) is bypassed entirely — fence F-APP-1 respected.

---

## 2. Integration decisions

### (a) `frontend/.gitignore` `!/build/` negation — **RATIFIED as placed**, plus one tightening

The mechanism is sound and was verified empirically, not assumed:

```
git check-ignore -v projects/.../frontend/build/icon.icns     -> exit 1 (not ignored)
git check-ignore -v projects/.../frontend/build/icon-macos.svg -> exit 1 (not ignored)
git check-ignore -v projects/.../frontend/build                -> frontend/.gitignore:13:!/build/  (winning rule)
git add --dry-run projects/.../frontend/build                  -> exactly 2 files, both intended
```

Git's documented limitation — "it is not possible to re-include a file if a
parent directory of that file is excluded" — does **not** bite here. The excluded
object is `build` *itself*, not a parent of it, and patterns in a deeper
`.gitignore` take precedence over a shallower one for the same path. Git
therefore un-excludes the directory and descends into it normally. Stage B's
reasoning that a nested `build/.gitignore` cannot work is also correct, for the
same rule read the other way.

Placement ratified in `frontend/.gitignore` rather than the repo root: the
exception is frontend-local, the root pattern remains a valid repo-wide
convention, and the leading `/` anchors the negation to `frontend/build` alone —
`**/build/` still ignores any deeper `build/` directory. `git add -f` was
rejected for the reason Stage B gave: it would leave a committed build resource
permanently invisible to `git status`, so later drift in `icon.icns` would go
unnoticed.

### (b) A6 `setPath('userData')` before `installBundledCliLauncher()` — **VERIFIED CORRECT, no fix required**

Stage B's ordering dependency holds in code:

- `applyUserDataOverride()` — `electron/main.ts:163`, **module scope**.
- `installBundledCliLauncher()` — `electron/main.ts:591`, inside `initializeGui()`,
  reachable only from the `app.whenReady().then(…)` callback at `main.ts:~712`.

Module-scope statements always execute before any `whenReady` callback, so the
launcher is rendered with the post-override path. Strengthened beyond the single
call site: every `app.getPath('userData')` read in `frontend/electron/*.ts` (8
sites across `main.ts`, `runtime-control-ipc.ts`, `runtime-host.ts`,
`api-key-storage.ts`, `cli-launcher.ts`) is inside a function body invoked after
line 163 — there is no module-scope userData read anywhere that could latch the
pre-override value.

### (c) `renderCliLauncher` breaking signature — **CONFIRMED, all callers updated**

Repo-wide grep (excluding `node_modules`/`dist`) finds exactly four call sites:
the single production caller `cli-launcher.ts:60` and three cases in
`src/__tests__/electron/cli-launcher.test.ts`. All four supply
`userDataDirectory`. Typecheck green. Stage B's intent — that a future second
caller fails loudly rather than silently emitting an unpinned launcher — is
preserved.

### (d) Runtime workspace `dist/` freshness — **CONFIRMED environment-only; standing note issued**

The frontend typecheck gate resolves `@chirality/*` through
`node_modules → dist/src/*.d.ts` (the root `tsconfig.json` carries no path
aliases), so a stale `runtime/packages/cli/dist/` surfaces as a spurious
`TS2554` on the new 4-argument `LaunchAgentManager` constructor. At my run the
dist was already current and typecheck passed with no manual step. `**/dist/` is
gitignored (root `.gitignore:42`); `git status` confirms no dist artifact is
staged or committed.

**Standing note for Stage V and any later round:** if `@chirality/*` type
resolution goes stale, run `npx tsc -b` in `runtime/packages/cli`. It is an
environment action. **Never commit `dist/`.**

---

## 3. Quit-veto behaviour review (brief-flagged, explicit verdict)

**Verdict: APPROVED. The veto cannot brick the daemon against launchd control, and GUI mode is untouched.**

The change: in `--runtime-daemon` mode, `before-quit` calls
`event.preventDefault()` and logs `runtime.daemon.quit_request_vetoed` unless
`shutdownAuthorized` is set (`main.ts:733-747`).

**launchd retains control on four independent paths:**

1. **`launchctl bootout` → SIGTERM.** `process.once('SIGTERM')` sets
   `shutdownAuthorized = true`, then `shutdown(0, 'signal:SIGTERM')` →
   `app.exit(0)`. `app.exit()` **does not emit `before-quit` at all**, so the veto
   is structurally unreachable on this path; the authorization flag is redundant
   belt-and-braces rather than the load-bearing mechanism. Two independent
   guarantees, not one.
2. **`launchctl kickstart -k` → SIGKILL.** Uncatchable by construction.
3. **A second SIGTERM.** `process.once` removes the listener after it fires, and
   Node restores the default signal disposition when the last listener for a
   signal is removed — so a second SIGTERM terminates the process even if
   `shutdown()` were to hang inside `runtimeHost.stop()`.
4. **`bootout`'s own escalation.** launchd follows SIGTERM with SIGKILL after its
   timeout regardless of what the process does.

**Failure-path exits remain possible.** The `whenReady().catch` sets
`shutdownAuthorized = true` before `shutdown(1, 'initialize-failed')`, so a daemon
that cannot start still exits non-zero rather than being trapped alive by its own
veto.

**GUI mode is untouched.** The veto branch is gated on `runtimeDaemonMode`; the
pre-existing GUI `before-quit` path is unchanged apart from the added `reason`
argument. Cmd-Q and Dock-Quit still quit the GUI. Confirmed at the packaging
level too: `dist/mac-arm64/Chirality.app/Contents/Info.plist` carries **no**
`LSUIElement` and **no** `LSBackgroundOnly` — the headless posture is applied at
runtime, in daemon mode only, so the GUI's Dock and menu-bar identity is
unaffected.

**Accepted residual risks (for Stage V observation, not blockers):**

- **R-1.** A permanently failing daemon startup is now a restart loop rather than
  a single dead job (`keepAlive:'always'` + `exit(1)`). Bounded by
  `ThrottleInterval` (≥10s) and fully evidenced in `desktop-daemon.log`. Stage V
  should report `launchctl print` `runs` counts alongside each drill.
- **R-2.** If `shutdown()` hangs before `app.exit()`, a *single* SIGTERM leaves
  the process alive until the second signal or launchd's SIGKILL escalation. Not
  brickable; Stage V should note `bootout` latency during cleanup.
- **R-3.** Operator-facing: the daemon can no longer be quit from the Dock or with
  Cmd-Q. The veto logs the correct hint. **Belongs in the owner deployment notes
  under decision gate 3.**

---

## 4. Defects found and remedies applied

| # | Defect | Severity | Remedy | Verification |
|---|---|---|---|---|
| D-1 | `!/build/` re-included the whole directory, so `generate-macos-icon.mjs --keep-iconset` (which materialises `frontend/build/icon.iconset/`, 10 intermediate PNGs) would surface regenerable rasteriser output as untracked-and-committable source. Stage B flagged the negation's breadth as a risk but left it open. | Low | Added `/build/icon.iconset/` immediately after the negation in `frontend/.gitignore`, with a comment stating why. | Materialised a scratch `build/icon.iconset/icon_16x16.png`: `git check-ignore -v` → `frontend/.gitignore:16:/build/icon.iconset/` (ignored); `git status` unchanged; scratch removed. |

**No other defects.** Every substantive claim in both returns that could be
re-derived was re-derived: the icon geometry mapping, the icns byte-identity, the
`.gitignore` mechanics, the A6 ordering, the caller inventory, the CSS token
inventory, and every gate count (§5).

**Test honesty — re-run, not trusted.** Full suite re-run from a clean
invocation: **1038 passed / 4 skipped (1042) across 135 passed / 1 skipped (136
files)** — matching Stage A's reported figures exactly. The `+50` delta from the
`988/992` baseline reconciles precisely: 45 in five new Stage A test files
(11 `runtime-connectivity` + 8 `desktop-log` + 9 `desktop-process-policy` +
9 `shell-runtime-connectivity` + 8 `shell-frame-runtime-connectivity`), +3 in
`runtime-control-ipc.test.ts` (Stage A), +2 in `cli-launcher.test.ts` (Stage B).
Cases were read, not counted: they assert behaviour (backoff ladder timing,
rebind after daemon loss, throwing-probe handling, credential redaction, log
rotation, `0600` mode, relative-path rejection) rather than restating the
implementation. The regression guard `leaves the working-root chip and its dot
untouched` is real and asserts exactly one `shell-root-dot*` node survives
alongside a runtime chip.

---

## 5. Gate outcomes (exact)

All from `projects/chirality-app-dev/frontend` unless noted.

| Gate | Result | Evidence |
|---|---|---|
| `npm run typecheck` | **PASS** | `tsc --noEmit` + `tsc -p tsconfig.electron.json --noEmit`, zero diagnostics. No manual `tsc -b` needed. |
| `npx vitest run` | **PASS** | `Test Files 135 passed \| 1 skipped (136)` · `Tests 1038 passed \| 4 skipped (1042)` · 10.75s |
| `npm run build` | **PASS** | `next build` OK; `build-electron.mjs` → `main.js` 1.3mb, `preload.js` 3.5kb, `chirality-cli.mjs` 70.0kb |
| `npm run harness:validate:section9` | **PASS** | `HARNESS_SECTION9_STATUS=pass`, `HARNESS_SECTION9_TEST_COUNT=16`, exit 0 |
| `npm run validate:release-quality` (1st, no skip) | **FAIL** | `HARNESS_PREMERGE_STATUS=fail`, `RELEASE_QUALITY_STATUS=fail`, exit 1. All 8 Section 8 rows `fetch failed` — no harness API on `http://127.0.0.1:3000`. |
| `npm run validate:release-quality -- --skip-premerge "<reason>"` | **PASS (pass_with_skips)** | `RELEASE_QUALITY_STATUS=pass_with_skips`, `RELEASE_QUALITY_PREMERGE_SKIPPED=true`, exit 0. Commands: `full_test` pass · `typecheck` pass · `section9` pass · `premerge` skipped. `summary.section9` pass, `summary.section8` skipped. |
| `npm run desktop:pack` | **PASS** | exit 0, `CSC_IDENTITY_AUTO_DISCOVERY=false`, code signing skipped as designed |
| ↳ `desktop:verify-dependencies` | **PASS** | `localPackageEntries: 0`, required present (`@anthropic-ai/claude-agent-sdk`, `@earendil-works/pi-coding-agent`, `next`), `forbiddenDevelopmentPackagesPresent: []`, `failures: []` |
| ↳ `instruction-root:integrity` | **PASS** | `status: pass`, 43 files checked, `missingInBundle: []`, `mismatchedFiles: []`. `sourceCompleteness: needs_remediation` — sole row is `KG-001-examples` (repo-root `examples/` absent). **Pre-existing, unrelated to this tranche.** |
| ↳ asar `public/` (extra check) | **PASS** | `asar list … \| grep -c "^/public"` → **2** (≥1 required): `/public`, `/public/chirality-app-icon.svg` |
| ↳ `Info.plist` icon (extra check) | **PASS** | `CFBundleIconFile => "icon.icns"` (was `electron.icns`). `CFBundleIdentifier => com.chirality.app` unchanged. |
| ↳ icns identity (extra check) | **PASS** | `Contents/Resources/icon.icns` sha256 `4b85b8f4…412ff058` == committed `build/icon.icns` — byte-identical, no re-conversion path ran |
| ↳ `build/` leak (extra check) | **PASS** | no `^/build` or `icon-macos` entry in the asar; `buildResources` stayed input-only |
| repo self-check (repo root) | **PASS** | `python3 tools/practitioner_harness/harness.py self-check` exit 0. `INFO=15, NOT_APPLICABLE=2, REVIEW=3, WARN=19` — every finding is under `_DomainEngines/`, `docs/governance_harness/`, or `projects/pec/`; **none touches a path changed by this tranche**; all pre-existing. |
| `runtime/packages/cli` `npm test` | **PASS** | `Test Files 1 passed (1)` · `Tests 14 passed (14)` |
| Lockfile discipline | **CLEAN** | `git status --porcelain -- '*package-lock.json'` empty **before and after** `desktop:pack` (which ran `@electron/rebuild` + native dependency install). No `git checkout --` needed. |

### Premerge skip — reason of record

```
No local harness API is reachable in this integration validation; fence F-APP-1
forbids provider/network expansion and the tranche's isolated packaged-app drills
(Stage V) use the stub adapter, so no provider-backed Section 8 run is producible
in this environment.
```

This is the documented path (`docs/RELEASE_QUALITY_RUNBOOK.md` §3) with in-repo
precedent (`plans/PLAN_COMPLETION_LOG.md:907`). Premerge requires a live Next
server on `HARNESS_BASE_URL` **plus** provider/key prerequisites; standing up
either would breach F-APP-1 and the no-network fence, and Stage V cannot produce
it either (its drills are stub-adapter and isolated). Recorded as a **residual,
not a satisfied gate** — see §7. Wrapper status is `pass_with_skips`, never
`pass`.

### Fence compliance evidence

- **F-APP-1 (no network/provider expansion).** No provider call, no network
  egress initiated. `desktop:pack`'s `• downloaded label=electron progress=100%`
  line was a **cache hit**, not a fetch: `~/Library/Caches/electron/` and every
  entry in it carry mtimes of `Jul 24 14:43` or earlier, unchanged across the
  19:55 pack. electron-builder's icon-converter toolset download never ran (a
  committed `.icns` bypasses that code path).
- **Owner live machine state untouched** (read-only `stat`, no writes, no reads of
  contents):

  | Artifact | mtime | Interpretation |
  |---|---|---|
  | `~/Library/LaunchAgents/com.chirality.runtime.plist` | 2026-07-24 18:30:40, 924 B | unchanged; still `SuccessfulExit:false`, no `EnvironmentVariables` |
  | `~/Library/Application Support/chirality-frontend` | 2026-07-24 19:15:07 | unchanged; predates all stage execution |
  | `~/.local/bin/chirality` | 2026-07-24 19:05:28, 703 B | unchanged; still the unpinned launcher |

  Every mtime predates the 19:2x–19:5x stage/validator execution window. The GUI
  was never launched; no LaunchAgent was installed, started, or booted out.
- **F-APP-3/4/5.** No `_DomainEngines`/piping writes, no lifecycle issuance, no
  signing/notarization claim. `desktop:pack` explicitly logs signing as skipped.

---

## 6. Commits

Four logically grouped commits on `feat/daemon-service`, generic-runtime change
separated from its project caller per D-GOV-20. Not pushed; no PR.

| # | SHA | Subject |
|---|---|---|
| 1 | `8c20f214dae63ee80211747f4765b870fffa7466` | `feat(runtime): parameterize LaunchAgent restart posture, label, and pinned environment` |
| 2 | `22752cf678e27fd8bdbcda793374d83312610b16` | `feat(app-dev): daemon as a real service — headless posture, supervised binding, durable diagnostics` |
| 3 | `987541feddc247dcc7a43012bfaa345cf40c9676` | `feat(app-dev): package public/, ship a committed macOS icns, pin CLI userData` |
| 4 | (this record) | `docs(app-dev): daemon-service tranche control-plane records + brief correction C-1` |

Commit 4's own SHA is recorded in `../RECORDS/` at closeout rather than here — a
record cannot contain its own hash. Examined-through for the code tranche is
commit 3: `987541feddc247dcc7a43012bfaa345cf40c9676`. All gate results in §5 were
produced against exactly this tree (the only later change is this record plus the
`ADOPTED_BRIEF.md` C-1 append — documentation only, no code).

`dist/mac-arm64/Chirality.app` is **left in place, unignored-by-git and
uncommitted**, for Stage V.

---

## 7. Residuals and handoff

### For Agent 0 (decisions / records)

1. **Premerge gate is NOT satisfied.** `validate:release-quality` is
   `pass_with_skips`. No claim of a current provider-backed Section 8 harness run
   exists for this branch. If the owner wants premerge satisfied before merge, it
   needs a live harness API + provider prerequisites — outside this tranche's
   fences, and an owner decision, not an Agent 1 one.
2. **Brief Correction C-1 is appended**, not rewritten — root cause #2 restated
   from "no `KeepAlive`/`RunAtLoad`" to "restart posture blind to a clean
   `exit(0)`". The records stage must carry the corrected wording, not the
   original.
3. **Deployment does not follow from the merge** (owner decision gate 3). The
   owner's installed plist keeps `SuccessfulExit:false` and no
   `EnvironmentVariables`, and `~/.local/bin/chirality` keeps no userData pin,
   until `daemon install` is re-run from a rebuilt app. Add R-3 (daemon no longer
   Dock/Cmd-Q quittable) to the deployment notes.
4. **Pre-existing, not introduced here:** `instruction-root:integrity`
   `sourceCompleteness = needs_remediation` for `KG-001-examples` (repo-root
   `examples/` absent), and the 3 REVIEW / 19 WARN self-check findings in
   `_DomainEngines`/`docs/governance_harness`/`projects/pec`. None are in this
   tranche's changed paths; none block.

### For Stage V (in addition to the returns' own lists)

5. **Highest-priority unknown stands:** safeStorage `isEncryptionAvailable()` +
   full `encryptString`/`decryptString` round-trip under
   `setActivationPolicy('prohibited')` (drill 6). Designed fallback on failure is
   `CHIRALITY_DAEMON_ACTIVATION_POLICY=accessory` — no code change. Failure of
   *both* is the escalation trigger under owner decision gate 2.
6. **Report which of the three A1 outcomes occurred** in drill 1 (daemon
   untouched / `activate_received` but survived / exited and was restarted ≤10s).
   All three satisfy the owner requirement; only the first confirms the hypothesis
   was neutralized at the cause.
7. **Add to the drill reporting:** `launchctl print` `runs` and `last exit code`
   for the isolated label at every drill boundary (covers R-1), and observed
   `bootout` latency during cleanup (covers R-2).
8. **Isolation is load-bearing and now verifiable first:** confirm A6 honours an
   **absolute** `CHIRALITY_USER_DATA` (relative values are ignored-and-logged by
   design) before relying on it, and pair it with
   `CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL`. Assert afterwards that the three owner
   artifacts in §5 are byte-unchanged.
9. **Do not run `npm install`** in the worktree; if a lockfile mutates,
   `git checkout --` it. `runtime/packages/cli/dist/` may need `npx tsc -b`
   (environment only, never commit).

### Branch divergence (found at integration close — for Agent 0's PR)

10. **`origin/main` advanced 14 commits while this tranche was in flight** (PRs
    #331, #332 — the PEC v2 decomposition through Gate 7, plus
    `9c2f330c6 test(harness): conscious pin update — projects/pec enters GEN-7
    pointer scope`). `feat/daemon-service` is `ahead 4, behind 14` of
    `origin/main`; merge-base is still `e9068c87d`.

    **File-level overlap with this tranche: zero.** `git diff --name-only`
    intersected across both ranges is empty; their changed paths are confined to
    `projects/pec/`, `_DomainEngines/pec/`, and `tools/practitioner_harness/`. A
    merge should be clean.

    I deliberately did **not** rebase or merge: branch operations are Agent 0 /
    CHANGE territory, and rewriting or re-parenting this tranche would detach the
    §5 gate evidence from the tree it was produced against.

    **One consequence for whoever integrates with main:** `9c2f330c6` changes
    `tools/practitioner_harness/`, so the **repo self-check must be re-run after
    the merge**. My run (§5, exit 0) is valid only for the pre-merge tree. The
    frontend gates are unaffected — no changed path of theirs is reachable from
    the frontend or runtime build.

### Escalations

**None.** No consequential decision (scope expansion, fence risk, unresolvable
gate failure) was encountered. The premerge skip is a documented,
precedented, in-latitude action recorded as a residual rather than a satisfied
gate; the single defect found (D-1) was a bounded one-line remedy.

---

## APPENDED CORRECTION — 2026-07-25, after Stage V

**Round 1 is not rewritten. This note corrects it.**

**§3 "Quit-veto behaviour review — APPROVED" was wrong, and its reasoning was
wrong in a way that mattered.** Stage V falsified it empirically
(`../V-PACKAGED-DRILLS/RETURN.md` V-D1, `evidence/v6/`). The verdict rested on
four "independent launchd control paths"; paths 1 and 3 do not exist:

- **Path 1 was wrong.** I wrote that `bootout` delivers SIGTERM, that
  `process.once('SIGTERM')` sets `shutdownAuthorized` and calls `shutdown()`, and
  that `app.exit()` makes the veto structurally unreachable. **The JS SIGTERM
  handler never runs in the packaged Electron main process.** Chromium's own
  native handler intercepts the signal first and calls `app.quit()`, which reaches
  `before-quit` — the veto — and was refused. `shutdownAuthorized` was never set
  and `shutdown()` was never called. Measured: a single SIGTERM left the daemon
  alive after 30.022 s.
- **Path 3 was wrong.** "A second SIGTERM restores Node's default disposition" was
  reasoning about a Node listener that was never installed in the first place. The
  second SIGTERM did kill the process, but by the native handler's one-shot
  behaviour and *without* any graceful shutdown.
- **Paths 2 and 4 held** (SIGKILL, and `bootout`'s SIGKILL escalation), which is
  why the conclusion "nothing is brickable" survived. That conclusion was right
  for the wrong reasons, and it was the wrong question.
- **What I missed by asking only "can it be bricked?":** `runtimeHost.stop()` ran
  on **no exit path in the entire drill set**. Every stop was a forced kill,
  `control.sock` was left stale after every death, and `bootout` took 5.083 s. My
  R-2 residual anticipated the 5 s case as a curiosity ("worth Stage V observing")
  rather than recognising it as the normal stop path. The veto's own hint text —
  which I read and did not question — told operators to use SIGTERM, which did
  not work.

**Method lesson, recorded deliberately.** The §3 verdict was reasoned from source
plus Electron documentation and presented with more confidence than desk analysis
can carry for signal delivery inside a packaged Chromium process. Round 2 replaced
that with measurement: every claim below is a timing or a log line from the
packaged app.

**Disposition.** Agent 0 directed the veto dropped entirely (not narrowed). Done,
with real graceful shutdown in its place. See `ROUND2_REVIEW.md`.

Two round-1 statements that **stand** as written: the `!/build/` ratification
(§2a), and the A6 ordering verification (§2b) — Stage V's V0 drill confirmed the
packaged app honours an absolute `CHIRALITY_USER_DATA` and that the launcher bakes
the post-override path.
