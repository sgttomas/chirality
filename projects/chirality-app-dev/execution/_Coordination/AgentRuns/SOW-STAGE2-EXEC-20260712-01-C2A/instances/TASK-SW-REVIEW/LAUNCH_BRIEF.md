# TASK-SW-REVIEW Sealed Brief

RequestedBy: `WORKING-C2A`
RunID: `SOW-STAGE2-EXEC-20260712-01-C2A`
ParentInstanceID: `WORKING-C2A`
ChildInstanceID: `TASK-SW-REVIEW`
AgentRole: `TASK` (Agent 2; no delegation)
TaskSkill: `software-code-review`
PackageID: `APP-FRONTEND-RUNTIME`
WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
ScopePath: `{WORKING_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A/instances/TASK-SW-REVIEW`
PROFILE_PATH: `{WORKING_ROOT}/software-workflow.json`
ApplyEdits: `false`

## Objective

Independently review the manager-owned C2A implementation candidate for
correctness, regression risk, exact scope containment, the ratified D-GOV-16
format contract, fail-closed behavior, DOMAIN/KTY and control-plane boundaries,
canonical document selection, and test sufficiency. Do not edit source or
perform lifecycle acceptance.

## Accepted basis and implementation brief

- synchronized root `main@e150c972889d05a8fc270239451a35c7512dc9a9`;
- live `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` and D-GOV-16 ruling
  `7584718aa32b112e415331736d1a8e68c12ac176`;
- P0 caller manifest and accepted Stage-2 `CALLER_REFRESH.md` §D;
- parent sealed package brief and
  `instances/TASK-SW-IMPL/LAUNCH_BRIEF.md` as the original implementation
  contract;
- `SUBSTRATE_FALLBACK.md` and `instances/TASK-SW-IMPL/RETURN.md`: the first
  child failed for duration after valid reconnaissance; WORKING-C2A made the
  bounded implementation as serialized integration owner;
- root C2R dirt is external, disjoint, and read-only.

## Diff basis

Review the unstaged working-tree diff against `main@e150c972889d05a8fc270239451a35c7512dc9a9`
for exactly these four changed paths:

1. `{WORKING_ROOT}/frontend/src/lib/workspace/filesystem.ts`
2. `{WORKING_ROOT}/frontend/src/components/shell/document-view.tsx`
3. `{WORKING_ROOT}/frontend/src/__tests__/api/project/deliverables-route.test.ts`
4. `{WORKING_ROOT}/frontend/src/__tests__/lib/workspace-deliverable-contract-scanner.test.ts`

The remaining five frozen caller/test paths are unchanged and must remain
compatible. All project-run evidence is outside the source diff. All root
C2R/root governance dirt is external state and must be excluded from findings
unless it proves a direct contradiction in the four-path candidate.

## Verification evidence supplied

- exact focused Vitest command covering all seven frozen test files: PASS,
  7 files / 69 tests;
- `npm run typecheck`: PASS;
- `git diff --check -- projects/chirality-app-dev/frontend`: PASS;
- source diff currently contains only four of the nine exact allowed paths;
- no `PILOT_DUAL`, `NEXT_PUBLIC_SCOPE_OF_WORK_PILOT`, D-GOV-15, or
  `scopeOfWorkPilot` token remains in the nine-path seam.

The manager will independently rerun these and all broader fan-in gates after
review. Treat the supplied results as evidence to audit, not authority.

## Review requirements

1. Validate source changed-path containment before semantic review using
   `validate_change_scope.py` with the four explicit candidate paths and nine
   exact allowed roots. Ignore pre-existing root/C2R and project evidence dirt.
2. Confirm `SOW_V1` and `LEGACY_FOUR_DOC` PASS and select the right production
   documents.
3. Confirm `MIGRATION_DUAL` requires an isolated-workspace assertion, an exact
   `D-GOV-16@<7-64 lowercase hex>` authority, exact allowed deliverable path,
   structurally valid Scope of Work, and matching embedded
   `<!-- migration-authority: ... -->`; normal project scans must not infer it.
4. Confirm missing-at-or-beyond-INITIALIZED, partial legacy, invalid/unreadable
   Scope of Work, unauthorized dual, authority/binding mismatch, and misleading
   requested format fail closed and select no production document.
5. Confirm the resolver does not silently validate an `INVALID` or
   `AMBIGUOUS` state merely because other findings are warnings.
6. Confirm DocumentView uses scanner-selected canonical production documents,
   removes the feature flag, keeps `_STATUS.md` as the default, resets safely
   on deliverable change, and preserves control-plane choices.
7. Confirm DOMAIN/KTY knowledge decomposition and control-plane files remain
   unaffected; flag any accidental application of PROJECT/SOFTWARE format
   semantics to independent schemas.
8. Assess tests for exact authority mismatch, missing binding, invalid schema,
   partial/missing format, normal-route dual ambiguity, selected document
   output, and compatibility of the five unchanged callers/tests.
9. Report only actionable findings with exact file and best-effort line,
   impact, evidence, and remediation. Separate blockers from non-blocking
   residual risks. State `PASS` only when no unresolved correctness,
   authority, fail-closed, containment, or test-sufficiency finding remains.

## Allowed writes and tools

Source is read-only. The only write target is this child instance directory
for `_run_records/TASK_RUN_*.md`, `SCOPE_VALIDATION.json`, `RETURN.md`, and
terminal `STATUS.json`. The effective skill allowlist is its four declared
`tools/software_workflow/` helpers. Use scope validation first and affected
check selection to audit evidence coverage. Do not rerun tests, edit source,
install, release, access providers/network, or perform Git actions.

## Expected return

- structured TASK review report;
- exact scope-validation evidence;
- actionable findings or explicit `NO_FINDINGS`;
- residual risks and evidence gaps;
- verdict `PASS | PARTIAL | BLOCKED | FAILED` for manager fan-in only.

## EXCLUSIONS and escalation

No source edits, no implementation repair, no Git/PR, receipt, deliverable,
lifecycle/status/Remaining/memory, provider/network, release/distribution,
domain-engine, issuance, H1, H2, root-governance, or root-run mutation. Do not
delegate. Return any scope/authority/acceptance conflict to WORKING-C2A.
