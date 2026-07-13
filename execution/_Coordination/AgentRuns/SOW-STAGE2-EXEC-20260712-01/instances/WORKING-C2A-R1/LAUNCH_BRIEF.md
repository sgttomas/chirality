# WORKING-C2A-R1 Launch Brief — v1

Role: `WORKING_ITEMS` (Agent 1 App frontend repair owner)

Package: `APP-FRONTEND-RUNTIME`

## Objective

Repair the App content/authority defect confirmed by RECON-C2F and EVAL-C2F:
an isolated path-scoped dual-format scan may resolve `MIGRATION_DUAL` only when
its authority equals exactly
`D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176` and the candidate binds that
same exact value. Syntactically valid but unruled authorities, including
`D-GOV-16@0123456`, must fail closed.

## Basis and write scope

Read D-GOV-16 items 4/8, accepted Stage-2 plan, initial C2A package evidence,
RECON-C2F/EVAL-C2F findings, and C2F-REMEDIATION-001.

Only these source paths may change:

- `projects/chirality-app-dev/frontend/src/lib/workspace/filesystem.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/workspace-deliverable-contract-scanner.test.ts`

Evidence writes are limited to:

- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A-R1/**`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-C2A-R1/**`

Preserve every other dirty source/evidence path. One sequential TASK
`software-code-review` child is permitted after the manager-owned bounded
repair; record its sealed brief/status before dispatch. No implementation
child is needed for this two-path corrective tranche.

## Acceptance

- exact ruled authority + isolation + exact path + bound valid candidate can
  resolve `MIGRATION_DUAL`;
- unruled valid-looking authority, missing/malformed/mismatched authority,
  non-isolated mode, wrong path, invalid SOW, partial legacy, and requested
  format mismatch fail closed with no selected production documents;
- SOW-only, legacy-only, Domain/KTY separation, DocumentView behavior, and
  prior fail-closed repair remain unchanged;
- run focused scanner/route/runtime tests, full frontend, typecheck, build,
  self-check, practitioner tests, applicable owned-server premerge, exact
  containment, and diff hygiene; classify substrate separately.

No deliverable/control/status/lifecycle/receipt/Git/provider/network/release/
H1/H2/legacy-retirement action. Return terminal `PASS | PARTIAL | BLOCKED |
DECISION_REQUIRED` with evidence, exact paths/hashes, blocker closure,
remaining blockers, reruns, and next owner.
