# Launch Brief — N2 DEL-02-03 M2 Preparation

- Parent: `HELP_HUMAN`, run `ROOT_V3_PHASE0_2026-08-22`
- Accepted basis: `main@6b0c5219b6a2653e2fc491b1d998abcf78fcf776`
- Dependency: dispatch only after HELP_HUMAN accepts N1 and supplies the exact
  N1 patch SHA-256.
- Objective: produce the DEL-02-03 M2 preparation package, with no instruction
  application or lifecycle change.
- Construction: bounded ephemeral-generalist Agent 2; delegation prohibited.
- Content write target: only
  `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-03_Delegation_Hierarchy_and_Entry_Rules/_run_records/DEL-02-03-M2-PREP-001/`.
- Control-plane writes: `STATUS.json` and `RETURN.md` in this instance folder.

## Required context and acceptance contract

Read the owner steer/G0 record, DEL-02-03 ScopeOfWork and status, N1 return and
proposal packet, live manifest schema/examples, and validator. Produce every
N2 item in the steer. The exact `AGENTS.md` delta is referenced only by N1
patch SHA/path; do not duplicate its bytes. Validate the draft manifest with
the repository validator, prove basis `13201dfe…` is a commit, recheck the SOW
hash and untouched status, and return exact hashes/checks/blockers. Stop at
`PREPARED — BLOCKED ON D-GOV-35 RULING`.
