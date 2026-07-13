# WORKING-C2A Sealed Package Brief

RequestedBy: `HELP_HUMAN`
RunID: `SOW-STAGE2-EXEC-20260712-01-C2A`
ParentInstanceID: root `SOW-STAGE2-EXEC-20260712-01`
InstanceID: `WORKING-C2A`
PackageID: `APP-FRONTEND-RUNTIME`
PackagePath: `projects/chirality-app-dev/frontend`
SelectedDeliverables: `INTEGRATION_SCOPE_ONLY — nine frozen callers`

## Objective and completion criteria

Activate the App runtime scanner/document view/tests for the D-GOV-16
production-format contract. Replace Stage-1 feature-flag/`PILOT_DUAL`
semantics with explicit `SOW_V1`, transitional `LEGACY_FOUR_DOC`, authorized
isolated `MIGRATION_DUAL`, fail-closed `AMBIGUOUS`/partial/missing/invalid
states, and correct selected canonical document display.

PASS requires implementation and separate read-only review children; exact
write containment; legacy-only and SOW-only PASS; missing, partial,
unauthorized dual, invalid, and misleading format requests fail closed;
control-plane and DOMAIN/KTY paths remain unaffected; and all registered plus
accepted C2A checks pass.

## Exact writable source paths

- `projects/chirality-app-dev/frontend/src/lib/workspace/filesystem.ts`
- `projects/chirality-app-dev/frontend/src/components/shell/document-view.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/api/project/deliverables-route.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/chirality-read-mcp.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/dependencies-register-contract.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/workspace-deliverable-api.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/workspace-deliverable-contract-scanner.test.ts`

Evidence writes are confined to this project run directory. All other project
and root paths are read-only. If implementation requires another source path,
return a typed cross-package notice and stop; do not expand the list.

## Child and check contract

Before each child dispatch, write its sealed brief/status under `instances/`.
Run children sequentially:

1. `TASK-SW-IMPL` with `TaskSkill: software-bounded-implementation`, exact
   source writes above, project-root read, registered profile tools, and
   required focused tests. As a Bash-bearing child it is the serialized
   project integration owner.
2. `TASK-SW-REVIEW` with `TaskSkill: software-code-review`, read-only source,
   review-evidence writes only, and explicit review of format resolution,
   fail-closed behavior, domain/control boundaries, and test sufficiency.

Manager fan-in runs the project profile-selected checks plus frontend build,
`npm run harness:validate:premerge`, focused scanner/view/API/MCP tests,
repo-wide self-check, and practitioner-harness pytest. Stop any owned dev
server before build/premerge. Record exact commands, exit codes, counts, and
skips.

Required package outputs: `CALLER_MANIFEST.tsv`, `CHANGED_PATHS.txt`,
`BEHAVIOR_MATRIX.md`, `TEST_RESULTS.md`, `HANDOFF_STATE.md`, child returns,
manager `RETURN.md`, and terminal `STATUS.json`.

No lifecycle/status/Remaining/memory/receipt update occurs because this is a
root-authorized runtime consumer activation candidate, not deliverable scope
execution or project-loop closeout. Return `PASS`, `PARTIAL`, `BLOCKED`, or
`DECISION_REQUIRED` to HELP_HUMAN. C2A PASS releases C2F only after C2R PASS.
