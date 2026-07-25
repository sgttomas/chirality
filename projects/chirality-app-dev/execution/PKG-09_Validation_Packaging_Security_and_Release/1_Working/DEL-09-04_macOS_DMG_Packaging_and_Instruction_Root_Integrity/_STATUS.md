# Status: DEL-09-04

**Current State:** IN_PROGRESS
**Last Updated:** 2026-07-25
**Authorization Basis:** D-APP-19 Option D ruling 2026-06-20; owner-approved SHA 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec recorded 2026-06-20
**Directive:** owner inspection-phase directive 2026-06-20
**Checking Approval SHA:** 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec

## Remaining

- Headless `--runtime-daemon`, the opt-in LaunchAgent, and bundled `chirality`
  CLI execution without global Node are packaged and evidenced on the packed app
  under isolation (2026-07-25 daemon-service tranche;
  `_run_records/R6_DAEMON_SERVICE_2026-07-25.md`). What remains of the original
  item is the login-time `RunAtLoad` path, never exercised because the drill
  plist deliberately lived outside `~/Library/LaunchAgents`, and DMG/dist
  packaging (gated: G5 packaging; no release authority; F-APP-2 fences signing,
  notarization and distribution).
- Packaging/release evidence for DEL-09-04's R4-P49 claim family is deferred on 2026-07-12 to a release-preparation phase; PARTIAL assessments and packaged-SDK proof gates remain open (D-APP-56 R4-P49; gate: owner-authorized release preparation).
- Give the daemon its own bundle identity (escalated to the owner as a future
  tranche). Activation-policy suppression does not stop LaunchServices resolving
  a bundle launch against the running daemon, which stays registered under the
  app's bundle identifier as a UI element; the current handling opens the GUI and
  retires the daemon, costing a brief self-healing runtime bounce bounded by the
  job throttle interval when the app is opened from Finder or the Dock while the
  daemon runs. The causal fix is a helper `.app` with its own
  `CFBundleIdentifier` and `LSUIElement`, with the LaunchAgent pointing at that
  binary.
- Recover-on-start is the only answer to a SIGKILLed daemon's stale control
  socket. SIGKILL is uncatchable, so no teardown runs; the next daemon start
  unlinks the socket and owner record only when the path is a socket owned by
  this uid and the recorded owner pid is demonstrably absent, and otherwise
  refuses rather than replacing a live or ambiguous owner. Rebinding after a
  killed daemon was observed in both drill rounds. Every other stop path is now
  graceful; decide whether the SIGKILL case needs anything further.
- Satisfy the release-quality premerge row for the daemon-service branch. The
  local run records `pass_with_skips` with the documented evidence-skip reason;
  no provider-backed Section 8 premerge run exists for the branch, and it is
  owed from the CI harness pre-merge workflow on the pull request
  (cross-reference DEL-09-01 for the Section 8 contract, DEL-09-05 for the CI
  workflow).
- Deploy the daemon service on the owner's machine post-merge (owner decision
  gate 3 of `TRB-APPDEV-DAEMON-SERVICE-2026-07-25`). Merging alone changes
  nothing on a machine whose LaunchAgent was installed earlier: the existing
  plist keeps the crash-only restart contract and carries no pinned environment
  until `daemon install` is re-run from a rebuilt app or the rebuilt CLI.
  Operator-facing behaviour changes are enumerated in the run record.
- Decide the instruction-root divergence for the packaged daemon (pre-existing,
  flagged 2026-07-24, deliberately not addressed in the 2026-07-25 tranche). The
  daemon resolves its instruction root per-process from the packaged resources
  path rather than from the manifest-resolved root; pinning it through the job
  environment would silently change resolution semantics and needs its own
  decision.

## History
- 2026-07-25 - Daemon-as-service and packaged-app fix tranche recorded in `_run_records/R6_DAEMON_SERVICE_2026-07-25.md`. The headless-daemon / LaunchAgent / bundled-CLI Remaining item is narrowed to its unexercised login-time path and the still-gated DMG/dist scope on the strength of isolated packaged-app evidence (headless daemon with a `safeStorage` round trip, LaunchAgent install/restart/graceful-stop and label scoping, bundled CLI from a clean environment, asar `public/` and `CFBundleIconFile` checks, an end-to-end stub-adapter turn). Six residuals are added: daemon helper-bundle identity (owner-escalated), the SIGKILL stale-socket recover-on-start case, the unsatisfied premerge row for this branch, post-merge owner-machine deployment (owner decision gate 3), the pre-existing packaged-daemon instruction-root divergence, and the login-time `RunAtLoad` path folded into the narrowed first item. No release, signing, notarization, or distribution authority is created. State remains IN_PROGRESS; lifecycle and Checking Approval SHA are unchanged.
- 2026-07-22 - D-APP-72 Electron `43.1.1` regression and packaged offline Pi `0.80.10` production-route proof completed. The unrelated D-APP-56 release-preparation item remains open; no release authority is created. State remains IN_PROGRESS; lifecycle and Checking Approval SHA are unchanged.
- 2026-07-21 - SCA-APP-002 added the Electron/Pi package prerequisite proof to Remaining; release fence and state remain unchanged.
- 2026-07-20 - D-APP-71 Option 2 closed the preload physical-lead residual by applying DEL-02-05 as coordination-only lead; DEL-09-06 retains `safeStorage`/security semantics, the packaging/release Remaining item is byte-preserved, and no source, SOW, dependency, lifecycle, or Approval-SHA change occurred.
- 2026-07-20 - D-APP-70 Option A closed the `chirality-window.d.ts`, scripted SDK proof, and contract-lint CQ-F1 residuals and applied only the shared-boundary annotation for `preload.ts`; its unnamed physical lead remains the sole CQ-F1 residual gated by D-APP-71; unrelated packaging/release Remaining is unchanged; no source, lifecycle, Approval SHA, SOW, or dependency change.
- 2026-07-12 - D-APP-56 consolidated R5 decision application recorded; generic concordance Remaining retained for R6; state remains IN_PROGRESS.
- 2026-05-20 - State set to INITIALIZED (TASK+four-documents P1/P2)
- 2026-05-20 - State set to OPEN (PREPARATION)
- 2026-05-23 - State set to SEMANTIC_READY (ORCHESTRATOR_PHASE_2_5_CLOSEOUT)
- 2026-06-16 - State set to IN_PROGRESS (HUMAN) [Human authority: active code implementation underway.]
- 2026-06-20 - State set to CHECKING (HUMAN)
- 2026-07-11 - State set to IN_PROGRESS (HUMAN) [Owner-ruled lifecycle rebaseline D-APP-54 2026-07-11: administrative correction superseding the D-APP-19 inspection-admission convention; prior approvals and history preserved (execution/_Coordination/_DECISIONS/D-APP-54_RULING_2026-07-11.md).]
- 2026-07-11 - Remaining item added: concordance bootstrap seeded at packet time per D-APP-55 packet; no state change.
- 2026-07-11 - Remaining item updated: concordance bootstrap gate flipped and pinned method revision 551f84ef6 substituted per the D-APP-55 ruling (Option A, whole corpus); no state change.
- 2026-07-12 - D-APP-56 R5 P40 applied UPD-075, UPD-078; generic concordance Remaining item retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - R6 closeout completed the D-APP-55 concordance bootstrap and removed it from Remaining; surviving deliverable-local items retained; state remains IN_PROGRESS.
