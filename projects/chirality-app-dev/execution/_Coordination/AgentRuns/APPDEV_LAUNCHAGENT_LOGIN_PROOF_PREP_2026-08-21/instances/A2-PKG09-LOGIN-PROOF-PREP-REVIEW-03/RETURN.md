# TASK return — final fresh login-proof review

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

`FAIL` — one actionable blocking finding remains. The candidate is not valid
for manager fan-in until it is remediated and freshly re-reviewed.

## Hash verification and review coverage

- `frontend/scripts/run-packaged-launchagent-login-proof.mjs`: 877 lines read
  (100%); SHA-256
  `b7694d5cfb27a4c17fa1b692c989aa35749ea2d77999d6b6eafa817d9dccdcfb`,
  exactly matching `FROZEN_PRODUCT_DIFF_03.md`.
- `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`:
  447 lines read (100%); SHA-256
  `ad58fc182f5632ba83c52699309eb541ff7d5728308c5f2ac347a52a1e5dccc8`,
  exactly matching `FROZEN_PRODUCT_DIFF_03.md`.
- Both complete new files were reviewed against `/dev/null`.

## Scope and evidence audit

- Deterministic exact two-path scope validation: `PASS`; no violations.
- Affected checks are `app-hold-integrity`, `frontend-test`,
  `frontend-typecheck`, and `harness-self-check`. Sealed evidence records
  syntax `PASS`, focused Vitest `1 file / 13 tests PASS`, and exact scope
  `PASS`; full registered checks remain manager fan-in gates.
- Both prior P1 remediations remain effective: concrete source revision is
  mandatory and rebound at capture; loaded-job cleanup performs exact
  program/argv/PID/executable ownership validation before bootout.
- The prior P2 remediation is effective for capture cleanup: every exception
  from the ownership-validation boundary records `jobMutationRefused: true`
  and exits without bootout, independent of exception text.
- The harness exposes no logout/login, bootstrap, or kickstart operation;
  preparation makes no proof claim; the default operator job/plist is excluded
  from mutation targets; public evidence redacts host paths and excludes the
  private consumed capture state.
- No live harness, LaunchAgent, host, Git, network, install, release, or owner
  action was performed by this review.

## Actionable finding

### [P1] Clean up a partially completed packaged install when the command times out

Location: `frontend/scripts/run-packaged-launchagent-login-proof.mjs:507-526`
and `:590-604`.

`installed` becomes `true` only after the awaited packaged CLI install returns.
`defaultRunCommand()` rejects on timeout after killing the child. If the CLI
has already written the proof RunAtLoad plist or runtime state but has not
exited before that timeout, the assignment is never reached and the catch
skips `cleanupProof()`. The failed preparation can therefore leave a persistent
proof LaunchAgent that auto-starts at a later login, while emitting only the
command-timeout error and no cleanup-incomplete evidence. In the other
post-install validation failures where cleanup does run, its returned errors
are discarded, so residue is likewise not truthfully surfaced. The focused
suite has no partial-install-then-rejection/timeout regression.

Remediation: mark the install as attempted before awaiting it, and on every
post-attempt failure inspect and clean the exact proof-owned job/plist/runtime
targets. Preserve and surface any cleanup refusal or incomplete result instead
of discarding it. Add a focused regression whose install mock writes the plist
and then rejects, proving the plist/runtime are removed (or that incomplete
cleanup is explicitly reported) and no unreported login-autostart residue
remains.

## Residual risks

- Actual logout/login, launchd login discovery, auto-start, capture, and
  evidence packaging remain unexecuted, owner-gated, and unproved.
- Mocked tests cannot establish macOS launchd timing or host behavior.
- The source-revision token is operator supplied and syntactically validated;
  the harness does not independently authenticate it against Git/package
  metadata, matching the prior accepted review boundary.

ToolsUsed:

- `python3 tools/software_workflow/validate_change_scope.py`
- `python3 tools/software_workflow/select_affected_checks.py`
- direct read-only source/evidence inspection (`sed`, `nl`, `rg`)
- read-only hash/line verification (`shasum`, `wc`)

ToolPolicyCompliance: PASS — scope validation was the first deterministic
review tool, affected checks were selected next, and remaining commands were
direct read-only inspection. No unregistered product command or check ran.

Outputs:

- This `RETURN.md`.
- Runtime-owned terminal `STATUS.json`.

MISSING:

- Remediation and a fresh full-diff independent review.
- Owner-gated on-host proof, intentionally not executed.

NEEDS_HUMAN_RULING:

- none

DEPENDENCY_NOTES:

- Manager fan-in remains blocked on the finding above; no dependency cycle was
  observed.

ProposedChanges:

- Make every attempted packaged install enter proof-owned cleanup on failure,
  and truthfully surface incomplete cleanup.
- Add a partial-install rejection/timeout no-residue regression.
