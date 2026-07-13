# P-F Evidence Portability Amendment 001

Status: `ACTIVE — NON-SEMANTIC EVIDENCE REPAIR`

## Trigger and classification

RECON-PF independently passed every substantive pilot gate but blocked P-G as
`PF-PORT-001`: the literal checkout prefix
`/Users/ryan/ai-env/projects/chirality/` appears 46 times across 17 derivative
child evidence files. Accepted evidence accounts for 42 occurrences in 16
files; the preserved unaccepted App DEL-07-01 substrate attempt accounts for
four occurrences in one file. The literal `/var/folders/` count is zero.

This is evidence portability only. It does not change a candidate, source,
status, lifecycle, mapping, parity result, checklist, render, verdict,
replacement/rollback action, authority, risk, objective, ownership class,
integration gate, H1/H2 posture, or accepted project truth. No human ruling is
required. The original terminal BLOCKED P4 preintegration package remains
unchanged; the clean rerun will write `preintegration-r1`.

## Exact repair scope

Replace only `/Users/ryan/ai-env/projects/chirality/` with `~/` in these exact
files:

App accepted evidence (32 occurrences, 12 files):

1. `instances/WORKING-P-A/TASK-APP-DEL-07-01-R1/RETURN.md`
2. `instances/WORKING-P-A/TASK-APP-DEL-07-02/RETURN.md`
3. `instances/WORKING-P-A/TASK-APP-DEL-07-03/RETURN.md`
4. `instances/WORKING-P-A/TASK-APP-DEL-07-04/RETURN.md`
5. `instances/WORKING-P-A/TASK-APP-DEL-07-05/RETURN.md`
6. `instances/WORKING-P-A/TASK-APP-DEL-07-06/RETURN.md`
7. `instances/WORKING-P-A/TASK-APP-DEL-07-01-R1/workspace/target_state/_run_records/TASK_RUN_2026-07-13_0351.md`
8. `instances/WORKING-P-A/TASK-APP-DEL-07-02/workspace/target_state/_run_records/TASK_RUN_2026-07-13_0400.md`
9. `instances/WORKING-P-A/TASK-APP-DEL-07-03/workspace/target_state/_run_records/TASK_RUN_2026-07-13_0402.md`
10. `instances/WORKING-P-A/TASK-APP-DEL-07-04/workspace/target_state/_run_records/TASK_RUN_2026-07-13_0408.md`
11. `instances/WORKING-P-A/TASK-APP-DEL-07-05/workspace/target_state/_run_records/TASK_RUN_2026-07-13_0412.md`
12. `instances/WORKING-P-A/TASK-APP-DEL-07-06/workspace/target_state/_run_records/TASK_RUN_2026-07-13_0417.md`

App preserved failed evidence (4 occurrences, one file):

13. `instances/WORKING-P-A/TASK-APP-DEL-07-01/workspace/target_state/_run_records/TASK_RUN_2026-07-13_0339.md`

Piping accepted evidence (10 occurrences, four files):

14. `instances/WORKING-P-P/children/TASK-PIP-13-01/workspace/_run_records/TASK_RUN_2026-07-13_0432.md`
15. `instances/WORKING-P-P/children/TASK-PIP-13-02/workspace/_run_records/TASK_RUN_2026-07-13_0432.md`
16. `instances/WORKING-P-P/children/TASK-PIP-13-03/workspace/_run_records/TASK_RUN_workspace_2026-07-13_0440.md`
17. `instances/WORKING-P-P/children/TASK-PIP-13-04/workspace/_run_records/TASK_RUN_2026-07-13_0441.md`

Paths are relative to
`execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/`.

## Owning-lane repair and rerun gates

`WORKING-P-A-R1` owns App files 1–13; `WORKING-P-P-R1` owns Piping files
14–17. Each manager must:

1. prove the exact pre-edit path and occurrence inventory;
2. apply only the literal substitution;
3. prove byte equivalence to the preimage under that substitution;
4. find and refresh only direct package-local hashes or summary bindings that
   name changed files, recording every refreshed surface;
5. preserve the failed App attempt as unaccepted and preserve all accepted
   child/package verdicts and substantive counts;
6. prove both checkout and temp-prefix counts are zero in its full package
   evidence root; validate JSON/CSV/TSV/Markdown structure as applicable;
7. rerun package hash/path/diff/containment checks and write a terminal repair
   return without rerunning substantive conversion or verifier reasoning.

Any candidate/source/status/project change, different substitution, semantic
delta, unexplained hash binding, new prefix, or required write outside package
evidence is a blocker. No Git, project, lifecycle, H1/H2, ISSUED, integration,
release, or retirement action is authorized.

After both repair lanes PASS, RECON-PF-R1 must repeat the complete sealed P-F
fan-in—not only portability—and write a new candidate under
`snapshots/P4_PILOTS/preintegration-r1/`. P-G remains parked until parent
accepts that rerun.
