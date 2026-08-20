# Launch Brief — A2-PKG09-RUNATLOAD-REVIEW-04

- RequestedBy: `WI-PKG09-RUNATLOAD-01`; fresh read-only `TASK + software-code-review`; no delegation/edits.
- Run/package/deliverable: `APPDEV_LAUNCHAGENT_RUNATLOAD_PROOF_2026-08-20` / `PKG-09` / `DEL-09-04`.
- ScopePath: this instance; `ApplyEdits: false`; runtime-managed records only.
- Objective: final 100% review after Amendment 03, especially immediate exact
  executable-identity reinspection before SIGKILL and its regressions.
- Basis: all original basis, implementation/amendment/run/check records,
  reviews 01–03, shared LaunchAgent/CLI sources, real R6 evidence, and
  `origin/main@7584de0a8` PR #590.
- Frozen hashes: workflow `3642152e730e3b6c59d48d860cbf1fd49a5c999d25d505deba4112dde62db2dc`;
  script `b2e5aedfc24c891d6952b2f0d1065206c08c3e0e36a211f10b06483a0bfe542f`;
  proof tests `b0bc86f23387e712f40027ada8020dbdd16f64309f2be0fadd552545436ffb61`;
  workflow test `1137dbf12f76649e7744695e9962e7a26ae34e4549b7fdf02ab64f7c3d9dea6a`.
- Evidence: `AMENDMENT_03_REGISTERED_CHECKS.json`
  `a3da82dcf5cc7b2edbf9e4a11dd97d971207375f3d647c8fde6338ac637a0c1d`;
  focused 30/30; full frontend 1,198/4 skipped; all five registered checks,
  syntax/diff/origin-main/scope PASS.
- Mandatory review: confirm every prior finding remains closed; every TERM and
  KILL is identity-gated at the instant of signal; PID exec/reuse refuses KILL;
  cleanup/retry/replacement/wait/terminal-failure semantics are safe; tests
  truly assert second inspection and no unsafe KILL. Recheck whole proof and
  workflow fences/label/failure-upload/path/no-kickstart/default protection.
- Compare tracked workflow/test against `origin/main@7584de0a8`; review new
  script/test whole-file. Use only read-only repo/Git and review allowlist.
- Return promptly: PASS only with zero actionable findings, else exact finding.
  No launchd, mutation, Git/PR, dependency, release, or lifecycle action.
