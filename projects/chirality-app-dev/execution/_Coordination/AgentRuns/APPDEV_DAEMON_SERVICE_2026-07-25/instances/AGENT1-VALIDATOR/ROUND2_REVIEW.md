# AGENT1-VALIDATOR — ROUND 2 REVIEW (Stage V remediation)

**Run:** TRB-APPDEV-DAEMON-SERVICE-2026-07-25 · **Agent 1 (opus)**, validator and serialized integration owner
**Branch:** `feat/daemon-service`, round-1 head `071bebf9e`
**Inputs:** `../V-PACKAGED-DRILLS/RETURN.md` + its `evidence/` · Agent 0 dispositions 1–6 (in-session 2026-07-25)
**Round-1 correction:** appended to `ROUND1_REVIEW.md` (not rewritten) — §3's quit-veto approval is retracted; paths 1 and 3 were factually wrong.
**Outcome:** all six findings remediated. Full gate set green. Re-drills PASS. **One escalation** (daemon bundle identity, §6).

---

## 1. Per-finding: fix, and the measurement that proves it

All timings are from the packaged app under the isolation contract in §4. "Before"
values are Stage V's measurements on round-1 code. Evidence paths are relative to
`ROUND2_DRILLS/evidence/`.

### V-D1 + V-D5 — quit veto dropped, real graceful shutdown · **FIXED**

Veto and `shutdownAuthorized` deleted, misleading hint text deleted. `shutdown()`
split into `teardown()` + exit so both exit routes share one teardown. `before-quit`
now tears down the runtime host (releasing `control.sock`) and exits 0.

| Stimulus | Before (Stage V) | After | Evidence |
|---|---|---|---|
| **single SIGTERM** | alive after **30.022 s**, vetoed | **0.028 s**, graceful | `d1/sigterm-timeline.txt` |
| `desktop.shutdown.started` / `.completed` | **never, on any path** | both, every graceful path | `d1/sigterm-log.txt` |
| stale `control.sock` | after **every** death | **none** on any graceful path | same |
| **`launchctl bootout`** | **5.083 s** (SIGKILL escalation) | **0.035 s**, graceful | `d2/bootout-timeline.txt` |
| bootout → stays stopped | yes | yes (`launchctl print` rc=113) | same |
| single SIGTERM, later run | — | **0.045 s**, graceful | `d1/sigterm-timeline-final.txt` |

`reason` logs as `"before-quit"`, independently confirming Stage V's diagnosis:
Chromium's native handler converts the signal into a quit request, and the fix is to
honour it rather than refuse it.

**The removal is safe because the restart contract covers the original bug.**
Measured: after the clean `exit(0)`, launchd revived the daemon **5 ms** later
(`runs` 1→2, `last exit code = 0`) — precisely the case the old
`KeepAlive {SuccessfulExit:false}` semaphore refused to act on
(`d2/keepalive-revive.txt`).

**SIGKILL restart, reported honestly:** first measurement **4.031 s**, second
**0.036 s** (Stage V baseline 0.098 s). Not a regression — the first kill fell ~4 s
into an unexpired 10 s `ThrottleInterval` window; the second was taken after the
window elapsed. Both readings kept (`d2/sigkill-timeline.txt`,
`d2/sigkill-timeline-unthrottled.txt`).

### V-D2 — CLI delivers the same posture and cannot escape its label · **FIXED**

`resolveRuntimeLaunchAgentOptions(environment, userDataDirectory)` added to the
generic package; `createDefaultCliDependencies()` uses it. The frontend's new
`desktop-daemon-posture.ts` is the single source of the desktop's values, read by
both `createDesktopDaemonLifecycle()` and the generated launcher. Env-driven, so
`runtime/packages/cli` still carries no project constant (D-GOV-20).

**Acceptance met** — fresh shell holding **only the launcher's own exports** +
`HOME`, then `chirality daemon install` (`d4/cli-rendered-plist-parsed.txt`):

