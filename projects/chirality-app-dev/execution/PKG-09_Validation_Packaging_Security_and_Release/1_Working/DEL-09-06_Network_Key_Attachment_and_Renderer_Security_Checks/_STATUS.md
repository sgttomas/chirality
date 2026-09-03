# Status: DEL-09-06

**Current State:** IN_PROGRESS
**Last Updated:** 2026-09-03
**Authorization Basis:** D-APP-19 Option D ruling 2026-06-20; owner-approved SHA 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec recorded 2026-06-20
**Directive:** owner inspection-phase directive 2026-06-20
**Checking Approval SHA:** 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec

## Remaining

- None for the selected D-APP-97 packaged-artifact network, key-attachment,
  and renderer-security scope. Deliverable lifecycle and dependency closure
  remain separate and unchanged; F-APP-2 continues to fence signing,
  notarization, distribution, and release authority.

- **DEL-09-06-V3-01** (`SELECTABLE`) — sender authorization on all six credential IPC handlers plus G-CSP renderer-hardening evidence.
  Trace: OUT-001 (renderer network allowlisting; API key storage checks), AC-001, VER-001; DEL-09-06-REQ-002/003/005/006/014/015; applied decomposition row L369 (verify renderer allowlist, API key redaction/storage, endpoint policy, and no unauthorized expansion).
  Plan: WP-07/WP-09; G-CSP (App security review); AT-033 and AT-057 sender-check portions. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: The six handlers registered at `frontend/electron/api-key-ipc.ts:110-176` adopt the `isAuthorizedSender` policy embodied by `frontend/electron/runtime-control-ipc.ts:85-95`; shared write surface with DEL-04-05-V3-01 (serialize or one integration owner); DEP-09-06-011. No owner gate blocks this App-only work.
  Write locus: `frontend/electron/api-key-ipc.ts`, `frontend/electron/**` window/CSP policy, packaged security tests, `Evidence/**`, and deliverable-local state.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched; packaged security probes run under the AGENTS.md host-capability escalation rule.
  Return: Unit and packaged tests proving every credential channel rejects unauthorized senders, plus CSP effectiveness, window-open denial, navigation constraint, explicit context isolation/sandbox, and per-window bounded egress, each with exact artifact/source identities; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the sender checks and G-CSP evidence land with review PASS.
- **DEL-09-06-V3-02** (`NOT_SELECTABLE_UNTIL: accepted Root/App account/consent contract and the K-NET-1 exact endpoint set routed to App (Root DEL-02-09/DEL-02-10)`) — verify typed account states, command-network consent postures, and App Server endpoint policy through the App boundary.
  Trace: OUT-001, AC-001, VER-001; DEL-09-06-REQ-004/005/007; applied decomposition row L369 (current provider endpoint policy; no unauthorized provider/network expansion).
  Plan: WP-04/WP-10; AT-020 App-boundary portion; G-KEY/G-WIRE; F-APP-1 remains a hard fence (no provider expansion beyond the accepted endpoint set). Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: Root DEL-02-09/DEL-02-10 accepted returns (routed notices); DEL-04-05-V3-02; DEL-02-05-V3-03.
  Write locus: Security tests and evidence under `frontend/**` plus deliverable-local state.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: Network guard and posture evidence proving denial of every unexpected `networkApprovalContext` request and restriction to the governed endpoint set; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the boundary verification lands with G-WIRE evidence.
- **DEL-09-06-V3-03** (`NOT_SELECTABLE_UNTIL: DEL-09-05-V3-04 authorized (owner host act) and DEL-04-05-V3-01 landed`) — preparation credential-transition drill evidence and evidence scanning for new field families.
  Trace: OUT-001, AC-001, VER-001; DEL-09-06-REQ-002/003/015.
  Plan: WP-09/WP-10; AT-051/AT-057 preparation portions; AT-025 App evidence-scan portion; G-KEY release lane excluded. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: DEL-09-05-V3-04; DEL-04-05-V3-01; DEL-05-03-V3-01 for field families.
  Write locus: Security evidence under `frontend/**` and deliverable-local state.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: Drill and scan evidence with synthetic secrets absent from every sink; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the drill and scan evidence land.

