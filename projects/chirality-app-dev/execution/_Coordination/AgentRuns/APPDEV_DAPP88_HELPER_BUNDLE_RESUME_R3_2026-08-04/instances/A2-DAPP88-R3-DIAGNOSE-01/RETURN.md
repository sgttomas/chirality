# A2-DAPP88-R3-DIAGNOSE-01 — defect diagnosis return

## Status

`CONFIRMED_BLOCKER`

The current evidence does not support one exact App-native remedy within
D-APP-88 authority. The mandatory post-GUI first-signal conjunct remains
failed and must not be weakened.

## Frozen symptom and expected behavior

- Symptom: on exact source-aligned helper bits after authenticated GUI contact,
  `/bin/kill -TERM 64825` at `2026-08-04T11:33:54-06:00` left the helper alive
  through 80 polls/8 seconds. The socket and owner record retained inodes
  `25329475` and `25329474`; no `desktop.shutdown.started` or completed event
  appeared.
- Expected: the first ordinary post-GUI stop enters the App shutdown funnel,
  invokes accepted Root bounded stop, exits the helper, and removes socket and
  owner state while the GUI remains a distinct client of the same daemon/store.

## Causal evidence matrix

| Evidence | Classification | Supported causal statement | Confidence / boundary |
|---|---|---|---|
| Fresh no-GUI first `SIGTERM` to PID `68812` exited in one poll, logged `desktop.shutdown.started/completed` with reason `before-quit`, and removed socket/owner state. | Control | The packaged helper can enter the App `before-quit -> shutdown -> RuntimeDaemon.stop()` funnel, and the accepted Root stop completes when entered. | High; exact implementer-02 evidence. |
| Exact post-GUI first `SIGTERM` to PID `64825` produced no App shutdown-start event and preserved process/socket/owner state for 8 seconds. | Earliest observable divergence | The failed run diverged before `teardown()` logged its first line. Root stop was not entered in this attempt. | High for the pre-teardown boundary; the evidence does not distinguish OS/native dispatch, JS `process.once` callback entry, or Electron `before-quit` entry because those seams were not separately logged. |
| A fresh post-GUI diagnostic repeated first-signal survival, then the second `SIGTERM` exited in one poll without App shutdown events and left socket/owner state. | Consequence / native fallback | Electron/native termination can end the process after the absorbed first signal while bypassing App/Root cleanup. It cannot satisfy the first-signal acceptance gate. | High; exact implementer-02 evidence. |
| Frozen `electron/runtime-helper-entry.ts` adds helper-only `single-process` and `disable-gpu` before importing `main.ts`. Frozen `main.ts` already registers both `process.once('SIGTERM', shutdown)` and `app.on('before-quit', shutdown)`. | Suspected contributing condition | `single-process` is a bounded hypothesis, not a proven cause. The existing two App-native funnels are present but produced no observable teardown entry after GUI contact. | High for source facts; causality unresolved. |
| R2 reports that a standard-process arm was observed to fail, but explicitly records no retained raw artifact. | Alternative considered | The historical observation prevents treating removal of `single-process` as a supported remedy; it is not independently usable as a causal finding. | Low / unauditable by the accepted R2 boundary. |
| The exact Electron 43.2.0 cached runtime was used for four run-local probe arms: standard-idle PID `70661`, standard-contact `70675`, single-idle `70667`, and single-contact `70683`. All exited `134` before `app.whenReady`/`probe.ready`, with no stdout, stderr, or event record. | Failed live comparison | This environment cannot supply a standard-versus-single native lifecycle matrix. No signal was sent and no arm receives causal credit. | High for the abort; cause of the pre-ready abort is unknown. |
| Root TM-ROOT-112 accepted bytes bound stop, force-close residual transports, and clean socket/owner state; implementer-02 proved these bytes work when App teardown calls them. | Alternative ruled out for this attempt | No further generic Root semantic is evidenced by the post-GUI failure. | High within this run; Node 22.19 remains unexecuted. |

## Causal conclusion

- Root cause: unresolved inside the Electron/App signal-dispatch seam between
  delivery of the first post-GUI `SIGTERM` and entry to the first observable
  App teardown line.
- Contributing condition: authenticated GUI contact is the proven condition
  across which behavior changes. Helper-only `single-process` remains a
  plausible but unproved contributor.
- Consequence: the first ordinary stop neither drains Root nor removes socket
  and owner state; the second signal terminates natively and leaves stale state.
- Unknowns: whether the first signal reaches Electron `before-quit`, whether
  the JS `process.once` callback runs, whether standard-process exact package
  bits behave differently, and what native state GUI contact changes.

No lifecycle-listener substitution, `single-process` deletion, signal-handler
ordering change, or other App-native source hunk is supported strongly enough
to brief an implementation node. Adding a wrapper, supervisor, singleton,
second daemon, Root change, or weakened first-signal gate remains prohibited.

## Exact next evidence and owner boundary

Next owner: App `HELP_HUMAN` through `WORKING_ITEMS`. It must either provide a
macOS execution context that can launch exact Electron 43.2.0 package bits with
the already-locked dependencies, or hold D-APP-88 open. No Root owner action is
supported by this diagnosis.

The next bounded diagnostic must return all of the following before another
implementation node is released:

1. Two source-aligned helper packages with identical source, Electron 43.2.0,
   bundle identity, and package topology, differing only by removal of
   `app.commandLine.appendSwitch('single-process')` in
   `electron/runtime-helper-entry.ts` for the standard arm.
2. Run-local seam instrumentation immediately on JS `SIGTERM` callback entry,
   `before-quit` entry, `will-quit`, `quit`, `teardown()` entry, and Root stop
   call/settlement. Instrumentation is diagnostic evidence, not a product fix.
3. Pre-GUI and authenticated-post-GUI first-signal runs for both arms, with
   exact PID, command/time, 0.1-second bounded polls, exit code, process/socket/
   owner inodes, Unix/TCP descriptors, logs, and source/package hashes.
4. If and only if one arm makes the first post-GUI signal deterministic, a
   focused regression that fails on the other arm plus the full D-APP-88
   package/live acceptance conjunction. Otherwise route an Electron-native
   reproduction to the appropriate upstream technical owner without changing
   Root or product semantics.

## Method and scope compliance

- Method: `software-defect-diagnosis` applied by a sealed ephemeral Agent 2;
  no delegation.
- Product/governance/Root/deliverable writes: none.
- Network, install, Git, provider, release, or owner-machine deployment: none.
- Retained writes: this return, cleanup record, and sanitized failed-probe
  metadata/empty logs under this instance only.
- Node 22.19: not executed.
