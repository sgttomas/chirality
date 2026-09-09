# PR764 CI worker-limit repair review V1

Verdict: **PASS**, no findings. The exact one-line worker limit is supported and preserves the required test/gate behavior. This is source/evidence acceptance of the repair, not a claim that the amended GitHub Actions run has passed.

Reviewer: `/root/astra_runtime_second_pass`, TASK; dispatched model `gpt-6-astra`, reasoning effort `high`. Read-only review; no source edits, retests, provider calls, native execution, staging or publication.

## Exact change

- Review base / current PR head: `9b005c23a76fc2619780d27f5fabb70e3221cf02`.
- Path: `.github/workflows/harness-premerge.yml`, line97.
- Base file SHA-256: `b2434b1d4afad7c1722794b96cf3dca5802f30395b7317df5f0304da507e03e5` (11738 bytes).
- Current file SHA-256: `a19d0fd1dd4b64cdf30b821fcd5eaa30b7be5b316b8649cb651366fd83d6961c` (11756 bytes).
- Full-index diff SHA-256: `ad9cd68c8a04147577167bfc932816f0080abf5f0998aaa02ee7a7e56c822a74` (561 bytes).
- Diff command: `git diff --no-ext-diff --full-index --binary 9b005c23a76fc2619780d27f5fabb70e3221cf02 -- .github/workflows/harness-premerge.yml`.

Byte comparison proves the complete file differs only by `npm test` → `npm test -- --maxWorkers=1` in Test shared runtime. Exact base, postimage and patch are retained under pr764-ci-worker-review-v1/. The Runtime source/tests/config/scripts have no HEAD diff; a separate coordination notice is outside this workflow repair and is not a product test change.

## Supported and effective option

Runtime package.json defines test as `vitest run` and pins Vitest3.2.7; package-lock and installed package agree. npm's `--` forwards the argument to that script. The retained run header confirms the effective command was `vitest run --maxWorkers=1`.

The installed Vitest CLI defines maxWorkers as the maximum number/percentage of workers (cac.BfaZ95xE.js:952). Its resolver parses that option (coverage.DfSpMS-b.js:3584). The forks pool uses maxWorkers as maxThreads and clamps the default minimum to that maximum (:2612–2613); the threads pool likewise uses maxWorkers. The repo's active vitest.config.ts supplies only existing exclusions, with no pool-specific override. Thus this command limits file workers to one rather than leaving an inert or misspelled flag.

The patch changes scheduling capacity only. It adds no filter, exclusion, shard, skip, bail, retry, testTimeout, hookTimeout, passWithNoTests, success fallback or continue-on-error. Existing test deadlines remain in force. It leaves maxConcurrency and test bodies untouched. In particular, runtime-v3-api.test.ts:285 still invokes both dynamic method loaders with Promise.all, so the intentional concurrent-union behavior remains exercised inside the test even with one file worker. Reduced incidental overlap between independent test files is the intended resource change, not replacement of the concurrency assertions.

## Gates and job budget

The job still runs on ubuntu-latest with Node24 and timeout-minutes30. Workflow triggers, concurrency cancellation, permissions, build/install commands, working directory, frontend checks, supply-chain policy, secret scan, instruction-root integrity, release-quality wrapper, stable-summary assertions, upload/failure diagnostics and cleanup are byte-identical. The test step still propagates npm/Vitest failure normally; no error suppression was added.

The observed Runtime test duration121.34s is about2.02 minutes, or6.74% of the unchanged30-minute job budget. That leaves a plausible budget for the remaining job, but local timing is not a measurement of the complete Ubuntu job. The job deadline has not been extended, and downstream gates must still complete normally in CI. This review does not assert a guaranteed total runtime or successful amended CI run.

## Retained execution evidence and limits

Raw serial log SHA-256: `6456b4acc6d078ddb2126c82aa8fde58d7f6f52cf1a237f258dcf4d22fdf2b23`, independently matched to /tmp/pr764-runtime-serial-test.log and copied into this review.

Selected clean log SHA-256: `b2f27f9420db94eaa8b57098de2ec09971c1a5456c2350d148168e41eb4f6d08`. The reviewer verified that it is exactly the raw output with trailing line whitespace and terminal blank lines removed. Both are retained, so normalization does not replace the original evidence.

The log records Vitest3.2.7, 53 passed test files/1 skipped, 772 passed tests/14 skipped, duration121.34s. The named concurrent dynamic-load union test completed in307ms; the separate active ordered-selection test completed in395ms. The full inventory was selected, and skipped counts remain reported rather than suppressed.

The triggering CI run34407146369 failure (one5000ms timeout, other765 pass/20 platform skips, approximately94s suite) is parent/manager-reported context; the reviewer did not retrieve an exact CI log. CI versus local platform skips/timings are not presented as equivalent measurements. The supported scheduling option plus successful unchanged local inventory supports this bounded contention mitigation; it does not conclusively prove the historical timeout's cause or certify future runs. Manager-reported YAML parse/diff-check PASS corroborates the exact one-line textual analysis; no parser/test rerun occurred here.

Handoff: accept this exact workflow repair for the next CI attempt. Preserve failure evidence and require the normal amended-head CI gates. No test requirement, timeout, job deadline or downstream acceptance gate was weakened.
