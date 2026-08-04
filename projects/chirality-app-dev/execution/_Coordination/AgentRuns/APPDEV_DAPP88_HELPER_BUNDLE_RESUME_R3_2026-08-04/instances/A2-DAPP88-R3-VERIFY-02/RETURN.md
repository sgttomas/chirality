# A2-DAPP88-R3-VERIFY-02 — fresh exact-matrix adversarial return

## Verdict

`PASS`

The R3 evidence supports truthful manager fan-in as a calibrated technical
blocker/handoff. It does not support D-APP-88 implementation acceptance or an
App-native remedy.

## Check-by-check result

| # | Result | Independent finding and evidence |
|---:|---|---|
| 1 | PASS | Root sequencing fitness remains correctly bounded. The signed acceptance transcript is SHA-256 `a10bda1c05fe1e1249a7efa266401ddf71752e4d9a8ab0448ec96251d5973046`; current `docs/SPEC.md`, `runtime-daemon.ts`, and `daemon.test.ts` match accepted hashes `647eee2d...d6a7f`, `22440300...ddf2`, and `c853f207...b352`. These bytes satisfy the prior App-rerun prerequisite, not R2 causality, Electron signal behavior, App process proof, or Node 22.19. See `ROOT_EVIDENCE_FITNESS.md` and `NOTICE_2026-08-04_ROOT_TM-ROOT-112_ACCEPTED_GRACEFUL_STOP_REPAIR.md`. |
| 2 | PASS | Implementer-02's corrected return remains SHA-256 `df18333874028dddf8e1b08218fb5d6751e30bbd4a20167f11bdd0f2d453143a`. `evidence/FIRST_SIGNAL_PROOF.md` (SHA-256 `a81cdd7f...f9ec`) binds authenticated GUI contact, helper/GUI PIDs `64825`/`64872`, `/bin/kill -TERM 64825` at `2026-08-04T11:33:54-06:00`, 80 polls at 0.1 seconds, both processes alive, and unchanged socket/owner inodes `25329475`/`25329474`. No App shutdown-start/completion occurred, so Root stop was not entered. This proves the failure boundary without assigning cause. |
| 3 | PASS | The frozen R2 candidate has 12 complete source files; its hashes independently reproduce the R2 manifest, including uninstrumented `electron/main.ts` `5eeac85f...f491` and SINGLE helper entry `7e0ab20f...e2bc`. Diagnosis-02-R2 preserves the other 11 candidate hashes and replaces only `main.ts` with identical diagnostic bytes `82e9a8da...2239` in both variants. `evidence/source/SINGLE_VS_STANDARD_SOURCE.diff` shows the sole inter-variant source difference: removal of `app.commandLine.appendSwitch('single-process');`; `disable-gpu` remains. Package comparison records exactly two derivative hash changes (`app.asar`, integrity-bearing `Info.plist`), zero additions/removals, 446 files each, and identical 14-relative-link manifests. |
| 4 | PASS | All four credited arms are auditable. SINGLE pre-GUI credit is the GUI-session rerun PID `81306` in `pre-gui-escalated.*`, not the earlier aborted PID `80464`; SINGLE post-GUI is helper/GUI `81840`/`81898`; STANDARD pre-GUI is `83291`; STANDARD post-GUI is `83398`/`83413`. Each credited helper reached ready, received its recorded first `/bin/kill -TERM <pid>`, exited 0 by poll 2, logged `before-quit.entry -> teardown.entry -> runtimeHost.stop.before -> runtimeHost.stop.after(resolved) -> quit.entry`, and had socket/owner absent afterward. Both post-GUI arms record authenticated binding at poll 2. The GUI survived helper settlement, then was deliberately cleaned up: helper `quit.entry` precedes GUI `before-quit.entry` by about 121 ms in both variants, and cleanup exits 0 at poll 1. It would be inaccurate to claim that either GUI remained running after the cleanup step. |
| 5 | PASS | The initial sandbox-contained SINGLE PID `80464` never reached ready and exited 134. It is isolated in `pre-gui.*`; the credited SINGLE pre-GUI arm is `pre-gui-escalated.*`. The abort receives context-only execution-substrate credit and no runtime-arm or causal credit. |
| 6 | PASS | Relative inference is calibrated. Both instrumented variants pass identically, so deleting `single-process` is not supported as cause, contributor, or remedy in this comparison. The common synchronous logger controls that relative comparison but changes `main.ts`, adds listeners, and performs synchronous writes in callbacks; it may perturb absolute timing. Therefore the earlier uninstrumented failure and later instrumented passes remain simultaneously valid and neither erases the other. See `CAUSAL_MATRIX.md` SHA-256 `e5635b6f...67be`. |
| 7 | PASS | No exact App-native remedy is supported. The evidence does not justify a lifecycle-listener substitution, signal-handler reordering, switch deletion, wrapper, supervisor, extra singleton/daemon, weakened first-signal gate, Root change, or product acceptance. `A2-DAPP88-R3-IMPLEMENT-03` must remain unreleased. |
| 8 | PASS — HANDOFF BOUNDARY | The proposed “exact earlier-R3 sequence replay with non-perturbing native/Electron capture” is not a concrete executable node on the retained evidence/current capability. Implementer-02 preserved outcome summaries and coarse timestamps, but not a byte-complete launch/interaction command transcript for every action in the roughly 102-second contact-to-signal interval. The current run also has no authorized out-of-process native tracer proven able to distinguish OS signal delivery, libuv JS callback entry, and Electron `before-quit` entry without modifying App bytes or adding synchronous callback work. The exact prerequisite for another node is: (i) owner-authorized interactive macOS GUI-session native signal tracing capability, including any required privilege/entitlement approval; (ii) a sealed replay script/transcript that fixes the uninstrumented R2 source/package hashes, stale-owner recovery, helper-to-GUI delay, authenticated contact, contact-to-signal delay, snapshot sequence, exact first signal, and cleanup; and (iii) trace evidence bound to PID/time that distinguishes delivery, JS callback entry, Electron lifecycle entry, teardown, and Root-stop entry. Immediate owner is App `HELP_HUMAN` through `WORKING_ITEMS`; absent those prerequisites, hold D-APP-88 open. This is not a request for generic “more diagnosis.” |
| 9 | PASS | Rollback/cleanup was independently reproduced. The seven original files match hashes `850f7b00...335b`, `16ad6688...1f`, `5006bef6...026a`, `1f14df17...ba53`, `a6759be0...5558`, `1918ae7d...91e9`, and `f8b6d8c2...36be`; unchanged `package-lock.json` is `5c8fce2a...a56`. All five additions, `frontend/node_modules`, `dist`, `dist-runtime-helper`, `dist-electron`, `dist-runtime`, `.next`, the instruction-root `latest` derivative, and all three named `/private/tmp/chirality-dapp88-r3*` trees are absent. Frontend Git status is empty. `kill -0` cannot signal any known R3/diagnostic PID. The diagnosis tree has 93 files; `EVIDENCE_SHA256.txt` inventories and successfully verifies all other 92 files, while its own SHA-256 is `51fb6ecb...7070`. Targeted secret-value review found token-file paths/public identifiers only, not token or credential values. |
| 10 | PASS | D-APP-89 remains the source baseline; live `frontend/package.json` is restored to `1f14df17...ba53`. D-APP-91 remains planning-only with its TM-PIP-025 rider and no product effect. `HISTORICAL_RELATIONS.csv` remains SHA-256 `e4f3896b...d1d8` with exactly six `HISTORICAL_RELATION_UNKNOWN` rows. DEL-09-04 remains `IN_PROGRESS` with Checking Approval SHA `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`. No foreign-loop, governance, release, lifecycle, reliance, or Git effect is supported. Limitations remain explicit: Node 22.19 unexecuted; safeStorage not rerun on the owner keychain; managed-service premerge and overall release-quality failed; practitioner pytest/PyYAML checks failed for environment reasons; no release credit follows. |
| 11 | PASS | D-APP-88 remains open and DEL-09-04 retains the helper-identity/first-signal residual. `TM-APP-036` remains an open non-blocking rider and does not fire unless a later governed D-APP-88 implementation acceptance occurs. The present exact-matrix result is diagnosis only. |

