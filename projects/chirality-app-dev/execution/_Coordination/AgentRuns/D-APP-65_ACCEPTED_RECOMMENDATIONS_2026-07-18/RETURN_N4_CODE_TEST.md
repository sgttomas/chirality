# Return — N4 Code-Test Child (T2, DEL-04-05 RQ-011 four-class assertions)

- **RunID:** D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18
- **Brief:** `LAUNCH_BRIEF_CODE_TEST_T2.md`
- **Status:** COMPLETE — all gates pass, no deviations

## Files Written (exactly the four in write scope)

1. `projects/chirality-app-dev/frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` — five additive tests inserted after the existing 401 → `INVALID_API_KEY` test; no existing test deleted or weakened.
2. `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge/_STATUS.md` — RQ-011 Remaining item (line 10) removed, list now `- None.`; the prescribed single History line appended verbatim. No Current State / lifecycle / Checking Approval SHA change.
3. `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge/_run_records/TASK_RUN_2026-07-18_DAPP65_RQ011_four_class_assertions.md` — new run record with purpose, authority, per-class assertion map, live-evidence basis citation, and gate results.
4. This return.

## New Tests (name → class covered)

| Test (lines) | Class |
|---|---|
| `maps SDK 429 status errors to typed rate-limited failures` (572-616) | RATE_LIMITED — numeric-status path (`status: 429`) |
| `maps named RateLimitError SDK errors without status to typed rate-limited failures` (618-658) | RATE_LIMITED — named-error path (`name: 'RateLimitError'`) |
| `maps SDK 5xx status errors to typed API response failures` (660-704) | API_RESPONSE_ERROR — `status: 529` (≥500 branch) |
| `maps unreachable-endpoint failures to typed 503 network errors` (706-748) | NETWORK_ERROR — `toNetworkError` path; asserts emitted `status: 503` |
| `maps stream timeouts to typed 504 request-timeout failures` (750-798) | REQUEST_TIMEOUT — timeout path via `CHIRALITY_ANTHROPIC_STREAM_TIMEOUT_MS=25` + abort-rejecting mock; asserts 504 |

Every new test asserts `type: 'SDK_FAILURE'`, the `category`, the status
surface, redaction where the mocked message embeds the configured key
(`[REDACTED_API_KEY]` present, `test-key` absent; NETWORK_ERROR asserts the
redacted `details.cause`), and the sibling-idiom lifecycle shape
(`session:init` → `turn.accepted` → `turn.failed`). Only fixture-marked
synthetic strings (`test-key`) were used; no unmarked `sk-ant-` material.

## Gate Verdicts

- Targeted vitest (`npx vitest run src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` from `projects/chirality-app-dev/frontend`): **PASS** — 87/87 tests, 1 file, 465ms.
- Test count: **82 before → 87 after** (+5 additive). Confirmed no deletion or weakening: all edits were pure insertions; every pre-existing assertion is intact.

## Attribution

No D-APP-64 attribution block emitted: straightforward pattern-following of
the brief's prescribed classes/paths and the existing mock/assertion idiom;
no selection among materially different defensible designs.

## Deviations

None.