```
KeepAlive => true                      (was {SuccessfulExit: false})
RunAtLoad => true
Label => com.chirality.runtime
EnvironmentVariables => {
  CHIRALITY_USER_DATA => …/userdata     (was: key absent entirely)
  CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL => com.chirality.runtime
  CHIRALITY_RUNTIME_KEEP_ALIVE => always
}
```

**Label scoping, proved two ways.** A recording `launchctl` shim captured every
service name across install/start/status/stop/uninstall — only the configured
label, and no `kickstart` after `bootstrap` (`d4/trace-default-label.txt`):

```
bootstrap gui/501 …/home/Library/LaunchAgents/com.chirality.runtime.plist
print    gui/501/com.chirality.runtime
bootout  gui/501/com.chirality.runtime
```

Then live against real launchd with an isolated label configured
(`d4/live-status.json`): `launchAgent {installed: true, loaded: true}` and the
service named in the detail is **`gui/501/com.chirality.runtime.tranchetest.a1r2`**
— where Stage V got the operator's `gui/501/com.chirality.runtime`. `daemon stop`
left the operator's job byte-identical (`d4/owner-job-before.txt` vs `-after.txt`).

**Beyond the disposition, one hole closed.** The resolver initially pinned only the
runtime directory, leaving a CLI-installed isolated daemon whose children would fall
back to the default label. It now pins the effective label and posture too, so an
installed job is self-describing. A test asserts the app-side and CLI-side job
environments are equal, so the two surfaces cannot drift again unnoticed.

### V-D4 — `activate` opens a window · **FIXED, with a cost and an escalation**

The daemon handles `activate` by spawning the GUI detached, **then retiring
itself**. The retirement is load-bearing and was not in the disposition — see §2,
where a three-arm measurement shows why omitting it would have silently regressed
V-D1.

| Check | Result | Evidence |
|---|---|---|
| `open <app>` (no `-n`) with daemon running | `activate_received` → `gui_spawned {pid}` | `d3/final-daemon-log.txt` |
| **window on screen** | `4679 6719 layer 0 Chirality "Chirality Workflow Shell" 1280x840` | `d3/final-windowlist.txt` |
| GUI survives the daemon's exit | yes | `d3/final-gui-pids.txt` |
| replacement daemon | up **2.2 s** later, `runs=2` | `d3/final-launchctl.txt` |
| GUI reconnects across the bounce | attempts 1–2 socket-absent → attempt 3 reached the daemon | `d3/final-gui-log.txt` |
| **replacement daemon stops gracefully** | `bootout` **0.029 s**, no stale socket | `d6/expF-post-spawn-replacement.txt` |

Cost: opening the app from Finder while the daemon runs bounces the runtime for
~2–10 s (bounded by `ThrottleInterval`). Self-healing, visible in the top-bar chip,
and strictly better than the alternative in §2.

`prohibited` still does not stop LaunchServices resolution — Stage V's finding
stands; this handles the resolution rather than preventing it. Prevention needs a
separate bundle identity: **escalated, §6.**

### V-D3 — launcher idempotent, with an opt-out · **FIXED**

Content-compared before writing; `CHIRALITY_SKIP_CLI_LAUNCHER=1` opts out; the
caller logs the outcome and continues on failure either way.

| Run | Result | Evidence |
|---|---|---|
| first packaged launch | `{"status":"written"}`, mode `-rwx------` | `d5/run1.txt` |
| second launch, same content | **`{"status":"unchanged"}`**, mtime and sha256 identical | `d5/run2.txt` |
| launch with opt-out, file absent | `{"status":"skipped","reason":"opted-out"}`, no file created | `d5/run3.txt` |
| changed content (different label) | `written` | unit test |

The opt-out replaced Stage V's `chmod 0500 ~/.local/bin` trick and became the
isolation mechanism for this round's drills — observed in the real packaged app at
`d3/final-gui-log.txt`.

### V-D6 — no redundant `kickstart` · **FIXED**

