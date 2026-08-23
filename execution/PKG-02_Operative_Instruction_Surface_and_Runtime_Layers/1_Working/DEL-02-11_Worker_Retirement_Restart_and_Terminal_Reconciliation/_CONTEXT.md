# Context: DEL-02-11

**Name:** Worker Retirement, Restart, and Terminal Reconciliation
**Package:** PKG-02 Operative Instruction Surface and Runtime Layers
**Type:** BACKEND_FEATURE_SLICE
**Responsible:** Ryan Tufts
**Context Envelope:** M

## Description

Provide WorkerRetirementCoordinatorPort, prepared/committed/reconciliation-required journal state, exactly-once active-turn terminalization, and restart behavior that uses thread/resume only under canonical-root, account-identity, and policy-digest continuity with canonical cwd, otherwise a fresh thread.

## Anticipated Artifacts

- WorkerRetirementCoordinatorPort contract
- retirement journal and reconciliation state
- exactly-once terminalization implementation
- conditional thread/resume continuity checks and fresh-thread fallback
- crash retirement and replay tests

## Scope and Objective Mappings

- Scope items: SOW-104
- Objectives: OBJ-001, OBJ-002, OBJ-004, OBJ-007

## Context Boundary

One bounded worker-retirement/recovery slice carrying G0 A4. It makes no in-flight re-attach or automatic replay claim.

## Anticipated Write Locus

`runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation/**`

This locus is an accepted planning note, never authorization. Implementation remains separately gated.

## Accepted Source

- Applied revision-1.3 deliverable-register row: `DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation`
- Approved propagation boundary: `execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md` §2, INIT-05
