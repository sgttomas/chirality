# Status: DEL-09-04

**Current State:** IN_PROGRESS
**Last Updated:** 2026-08-21
**Authorization Basis:** D-APP-19 Option D ruling 2026-06-20; owner-approved SHA 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec recorded 2026-06-20
**Directive:** owner inspection-phase directive 2026-06-20
**Checking Approval SHA:** 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec

## Remaining

- Actual login-session discovery and auto-start remain unproved. The exact
  reviewed two-phase harness/test candidate is restored at live frontend paths
  under the owner's superseding **“Push through failures”** direction.
  Implementation preparation is complete: Agent 0 repaired only the ignored
  dependency workspace, and mandatory integrated Vitest/typecheck/build plus
  the focused affected trio now pass. Fresh integrated review found only three
  record defects; amendment 10 fixed them and the direct backcheck passed with
  zero actionable findings and unchanged product hashes. The local managed premerge attempt reached
  a READY Next service but returned HTTP 503 because the shared runtime
  daemon/project registration lifecycle was absent; premerge is PR-CI-owned and
  must rerun after PR. Root runtime writes, unrelated App mocks, and tracked
  setup files remain untouched. See
  `_run_records/R12_LOGIN_SESSION_PROOF_PREPARATION_2026-08-21.md`. Logout/login
  and capture remain unexecuted owner acts. A current unsigned app-directory
  package has now been rebuilt from exact commit
  `1b375af4f1219ecfc00fc2755854aa7fd4220901`; current-byte instruction-root
  integrity, including the post-#602 HELP_HUMAN bytes, passed and the concrete
  two-phase owner procedure is staged without execution in
  `_run_records/R13_POST_ROOT_LOGIN_PROOF_ENABLEMENT_2026-08-21.md`. No proof or
  publication is claimed.
- After a rebuilt C1 artifact exists, the owner may deploy the daemon service
  on the owner's machine and report the result (owner act, not agent work;
  owner decision gate 3 of `TRB-APPDEV-DAEMON-SERVICE-2026-07-25`). Merging alone changes
  nothing on a machine whose LaunchAgent was installed earlier: the existing
  plist keeps the crash-only restart contract and carries no pinned environment
  until `daemon install` is re-run from a rebuilt app or the rebuilt CLI.
  Operator-facing behaviour changes are enumerated in the run record.

## History
- 2026-08-21 - Post-Root login-proof enablement rebuilt the unsigned arm64 app
  directory with `npm run desktop:pack` from exact commit
  `1b375af4f1219ecfc00fc2755854aa7fd4220901`. The dependency-boundary and
  current-byte instruction-root checks passed; source and bundle
  `AGENT_HELP_HUMAN.md` both match SHA-256
  `0285715cbe41ac2c8b7bfd8b6dbd56ad1f0cbb1a970a4f7afed290fc30d1e981`.
  The frontend-tree commit-to-HEAD diff is empty. R12's owner procedure is now
  staged with concrete unique absent proof values, but prepare, logout/login,
  capture, GUI launch, operator deployment, and proof remain unexecuted owner
  acts. The accepted first-GUI-launch launcher rewrite is recorded as an
  expected operator-facing effect, not a park condition. DEL-09-04 remains
  IN_PROGRESS; no signing, notarization, distribution, publication,
  release-readiness, issuance, or reliance claim is made. See
  `_run_records/R13_POST_ROOT_LOGIN_PROOF_ENABLEMENT_2026-08-21.md`.
- 2026-08-21 - Owner-authorized PREPARE-THEN-OWNER work produced a reviewed
  fail-closed two-phase candidate and minimal future owner procedure. Focused
  tests, syntax, exact scope, practitioner checks, APP-HOLD integrity, and final
  fresh review passed, while mandatory integrated gates exposed the external
  `RUNTIME_INSTRUCTION_ROOT_ENV` alignment. The owner immediately superseded a
  stop disposition with **“Push through failures.”** Exact frozen diff 04 bytes
  were restored to live candidate paths. Agent 0 rebuilt current runtime only
  inside ignored frontend dependencies; registered typecheck/build, host full
  Vitest (1,214 passed / 4 skipped), and focused affected tests (35/35) now pass
  without tracked root/App setup changes. Local premerge reached a READY Next
  service but returned HTTP 503 without shared runtime/project registration, so
  it remains PR-CI-owned. Preparation and local fan-in are complete pending
  Git/PR and PR-CI. Logout/login and capture remain unexecuted,
  DEL-09-04 stays IN_PROGRESS, and no proof, publication, lifecycle, release,
  signing, notarization, distribution, or reliance claim is made. See
  `_run_records/R12_LOGIN_SESSION_PROOF_PREPARATION_2026-08-21.md`.
