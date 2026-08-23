# Context: DEL-02-09

**Name:** Hosted Account and Consent Boundary
**Package:** PKG-02 Operative Instruction Surface and Runtime Layers
**Type:** SECURITY_CONTROL
**Responsible:** Ryan Tufts
**Context Envelope:** M

## Description

Provide HostedEngineConsentPort and the per-root hosted-account boundary: root-private app-owned CODEX_HOME, account/epoch and policy continuity, and K-ROLE-2 role-posture digest. Always offer Agent 0/1/2 role entry for Codex sessions; when G-ROLE cannot mechanically prove Agent-2 non-delegation, still offer explicit Agent 2/TASK labelled role not mechanically enforced. Each canonical root chooses under consent: no command network by default; ask per destination through networkApprovalContext showing host/protocol, with a grant possibly unblocking queued requests to the same destination and acceptForSession allowed only by explicit user act; or labelled command network on with network_access = true.

## Anticipated Artifacts

- HostedEngineConsentPort contract
- root-private CODEX_HOME and account-continuity controls
- K-ROLE-2 digest schema
- Agent 0/1/2 parity and labelled Agent 2/TASK fallback controls
- per-root three-posture consent-state model
- isolation consent and continuity tests

## Scope and Objective Mappings

- Scope items: SOW-104
- Objectives: OBJ-001, OBJ-002, OBJ-004, OBJ-007

## Context Boundary

One cohesive account/consent security boundary carrying G0 A3 and A7. Ambient `~/.codex` is excluded, consent never crosses root, account, or policy-digest drift, and hard filesystem/network/process containment is unchanged.

## Anticipated Write Locus

`runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-09_Hosted_Account_and_Consent_Boundary/**`

This locus is an accepted planning note, never authorization. Implementation remains separately gated.

## Accepted Source

- Applied revision-1.3 deliverable-register row: `DEL-02-09_Hosted_Account_and_Consent_Boundary`
- Approved propagation boundary: `execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md` §2, INIT-03