## Blocking and nonblocking findings

- Blocking technical finding: the mandatory uninstrumented post-GUI first-signal
  conjunct failed, while the later instrumented variants both passed. No
  causal App-native source hunk follows from that evidence.
- Blocking handoff prerequisite: a further causal replay requires the exact
  native tracing capability and sealed replay record described in check 8.
- No evidence-integrity, rollback, preservation, or calibration defect blocks
  manager fan-in as `BLOCKED / CONFIRMED_BLOCKER`.
- Node 22.19, owner-keychain safeStorage, premerge/release-quality, and
  practitioner-environment gaps remain limitations and receive no credit.

## Exact blocker/handoff wording verified for manager fan-in

> D-APP-88 remains open. The exact uninstrumented R3 helper failed the
> mandatory authenticated post-GUI first SIGTERM before observable App
> teardown: after 80 0.1-second polls, helper and GUI were alive, socket and
> owner inodes were unchanged, no shutdown-start entry existed, and Root stop
> was not entered. The later exact instrumented SINGLE and STANDARD packages
> both passed pre-GUI and authenticated post-GUI first-SIGTERM controls
> identically, entering `before-quit`, teardown, and resolved Root stop,
> removing socket/owner state, and exiting 0 by poll 2; each GUI survived helper
> settlement and was then deliberately cleaned up. Therefore removal of
> `single-process` and every other App-native remedy remain unsupported. The
> common synchronous logger controls the relative comparison but may perturb
> absolute behavior, so neither the earlier failure nor later passes erase the
> other. A further exact replay is held until App `HELP_HUMAN` / `WORKING_ITEMS`
> can authorize an interactive GUI-session native signal tracer and seal the
> complete uninstrumented launch/contact/timing transcript needed to
> distinguish OS delivery, libuv callback entry, Electron lifecycle entry,
> teardown, and Root-stop entry. No wrapper, supervisor, singleton, weakened
> gate, Root change, DEL reconciliation, parity firing, release, or Git effect
> follows. Node 22.19 and the stated safeStorage/premerge/release-quality/
> practitioner limitations remain open.

Final verdict: `PASS`.