- 2026-08-20 - PR #591 Desktop run `32410644968` / job `96560074456`
  passed the D-APP-97 packaged-service proof on `macos-15`. The packaged CLI
  installed a unique non-default job in the disposable account's canonical
  `~/Library/LaunchAgents`; one bootstrap relied on `RunAtLoad` without
  `kickstart`; automatic launch, exact loaded argv and executable identity,
  complete process/job/plist/runtime cleanup, and default job/plist protection
  all passed in retained evidence. This materially narrows the login-time
  `RunAtLoad` Remaining item to actual login-session discovery/auto-start; it
  does not recreate a full logout/login session. `IN_PROGRESS`, lifecycle,
  Checking Approval SHA, owner-machine deployment act, and all release fences
  remain unchanged. See
  `_run_records/R11_DAPP97_RUNATLOAD_PR_CI_PROOF_2026-08-20.md`.
- 2026-08-20 - The coordinated DEL-09-06 fresh packaged-security proof passed
  for the exact unsigned arm64 app identity and closed DEL-09-04 REQ-009 /
  R4-P49 packaged-network evidence. Blocked renderer probes, five usable
  descendant TCP snapshots, zero non-allowlisted outbound, provider isolation,
  secret containment, and cleanup all passed. Only the named packaged-network
  Remaining item is removed; login-time `RunAtLoad` and the later owner-machine
  deployment act remain. State stays IN_PROGRESS; lifecycle, Checking Approval
  SHA, signing, notarization, distribution, publication, and release readiness
  remain unchanged.
- 2026-08-19 - PR #585 external proof accepted for the exact selected
  D-APP-97 packaged-SDK/R4-P49 engineering gap. Desktop run `32332985341` /
  job `96317050414` passed separate scripted no-live-provider verifier runs
  against the staged packaged app and the read-only `RUNNER_TEMP`-mounted DMG
  app; both retained summaries report `status: pass`, distinct bundle roots,
  and the same packaged executable identity. Harness run `32332985346` / job
  `96317050162` and governance run `32332985350` / job `96317050220` also
  passed. The packaged-SDK/DMG and release-quality premerge Remaining items
  are removed. Login-time `RunAtLoad`, packaged network-policy proof, and the
  later owner-machine deployment act remain. State stays IN_PROGRESS;
  lifecycle, Checking Approval SHA, signing, notarization, distribution,
  publication, and release-readiness posture are unchanged.
- 2026-08-19 - Pre-CI D-APP-97 packaged-SDK workflow integration added
  separate fail-closed scripted no-live-provider proofs for the staged app and
  read-only mounted DMG app, with both summaries retained in the unsigned CI
  artifact evidence. Local static and deterministic checks passed. Actual
  macOS staged/mounted execution and candidate-range G4 remain PR-CI-owned, so
  the packaged-SDK/R4-P49 Remaining item stays open; state remains IN_PROGRESS
  and lifecycle, Checking Approval SHA, signing, notarization, distribution,
  publication, and release-readiness posture are unchanged.
- 2026-08-19 - D-APP-100 landed as a bounded product-source node. The packaged
  daemon now prefers the registered manifest-resolved instruction root shared
  by app/CLI runtime requests and durably logs packaged-resources fallback only
  when registration/manifest resolution is unavailable. Agreement regression,
  unsigned packaged-under-isolation proof, full deterministic gates, and fresh
  independent review passed. The exact D-APP-100 Remaining item was removed;
  unrelated Remaining items, lifecycle, Checking Approval SHA, signing,
  notarization, distribution, and release-readiness posture are unchanged.
- 2026-08-17 - D-APP-95 accepted guarded recover-on-start as complete handling
  for a SIGKILLed daemon; the stale-socket residual was removed. D-APP-97
  opened the named unsigned release-preparation, `RunAtLoad`, packaged-SDK,
  DMG/dist, and premerge scope while preserving F-APP-2 and APP-HOLD-1. The
  owner-machine deploy remains a later owner act. D-APP-100 authorized the
  packaged-daemon instruction-root engineering node, which remains in
  Remaining until it lands. No engineering or product byte, lifecycle,
  Checking Approval SHA, release, signing, notarization, or distribution act
  occurred in this recording tranche.
