# Amendment 01 — Review remediation and PR #590 integration

- Parent disposition: `AMEND` the current implementation node in place.
- Trigger: fresh review v1 returned six actionable findings; upstream PR #590
  merged after the v1 freeze at `origin/main@7584de0a8` and overlaps the two
  tracked workflow/test files.
- Objective unchanged: fail-closed disposable-account packaged LaunchAgent
  `RunAtLoad` proof.
- Required remediation:
  1. Recognize only an exact supported launchctl not-found result as job
     absence; fail on permission/domain/transient errors in unique/default
     preflight and cleanup. Add focused cases.
  2. Safely invalidate stale PASS evidence before platform/uid/HOME/label
     preflight failures and test seeded stale evidence.
  3. Canonicalize or no-follow-protect output-root ancestors so symlinks cannot
     redirect evidence into `~/Library/LaunchAgents` or the app. Add symlink
     regressions.
  4. Parse and require the exact plist argument vector
     `[packaged executable, --runtime-daemon]`; bind loaded arguments if
     available. Add missing/wrong/extra cases.
  5. Retain redacted FAIL proof evidence in CI with a dedicated `if: always()`
     upload using `if-no-files-found: warn`, without weakening the existing
     successful unsigned artifact upload.
  6. Never report unknown PID as proven absent. Capture observed PID before
     later identity assertions or mark absence unproven and perform bounded
     identity cleanup. Add partial-failure/lingering-process coverage.
- Upstream byte intent to preserve:
  - workflow `pull_request.types: [opened, synchronize, reopened, labeled]`;
  - job gate `if: ${{ github.event_name == 'workflow_dispatch' || contains(github.event.pull_request.labels.*.name, 'artifact-proof') }}`;
  - the corresponding 25-line workflow contract test from PR #590.
- Checks: focused tests, full frontend test/typecheck/build, harness self-check,
  APP-HOLD integrity, scope/diff checks. Do not run local launchd proof.
- Return: exact changed paths, per-finding disposition, upstream preservation,
  new evidence, residual PR-CI proof, and final hashes.
- All original write fences/exclusions remain unchanged.
