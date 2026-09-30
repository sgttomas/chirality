# Backcheck commands and results

Root-relative `Run` is the response AgentRuns directory. All outputs below are
inside `Run/instances/GUARD-REVIEW/continuation_01`. Python executions used
PYTHONDONTWRITEBYTECODE=1. No live provider/controller script was invoked.

- `diff -u Run/tools/host_guard.py Run/tools/host_guard_v2.py`: expected exit 1,
  two source hunks. Read full new helper and caller; AST comparison of all
  top-level nodes is retained in SOURCE_CHECKS.json. All nodes except read_job
  match after excluding the added helper. All 15 v2 manifest entries verify.
- Run GUARD-IMPLEMENTATION/continuation_01/run_original_against_v2.py:
  original-against-v2.log, 41 tests pass. Run test_compile_admission.py:
  author-regressions.log, 70 tests pass. Both harnesses were inspected first.
- Run independent_schema_check.py: independent-schema-results.json, 24 cases
  match independently specified expectations. Fake files and live-capability
  blockers are applied; no compiler executable is invoked.
- Read complete provider witness/controllers and exact v1/v2 and v2/v3 diffs;
  parse raw/portable event/controller/registry/job/latch records. Run
  check_live_evidence.py: LIVE_CHECKS.json, all checks pass. Runtime path is
  resolved from existing TMPDIR and RUNTIME_BINDING; reads only. It hashes
  83 original files and portable copies without printing personal paths or
  querying process state. No process/provider method is called.
- Run reproduce_stopped_cleanup.py: stopped-cleanup-results.json reproduces
  TimeoutExpired and skipped sentinel/persistence using only the v2 finalizer
  AST and fake objects. No controller import/main/live function is executed.
- Run ROOT-GUARD-QUALIFICATION/continuation_01/test_cleanup.py after inspecting
  it and v3: controller-v3-tests.log, five tests pass. Run
  check_repaired_cleanup.py: repaired-cleanup-results.json, same finalizer path
  now reaches cleanup/persistence in both ordinary stopped and persistent-wait
  failure variants, using only actual AST and fake objects.
- Read-only Git: `git diff --stat`, `git diff --name-status`, `git diff --binary`,
  `git show <candidate>:<path>` for fe6ca966..888e3888; graph diff inspected in
  full. FINAL_SCOPE.json binds full SHAs, diff hashes and all 181 candidate
  blobs. Their current working bytes match. No whole diff copy retained.
- Standard-library incremental checks: read new SHA256SUMS from containing
  directory (repository-root entries resolved as such), sha256 every target,
  json.loads for JSON/each JSONL line, ast.parse for Python, tomllib for Cargo
  manifest/lock. INCREMENTAL_CHECKS.json: all 169 entries in nine manifests
  match; 98 JSON/JSONL, 15 Python, two TOML parse. A0 24/880/UNRUN and exact
  lock inventory verify. K0 overlay/preimage/append/postimage/patch hashes and
  126 proposed-row count verify against product Git bytes without applying.
- Initial guessed test_controller_cleanup.py path was absent; corrected through
  rg --files to test_cleanup.py before execution. No failed read was a pass.

Checks of stored provider/root-resolution outcomes are independent file and
source inspection, not reexecution of ROOT's native work. Review claim scope
and residual limitations are in REVIEW.md. No A0 numerical oracle generation,
compiler/model, K0 witness, network, install, Git/index mutation or delegation
was performed. Root/project/TASK/selected skill bodies are retained from the
initial review and hash-checked unchanged in CONTEXT.json.
