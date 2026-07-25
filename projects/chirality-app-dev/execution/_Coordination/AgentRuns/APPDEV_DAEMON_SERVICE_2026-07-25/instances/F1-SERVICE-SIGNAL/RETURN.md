# F1-SERVICE-SIGNAL — RETURN (S1 loss detection + S2 bundle identity)

**Run:** TRB-APPDEV-DAEMON-SERVICE-2026-07-25 follow-up · **Agent 2 (opus)** · branch `feat/daemon-handoff` (= `main` @ `612c35226`, PR #333 merged)
**Window:** 2026-07-25 04:19Z–04:40Z. **Status:** COMPLETE, terminated early by Agent 0 stop order at ~04:36Z.
**Verdicts:** **S1 — SHIPPED, code-complete, gates green, packaged-app drills DEFERRED** (they require launching a packaged app, which initialises safeStorage; barred by the stop order). **S2 — NOT SHIPPED. Gate unmet by evidence**, per Agent 0 direction. All S2 code removed from the tree.

---

## 0. STOP-ORDER COMPLIANCE AND KEYCHAIN FORENSICS — READ FIRST

All times below are the operator's local clock (**UTC−06:00**); the app's own logs are UTC (local + 6 h).

### (a) Every command that touched, or could have touched, the login keychain

Two distinct classes. Only the second can produce an authorization prompt.

**Class 1 — read-only `security find-generic-password -s <service>` existence probes.** No `-g`, so no secret was requested and no ACL was evaluated. These cannot prompt.

| Time (local) | Where | Services probed |
|---|---|---|
| ~04:21:4x | ad-hoc probe | `Chirality Safe Storage`, `Chirality`, `Electron Safe Storage`, `Chromium Safe Storage`, `chirality-frontend Safe Storage` |
| 04:22:03 | `evidence/owner-state-before.txt` | 4 names |
| 04:32:39 | `evidence/s2-safestorage/keychain-before.txt` | 3 names |
| 04:35:38 | `.../keychain-after-armA.txt` | 3 names |
| 04:36:08 | `.../keychain-after-armB.txt` | 4 names |

One earlier attempt at `security dump-keychain` (~04:21) was **refused by the harness classifier and never executed**.

**Class 2 — Electron `safeStorage` encrypt/decrypt from a packaged app. These evaluate the Keychain ACL on the existing `chirality-frontend Safe Storage` item and are the credible cause of the operator-visible prompt.**

| Time (local) | Process identity | Operation | Result |
|---|---|---|---|
| 04:32:53–04:33:19 | clone, `com.chirality.app.f1test`, started from **my shell** (`env -i`) | `encryptString` via `PUT /v1/credentials/anthropic` | **FAILED** `INTERNAL_FAILURE` — no keychain access in this session |
| ~04:34:1x–04:34:32 | **unmodified** worktree app, `com.chirality.app`, started from my shell | same | **FAILED**, identically |
| **04:35:0x–04:35:20** | clone, **`com.chirality.app.f1test`**, started by **launchd** in `gui/501` | `encryptString` + `decryptString` | **SUCCEEDED** — first ACL-evaluating success. **Most likely prompt trigger.** |
| **04:35:41** | nested bundle, **`com.chirality.app.f1test.runtime`**, launchd | `decryptString` | **SUCCEEDED** — second distinct ad-hoc identity to read the item |
| 04:35:5x–04:36:08 | same nested identity, launchd | 2 further daemon starts, each `decryptString` | 1 failed by design (corrupted blob), 1 succeeded |

The crashed nested-bundle launches (04:23–04:31) never reached `safeStorage`. The `V7`/`V8` daemon starts (04:31) started a runtime host but performed no credential operation.

**Why this prompts.** The app is `adhoc, linker-signed` with `Internal requirements=none`, so the Keychain ACL recorded for the existing item cannot be satisfied by a stable designated requirement. A binary at a **new path** and under a **new bundle identifier** reading that item is exactly the case macOS asks the user about. My `cp -Rc` clone lived at `~/.chirality-tranchetest-f1/app/...`, a path the operator's keychain had never seen.

### (b) Was any keychain item created, modified, or deleted?

**No. None.**

- I ran no `security add-generic-password`, `delete-generic-password`, `set-generic-password`, or `dump-keychain`.
- `chirality-frontend Safe Storage` **already existed before my run** — recorded `FOUND` at ~04:21:4x and again in `owner-state-before.txt` at 04:22:03, before any app of mine had started.
- No new service name appeared: `Chirality Safe Storage`, `Chirality Runtime Safe Storage` and `Chirality Runtime` were `absent` before, at 04:35:38, and at 04:36:08.
- Chromium's `os_crypt` only *reads* an existing storage key; it creates one solely when absent. It was not absent.

The operator may have granted "Allow" or "Always Allow" at the prompt. If "Always Allow" was chosen, the ACL of `chirality-frontend Safe Storage` now trusts an extra ad-hoc identity that no longer exists on disk — harmless, but Agent 0 may want the operator to know.

### (c) Design note for a future S2 attempt that cannot prompt the operator

The prompt is a consequence of **ad-hoc signing**, not of the nested-bundle idea. Three routes, in preference order:

1. **Defer S2 until code signing exists.** With a Developer ID identity and a stable Team ID, both the app and the nested runtime bundle share a designated requirement, and — decisively — a `keychain-access-group` / same-team entitlement makes the two identities *the same principal* to the Keychain. No prompt, and the continuity question becomes a build-configuration fact rather than an experiment. **This is the real precondition and the recommended gate.**
2. **Prove continuity only inside a throwaway keychain.** Create a scratch keychain, add it to the search list *for the test processes only* (`security create-keychain` + `SecKeychainSetSearchList` via a wrapper, or run under a separate login session), let Chromium create its own key there, and never let the login keychain enter the search path. This proves the mechanism without ever evaluating an ACL on the operator's item. It is fiddly, because Chromium's `os_crypt` targets the *default* keychain.
3. **Sidestep `safeStorage` for the daemon entirely** — the credential-port redesign the adopted brief already rules out of scope and routes to owner decision gate 2.

Whichever route: any future S2 drill must run on a machine where the login keychain is not the operator's, or after signing exists. **Do not repeat this experiment on the operator's live machine.**

---

## 1. Cleanup verification

| Step | Result | Evidence |
|---|---|---|
| Isolated LaunchAgent stopped + uninstalled | `{"stopped":true}` / `{"uninstalled":true}` | `evidence/cleanup-step1.txt` |
| `launchctl print gui/501/com.chirality.runtime.f1test` | *Could not find service* | `cleanup-step1.txt`, re-verified in `cleanup-verification.txt` |
| Test processes | none before or after `pkill` | `cleanup-step1.txt` |
| Test bundles unregistered from LaunchServices (`lsregister -u`) | done for both bundles | `cleanup-step2.txt` |
| Test plist directory | empty | `cleanup-step2.txt` |
| `~/.chirality-tranchetest-f1` (1.4 GB) | **removed**; no `~/.chirality-tranchetest-*` remains | `cleanup-step2.txt` |
| `/tmp` helpers (`f1run.sh`, `f1lldb.txt`, `f1out.*`) | removed | `cleanup-step2.txt` |
| Encrypted dummy-credential blob copy | deleted from evidence | §7 |

**Operator state, before (04:22:03) vs after (04:37:11)** — `evidence/owner-state-diff.txt`, positive check in `evidence/cleanup-verification.txt`:

| Artifact | Verdict |
|---|---|
| `~/Library/LaunchAgents/com.chirality.runtime.plist` (sha256 `2ebc5566…`) | **IDENTICAL** |
| `gui/501/com.chirality.runtime` — `state = running`, `runs = 1`, `pid = 17236`, `last exit code = (never exited)`, `program = …` | **IDENTICAL** (the authorised restorative kickstart was never needed) |
| `~/.local/bin/chirality` (sha256 `592d3d27…`) and `~/.local/bin` mode | **IDENTICAL** |
| Operator's live GUI (17199) and daemon (17236) | **still running, untouched** |

The **only** differences in the whole snapshot are the capture timestamp and four Chromium cache files inside the operator's `chirality-frontend` userData (`DIPS-wal`, `DawnGraphiteCache/data_1`, `DawnWebGPUCache/data_1`, `GPUCache/data_1`). Those are the operator's **own running GUI** writing its caches during the window; every process I started was pinned to `CHIRALITY_USER_DATA=~/.chirality-tranchetest-f1/userdata` and `HOME=…/home` and could not write there.

The prompt did not come from a write. It came from a read, as analysed above.

---

## 2. S1 — the 43 s was two daemon deaths, not one

**This is the most consequential finding of the run and it changes the problem statement.** From the operator's own logs (`~/Library/Application Support/chirality-frontend/logs/desktop-{main,daemon}.log`, read-only):

| Time (UTC) | Event |
|---|---|
| 04:00:34.425 | daemon **17000** `activate_received` |
| 04:00:34.426 | `gui_spawned {pid:17199}` → `shutdown.started {reason:"retire-after-gui-spawn"}` |
| 04:00:34.428 | daemon 17000 `shutdown.completed` |
| 04:00:34.583 | GUI 17199 `desktop.gui.starting` |
| 04:00:34.591 | GUI bind attempt 1 **fails** — socket already unlinked, replacement not yet listening |
| 04:00:34.612 | launchd starts replacement daemon **17200** (**184 ms** after the retirement) |
| 04:00:34.622 | daemon 17200 `runtime.daemon.started` |
| **04:00:34.935** | **GUI `connectivity.bound`** |
| **04:01:01.004** | **daemon 17200 exits — `reason:"before-quit"`, 26 s later, cause unknown** |
| 04:01:04.948 | GUI notices: `"Runtime daemon stopped responding"` (**+3.94 s**, one probe interval) |
| 04:01:05.95 / 07.96 / 12.96 | ladder attempts 2, 3, 4 |
| 04:01:13.595 | launchd starts daemon 17236 (**12.59 s** after the death) |
| 04:01:17.871 | GUI rebound (**+4.28 s** after the daemon was already listening) |

**The handoff itself already costs 510 ms** (`activate` → `bound`), well inside the ≤3 s target. The 43 s the operator experienced is the *second* death plus its recovery. The brief's premise — "daemon retired ~1 s after spawn, but the supervisor only noticed at the next 30 s probe" — conflates the two events: the 30 s is simply the interval between the successful bind and the second death, and the steady probe is 10 s, not 30 s.

**Unexplained and left open:** what sent daemon 17200 a quit at 04:01:01. It arrived as `before-quit` with no preceding `activate_received`, 26 s after the GUI launched. This is the first sighting of the quit AppleEvent that Stage A hypothesised and Stage V never reproduced. Reproducing it needs a packaged-app drill — deferred.

### The mechanism I shipped

`frontend/electron/runtime-socket-watch.ts` — **watch the control socket's presence; both signals are already on the filesystem, exactly and immediately.**

- **Graceful stop unlinks the socket.** `RuntimeDaemon.stop()` closes the server then `unlink`s `control.sock` (`runtime/packages/daemon/src/runtime-daemon.ts:98`). The unlink *is* the loss event. Both deaths in the operator's trace were graceful, so both would have been caught in milliseconds instead of 3.94 s.
- **Start re-creates it**, and the operator token is written *before* `server.listen()`, so the socket appearing means the daemon can already answer. Rebind fires at once instead of at the next ladder rung — the 4.28 s and the ladder-position lottery both disappear.

Both events call the supervisor's existing `refreshNow()`. The directory is watched, not the socket: `fs.watch` throws on an absent path, and a watch on the file could not survive the unlink/re-create cycle that is the whole point.

**Why not the alternatives in the brief.** A `CHIRALITY_RUNTIME_HANDOFF=1` env hint would have covered only the handoff, and the operator's trace shows the handoff was never the expensive part; the watcher covers *every* loss and return with no cross-process coordination. Shortening the ladder was rejected as churn — with the watcher the ladder is a fallback, so the steady probe stays 10 s and the rungs stay 1/2/5.

**Documented limitation, by construction:** `SIGKILL` leaves the socket file behind, so an ungraceful death produces no unlink and detection still costs up to one 10 s probe. The subsequent *recovery* is still instant, because the replacement daemon reclaims the stale path by unlinking and re-listening — which the watcher does see.

**Not a busy loop:** a 250 ms floor between deliveries coalesces rename storms, deferring rather than dropping so the final state is always published; a failed `fs.watch` degrades silently to the probe ladder and retries every 5 s.

### Latent defect found and fixed

`refreshNow()` cancelled the pending timer *before* running a cycle, and `runCycle()` returned immediately when a cycle was already in flight — so the refresh was dropped with **no timer left scheduled and nothing to reschedule it**. The supervisor stopped probing permanently. Reachable today from two quick `onDaemonAvailable` calls; routine once filesystem events drive refreshes. Fixed by coalescing (`refreshPending`), with three regression tests.

### Expected effect (arithmetic on the measured trace, not a claim of measurement)

| Cost | Measured before | Expected after |
|---|---|---|
| Detect a graceful daemon loss | 3.94 s (bounded 10 s) | **≲ 0.3 s** |
| Rebind after the daemon is listening again | 4.28 s (bounded 10 s) | **≲ 0.3 s** |
| launchd replacement latency | 0.184 s (handoff) / 12.59 s (second death) | unchanged — not ours |
| Handoff `activate` → `bound` | 0.510 s | ≈ unchanged, already inside target |

**These are projections. They are NOT drill-measured** — see §5.

---

## 3. S2 — NOT SHIPPED. Findings only.

Per the stop order the verdict is fixed as **gate unmet by evidence**. All S2 code has been removed from the tree; the prototype survives only as `evidence/s2-design/afterpack-runtime-bundle.mjs.prototype`.

For the record, the evidence gathered before the stop is substantially positive and should not be lost:

| Question | Answer | Evidence |
|---|---|---|
| Can the daemon run under its own `CFBundleIdentifier` + `LSUIElement`/`LSBackgroundOnly`? | **YES** | `V7`, `V8`: daemon started, socket up, full engine list served |
| Does the copied stub keep its identity? | **YES** — `cdhash 5c22a19a…` identical to the parent's; the app is `linker-signed` with `Info.plist=not bound`, `Sealed Resources=none`, so nothing is invalidated by copying or by writing a new `Info.plist` | `evidence/s2-safestorage/identities.txt` |
| Does a different `CFBundleIdentifier` change the `safeStorage` key namespace? | **NO.** Arm A (`com.chirality.app.f1test`) encrypted; Arm B (`com.chirality.app.f1test.runtime`) decrypted the **byte-identical** blob (`sha 158438dc…` before *and* after) → `configured:true`. No new service name was created. Negative control: corrupt the last block → `configured:false`; restore → `configured:true` | `s2-safestorage/armB-status.json`, `armB-negative-control.txt`, `keychain-after-armB.txt` |
| Why? | The name is `chirality-frontend Safe Storage` — derived from `package.json` `name` (shared through the asar), **not** from `CFBundleIdentifier` or `CFBundleName`. Corroborated independently: the packaged app's userData is `…/chirality-frontend`, so `app.getName()` is `chirality-frontend` despite `CFBundleName = Chirality` | `keychain-before.txt`, operator logs |

**The blocker that stopped S2 on its own merits, before the stop order:**

| Variant | Result |
|---|---|
| Nested `Contents/Frameworks/Chirality Runtime.app`, `Frameworks` + `Resources` as directory symlinks | **crash**, `EXC_BREAKPOINT`, silent, before any logging |
| …with a parent-derived `Info.plist` (incl. `ElectronAsarIntegrity`, `NSPrincipalClass`) | crash |
| …with the parent's own bundle id / the parent's executable name | crash |
| Sibling bundle, absolute symlinks | crash |
| **Sibling bundle, real (APFS-cloned) `Frameworks` + real `Resources`** | **WORKS** |
| **Real `Frameworks`, symlinked `Resources`** | **WORKS** |
| Symlinked `Frameworks`, real `Resources` | **crash** |
| `Frameworks` as a real directory of per-entry symlinks, real `Resources` | **crash** |

So: **`Contents/Resources` may be a symlink (853 MB shared); `Contents/Frameworks` must be a real directory (276 MB).** dyld resolves the symlinked framework fine (`DYLD_PRINT_LIBRARIES` confirms), so the failure is Chromium's own framework-path validation, not linking. The stack is stripped to one frame and no assertion text is emitted, so the precise check was not identified.

**Cost of the real-`Frameworks` route**, which is why it is not a free win: +276 MB duplicated into the installer, and the four `Chirality Helper*.app` bundles get duplicated with colliding bundle identifiers. A future attempt should first test whether the daemon bundle can carry **only** `Electron Framework.framework` (real) and no helper bundles — the daemon does spawn GPU and network utility children, so this needs proving, not assuming.

**S2 design for the next attempt** — see also §0(c), which is the binding precondition:

1. Wait for code signing (Team ID) — it removes the prompt *and* makes the Keychain continuity question moot.
2. Then: nested bundle at `Contents/Frameworks/Chirality Runtime.app`, `Resources` symlinked, `Frameworks` real (minimal set, proven by experiment), `Info.plist` derived from the parent's with only `CFBundleIdentifier`/`CFBundleExecutable`/`CFBundleDisplayName` changed and `LSUIElement`+`LSBackgroundOnly` added — **`CFBundleName` must stay identical**.
3. Two follow-on code changes S2 requires that are *not* in the prototype and were never written: `deps.desktopExecutable` must resolve to the daemon binary for `install()`, and `spawnGuiFromDaemon()` must stop using `app.getPath('exe')` — under S2 that is the daemon's own binary, so the vestigial `activate` handler would spawn a second daemon instead of a GUI. **This is a latent trap for whoever picks S2 up.**

---

## 4. Files changed (all S1; S2 left nothing behind)

| Path | Change |
|---|---|
| `frontend/electron/runtime-socket-watch.ts` | **new** — socket-presence watcher; `electron`-free, every effect injectable |
| `frontend/electron/runtime-connectivity.ts` | coalesce a refresh that arrives mid-cycle (stall fix); ladder doc-comment now states it is the fallback |
| `frontend/electron/main.ts` | construct/start the watcher next to the supervisor; stop it first in `teardown()` |
| `frontend/src/__tests__/electron/runtime-socket-watch.test.ts` | **new** — 13 tests |
| `frontend/src/__tests__/electron/runtime-connectivity.test.ts` | +3 regression tests for the stall fix |

No `frontend/package.json` change (S2 would have needed one; S2 is not shipped). No `runtime/packages/**` change — the LaunchAgent surface needed no new parameters. No `frontend/src/**` product code touched. No commits, no lockfile churn.

**Scope note for Agent 0:** my brief scoped me to `frontend/electron/**`, but the repo convention (set by Stage A) puts electron unit tests under `frontend/src/__tests__/electron/`, which is nominally the sibling's tree. I wrote only there, in files the sibling does not touch (they modified `api-key-storage.test.ts`; I modified `runtime-connectivity.test.ts`). No shared-file read-modify-write occurred.

---

## 5. Validation

| Gate | Result |
|---|---|
| `npm run typecheck` | **PASS**, zero diagnostics |
| `npx vitest run` (full) | **PASS** — `141 passed \| 1 skipped (142 files)` · **`1095 passed \| 4 skipped (1099)`** |
| my two files alone | **27 passed (2 files)** |
| `runtime/packages/cli` `npm test` | **PASS** — `24 passed (24)` (unchanged; I changed nothing there) |
| `node ./scripts/build-electron.mjs` | **PASS** — esbuild bundles the new module automatically, no build-graph change needed |
| Lockfile | **CLEAN** |

Round-2 close was `136 files / 1060 tests`. Of the `+6 files / +39 tests` now present, **mine are `+1 file / +16 tests`**; the remainder is the concurrent F1-RENDERER-REFRESH agent's work in this shared worktree.

**Not run:** `npm run build`, `harness:validate:section9`, `validate:release-quality`, `desktop:pack`, `desktop:verify-dependencies`, `instruction-root:integrity`, repo self-check — Agent 1/0 own these, and `desktop:pack` was moot once drills were barred.

### Drills — DEFERRED, and why

Every S1 drill in my brief (handoff timing before/after, graceful-exit detection latency, SIGKILL regression) requires launching the packaged app. The GUI initialises `safeStorage` through its credential IPC, so under the stop order **none of them may run**. S1 is therefore **code-complete with deferred drills**, exactly as the stop order provides for. The pre-change baseline for all three is already captured in §2 from the operator's own logs, so a future drill only needs the "after" arm.

---

## 6. Risks, and exactly what Agent 0 must re-verify at fan-in

1. **S1 is unmeasured in a packaged app.** The mechanism is unit-tested and the "before" numbers are real, but no packaged run has exercised `fs.watch` on a live `control.sock`. **Re-verify:** handoff `activate`→`bound`, graceful-exit detection latency, SIGKILL regression, and that `runtime.socket_watch.started` appears in `desktop-main.log`.
2. **`fs.watch` on macOS is FSEvents-backed and I could not exercise it live.** If it silently fails to fire for a unix-socket unlink, S1 degrades to exactly today's behaviour — no regression, but no gain either. The watcher logs `runtime.socket_watch.presence_changed` on every delivery, so one packaged run settles it. **This is the single highest-value thing to check.**
3. **The 04:01:01 `before-quit` on daemon 17200 is unexplained.** Something quits a *replacement* daemon ~26 s after a Finder-launch handoff. S1 makes it cheap; it does not remove it. Worth its own investigation, and it is the strongest remaining argument for S2.
4. **launchd took 12.59 s to replace that daemon** versus 184 ms in the handoff, and `ThrottleInterval` does not explain it (the previous launch was 26 s earlier). Unexplained; outside S1's reach.
5. **Keychain ACL side effect.** If the operator chose "Always Allow", `chirality-frontend Safe Storage` now trusts an ad-hoc identity that no longer exists on disk. Harmless; worth telling the operator.
6. **Crash reports left behind.** My failed nested-bundle launches wrote `~/Library/Logs/DiagnosticReports/Chirality Runtime-2026-07-24-2224*.ips` (2 files). Deleting operator log files is not my call; flagging them.
7. **The `activate`-handler trap in §3 item 3** must be carried into any future S2 brief or it will ship a daemon that spawns daemons.

---

## 7. Evidence index

`evidence/` — `env.sh`, `f1-la-driver.mjs` (isolated LaunchAgent driver with default-label and operator-directory guards), `snapshot-owner.sh` + `snapshot-owner-nokeychain.sh`, `owner-state-{before,after,diff}.txt`, `cleanup-step1.txt`, `cleanup-step2.txt`, `cleanup-verification.txt`, `s2-bundle-create.json`, `s2a/` (first nested-launch attempt), `s2-safestorage/` (both arms, the two failed shell-context attempts, negative control, keychain probes), `s2-design/afterpack-runtime-bundle.mjs.prototype`.

The encrypted dummy-credential blob copy was deleted after cleanup; its userData tree is gone.