`kickstart -k` now runs only for an already-loaded job (the restart path) or when
`RunAtLoad` is off. Throttle interaction documented on `start()`.

| Measurement | Before | After |
|---|---|---|
| `LaunchAgentManager.start()` | **10.07 s** | **5 ms** (`d1/start.json`) |
| launch count per start | 2 | **1** (`d1/launchctl-after-start.txt`) |

New tests cover both cases that still need the kickstart, plus that a bootstrap
failure for any *other* reason still throws.

### Minor — credential status no longer throws to the renderer · **FIXED**

`chirality:api-key-status` and `chirality:provider-api-key-status` catch a
daemon-down failure and return
`{ unavailable: true, hasKey: false, source: 'none', error }` instead of rejecting.
An unsupported provider is still rejected before the daemon is consulted. Four
tests, including one asserting a real answer is *not* marked unavailable.

---

## 2. The defect I introduced, and how it was caught

The substantive event of this round. The first V-D4 implementation
(`child_process.spawn`, daemon keeps running) **worked** — window verified — and
**silently regressed V-D1**. I found it only by re-checking `bootout` on a daemon
that had served an `activate`, rather than trusting the drill (iii) pass.

Isolated with a three-arm measurement, using a `CHIRALITY_DAEMON_GUI_SPAWN=0`
control arm added for the purpose:

| Arm | `activate` | spawn | `bootout` latency | graceful | evidence |
|---|---|---|---|---|---|
| A | no | no | **0.034 s** | yes | `d6/expA-no-activate.txt` |
| E | **yes** | no | **0.034 s** | yes | `d6/expE-activate-nospawn.txt` |
| B | yes | **yes** | **5.056 s** | **no**, stale socket | `d6/expB-after-activate.txt` |

Conclusion: forking from Chromium's browser process breaks that process's signal
handling. The `activate` event is innocent; the fork is not.

Three candidates, measured in order:

1. **`spawn`, daemon persists** — window works, stop path broken (arm B).
   Rejected: silently reintroduces the HIGH finding.
2. **`app.relaunch()` + `app.quit()`** — no fork, shutdown stayed graceful, but
   **produced no GUI at all**, twice, including after restructuring so Electron's
   own quit path (not `app.exit()`) ran to completion
   (`d3/relaunch-daemon-log.txt`). Rejected: fails the disposition.
3. **Adopted — spawn, then retire.** The fork-damaged process exits within
   milliseconds through our *own* path, where no signal is involved and the damage
   cannot matter; `KeepAlive` supplies a fork-free replacement whose stop path is
   intact. Both dispositions hold simultaneously; verified in §1 (V-D4, last row).

The `teardown()`/`shutdown()` split exists to serve this: one teardown, two exit
routes. The dead `buildGuiLaunchEnvironment` deny-list from attempt 2 was removed
rather than left behind.

---

## 3. Gate outcomes (exact, all re-run against the final code)

| Gate | Result |
|---|---|
| `npm run typecheck` | **PASS**, zero diagnostics |
| `npx vitest run` | **PASS** — `136 passed \| 1 skipped (137 files)` · **`1060 passed \| 4 skipped (1064)`** |
| `npm run build` | **PASS** |
| `npm run harness:validate:section9` | **PASS** — `STATUS=pass`, `TEST_COUNT=16` |
| `npm run validate:release-quality -- --skip-premerge "<reason>"` | **`pass_with_skips`**, `PREMERGE_SKIPPED=true`, exit 0 |
| `npm run desktop:pack` | **PASS**, exit 0, signing skipped as designed |
| ↳ `desktop:verify-dependencies` | **PASS** |
| ↳ `instruction-root:integrity` | **pass**, 43 files (`sourceCompleteness: needs_remediation` — `KG-001-examples`, pre-existing, unrelated) |
| ↳ asar `^/public` count | **2** (≥1 required) |
| ↳ `CFBundleIconFile` | **`icon.icns`** |
| ↳ packaged icns == committed | sha256 `4b85b8f4…412ff058`, byte-identical |
| repo self-check | **exit 0** — `INFO=15, NOT_APPLICABLE=2, REVIEW=3, WARN=19`; **zero** findings in `chirality-app-dev/frontend` or `runtime/packages`; all pre-existing |
| `runtime/packages/cli` `npm test` | **PASS** — `24 passed (24)` (14 at round-1 close) |
| Lockfile discipline | **CLEAN** — no `package-lock.json` change, before or after five `desktop:pack` runs |

