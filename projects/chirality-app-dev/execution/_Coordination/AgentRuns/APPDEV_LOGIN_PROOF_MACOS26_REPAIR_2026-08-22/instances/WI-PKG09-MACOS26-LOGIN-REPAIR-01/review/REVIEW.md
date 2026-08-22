# Fresh review — A2-PKG09-MACOS26-REVIEW-01

- Verdict: `FINDINGS`
- Accepted basis / reviewed HEAD: `9bfe529352afb8bb43a8f0c6afd9a4b3945453b1`
- Branch: `codex/app-login-proof-macos26-repair`
- Scope: 100% of the frozen source, focused test, `_STATUS.md`, R14, R15,
  implementation brief, and executor return
- Review mode: evidence-only; no repair

## Actionable finding

### F-01 — Focused tests do not cover all enumerated fail-closed classes

The negative preflight tables in
`frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts:228`
through line 341 cover console/domain mismatch, generic malformed output,
exit-code failure, stderr-bearing success, and selected ambiguity cases, but
they do not exercise the explicitly required non-Darwin, root-UID,
process/account-UID mismatch, invalid current-account identity
(`root`/`loginwindow`/`_mbsetupuser`), setup console identity, signaled `stat`,
signaled `launchctl`, trailing domain output, or incomplete-brace paths.
Consequently R15's comprehensive-suite statement at
`_run_records/R15_MACOS26_LOGIN_IDENTITY_REPAIR_2026-08-22.md:57` and review
matrix item 8 are not yet supported, even though source inspection indicates
the corresponding branches fail closed.

Required repair: add direct focused cases for each listed class, including
assertions that preflight emits no success result, invokes no product/install
or service-level/mutating operation, and creates no session root. Then rerun
syntax, the focused suite, typecheck, full Vitest, live preflight with proposed
root absence before/after, APP-HOLD, practitioner self-check, hashes,
containment, and `git diff --check`; update the focused count/hash and affected
R15/status/executor claims before a fresh reviewer reruns this matrix.

## Evidence matrix

| # | Result | Evidence |
|---|---|---|
| 1 | PASS | R14 lines 11-29 attribute the exact JSON error and no-plist/no-job state to the owner; lines 31-41 separately bound the manager's empty mode-0700 old-root observation and infer no acceptance. |
| 2 | PASS | Full source review and independent scan found no product `osascript`, JXA, CoreGraphics, or `CGSessionCopyCurrentDictionary` reference. |
| 3 | PASS | Source lines 333-443 execute only `/usr/bin/stat -f %Su:%u /dev/console` and `/bin/launchctl print gui/<uid>` for identity; preflight returns before all job/service paths. |
| 4 | PASS (implementation) | Source lines 260-290 and 333-353 fail closed for platform, UID/account, real-user, console-user, and console-UID errors. Direct coverage is incomplete per F-01. |
| 5 | PASS (implementation) | Source lines 355-430 are depth-aware, select only top-level identity fields/direct security-context fields, and reject required-field ambiguity, malformed braces/trailing output, unsafe values, wrong UID/type/session, and handle/`asid` mismatch. Direct coverage is incomplete per F-01. |
| 6 | PASS | Source lines 446-459, 662-665, 725-745, and 916-923 use one private nonempty random salt across prepare/capture, expose SHA-256 digests, bind the session identifiers, and retain unchanged-identity rejection. |
| 7 | PASS | Source lines 56-64 and 1042-1058 make preflight optionless and resolve it before session-root handling; live output contains no raw username/handle and reports calibrated read-only/no-root fields. |
| 8 | FAIL | Focused suite passes 34/34 and legacy prepare/capture/cleanup/default-protection cases remain green, but enumerated direct negative coverage is incomplete; F-01. |
| 9 | PASS with F-01 caveat | Independent `node --check`, focused Vitest (34/34), and typecheck passed. Executor's full-suite record coherently distinguishes sandbox socket `EPERM` from the exact unrestricted 1,233-pass/4-skip rerun and states no intervening source change. |
| 10 | PASS | Independent live preflight passed on macOS 26.6.2 build 25G83. Proposed root `/private/tmp/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20` was absent before and after; only the optionless product preflight was run. |
| 11 | PASS | R15 and `_STATUS.md` remain `IN_PROGRESS`, unproved, uncommitted, and unbuilt; exact `PROOF_REVISION`/`PROOF_APP` remain unavailable and the proposed root/label are explicitly non-executable. |
| 12 | PASS | Frozen records, current Git state, and artifact mtimes are coherent with no build/package, GUI, proof, service mutation, deployment, release, provider/network, or Git publication action in this node. |
| 13 | PASS | Current porcelain is limited to the two frontend paths, status, R14, R15, and this unique run root, all under `projects/chirality-app-dev/`; index is empty. Diff numstat is 204/36 plus 223/10, `git diff --check` is clean, and all five recorded SHA-256 values match. |
| 14 | PASS | R15 and the executor return explicitly state derivative status, no implementation blocker, rerun conditions, and the committed-repair then separately authorized unsigned-rebuild handoff. |

## Independent checks

- `node --check scripts/run-packaged-launchagent-login-proof.mjs`: PASS
- focused Vitest: PASS, 34/34
- `npm run typecheck`: PASS
- optionless live preflight: PASS; proposed root absent before/after
- `python3 execution/_Scripts/app_hold.py scan --require-register-match`: PASS,
  53 contracts, register match
- `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check`:
  PASS at the existing baseline
- forbidden product-source scan: PASS
- recorded SHA-256 values: PASS
- `git diff --check -- projects/chirality-app-dev`: PASS
- staged index: empty

## Final verdict

`FINDINGS` — return to a fresh bounded repair cycle for F-01, then require a
fresh evidence-only reviewer. No product/source/record repair was performed by
this reviewer.
