# Return — A2-PKG09-RUNATLOAD-IMPLEMENT-01

- Verdict: `SUCCESS`; Amendment 03 is complete and ready for fresh review v4.
- Changed product/test paths remain exactly:
  - `.github/workflows/desktop-release-template.yml`
  - `projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-runatload-proof.mjs`
  - `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-runatload-proof.test.ts`
  - `projects/chirality-app-dev/frontend/src/__tests__/scripts/desktop-release-workflow.test.ts`
- Cleanup-race behavior remains: cleanup uses five bounded service inspections
  and bootout attempts. Only exact supported launchctl not-found is terminal
  success. After an ineffective attempt, it identity-checks the observed PID
  before signaling, reinspects to capture any KeepAlive replacement PID, and
  retries bootout. SIGTERM and SIGKILL both have bounded absence waits. A still
  loaded service or live tracked process is terminal FAIL. Immediately before
  SIGKILL it now reinspects the numeric PID and requires one exact packaged text
  executable; changed, missing, or ambiguous identity refuses SIGKILL and is a
  persistent terminal failure.
- New focused regressions prove identity change after TERM sends no SIGKILL and
  fails closed, while the successful KILL path performs the second inspection.
  All prior amendment regressions remain green.
- PR #590: exact overlapping byte intent at `origin/main@7584de0a8` remains
  preserved; origin-main diff contains only this node's proof additions.
- Checks: focused Vitest PASS (2 files / 30 tests); registered frontend test
  PASS (151 files passed, 1 skipped; 1,198 tests passed, 4 skipped), typecheck
  PASS, build PASS, harness self-check PASS, and APP-HOLD integrity PASS.
  Syntax, diff, origin-main, and explicit containment checks pass.
- Evidence: `AMENDMENT_03_REGISTERED_CHECKS.json` SHA-256
  `a3da82dcf5cc7b2edbf9e4a11dd97d971207375f3d647c8fde6338ac637a0c1d`.
- Final product/test SHA-256 values:
  - workflow: `3642152e730e3b6c59d48d860cbf1fd49a5c999d25d505deba4112dde62db2dc`
  - proof script: `b2e5aedfc24c891d6952b2f0d1065206c08c3e0e36a211f10b06483a0bfe542f`
  - proof tests: `b0bc86f23387e712f40027ada8020dbdd16f64309f2be0fadd552545436ffb61`
  - workflow contract test: `1137dbf12f76649e7744695e9962e7a26ae34e4549b7fdf02ab64f7c3d9dea6a`
- Residual: PR CI `verify-unsigned-macos` / `Prove packaged LaunchAgent
  RunAtLoad` must run the real launchd proof on `macos-15` and retain its
  redacted summary artifact.
- No local launchd proof, owner/default LaunchAgent mutation, dependency or
  lockfile change, Git history action, commit, push, or PR operation occurred.
  No owner decision is required before fresh review v4.
