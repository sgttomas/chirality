# HELP_HUMAN orchestration plan — plan version 18

Run ID: `ROOT_FOUR_LANES_2026-08-02`
Selection authority: `HUMAN`
Posture: `SEQUENTIAL_RESYNC_THEN_CLOSEOUT`

## Live basis

- Task HEAD: `6fbdc31c3b1e1f462fdd8554cd5fdd79d43e67a5`.
- New server-verified main: `cf6bc15b966346f1d6c5bd27af6312c7b8e6a5c3`.
- New delta: PEC-only, zero overlap with C6-R2's 238-path pre-return tranche.
- C6-R2: stopped before validation/staging/push/PR update.

## Nodes

| Node | Agent 1 | Objective | Stop |
|---|---|---|---|
| C7 | CHANGE | Freeze the expanded dirty/untracked tranche, fetch current refs, integrate exact current main without rebase/force, restore every byte, and prove parity/ancestry/containment. | No stage, tranche commit, push, PR mutation, semantic edit, stash deletion, task-branch-to-main merge, rebase, or force. |
| C8 | CHANGE | After C7 and HELP_HUMAN revalidation, repeat scoped commit/push/PR #491 closeout. | Held. No merge. |

## Acceptance

C7 passes only on exact path/status/type/mode/size/hash restoration, current
main ancestry, zero staged/unmerged residue, retained recovery material, and
no forbidden effect. Any overlap, drift, or semantic uncertainty returns to
HELP_HUMAN.
