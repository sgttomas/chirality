# Context: DEL-02-07

**Name:** Process Supervisor and Purpose-Limited Control
**Package:** PKG-02 Operative Instruction Surface and Runtime Layers
**Type:** BACKEND_FEATURE_SLICE
**Responsible:** Ryan Tufts
**Context Envelope:** M

## Description

Provide DelegatedHarnessProcessSupervisorPort, the purpose-limited second private Unix socket, worker acquisition/inventory/reconnect, generation fencing and stale recovery, and the daemon-plus-supervisor two-job launch topology while retaining one daemon as the sole runtime broker and no TCP listener. Require authentication-token validation for every socket request, with each token bound to the socket owner and worker generation and invalidated during stale-socket recovery. Preserve Agent 0/1/2 role-entry parity for primary Codex sessions inside unchanged hard filesystem/network/process containment.

## Anticipated Artifacts

- DelegatedHarnessProcessSupervisorPort contract
- purpose-limited Unix-socket protocol with 0700/0600 ownership controls and authentication-token, owner, generation, and stale-recovery rules
- worker acquisition inventory reconnect and generation-fencing implementation
- daemon-plus-supervisor launch integration
- Agent 0/1/2 role-entry parity and hard-containment tests

## Scope and Objective Mappings

- Scope items: SOW-104
- Objectives: OBJ-001, OBJ-002, OBJ-004, OBJ-007

## Context Boundary

One cohesive PKG-02 supervisor/control slice; delegated-harness-native descent does not assign a role, the daemon remains the sole runtime broker, and the socket is never renderer- or CLI-callable. The purpose-limited control surface is a private Unix socket; no TCP listener is introduced.

## Anticipated Write Locus

`runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control/**`

This locus is an accepted planning note, never authorization. Implementation remains separately gated.

## Accepted Source

- Applied revision-1.3 deliverable-register row: `DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control`
- Approved propagation boundary: `execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md` §2, INIT-01
