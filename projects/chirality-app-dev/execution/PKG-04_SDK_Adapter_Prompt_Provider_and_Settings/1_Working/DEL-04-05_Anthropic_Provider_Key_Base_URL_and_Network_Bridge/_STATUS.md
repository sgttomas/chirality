# Status: DEL-04-05

**Current State:** IN_PROGRESS
**Last Updated:** 2026-09-03
**Authorization Basis:** D-APP-19 Option D ruling 2026-06-20; owner-approved SHA 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec recorded 2026-06-20
**Directive:** owner inspection-phase directive 2026-06-20
**Checking Approval SHA:** 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec

## Remaining

- **DEL-04-05-V3-01** (`SELECTABLE`) — typed safeStorage states at the App credential bridge.
  Trace: OUT-001, AC-001, VER-001; CLM requirements DEL-04-05-RQ-002/003/004/012; applied decomposition row L316 (preserve App credential entry/status and packaged-daemon `safeStorage` boundary participation without creating a second credential owner).
  Plan: WP-04/WP-08; AT-057 storage-state portion (`missing`, `storageUnavailable`, `decryptFailed`, `available`) and AT-011 safeStorage analogue; production signing and G-KEY release-lane claims excluded. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: Existing store-owned `ui | env | none` status (2026-08-20 repair); DEL-09-06-V3-01 shares the `frontend/electron/api-key-ipc.ts` write surface, so the two items are serialized or executed under one integration owner. No owner gate blocks preparation-identity work.
  Write locus: `frontend/electron/**` credential store/IPC, `frontend/src/**` bridge types and tests, and deliverable-local state; the daemon remains the runtime credential owner.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: Non-destructive corrupt-ciphertext and unavailable-store fixtures proving the four typed states without plaintext exposure or silent loss; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the typed states and fixtures land with review PASS.
- **DEL-04-05-V3-02** (`NOT_SELECTABLE_UNTIL: accepted Root/App account/consent contract and the K-NET-1 exact endpoint set routed to App (Root DEL-02-09/DEL-02-10)`) — carry the three per-root command-network postures and typed account/login-state transport through the App bridge.
  Trace: OUT-001, AC-001, VER-001; DEL-04-05-RQ-008/009/010/014; App `docs/CONTRACT.md` K-NET-1 and K-KEY-1.
  Plan: WP-04/WP-07; AT-020 and AT-044 App-boundary portions; AT-008 typed login-channel transport portion (only `verificationUrl`/`userCode` traverse the ephemeral channel); G3/G-WIRE for live claims. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: Root DEL-02-09 and DEL-02-10 accepted returns (routed notices); DEL-02-05-V3-03; DEL-09-06-V3-03. OAuth/device-code/keyring semantics and root-account transitions remain Root-owned; the bridge conforms and never becomes a second credential owner.
  Write locus: `frontend/electron/**`, `frontend/src/**` bridge and tests, and deliverable-local state.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: Conformance fixtures proving default-off command network, per-destination prompts with explicit-user-only `acceptForSession`, labelled `network_access = true`, and token-free typed login transport; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the bridge conformance lands with G-WIRE evidence.

## History
- 2026-09-03 - v3.0.0-rc.1 pathway seating (A12; App counterpart of Root R17): `ScopeOfWork.md` re-pinned to the applied decomposition at `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`; v3 Remaining items seeded (2, of which 1 SELECTABLE) with dependency, gate, write-locus, check, and return contracts; run evidence `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/`. No implementation, lifecycle, dependency-acceptance, release, or Root act; Current State, Checking Approval SHA, and lifecycle are unchanged.
- 2026-08-20 - Owner-authorized DEL-04-05-RQ-001 repair changed the Electron
  Anthropic environment fallback to UI safeStorage, then
  `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`, and exposed the
  store-owned non-secret `ui | env | none` status source needed by dependent
  DEL-02-05-R03; positive regression coverage, focused/full frontend gates,
  harness, APP-HOLD, secret/scope checks, and fresh Review 03 pass. Evidence:
  `Evidence_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20.md`. State remains
  IN_PROGRESS; Remaining stays empty; lifecycle and Checking Approval SHA are
  unchanged.
- 2026-07-22 - D-APP-72 authenticated literal-loopback oMLX validation, exact model discovery, isolated key handoff, and typed redacted failures completed without weakening the Anthropic path; fake-provider and live proofs pass. State remains IN_PROGRESS; lifecycle and Checking Approval SHA are unchanged.
- 2026-07-21 - SCA-APP-002 opened the bounded local-provider bridge item; state remains IN_PROGRESS.
- 2026-07-12 - D-APP-56 consolidated R5 decision application recorded; generic concordance Remaining retained for R6; state remains IN_PROGRESS.
- 2026-05-20 - State set to OPEN (PREPARATION)
- 2026-05-20 - State set to INITIALIZED (TASK+four-documents)
- 2026-05-23 - State set to SEMANTIC_READY (ORCHESTRATOR_PHASE_2_5_CLOSEOUT)
- 2026-06-16 - State set to IN_PROGRESS (HUMAN) [Human authority: active code implementation underway.]
- 2026-06-20 - State set to CHECKING (HUMAN)
- 2026-07-11 - State set to IN_PROGRESS (HUMAN) [Owner-ruled lifecycle rebaseline D-APP-54 2026-07-11: administrative correction superseding the D-APP-19 inspection-admission convention; prior approvals and history preserved (execution/_Coordination/_DECISIONS/D-APP-54_RULING_2026-07-11.md).]
- 2026-07-11 - Remaining item added: concordance bootstrap seeded at packet time per D-APP-55 packet; no state change.
- 2026-07-11 - Remaining item updated: concordance bootstrap gate flipped and pinned method revision 551f84ef6 substituted per the D-APP-55 ruling (Option A, whole corpus); no state change.
- 2026-07-12 - D-APP-56 R5 P40 applied UPD-069, UPD-079; generic concordance Remaining item retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - D-APP-56 R5 P44 assessment-pointer rider applied as a forward annotation; generic concordance Remaining retained for R6; state remains IN_PROGRESS.
- 2026-07-12 - R6 closeout completed the D-APP-55 concordance bootstrap and removed it from Remaining; surviving deliverable-local items retained; state remains IN_PROGRESS.
- 2026-07-18 - D-APP-65 disposition 2 accepted the RQ-011 criterion (three-of-four live basis from the D-APP-52 packs plus unit-level simulated assertions) and authorized this tranche; explicit category assertions for REQUEST_TIMEOUT, RATE_LIMITED, NETWORK_ERROR, and API_RESPONSE_ERROR added to harness-anthropic-agent-sdk-manager.test.ts. No state or lifecycle change.
