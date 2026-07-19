# Sealed Launch Brief — N4 Code-Test Child (T2, DEL-04-05 RQ-011 four-class assertions)

- **Parent:** HELP_HUMAN (Agent 0), RunID `D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18`
- **Authority:** D-APP-65 disposition 2 (packet `execution/_Coordination/_DECISIONS/D-APP-65_PACKET_ACCEPTED_RECOMMENDATIONS_2026-07-18.md`): the owner accepted that a three-of-four live evidence basis (D-APP-52 packs: success, auth-401, network) plus unit-level simulated assertions for all four gap classes satisfies the DEL-04-05 RQ-011 four-class verification gap, and authorized this test tranche.
- **Posture:** fresh context; bounded scope; Bash allowed only for `npx vitest run` on the single test file and `npx tsc --noEmit` if needed; no delegation.

## Objective

Close the RQ-011 four-class category-assertion gap in
`projects/chirality-app-dev/frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts`:
today `RATE_LIMITED`, `REQUEST_TIMEOUT`, `NETWORK_ERROR`, and
`API_RESPONSE_ERROR` have source coverage in
`frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` but zero
category-level test assertions.

## Write scope (exactly these)

1. `projects/chirality-app-dev/frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` (edits — additive tests only; do not weaken or delete existing assertions)
2. `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge/_STATUS.md` (Remaining discharge + one History line only; no Current State / lifecycle / Checking Approval SHA change)
3. `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge/_run_records/TASK_RUN_2026-07-18_DAPP65_RQ011_four_class_assertions.md` (new)
4. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18/RETURN_N4_CODE_TEST.md` (your return)

## Test requirements

Read the source first (`classifyHttpError` ~:525-553; `toAnthropicSdkError` ~:596-636; `toNetworkError` ~:648-670; timeout path ~:975-977) and pattern-match the file's existing mock and assertion style (see the existing 401 → `INVALID_API_KEY` case near :565). Add explicit `category` assertions covering at least:

- **RATE_LIMITED** — (a) numeric-status path: rejected error with `status: 429`; (b) named-error path: error whose constructor/name matches `RateLimitError`.
- **API_RESPONSE_ERROR** — a ≥500 status (e.g. 500 or 529).
- **NETWORK_ERROR** — the network-failure path handled by `toNetworkError` (assert the emitted `status: 503` + category).
- **REQUEST_TIMEOUT** — the timeout path (assert category and its 504 status surface).

Each new test also asserts the failure is typed `SDK_FAILURE` and (where a message could embed a key) that redaction holds, consistent with sibling tests. Use only fixture-marked synthetic secrets if any secret-like string is needed (must contain a sanctioned fixture marker such as `fake`/`test`/`dummy`; never an unmarked `sk-ant-` continuation).

## Kit writes

- `_STATUS.md`: remove the single RQ-011 Remaining item (line 10); if the list becomes empty use `- None.`; append History line:
  `- 2026-07-18 - D-APP-65 disposition 2 accepted the RQ-011 criterion (three-of-four live basis from the D-APP-52 packs plus unit-level simulated assertions) and authorized this tranche; explicit category assertions for REQUEST_TIMEOUT, RATE_LIMITED, NETWORK_ERROR, and API_RESPONSE_ERROR added to harness-anthropic-agent-sdk-manager.test.ts. No state or lifecycle change.`
- Run record (new file): purpose, authority (D-APP-65 disposition 2), the four classes and where each is now asserted (test names + line ranges), the live-evidence basis citation (DEL-04-01 files `Evidence_DAPP52_LIVE_PROBE_2026-07-18_summary.json` — 401 shape `api_error_status:401` / `error:"authentication_failed"`, network shape `error_status:null`/`error:"unknown"`, success shape — and the honest statement that RATE_LIMITED was not live-triggered and is covered by simulated assertions per the accepted criterion), gate results, and a D-APP-64 attribution block **only if** you make a selection among materially different defensible designs (schema: OwnerStandingApproval: D-APP-64 §3 / AgentJudgment: SELECT_AND_ADVANCE / SelectedOutcome / JudgedBy / OwnerCaseSelection: NONE / RejectedAlternatives / RationaleArtifact / IndependentVerifier / EffectStatus / PreservedGates). Straightforward pattern-following needs no attribution block.

## Gates (run yourself, record verdicts in the return)

- `npx vitest run src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` from `projects/chirality-app-dev/frontend` — all tests pass, including the new ones.
- Confirm no test was deleted/weakened (state the before/after test count).

Parent runs full typecheck/vitest/secret-scan afterward.

## Return format

`RETURN_N4_CODE_TEST.md`: files written, new test names with the class each covers, gate outputs (summarized), before/after test counts, deviations (should be none).
