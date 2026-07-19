# Sealed Verifier Brief — T2 Adversarial Governed-Diff Verifier (refutation-only)

- **Parent:** HELP_HUMAN (Agent 0), RunID `D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18`
- **Posture:** fresh context; no shared authorship; read-only except the single return file; sole deliverable `COMMIT-SAFE` or `BLOCK`; default `BLOCK` if uncertain. Repo-relative paths in the return.
- **Write scope:** exactly `projects/chirality-app-dev/execution/_Coordination/AgentRuns/D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18/RETURN_T2_GOVERNED_DIFF_1.md`.

## Scope under test

The staged diff (`git diff --cached`) against HEAD = commit `7fd0466f9` (the D-APP-65 T1 commit). This brief file itself is the declared untracked addition besides your return.

## Claims to refute

1. **Whole-diff claim.** The staged diff touches only: `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts`; DEL-04-05 `_STATUS.md`; new `DEL-04-05 .../_run_records/TASK_RUN_2026-07-18_DAPP65_RQ011_four_class_assertions.md`; run-directory files `LAUNCH_BRIEF_CODE_TEST_T2.md` and `RETURN_N4_CODE_TEST.md`. Nothing else; no runtime source file changed (test file only in `frontend/src`).
2. **Additive-tests claim.** The test-file diff adds tests only: no existing test deleted, renamed, skipped, or weakened (no removed `expect` lines, no `.skip`/`.only` introduced). The five new tests assert `category` values `RATE_LIMITED` (both a 429-status path and a named `RateLimitError` path), `API_RESPONSE_ERROR` (5xx), `NETWORK_ERROR` (503 surface), and `REQUEST_TIMEOUT` (504 surface), each typed `SDK_FAILURE`, and include redaction assertions. Run `npx vitest run src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts` from `projects/chirality-app-dev/frontend` yourself and confirm all pass.
3. **Assertion-truth claim.** For each of the four classes, the asserted category/status pairing matches the live source behavior in `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` (`classifyHttpError`, `toAnthropicSdkError`, `toNetworkError`, the stream-timeout path) — i.e. the tests pin real code paths, not mocks of mocks.
4. **Status-surface rules.** DEL-04-05 `_STATUS.md`: exactly the RQ-011 Remaining item removed (list now `- None.`) and exactly one dated History line appended; no `Current State`/lifecycle/`Last Updated`/`Checking Approval SHA` change.
5. **Evidence honesty.** The run record cites the D-APP-52 live packs for the live-evidenced shapes and states plainly that RATE_LIMITED was not live-triggered and is covered by simulated assertions under the D-APP-65 disposition-2 criterion; no document claims live rate-limit evidence or any lifecycle/adoption effect.
6. **Hygiene.** No staged file introduces an unmarked `sk-ant-`-continuation token or credential material (fixture-marked synthetics allowed); `npm run proof:secret-scan` from `projects/chirality-app-dev/frontend` reports zero blocked findings; repo-wide `python3 tools/practitioner_harness/harness.py self-check` exits 0 at the pinned baseline (INFO=15, NOT_APPLICABLE=2, REVIEW=33, WARN=6).

## Return format

`RETURN_T2_GOVERNED_DIFF_1.md`: verdict line first, then per-claim findings with evidence commands and observed values.
