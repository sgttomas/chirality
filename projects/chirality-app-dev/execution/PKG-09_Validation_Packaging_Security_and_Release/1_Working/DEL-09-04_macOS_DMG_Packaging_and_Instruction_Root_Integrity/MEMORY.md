# MEMORY - DEL-09-04

- 2026-08-21 — The owner-authorized PREPARE-THEN-OWNER tranche produced a
  reviewed two-phase actual-login proof candidate and minimal future procedure,
  recorded in `_run_records/R12_LOGIN_SESSION_PROOF_PREPARATION_2026-08-21.md`.
  Focused tests passed 15/15 and final fresh review passed with zero findings;
  integrated gates exposed the external `RUNTIME_INSTRUCTION_ROOT_ENV`
  alignment. The owner immediately superseded a stop with **“Push through
  failures.”** Exact frozen diff 04 bytes are restored to live candidate paths.
  Agent 0 rebuilt current runtime only under ignored frontend dependencies;
  registered typecheck/build, host full Vitest (1,214 passed / 4 skipped), and
  focused affected tests (35/35) now pass without tracked setup changes.
  Local premerge reached a READY Next service but returned HTTP 503 without the
  shared runtime/project registration lifecycle; it remains PR-CI-owned.
  Fresh integrated review found only three record defects; amendment 10 fixed
  them and the direct backcheck passed with zero actionable findings and
  unchanged product hashes. Preparation and local fan-in are complete pending
  Git/PR and PR-CI. The host proof remains unexecuted, state remains
  IN_PROGRESS, and all
  publication/release/lifecycle fences are unchanged.
- 2026-08-20 — PR #591 Desktop run `32410644968` / job `96560074456`
  materially narrowed the login-time `RunAtLoad` gap. Retained artifact
  `chirality-packaged-launchagent-runatload-proof` reports PASS for automatic
  bootstrap-triggered launch from the disposable account's canonical
  `~/Library/LaunchAgents`, exact loaded argv and packaged executable identity,
  complete process/job/plist/runtime cleanup, and unchanged default targets.
  The proof invokes bootstrap directly and does not recreate login-session
  discovery through a full logout/login. DEL-09-04 remains IN_PROGRESS on that
  host-capability residual and the later owner-machine deployment act;
  lifecycle, Checking Approval SHA, signing, notarization, distribution,
  publication, release, and reliance posture are unchanged.
- 2026-08-20 — The coordinated DEL-09-06 host proof closed DEL-09-04's
  selected REQ-009 / R4-P49 packaged-network residual against a fresh unsigned
  arm64 app and DMG. Compact D-APP-99 evidence identity-binds the packaged
  subject and records blocked renderer probes, five usable descendant TCP
  snapshots with zero non-allowlisted outbound, provider isolation, secret
  containment, and confirmed cleanup. Login-time `RunAtLoad` and the later
  owner-machine deployment act remain open. DEL-09-04 stays IN_PROGRESS;
  lifecycle, Checking Approval SHA, signing, notarization, distribution,
  publication, and release readiness remain unchanged.
- 2026-08-19 — PR #585 closed the selected D-APP-97 packaged-SDK/DMG proof
  gap on exact source revision
  `3a02eeedeb3561748d96b10f57a1aa7f5546eeb5`. Desktop run
  `32332985341` / job `96317050414` executed the unchanged scripted
  no-live-provider verifier successfully against both the staged packaged app
  and the app mounted read-only from the unsigned DMG under `RUNNER_TEMP`.
  Their separate summaries report `status: pass`,
  `proofMode: scripted-no-live-provider`, distinct bundle roots, and matching
  executable SHA-256
  `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`.
  The aggregate unsigned-artifact summary also passed and identity-bound the
  mounted app to the staged app; Harness run `32332985346` / job
  `96317050162` and governance run `32332985350` / job `96317050220` passed.
  This closes only the selected packaged-SDK/DMG and premerge evidence gap.
  The packaged network-policy proof, login-time `RunAtLoad`, and later
  owner-machine LaunchAgent deployment remain open. DEL-09-04 stays
  IN_PROGRESS; lifecycle, Checking Approval SHA, signing, notarization,
  distribution, publication, and release-readiness posture are unchanged.
- 2026-08-19 — Pre-CI D-APP-97 packaged-SDK workflow integration now invokes
  the existing scripted no-live-provider verifier against both the staged app
  resources and the read-only mounted DMG app resources. The two distinct
  summaries are fail-closed on `status: pass` and
  `proofMode: scripted-no-live-provider` and are retained under the unsigned
  artifact evidence tree. Focused tests, typecheck, full Vitest, YAML/Bash
  static validation, G4 schema validation, APP-HOLD integrity, practitioner
  checks, receipt validation, and corpus status passed locally. The actual
  staged/mounted proof and candidate-range G4 check remain PR-CI-owned;
  DEL-09-04 stays IN_PROGRESS and the R4-P49 Remaining scope stays open.
- 2026-08-19 — D-APP-100 implementation passed fresh independent review and an
  unsigned packaged-under-isolation run. The packaged daemon now resolves the
  registered manifest instruction root before falling back to packaged
  resources; fallback is durable and classified. The proving app, `app.asar`,
  and bundled CLI were identity-bound, and app/CLI/daemon agreed on the root.
  The exact D-APP-100 residual closed without changing lifecycle, Checking
  Approval SHA, signing/notarization/distribution, or release readiness.