Test delta from round 1: **1038 → 1060** frontend (+22) and **14 → 24** runtime CLI
(+10). Premerge skip reason unchanged from round 1 and still a **residual, not a
satisfied gate** (`docs/RELEASE_QUALITY_RUNBOOK.md` §3).

---

## 4. Isolation contract and owner-state verification

Stage V's contract with a **distinct label** so the two runs could never collide:
`CHIRALITY_USER_DATA=$HOME/.chirality-tranchetest-a1r2/userdata`, `HOME=…/home`
(relocating the LaunchAgents dir, the CLI launcher and Chromium caches), label
`com.chirality.runtime.tranchetest.a1r2`.

Guards in `la-driver.mjs`: it refuses to run against the default label, and refuses
to write into the operator's `LaunchAgents` directory. Drills that could reach
`~/.local/bin` also ran under `chmod 0500` *plus* the new
`CHIRALITY_SKIP_CLI_LAUNCHER=1` pin, with the launcher's sha256 checked before and
after (`d3/owner-launcher-{before,after}.txt` — byte-identical). Windows were
evidenced with a scoped `CGWindowList` query; **no screenshots taken**.

**Cleanup verified.** Test label booted out (`launchctl print` → "Bad request."),
test plist removed, temp tree deleted, `~/.local/bin` restored to `0755`, no
Chirality processes left. `owner-state-before.txt` vs `owner-state-after.txt`
differs **only in the capture-timestamp line** (`cleanup/owner-state-diff.txt`):
owner plist sha `6446817153f0…` unchanged, owner launcher sha `2c012007983…`
unchanged, `gui/501/com.chirality.runtime` still `state = not running, runs = 4,
last exit code = 0`, owner userData mtime unchanged.

Fences: no network egress (`desktop:pack`'s electron fetch was a cache hit
throughout — `~/Library/Caches/electron` mtimes unchanged), no signing claim, no
`_DomainEngines`/piping writes, no issuance.

---

## 5. Commits

| # | SHA | Subject |
|---|---|---|
| 1 | `ee2154976624ae3bc3b791fd22a59c32202c3f27` | `fix(runtime): env-configurable job posture for the CLI, and stop double-launching on start` |
| 2 | `c3616aa695a6a60814ebce17bbfd47321870d2bd` | `fix(app-dev): drop the daemon quit veto for real graceful shutdown; open the GUI on activate` |
| 3 | `3e7e57e045d49e0227330aa7d2c15b14af8c2287` | `fix(app-dev): one daemon posture for both install surfaces; idempotent launcher; no throw on daemon-down status` |
| 4 | (this record) | `docs(app-dev): Stage V evidence, round-2 drills, and the ROUND1 §3 correction` |

Not pushed. No PR. Freshly packed app left at
`projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app`, built from
commit 3's tree — every drill above ran against those shipped bits.

---

## 6. ESCALATION — daemon bundle identity (owner decision gate 2)

**What.** `setActivationPolicy('prohibited')` cannot stop LaunchServices from
resolving a launch of `Chirality.app` against the running daemon: it stays
registered under `com.chirality.app`, reclassified `UIElement`, and Stage V
reproduced the resolution 3/3. Round 2 *handles* the resolution (open a window,
retire the daemon) but does not *prevent* it.

**Cost of the handling.** Opening the app from Finder/Dock while the daemon runs
bounces the runtime for ~2–10 s. Self-healing and visible, but real.

