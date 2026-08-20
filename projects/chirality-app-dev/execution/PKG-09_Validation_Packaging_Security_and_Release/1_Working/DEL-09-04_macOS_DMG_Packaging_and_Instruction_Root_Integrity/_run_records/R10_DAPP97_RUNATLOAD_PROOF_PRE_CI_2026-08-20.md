# DEL-09-04 D-APP-97 packaged LaunchAgent RunAtLoad proof — pre-CI record

- Date: 2026-08-20
- Run: `APPDEV_LAUNCHAGENT_RUNATLOAD_PROOF_2026-08-20`
- Accepted upstream: D-APP-97 C1; live DEL-09-04 SOW/Remaining/dependencies;
  R6 daemon-service evidence; `origin/main@7584de0a8` including PR #590.
- Product result: a reusable fail-closed proof is integrated into the unsigned
  Desktop macOS workflow. It uses a unique non-default label and the disposable
  account's canonical `~/Library/LaunchAgents`, installs through the packaged
  CLI, bootstraps once without `kickstart`, binds job/argv/process identity to
  the packaged executable, and verifies process/job/plist/runtime-data cleanup
  plus default job/plist protection.
- Safety remediation: four fresh reviews drove strict launchctl error
  classification, stale-evidence invalidation, symlink-safe output, exact daemon
  argv, failure artifact retention, PID accounting, bounded KeepAlive cleanup
  retries/replacement tracking, post-signal waits, and immediate identity
  reinspection before SIGKILL. Final fresh review: PASS, zero findings.
- Final product hashes:
  - workflow `3642152e730e3b6c59d48d860cbf1fd49a5c999d25d505deba4112dde62db2dc`
  - proof script `b2e5aedfc24c891d6952b2f0d1065206c08c3e0e36a211f10b06483a0bfe542f`
  - proof tests `b0bc86f23387e712f40027ada8020dbdd16f64309f2be0fadd552545436ffb61`
  - workflow test `1137dbf12f76649e7744695e9962e7a26ae34e4549b7fdf02ab64f7c3d9dea6a`
- Checks: focused 30/30 PASS; registered frontend test 1,198 passed / 4
  skipped; typecheck, build, harness self-check, APP-HOLD integrity, syntax,
  diff, origin-main intent, scope containment, and final review PASS. Registered
  evidence SHA-256:
  `a3da82dcf5cc7b2edbf9e4a11dd97d971207375f3d647c8fde6338ac637a0c1d`.
- Residual: the actual `macos-15` disposable-account launchd execution remains
  owed on the PR. Apply label `artifact-proof`, require job
  `verify-unsigned-macos` and step `Prove packaged LaunchAgent RunAtLoad` to
  pass, and inspect the retained redacted summary before removing the Remaining
  item.
- State: `IN_PROGRESS`; login-time Remaining remains open pending that external
  proof. The later owner-machine deployment act remains untouched. No release,
  signing, notarization, distribution, lifecycle, reliance, or Checking
  Approval SHA effect.
- Derivative status: current to the named dirty-tree product hashes and accepted
  upstream; this pre-CI evidence does not substitute for product truth or the
  required PR-CI proving run.
