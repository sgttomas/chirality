# Brief — audit-decomp post-change audit (SCA-006 checkpoint-3 preparation, plan item C4.1–C4.2)

The WORKING_ITEMS manager of brief B6 dispatched this run. B6 belongs to work-graph
node R3 of HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`. The run
went to a Type 2 TASK instance executing `Workflow: audit-decomp` at its current
edition in the worktree. Type 2 does not delegate. The brief asked for high
reasoning. The host reports the model as Opus 5.5 (`claude-opus-5-5`); this is
recorded as the runtime exposes it, not inferred from the steer.

## Parameters (as supplied, normalized)

| Parameter | Value |
|---|---|
| Worktree | `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a2942849b8715f72c`, branch `claude/pec-sca006-cp3-execution` |
| `EXECUTION_ROOT` | `projects/pec/execution` |
| `DECOMPOSITION_PATH` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`, revision 1.6, pre-acceptance form (`status: candidate_pending_checkpoint_3`; `accepted: not yet accepted …`). Brief SHA-256 `3ef0412a99812885e247bc4e9726fe005ce3446372f609c47274b6ad25b29b59`; live bytes match |
| Companion registers (brief prefixes) | `ScopeLedger.csv` `1d24a4b8…e916e`, `Deliverables.csv` `94ee5d18…9805`, `ContextBudgetQA.csv` `93b0bb07…c7c`, `Companion_Inventory.csv` `1597ceec…8662`; live bytes match (full values in `QA_Report.md`) |
| PRD | `projects/pec/docs/PRD.md` v2.4 `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe`; live bytes match |
| Changed `_CONTEXT.md` mirrors | DEL-04-03, DEL-08-01, DEL-08-03 |
| `DECOMP_VARIANT` / `SCOPE` | `SOFTWARE` / `ALL` |
| `RUN_LABEL` | `COV_SCA006_POSTCHANGE` |
| `REQUESTED_BY` | WORKING_ITEMS (B6) |
| Output folder | `projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA006_POSTCHANGE_2026-09-26_0051/` (name fixed by the brief; see `Decision_Log.md` D-3) |
| Expected revision / candidate | 1.6 / SCA-006 |
| `EXPECTED_SOURCE_SNAPSHOT` | candidate `projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/` (incomplete until the manager finishes A5); accepted group-2 decision `projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`; `_ScopeChange/_LATEST.md` names SCA-005, posture `ACCEPTED_PREDECESSOR` |
| `EXPECTED_HANDOFF_PHASE` | SCA-006 checkpoint-3 preparation (pre-acceptance poststate) |
| `PRIOR_RUN_LABEL` | `COV_SCA005_POSTSETUP_2026-09-25_1606`; its `coverage_summary.json` is byte-identical to `SCA-006_2026-09-25_1912/Pre_Change_Coverage.json` (`b7b432a2…128d`, verified) |
| `ACCEPTED_DECISIONS` | `D-PEC-95` (register row; run root `_Coordination/CURRENCY_REV15_D95_2026-09-25/`); `D-PEC-97` with the SCA-006 group-2 snapshot and its amendment 1 (`checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/`); the accepted SCA-006 `Propagation_Plan.md` (Lane B §B1, §B3, §B7; §"Basis currency since checkpoint 1"; §C4) |

## Classification the brief asked for (applied only where the records prove it)

1. Baseline COV-068, COV-069, COV-072, COV-073: determine from the live tree
   whether each is resolved; attribute any resolution to `D-PEC-95` (PR #924,
   merge `abfd0897b`), not to SCA-006; say plainly what is not resolved.
2. Expected SCA-006 consequences, `EXPECTED_CONSEQUENCE` with `DecisionRef`
   `D-PEC-97` / plan §B1, §B3, §B7, only if the live evidence matches: the two
   absent folders (B1); exactly two stale EvidenceQuotes, DEP-09-06-003 and
   DEP-10-03-003, with DEP-09-06-004 and DEP-10-12-004 still verbatim (B3); the
   63 other `_CONTEXT.md` and 66 `_REFERENCES.md` naming revision 1.5 / PRD
   v2.3 (B7). The unmoved pointers and the pre-acceptance front matter are the
   designed pre-acceptance state (plan §A6).
3. Everything else keeps its ordinary severity; any BLOCKER is reported
   plainly; unforeseen findings are recorded.

## Sealed boundary

- Write only inside this folder. Read-only everywhere else, including every
  deliverable file, `_CONTEXT.md`, `_STATUS.md`, `Dependencies.csv`, the
  decomposition, the registers and all three `_LATEST.md` pointers.
- No Git state change (no add, commit, checkout, stash, reset, push);
  read-only Git only. The manager commits this folder.
- Paired read: every `_STATUS.md` read is paired with a sibling `_MEMORY.md` /
  `MEMORY.md` when present, as non-authoritative context.
- PEC reliance-hold preflight (`candidate-validation`) before relying on
  inputs; a BLOCK stops the run. Result: `ALLOW` for every target
  (`QA_Report.md`).
- No CHECKING, ISSUED, acceptance, readiness or reliance claim. This snapshot
  is derivative evidence; it accepts and authorizes nothing.

## Instruction and method basis (SHA-256, verified before loading)

| File | SHA-256 | Brief value |
|---|---|---|
| `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` | — |
| `projects/pec/AGENTS.md` (post-A4 tranche bytes) | `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c` | — |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` | — |
| `workflows/audit-decomp/WORKFLOW.md` | `7ba6291c836973a6af0aeb81d56d60ede89466c3d006673d7ef07f09b984246b` | match |
| `workflows/audit-decomp/resources/contract.md` | `704929c7c006a20a5fbe3fc903d4f172e2edb4c6a451c4b6db40506b40004e75` | match |
| `workflows/audit-decomp/resources/method.md` | `51a0c69b389d0c641f88e8faa7bebbc2b3650518eede8882436853c583308827` | match |

This is the Root wave-2A edition carrying the `EXPECTED_CONSEQUENCE` severity.
The baseline ran the prior edition (`contract.md` `70a5abeb…401a0c`,
`method.md` `97df8402…d79c2`). The scope-change workflow for SCA-006 runs at its
pinned edition; that mix was disclosed to the owner (group-2 amendment 1). No
other role instructions and no other workflow or skill body were loaded.
