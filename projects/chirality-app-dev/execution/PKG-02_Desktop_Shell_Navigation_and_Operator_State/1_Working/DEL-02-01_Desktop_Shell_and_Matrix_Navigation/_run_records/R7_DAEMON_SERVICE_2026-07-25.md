# R7 Daemon-as-Service and Packaged-App Fixes — DEL-02-01

- Date: 2026-07-25
- Run: `APPDEV_DAEMON_SERVICE_2026-07-25`
- Basis: `TRB-APPDEV-DAEMON-SERVICE-2026-07-25`
  (`execution/_Coordination/AgentRuns/APPDEV_DAEMON_SERVICE_2026-07-25/ADOPTED_BRIEF.md`),
  adopted by owner direction in-session 2026-07-25 ("draft the brief and proceed
  using the same subagent delegation model established in this session"). The
  brief carries an appended `## Corrections` section (C-1); the correction, not
  the original root-cause text, is the record of the LaunchAgent defect.
- Branch: `feat/daemon-service` (`8c20f214d` … `45aeaa465`, base
  `e9068c87d76c75b133f3686db8bf453565ce8fa2`).
- Predecessor record: `_run_records/R6_WOVEN_REDESIGN_2026-07-24.md`, whose four
  residuals this tranche was raised against.
- Lifecycle effect: none. State remains `IN_PROGRESS`; `Authorization Basis`,
  `Directive`, and `Checking Approval SHA` are unchanged by this record.

## What landed for DEL-02-01

**Owner-reported defect.** On the packaged app the redesigned shell showed no
quincunx logo and every harness request failed with
`ENGINE_UNAVAILABLE: Chirality runtime daemon client is not configured`. The
owner rejected per-launch manual workarounds and directed that the daemon become
a real machine-local service.

| Commit | Content bearing on DEL-02-01 |
|---|---|
| `22752cf67` | Daemon sheds app identity (`setActivationPolicy('prohibited')`, hidden Dock); supervised GUI binding (`electron/runtime-connectivity.ts`, retry ladder 1s→2s→5s→10s steady plus a 10s liveness probe, main-process owned); connectivity IPC (query + push to every window) and preload bridge; the runtime-connectivity chip in `shell-frame.tsx` as a sibling of the working-root chip; durable file logging (`desktop-main.log` / `desktop-daemon.log`) replacing the swallowed `console.warn` |
| `987541fed` | `public/**/*` added to `build.files`, so `<img src="/chirality-app-icon.svg">` in the shell top bar resolves inside the asar; committed `frontend/build/icon.icns` + `build.mac.icon` |
| `c3616aa69` | Daemon quit veto dropped for real graceful teardown; the daemon opens the GUI on `activate` and then retires, so a Finder/Dock launch produces a window instead of nothing |
| `3e7e57e04` | One daemon posture for both install surfaces; idempotent CLI launcher; daemon-down credential status no longer rejects into the renderer (removing the top-bar-adjacent error noise; DEL-02-05 owns that surface) |

**Presentation discipline.** The chip uses existing tokens only (`--sage*`,
`--slate*`, `--danger*`, `--rule`, `--ground`, `--ink-*`); no token was added or
changed. New classes live on the disjoint `shell-runtime-*` prefix and a
regression test asserts exactly one `shell-root-dot*` node survives beside a
runtime chip, so the working-root dot contract from the redesign is preserved
rather than incidentally intact. The chip renders `null` when no bridge exists
(SSR, browser, older preload) so a web render never claims a runtime state it
cannot observe.

**Packaged Desktop evidence now exists for the redesigned shell.** Stage V ran
the packed `Chirality.app` under a full isolation contract (temp
`CHIRALITY_USER_DATA`, temp `HOME`, distinct LaunchAgent label) and captured
window-scoped frames of the shell itself: the quincunx logo tile and serif
wordmark, the `RUNTIME connected` chip beside the `ROOT` chip, the
Dialogue/Workbench/Pipeline navigator groups, the Work/Agents coordination
projection, the Activity shelf, and the legacy-window affordance. Connectivity
transitions were observed on the packaged app across a daemon outage —
offline → connected → offline mid-session → connected — with no restart, no
devtools and no manual action, and an end-to-end stub-adapter turn completed
through the packaged GUI's harness surface (`process:exit` exit code zero),
which is the direct falsification of the reported `ENGINE_UNAVAILABLE` symptom.

**Packaged application icon shipped.** `Info.plist` `CFBundleIconFile` is
`icon.icns`, the packaged icns is byte-identical to the committed
`frontend/build/icon.icns`, and the extracted representations plus the Dock and
Finder captures show the quincunx rather than the stock Electron atom. The icns
is an icns-tuned redraw on a 1024 canvas (mark footprint reduced to the Apple
icon grid, hairline stroke rescaled), not an upscale of the 32-unit in-app mark,
and it is generated offline by a one-time script kept out of the build graph so
electron-builder never fetches its icon toolset.

## Evidence pointers

- `execution/_Coordination/AgentRuns/APPDEV_DAEMON_SERVICE_2026-07-25/instances/A-DAEMON-SERVICE/RETURN.md`
  (§5 connectivity surface design; §7 known limits)
- `.../instances/B-PACKAGING/RETURN.md` (§B1/B2 packaging and icon decisions,
  including the packaging-leak check that keeps `build/` out of the asar)
- `.../instances/V-PACKAGED-DRILLS/RETURN.md` + `.../evidence/`
  — `v3/v3-window-connected.png`, `v3/v3-quincunx-logo.png`,
  `v3/v3-topbar-connected.png`, `v0/v0-window-disconnected.png`,
  `v0/v0-topbar-offline.png`, `v5/v5-topbar-error.png`,
  `v5/v5-topbar-reconnected.png`, `v7/v7-dock-tile.png`,
  `v7/v7-finder-window.png`, `v7/summary.json`, `v9/turn-sse.txt`
- `.../instances/AGENT1-VALIDATOR/ROUND1_REVIEW.md` (integration validation and
  its appended correction) and `.../ROUND2_REVIEW.md` (remediation round, gate
  table, escalation §6)
- `.../HANDOFF_STATE.md` (accepted upstream basis, closure verdict, rerun
  requirements, residuals)

## Residuals recorded in `_STATUS.md` `## Remaining`

Closed by this tranche: packaged Desktop smoke evidence for the redesigned
shell; the true runtime-connectivity indicator; the `.icns` / electron-builder
packaged application icon (DEL-09-04 carries the packaging-side record).

Retained: the record-only `metadata.icons` file-convention note.

Newly named:

1. Opening the app from Finder or the Dock while the daemon runs bounces the
   runtime briefly (self-healing, visible in the chip). The causal fix is a
   daemon helper bundle with its own identity; that is escalated to the owner
   and recorded against DEL-09-04.
2. The connectivity chip has no operator reconnect affordance. `refreshNow()`
   exists and is reachable only through the runtime panel's daemon actions; a
   top-bar control was out of scope.
3. Packaged Desktop evidence for the Workbench and Pipeline surfaces
   (DEL-02-02) and for the navigator recorded-session selection path
   (DEL-08-02) is still owed and stays recorded against those deliverables —
   the packaged frames captured here show the shell at the Dialogue surface
   with no recorded sessions in the isolated user data.

## Other notes of record

- The `pending` (slate) chip tone was never observed in the packaged drills:
  binding either succeeds in tens of milliseconds or fails immediately, so the
  observed sequence is `error → ready` rather than the predicted
  `pending → error → ready`. Presentation is correct; the prediction was wrong.
- The daemon is no longer un-quittable. The round-1 quit veto was dropped after
  drills showed it swallowed SIGTERM; graceful teardown plus a restart-always
  LaunchAgent posture carry the original defect instead.
- All drills ran against isolated state; the owner's live LaunchAgent, user
  data, CLI launcher and main checkout were verified byte-unchanged before and
  after both drill rounds.
