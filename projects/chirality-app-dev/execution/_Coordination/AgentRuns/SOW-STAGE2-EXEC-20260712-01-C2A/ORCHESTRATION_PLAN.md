# C2A App Frontend Runtime Activation Plan

Status: `ACTIVE — IMPLEMENTATION PENDING`
Parent: root `SOW-STAGE2-EXEC-20260712-01`
Manager: `WORKING_ITEMS`
PackageID: `APP-FRONTEND-RUNTIME`
PackagePath: `projects/chirality-app-dev/frontend`
Selection authority: `HUMAN` through accepted D-GOV-16 Stage-2 plan
Posture: `TERMINAL_FAN_OUT_IN` with sequential children
Graph version: `1`

## Objective and basis

Prepare and independently review the App runtime transition from Stage-1
`PILOT_DUAL`/feature-flag behavior to the live `SOW_V1` and transitional
`LEGACY_FOUR_DOC` contract. SOW-only and legacy-only folders must resolve and
render correctly; missing, partial, invalid, and unauthorized dual folders
must fail closed. Control-plane and DOMAIN/KTY documents remain unaffected.

Basis is synchronized root `main@e150c972889d05a8fc270239451a35c7512dc9a9`,
accepted P1_CANON, the P0 caller manifest, D-GOV-16, and the project-local
instructions, standing plan, newest Receipt 50, and
`software-workflow.json`. Root C2R candidate changes are external disjoint
state and not App authority.

## Work graph and boundaries

`IMPL` uses `TASK + software-bounded-implementation` and is the serialized
project-root Bash/integration owner. `REVIEW` depends on `IMPL` and uses
`TASK + software-code-review` read-only on source, writing only review
evidence. WORKING_ITEMS validates both returns and the registered checks.

No child may delegate. No provider/network expansion, release/distribution,
domain-engine work, issuance, lifecycle/status, project deliverable, root
governance, receipt, Git, or H1/H2 action is allowed. Any additional source
caller or write target is a cross-package notice and blocks dependent work.

The C2A candidate is derivative until C2F and CHANGE C2G. This package does
not accept or integrate itself.
