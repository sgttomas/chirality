# CHANGE-CLEAN-REPAIR Preintegration Checks

Verdict: `PASS`

- Accepted manifest SHA-256: `f3f17fec99fa54cad63fb6d05af0272c47d3b3f505ac6787dfa58661dae8e2b6`.
- Atomic project commits: 57/57, one accepted path each, sorted manifest order.
- Before, after, and finalization-report hashes: 57/57 reproduced.
- Production forbidden tokens: zero.
- ScopeOfWork tool suite: PASS.
- Practitioner harness: 264 PASS.
- Root instruction validators: 4 PASS.
- App: typecheck PASS; 713 PASS and 4 skipped; build PASS.
- Piping: WASM build PASS; 476 PASS; desktop build PASS.

The retained `CHECK_RESULTS.json` records the initial incomplete-layout App
fixture attempt as nonzero. `APP_TEST_RERUN.json` and
`checks/app_tests_r1.txt` bind the corrected complete-layout PASS.
