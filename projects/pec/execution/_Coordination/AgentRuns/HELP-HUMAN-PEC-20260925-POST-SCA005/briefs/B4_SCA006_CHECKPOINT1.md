# Brief B4 — SCA-006 checkpoint-group-1 package: D-PEC-90 reliance amendment (WORKING_ITEMS, scope-change)

Parent: HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, graph node R1. Work graph: `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`. Role: WORKING_ITEMS (Type 1), with `Workflow: chirality-root:bundled:workflow:scope-change`. Load `WORKFLOW.md`, `resources/contract.md` and `resources/method.md`, and record their SHA-256. Model steer: `claude-opus-5-5`, high, for you and your children.

## Authority

- **`D-PEC-90` R-A.** Ruling at `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-90_RULING_2026-09-25.md`; proposal `D-PEC-90_agent_reliance_on_pec_data_proposal_2026-09-25.md`. Operational reliance on PEC data is PEC product direction. Authority is unchanged: PEC-K-01, PEC-K-02 and K-AUTH-1 stand. Its grant item 3 is: "prepare the exact PRD and `projects/pec/AGENTS.md` amendment as the next PEC scope change once SCA-005 checkpoint 2 is accepted, including the direct-query access text".
- **Direct-query answer.** The owner answered on 2026-09-25, verbatim: "agents may eventually query PEC directly, yes.  Through tool calls."
- **Carry-forward.** The D-PEC-91 ruling's carry-forward note says response-size budgets for agent consumers belong in this amendment and in the API/orientation work.
- **Loop.** The owner's `D-PEC-94` direction places this in the post-SCA-005 work graph.
- **Stage.** Checkpoint group 1 only, method parts A and B. Produce the complete reviewable package, get it independently verified, and stop.

## Settings

- Variant: `SOFTWARE`.
- `CONTEXT_ROOT = projects/pec/execution/`.
- `DECOMPOSITION_PATH = projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.5).
- `SCOPE_CHANGE_ROOT = projects/pec/execution/_ScopeChange/`.
- `AMENDMENT_ID = SCA-006`.
- `ALLOW_RENUMBERING = false`.

Mirror the SCA-005 checkpoint-1 package form (`_ScopeChange/SCA-005_2026-09-23_2139/`) wherever the method is silent.

## Inputs (read; do not modify)

- **PRD and PEC instructions:**
  - `docs/PRD.md` v2.3: PEC-K-02, PEC-K-03, PEC-K-11, §4.2, §8 (agents, access classes), §9 (ORI, API), §11, §12, §16 item 6.
  - `projects/pec/AGENTS.md`: the K-02 gloss, and the loop and fence sections.
- **Affected deliverables:**
  - DEL-04-01 `ScopeOfWork.md` (CLM-016, AX-007);
  - DEL-00-03 `artifacts/v2/SPEC.md` (K-03 row);
  - DEL-08-01 through DEL-08-04 (API and access), where affected;
  - DEL-01-06 (the loop registry and consumers), where affected.
- **Coordination records:**
  - `D-PEC-67`, the K03-A exact-row adoption coordinated with the App loop;
  - the L-A1 reliance-hold control. It is distinct from "operational reliance", and the two must be kept apart.
- **Root:**
  - Root `AGENTS.md` L54–55 and `docs/PRD_ROOT.md` N-1 (notice-only surfaces);
  - `docs/CONTRACT.md` K-RUNTIME-1 and the D-GOV-43 A2 consumer path.
- **Decomposition:** the accepted revision 1.5 package and registers, including which SOW rows (for example SOW-004 orientation and the SOW-08x API rows) cite the affected PRD text.
- **Audit baseline:** `_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_2026-09-25_1606/` is the latest. Decide whether it can serve as the pre-change baseline or whether the method needs a fresh `audit-decomp` pre-change run, and justify the choice.

## Write boundary

Work in an isolated worktree on branch `claude/pec-sca006-cp1-package`, cut from fresh `origin/main`.

**Write only:**
- a new snapshot folder `projects/pec/execution/_ScopeChange/SCA-006_<YYYY-MM-DD>_<HHMM>/`, containing:
  - `Brief.md`;
  - `Impact_Assessment.md`;
  - `Amendment_Actions.csv` (PROPOSED);
  - `Pre_Change_Coverage.json`;
  - `Decision_Log.md`: SCA006-G1 opened by owner direction under D-PEC-90 R-A and D-PEC-94, quoted verbatim, with the checkpoint-1 row set to `AWAITING_OWNER`;
  - `Handoff_State.md`;
- a pre-change audit folder, only if one is needed;
- `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/B4_SCA006_CHECKPOINT1.md` (your return) and `returns/B4_VERIFIER_VERDICT_NN.md`.

**Do not modify:**
- `_LATEST.md` pointers, `checkpoint_snapshots/`, the decomposition, registers, PRD, any SOW, `_CONTEXT.md`, `_STATUS.md`, `projects/pec/AGENTS.md`;
- `_DECISIONS/**`, the work graph, `docs/STATUS.md`, `README.md`, `v2/**`;
- any foreign path.

## Content

Parse the change into atomic actions. Candidates:
- **PEC-K-03:** replace verify-before-rely with operational reliance within the declared pin, coverage and tier. Keep "non-authoritative" in the authority sense, and keep pull-oriented, consumer-owned use.
- **§8:** agents may act on PEC data received through an enabled consumer, and may query PEC directly through tool calls. This adds an access class or a mechanism; §16 item 6 on auth reuse becomes relevant.
- **§9:** a reliance-envelope requirement plus response-size budgets.
- **§12:** a release gate proving parity and coverage before reliance is advertised.
- **`projects/pec/AGENTS.md`:** the K-02 gloss.
- **DEL-04-01 and DEL-00-03:** the quotations.
- **Other affected rows:** any other decomposition, SOW or SPEC rows the change touches.

Each action cites its evidence and passes method part A validation.

**Impact Assessment.** It has the method's required tables, and must say:
- which surfaces are PEC-owned and which are notice-only (Root, App, Runtime);
- how the change stays within `D-GOV-01`, Root PRD N-1 and K-AUTH-1;
- where option choices change the action set. Present the recommended option and the deltas for the alternatives, for example whether §8 direct query is specified now or deferred behind an access-class decision.

**Checkpoint-1 owner question set.**
- Confirm the parsed change set.
- Accept the Impact Assessment at its exact SHA-256.
- Choose among the genuine options.
- Say whether R-C remains excluded; it does under D-PEC-90.

## Checks

- `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict`, unchanged at 0/0.
- Preimage hashes.
- `Amendment_Actions.csv` parses against the contract's columns and enums.
- `validate_scope_change_packet.py`, if its schema fits.
- Reliance-hold preflight with `exact-correction-preparation`.
- `git diff --check`.
- Containment.

## Delegation

- You may dispatch `pec-task` children (opus) to draft disjoint files, and a TASK `audit-decomp` child if a pre-change audit is needed.
- Before returning, dispatch one fresh read-only verifier (`pec-reviewer`, opus). Loop until it reports nothing blocking, and save each verdict.
- Commit your return to the branch before you hand back.

## Publication

- Commit, ending each message with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Push and open a PR against `main`, ending the body with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
- Do not merge. The PR publishes the package; it applies nothing.

## Return

- PR URL and head SHA;
- the package files with SHA-256;
- action counts;
- the owner question set;
- check results;
- verifier verdicts;
- containment;
- anything unresolved.

## Limits

- No PRD, AGENTS, SOW, decomposition or lifecycle application.
- No CHECKING, ISSUED or acceptance. Do not ask the owner about CHECKING.
