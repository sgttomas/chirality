# TASK-SW-REVIEW Sealed Brief

RequestedBy: `WORKING-C2A-R1`
RunID: `SOW-STAGE2-EXEC-20260712-01-C2A-R1`
ParentInstanceID: `WORKING-C2A-R1`
ChildInstanceID: `TASK-SW-REVIEW`
AgentRole: `TASK` (Agent 2; no delegation)
TaskSkill: `software-code-review`
PackageID: `APP-FRONTEND-RUNTIME`
WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
ScopePath: `{WORKING_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A-R1/instances/TASK-SW-REVIEW`
PROFILE_PATH: `{WORKING_ROOT}/software-workflow.json`
ApplyEdits: `false`

## Objective

Independently review the manager-owned C2A-R1 exact-authority repair for
correctness, fail-closed behavior, regression risk, test sufficiency, evidence
coverage, and exact scope containment. Do not edit source.

## ImplementationBrief

The scanner must resolve isolated path-scoped dual format as `MIGRATION_DUAL`
only when the supplied authority equals exactly
`D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176` and the valid
`ScopeOfWork.md` binds that same exact value. Any other authority, including
syntactically valid `D-GOV-16@0123456`, must fail closed with no selected
production documents. Only two source paths are in this remediation.

## AcceptedBasis

- D-GOV-16 items 4 and 8 and ruling publication
  `7584718aa32b112e415331736d1a8e68c12ac176`;
- root amendment `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/amendments/C2F-REMEDIATION-001.md`;
- parent brief `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-C2A-R1/LAUNCH_BRIEF.md`;
- initial C2A package and RECON-C2F/EVAL-C2F returns.

## DiffBasis

Review the current working-tree versions of exactly:

1. `{WORKING_ROOT}/frontend/src/lib/workspace/filesystem.ts`
2. `{WORKING_ROOT}/frontend/src/__tests__/lib/workspace-deliverable-contract-scanner.test.ts`

The initial C2A final hashes were respectively
`f5e99eac407d1da5d1262a8e5e2664f789557719e207bddbbe4e9c6f26aaa2fb`
and `f51e0d4ce8f4e373878070a9ee576f9f2df94755625d78b497a0a8310c1597c9`.
The current remediation is the exact-equality constant/check and associated
positive/negative regression updates. Treat all other dirty repository paths
as external state.

## AllowedWriteTargets

- `{ScopePath}/**` for runtime-owned `RETURN.md`, `STATUS.json`, and optional
  `_run_records/**` only.

No source or other evidence write is authorized.

## AllowedTools

- `tools/software_workflow/validate_change_scope.py`
- `tools/software_workflow/select_affected_checks.py`

Use scope validation first. Read code/tests/evidence directly. Do not rerun
completed checks, install, release, use network/provider surfaces, or invoke
Git mutation.

## VerificationEvidence

- focused seam: 7 files / 75 tests PASS;
- registered full frontend test, typecheck, and root self-check PASS in
  `REGISTERED_CHECK_RESULTS.json`;
- registered frontend build and practitioner pytest PASS in
  `ADDITIONAL_CHECK_RESULTS.json`;
- owned-server premerge PASS in `PREMERGE_CHECK_RESULTS.json`.

## AcceptanceChecks

1. Exact ruled authority plus exact candidate binding, isolation, exact path,
   complete legacy kit, and valid SOW is the only dual-format success path.
2. Unruled-looking, malformed, missing, non-isolated, wrong-path, binding
   mismatch, invalid SOW, partial legacy, and format mismatch fail closed with
   no selected production documents.
3. SOW-only and legacy-only behavior is unchanged.
4. Current source writes are exactly the two authorized paths; child writes
   remain inside this instance directory.
5. Evidence covers affected profile checks and required broader gates.

## ExpectedReturn

Return `SUCCESS | FAILED` with actionable findings (file and best-effort line),
blocking/non-blocking classification, scope verdict, evidence-coverage
verdict, residual risk, and manager fan-in recommendation. Produce terminal
`RETURN.md` and `STATUS.json` in this instance directory. Do not delegate.

## EXCLUSIONS

No source edit; no deliverable/control/status/lifecycle/receipt/Git/provider/
network/release/H1/H2/legacy-retirement action; no review of unrelated dirty
files; no lifecycle acceptance.
