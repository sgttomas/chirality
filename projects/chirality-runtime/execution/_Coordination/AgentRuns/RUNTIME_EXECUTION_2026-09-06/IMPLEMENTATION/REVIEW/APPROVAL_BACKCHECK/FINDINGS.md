# Approval/native posture independent findings

Current verdict: CHANGES_REQUIRED. Findings are source/controlled evidence, not an empirical supplier enforcement verdict. Parent notified as each finding was established.

## A1 — missing managed network proxy activation (P1)

Baseline native compiler sets named profile network.enabled=true for ask/on and domain proxy settings, but omits features.network_proxy. Exact source commit758ef40 core/config/permissions.rs:120–130 explicitly resets proxy config.enabled=false and states that a named network table does not start the proxy; lines515–517 map profile enabled=true to enabled sandbox networking. Exact features/src/lib.rs:1096–1104 declares network_proxy default false; core/config/mod.rs:3555–3563 enables the proxy only when the feature is enabled and profile networking is enabled. Therefore on-request plus the baseline profile does not establish ask-before-network; source semantics permit network without the intended proxy. Fix compiler and effective readback to explicitly enable/attest the feature and prevent feature configuration from overriding the pinned proxy table. No actual network bypass was executed; the exact source contradiction is sufficient to reject this candidate mapping.

Captured official source16 hashes were verified against PROVIDER_INTEGRATION/SOURCE_PINS.json. Three supplementary source files were captured byte-for-byte with git show at exact commit758ef40 from the existing supplier study checkout; hashes and compressed bytes are in EXACT_SOURCE_PINS.json and local .gz files. No candidate patch or vendor execution was performed.

## A2 — sent:true precedes transport write result (P2)

Baseline CodexTurnSession.replyNetworkApproval calls its synchronous write helper and immediately returns sent:true. The Writable callback may fail asynchronously; the helper then fails/closes the actor, but the successful receipt has already escaped and the broker may report applied:true. This contradicts the stated successful-transport-write meaning (independent of any provider execution acknowledgement). transport-failure-repro.test.ts.source reproduces a synthetic broken-pipe callback after sent:true; actor then closes and turn rejects. Reproduction passed. Repair must await successful bounded write completion and reserve the decision while the write is in flight so it cannot be sent twice.

## A3 — reusable coordinator does not enforce its one-child/returned-child contract (P2)

The child-presence guard precedes awaited residency lookup and session creation. Two concurrent delegate hooks both pass, create and run two children; the final run record retains only the second and reports completed. concurrent-delegation-repro.test.ts.source reproduces this using the actual coordinator with controlled ports and storage. Separately, review checks only child identity, and the final completion condition checks only child/review presence. A manager port can catch a failed child and review that child, causing a completed manager record with child.status=failed and no completed return. failed-child-review-repro.test.ts.source reproduces that case.

The built-in Codex mailbox serializes callbacks and propagates callback failures, masking these cases through that particular port. They remain real defects at the reusable coordinator's allowed manager-port boundary. Reserve one delegation synchronously before awaiting; require an actual completed child return before review/completion, and preserve explicit single-review semantics. Do not rely on an individual port to enforce the coordinator contract.

## Positive checks and exclusions

Governed Pi no-fallback guards pass independently for each parentSessionId, childKind and orchestrationRunId marker, both at preflight and startTurn before any SDK/provider request. Releasing a valid binding and removing its marker still cannot reopen a broad read fallback. Three added marker checks plus21 actual-SDK tests passed; the concurrent-delegation reproduction also passed in that run (25 total). Actor broken-pipe reproduction and failed-child review reproduction each passed separately. A passing reproduction demonstrates a defect, not correct behavior.

Historical reproduction/extra check sources end .test.ts.source to avoid auto-discovery. Parent is repairing A1/A2 and has received A3. New conformance admission/helper changes remain excluded pending coherent transfer. Exact-supply approval/grouping/kernel enforcement, account use, release, and owner acts are not established by this review.
