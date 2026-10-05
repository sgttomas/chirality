# Brief PM: draft the Agent User Manual's PEC corrections

TASK (Type 2) for HELP_HUMAN (ROOT), run `ROOT-AUM-PEC-AND-FOLLOWUPS-20261005`. You return to ROOT and do not delegate. You make no Git writes. Write only `RUN3/AUM_PEC_EDITS.md`.

**Placeholders.**
- `WT` = the T3 worktree root.
- `NUM` = `WT/numerics`. It equals main `7ba1181d43`, so read here.
- `RUN3` = `NUM/execution/_Coordination/AgentRuns/ROOT-AUM-PEC-AND-FOLLOWUPS-20261005`.
- `AUM` = `NUM/docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v3.md`.
- `PEC` = `NUM/projects/pec`.

## The basis

- **The owner's direction:** `RUN3/OWNER_DECISIONS.md`. Correct the AUM's PEC statements "based on the current state of PEC".
- **PEC's current state, from its own records. Establish it; do not assume it:**
  - `PEC/AGENTS.md`;
  - `PEC/loop/LOOP_INIT.md` and `PEC/init/`;
  - the adoption on 2026-09-25: commit `11be801130`, the tranche manifests named `PEC-*` under `NUM/docs/governance_harness/tranche_manifests/`, and the related notices under `PEC/execution/_Coordination/`;
  - PEC's receipt arrangement: `PEC/loop/LOOP_RECEIPTS.md`, and whether it still validates receipts or uses central receipts;
  - its work graphs, Task Management, and how it is entered. Is there a launcher in `NUM/init/dev-loop-init-prompt.md`?
  - `NUM/workflows/construct-local-work-graph/WORKFLOW.md` §3, which lists PEC as an adopter.
- **What a prior TASK found:** AM's list in `NUM/execution/_Coordination/AgentRuns/ROOT-LOOPINIT-AUM-ALIGNMENT-20261005/AUM_EDITS.md`, §3 L5. It covers AUM lines 62, 74 (the "Runtime or PEC" row), 106, 667 and 684/690, at the time of that edit. Line numbers have shifted since #1094; find the passages again.

## The output: `RUN3/AUM_PEC_EDITS.md`

1. **A short statement of PEC's current state,** with citations: entry, loop form, graph method, closeout, receipts and MEMORY, Task Management, and anything PEC keeps that App or Piping do not.
2. **Exact before and after edits to `AUM`,** each with line numbers and a one-line reason. Each "before" must occur exactly once (check with a byte count).
   - Cover every AUM statement about PEC that is untrue at main `7ba1181d43`. That includes §17 "Enter PEC development", and every passage that groups PEC with Runtime as outside the shared graph, closeout and memory arrangement, or with App and Piping as inside it.
   - Keep the edits minimal and in AUM's voice. Do not revise anything else.
   - Where a sentence covers several projects, change only the PEC part, and keep the rest true.
   - Use existing link definitions where they fit. Give any new definition exactly.
3. **If the edits warrant it,** an update to the revision note at AUM line 5, following #1094's E1, which added a 5 October entry. Extend that entry rather than adding another.
4. **Listed only, not proposed:**
   - Runtime statements that look stale;
   - Field Book or Consolidated v8 statements about PEC that conflict.

## Rules

- Read sections, not whole chapters. Read PEC's `LOOP_INIT.md` and `AGENTS.md` in full.
- Verify every quote.
- Use no machine-absolute paths.
- No tests, cargo, network, installs, or writes outside `RUN3/`.
- **Time box:** 60 minutes.
- **End your turn** with:
  - the summary of PEC's current state in a few lines;
  - the number of AUM edits, with a few words each;
  - the listed-only items;
  - any question for ROOT;
  - the output's sha256.
