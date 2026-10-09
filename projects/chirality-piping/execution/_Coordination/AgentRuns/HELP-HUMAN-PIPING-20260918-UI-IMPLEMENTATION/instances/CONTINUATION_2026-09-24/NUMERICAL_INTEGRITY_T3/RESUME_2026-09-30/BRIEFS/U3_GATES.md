# I112, round 2: the U3 PR's T9 and both-entry gate

TASK (Type 2), continued by WORKING_ITEMS for T3 (Agent 1), your return path. Your round-1 brief `PR_N_GATES.md`, its grant (solver at scale for these two gates only; part 2 under `t3_exclusive.sh`) and its method (I61's) apply.

## The revisions

- **Base B:** main `ba500defa4` (PR-B1 and PR-N merged).
- **Candidate C:** the U3 PR's code commit `8a12de28db` (`codex/piping-t3-pressure-retire-pr-20261009`, PR #1168).
- C is the legacy pressure retirement: refusals, removals, joint refusals and text corrections. See `R/I110/pressure_retire_01..06/` and the package `T/IMPLEMENTATION/U3/`.

## Acceptance

Identity is required, except for the differences below. List each one and classify it.

1. **A designed refusal.** The input carries the legacy label, any legacy pressure primitive, or a joint that is now refused (`JOINT_ELEMENT_STIFFNESS_INCOMPLETE`, `JOINT_ELEMENT_MAPPING_UNRESOLVED`). Its output becomes a refusal envelope with the documented code and text.
2. **A declared text correction** under ROOT's extended check: T1, T2, T3 or V1 in `CHANGE_RECORD` §6.
   - Only the declared string may differ.
   - The digests that bind it must equal the product's recomputation from the normalized content: `publication_sha256`, `receipt_sha256`, and for export documents RE `derivative::digest` and `derivative_hash`.
3. **A removed case:** an input or benchmark that the retirement removed, listed in `CHANGE_RECORD` §4.

Any other difference is a **stop**. gate_check must pass with 0 trusted breach triples on both sides.

## Host and records

- Targets go under `WT/targets/i112-u3*` and scratch in `WT/scratch/i112_u3/`. Reuse your rebuilt scripts and record their sha256.
- Records go in `R/I112/u3_gates_01/`, placeholder paths only.

End your turn with:
- T9's verdict and each part's;
- the differences, each classified;
- RETURN's sha256;
- any stop.
