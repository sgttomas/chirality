# AUTHOR-DEL-09-01 Return

RUN_STATUS: FAILED_INPUTS

ControlSurface: FILE

TaskProfile: NONE

TaskSkill: scope-of-work

ScopePath: `{REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/AUTHOR-DEL-09-01/workspace`

ResolvedSkillPath: `{REPO_ROOT}/skills/scope-of-work`

ResolvedSkillVersion: 1

ResolvedTaskProfileRequirement: NONE

CompanionFiles: BRIEF_SCHEMA.md (found), TOOL_POLICY.md (found), QA_CHECKS.md (found)

AllowedTools: the six registered `python3 tools/scope_of_work/*.py` command specifications from the skill; none invoked because normalization failed first

RuntimeOverrides: MODE=CONVERT; DELIVERABLE_PATH equals the sealed ScopePath; DECOMPOSITION_BASIS, PROJECT_SCOPE_REFS, PACKAGE_OBJECTIVE_REFS, MODE_AUTHORITY, FORMAT_AUTHORITY_REF, SOURCE_STATE, and RENDER_HTML as sealed in `LAUNCH_BRIEF.md`

ToolsUsed:

- none

ToolPolicyCompliance: PASS

WriteAuthorization: ALLOWED_WRITE_TARGETS

Outputs:

- Terminal `STATUS.json` and this `RETURN.md` in the child evidence directory.

MISSING:

- The exact sealed ScopePath does not exist. The brief says the workspace is pre-created, but only the child directory and `LAUNCH_BRIEF.md` exist.
- No candidate, conversion evidence, checklist, render, manifest, or TASK run record was produced.

NEEDS_HUMAN_RULING:

- none

DEPENDENCY_NOTES:

- none

AppliedChanges:

- Recorded this terminal fail-closed return only; no project, candidate, Git, lifecycle, or workspace source files were written.

## Failure basis

`AGENT_TASK.md` normalization rule 8 requires `ScopePath` to resolve to an existing local path. Because the sealed ScopePath is absent, execution must stop before the run-record lifecycle, source seeding, hashing, converter invocation, or any downstream QA.

## Rerun requirement

The parent must pre-create exactly:

`execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-A3-PKG09/children/AUTHOR-DEL-09-01/workspace`

Then launch a fresh TASK run against the unchanged accepted basis. This failed instance must not be repaired after the fact.
