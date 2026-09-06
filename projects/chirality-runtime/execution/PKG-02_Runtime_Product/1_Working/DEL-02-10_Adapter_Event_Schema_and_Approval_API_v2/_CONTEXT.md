# Context: DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2

**Name:** Adapter Event Schema and Approval API v2
**Package:** PKG-02_Runtime_Product Generic Runtime Product
**Discipline:** TBD (not declared in accepted binding)
**Type:** API_CONTRACT
**Responsible:** Ryan Tufts (accountable human); WORKING_ITEMS (production manager); bounded Agent 2 executor by sealed brief
**Context Envelope:** M
**Objectives:** OBJ-001;OBJ-002;OBJ-004;OBJ-007
**Scope:** SOW-104
**Inherited Source Identity:** root::DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2

## Description
Define runtime API v2 with attributed approval request/decision records, managed-network prompt routing, a closed HarnessEvent schema v2 with four terminal events, and adapter projection that rejects, redacts, or projects unknown provider payloads. Represent Agent 0/1/2 role-entry parity and the explicit Agent 2/TASK fallback labelled role not mechanically enforced, with governed-workflow evidence marked instruction-asserted when G-ROLE cannot mechanically prove non-delegation.

## Anticipated Artifacts
- Runtime API v2 contract
- attributed approval request and decision schemas
- closed HarnessEvent v2 union whose only terminal identifiers are turn.completed, turn.failed, turn.interrupted, and turn.cancelled
- role-posture and instruction-asserted evidence projection
- networkApprovalContext routing showing host/protocol, same-destination queued-request grouping caveat, and acceptForSession only by explicit user act
- adapter projection and redaction fixtures

## Decomposition Reference
- **Decomposition:** projects/chirality-runtime/execution/_Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md
- **Deliverable ID:** DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2
