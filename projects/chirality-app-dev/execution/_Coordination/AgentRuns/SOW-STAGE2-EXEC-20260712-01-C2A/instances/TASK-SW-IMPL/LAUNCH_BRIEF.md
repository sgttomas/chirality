# TASK-SW-IMPL Sealed Brief

RequestedBy: `WORKING-C2A`
RunID: `SOW-STAGE2-EXEC-20260712-01-C2A`
ParentInstanceID: `WORKING-C2A`
ChildInstanceID: `TASK-SW-IMPL`
AgentRole: `TASK` (Agent 2; no delegation)
TaskSkill: `software-bounded-implementation`
PackageID: `APP-FRONTEND-RUNTIME`
DeliverableIDs: `INTEGRATION_SCOPE_ONLY — nine frozen callers`
WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
ScopePath: `{WORKING_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A/instances/TASK-SW-IMPL`
PROFILE_PATH: `{WORKING_ROOT}/software-workflow.json`
ApplyEdits: `true`

## Objective

Implement the C2A App runtime consumer activation for the ratified D-GOV-16
production-format contract. Replace Stage-1 feature-flag and `PILOT_DUAL`
semantics with explicit fail-closed resolution of `SOW_V1`, transitional
`LEGACY_FOUR_DOC`, authorized isolated `MIGRATION_DUAL`, `AMBIGUOUS`, and
`INVALID`, and make the document viewer expose the selected canonical
production document without a feature flag.

## Accepted basis

- synchronized root `main@e150c972889d05a8fc270239451a35c7512dc9a9`;
- accepted `P1_CANON` and
  `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/P1_CANON/POSTMERGE_HANDOFF.md`;
- live `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`, especially §§3, 7, and 10;
- D-GOV-16 ruling publication
  `7584718aa32b112e415331736d1a8e68c12ac176`;
- P0 `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/basis/CALLER_MANIFEST.tsv`;
- accepted `execution/_Coordination/AgentRuns/SOW-STAGE2-PLAN-20260712/CALLER_REFRESH.md` §D;
- project `AGENTS.md`, loop/profile sources, parent sealed brief, and this brief;
- root C2R candidate is external read-only evidence only. When useful, mirror
  its fail-closed vocabulary and `D-GOV-16@<accepted-sha>` authority syntax,
  but do not edit, integrate, or depend on its dirty source files.

## Dependencies

- `C1G_ACCEPTED`: satisfied.
- No dependency on C2R integration; root C2R dirt remains external read-only.
- `TASK-SW-REVIEW` remains parked until this return is accepted by WORKING-C2A.

## Exact allowed source writes

1. `{WORKING_ROOT}/frontend/src/lib/workspace/filesystem.ts`
2. `{WORKING_ROOT}/frontend/src/components/shell/document-view.tsx`
3. `{WORKING_ROOT}/frontend/src/__tests__/api/project/deliverables-route.test.ts`
4. `{WORKING_ROOT}/frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts`
5. `{WORKING_ROOT}/frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts`
6. `{WORKING_ROOT}/frontend/src/__tests__/lib/chirality-read-mcp.test.ts`
7. `{WORKING_ROOT}/frontend/src/__tests__/lib/dependencies-register-contract.test.ts`
8. `{WORKING_ROOT}/frontend/src/__tests__/lib/workspace-deliverable-api.test.ts`
9. `{WORKING_ROOT}/frontend/src/__tests__/lib/workspace-deliverable-contract-scanner.test.ts`

The child instance directory is additionally writable for its TASK run record,
normalized check output, and terminal `RETURN.md` / `STATUS.json`. No other
path may be written. Use `apply_patch` for source and evidence edits; check
commands may write only ignored build/test caches they normally own.

## Initial source identities

The nine source paths begin at the SHA-256 identities frozen in the P0 caller
manifest and reproduced in the manager's activation scan. Any pre-existing
delta on one of these paths is a conflict and must stop the child before edits.

## Required behavior

