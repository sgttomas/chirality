# Fresh review after repair cycle 1 — A2-PKG09-MACOS26-REVIEW-02

- Verdict: `PASS`
- Accepted basis / reviewed HEAD: `9bfe529352afb8bb43a8f0c6afd9a4b3945453b1`
- Branch: `codex/app-login-proof-macos26-repair`
- First-review basis SHA-256:
  `adc3de73ed0ab46043ad599c9dbac34078c2982a7db9b9c8a7a42ce5a30b64d8`
- Remediation-return basis SHA-256:
  `c0d35ab67934859fd542eac421d84f9a111876de6f3253f47d859be100dbe3c6`
- Review mode: evidence-only; no repair, build, prepare, capture, Git mutation,
  operator-path access, or service/job mutation

## F-01 closure

`frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`
now directly covers every class required by F-01:

- lines 259-286: non-Darwin, root UID, process/account UID mismatch, and
  invalid current accounts `root`, `loginwindow`, and `_mbsetupuser`;
- lines 288-317: setup/loginwindow console identities, command failure,
  signaled `stat`, and stderr-bearing `stat`;
- lines 319-430: malformed/ambiguous/mismatched domains, signaled top-level
  launchctl, trailing domain output, and incomplete top-level and security
  context braces.

All twelve added classes flow through the shared assertion at lines 165-190.
That assertion requires an error with no PASS result, no packaged-app/install
execution, no service-level or mutating launchctl operation, and no session
root. The focused suite independently passed 46/46. F-01 is closed.

## Evidence matrix

| # | Result | Evidence |
|---|---|---|
| 1 | PASS | R14 lines 11-29 records the exact owner-reported JSON error and no-plist/no-job claim; lines 31-41 separately bound the manager's read-only empty mode-0700 old-root observation and infer no acceptance. |
| 2 | PASS | Full product-source review plus an independent forbidden scan found no `osascript`, JXA, CoreGraphics, or `CGSessionCopyCurrentDictionary` runtime path. |
| 3 | PASS | Source lines 333-443 use exactly `/usr/bin/stat -f %Su:%u /dev/console` and `/bin/launchctl print gui/<uid>` for identity. Preflight returns at lines 1042-1046 before every service/job/session-root route. |
| 4 | PASS | Source lines 260-290 and 333-353 fail closed for platform, root/invalid account, UID mismatch, and loginwindow/setup console identities; direct cases pass at test lines 259-317. |
| 5 | PASS | Source lines 355-430 track nesting depth, read only top-level identity and direct security-context fields, and reject malformed/trailing/incomplete, duplicate/ambiguous, unsafe, wrong-UID/type/session, and handle/`asid` mismatch evidence. Direct negative cases pass at test lines 319-430. |
| 6 | PASS | Source lines 446-459, 662-665, 725-745, and 916-923 keep one nonempty private random salt across prepare/capture, expose SHA-256 only, bind handle/security identifiers, and retain unchanged-session rejection. The transition and unchanged-session tests pass. |
| 7 | PASS | Source lines 56-64 and 1042-1058 make preflight optionless and resolve it before session-root handling. Its independently observed output contains only calibrated booleans and a digest, with `serviceOrJobInspection`, `mutationsPerformed`, and `sessionRootCreated` all false. |
| 8 | PASS | Focused Vitest passed 46/46, including all F-01 classes and retained prepare/capture/cleanup/default-protection tests. Every negative preflight case uses the common no-install/no-service/no-root assertion. |
| 9 | PASS | Independent syntax, focused Vitest, and typecheck passed. The retained remediation evidence coherently distinguishes 21 sandbox socket-bind `EPERM` failures from the exact unrestricted 1,245-pass/4-skip rerun and records no intervening source/test change; current hashes match, so a second full-suite rerun was not required. |
| 10 | PASS | Independent optionless preflight passed on macOS 26.6.2 build 25G83. Proposed root `/private/tmp/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20` was absent before, after, and at final review check. Source and test command capture establish only top-level read-only inspection. |
| 11 | PASS | R15 and `_STATUS.md` remain `IN_PROGRESS`, unproved, uncommitted, and unbuilt. Exact `PROOF_REVISION`/`PROOF_APP` remain unavailable; the proposed root/label are explicitly non-executable. |
| 12 | PASS | Records and current Git/artifact state remain consistent with no build/package, GUI, prepare/capture, logout/login, LaunchAgent/operator-path action, bootstrap/kickstart, deployment, network/provider, release, signing/notarization/distribution, publication/issuance, or Git publication action. |
| 13 | PASS | Dirty paths are limited to the two frontend paths, status, R14, R15, and this unique App run root. All are under `projects/chirality-app-dev/`; index empty, `git diff --check` clean, source/test numstat 204/36 and 313/10, and all recorded hashes match. |
| 14 | PASS | R15 and remediation evidence explicitly state derivative status, no repair blocker, rerun conditions, and the separately authorized commit-then-unsigned-rebuild handoff before any executable owner procedure. |

## Independent checks

- `node --check scripts/run-packaged-launchagent-login-proof.mjs`: PASS
- focused Vitest: PASS — 46/46
- `npm run typecheck`: PASS
- optionless live preflight: PASS; proposed root absent before/after/final
- APP-HOLD `scan --require-register-match`: PASS — 53 contracts, register match
- practitioner harness `self-check`: PASS at the existing disclosed baseline
- forbidden product-source scan: PASS
- `git diff --check -- projects/chirality-app-dev`: PASS
- containment: PASS — no dirty path outside the App root
- staged index: empty
- source SHA-256:
  `64031e7aab464d1178f2e94d3a1451444594b050318181aafd4d2805bbb8aa98`
- focused-test SHA-256:
  `76d3d2a36ee47f327bbecb09c1fc2832480086855a116477988eccb0a4487631`
- `_STATUS.md` SHA-256:
  `f4f020921f3ef6fdc9fd145436cbfbcd562672def9748ce58aadf69c81a03fce`
- R14 SHA-256:
  `7a124d6cdbc519c32d573664eca4f8f4d0327fdae2b92a90b0fe8ad16cf08234`
- R15 SHA-256:
  `0ffc3995b6ad3e599c62c5dd7e05d4f29de66a0492da9e8f8bbb009e496c03e7`

## Final verdict

`PASS` — the complete 14-item matrix passes after repair cycle 1, F-01 is
closed, and no actionable finding remains. This is local repair-review evidence
only; it establishes no packaged-app identity, login auto-start proof,
lifecycle acceptance, release readiness, signing, notarization, distribution,
publication, issuance, or reliance.
