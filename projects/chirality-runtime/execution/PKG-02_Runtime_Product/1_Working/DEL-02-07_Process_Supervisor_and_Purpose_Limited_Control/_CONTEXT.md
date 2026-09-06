# Context: DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control

**Name:** Process Supervisor and Purpose-Limited Control
**Package:** PKG-02_Runtime_Product Generic Runtime Product
**Discipline:** Not specified in accepted decomposition
**Type:** BACKEND_FEATURE_SLICE
**Responsible:** Ryan Tufts (accountable human); WORKING_ITEMS (production manager); bounded Agent 2 executor by sealed brief
**Context Envelope:** M
**Objectives:** OBJ-001;OBJ-002;OBJ-004;OBJ-007
**Scope:** SOW-104
**Inherited Source Identity:** root::DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control

## Description
Provide DelegatedHarnessProcessSupervisorPort, the purpose-limited second private Unix socket, worker acquisition/inventory/reconnect, generation fencing and stale recovery, and the daemon-plus-supervisor two-job launch topology while retaining one daemon as the sole runtime broker and no TCP listener. Require authentication-token validation for every socket request, with each token bound to the socket owner and worker generation and invalidated during stale-socket recovery. Preserve Agent 0/1/2 role-entry parity for primary Codex sessions inside unchanged hard filesystem/network/process containment.

## Anticipated Artifacts
- DelegatedHarnessProcessSupervisorPort contract
- purpose-limited Unix-socket protocol with 0700/0600 ownership controls and authentication-token, owner, generation, and stale-recovery rules
- worker acquisition inventory reconnect and generation-fencing implementation
- daemon-plus-supervisor launch integration
- Agent 0/1/2 role-entry parity and hard-containment tests

## Decomposition Reference
- **Decomposition:** projects/chirality-runtime/execution/_Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md
- **Deliverable ID:** DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control
