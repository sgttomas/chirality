# C2G Evidence Portability Amendment 001

Status: `ACTIVE — NON-CONSEQUENTIAL EVIDENCE REPAIR`

## Trigger

PR #221's `governance-harness` check failed after the accepted C2 source and
evidence packages were pushed. Ten newly tracked App project-run evidence
files expose the checkout-specific prefix
`/Users/ryan/ai-env/projects/chirality`, increasing the live GEN8
`ABS_PATH_IN_PROJECT_SURFACE` inventory from the accepted 24-item baseline to
34 and the REVIEW self-check total from 27 to 37. Two additional run-record
files in the same sealed App evidence packages contain the same prefix even
though GEN8 excludes those paths.

## Disposition

This amendment does not change source behavior, authority, objective, risk,
ownership, lifecycle meaning, acceptance criteria, check verdicts, test
counts, or the P2_CONSUMERS source-hash basis. It repairs derivative evidence
portability before C2G integration. No new human ruling is required.

`HELPS-C2G-P1` is authorized to replace only the literal checkout prefix
`/Users/ryan/ai-env/projects/chirality` with the repository-neutral harness
form `~` in the following twelve already-tracked evidence files:

1. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A-R1/FINAL_PREMERGE_CHECK_RESULTS.json`
2. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A/instances/TASK-SW-REVIEW/RETURN.md`
3. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A-R1/FINAL_AFFECTED_CHECK_RESULTS.json`
4. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A-R1/POST_REVIEW_CHECK_RESULTS.json`
5. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A-R1/REGISTERED_CHECK_RESULTS.json`
6. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A-R1/ADDITIONAL_CHECK_RESULTS.json`
7. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A-R1/PREMERGE_CHECK_RESULTS.json`
8. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A-R1/instances/TASK-SW-REVIEW/RETURN.md`
9. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A/MANAGER_CHECK_RESULTS.json`
10. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A/PREMERGE_RERUN_RESULTS.json`
11. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A/instances/TASK-SW-IMPL/_run_records/TASK_RUN_2026-07-13_0058.md`
12. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A/instances/TASK-SW-REVIEW/_run_records/TASK_RUN_2026-07-13_0709.md`

No other substitution, regeneration, or evidence-content edit is authorized.
The manager must verify that the literal prefix is absent from both App run
roots, inspect for downstream hash bindings, run the local governance harness
and its live self-check/GEN8 anchors, and return exact changed-path and check
evidence. Any semantic delta or required edit outside these twelve files is a
blocker.

After `HELPS-C2G-P1` PASS, CHANGE may create one additive portability commit
containing the twelve evidence repairs plus this amendment, the sealed manager
brief/return/status, and the corresponding work-graph update. CHANGE must not
rewrite published history. It must push the existing PR branch, wait for all
required checks, and merge only on PASS under `HUMAN-STEER-001`.

Scope correction 001-A: the initial sealed list placed
`FINAL_PREMERGE_CHECK_RESULTS.json` under the C2A run root. The pre-edit
inventory proved that file does not exist there and that the actual twelfth
prefix-bearing file is the identically named result under C2A-R1. Item 1 is
corrected to that exact existing path before any evidence edit. The inventory
remains twelve files and 97 literal-prefix occurrences; no write-scope class,
criterion, or semantic authority changed.

Scope clarification 001-B: after the 97 checkout-prefix occurrences were
removed, the focused live anchors still reported four GEN8 findings. The
remaining cause is the distinct machine-temporary prefix
`/var/folders/0s/50y7rb796d1bqdxmpcz6qg800000gn/T`, present 14 times across
four files already inside the sealed twelve-file scope:

- C2A `MANAGER_CHECK_RESULTS.json` (2 occurrences);
- C2A `PREMERGE_RERUN_RESULTS.json` (4 occurrences);
- C2A-R1 `FINAL_PREMERGE_CHECK_RESULTS.json` (4 occurrences); and
- C2A-R1 `PREMERGE_CHECK_RESULTS.json` (4 occurrences).

`HELPS-C2G-P1` is authorized to replace only that exact temporary prefix with
`~` in those four files, then rerun the unchanged checks. No new path enters
scope and no verdict, count, source, authority, lifecycle, or evidence meaning
may change.

Evidence-format normalization 001-C: CHANGE-C2G's cached diff gate found one
terminal blank line in the parent-authored `HELPS-C2G-P1/LAUNCH_BRIEF.md`.
HELP_HUMAN authorized removal of only that EOF blank line before restaging.
No brief term, finding, verdict, source, hash, evidence claim, or acceptance
criterion changed.
