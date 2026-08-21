# Frozen product diff 04

- Supersedes rejected frozen diffs 01-03 after all recorded remediations.
- Both complete candidate files were reviewed as new against `/dev/null`.
  The owner superseded the interim stop with **“Push through failures,”** and
  the exact bytes are restored to the live candidate paths.
- Script: `frontend/scripts/run-packaged-launchagent-login-proof.mjs` — 902
  lines; SHA-256
  `980e2e710ab66006baeefc14d400584bc8837f3ea3b35390db94b879413e2c20`.
- Test:
  `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`
  — 484 lines; SHA-256
  `f168e7d18326a536ff07b4e3a82019904bc43753fa3999acd439b8353171f01a`.
- Manager reproduction: syntax PASS; focused Vitest 15/15 PASS, 501 ms;
  exact two-path scope PASS.
- No host proof/action; proof remains owner-gated.
- Publication state: `PREPARATION_COMPLETE_PUBLISHABLE_PENDING_GIT_PR_CI`;
  local typecheck/build/full Vitest and focused affected tests pass. Direct
  integrated review 01 found three record-only issues; amendment 10 corrected
  them, and direct backcheck 02 passed with zero findings and unchanged hashes.
  Premerge remains PR-CI-owned because the local managed Next attempt lacked
  the shared runtime daemon/project registration lifecycle, returning HTTP 503.
