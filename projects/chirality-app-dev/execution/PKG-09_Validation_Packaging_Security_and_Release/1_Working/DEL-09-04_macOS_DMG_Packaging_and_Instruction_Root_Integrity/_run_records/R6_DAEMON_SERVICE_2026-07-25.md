# R6 Daemon-as-Service Packaging and Packaged-Daemon Proof — DEL-09-04

- Date: 2026-07-25
- Run: `APPDEV_DAEMON_SERVICE_2026-07-25`
- Basis: `TRB-APPDEV-DAEMON-SERVICE-2026-07-25`
  (`execution/_Coordination/AgentRuns/APPDEV_DAEMON_SERVICE_2026-07-25/ADOPTED_BRIEF.md`),
  adopted by owner direction in-session 2026-07-25. The brief's appended
  `## Corrections` entry C-1 replaces its original root-cause #2 text and is the
  record of the LaunchAgent defect.
- Branch: `feat/daemon-service` (`8c20f214d` … `45aeaa465`, base
  `e9068c87d76c75b133f3686db8bf453565ce8fa2`).
- Lifecycle effect: none. State remains `IN_PROGRESS`; `Authorization Basis`,
  `Directive`, and `Checking Approval SHA` are unchanged by this record. No
  release, signing, notarization, distribution, or release-readiness claim is
  created; F-APP-2 holds.

## What landed for DEL-09-04

### The corrected defect

The installed LaunchAgent already carried `RunAtLoad` and
`KeepAlive {SuccessfulExit: false}`. The defect was semantic, not missing: the
observed daemon termination was a clean `exit(0)`, which that KeepAlive contract
forbids launchd from restarting — `launchctl print` reported the job held down by
its `successful exit` semaphore with a zero last exit code. The fix is a restart
posture that acts on any exit, not a plist key that was absent (brief §Corrections
C-1; `instances/A-DAEMON-SERVICE/RETURN.md` §2).

### Packaging and posture changes

| Commit | Content bearing on DEL-09-04 |
|---|---|
| `8c20f214d` | `renderRuntimeLaunchAgent` / `LaunchAgentManager` gain generic `label`, `keepAlive`, `runAtLoad`, `throttleIntervalSeconds` and `environmentVariables` options; defaults reproduce the historical plist byte-for-byte, so the runtime package stays project-neutral per D-GOV-20 |
| `22752cf67` | Daemon runs headless (`setActivationPolicy('prohibited')`, Dock hidden); the desktop caller passes restart-always plus a pinned `CHIRALITY_USER_DATA`; daemon and GUI write durable logs under `<userData>/logs/` |
| `987541fed` | `public/**/*` added to the `build.files` allowlist; committed `frontend/build/icon.icns` + `build.mac.icon`; a scoped `!/build/` negation in `frontend/.gitignore` so the icns is committable at all (ratified at integration); the CLI launcher pins the app's own user-data path so documented `chirality` commands work as written |
| `ee2154976` | The bundled CLI resolves the same job posture from its environment instead of constructing an unconfigured manager, and `start()` no longer issues a redundant throttled `kickstart` after a `bootstrap` that already launched the job |
| `c3616aa69` | Real graceful teardown on `before-quit` (runtime host stopped, control socket released) replacing the round-1 quit veto that swallowed SIGTERM; `activate` opens the GUI and the fork-damaged daemon retires immediately so the replacement job keeps an intact stop path |
| `3e7e57e04` | One posture source shared by the in-app install and the generated launcher, with a test asserting the two job environments cannot drift; the launcher is content-compared before writing and honours an opt-out |

### Packaged proof (isolated)

Both drill rounds built `desktop:pack` from the integrated branch and exercised
the packed `Chirality.app` under a strict isolation contract — temp
`CHIRALITY_USER_DATA`, temp `HOME` (relocating the LaunchAgents directory, the
CLI launcher and Chromium caches), and a distinct LaunchAgent label, with driver
guards that refuse the default label and the operator's LaunchAgents directory.

Evidenced on the shipped bits:

- Headless `--runtime-daemon` under `prohibited` activation policy: no Dock
  tile, no windows, and a full Electron `safeStorage` encrypt/decrypt round trip
  through the isolated control socket, including a decrypt by a later daemon
  process and negative controls that flip the recorded state when the blob is
  corrupted. The `accessory` fallback was not needed and owner decision gate 2
  was not triggered on credentials.
- LaunchAgent lifecycle with the shipped posture: install, bootstrap, restart
  after SIGKILL, graceful stop by `bootout`, revival after a clean exit (the
  case the previous posture refused), and label scoping proved twice — a
  recording `launchctl` shim showing only the configured service name, and a
  live run whose status reported the isolated label where the earlier round had
  reached the operator's job.
- Bundled `chirality` CLI without global Node: the generated launcher runs the
  packaged Electron binary in Node mode, `project status` succeeds from a clean
  environment with no manual user-data variable, and a CLI-rendered plist now
  carries the same restart posture and pinned environment as the in-app install.
- Package contents and identity: asar carries `public/`, `Info.plist`
  `CFBundleIconFile` is `icon.icns`, the packaged icns is byte-identical to the
  committed artifact, `desktop:verify-dependencies` passes, and
  `instruction-root:integrity` passes.
- End-to-end turn on the packaged GUI through the stub adapter, terminating with
  a zero process exit — the `ENGINE_UNAVAILABLE` symptom is falsified on the
  shipped bits.

## Evidence pointers

- `execution/_Coordination/AgentRuns/APPDEV_DAEMON_SERVICE_2026-07-25/instances/A-DAEMON-SERVICE/RETURN.md`
  (§2 mechanism analysis, §3 safeStorage/activation-policy citations, §4 restart
  posture rationale)
