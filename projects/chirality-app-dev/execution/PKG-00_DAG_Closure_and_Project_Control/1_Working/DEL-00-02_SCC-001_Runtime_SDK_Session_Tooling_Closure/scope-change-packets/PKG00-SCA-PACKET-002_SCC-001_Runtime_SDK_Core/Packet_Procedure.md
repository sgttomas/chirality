# Packet Procedure: PKG00-SCA-PACKET-002 SCC-001 Runtime SDK Core

## Intake Procedure

1. Human reviews this packet and decides whether to initiate SCOPE_CHANGE.
2. If initiated, use `SCOPE_CHANGE_INIT.md` as the seed request.
3. Load the accepted upstream DepClosure snapshot and decomposition authority named in the datasheet.
4. Review `Evidence_Index.csv` and the owning product dependency registers listed in `Affected_Surfaces.csv`.
5. For each action in `Proposed_SCA_Actions.csv`, decide whether it is accepted, rejected, split, merged, or left `TBD`.

## Gate-by-Gate Use

| Gate | Required Packet Use |
|---|---|
| Intake | Confirm the request is human-initiated and bounded to SCC-001 runtime SDK core. |
| Evidence | Verify each proposed action has cited evidence. |
| Impact | Check all affected deliverables and files before any amendment. |
| Amendment | Apply only accepted SCOPE_CHANGE actions through the owning workflow. |
| Verification | Run dependency validation and DepClosure after accepted changes. |
| Handoff | Record accepted snapshot, derivative-package status, closure verdict, rerun requirements, and blockers. |

## Required Reviews

- Runtime contract owner review for `DEL-03-01`, `DEL-03-02`, `DEL-03-03`, and `DEL-03-04`.
- SDK adapter owner review for `DEL-04-01`, `DEL-04-02`, `DEL-04-03`, `DEL-04-04`, and `DEL-04-05`.
- RECONCILIATION or SCOPE_CHANGE review for row-level direction and dependency-type rulings.

## Stop Conditions

- Missing owning register evidence.
- Disagreement between decomposition authority and product deliverable registers.
- Attempt to report SCC closure or project-wide blocker state from this packet.
- Attempt to alter product dependency rows outside an accepted SCOPE_CHANGE workflow.
