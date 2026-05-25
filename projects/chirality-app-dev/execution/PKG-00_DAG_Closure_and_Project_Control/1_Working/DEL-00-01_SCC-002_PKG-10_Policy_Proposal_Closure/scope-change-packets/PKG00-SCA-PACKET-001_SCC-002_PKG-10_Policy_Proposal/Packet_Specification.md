# Packet Specification: PKG00-SCA-PACKET-001

## Purpose

Prepare a conservative SCOPE_CHANGE-compatible packet for SCC-002, the PKG-10 policy/proposal pair formed by DEL-10-02 and DEL-10-03. This packet organizes evidence and candidate actions only.

## Proposed Amendment Requirements

| ReqID | Requirement | Evidence | Status |
|---|---|---|---|
| SCA-PKT-001 | Any later SCOPE_CHANGE must preserve PKG-10 as future-boundary scope and must not activate current-release domain operation execution. | EVID-006; EVID-007 | PROPOSED |
| SCA-PKT-002 | Any later SCOPE_CHANGE must preserve the DEL-10-03 dependency on protected path/proposal path policy unless a source-grounded ruling proves satisfaction or non-applicability. | EVID-002; EVID-003; EVID-005 | PROPOSED |
| SCA-PKT-003 | Any later SCOPE_CHANGE must reconcile the DEL-10-02 opposite-direction interface row with the DEL-10-03 prerequisite row without silently waiving either row. | EVID-002; EVID-003; EVID-004; EVID-005 | PROPOSED |
| SCA-PKT-004 | Any later SCOPE_CHANGE must keep concrete path glob syntax, hook API, adapter manifest behavior, and acceptance evidence details as TBD unless accepted source evidence supplies them. | EVID-008; EVID-009 | PROPOSED |
| SCA-PKT-005 | Any later SCOPE_CHANGE must distinguish a dependency-edge ruling from a decomposition amendment, and must record which authority owns the accepted change. | EVID-002; EVID-003 | PROPOSED |

## Action Candidates

The packet action table is in `Proposed_SCA_Actions.csv`. The conservative candidates are:

- MODIFY dependency-row interpretation guidance for DEP-10-02-004.
- MODIFY dependency-row interpretation guidance for DEP-10-03-006.
- MODIFY decomposition or package/deliverable metadata only if SCOPE_CHANGE decides the current PKG-10 policy/proposal split needs clarification.
- TBD action for owner/ruling assignment because the accessible evidence does not name an owner.

## Acceptance Criteria

| Criterion | Pass Condition |
|---|---|
| Evidence-backed | Every action row cites at least one evidence ID. |
| No direct mutation | No packet text says product registers or deliverables have been changed by this packet. |
| Human-gated | `SCOPE_CHANGE_INIT.md` states that human initiation is required. |
| TBD preservation | Unresolved rulings remain marked `TBD`. |
| Authority separation | DepClosure evidence, decomposition authority, product dependency registers, and SCOPE_CHANGE gates remain separate. |

## Invariant Checks

- DEL-10-02 and DEL-10-03 remain PKG-10 future-boundary deliverables.
- Protected path policy remains sibling support for OperationProposal workflow.
- OperationProposal workflow remains dependent on explicit human gate and protected-path posture.
- Proposal artifacts do not become protected domain-engine truth.
- The packet does not report graph-wide blocked or unblocked state.
