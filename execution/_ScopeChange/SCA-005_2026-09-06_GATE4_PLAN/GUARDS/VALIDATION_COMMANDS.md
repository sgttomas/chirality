# Commands for implementation acceptance

Run from repository root. Capture command, exit, stdout/stderr and exact code/config basis in the implementation return. Negative cases in ACCEPTANCE_CHECKS.csv require isolated fixture mutations, never mutation of live accepted authority.

```sh
python3 -m pytest -q tools/validation/test_validate_root_materialization_fence.py tools/validation/test_validate_root_harness_adapter.py tools/validation/test_validate_root_surface_ownership.py tools/validation/test_validate_root_work_graph_dispatch.py tools/validation/test_validate_instruction_tranche_manifest.py
python3 -m pytest -q tools/practitioner_harness
python3 tools/validation/validate_root_materialization_fence.py
python3 tools/validation/validate_root_harness_adapter.py
python3 tools/validation/validate_root_surface_ownership.py
python3 tools/validation/validate_root_work_graph_dispatch.py
python3 tools/validation/validate_instruction_tranche_manifest.py
python3 tools/validation/validate_instruction_entrypoints.py
python3 tools/validation/validate_candidate_whitespace.py --base-ref origin/main
python3 tools/practitioner_harness/harness.py status --project root
python3 tools/practitioner_harness/harness.py drift --project root
python3 tools/practitioner_harness/harness.py self-check
python3 tools/run_affected_tests.py --base origin/main
```

Include new helper/parser test paths in direct pytest command if created; practitioner directory command already discovers its new tests. After the candidate commit exists, run:

```sh
python3 tools/validation/validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only
```

G3's existing dispatch CLI is `python3 tools/validation/validate_root_work_graph_dispatch.py --work-graph PATH --brief PATH` with repeatable brief. Use exact implementation fixture graph and actual governed brief paths, recording them instead of leaving placeholders. G0-G2 expose check(root) for temporary fixture roots; avoid proposed unsupported CLI flags. Runtime lane runs existing project registry tests using its ordinary package scripts and an isolated scratch runtime directory; host/account registration is not a test target.

Required new-tool fixture command after implementation: `python3 -m pytest -q tools/validation/test_apply_root_retirement.py`. Run its no-write dry-run before any source retirement; the proposed CLI and acceptance checks are specified in REPORT.md. This planning packet does not claim the tool exists.