- 2026-08-13 - Owner ruling disposed D-APP-93 with the landed PR #551 normalized trace evidence accepted as its complete and sufficient product; no further packet execution or lineage is required or authorized. D-APP-88 is concluded: the accepted engineering explanation is that no SIGTERM handler was bound in the shipped helper at the stop instant combined with the retired `before-quit` veto that swallowed SIGTERM. The held-connection `server.close()` stall hypothesis is neither confirmed nor refuted and is not a cause. PR #552's signal binder, bounded teardown, and held-connection regression are accepted as closing the failure mode under either variant. The helper-stop residual is removed from Remaining. DEL-09-04 stays IN_PROGRESS on its unrelated residuals; lifecycle and Checking Approval SHA are unchanged.
- 2026-08-13 - Runtime helper graceful-stop hardening prepared for review: a shared one-shot process-signal binder now drives the shipped daemon through the complete Electron teardown funnel, native `before-quit` remains vetoed until teardown completes, and the existing two-second grace/forced-transport close remains unchanged. A spawned-process regression arms a daemon-parsed complete-header/incomplete-body Unix-socket request, sends `SIGTERM`, and proves natural exit plus socket/owner cleanup in 2.146 s. Runtime tests passed 76/76; frontend tests passed 1113 with 6 skips; both typechecks and fresh code review passed. This is product implementation evidence only: DEL-09-04 remains IN_PROGRESS and no D-APP-93/D-APP-88 disposition, acceptance, closure, lifecycle, or Checking Approval SHA act is made.
- 2026-08-11 - The owner froze and executed the D-APP-93 owner-operated LLDB trace packet; Step 0 passed and the capture completed with zero stop rules. Landed evidence records SIGTERM delivered to `CrBrowserMain` in the AppKit event loop while two helper control-socket clients were live, with no Node/libuv/V8 signal-handler frames at the stop instant. LLDB intercepted the signal (`PASS=false`), so unintercepted processing was not tested. The helper remained alive after detach and continued serving. Evidence disposition and all D-APP-88 conclusion/remedy/acceptance acts remain reserved to the owner. DEL-09-04 remains IN_PROGRESS; lifecycle and Checking Approval SHA are unchanged.
- 2026-08-04 - D-APP-88 R3 accepted Root TM-ROOT-112 as fit to release the App rerun, reconstructed the exact source-aligned helper, and produced auditable authenticated post-GUI first-signal failure evidence: helper/GUI remained alive through 80 polls, socket/owner persisted, and App teardown/Root stop were not entered. An exact instrumented SINGLE/STANDARD matrix then passed all four credited first-signal arms identically, so `single-process` removal and every other App-native remedy remain unsupported; the instrumentation may perturb absolute timing and does not erase the earlier failure. Fresh verifier PASS accepted the calibrated blocker/handoff only. Product/config/test and local runtime/build residue were rolled back. DEL-09-04 remains IN_PROGRESS, D-APP-88 remains open, TM-APP-036 does not fire, and the next replay is held for owner-authorized interactive GUI-session native tracing plus a sealed uninstrumented command/timing transcript. Lifecycle and Checking Approval SHA are unchanged.
- 2026-08-03 - D-APP-88 R2 evaluated the previously untried separately built full Electron helper. The standalone `com.chirality.app.runtime-helper` package, builder-generated child topology, whole-bundle embedding, relocatability, and fresh graceful-stop evidence passed. Acceptance remains BLOCKED because retained post-GUI evidence proves helper restart, GUI contact, no later daemon shutdown entry, and eventual transport loss but does not independently bind the operator-observed first-signal survival/socket retention. The mandatory post-GUI first-signal graceful-stop proof therefore failed. A Root-side live-connection/server-close interaction is recorded only as an investigation hypothesis. Exact candidate bytes were frozen under the R2 run root and all R2 product/config/test changes were rolled back while preserving D-APP-89. State remains IN_PROGRESS; lifecycle and Checking Approval SHA are unchanged.
- 2026-08-03 - D-APP-88 Option B bounded implementation produced a distinct LoginItems helper candidate with relocatable relative framework links and helper-routed LaunchAgent/CLI paths. Package, focused tests, typecheck, dependency boundary, instruction-root integrity, fresh helper SIGTERM, CLI status, GUI coexistence, and SIGKILL recovery were evidenced. Acceptance remains BLOCKED because first-signal graceful teardown failed after GUI coexistence and an alternate SIGUSR2 diagnostic failed likewise. Exact candidate bytes were frozen under the run root and all D-APP-88 product/config/test changes were rolled back while preserving D-APP-89. State remains IN_PROGRESS; lifecycle and Checking Approval SHA are unchanged.
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
