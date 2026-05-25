# Packet Contract: PKG00-SCA-PACKET-001

## Identity

| Field | Value |
|---|---|
| PacketID | PKG00-SCA-PACKET-001 |
| PacketTitle | SCC-002 PKG-10 Policy Proposal |
| SCC_ID | SCC-002 |
| DecompositionVariant | SOFTWARE |
| DecompositionAuthority | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| UpstreamSnapshot | `execution/_Reconciliation/DepClosure/CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431` |
| AffectedDeliverables | DEL-10-02; DEL-10-03 |
| FocusRows | DEP-10-02-004; DEP-10-03-006 |
| PacketStatus | PROPOSAL_PACKET |

## Authority Limits

This packet is a bounded consumable for later human-reviewed SCOPE_CHANGE intake. It is not an amendment, dependency ruling, closure decision, or register mutation.

The packet may be used to seed SCOPE_CHANGE analysis for SCC-002, but it has no authority to:

- alter product deliverables;
- alter any `Dependencies.csv`;
- amend decomposition truth;
- update `_ScopeChange` or `_Reconciliation`;
- declare SCC closure;
- initiate SCOPE_CHANGE by itself;
- report project-wide blocker state.

## Consumption Rules

1. Treat all proposed actions as candidate inputs.
2. Require a human to explicitly initiate SCOPE_CHANGE before any SCOPE_CHANGE gate is active.
3. Preserve `TBD` wherever the source evidence does not establish an accepted ruling.
4. Use `Evidence_Index.csv` as the citation map for every proposed action.
5. If product files or dependency registers are later edited, that work must occur in the authorized owning workflow, not through this packet.

## Gate Mapping

| SCOPE_CHANGE Gate | Packet Use |
|---|---|
| Intake | Read `SCOPE_CHANGE_INIT.md`, identity fields, affected rows, and packet limits. |
| Impact Assessment | Use `Affected_Surfaces.csv` to bound read and write candidates. |
| Amendment Design | Use `Proposed_SCA_Actions.csv` as conservative action candidates. |
| Evidence Review | Use `Evidence_Index.csv` and the rationale file to verify source support. |
| Closure Review | Confirm any accepted changes are separately recorded by SCOPE_CHANGE and product owners. |

## Non-Goals

- This packet does not decide whether DEP-10-02-004 should be converted, satisfied, retired, or kept.
- This packet does not decide whether DEP-10-03-006 is satisfied.
- This packet does not resolve ownership or responsible-party TBDs.
- This packet does not replace the DepClosure snapshot or the decomposition authority.
