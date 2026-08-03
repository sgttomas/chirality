# C7 CHANGE launch brief — expanded-tranche current-main sync

- Parent: `HELP_HUMAN/ROOT_FOUR_LANES_2026-08-02`.
- Role: `CHANGE` Agent 1.
- Governing plan: `ORCHESTRATION_PLAN_V18.md` and `WORK_GRAPH_V18.json`.
- Branch: `codex/root-four-lanes-20260802`.
- Pre-sync HEAD: `6fbdc31c3b1e1f462fdd8554cd5fdd79d43e67a5`.
- Observed server main: `cf6bc15b966346f1d6c5bd27af6312c7b8e6a5c3`.

## Objective

Repeat C5's exact preservation method for the expanded tranche. Inventory all
dirty/untracked paths with status, type, mode, size, and SHA-256; preserve them
recoverably; fetch current refs; integrate exact current main into the task
branch without rebase or force; restore every path byte-identically; and prove
parity, ancestry, overlap/containment, recovery retention, and zero staged or
unmerged residue.

## Authority and stop

Do not stage the tranche, create a tranche commit, push, mutate PR #491,
delete any recovery object, edit semantic content, merge the task branch into
main, rebase, or force. Stop on overlap, conflict, lost path, inventory drift,
remote advance during the operation, or semantic uncertainty.

Write only C7 `RETURN.md` and `STATUS.json` beside this brief, reporting exact
remote/local identities, inventory proofs, retained recovery identities,
forbidden-effect audit, and C8 release condition.
