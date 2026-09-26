# Work graph — retire PEC's deliverable `## Remaining` sections

This graph is saved at `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT/WORK_GRAPH.md` under `projects/pec/loop/LOOP_INIT.md`, the shared method (`D-PEC-94`). Method: `chirality-root:bundled:workflow:construct-local-work-graph`.

## Intent and selected route

- **Stable run identity:** `HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT`.
- **Steering basis:** the owner's words on 2026-09-26, verbatim:
  - "Why am I seeing `remaining-items` appearing?  There must not be any of those going forward, so no need to scan for them."
  - After HELP_HUMAN explained RS1 (node RS1 of `HELP-HUMAN-PEC-20260925-POST-SCA005`): "open RS1".

  *Interpretation:* this opens the separate owner-directed undertaking that `projects/pec/AGENTS.md` names, retiring the sections "as App and Piping did". It rules no packet.
- **Intended result:**
  - Every open item in PEC's 57 deliverable `_STATUS.md` `## Remaining` sections is moved to its governing home, with no obligation lost. Homes are a Scope of Work or governing decision, a Task Management row, a work-graph node, or an owner decision.
  - Items already satisfied or superseded are shown so with evidence.
  - The sections are then removed under an owner-ruled packet, and `projects/pec/AGENTS.md` is corrected in an instruction tranche.
- **Precedent:**
  - Piping's `TM_PIP_REMAINING_RETIREMENT_20260922/` and commit `82f4a16ce`;
  - App's commit `1f78abfd4`;
  - PEC's `D-PEC-83` concordance.
- **Left for later:** the 73 held or conditional `D-PEC-83` residuals, which were never in any Remaining section.
- **Route:**
  - After the SCA-006 checkpoint-3 merge (PR #943): the instruction change builds on the owner-approved amendment-1 paragraph.
  - Items whose receiving SOW is rewritten by a pending SOW-currency node are carried by that node. As ruled (`D-PEC-99`, Q1 a), S1, S2 and S4 of `HELP-HUMAN-PEC-20260925-POST-SCA005` carry them (4 each); D1 carries none. The bound tranche manifest's `scope_limits` keeps its preparation-time wording.

## Work

| ID / outcome | Deliverables and write scope (owner) | Needs / why | Completion check | State |
|---|---|---|---|---|
| RR1 Census, decision account and draft packet | `_TaskManagement/TM_PEC_REMAINING_RETIREMENT_2026-09-26/` (WORKING_ITEMS) | Owner direction ("open RS1") | Account finite and closed; every item keyed and disposed with evidence; verifier passes | COMPLETE — PR #951 merged as `d67fdc31b`: census (92 keys, matching `D-PEC-83`), decision account and draft packet; verifier verdict 03 PASS WITH NOTES, nothing blocking. Brief `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/RR1_REMAINING_RETIREMENT_ACCOUNT.md` (`e0bda78f…6227`) |
| RR2 Owner ruling on the retirement packet | Decision record and register row (HELP_HUMAN records) | RR1 published and reviewed | Owner rules | COMPLETE — the owner ruled on 2026-09-26: “D-PEC-99: A; Q1 a; Q2 a; Q3 a; confirm F; no MEMORY; defaults”. The draft is published unchanged as `_DECISIONS/D-PEC-99_remaining_retirement_proposal_2026-09-26.md` (`29e2ff57…6c79`) with register row `D-PEC-99`; ruling `_DECISIONS/D-PEC-99_RULING_2026-09-26.md` |
| RR3 Retirement act | The 62 paths `D-PEC-99` A grants: 57 `_STATUS.md` sections removed, `projects/pec/AGENTS.md` (instruction tranche), the exhibit, the tranche manifest and notices to Root and Runtime; run root `_Coordination/REMAINING_RETIREMENT_D-PEC-99_{D}/`. No Task Management row (none needed). In the same PR HELP_HUMAN adds the “Absorbs … Part B items” sentences to rows S1, S2 and S4 of graph `HELP-HUMAN-PEC-20260925-POST-SCA005` (WORKING_ITEMS) | RR2; SCA-006 checkpoint 3 merged (PR #943, `db9328789`) | `verify_d99.py` closure before and after; the proposal's validators; fresh verifier; review | ACTIVE — in PR #957, awaiting review and merge: one generator run on 2026-09-26 (`WROTE 62 files`; 57 sections removed; 92 keys: 9 closed, Part A 71, Part B 12); closure check PASS before and after; verifier verdicts 01 and 02 PASS WITH NOTES; run root `_Coordination/REMAINING_RETIREMENT_D-PEC-99_2026-09-26/`; brief `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/RR3_D99_RETIREMENT_ACT.md`. The Part B sentences are in graph `HELP-HUMAN-PEC-20260925-POST-SCA005` rows S1, S2 and S4 |
| C1 / M1 / F1 Closeout, receipt, final PR | Affected records (HELP_HUMAN) | RR3 | Merged | PLANNED |

## Current state and recovery

- **Checked basis:** `origin/main` `189f205ff` (PR #954: the `D-PEC-99` ruling, publication and register row).
- **Local or unmerged work:** PR #957, the RR3 act with these records.
- **Active operations:** none. The RR1 and RR3 managers handed back.
- **Next work:** C1 / M1 / F1 after PR #957 merges. The `FINAL_ROW_ACCOUNT.csv` keeps `HumanDecision=PENDING` because the grant names only `AppliedResult`; the owner's decision is the `D-PEC-99` ruling.
- **Graph maintainer:** HELP_HUMAN.
