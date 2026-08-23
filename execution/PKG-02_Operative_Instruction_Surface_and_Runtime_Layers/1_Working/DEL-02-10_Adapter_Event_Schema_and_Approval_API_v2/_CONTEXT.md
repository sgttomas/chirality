# Context: DEL-02-10

**Name:** Adapter Event Schema and Approval API v2
**Package:** PKG-02 Operative Instruction Surface and Runtime Layers
**Type:** API_CONTRACT
**Responsible:** Ryan Tufts
**Context Envelope:** M

## Description

Define Root runtime API v2 with attributed approval request/decision records, managed-network prompt routing, a closed HarnessEvent schema v2 with four terminal events, and adapter projection that rejects, redacts, or projects unknown provider payloads. Represent Agent 0/1/2 role-entry parity and the explicit Agent 2/TASK fallback labelled role not mechanically enforced, with governed-workflow evidence marked instruction-asserted when G-ROLE cannot mechanically prove non-delegation.

## Anticipated Artifacts

- Root runtime API v2 contract
- attributed approval request and decision schemas
- closed HarnessEvent v2 union whose only terminal identifiers are `turn.completed`, `turn.failed`, `turn.interrupted`, and `turn.cancelled`
- role-posture and instruction-asserted evidence projection
- networkApprovalContext routing showing host/protocol, same-destination queued-request grouping caveat, and acceptForSession only by explicit user act
- adapter projection and redaction fixtures

## Scope and Objective Mappings

- Scope items: SOW-104
- Objectives: OBJ-001, OBJ-002, OBJ-004, OBJ-007

## Context Boundary

One versioned adapter/API slice carrying G0 A7 with deterministic wire fixtures. Managed prompts implement ask per destination, no command network remains the default, labelled `network_access = true` is the command-network-on posture, and provider-shaped persistence and unattributed decisions are excluded.

## Anticipated Write Locus

`runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2/**`

This locus is an accepted planning note, never authorization. Implementation remains separately gated.

## Accepted Source

- Applied revision-1.3 deliverable-register row: `DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2`
- Approved propagation boundary: `execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md` §2, INIT-04
