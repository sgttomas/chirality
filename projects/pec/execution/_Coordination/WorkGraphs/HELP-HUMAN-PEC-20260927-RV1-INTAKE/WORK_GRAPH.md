# Work graph — RV1 re-review, closeout intake dispositions and K3 row

This graph lives at `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260927-RV1-INTAKE/WORK_GRAPH.md`. It follows `projects/pec/loop/LOOP_INIT.md`, the shared method (`D-PEC-94`), and uses the method `chirality-root:bundled:workflow:construct-local-work-graph`.

## Intent and selected route

- **Stable run identity:** `HELP-HUMAN-PEC-20260927-RV1-INTAKE`.
- **Steering basis:** the owner's direction of 2026-09-27, verbatim in `../../_DECISIONS/D-PEC-107_OWNER_DIRECTION_2026-09-27.md`.
- **Intended result:**
  - the owner's intake dispositions are recorded in PEC Task Management;
  - CAND-03 is routed to Root;
  - K3 is tracked as a PEC Task Management row;
  - the RV1 REVIEW of the `D-PEC-105` bytes is done and brought to the owner for re-acceptance.
- **Carried in:** from `HELP-HUMAN-PEC-20260925-POST-SCA005` (its [receipt](../../AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/RECEIPT.md) names both): RV1, and K3, which leaves the graph as a Task Management row.
- **Freeze point:** by the owner's direction (`D-PEC-107` §Freeze point), PEC's state after PR #1014 is a freeze point for a later ground-up reassessment. No scope change is opened. The consumer-contract design, the next PEC scope change and re-reviews of DEL-04-01 and DEL-03-01 are recorded as considerations only. This graph holds only the directed, bounded TM1 and RV1 work, which the owner confirmed under the freeze ("Yes I still want you to complete the task management work and the RV1.").
- **Left out:** production. By owner direction, production happens in a different session. This graph prepares a production packet only if one becomes a dependency of something necessary here.
- **Completion:** every node below is COMPLETE, or CARRIED (named in the central receipt with its next home), or the owner has explicitly removed it. The closeout and the receipt are done; the DEL-00-01 and DEL-00-03 MEMORY rows are written under an owner grant, or the owner's decision to complete without them is recorded here; and the final PR is merged.

## Work

| ID / outcome | Deliverables and write scope (owner) | Needs / why | Completion check | State |
|---|---|---|---|---|
| DIR Direction record | `D-PEC-107` record and register row; this graph; STATUS under `D-PEC-88` (HELP_HUMAN) | The owner's direction | Merged | COMPLETE — merged as PR #1018 (`acc7d3cc7`) after reviews 01–03 (`../../AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/returns/REVIEW_PR1018_0{1,2,3}.md`) |
| TM1 Intake dispositions, K3 row, Root notice | `_Coordination/_TaskManagement/**` (dispositions of CAND-01/02/03; promoted rows for CAND-02 and CAND-03; a K3 row; the consumer-contract design item added to the CAND-02 row) and one Root coordination notice for CAND-03 (WORKING_ITEMS, `task-management`) | DIR | `taskmgmt validate` passes; each disposition cites `D-PEC-107` | COMPLETE — merged as PR #1021 (`56f7d4602`) after reviews 01–03 (`../../AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/returns/REVIEW_PR1021_0{1,2,3}.md`): CAND-01 disposition (b); TM-PEC-026 (CAND-02, OPEN); TM-PEC-027 (CAND-03, ELEVATED to Root, notice `execution/_Coordination/NOTICE_2026-09-27_PEC_HOSTED_CI_V2_CHECKS.md`); TM-PEC-028 (K3, DEFERRED); the MEMORY grant supplement `../../_DECISIONS/D-PEC-107_MEMORY_GRANT_2026-09-27.md` |
| RV1 D1 re-review | DEL-00-01 and DEL-00-03 `_REVIEW.md`, `Review_Findings.csv`, one new `_Evaluation/Reviews/REV_*` snapshot each and the reviews `_LATEST.md` pointer as the method requires (WORKING_ITEMS dispatching the REVIEW; `D-PEC-107` RV1 authorization) | DIR; the `D-PEC-105` act (PR #1007) | Findings recorded against the reviewed hashes; no lifecycle, SOW or artifact write; any correction a finding calls for recorded only (freeze) | COMPLETE — merged as PR #1023 (`31a90f3e6`) after reviews 01–02 (`../../AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/returns/REVIEW_PR1023_0{1,2}.md`): DEL-00-01 SELF_CHECK (one MAJOR, RF-001: AC-002 partly met, the ADR Context omits the §16 adapter-level basis element; three MINOR; one OBSERVATION); DEL-00-03 PEER_REVIEW (AC-001–AC-010 pass; two MINOR; five OBSERVATION; CU-001 retired as history); no lifecycle, SOW or artifact change; corrections recorded only (freeze) |
| ACC Owner re-acceptance | Owner `ACCEPT_EXACT_BYTES` of the reviewed hashes, with DEL-00-01 AC-007 and DEL-00-03 AC-011; recorded by HELP_HUMAN | RV1; any correction packet its findings require | Owner act recorded | COMPLETE — the owner ruled on 2026-09-27: "ACC: option 1; accept all findings as is; re-accept DEL-00-01 and DEL-00-03 exact bytes; retire CU-001" (`../../_DECISIONS/D-PEC-108_D1_REACCEPTANCE_2026-09-27.md`, register row `D-PEC-108`). HELP_HUMAN's presentation (PR #1023 review 02, NB-1): options 1 (accept every finding as-is and re-accept both deliverables' exact bytes; recommended), 2 (revise, corrections recorded only under the freeze) and 3 (re-accept DEL-00-03 only); RF-001's severity was put as the owner's call, and the owner made none, so it stays MAJOR; option 1's AC-007 and AC-011 confirmations, CU-001 retirement and exact-bytes scope (no C-05 act) as `D-PEC-108` transcribes them. Recorded in both review records and snapshots `REV_DEL-00-01_2026-09-27_1655`, `REV_DEL-00-03_2026-09-27_1658` in PR #1028 |
| C1 / M1 / F1 Closeout, receipt, final PR | Affected records; central `RECEIPT.md` (HELP_HUMAN); the two granted MEMORY rows (WORKING_ITEMS). `D-PEC-107` granted no `MEMORY.md` path; the owner then granted the rows for DEL-00-01 and DEL-00-03 (below), so M1 appends one row to each existing `MEMORY.md` at closeout | TM1, RV1, ACC | Final PR merged | READY FOR FINAL MERGE — PR #1028 (https://github.com/sgttomas/chirality/pull/1028). C1 bounded closeout at `31a90f3e6`: the graph, TM rows, notice, both review records, STATUS and README compared, with the STATUS refresh below and no README change; the supplement wording error (PR #1021 review 03, Q1) is corrected in the receipt, since a run manifest pins the supplement's bytes. M1: the two granted rows (WORKING_ITEMS, brief `../../AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/briefs/ACCCLOSE_ACCEPTANCE_AND_MEMORY.md`) and the central receipt `../../AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/RECEIPT.md`. F1: PR #1028 |

