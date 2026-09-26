# D-PEC-96 A — Loop-Registry Schema v2 Act Validation

All commands ran in worktree `agent-a250ffe27d6b8a45c` on branch
`claude/pec-d96-registry-act`, which was cut from `origin/main` `f90320c1d`. Each ran with
`PYTHONDONTWRITEBYTECODE=1` and the interpreter
`/Library/Frameworks/Python.framework/Versions/3.13/bin/python3` (CPython 3.13.7,
first `python3` on `PATH`, so it is also the interpreter that
`run_registered_checks.py` spawns). The local date was 2026-09-26 (MDT). Registered checks ran from
the repository root through `tools/software_workflow/run_registered_checks.py`
(`665a4ac1…c766`), which runs each at its registered cwd (`projects/pec`, or
`.` for `harness-self-check`). `checks/COMMANDS.txt` lists every command in order, with its cwd
and exit code. Each output is the file named in the table.

Three baselines exist:
- `pristine_*` ran in the clean worktree at `f90320c1d` before the run root existed.
- `pre_*` ran after the run root and the scripts were added, before the act.
- `post_*` ran after the act.

`pristine_harness.out`, `pre_harness.out` and `post_harness.out` are byte-identical. So are
`pristine_strict.out`, `pre_strict.out` and `post_strict.out`.

## Preconditions

