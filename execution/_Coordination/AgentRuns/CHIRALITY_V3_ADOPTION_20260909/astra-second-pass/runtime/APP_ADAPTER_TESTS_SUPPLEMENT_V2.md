# App adapter tests custody supplement V2 — successor

Verdict: **PASS. R2-8 is closed; no unresolved findings in this bounded successor review.** This report supersedes the pre-repair FAIL in APP_ADAPTER_TESTS_SUPPLEMENT_V1.md for the exact corrected subject. V1 remains unchanged. Together with terminal V4 and the engine-contract custody supplement, this restores the reviewed Section3 successor/context conclusion on the complete bound source.

Reviewer: `/root/astra_runtime_second_pass`, TASK; dispatched model `gpt-6-astra`, reasoning effort `high` (dispatch identification, not independent supplier attestation). Base: `c16812685831a1cae3d44bf478d08b033c605c3a`. No product edits, staging, commit, broad test rerun, native build, live provider request or supplier qualification.

## Exact subject and custody

Manager SOURCE_FREEZE_V6.json SHA-256: `559b0166c5488e8309481ac1f2f46c7270ae7b4415aede9748859ae66a68cc8e`. All48 members plus both shared fixtures matched before testing. The two formerly omitted tests and new integration test are now included.

Reviewer `app-adapter-tests-supplement-v2/SOURCE_MANIFEST.json` SHA-256: `1b6fd5ad1cbea8797233a1ef6cd0746552f4ed2fb0a79d14f7581438249a2d56`. It binds61 source/test/fixture files, including the earlier57, engine.ts and three additional adapter tests. Exact copies are preserved under its source/ directory; AFTER_TEST_CHECK.json confirms61/61 unchanged after executable checks.

Author seven-path aggregate SHA-256: `76c34bf6d6bd3f9322f1c3fa0ab6449ea61cb9cc4ff64af7093b79c6a8fbb123`, preserved as AUTHOR_HASHES.txt.

| Corrected/reviewed App member | SHA-256 |
|---|---|
| src/lib/harness/claude-agent-sdk-manager.ts | b8cbf8cc066e090d6f6b16c14ba5e33c18a54e06a0329d1f23e6873d9ef38af4 |
| src/lib/harness/anthropic-agent-sdk-manager.ts | 972d1c667ecafc17232e3979df507c81e398ead9305205bfb3efb9a4ceabd893 |
| src/lib/harness/pi-agent-engine-adapter.ts | e44cf3c3e55a0fed01ce9c9ad7faad67b903def2d4d4d10b87c333c87d7ad90b |
| src/__tests__/integration/runtime-successor-adapters.integration.test.ts | 462e2ad1ae543c22aa64d82ee14e02d9889478225365311287eca21796fa6178 |
| src/__tests__/lib/claude-agent-sdk-manager.test.ts | 4cea167779d0cbfb63008afa46a65a033ad3770cb64d319e1f7c7d8f51a502b9 |
| src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts | 76c8ea537f6a6762e9261b29a07c0cf09ff6cbe1aef9b58586097da67ba9b633 |
| src/__tests__/lib/pi-agent-engine-adapter.test.ts | b005dfa5bea816777865f61cdb1b13822596e7981b6a9b306bfb5951a14b220d |

The two omitted test postimages are unchanged from the exact V1 subjects. Their base and full-index diff hashes remain respectively:

- Claude base `8ca8b5ab9858f6753986b0a84cb4b062e0c97152d525cddf85e3528fcff50956`; diff `f95d64cd3e995b77613e52ed51766b0182481d82c0366dc68034dba4e97bde0d`.
- Anthropic base `be381ea61b66f36e56afc68845a309d696ffc96a31006bb24bf9cd74c8a6bb34`; diff `d8bca27812051bfd7294d65325d9076fb6d91407b91c054eb291176f4bb43ba9`.

V1 preserved their exact base/current/diff bytes. This successor rechecks their postimages and supplies newly executed durable evidence at those hashes, closing the prior execution-custody gap.

## R2-8 closure and actual dataflow

All three production App preparers now return `targetReference = toBasisPreview.id + ':' + toBasisPreview.sha256`: Claude at line139, Anthropic at line699, Pi at line733. The remainder of each preparation payload and continuation hashing remains intact. The production Electron wrapper and LegacyAgentEngineAdapter still forward the actual preparation without transformation. RuntimeMethodService:225 retains its exact target-reference, target-basis, predecessor and continuation-hash checks; resolveForTurn:133 retains the fresh target comparison. The repair changes the producer contract, not the admission guard.

The new integration test creates an actual RuntimeService, ProjectRegistry, SessionStore and TurnCoordinator, initializes an accepted predecessor using controlled preflight/startTurn, and replaces a selected method using the actual production preparer. For Claude it binds ClaudeAgentSdkManager.prepareContextSuccessor; for Anthropic it goes through the actual LegacyAgentEngineAdapter forwarding path to AnthropicAgentSdkManager. Real Runtime replacement now accepts and records the preparation. This is the seam that the former direct tests skipped.

Pi advertises durableResume=false. Runtime therefore does not invoke successor preparation for its current non-resuming lifecycle; the test does not artificially enable resume. It verifies that the callable Pi preparation contract is canonical directly. The pre-repair report's impact must be read with this calibration: the active Runtime failure affected the durable Claude and Anthropic paths; Pi's old string was a contract-parity issue, not evidence that current Runtime Pi replacement invoked and failed that guard.

The pre-existing direct manager tests still establish resume omission/fresh local identity, subsequent preference for committed engine identity over stale legacy fields, supplied system-context versus user-attachment separation, bootstrap lifecycle behavior, and Anthropic's explicit rejection of unsupported Runtime tools. Their scope limits described in V1 remain: mocked suppliers, synthetic hashes/context, partial forwarding assertions and no provider-native qualification. The new integration test covers preparation admission; it uses controlled provider turns and is not a complete live successor lifecycle test. Previously retained lifecycle/permission evidence supplies the other source-level checks without expanding their claims.

## Independent verification

- **118/118 passed across four files**, including both exact formerly omitted manager tests, Pi adapter tests and the new Runtime successor integration tests. Evidence: FOCUSED_TESTS.log. The reviewer configuration explicitly aliases `@chirality/runtime-core` to current source, avoiding reliance on a stale compiled core package. Execution used one worker and no file parallelism.
- **2/2 independent negative checks passed.** The reviewer-derived fixture calls the actual Claude or Legacy→Anthropic preparer, changes only its returned targetReference, and submits it through real Runtime selection replacement. Both reject with ENGINE_UNAVAILABLE/502. This proves the positive test cannot be satisfied by silently relaxing the binding guard. Evidence: target-binding-negative.test.ts and NEGATIVE_TESTS.log.
- **61/61 assessed source files stable after tests**; all50 manager freeze bindings matched. Exact test configuration, logs, negative probe and post-test hashes are retained in this supplement.

Author and manager typecheck/focused results are separate corroboration. The reviewer did not run a new typecheck, full frontend suite, provider call or native qualification. Default adapter constructors are instantiated, but provider preflight/startTurn are controlled and the actual preparation methods are pure; no real credential or supplier endpoint is needed for these checks.

Handoff: the exact V6 successor closes R2-8 and the two omitted-test custody gaps. The engine contract supplement remains applicable. Parent/manager may proceed with source adoption/custody under their own gates; this review grants no release or native supplier qualification. Preserve all preceding FAIL and PASS snapshots as historical evidence.
