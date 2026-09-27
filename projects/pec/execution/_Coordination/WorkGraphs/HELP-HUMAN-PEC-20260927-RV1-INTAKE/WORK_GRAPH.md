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
- **Freeze point:** by the owner's direction (`D-PEC-107` §Freeze point), PEC's state after PR #1014 is a freeze point for a later ground-up reassessment. No scope change is opened. The consumer-contract design, the next PEC scope change and re-reviews of DEL-04-01 and DEL-03-01 are recorded as considerations only. This graph holds only the directed, bounded TM1 and RV1 work, and the owner may hold RV1 as part of the freeze.
- **Left out:** production. By owner direction, production happens in a different session. This graph prepares a production packet only if one becomes a dependency of something necessary here.
- **Completion:** every node below is COMPLETE, or CARRIED (named in the central receipt with its next home), or the owner has explicitly removed it. The closeout, the receipt and the MEMORY rows are done, and the final PR is merged.

## Work

| ID / outcome | Deliverables and write scope (owner) | Needs / why | Completion check | State |
|---|---|---|---|---|
| DIR Direction record | `D-PEC-107` record and register row; this graph; STATUS under `D-PEC-88` (HELP_HUMAN) | The owner's direction | Merged | ACTIVE — in this PR |
| TM1 Intake dispositions, K3 row, Root notice | `_Coordination/_TaskManagement/**` (dispositions of CAND-01/02/03; promoted rows for CAND-02 and CAND-03; a K3 row; the consumer-contract design item added to the CAND-02 row) and one Root coordination notice for CAND-03 (WORKING_ITEMS, `task-management`) | DIR | `taskmgmt validate` passes; each disposition cites `D-PEC-107` | PLANNED — ready when DIR merges |
| RV1 D1 re-review | DEL-00-01 and DEL-00-03 `_REVIEW.md`, `Review_Findings.csv`, one new `_Evaluation/Reviews/REV_*` snapshot each and the reviews `_LATEST.md` pointer as the method requires (WORKING_ITEMS dispatching the REVIEW; `D-PEC-107` RV1 authorization) | DIR; the `D-PEC-105` act (PR #1007) | Findings recorded against the reviewed hashes; no lifecycle, SOW or artifact write; any correction a finding calls for recorded only (freeze) | PLANNED — ready when DIR merges; the owner confirmed RV1 under the freeze |
| ACC Owner re-acceptance | Owner `ACCEPT_EXACT_BYTES` of the reviewed hashes, with DEL-00-01 AC-007 and DEL-00-03 AC-011; recorded by HELP_HUMAN | RV1; any correction packet its findings require | Owner act recorded | PLANNED — BLOCKED on RV1; presented as an owner option under the freeze |
| C1 / M1 / F1 Closeout, receipt, final PR | Affected records; central `RECEIPT.md` (HELP_HUMAN). `D-PEC-107` grants no `MEMORY.md` path, so RV1 is recorded in the graph and receipt only unless the owner grants rows at closeout | TM1, RV1, ACC | Final PR merged | PLANNED |

**Order.** DIR → TM1 and RV1 (in parallel; they share no file) → ACC (owner) → C1 → M1 → F1.

## Current state and recovery

- **Checked basis:** `origin/main` `974bf7da4` (the PR #1014 merge closing `HELP-HUMAN-PEC-20260925-POST-SCA005`).
- **Next work:** merge this direction PR, then dispatch TM1 and RV1.
- **Local or unmerged work:** this PR.
- **Active operations and ownership:** none yet.
- **Graph maintainer:** HELP_HUMAN.
- Nothing here prompts about CHECKING. DEL-00-01 and DEL-00-03 stay `CHECKING` unless the owner acts.

## Owner-direction evidence and D-PEC-88 trace

- 2026-09-27, owner, verbatim: see `D-PEC-107`. The owner's earlier question on K3 ("The tool's exact shape will be negotiated with each app?" … "There should be a contract with PEC from each project.  PEC determines what it publishes.  The design of PEC is my responsibility.") informed the recommendation the owner took.
- STATUS/README changes made under `D-PEC-88` in this undertaking:
  - Direction PR: `docs/STATUS.md` records the new undertaking, the intake dispositions, RV1 authorized, K3's new home and the freeze point; `README.md` unchanged.
