# Fresh P2 review — findings and limited diagnostic admission

RUN_STATUS: SUCCESS (review complete; two conformance assertion findings)
ControlSurface: MERGED
TaskProfile: NONE
TaskSkill: NONE
ScopePath: /Users/ryan/.codex/worktrees/341e/chirality/projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_CONFORMANCE_RESUME_2026-09-06/IMPLEMENTATION/REVIEW_P2
ToolsUsed: zsh read commands; python3 evidence/hash generation; node --check; node_modules/.bin/vitest with actual profile disabled; /bin/sh -n through pure tests.
ToolPolicyCompliance: PASS
WriteAuthorization: ALLOWED_WRITE_TARGETS — REVIEW_P2 only.
Attribution: OpenAI GPT-6; exact serving model ID unavailable. Fresh ephemeral native Agent2 role and nondelegation are instruction-asserted, not mechanically enforced. No delegation and no source edits.

## Findings

1. **P2 — timeout profiles accept unrelated session failure as timeout proof.** `tests/exact-process-conformance.test.ts:165` converts every rejected waitTurn to an error string; line 194 checks only existence of `error`. In `packages/daemon/src/codex-session.ts:451` the configured turn timer fails with `Codex turn timed out`, but transport/protocol failure also rejects waitTurn and triggers host close. If such a failure arrives after PROCESS_READY, disappearance, null finished marker and the current upper time bound can all pass. Require a positively identified configured timeout cause (at minimum the precise current timeout result), preserve bounded structured cause, and assert elapsed timing consistent with the configured timer. A separate control must reject an unrelated post-ready session failure. Do not treat current timeout-primary/timeout-child verdicts alone as timeout proof.

2. **P2 — census failure is not excluded from successful disappearance/cleanup.** `tests/exact-process-conformance.test.ts:185-197` uses reconcile snapshots for owned identity/disappearance and lines 248-253 accept empty group/detached lists at cleanup without checking snapshot.failure. `packages/core/src/descendant-tracker.ts:94-109` deliberately catches census failure and returns last census plus failure and LATEST_CENSUS_MAY_BE_STALE. A prior empty/stale observation may therefore satisfy the predicate even when the current census failed; a recovered census also retains failure in this implementation. Require failure absent at every snapshot relied on for positive lineage/disappearance/cleanup claims, persist any failure as profile failure, and test a failed census with superficially empty lists. Preserve tracker limitations and no arbitrary signal authority. This blocks positive lifecycle/process closure claims until repaired or explicitly rejected by independent parent evidence review.

## Mechanics reviewed

The new probe emits newline-delimited standalone markers, per-role host files, nested foreground-shell evidence, signal-attempt and actual nonzero signal-status plus denial markers. The normal host test requires both standalone output and matching host files; echoed rejected commands alone cannot pass. Sibling PID input is fixed/validated; host positive signal control precedes execution and identity/liveness plus another positive control follow it. Protected synthetic host sentinel hash is unchanged. Earliest provider-return observation is de-duplicated by issued callId and records explicit null for interrupted calls. This is first provider-observed return timing, not direct shell output emission timing.

Normal checks exactly one probe for primary and child and complete host evidence. Each lifetime profile checks selected role's ready/PID, foreground/signal prefix, no finished file, independently observed lineage, interruption/error terminal and disappearance before fixture cleanup. Four lifetime scenarios remain private actor tests; publicRuntimeCancellationProven is false. Bounds are <=10 seconds for returned calls and lifetime ready/terminal/action, <=60 seconds profile. These bounds are asserted after operations; test/watchdog/transport bounds still determine failure-run termination. Cleanup signals only the fixture-owned spawned host process group and spawned sibling; observed census PIDs are never signaled. Natural sleep is seven seconds.

Catch/finally persist original bounded failure name/code/phase and accumulate individual cleanup failures, allowing later cleanup and evidence writing. Setup before the try and evidence-write filesystem failure are not covered by durable process-conformance.json; parent output.log remains necessary for those failure paths. Raw supplier stderr is intentionally discarded. Failed profile can retain PROFILE_NOT_COMPLETED plus failure rather than explicit PROFILE_FAILED; parent must require exact pass verdict and no failure. This review does not promote either limitation to a new acceptance claim.

## Basis and validation

Consumed manager PLAN.md/BASIS.json, sealed P2 BRIEF.md/AMENDMENT_1.json, report/check/freeze/output manifest, live source and referenced session/tracker source, actual predecessor PROCESS_NORMAL_1 JSON/output and FOLLOWON_01 checkpoint. Accepted upstream remains OWNER_DIRECTION/SPEC_FAN_IN indexed by BASIS.json. This review is a derivative package, not decomposition truth or accepted conformance.

The prior actual normal attempt was source-stable but failed concatenated output assertion after shell selector denial diagnostics; elapsed 3673ms, sibling count1, empty ownedGroup/detached after cleanup. Its failed status and bytes remain unchanged; historical PID supplies no current authority. Current source test SHA256 aaaebc5e663f4b1708cc27669b2980593858f069e091a5c1ec797a5cf014513e; helper SHA256 57e3c4e09183a0cebe825ca41fb5892f3a8836c635227d27aa1d7ce526e87a81. All six source hashes match before/after and all P2 output-package hashes verified.

Independent default-skip run: six pure tests passed, actual supplier profile skipped. Helper syntax check exit0. No actual supplier, valid provider listener, oMLX, account, signal probe or network canary executed. CHECKS.log and source manifests are durable evidence.

## Admission and handoff

Bounded **normal diagnostic execution is admitted** against these exact frozen bytes by the parent, with exact supplier/source identity and fresh evidence directory. This is readiness to collect evidence, not profile acceptance. Parent must independently reject failure-bearing census snapshots and any failure/providerFailures/cleanupFailures, require host markers/sentinel and sibling controls, stable inputs/supply, <=60 seconds and empty trustworthy cleanup lists. Cancel profiles require the same trustworthy census checks. **Timeout proof is not admitted from the current assertion alone.** Repair both findings, freeze new bytes, rerun focused checks and request fresh limited review before claiming positive lifecycle coverage. Prior frozen evidence must remain unchanged.

Closure: independent review complete with findings; implementation/conformance closure remains open. No governed state, supplier acceptance, public cancellation, full G-SBX, client acceptance, release or hold changed. No child-owned process remains and no cleanup ownership transfers.

Outputs: REPORT.md; SOURCE_BEFORE.json; SOURCE_AFTER.json; INPUT_PACKAGE_VERIFICATION.json; CHECKS.log; OUTPUTS.json; local run record.
MISSING: repaired assertions and parent actual source-pinned five-scenario evidence.
NEEDS_HUMAN_RULING: none for scoped repair/diagnostic work.
DEPENDENCY_NOTES: author repair then fresh source freeze and parent execution; no cycle.