**Order.** DIR → TM1 and RV1 (in parallel; they share no file) → ACC (owner) → C1 → M1 → F1.

## Current state and recovery

- **Checked basis:** `origin/main` `31a90f3e6` (the PR #1023 merge, RV1).
- **Next work:** none after PR #1028 merges. PEC rests at the `D-PEC-107` freeze point; what carries is named in the receipt.
- **Local or unmerged work:** the final PR, #1028.
- **Active operations and ownership:** none running. Handed back: the ACCCLOSE manager (return `../../AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/returns/ACCCLOSE_ACCEPTANCE_AND_MEMORY.md`), the RV1 manager and the TM1 manager.
- **Graph maintainer:** HELP_HUMAN.
- Nothing here prompts about CHECKING. DEL-00-01 and DEL-00-03 stay `CHECKING`.

## Owner-direction evidence and D-PEC-88 trace

- 2026-09-27, owner, verbatim: see `D-PEC-107`. The owner's earlier question on K3 ("The tool's exact shape will be negotiated with each app?" … "There should be a contract with PEC from each project.  PEC determines what it publishes.  The design of PEC is my responsibility.") informed the recommendation the owner took.
- 2026-09-27, owner, verbatim (answering the MEMORY grant this graph said HELP_HUMAN would ask for): "grant the MEMORY rows for DEL-00-01 and DEL-00-03". HELP_HUMAN reads it as granting one row in each existing `MEMORY.md` (created under `D-PEC-105` add-on M), written at M1. The grant, with the exact paths, is recorded in `../../_DECISIONS/D-PEC-107_MEMORY_GRANT_2026-09-27.md`, a supplement that leaves the merged `D-PEC-107` record unchanged.
- STATUS/README changes made under `D-PEC-88` in this undertaking:
  - Direction PR: `docs/STATUS.md` records the new undertaking, the intake dispositions, RV1 authorized, K3's new home and the freeze point; `README.md` unchanged.
  - TM1 PR (#1021), HELP_HUMAN commit: no `docs/STATUS.md` or `README.md` change. Review-01 repairs: RV1 row ACTIVE; the MEMORY grant recorded with exact paths (review 02: moved to a separate supplement record).
  - RV1 PR (#1023), HELP_HUMAN commit: no `docs/STATUS.md` or `README.md` change.
- 2026-09-27, owner, verbatim (ACC): "ACC: option 1; accept all findings as is; re-accept DEL-00-01 and DEL-00-03 exact bytes; retire CU-001" (`D-PEC-108`).
  - Final PR (#1028), HELP_HUMAN commit: `docs/STATUS.md` records RV1 done, the owner's `D-PEC-108` re-acceptance, the undertaking's closeout and the freeze point; `README.md` unchanged (it names no RV1 or D1 acceptance state).
