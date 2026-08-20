# Return — Root Governance CI Fix

- Executor: ephemeral Agent 2 generalist
- Parent: `HELP_HUMAN` via `HELPS_HUMANS`
- Status: implementation complete; verification passed
- Scope: root governance CI only; no writes under `projects/**`
- Next lawful owner: `CHANGE` for Git state, review, push, and PR operations

## Evidence basis

The observed failure began when the GitHub-hosted runner changed from Git
2.54.0 to 2.55.0 on 2026-08-19 between 15:05Z and 19:52Z. Run `32267168751`
was the last green main run on 2.54.0. Runs `32295433879` attempt 1 and
`32304190391` attempt 2 ran on 2.55.0 and each reported `5 failed, 655 passed`
from different tests and fixture templates. Two of three full-suite executions
on 2.55.0 failed, so a single green rerun is not treated as proof.

The defect was a race between Git's detached automatic maintenance and the
session template cache copying a just-committed fixture repository. The fix
restores the required invariant: fixture repositories are quiescent before
`harness_template_cache` copies them.

The workflow repair also addresses the independent zsh-install hangs in runs
`32295433879` attempt 2 and `32304190391` attempt 1.

## Changed files

- `.github/workflows/governance-harness.yml`
  - adds a 15-minute harness-job timeout;
  - reuses the canonical Ubuntu source step from
    `.github/workflows/piping-desktop-e2e.yml` verbatim before apt; and
  - adds a 3-minute timeout to the zsh-install step.
- `tools/practitioner_harness/conftest.py`
  - injects `maintenance.auto=false`, `gc.auto=0`, and
    `gc.autoDetach=false` by appending to Git's process environment before
    test collection/build activity, preserving caller-provided process config
    while covering helper-wrapped and raw Git subprocesses in every fixture
    builder.
- `tools/practitioner_harness/test_fixture_git_config.py`
  - deterministically asserts all three effective settings in the built cache
    template after init and after commit, then again in its materialized copy.
- `execution/_Coordination/AgentRuns/HELP-HUMAN-ROOT-20260819-GOVERNANCE-CI-FIX/RETURN.md`
  - this root-homed handoff record.

## Fixture Git path inventory

All existing fixture init/commit paths under `tools/practitioner_harness/`
inherit the process-level Git configuration:

- `test_abs_path_lint_fixtures.py`
  - `test_gitignored_build_output_is_not_audited`: init and base commit.
- `test_brief_adoption.py`
  - `build_adoption_repo`: init and base commit;
  - `_add_brief`: subsequent brief commits; and
  - `test_adopted_committed_matched_actor_activates_fence`: subsequent
    unrelated commit.
- `test_coord_check.py`
  - `_repo`: init and base commit; and
  - coord-check cases: subsequent packet, change-prep, anchor, run-record, and
    removal commits through the shared `_git` helper.
- `test_drift_fixtures.py`
  - `test_drift_approval_sha_reachable_and_unreachable`: init and seed commit.
- `test_readonly_guarantee.py`
  - readonly mutation case: subsequent in-fence commit on a repo produced by
    `build_run_repo`.
- `test_run_validations.py`
  - `build_run_repo._build`: cached-template init and base commit.
- `test_scope_evidence_closeout.py`
  - `_commit_file` plus the move-into-fence, external-evidence-target, and
    root-adapter cases: subsequent commits on repos produced by
    `build_run_repo`.
- `test_surface_roles.py`
  - `test_raw_evidence_attributes_preserve_diff_check_boundary`: raw
    subprocess init and base commit; and
  - `test_untracked_active_managed_control_is_checked_before_commit`: raw
    subprocess init and base commit.
- `test_write_status_guard.py`
  - `make_repo`: init and base commit; and
  - ampersand-ruling case: subsequent commit.

`test_self_check_fixtures.py::build_mini_repo` is also a cached template
builder. It does not initialize Git itself, but callers that initialize and
commit its materialized copies are included above.

## Verification

- Focused cache/config regression:
  - `python3 -m pytest -q tools/practitioner_harness/test_fixture_git_config.py`
  - PASS: `1 passed`.
- Pre-existing process-config composition:
  - imported the suite conftest with one caller-provided `GIT_CONFIG` entry;
  - PASS: the caller entry remained at index 0 and the three fixture
    quiescence entries were appended at indices 1 through 3.
- Focused cache-heavy and Git-fixture tests:
  - `python3 -m pytest -q tools/practitioner_harness/test_fixture_git_config.py tools/practitioner_harness/test_run_validations.py tools/practitioner_harness/test_brief_adoption.py tools/practitioner_harness/test_write_status_guard.py`
  - PASS: `79 passed`.
- Full practitioner-harness suite with xdist:
  - `python3 -m pytest -q -n auto --dist loadscope tools/practitioner_harness`
  - PASS: `350 passed`.
- Workflow YAML/static checks:
  - PyYAML parse passed;
  - job timeout is 15 minutes;
  - canonical source step precedes zsh install;
  - zsh step timeout is 3 minutes; and
  - extracted source block is byte-identical to the Piping workflow block.
- Root self-check:
  - `python3 tools/practitioner_harness/harness.py self-check`
  - PASS (exit 0). Existing non-blocking findings remain outside this tranche:
    `REVIEW=4`, `WARN=31`, `INFO=14`, `NOT_APPLICABLE=1`.
- `git diff --check`: PASS.

## Residual blockers and reruns

- No implementation blocker remains.
- Hosted Git 2.55 CI remains the external integration proof surface. Its
  result should supplement, not replace, the deterministic config regression.
- No commit, push, PR, or merge operation was performed by this executor.
