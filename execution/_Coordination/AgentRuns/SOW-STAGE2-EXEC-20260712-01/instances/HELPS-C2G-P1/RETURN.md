# HELPS-C2G-P1 Evidence Portability Return

Verdict: `PASS`
Role: `HELPS_HUMANS` (Agent 1)
Node: `C2G-P1`
Recorded: `2026-07-13`

## Basis and disposition

This run applied only the non-semantic evidence-portability substitutions
authorized by `C2G-EVIDENCE-PORTABILITY-001`, including clerical scope
correction 001-A and temporary-prefix clarification 001-B. The accepted basis
remains D-GOV-16, P2_CONSUMERS C2F-R2 PASS, and PR #221 source head
`42c347ad8e75d95ea4605868463a0380f682d69f`.

The initial pre-edit inventory found exactly twelve prefix-bearing evidence
files and 97 occurrences of
`/Users/ryan/ai-env/projects/chirality`. The initial amendment placed
`FINAL_PREMERGE_CHECK_RESULTS.json` under C2A rather than C2A-R1; no evidence
was edited until the parent recorded scope correction 001-A. After the 97
authorized substitutions, the focused harness exposed 14 occurrences of the
distinct temporary prefix
`/var/folders/0s/50y7rb796d1bqdxmpcz6qg800000gn/T` in four already-scoped
JSON files. No second substitution occurred until the parent recorded
clarification 001-B.

Final occurrence counts:

- checkout prefix: `97 before / 0 after`;
- temporary prefix: `14 before / 0 after`;
- changed evidence files: `12`, exactly the sealed set below.

## Exact changed evidence paths

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

The manager also wrote only this return and its sibling `STATUS.json`. The
parent-owned amendment and work-graph edits were present concurrently and are
not manager-authored evidence repairs.

## Hash binding and semantic containment

- `git grep -n -F -f /tmp/helps-c2g-p1-pre-edit-hashes.txt -- .` found no
  tracked reference to any of the twelve pre-edit SHA-256 values.
- Direct-path searches found no reference to the twelve files in
  `snapshots/P2_CONSUMERS` or `instances/CHANGE-C2G`.
- `snapshots/P2_CONSUMERS/MANIFEST.tsv` binds the App caller manifest and App
  handoff, not any of these twelve files.
- For every evidence file, transforming its `HEAD` bytes with only the two
  authorized literal substitutions produced a byte-for-byte match with the
  working file (`cmp` PASS).
- All changed JSON files parse with `python3 -m json.tool`.

Accordingly, no check verdict, test count, source claim, authority binding,
lifecycle state, or evidence meaning changed. This is derivative-evidence
portability normalization only.

## Commands and results

- Prefix inventory with `rg -l/-o --fixed-strings`: exactly `12` files and
  `97` checkout-prefix occurrences before editing; `0` after.
- Temporary-prefix inventory with `rg -o --fixed-strings`: exactly `14`
  occurrences across the four 001-B files before editing; `0` after.
- Focused anchors:
  `python3 -m pytest tools/practitioner_harness/test_live_baseline.py::test_live_self_check_severity_totals_are_recorded_loop_anchors tools/practitioner_harness/test_live_baseline.py::test_live_gen8_abs_path_24_file_baseline -q`
  — `2 passed in 9.95s`.
- Full harness: `python3 -m pytest tools/practitioner_harness -q` —
  `264 passed in 65.59s`.
- Direct self-check: no refusal; `REVIEW=27`, `INFO=15`, `WARN=6`,
  `NOT_APPLICABLE=2`; GEN8 file count `24`.
- Exact substitution-equivalence comparison against `HEAD`: `PASS` for all
  twelve files.
- JSON parse validation: `PASS`.
- Scoped `git diff --check` over the twelve evidence files: `PASS`.

## Closure and handoff

Blockers, waivers, and material unknowns: none.

Rerun this repair validation if either normalized literal reappears in either
App run root, any of the twelve files changes before integration, a downstream
hash binding is introduced, the live self-check/GEN8 baseline moves, or the
PR source head changes. The next lawful owner is `CHANGE-C2G`, which may add
the authorized additive portability commit and resume PR #221 checks and
merge gates. This return authorizes no source, lifecycle, H1/H2, release, or
retirement action.
