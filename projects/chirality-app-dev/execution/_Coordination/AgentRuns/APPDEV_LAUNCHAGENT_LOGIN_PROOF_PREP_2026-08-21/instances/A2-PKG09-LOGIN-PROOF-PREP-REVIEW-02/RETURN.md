# TASK return — fresh post-remediation login-proof review

RUN_STATUS: FAILED

ControlSurface: FILE

TaskProfile: NONE

TaskSkill: software-code-review

ScopePath: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`

ResolvedSkillPath: `/Users/ryan/.codex/worktrees/ef5e/chirality/skills/software-code-review`

ResolvedSkillVersion: `1`

ResolvedTaskProfileRequirement: `NONE`

CompanionFiles: `BRIEF_SCHEMA.md (found), TOOL_POLICY.md (found), QA_CHECKS.md (found)`

AllowedTools: `python3 tools/software_workflow/select_affected_checks.py:*`, `python3 tools/software_workflow/validate_change_scope.py:*`, `python3 tools/software_workflow/compare_structured.py:*`, `python3 tools/software_workflow/verify_generated_manifest.py:*`

RuntimeOverrides: none

WriteAuthorization: runtime-owned `RETURN.md` / `STATUS.json` only

## Terminal verdict

`FAIL` — one actionable evidence-contract finding remains. The candidate is not
valid for manager fan-in until it is remediated and freshly re-reviewed.

## Hash verification and review coverage

- `frontend/scripts/run-packaged-launchagent-login-proof.mjs`: 875 lines read
  (100%); SHA-256
  `4c524234788cc2e0963dab2e9417475da0b2843f22fdb7f9fca898f57ef370a0`,
  exactly matching `FROZEN_PRODUCT_DIFF_02.md`.
- `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`:
  437 lines read (100%); SHA-256
  `434406fee9bf15b80e46f60a043d953fc0ab45b8aa8928a705f606f4d16b09d4`,
  exactly matching `FROZEN_PRODUCT_DIFF_02.md`.
- Both files were reviewed completely as new files against `/dev/null`.

## Scope and evidence audit

- Deterministic exact two-path scope validation: `PASS`; no violations.
- Affected-check selection: `app-hold-integrity`, `frontend-test`,
  `frontend-typecheck`, and `harness-self-check`. The sealed evidence records
  syntax `PASS`, focused Vitest `1 file / 11 tests PASS`, and exact scope
  `PASS`; the selected full/always checks remain manager fan-in gates.
- The mandatory concrete source-revision remediation is present before session
  creation and install, rejects blank/path-like/placeholder identities, binds
  the value into private and public state, and revalidates it during capture.
- Loaded-job cleanup validates running state, exact program and argv, PID, and
  unique packaged executable identity before each `bootout`. The focused
  missing-argv/program/argv/executable-ambiguity cases issue no `bootout`.
- The harness performs no logout/login, `bootstrap`, or `kickstart`; preparation
  does not claim proof; the default operator LaunchAgent is recorded and
  checked but excluded from mutation targets; public evidence excludes private
  capture state and uses redacted path representations.
- No live harness, LaunchAgent, host, Git, network, or release action was
  invoked by this review.

## Actionable finding

### [P2] Report every ownership-validation refusal as a refused mutation

Location:
`frontend/scripts/run-packaged-launchagent-login-proof.mjs:358-385` and
`:403-427`.

`cleanupProof()` sets `jobMutationRefused` only when the thrown message begins
with `Refusing proof-service bootout`. Several ownership-validation failures do
not use that prefix: `parseLaunchctlJob()` can throw for ambiguous process or
argument identity, and `inspectProcessExecutables()` can throw when executable
identity cannot be inspected. In those cases the code safely issues no
`bootout` and ultimately fails the proof, but emits
`cleanup.jobMutationRefused: false`. That contradicts the remediation contract
that missing or ambiguous identity records a refused mutation and makes the
evidence package misstate why cleanup remained incomplete.

Remediation: treat any failure returned from the ownership-validation call as
a mutation refusal independently of message text, break without `bootout`, and
add focused duplicate/ambiguous launchctl-identity and executable-inspection
failure tests asserting `jobMutationRefused: true` and zero `bootout` calls.

## Residual risks

- Actual logout/login, launchd login discovery, auto-start, capture, and
  evidence packaging remain unexecuted, owner-gated, and unproved.
- Mocked tests cannot establish macOS launchd timing or host behavior.
- The accepted contract treats the required path-free source-revision token as
  the source identity; the harness does not independently query Git or package
  metadata to authenticate that operator-supplied token.

ToolsUsed:

- `python3 tools/software_workflow/validate_change_scope.py`
- `python3 tools/software_workflow/select_affected_checks.py`
- direct read-only source inspection (`sed`, `nl`, `rg`)
- read-only hash/line verification (`shasum`, `wc`)

ToolPolicyCompliance: PASS — scope validation ran first, affected checks were
selected next, and remaining commands were direct read-only inspection. No
unregistered product command or check was executed.

Outputs:

- This `RETURN.md`
- Runtime-owned terminal `STATUS.json`

MISSING:

- Remediation and fresh re-review of the finding above.
- Owner-gated on-host proof, intentionally not executed.

NEEDS_HUMAN_RULING:

- none

DEPENDENCY_NOTES:

- Manager fan-in remains blocked on the finding above; no dependency cycle was
  observed.

ProposedChanges:

- Make the ownership-validation result, rather than exception-message text,
  control the mutation-refusal evidence flag and no-bootout exit.