| Check | Result |
|---|---|
| Fetched `origin/main` is `f90320c1d110cad75d04c96c91a595b7eb244498` (PR #946). It contains `D-PEC-96_RULING_2026-09-26.md` (`852057f0…399e`, the same bytes via `git show origin/main:`) and exactly one register row `D-PEC-96 … RULED A / EFFECTIVE ON MERGE` | holds |
| Branch cut from fresh `origin/main` in an isolated worktree | `claude/pec-d96-registry-act` at `f90320c1d` |
| Brief hash | `e9dadc1a…4594` verified |
| Proposal and bound-script hashes | proposal `4506597b…180e`; `apply_d96.py` `80725b4f…bbf3`; `mutate_d96.py` `57c2f031…26f0`; the run-root copies are `cmp`-identical to the preparation copies |
| Reliance-hold preflight, `dispatch-for-production`, 13 targets (the 11 product paths, DEL-01-06 `MEMORY.md` and the run root), before the act | 13/13 `{"status": "ALLOW"}`, exit 0 (`checks/hold_dispatch-for-production.tsv`, targets in `checks/hold_targets.txt`). `ACTIVE_RELIANCE_HOLDS.csv` (`f877d931…41cbc`) has a header and no rows. Script `b1712e4b…cd0e` |
| Reliance-hold preflight, `rely-for-production`, the same 13 targets, before fan-in | 13/13 `ALLOW`, exit 0 (`checks/hold_rely-for-production.tsv`) |
| Preimages and must-remain files | The script's own fail-closed checks passed in `--check-only` and in the act: 10 preimages and 1 absent path as tabled, 6 must-remain files UNCHANGED |

## Finite verification (proposal table)

| Check | Required | Observed | Output |
|---|---|---|---|
| Selection | exactly `harness-self-check`, `v2-api-contract`, `v2-core-posture`, `v2-loop-registry`, `v2-store-guard` | exactly those five, exit 0 | `checks/selection.out` |
| **`v2-loop-registry`** (VER-001, VER-003 rerun) | exit 0; Ran 19, OK (12 before) | exit 0; **Ran 19, OK** (pre: Ran 12, OK) | `checks/post_v2-loop-registry.json`, verbose `checks/post_loop_registry_verbose.out` (pre in `pre_*`) |
| `v2-store-guard` | exit 0; Ran 13, OK | exit 0; Ran 13, OK (pre the same) | `checks/post_v2-store-guard.json` |
| `v2-core-posture` | exit 0; PASS, 0 findings; `core_tree_sha256` `88f590c0…c016` → `dd7e1dda…6e5a`; config and workflow hashes unchanged | exit 0; `"verdict": "PASS"`, `findings: []`, assertions dependency/locality/registration PASS; core tree `88f590c019eb67febfbb569a34ec688831edc7e867f251376ecebe3f7799c016` → `dd7e1ddaddb269525e45699158e31e5a9ce6d252dab27b14ce59c5b2ad9e6e5a`; config `20d64ff3…09ed` and workflow `8ec9ba6d…a58b` unchanged | `checks/pre_v2-core-posture.json`, `checks/post_v2-core-posture.json` |
| DEL-01-05 enforcement tests | exit 0; Ran 28, OK | exit 0; Ran 28, OK before and after (outputs differ only in elapsed time) | `checks/pre_enforcement.out`, `checks/post_enforcement.out` |
| `v2-api-contract` | exit 0; Ran 6, OK | exit 0; Ran 6, OK (pre the same) | `checks/post_v2-api-contract.json` |
| `harness-self-check` | exit 0; output identical to the pre-act run | exit 0 before and after. Direct runs are byte-identical: `pristine_`, `pre_` and `post_harness.out` all `8856b78faa658f6d2ee1a6b762dadcf26ce61c2498d2c462c7ad93904ed870fe`, with `INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=126`. The registered-check runs also pass. The proposal's prototype figure (`WARN=124`, stdout `e5f9ff70…d110`) was taken at `8f9bd314c`. `origin/main` has moved since then, and the requirement is identity with this act's own pre-act run, which holds | `checks/*_harness.out`, `checks/*_harness-self-check.json` |
| Receipts validator | exit 0; output unchanged | exit 0; `pre_` and `post_receipts.out` byte-identical (`087c6e54…1558`): "frozen through Receipt-166; versioned receipt contract satisfied" | `checks/pre_receipts.out`, `checks/post_receipts.out` |
| Mutation evidence | baseline passes; M1–M19 each CAUGHT, none `NOT_APPLIED`; `TOTAL 19/19 CAUGHT`; `RESULT PASS` | `BASELINE exit=0`; M1–M19 each `CAUGHT (exit=1)`; no `NOT_APPLIED`; **`TOTAL 19/19 CAUGHT`**; **`RESULT PASS`**; runner exit 0 | `checks/mutate_d96.out` |
| Byte identity | SHA-256 of the 11 paths equals the grant table | 11/11 `OK` against the grant's postimage column. All 11 are also `cmp`-identical to `PEC_REGISTRY_D96_PREP_2026-09-25/postimages/optionA_v2/`. Path-list hash `b5db12e5…c73c`. Must-remain hashes unchanged | `checks/byte_identity.out`, `checks/grant_postimages.txt` |
| Basis citations | `test -f` on each `basis` and `loop_init_path` | 4/4 PRESENT (the D-PEC-94 record twice, `projects/pec/AGENTS.md`, `projects/pec/loop/LOOP_INIT.md`) | `checks/basis_citations.out` |
| Containment | `git diff --name-status origin/main...HEAD` shows the 11 paths, the run root and `MEMORY.md`, and nothing else | At `dd63560a7`: 66 changed paths, namely 11 PRODUCT (10 M, 1 A, each with its granted act), 54 RUN_ROOT, 1 MEMORY (A), 0 outside; `RESULT CONTAINED`. The final rerun at the PR head is recorded in `HANDOFF_STATE.md` | `checks/containment_name_status.txt`, `checks/containment.out` (`containment.py`) |
| Whitespace and encoding | `git diff --check origin/main...HEAD` clean; 0 non-ASCII bytes in the 11 postimages | `git diff --check` exit 0, no output (at `dd63560a7`, printed to the terminal and indexed in `COMMANDS.txt`); non-ASCII 0 in each of the 11 | `checks/non_ascii.out` |
| Vocabulary scan (verifier item 4) | no `remaining` in `v2/` | `grep -rniE remaining v2/` exit 1, no match | `checks/grep_remaining.out` |

### Strict register validator (basis note)

Root D-GOV-48 (PR #942) makes `validate_decomposition_registers.py --strict
projects/pec/execution` report 26 pre-existing `XRG-013` warnings on PEC, and
the validator exits 1 under `--strict`. This act touches no register. The
requirement is identical output before and after, with no new finding.

- It exited 1 in all three phases, with 0 errors and 26 warnings, all `XRG-013`.
- `pristine_strict.out`, `pre_strict.out` and `post_strict.out` are byte-identical
  (`0aa450c52a2bef4c78ae140887961ba4a632a98223e5c4f26afdee03ee87e905`).
- There is no new finding.

The proposal's prototype figure ("0 errors / 0 warnings", exit 0) predates D-GOV-48.

### `v2-loop-registry` tests mapped to DEL-01-06 verification methods

The 19 tests are those in `checks/post_loop_registry_verbose.out`, all `ok`. The mapping is the proposal's.

| Method | Tests |
|---|---|
| VER-001 format against the default and malformed fixtures | `test_schema_documents_every_field_and_the_exact_default`, `test_checked_in_default_has_exactly_the_pec_loop`, `test_schema_version_1_is_rejected_with_location`, `test_missing_loop_id_is_rejected_with_location`, `test_duplicate_loop_id_is_rejected_with_location`, `test_malformed_json_is_rejected_with_line_and_column`, `test_invalid_feed_profiles_are_rejected_with_location`, `test_shipped_vocabulary_surfaces_are_pairwise_disjoint`, `test_overlapping_profiles_are_rejected_with_location`, `test_failures_do_not_echo_document_values` |
| VER-002 one loop at P1; more by entries only | `test_checked_in_default_has_exactly_the_pec_loop`, `test_additional_loops_need_entries_only` |
| VER-003 invalid, unreadable and absent fail explicitly, with no partial set | `test_absent_file_is_rejected_explicitly`, `test_unreadable_path_is_rejected_explicitly`, `test_invalid_document_never_returns_partial_or_empty_set`, `test_malformed_json_is_rejected_with_line_and_column` |
| VER-004 consumer interface carries no path or serialization detail | `test_port_has_only_the_typed_capability_method`, `test_registered_loop_is_immutable`, `test_registered_loop_carries_the_typed_feed_profile_field` |
| VER-005 no third-party dependency or network call | `test_core_imports_no_adapter_or_outer_io_module`, `test_implementation_uses_only_stdlib_and_no_network_module`, plus `v2-core-posture` and `v2/tests/enforcement` |
| VER-006 the suite runs and passes | `v2-loop-registry` |

## Checks not run, with reason

- Decomposition and dependency validators as gates: no register,
  decomposition or dependency file changed. The strict validator ran anyway
  as a before/after identity check (above).
- Task Management and instruction-entrypoint validators: no Task Management,
  launcher, init or posture surface changed.
- Kill test and parity diff: not applicable. No runtime capability exists or
  changed; this is a configuration, adapter and test slice with no consumer.

## Operator notes (disclosed)

- **Selection first run.** `select_affected_checks.py` was first called with
  repository-relative paths (`projects/pec/v2/...`). The profile's path rules
  are project-relative, so that call selected only the three `always_checks`.
  That output is kept as `checks/selection_repo_relative_paths_WRONG_FORM.out`.
  It was rerun with the project-relative paths the proposal tables, which
  selected all five (`checks/selection.out`). `post_checks.sh` was corrected
  to match. No product byte was involved.
- **Registered-check output location.** `run_registered_checks.py` requires
  `--output` inside the workspace, so a first attempt that wrote to the
  session scratchpad failed with a `ValueError` before any check ran. The
  `pre_` phase was then run with outputs in this run root.
- **Absolute paths.** `checks/COMMANDS.txt`, the registered-check JSON
  and the receipts output carry this worktree's absolute path. They are raw
  tool evidence and are kept unnormalized.

## Not claimed

No CHECKING, ISSUED, acceptance, readiness or reliance claim. No lifecycle
change, DEL-01-06 Gate 5 act or `_STATUS.md` write. Git closeout is
source-control hygiene, not lifecycle issuance. Independent verification is
recorded in `VERIFIER_VERDICT_NN.md`.