1. `LEGACY_FOUR_DOC`: exactly all four valid legacy production documents and
   no `ScopeOfWork.md`; transitional PASS and selected canonical documents are
   the four legacy files.
2. `SOW_V1`: one structurally valid `ScopeOfWork.md` and no legacy production
   documents; PASS and selected canonical production document is
   `ScopeOfWork.md`.
3. `MIGRATION_DUAL`: both complete valid formats are valid only when the caller
   explicitly asserts an isolated conversion workspace, supplies an exact
   `D-GOV-16@<accepted-sha>` migration authority, and the Scope of Work binds
   that same authority. The selected canonical production document remains
   `ScopeOfWork.md`; this state is never inferred in the normal project route.
4. Complete dual format without the exact authority/isolation/binding resolves
   `AMBIGUOUS`, fails closed, and selects no canonical production document.
5. Partial legacy kit, invalid/unreadable Scope of Work, missing production
   contract at or beyond `INITIALIZED`, misleading requested format, and other
   invalid combinations resolve/fail closed as `INVALID` or an explicit
   request mismatch with no selected canonical production document.
6. Preserve the required metadata, preparation, memory, optional-file,
   references-warning, and lifecycle findings. Do not convert warnings into
   hidden acceptance.
7. Keep control-plane files and DOMAIN/KTY detection/options unaffected. Do
   not apply the PROJECT/SOFTWARE production-format contract to independent
   schemas.
8. Remove `NEXT_PUBLIC_SCOPE_OF_WORK_PILOT`; the document viewer must normally
   offer `ScopeOfWork.md` and the legacy files so the selected canonical
   document can be displayed. Keep `_STATUS.md` as the viewer default unless
   existing API state gives a safer canonical selection without another write
   path.
9. Update only tests in the frozen nine-file set. Do not change API route or
   MCP implementation paths; their existing behavior must remain compatible
   through scanner output and tests.

## Acceptance criteria

- Tests prove legacy-only PASS and SOW-only PASS.
- Tests prove missing, partial, structurally invalid, unauthorized dual,
  authority mismatch, missing embedded binding, and misleading format request
  fail closed.
- Tests prove exact authorized isolated dual reports `MIGRATION_DUAL` and
  selects only `ScopeOfWork.md`.
- Tests prove normal project/API scans never infer authorized dual.
- Tests prove control-plane and DOMAIN/KTY paths/options remain unaffected.
- No Stage-1 pilot feature flag, `PILOT_DUAL`, or D-GOV-15 variance behavior
  remains in the nine active caller files.
- Registered `frontend-typecheck` and `frontend-test` checks pass, or the exact
  failure is returned. Do not run install, release, network, provider, desktop
  packaging, or unregistered lifecycle commands.
- `validate_change_scope.py` confirms every source write is one of the exact
  nine, with this child evidence directory separately accounted for.

## Allowed tools and checks

The effective skill allowlist is the five declared `tools/software_workflow/`
helpers. Use `select_affected_checks.py`, then
`run_registered_checks.py` for only `frontend-typecheck` and `frontend-test`,
and `validate_change_scope.py` before return. Direct targeted Vitest commands
may be proposed to the manager but must not replace registered evidence.

## Expected outputs and return

- minimal coherent implementation and tests in the exact nine source paths;
- child `_run_records/TASK_RUN_*.md`;
- child `CHECK_RESULTS.json` from registered checks;
- child `RETURN.md` with structured TASK report, changed paths, behavioral
  summary, exact commands/exit status/counts, write-fence result, residual
  risks, blockers, and coordination notices;
- child terminal `STATUS.json` with `PASS | PARTIAL | BLOCKED | FAILED`.

## EXCLUSIONS and escalation

No Git, PR, receipt, deliverable, lifecycle, status/Remaining, memory,
provider/network, release/distribution, domain-engine, issuance, H1, H2,
root-governance, root-tool, root-skill, or root-run mutation. Do not delegate.
If any additional source write target, caller, authority change, public
contract expansion, or acceptance change is needed, stop and return a typed
coordination notice to WORKING-C2A.
