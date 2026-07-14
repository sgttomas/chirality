# PKG-03 Acceptance Checks

Terminal technical verdict: `PASS`.

- HEAD, local `main`, `origin/main`, and remote `main` equal
  `5f124ad80fe84357f6dc33072dc4fbdbeb05d545`.
- Prior full-package snapshot manifest rehashed 102/102.
- Five upstream manifests rehashed 3,610/3,610 with portability,
  containment, existence, uniqueness, self-exclusion, byte, and hash checks.
- Current live source/status/control/dependency bindings passed 72/72;
  candidate evidence/production/finalization bindings passed 24/24.
- Full Agent-1 reproduction passed all eight members, 234 mappings,
  1,966/1,966 source lines, exact 40-row replacement and inverse rollback,
  8/8 simulations, and 16/16 fail-closed negative probes.
- Fresh `tools/practitioner_harness/harness.py self-check` exited 0.
- Fresh `pytest -q -p no:cacheprovider tools/practitioner_harness` passed
  264/264; JUnit records zero failures, errors, or skips.
- Piping tree rehash after validation is exactly the prior before/after value:
  191,240 files, SHA-256
  `974fe2fad26880ba85c0359ee18f9ee87a404fd097a83bb6248cc6348b391a92`.
  Tracked and untracked non-ignored Piping status is clean; ignored state is
  included in the byte-tree digest.

Separate verdicts: schema `PASS`; content/authority `PASS`;
preservation/containment `PASS`; execution substrate `PASS`.
