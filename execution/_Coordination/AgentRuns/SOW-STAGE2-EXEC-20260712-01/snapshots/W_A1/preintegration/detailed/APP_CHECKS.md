# W-A1 Independent App Check Reproduction

Verdict: `PASS`.

All six accepted App checks were independently rerun. Root harness checks were
read-only with bytecode and pytest-cache writes disabled. Frontend checks ran
from a copy-on-write isolated canonical repository layout under the authorized
reconciliation snapshot scratch area. The accepted live-stub premerge used a
temporary local Next API, a keyless `stub` provider, an isolated mutable
project root, and natural split instruction-root discovery. The server was
stopped after the run and the scratch tree was removed after evidence
promotion.

| Check | Accepted result |
|---|---|
| harness-self-check | PASS |
| harness-pytest | PASS — 264 tests |
| frontend-typecheck | PASS |
| frontend-test | PASS — 97 files / 713 tests; 1 file / 4 tests skipped |
| frontend-build | PASS |
| frontend-premerge | PASS — Section 8: 8; Section 9 report-only: 16 |

## Preserved execution-substrate attempts

- The first frontend-test copy used a shallow scratch layout, so four tests
  correctly failed when their repository-relative fixtures did not resolve.
  The canonical `isolated-root/projects/chirality-app-dev/frontend` R1 rerun
  passed the full suite.
- Premerge attempts 0–R2 used an incomplete or incorrectly rooted isolated
  instruction tree and failed closed before an accepted result. R3 passed all
  eight Section 8 checks, but explicitly exporting the instruction root into
  Section 9 invalidated one split-root auto-detection fixture; Section 9 is
  report-only, but this run was not accepted. R4 removed that override and
  used the canonical natural split layout; Section 8 passed 8/8 and Section 9
  passed 16/16.

These attempts changed no project, candidate, package, source, status,
control, lifecycle, authority, or acceptance semantics. They are preserved as
execution-substrate evidence, not accepted check outcomes. Generated accepted
evidence contains repository/run-relative paths only.
