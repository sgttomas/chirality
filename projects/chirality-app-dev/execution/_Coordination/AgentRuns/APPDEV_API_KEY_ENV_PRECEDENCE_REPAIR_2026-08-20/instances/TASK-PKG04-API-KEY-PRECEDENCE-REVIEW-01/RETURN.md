# Return — TASK-PKG04-API-KEY-PRECEDENCE-REVIEW-01

RUN_STATUS: FAILED

Verdict: **FAIL** — one blocking actionable finding; manager fan-in is not
valid on the frozen evidence set.

ControlSurface: FILE

TaskProfile: NONE

TaskSkill: software-code-review

ScopePath: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge`

ResolvedSkillPath: `/Users/ryan/.codex/worktrees/ef5e/chirality/skills/software-code-review`

ResolvedSkillVersion: `1`

ResolvedTaskProfileRequirement: NONE

CompanionFiles: `BRIEF_SCHEMA.md (found), TOOL_POLICY.md (found), QA_CHECKS.md (found)`

AllowedTools: `python3 tools/software_workflow/validate_change_scope.py:*`,
`python3 tools/software_workflow/select_affected_checks.py:*`; repository
reads. Structured comparison and generated-manifest checks were not relevant.

RuntimeOverrides: none

WriteAuthorization: managed instance `STATUS.json` and `RETURN.md` only

## Blocking findings

1. **Required affected checks are absent from the frozen evidence.** The active
   profile registers `harness-self-check` and `app-hold-integrity` as
   `always_checks` at `projects/chirality-app-dev/software-workflow.json:38`.
   Deterministic affected-check selection for the two reviewed paths returned
   those checks in addition to `frontend-test` and `frontend-typecheck`. The
   frozen evidence at
   `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge/_run_records/TASK_RUN_2026-08-20_0911_REGISTERED_CHECKS.json:4-48`
   contains only `frontend-test`, `frontend-typecheck`, and the extra
   `frontend-build`; it contains no result for either always check. This also
   conflicts with the frozen N1 check contract at
   `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/ORCHESTRATION_PLAN.md:68-70`.

   Impact: the product/test behavior is supported by passing frontend evidence,
   but the declared registered-check and APP-HOLD integrity gates are
   incomplete, so the frozen return cannot advance to manager fan-in.

   Bounded remediation: run the registered `harness-self-check` and
   `app-hold-integrity` checks against the unchanged reviewed bytes, freeze
   their normalized passing evidence in a replacement manifest, and dispatch a
   fresh read-only review. No product or test change is requested by this
   finding.

## Identity and coverage

- Accepted basis: `6710ee6354debc201f6a454e2802897026cd4b38`.
- Frozen hashes: PASS, all 5 of 5 SHA-256 values independently recomputed and
  matched exactly.
- Scope validation: PASS, zero violations for the two declared product/test
  paths.
- Diff coverage: 100% of the exact basis diff inspected. It contains only a
  one-line Anthropic fallback reorder and the replacement of one expected-fail
  test with seven positive cases.
- File coverage: 100% of
  `projects/chirality-app-dev/frontend/electron/api-key-storage.ts` (212 lines)
  and
  `projects/chirality-app-dev/frontend/src/__tests__/electron/api-key-storage.test.ts`
  (284 lines) inspected.
- Call/contract trace: reviewed the runtime-host credential consumer and the
  IPC status path. No public interface, persistence, migration, generated
  artifact, dependency, or lockfile effect was introduced.

## Implementation assessment

No actionable code or test defect was identified. The implementation at
`projects/chirality-app-dev/frontend/electron/api-key-storage.ts:168-180`
resolves a non-whitespace safeStorage credential first, preserves the oMLX-only
environment branch, then resolves trimmed `ANTHROPIC_API_KEY` before trimmed
`CHIRALITY_ANTHROPIC_API_KEY`. The positive cases at
`projects/chirality-app-dev/frontend/src/__tests__/electron/api-key-storage.test.ts:210-283`
cover persisted UI precedence, each environment variable alone, both together,
and truthful whitespace fallthrough. This matches SPEC 12.3, PRD FR-030, and
DEL-04-05 RQ-001. The change is narrow and does not disturb storage or error
semantics.

The frozen frontend evidence reports focused coverage through the full suite
(150 passed files, 1 skipped; 1165 passed tests, 4 skipped), passing frontend
and Electron typecheck, and a passing build. Those results support the
implementation slice of AC-001/VER-001 but do not cure the blocking registered
always-check omission above.

## Risk and fan-in

- Blocking findings: 1 (verification coverage).
- Non-blocking findings: 0.
- Residual implementation risk: low; no defect found within the frozen
  two-file scope. This review did not re-establish broader DEL-04-05 lifecycle
  acceptance or release readiness.
- Fan-in validity: **INVALID** until the missing checks pass, their evidence is
  frozen, and a fresh review returns PASS with zero actionable findings.

## Rerun requirements

- Run registered `harness-self-check` and `app-hold-integrity` against the
  unchanged bytes.
- Re-freeze every reviewed artifact and evidence hash in a new manifest.
- Dispatch a fresh independent `software-code-review` review over that exact
  manifest and basis diff.
- If either product/test file changes, rerun the focused/full frontend test,
  typecheck, affected checks, and review from a newly frozen identity.

## Tools Used

- `python3 tools/software_workflow/validate_change_scope.py`
- `python3 tools/software_workflow/select_affected_checks.py`

ToolPolicyCompliance: PASS

Outputs:

- This managed `STATUS.json`.
- This managed `RETURN.md`.

MISSING:

- Frozen passing `harness-self-check` evidence.
- Frozen passing `app-hold-integrity` evidence.

NEEDS_HUMAN_RULING: none

DEPENDENCY_NOTES: none
