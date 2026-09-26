# Brief — COV_D101_POSTSETUP_2026-09-26_1651

## Launch message (as received from the dispatching WORKING_ITEMS instance)

> You are TASK (Type 2) in the Chirality repository, executing chirality-root:bundled:workflow:audit-decomp for D-PEC-101 add-on V. Model steer: claude-opus-5-5 at high reasoning. Your complete brief is
> /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d101-act/projects/pec/execution/_Coordination/REV16_CURRENCY_SETUP_D101_2026-09-26/child_briefs/T_V_AUDIT.md
> (SHA-256 d9e3f4e76b72823ff0a4c464683d232a45ca979e759f3b17e3c3632662d66194). Verify its hash, read it in full and execute it exactly. Work only in the worktree /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d101-act (absolute paths; cwd resets between shell calls; run the snapshot-folder script from that worktree root). Write only inside the new snapshot folder (and the named scratch directory). Do not touch _Evaluation/DecompCoverage/_LATEST.md or any other file. No git add, commit or push. Return the report the brief's Return section specifies.

The brief's hash was recomputed before use and matched
(`d9e3f4e76b72823ff0a4c464683d232a45ca979e759f3b17e3c3632662d66194`).

## Verbatim brief (`child_briefs/T_V_AUDIT.md`)

    # Child brief T_V_AUDIT — D-PEC-101 add-on V: post-setup `audit-decomp` re-audit (TASK)

    Parent: WORKING_ITEMS (Type 1), brief K14A (`AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/K14A_D101_ACT.md`,
    SHA-256 `b253797178dfb4b117491d5d056120a23e2b2538485fa83119c5e4851961d2ec`), undertaking
    `HELP-HUMAN-PEC-20260925-POST-SCA005`, nodes K1/K4. Role: TASK (Type 2) executing
    `chirality-root:bundled:workflow:audit-decomp` (`workflows/audit-decomp/WORKFLOW.md`, expected
    `7ba6291c836973a6af0aeb81d56d60ede89466c3d006673d7ef07f09b984246b`; load `resources/contract.md` and
    `resources/method.md` and record their hashes). You do not delegate. Model: `claude-opus-5-5`, high
    reasoning. Read root `AGENTS.md`, `projects/pec/AGENTS.md` and `agents/AGENT_TASK.md`; record hashes.

    ## Parameter source (not enlarged)

    The ruled proposal `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-101_rev16_currency_setup_proposal_2026-09-26.md`
    (`7ad176063b10b4cb3093bc9c1d5c6efbab83fcdb5e6a059e6122c466fd095a25`), section "Add-on V", and the ruling
    `D-PEC-101_RULING_2026-09-26.md` (`baa4fc09525aaef89cdb519b934b00c90e699a2111a5c604f906fc5ed2edba28`),
    question 3: "V".

    ## Parameters

    | Parameter | Value |
    |---|---|
    | Repository root | `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d101-act` (branch `claude/pec-d101-act`, HEAD `fcc1cd26b43e1c75392ac38c64be459f8e6b1c39 (product bytes unchanged since the K4 commit 62230fa46)`) |
    | `EXECUTION_ROOT` | `projects/pec/execution` |
    | `DECOMPOSITION_PATH` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`, revision 1.6, `status: current_basis`, expected `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1` |
    | Companion registers (live; verify) | `ScopeLedger.csv` `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e`; `Deliverables.csv` `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805`; `ContextBudgetQA.csv` `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c`; `Companion_Inventory.csv` `1597ceec7af45f33fe348d46429cc3f82042db5dbd6a083903ae04c7bf908662` |
    | `SCOPE` | `ALL` |
    | `DECOMP_VARIANT` | `SOFTWARE` |
    | `RUN_LABEL` | `D101_POSTSETUP` |
    | Output folder | created by running, from the repository root, `bash tools/scaffolding/create_snapshot_folder.sh projects/pec/execution/_Evaluation/DecompCoverage COV D101_POSTSETUP` (use the printed path; tool `7db42ee6…5640`) |
    | `REQUESTED_BY` | WORKING_ITEMS (K14A, HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`) |
    | `PRIOR_RUN_LABEL` | `COV_SCA006_POSTCHANGE_2026-09-26_0051` (`coverage_summary.json` `b9a068c078ba6ca4daf5d6129c2823141cae787f7770068e1d70644b13a09cf0`; issue log `37f4f6dc730cebfec173ca965c5afe00b5c506afbec5cb67f4f1e498087026d3`) |
    | `EXPECTED_SOURCE_SNAPSHOT` | Revision 1.6 `current_basis` (`9374c21f…08eb1`), SCA-006 `CLOSED_FOR_SCOPE_CHANGE_ONLY` (`_ScopeChange/_LATEST.md` `7a2fd074…6e5f`), plus the D-PEC-101 poststate: commit `fcc1cd26b43e1c75392ac38c64be459f8e6b1c39 (product bytes unchanged since the K4 commit 62230fa46)` (K1 and K4 with C applied and verified; run root `projects/pec/execution/_Coordination/REV16_CURRENCY_SETUP_D101_2026-09-26/`) |
    | `EXPECTED_HANDOFF_PHASE` | D-PEC-101 post-setup re-audit, after the product writes are verified and before publication |

    ## Expected results (a prediction to test, not a result to reproduce)

    - Resolved: prior COV-003/004/073/074 (the two absent folders), COV-075/076 (the two stale quotes),
      COV-080 (no register traced SOW-097..100) and, with K4, COV-077/078 (revision 1.5 re-pin). Forward
      production-unit coverage back at 100 % (68/68).
    - Unchanged: the three pre-existing Check-6 warnings.
    - 0 BLOCKER.

    Number this snapshot's findings sequentially; `PrePost_Comparison.md` maps every prior ID to its
    disposition (`CARRIED`, `CHANGED`, `NEW`, `RESOLVED`) and new ID. Classify each finding
    `EXPECTED_CONSEQUENCE` (name the decision), `PRE-EXISTING` or `DEFECT`. Report honestly whatever you
    find, including findings about the D-PEC-101 bytes.

    ## Sealed boundary

    - Write only inside the new snapshot folder: the method's output files, `PrePost_Comparison.md`
      and any output the method's own tools write there. Nothing else anywhere (no product file, no
      `_LATEST.md`, no run-root file). Scratch work, if any, only under
      `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/d101act/audit/`.
    - Do not update `_Evaluation/DecompCoverage/_LATEST.md`; the manager decides the pointer.
    - No git add, commit, push or branch operation.

    ## Return

    The snapshot folder path; its file list with SHA-256; BLOCKER / WARNING / INFO counts and
    `overall_status`; the prior-ID dispositions for COV-003/004/073–078/080 and the Check-6 warnings;
    any `DEFECT`; the instruction hashes you read; and anything unexpected.