- 2026-07-12 — D-APP-56 consolidated R5 decision application recorded for DEL-09-04; governed kit wording/ruling state updated without lifecycle transition. Original D-APP-55 run evidence remains immutable.
- 2026-08-03 — D-APP-88 Option B remains BLOCKED, not accepted closure. Attempt 1 proved relocatable copied-main package mechanics but failed post-GUI graceful teardown; its exact evidence remains at `execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_2026-08-02/`. R2 then evaluated the separately built full Electron helper: distinct bundle identity/UI posture, builder-generated child topology, whole-bundle embedding, relocatability, and fresh graceful-stop evidence passed. Retained post-GUI evidence proves helper restart, GUI contact, no later daemon shutdown entry, and eventual transport loss; first-signal survival/socket retention is an operator observation without a preserved command/process/socket snapshot. The mandatory proof therefore failed. An active-client interaction with Root `RuntimeDaemon.stop()` is only an investigation hypothesis, not a finding or authorized Root change. R2 candidate bytes were frozen and all R2 product/config/test changes rolled back while preserving D-APP-89. Evidence: `execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/`.
- 2026-08-04 — D-APP-88 R3 remains `BLOCKED / CONFIRMED_BLOCKER`, not implementation acceptance. Accepted Root TM-ROOT-112 bytes released the rerun. The exact uninstrumented helper then failed the mandatory authenticated post-GUI first SIGTERM with full process/socket/owner evidence and no App teardown or Root-stop entry. An exact instrumented SINGLE/STANDARD matrix passed all four credited arms identically; this excludes `single-process` removal as a supported cause/remedy but does not erase the uninstrumented failure because synchronous callback logging may perturb timing. Fresh verifier SHA-256 `ef3e26b61965adbf2e0c3e39710f6a099286c1173eb7be6207fcfe2b3ef9605c` accepted the calibrated blocker and exact handoff: another causal replay requires owner-authorized interactive GUI-session native signal tracing plus a sealed uninstrumented launch/contact/timing transcript. All candidate/generated/runtime residue was removed, D-APP-89 remains the product baseline, DEL-09-04 remains IN_PROGRESS, D-APP-88 remains open, and TM-APP-036 does not fire. Evidence: `execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_RESUME_R3_2026-08-04/`.
- 2026-08-11 — The owner froze and executed D-APP-93 at aggregate packet SHA-256 `db704c969143dad9ddfe832fa630748e091cb8a9b1524bb3d30d28dc74c56f83`. Step 0 passed and the trace completed with zero stop rules. Under two live helper control-socket connections, SIGTERM landed on `CrBrowserMain` in `mach_msg2_trap` under the AppKit event loop; no Node/libuv/V8 signal-handler frames appeared. LLDB used `PASS=false`, so unintercepted processing was not tested; the helper remained alive after detach and continued serving. Exact evidence: `execution/_Coordination/AgentRuns/APPDEV_DAPP93_OWNER_TRACE_2026-08-11/`. No D-APP-88 conclusion/remedy/acceptance, DEL-09-04 closure/lifecycle, or evidence disposition is inferred; all remain reserved to the owner.
- 2026-08-13 — Runtime graceful-stop hardening prepared as product code: the existing bounded `RuntimeDaemon.stop()` transport close is now reached through a reusable one-shot process-signal binder in shipped daemon mode, and an Electron shutdown policy prevents native `before-quit` from bypassing in-flight teardown. The regression uses a real child process, daemon-parsed partial HTTP body, OS `SIGTERM`, natural code-0 exit, and socket/owner cleanup (2.146 s). Full runtime/frontend tests, both typechecks, and fresh review passed. This does not dispose, close, or accept D-APP-93 or D-APP-88 and makes no DEL-09-04 lifecycle act.
- 2026-08-13 — Owner ruling disposed D-APP-93: PR #551's landed normalized owner-trace evidence is accepted as complete and sufficient, and no further packet execution or lineage is required or authorized. D-APP-88 is concluded on the accepted finding that no SIGTERM handler was bound in the shipped helper at the stop instant combined with the retired `before-quit` veto that swallowed SIGTERM. The held-connection `server.close()` stall hypothesis is neither confirmed nor refuted and is not a cause. PR #552's signal binder, bounded teardown, and held-connection regression are accepted as closing the failure mode under either variant. DEL-09-04 remains IN_PROGRESS on unrelated residuals; evidence and packet bytes remain unchanged.

## Decisions And Evidence

- 2026-06-16 - Human project authority advanced this deliverable lifecycle from SEMANTIC_READY to IN_PROGRESS because active code implementation is underway. This does not imply CHECKING, ISSUED, release readiness, dependency satisfaction, professional approval, certification, sealing, authentication, or code-compliance acceptance.
- 2026-06-21 - ADQ-15 refreshed macOS packaging and instruction-root evidence with `npm run desktop:dist`, build-directory and mounted-DMG instruction-root integrity checks, and build-directory and mounted-DMG scripted no-live packaged Agent SDK subprocess proofs. Evidence is recorded in `Evidence_ADQ-15_Packaging_Instruction_Root_Refresh.md`. The generated `frontend/dist/` and `frontend/artifacts/` outputs are ignored evidence artifacts and are not project truth. No signing, notarization, publication, external distribution, lifecycle issuance, professional approval, certification, sealing, authentication, code-compliance acceptance, or release-readiness claim changed.
- 2026-07-12 - D-APP-56 R5 P40 executed UPD-075, UPD-078: REF-006 current-state kit/register wording now agrees with D-APP-38 MATCH; dated source-warning and assessment history is preserved. No lifecycle transition.
- 2026-07-12 - D-APP-56 consolidated decision-application tranche recorded the applicable ruled ownership, mapping, gate-reaffirmation, or dated-deferral result for DEL-09-04; proposal-only source rows were not treated as human rulings, no unruled work was executed, and no lifecycle transition occurred.
