# TASK Run Record — RQ-011 Four-Class Category Assertions

- **Date:** 2026-07-18
- **RunID:** D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18 (N4 code-test child, sealed brief `LAUNCH_BRIEF_CODE_TEST_T2.md`)
- **Deliverable:** DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

## Purpose

Close the RQ-011 four-class category-assertion gap in
`frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts`:
`RATE_LIMITED`, `REQUEST_TIMEOUT`, `NETWORK_ERROR`, and `API_RESPONSE_ERROR`
had source coverage in `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts`
(`classifyHttpError` :525-553, `toAnthropicSdkError` :596-636, `toNetworkError`
:648-670, timeout path :973-977) but zero category-level test assertions.

## Authority

D-APP-65 disposition 2 (packet
`execution/_Coordination/_DECISIONS/D-APP-65_PACKET_ACCEPTED_RECOMMENDATIONS_2026-07-18.md`):
the owner accepted that a three-of-four live evidence basis (D-APP-52 packs:
success, auth-401, network) plus unit-level simulated assertions for all four
gap classes satisfies the DEL-04-05 RQ-011 four-class verification gap, and
authorized this test tranche.

## Classes and Where Each Is Now Asserted

All tests are in
`frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts`.
Each new test asserts the failure is typed `SDK_FAILURE` with the expected
status, asserts the `category` in `details`, and asserts key redaction
(`[REDACTED_API_KEY]` present, configured key absent) where the mocked error
message embeds the configured key. All secret-like strings are fixture-marked
(`test-key`); no unmarked `sk-ant-` continuations were introduced.

| Class | Test name | Lines | Simulated path |
|---|---|---|---|
| RATE_LIMITED (numeric-status path) | `maps SDK 429 status errors to typed rate-limited failures` | 572-616 | Rejected error `{ status: 429 }` → `classifyHttpError(429)`; asserts `SDK_FAILURE` / 429 / `RATE_LIMITED` + redaction |
| RATE_LIMITED (named-error path) | `maps named RateLimitError SDK errors without status to typed rate-limited failures` | 618-658 | Rejected `Error` with `name = 'RateLimitError'`, no status → `toAnthropicSdkError` name branch; asserts `SDK_FAILURE` / 429 / `RATE_LIMITED` + redaction |
| API_RESPONSE_ERROR | `maps SDK 5xx status errors to typed API response failures` | 660-704 | Rejected error `{ status: 529 }` (≥500 branch of `classifyHttpError`); asserts `SDK_FAILURE` / 529 / `API_RESPONSE_ERROR` + redaction |
| NETWORK_ERROR | `maps unreachable-endpoint failures to typed 503 network errors` | 706-748 | Rejected plain `Error` (no status/name match) → `toNetworkError`; asserts `SDK_FAILURE` / emitted `status: 503` / `NETWORK_ERROR` + redacted `details.cause` |
| REQUEST_TIMEOUT | `maps stream timeouts to typed 504 request-timeout failures` | 750-798 | `CHIRALITY_ANTHROPIC_STREAM_TIMEOUT_MS=25` with a `create` mock that rejects with `AbortError` on signal abort → `timedOut` branch; asserts `SDK_FAILURE` / 504 / `REQUEST_TIMEOUT` and the fixed timeout message |

Each new test also asserts the bridged lifecycle event shape
(`session:init` → `turn.accepted` → `turn.failed`), matching the sibling
401 → `INVALID_API_KEY` test idiom.

## Live-Evidence Basis

DEL-04-01 file `Evidence_DAPP52_LIVE_PROBE_2026-07-18_summary.json` (D-APP-52
live probe packs) provides live evidence for three of the four classes'
adjacent surfaces: the 401 shape (`api_error_status:401` /
`error:"authentication_failed"`), the network shape (`error_status:null` /
`error:"unknown"`), and the success shape. RATE_LIMITED was **not**
live-triggered; per the accepted D-APP-65 disposition 2 criterion it is
covered by the unit-level simulated assertions above (both the numeric-status
and named-error paths). This is the honest three-of-four live basis plus
simulated four-class assertion coverage the owner accepted.

## Gate Results

- `npx vitest run src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts`
  (from `projects/chirality-app-dev/frontend`): **PASS** — 1 file, 87/87 tests
  passed (duration 465ms).
- Test count before: 82. After: 87 (+5 additive). No existing test deleted or
  weakened; all edits were additive insertions between the existing 401
  classification test and the redaction test block.

## Attribution

No D-APP-64 attribution block: the work was straightforward
pattern-following of the sealed brief's prescribed classes, paths, and the
existing sibling-test idiom; no selection among materially different
defensible designs was made.
