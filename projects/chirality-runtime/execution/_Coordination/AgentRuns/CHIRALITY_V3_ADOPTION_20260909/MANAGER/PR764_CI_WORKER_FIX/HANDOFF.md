# PR764 shared Runtime CI worker repair

The shared Runtime CI step now runs `npm test -- --maxWorkers=1`. This deterministically limits file-level Vitest concurrency while retaining the complete test inventory, the concurrent behavior inside the ordered-union test, all existing timeouts and production deadlines, and every downstream gate.

Exact source freeze: `SOURCE_FREEZE.json`. Workflow postimage SHA-256: `a19d0fd1dd4b64cdf30b821fcd5eaa30b7be5b316b8649cb651366fd83d6961c`. The only source change is the Test shared runtime command.

The exact serial command passed 53 test files with one expected skip and 772 tests with 14 expected skips in 121.34 seconds. The ordered-union test passed in 307 ms. YAML parsing and diff checks passed. `VALIDATION.json` binds the whitespace-clean selected log and independent review.

Independent `/root/astra_runtime_second_pass` returned PASS with no findings. Review SHA-256: `fde809c7a99f30a33bb7841ac57259b36cf95b1a3c13c38f9e65d304a0e485e9`. Manifest SHA-256: `a26c45f54e0157de6296b6060f9be20aa5b6c30c4a2771619d8b27979a2ad3c9`.

This repair does not assert that amended-head CI has passed. Normal CI must rerun. No test, timeout, job deadline, failure propagation, provider operation, native operation, or acceptance gate was removed or weakened.