## Normalized parameters

| Parameter | Value used |
|---|---|
| `EXECUTION_ROOT` | `projects/pec/execution` |
| `DECOMPOSITION_PATH` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.6, `status: current_basis`, `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1`, matches) |
| Companion registers | `ScopeLedger.csv` `1d24a4b8…e916e`, `Deliverables.csv` `94ee5d18…9805`, `ContextBudgetQA.csv` `93b0bb07…4c7c`, `Companion_Inventory.csv` `1597ceec…8662`: all match the brief |
| `SCOPE` | `ALL` |
| `DECOMP_VARIANT` | `SOFTWARE` |
| `RUN_LABEL` | `D101_POSTSETUP` |
| Snapshot folder | `projects/pec/execution/_Evaluation/DecompCoverage/COV_D101_POSTSETUP_2026-09-26_1651/`, the path printed by `bash tools/scaffolding/create_snapshot_folder.sh projects/pec/execution/_Evaluation/DecompCoverage COV D101_POSTSETUP` (tool `7db42ee6…5640`, matches), run from the worktree root at 16:51 MDT |
| `REQUESTED_BY` | WORKING_ITEMS (K14A, HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`) |
| `PRIOR_RUN_LABEL` | `COV_SCA006_POSTCHANGE_2026-09-26_0051` (`coverage_summary.json` `b9a068c0…cf0`, issue log `37f4f6dc…6d3`: both match) |
| `EXPECTED_SOURCE_SNAPSHOT` | revision 1.6 `current_basis`; SCA-006 `CLOSED_FOR_SCOPE_CHANGE_ONLY` (`_ScopeChange/_LATEST.md` `7a2fd074…6e5f`, matches); D-PEC-101 poststate |
| `EXPECTED_HANDOFF_PHASE` | D-PEC-101 post-setup re-audit, after the product writes are verified and before publication |
| `ACCEPTED_DECISIONS` (for `EXPECTED_CONSEQUENCE`) | `D-PEC-101` (proposal `7ad17606…a095a25`, ruling `baa4fc09…2edba28`, both match); SCA-006 checkpoint acceptances as recorded |
| Audited tree | worktree HEAD `43b60687b2f3a2176358d00e4f24a8a6ca08ba33` (the commit adding this brief), not the brief's stated `fcc1cd26b…`; `git diff 62230fa46 HEAD` touches only the run root, so the product bytes are those the brief names (`Decision_Log.md` D-2) |
| Scratch | `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/d101act/audit/` |
| Model | `claude-opus-5-5` as steered; role identity is instruction-asserted |
