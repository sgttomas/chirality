# Return — TASK-PKG02-API-KEY-STATUS-CONSUMER-REVIEW-01

RUN_STATUS: FAILED

ReviewVerdict: **FAIL**

ControlSurface: FILE

TaskProfile: NONE

TaskSkill: software-code-review

ScopePath: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback`

ResolvedSkillPath: `/Users/ryan/.codex/worktrees/ef5e/chirality/skills/software-code-review`

ResolvedSkillVersion: `1`

ResolvedTaskProfileRequirement: NONE

CompanionFiles: `BRIEF_SCHEMA.md (found), TOOL_POLICY.md (found), QA_CHECKS.md (found)`

AllowedTools:

- `python3 tools/software_workflow/validate_change_scope.py:*`
- `python3 tools/software_workflow/select_affected_checks.py:*`
- `python3 tools/software_workflow/compare_structured.py:*`
- `python3 tools/software_workflow/verify_generated_manifest.py:*`

RuntimeOverrides: none

ToolsUsed:

- `python3 tools/software_workflow/validate_change_scope.py`
- `python3 tools/software_workflow/select_affected_checks.py`

ToolPolicyCompliance: PASS

WriteAuthorization: review-instance `STATUS.json` and `RETURN.md` only

## Frozen identity and scope

- Restarted verification against `FROZEN_DIFF_MANIFEST.md` frozen at
  `2026-08-20T16:10:00Z` after the manager's evidence-only update.
- All **13/13** frozen SHA-256 identities matched, including both accepted N1
  files, both N2 product/test files, all four DEL-02-05 calibration records,
  both implementer records, harness-pytest evidence, final APP-HOLD reliance,
  and final secret-scan evidence.
- Explicit N2 product/test scope validation: PASS, two paths, zero violations.
- Affected-check selection was run with project-relative paths, as required by
  the profile. It selects `frontend-test`, `frontend-typecheck`,
  `harness-pytest`, `harness-self-check`, and `app-hold-integrity`.
  `frontend-build` is additionally required by the sealed N2 brief and v2
  amendment.

## Full-source coverage

Read 100% of:

- `frontend/electron/api-key-ipc.ts` (191/191 lines);
- `frontend/src/__tests__/electron/api-key-ipc.test.ts` (297/297 lines);
- accepted N1 `frontend/electron/api-key-storage.ts` (223/223 lines); and
- accepted N1 `frontend/src/__tests__/electron/api-key-storage.test.ts`
  (339/339 lines).

The review also traced the runtime daemon's credential serialization,
`RuntimeClient.credentialStatus`, Electron main/preload registration, and the
settings-view consumer/tests. All four DEL-02-05 calibration records and the
R02/R03/R08 ScopeOfWork clauses were read in full or in their complete
governing sections.

## Actionable finding

### F1 — Blocking — required registered-check evidence is not persisted

Location:

- `projects/chirality-app-dev/AGENTS.md:93` requires the multi-agent record
  contract and, at lines 98-99, registered-check JSON written once per run.
- `instances/WI-PKG02-API-KEY-PRECEDENCE-01/LAUNCH_BRIEF.md:93` requires exact
  check evidence; lines 103-105 require the frontend, self-check,
  practitioner-harness, APP-HOLD, scope, parse/schema, whitespace, and diff
  gates.
- `instances/TASK-PKG02-API-KEY-STATUS-CONSUMER-IMPLEMENT-01/RETURN.md:61`
  through line 76 and its `STATUS.json:13` through line 22 contain only
  narrative PASS assertions for most checks.
- The frozen N2 manager evidence contains normalized JSON for
  `harness-pytest` only. It does not contain the registered-run JSON for
  `frontend-test`, `frontend-typecheck`, `frontend-build`,
  `harness-self-check`, or `app-hold-integrity`.

Impact: the reviewer cannot bind those asserted results to exact registered
commands, working directories, exit codes, durations, and outputs. The frozen
candidate therefore does not satisfy the App multi-agent evidence contract or
the N2 requirement for exact check evidence, even though the narrative results
are internally consistent.

Remediation: persist one manager-owned normalized registered-check JSON for the
missing checks (including the brief-required build), update the calibration
records only if their cited counts/results change, refreeze every evidence
identity, and dispatch a fresh read-only review. Preserve the already valid
`N2_MANAGER_HARNESS_PYTEST.json` or include that result in the complete
manager-owned evidence bundle.

## Product, contract, security, and lifecycle assessment

No actionable product-source finding was found:

- IPC no longer reads Anthropic or oMLX environment variables to infer source.
- It validates the daemon-owned `configured` and `source` fields, requires
  them to agree, projects only `hasKey`, `encryptionAvailable`, and
  `ui | env | none`, and fails malformed/missing/inconsistent responses closed.
- The accepted resolver order is safeStorage/UI, canonical
  `ANTHROPIC_API_KEY`, then compatibility alias
  `CHIRALITY_ANTHROPIC_API_KEY`; oMLX remains isolated.
- Store/remove, unsupported-provider, and daemon-unavailable behavior remain
  compatible. The unchanged runtime contract type omits `source`, but JSON
  serialization preserves the accepted N1 extra field and the N2 consumer
  deliberately treats the response as `unknown` before validation.
- No dependency or lockfile changed. The frozen secret scan reports 5,846
  files, zero blocked findings, and `rawSecretValuesWritten: false`.

The DEL-02-05 records truthfully preserve the dated 2026-06-20 assessment and
supersede only R03. State remains `IN_PROGRESS`; `## Remaining` is empty;
dependencies are unchanged; Checking Approval SHA remains
`8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`. No lifecycle promotion is made.

## Findings summary

- Blocking findings: **1** (F1, evidence completeness).
- Non-blocking findings: **0**.
- Product-source findings: **0**.

## Residual risk

The implementation itself is low residual risk based on complete source/test
review and consistent narrative results. Fan-in risk remains blocking until
the missing normalized registered-check evidence is frozen and independently
reviewed. Any product/test or calibration-byte change also invalidates this
review.

## Fan-in recommendation

**REJECT current N2 return for manager fan-in.** Do not release N3 from this
review. Remediate F1, refreeze, and obtain a fresh PASS with zero actionable
findings.

## Read-only confirmation

No candidate, deliverable, manager, shared, Git, lifecycle, commit, push, PR,
merge, release, or delegation action was performed. Writes were limited to
this review instance's `STATUS.json` and `RETURN.md`.

## MISSING

- Complete manager-owned normalized registered-check JSON described in F1.

## NEEDS_HUMAN_RULING

none

## DEPENDENCY_NOTES

- Accepted amended N1 was consumed byte-identically.
- N3 remains gated behind an accepted terminal N2 handoff.