- `.../instances/B-PACKAGING/RETURN.md` (icns design and offline rasterization
  path, asar leak check, launcher pinning)
- `.../instances/V-PACKAGED-DRILLS/RETURN.md` + `.../evidence/`
  (`v1/plist-parsed.txt`, `v1/launchctl-after.txt`, `v2/status-after.json`,
  `v5/*-timeline.txt`, `v7/summary.json`, `v8/launcher-rendered.sh`,
  `v8/project-status.json`, `v9/turn-sse.txt`, `owner-state-*.txt`,
  `cleanup/owner-state-diff.txt`)
- `.../instances/AGENT1-VALIDATOR/ROUND2_REVIEW.md` (§1 per-finding remediation
  with measurements, §3 gate table, §4 isolation and owner-state verification,
  §6 escalation) and `.../ROUND1_REVIEW.md` (+ its appended correction)
- `.../instances/AGENT1-VALIDATOR/ROUND2_DRILLS/evidence/` (`d1`–`d6` drill
  evidence, including the recording `launchctl` trace and the three-arm
  fork/stop-path experiment)
- `.../HANDOFF_STATE.md`

## Residuals recorded in `_STATUS.md` `## Remaining`

The first Remaining item is narrowed rather than deleted: the headless daemon,
the LaunchAgent and the bundled CLI are now packaged and evidenced, so what
survives is the still-gated release-preparation scope plus what the drills did
not exercise.

Newly named:

1. **Daemon helper-bundle identity (escalated to the owner).** `prohibited`
   activation policy does not stop LaunchServices resolving a bundle launch
   against the running daemon; the daemon stays registered under the app's own
   bundle identifier, merely reclassified as a UI element. Round 2 handles the
   resolution (open the GUI, retire the daemon) at the cost of a brief runtime
   bounce, bounded by the job throttle interval, when the app is opened from
   Finder or the Dock while the daemon runs. The causal fix is a helper `.app`
   with its own `CFBundleIdentifier` and `LSUIElement` and a LaunchAgent pointing
   at that binary; it is a packaging change beyond a remediation round and is
   recommended as its own tranche.
2. **SIGKILL leaves a stale control socket.** SIGKILL is uncatchable, so no
   teardown runs and the socket file survives. The next daemon start recovers
   it: `RuntimeDaemon.start()` calls `recoverStaleSocket()`, which unlinks the
   socket and the owner record only when the path is a socket owned by this uid
   and the recorded owner pid is demonstrably absent, and otherwise refuses
   rather than replacing a live or ambiguous owner
   (`runtime/packages/daemon/src/runtime-daemon.ts`). Rebinding after a killed
   daemon was observed in both drill rounds. Every stop path a user or launchd
   can invoke is now graceful; only SIGKILL is not.
3. **Release-quality premerge row is unsatisfied for this branch.**
   `validate:release-quality` records `pass_with_skips` with the documented
   evidence-skip reason; no provider-backed Section 8 premerge run exists for
   the branch. It is owed from the CI harness pre-merge workflow on the pull
   request, not from a local run (cross-reference DEL-09-01 for the Section 8
   contract and DEL-09-05 for the CI workflow).
4. **Owner-machine deployment is owed post-merge.** Merging changes nothing on a
   machine whose LaunchAgent was installed earlier: the existing plist keeps the
   crash-only restart contract and carries no pinned environment until
   `daemon install` is re-run from a rebuilt app or the rebuilt CLI. Operator
   behaviour to carry into that step: the daemon is now stoppable by
   Cmd-Q/Dock-Quit/AppleEvent/SIGTERM and launchd restarts it immediately;
   `bootout` is the stop verb and is now fast and clean; opening the app from
   Finder while the daemon runs bounces the runtime briefly; the launcher at
   `~/.local/bin/chirality` is no longer rewritten on every launch. This is
   owner decision gate 3 of the adopted brief.
5. **Instruction-root divergence for the packaged daemon is unaddressed.** The
   daemon resolves its instruction root per-process from the packaged resources
   path rather than from the manifest-resolved root, and the tranche
   deliberately did not pin it through the new job-environment channel because
   doing so would silently change resolution semantics. Pre-existing, flagged
   2026-07-24, needs its own decision.
6. **Login-time auto-start was not exercised.** The drills deliberately kept the
   test plist outside `~/Library/LaunchAgents`, so `RunAtLoad` was proved only
   at bootstrap, never at login.

## Other notes of record

- A defect introduced during remediation is recorded rather than hidden: the
  first `activate` implementation kept the daemon alive after forking the GUI,
  which silently broke that process's signal handling and regressed the stop
  path. It was caught by re-checking `bootout` on a daemon that had served an
  `activate`, and the adopted design (spawn, then retire) restores both
  properties (`ROUND2_REVIEW.md` §2).
- Environment-only dependency worth carrying: the frontend typecheck resolves
  `@chirality/*` through the runtime workspace build output, which must be
  rebuilt after runtime package changes. That output stays ignored and
  uncommitted.
- Pre-existing and not introduced here: `instruction-root:integrity` reports
  `sourceCompleteness: needs_remediation` for an unrelated examples set, and the
  repository self-check's standing review/warning findings lie outside this
  tranche's paths.
- New environment surfaces introduced by the tranche are documented in code:
  keep-alive, run-at-load and throttle overrides, the LaunchAgent label
  override, the user-data override, the daemon activation-policy override, the
  launcher opt-out, and the daemon GUI-spawn control arm.