**The correct fix** is the first option Stage V itself listed: give the daemon its
own bundle identity — a helper `.app` with its own `CFBundleIdentifier` and
`LSUIElement`, with the LaunchAgent pointing at that binary. Finder would then never
resolve to the daemon, no `activate` would arrive, and no fork or bounce would be
needed. A2's original objective would be met at the cause.

**Why I did not do it.** It is a packaging change (new bundle in electron-builder,
daemon program path change, LaunchAgent migration) — scope expansion beyond a
remediation round, and it touches the packaging fence. Per my brief that is an
Agent 0 / owner decision.

**Recommendation.** Merge round 2 as-is; open the bundle-identity change as its own
tranche. Nothing in it invalidates this round's work — the `activate` handler becomes
dead code the day Finder stops resolving to the daemon, and can be deleted then.

---

## 7. Residuals and handoff

**For Agent 0 / owner**

1. **Premerge still not satisfied** — `pass_with_skips`; no provider-backed
   Section 8 run exists for this branch. Owner decision, unchanged from round 1.
2. **Deployment story (gate 3) is now better than Stage V reported.** Re-running
   `chirality daemon install` from a rebuilt app **does** now deliver
   `KeepAlive=true` and the pinned environment, so V-D2's warning that only the
   in-app install works no longer applies. Deployment still requires re-installing
   the LaunchAgent — the merge alone changes nothing on a machine whose plist was
   installed earlier.
3. **Operator-facing changes to document:** the daemon *is* now stoppable by
   Cmd-Q/Dock-Quit/AppleEvent/SIGTERM and launchd immediately restarts it
   (`KeepAlive=always`); `launchctl bootout` is the stop verb and is now fast
   (~35 ms) and clean; opening the app from Finder while the daemon runs bounces the
   runtime briefly; `~/.local/bin/chirality` is no longer rewritten on every launch.
   **Round-1 residual R-3 (daemon not quittable) is obsolete** — deleted by this
   round.
4. **`origin/main` divergence** (round-1 residual 10) still applies: `ahead 7,
   behind 14`, zero file-level overlap, and the repo self-check must be re-run after
   merging main because `9c2f330c6` touches `tools/practitioner_harness/`.
5. **Pre-existing, not introduced:** `sourceCompleteness: needs_remediation`
   (`KG-001-examples`) and the 3 REVIEW / 19 WARN self-check findings outside this
   tranche's paths.

**Environment / method notes**

6. `runtime/packages/cli/dist` must be rebuilt (`npx tsc -b`) after the runtime
   package changes for the frontend typecheck to resolve `@chirality/*`.
   Environment-only; `dist/` remains gitignored and uncommitted.
7. New env surface, all documented in code: `CHIRALITY_RUNTIME_KEEP_ALIVE`,
   `CHIRALITY_RUNTIME_RUN_AT_LOAD`, `CHIRALITY_RUNTIME_THROTTLE_INTERVAL_SECONDS`,
   `CHIRALITY_SKIP_CLI_LAUNCHER`, `CHIRALITY_DAEMON_GUI_SPAWN` (plus the existing
   `CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL`, `CHIRALITY_USER_DATA`,
   `CHIRALITY_DAEMON_ACTIVATION_POLICY`).
8. **Drill scripts are reusable** and kept as part of the method record:
   `ROUND2_DRILLS/env.sh`, `la-driver.mjs` (with label/path refusal guards),
   `winlist.swift`. The recording `launchctl` shim described in §1 (V-D2) proves
   label scoping with zero risk and is worth reusing.
9. **Not re-verified this round** (Stage V's results stand, code paths untouched):
   safeStorage round-trip under `prohibited`, the stub-adapter end-to-end turn, and
   the icon drills. Icon and asar checks were re-run as part of `desktop:pack`.
10. **Known and accepted:** SIGKILL still leaves a stale `control.sock` — uncatchable
    by construction, and the next daemon rebinds (observed). Only graceful paths
    clean up, which is now every path a user or launchd can invoke.
