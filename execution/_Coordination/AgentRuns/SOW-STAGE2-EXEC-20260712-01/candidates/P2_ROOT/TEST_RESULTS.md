# C2R Test Results

Verdict: `PASS`
Basis: `main@e150c972889d05a8fc270239451a35c7512dc9a9`

## C2R-R3 checklist raw-authority refresh

| Check | Exact command | Exit | Result |
|---|---|---:|---|
| Focused regressions | `python3 -m pytest tools/scope_of_work/test_scope_of_work_tools.py tools/reporting/test_generate_coverage_csv.py -q` | 0 | 19 passed |
| Full root tool suite | `python3 -m pytest tools/ -q` | 0 | 792 passed |
| Python compile | `python3 -m py_compile tools/scope_of_work/derive_review_checklist.py tools/scope_of_work/test_scope_of_work_tools.py` | 0 | PASS |
| Diff hygiene | `git diff --check` | 0 | PASS |
| Repair containment | caller-manifest hash comparison and write-scope inspection | 0 | two authorized checklist source/test paths plus P2_ROOT and HELPS-C2R-R3 evidence |

The end-to-end regression keeps the candidate marker exact, supplies leading
or trailing whitespace only on the CLI authority, and proves nonzero exit with
no requested output. Exact dual and SOW-only runs remain byte-stable with
identical item ordering, text, and linkage.

## C2R-R2 whitespace fail-closed refresh

| Check | Exact command | Exit | Result |
|---|---|---:|---|
| Focused exact-authority, whitespace, and ISSUED binding regressions | `python3 -m pytest tools/scope_of_work/test_scope_of_work_tools.py tools/reporting/test_generate_coverage_csv.py -q` | 0 | 18 passed |
| Full root tool suite | `python3 -m pytest tools/ -q` | 0 | 791 passed |
| Python compile | `python3 -m py_compile tools/scope_of_work/common.py tools/scope_of_work/convert_four_documents_to_scope_of_work.py tools/scope_of_work/test_scope_of_work_tools.py` | 0 | PASS |
| Diff hygiene | `git diff --check` | 0 | PASS |
| Repair containment | exact C2R-R1 baseline reconstruction and write-scope comparison | 0 | three authorized source/test paths plus P2_ROOT and HELPS-C2R-R2 evidence; no project, domain, deliverable, lifecycle, Git, release, H1/H2, or retirement action |

The added regression keeps the candidate marker equal to the exact ruled
token while supplying either a leading-space or trailing-tab authority.
Resolver selection fails as `AMBIGUOUS`, converter execution refuses the
input and writes no `ScopeOfWork.md`, and exact unpadded behavior remains
green. The C2R-R1 unruled-authority and ISSUED binding coverage is retained.

## C2R-R1 remediation refresh

| Check | Exact command | Exit | Result |
|---|---|---:|---|
| Focused exact-authority and ISSUED binding regressions | `python3 -m pytest tools/scope_of_work/test_scope_of_work_tools.py tools/reporting/test_generate_coverage_csv.py -q` | 0 | 17 passed |
| Full root tool suite | `python3 -m pytest tools/ -q` | 0 | 790 passed |
| Python compile | `python3 -m py_compile tools/scope_of_work/common.py tools/scope_of_work/convert_four_documents_to_scope_of_work.py tools/scope_of_work/test_scope_of_work_tools.py tools/reporting/test_generate_coverage_csv.py` | 0 | PASS |
| Diff hygiene | `git diff --check` | 0 | PASS |
| Repair containment | exact write-scope comparison | 0 | four authorized source/test paths plus P2_ROOT and HELPS-C2R-R1 evidence; no skill-schema, project, domain, deliverable, lifecycle, Git, release, H1/H2, or retirement action |

The focused suite proves the ruled authority succeeds only in isolated dual
mode; unruled syntactic tokens, another valid-looking SHA, malformed/missing
authority, non-isolated mode, and mismatched markers fail closed. It also
proves ISSUED preparation rejects missing or unsafe accepted-basis values,
embeds every required binding exactly, and preserves `_STATUS.md` bytes.
Scope clarification 001-A authorized the reporting fixture's exact-token
refresh after it was identified as a full-suite dependency.

## Initial C2R evidence retained

| Check | Exact command | Exit | Result |
|---|---|---:|---|
| Focused resolver/reporting/semantic tests | `python3 -m pytest tools/scope_of_work/test_scope_of_work_tools.py tools/reporting/test_generate_coverage_csv.py tools/validation/test_semantic_artifact_validators.py -q` | 0 | 30 passed |
| Full root tool suite | `python3 -m pytest tools/ -q` | 0 | 788 passed |
| Agent contracts | `python3 tools/validation/validate_agent_instructions.py agents/AGENT_*.md --repo-root .` | 0 | 33 files, 0 errors, 0 warnings |
| Skill contracts | `python3 tools/validation/validate_skill_metadata.py skills` | 0 | 44 valid, 0 invalid |
| Practitioner compatibility | `python3 -m pytest tools/practitioner_harness/test_prose_bullet_v1.py tools/practitioner_harness/test_write_status_guard.py -q` | 0 | 51 passed |
| Public export profile | `python3 -m pytest tools/validation/test_public_export_profile.py -q` | 0 | 1 passed |
| Instruction entrypoints | `python3 tools/validation/validate_instruction_entrypoints.py` | 0 | PASS |
| Path anchors | `python3 tools/validation/validate_path_anchors.py . --text` | 0 | 447 surfaces, no literal home path |
| Python compile | `python3 -m py_compile <changed Python callers>` | 0 | PASS |
| Shell syntax | `bash -n tools/evaluation/count_deliverable_files.sh` | 0 | PASS |
| Diff hygiene | `git diff --check` | 0 | PASS |
| Containment/caller census | manager Python comparison of HEAD diff to P0 exact rows | 0 | 64/64 rows; 48 C2R tracked paths; 0 extra; 0 project/domain paths |

The initial C2R first full-suite attempt exited 2 during collection because a generic Python `common` import resolved to the software-workflow module. C2R isolated the Scope-of-Work import under a unique module name and reran the focused and full suites successfully. This corrected historical failure is retained as execution evidence, not omitted.

The export manifest was regenerated from accepted sources by loading `exports/chirality-app/export_public.py`, building a transient stage inside `candidates/P2_ROOT/`, and invoking its governed `write_manifest`; result: 610 rows, zero sanitizations. The transient stage was removed automatically. No export report, tracked staging tree, or external target was written.