## History
- 2026-09-03 - v3.0.0-rc.1 pathway seating (A12; App counterpart of Root R17): `ScopeOfWork.md` re-pinned to the applied decomposition at `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`; v3 Remaining items seeded (3, of which 1 SELECTABLE) with dependency, gate, write-locus, check, and return contracts; run evidence `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/`. No implementation, lifecycle, dependency-acceptance, release, or Root act; Current State, Checking Approval SHA, and lifecycle are unchanged.
- 2026-08-20 - Fresh unsigned arm64 packaging and the fail-closed packaged
  security proof passed against the accepted N1/N2 API-key precedence bytes.
  Compact evidence records exact artifact/source identities, UI/canonical-env/
  compatibility-env precedence, safeStorage encryption/status/removal,
  provider isolation, blocked renderer probes, five usable descendant TCP
  snapshots with zero non-allowlisted outbound, confirmed cleanup, and a
  5,868-file secret scan with zero blocked findings. The exact D-APP-97
  packaged-security Remaining item is removed. State stays IN_PROGRESS;
  Checking Approval SHA, dependencies, F-APP-2, and all release fences remain
  unchanged.
- 2026-08-17 - D-APP-97 converted DEL-09-06's D-APP-56-deferred R4-P49 claim
  family into open unsigned local/CI-only release-preparation engineering over
  the packaged artifact. No product/security byte, lifecycle, Checking
  Approval SHA, release, signing, notarization, or distribution act occurred
  in this recording tranche.
- 2026-08-01 - SCA-APP-007 migrated 38 byte-identical historical network-policy proof files from the retired physical DEL-03-06 container into `Evidence/Historical_DEL-03-06/`, with a durable old/new path and SHA-256 provenance manifest. This is an evidence-routing correction only. State remains IN_PROGRESS; Remaining items, authorization basis, lifecycle, approval state, and Checking Approval SHA are unchanged.
- 2026-07-22 - D-APP-72 authenticated `127.0.0.1` oMLX, redirect/credential rejection, provider-key isolation, redaction, and renderer-egress proofs completed. The unrelated D-APP-56 release-preparation item remains open. State remains IN_PROGRESS; lifecycle and Checking Approval SHA are unchanged.
- 2026-07-21 - SCA-APP-002 added bounded oMLX network/key security proof to Remaining; release fence and state remain unchanged.
- 2026-05-20 - State set to INITIALIZED (TASK+four-documents; P1/P2 complete with all four documents non-empty)
- 2026-05-20 - State set to OPEN (PREPARATION)
- 2026-05-23 - State set to SEMANTIC_READY (ORCHESTRATOR_PHASE_2_5_CLOSEOUT)
- 2026-06-16 - State set to IN_PROGRESS (HUMAN) [Human authority: active code implementation underway.]
- 2026-06-20 - State set to CHECKING (HUMAN)
- 2026-07-11 - State set to IN_PROGRESS (HUMAN) [Owner-ruled lifecycle rebaseline D-APP-54 2026-07-11: administrative correction superseding the D-APP-19 inspection-admission convention; prior approvals and history preserved (execution/_Coordination/_DECISIONS/D-APP-54_RULING_2026-07-11.md).]
- 2026-07-11 - Remaining item added: concordance bootstrap seeded at packet time per D-APP-55 packet; no state change.
- 2026-07-11 - Remaining item updated: concordance bootstrap gate flipped and pinned method revision 551f84ef6 substituted per the D-APP-55 ruling (Option A, whole corpus); no state change.
- 2026-07-12 - D-APP-56 R5 P40 applied UPD-075, UPD-078; generic concordance Remaining item retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - R6 closeout completed the D-APP-55 concordance bootstrap and removed it from Remaining; surviving deliverable-local items retained; state remains IN_PROGRESS.
