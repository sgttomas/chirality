# P2 REPAIR_1 — timeout and census assertions

RUN_STATUS: SUCCESS — bounded repair and pure/default-skip validation; actual conformance unrun.
Parent: /root/conformance_manager. Agent: /root/conformance_manager/p2_process, ephemeral Agent2.
Model: OpenAI GPT-6; exact serving model ID unavailable. Role/nondelegation instruction-asserted, not mechanically enforced. No delegation.
WriteAuthorization: same exact test/helper and P2 evidence scope under original BRIEF/AMENDMENT_1 plus explicit parent REPAIR_1 dispatch. Only the test changed; helper bytes unchanged.
ToolPolicyCompliance: PASS. Reads, scoped Python writes, node syntax check, default-skip Vitest, shell syntax parsing, scoped diff check and parent messages only.

## Basis and result

Read fresh REVIEW_P2/REPORT.md SHA256 dc38926b4e0c5ec4268a1a6c2635dfec34e27d131ae8a0a3251882ab464fac33 and actual CodexTurnSession/DescendantTracker implementations. Prior P2 freeze/report/OUTPUTS, review package and historical failed supplier evidence remain unchanged. Accepted upstream authority remains OWNER_DIRECTION/SPEC_FAN_IN through ../../BASIS.json and original P2 brief. This is derivative repair evidence, not conformance acceptance or authority truth.

Timeout terminal rejection is now a bounded structured record. It is classified CONFIGURED_TURN_TIMEOUT only for an actual RuntimeError with ENGINE_UNAVAILABLE, status503, CODEX_PROTOCOL_FAILURE and the exact current message Codex turn timed out; unrelated errors classify OTHER_SESSION_FAILURE. The timeout profile requires that exact cause plus elapsed >= configured5000ms minus25ms timer/clock granularity and <=10000ms. Evidence includes configuredTurnTimeoutMs, actionStartedAt, terminalReceivedAt and timeoutObservedElapsedMs. Raw error bodies are no longer retained by this terminal path. Cancellation request timestamps are recorded only for actual cancel calls.

Every actual fixture reconciliation used for positive identity, pre-cleanup disappearance, pre-cleanup census, cleanup polling and final cleanup now rejects any snapshot.failure or LATEST_CENSUS_MAY_BE_STALE limitation. Failure snapshots with their exact phase are retained in censusFailures. Any such failure forces a failed verdict and cannot be cleared by superficially empty lists or a later recovery. Existing cleanup continues and retains its own failure accumulation; no PID signal authority or policy grant changed.

## Validation

Eight pure tests passed; actual supplier profile skipped. The two added controls reject unrelated errors, wrong timeout class/message and early/late elapsed values, and use the actual tracker with an injected failing census to demonstrate rejection of stale empty lists and retained-failure recovery. Helper node syntax and scoped whitespace checks pass. CHECKS.log records commands/results. No supplier ran and no child-owned active process remains.

## Parent contract and handoff

Use REPAIR_1/SOURCE_FREEZE.json for new source hashes. Parent invocation remains exactly ../REPORT.md's single-scenario command: normal, then cancel-primary, cancel-child, timeout-primary, timeout-child, each fresh evidence directory and separately verified supplier. New checks supplement, never replace, prior marker/source/supply/sentinel/lineage/timing/cleanup requirements.

Require censusFailures == [], no failure field or stale-census limitation in every lifecycle/cleanup snapshot used as proof, no failure/providerFailures/cleanupFailures, and exact pass verdict. Timeout runs additionally require terminal.error.cause == CONFIGURED_TURN_TIMEOUT, bounded RuntimeError/ENGINE_UNAVAILABLE identity, configuredTurnTimeoutMs ==5000 and timeoutObservedElapsedMs in[4975,10000], consistent with terminalReceivedAt-actionStartedAt. Retain sourceBefore==sourceAfter and supplierBefore/After exact identity.

Closure: repair ready for fresh independent backcheck and parent actual runs; supplier/conformance acceptance remains unperformed. publicRuntimeCancellationProven remains false: all four lifetime profiles use private actor cancellation/timeout. Full G-SBX, orphan proof, account owner-live, supplier acceptance, client/release/lifecycle and hold decisions remain separate. No production code, previous sealed evidence or governed state changed.

Outputs: INPUTS.json; test/helper .preimage.source and .postimage.source; SOURCE_FREEZE.json; CHECKS.log; RUN_RECORD.md; REPORT.md; OUTPUTS.json.
MISSING: fresh review and parent actual five-profile evidence.
NEEDS_HUMAN_RULING: none.
DEPENDENCY_NOTES: parent source-generation freeze and actual supplier execution; no cycle.
