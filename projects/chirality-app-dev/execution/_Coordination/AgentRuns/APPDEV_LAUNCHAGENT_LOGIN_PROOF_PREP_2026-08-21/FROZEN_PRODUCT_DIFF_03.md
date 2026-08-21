# Frozen product diff 03

- Supersedes rejected frozen diffs 01 and 02 after P1/P2 remediation.
- Both paths are complete new files against `/dev/null`; review coverage 100%.
- Script: `frontend/scripts/run-packaged-launchagent-login-proof.mjs`
  - lines: 877
  - SHA-256: `b7694d5cfb27a4c17fa1b692c989aa35749ea2d77999d6b6eafa817d9dccdcfb`
- Test: `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`
  - lines: 447
  - SHA-256: `ad58fc182f5632ba83c52699309eb541ff7d5728308c5f2ac347a52a1e5dccc8`
- Manager reproduction: syntax PASS; focused Vitest 1 file / 13 tests PASS,
  493 ms; prior exact two-path scope PASS remains applicable.
- No host proof/action; proof remains owner-gated.
