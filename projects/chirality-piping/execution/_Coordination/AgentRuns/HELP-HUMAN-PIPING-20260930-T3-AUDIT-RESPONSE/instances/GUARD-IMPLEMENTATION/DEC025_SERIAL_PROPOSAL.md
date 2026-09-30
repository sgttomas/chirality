# Separate minimal serial DEC-025 adaptation proposal

**Proposed only. No driver or archived record was edited or executed.**
A later driver is a new response-owned artifact with an independent review.
It is not part of the initial direct-command guard qualification.

Inspected references under the historical T3 root (full paths/hashes in
CONTEXT.json):

- `IMPLEMENTATION/M03_SKEW_PIN_MERGE/dec025/dec025_mac.sh.txt`: sets cargo jobs=8
  and test threads=4 internally; invokes the fail-fast maintained sweep, copies
  its JSON, calls the old scratch no-fail-fast suite runner, then Python tests,
  wasm build, desktop tests and desktop production build with explicit exit logs.
- `IMPLEMENTATION/K3/_run_records/checkpoint_b/suites/run_suites_nff.sh.txt`:
  discovers manifests with the maintained `discover_cargo_manifests`, fetches,
  then tests every manifest offline/locked/no-fail-fast, reporting exit code and
  summed pass/fail/ignored counts. It also overrides concurrency to 8/4.
- `PLATFORM_CALIBRATION_MAC/suites/run_suites.sh.txt`: earlier similar driver
  without no-fail-fast. It must not silently replace the later suite contract.

The minimal adaptation is a new driver preserving that inventory and reporting
shape, with these explicit deltas:

1. Seal clean candidate and same-M3 base source identities, requirements/toolchain
   and driver hash. Use an actual clean Git checkout for the maintained sweep
   and GEN-8. ROOT owns source preparation; do not present an archive as a clean
   tracked-set witness. Original M5 evidence remains historical.
2. Set the isolated Rust/Python/Node homes and `RUSTUP_TOOLCHAIN=1.97.1`,
   `RUSTUP_AUTO_INSTALL=0`, `CARGO_INCREMENTAL=0`, `CARGO_BUILD_JOBS=1`,
   `RUST_TEST_THREADS=1` **inside both new driver layers**. Cargo invocations
   retain `--offline --locked` and explicit `-j 1`. Retain --no-fail-fast in
   the complete suite pass. One pytest worker (serial; no -n auto), one supported
   desktop-test worker, and sequential phases. Verify actual commands so a
   nested export/script cannot silently restore 8/4 or parallelize phases.
3. Enumerate and save the complete current manifest list with the maintained
   discovery function. Run every manifest once per selected clean candidate,
   preserving per-manifest raw logs, original return code, pass/fail/ignored
   totals, failures with no summary, and discovery errors. Do not hard-code
   the historical 39/40 count or filter known Mac failures. Compare manifest
   inventories explicitly and report missing/added items.
4. Move dependency fetch to the separately authorized setup stage. Missing
   offline dependencies become named unavailable gates, with no hidden fetch
   inside the guarded execution stage and no lockfile edits to obtain a pass.
5. Keep the maintained fail-fast sweep invocation and record its exact outcome,
   then all-manifest no-fail-fast evidence, pytest, wasm build, desktop tests
   and production build with their existing assertions. Preserve the sweep JSON
   and candidate binding. Keep expected-failure reporting distinct from success:
   old M5 platform failures are hypotheses until the same-M3 base is measured.
   Continue ordinary test-failure inventory only while guard health is confirmed.
   On guard refusal/kill/unknown containment, stop and list unrun gates; never
   print SUITES-DONE/ALL-DONE as if omitted gates ran.
6. Run sequential admitted commands under the one runtime slot. Guard event
   `guard_healthy` and `workload_returncode` distinguish a contained test failure
   from guard failure (both can give CLI exit 2). Preserve original return values
   in the driver summary. Size/extend output budgets only by reviewed change;
   current 8 MiB workload output and 1-hour limit may not fit full suite stages.

Admission of the full driver needs command-type coverage beyond initial cargo/
tiny probes, including Node/Python/native subprocesses and separate-group tests.
Keep K6/VR unsupported until their adapter is independently qualified. A driver
that wraps unsupported nested groups is not protected simply because its outer
command holds the slot. No tests, tolerances, expected failures, evidence-sweep
surfaces, GEN-8, native witnesses or protected criteria are waived here.
