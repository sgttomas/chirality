# Software Workflow Activation Profile

**Status:** RATIFIED by the owner-approved Agent Hierarchy and Multi-Agent
Orchestration implementation plan (2026-07-11).

## Purpose

Software development is a specialization of package work, not a separate
manager role in this tranche. Use:

```text
WORKING_ITEMS Agent 1
+ one project-local software-workflow.json
+ software-* TASK skills
+ deterministic tools/software_workflow helpers
```

The profile freezes project-specific check commands and path-to-check mappings.
It does not authorize work, expand a brief, or replace accepted project and
decomposition state.

## Activation

A WORKING_ITEMS package activation identifies:

- the package and selected deliverables;
- the accepted project/decomposition basis;
- the project-local `software-workflow.json`;
- changed or expected paths;
- applicable software TASK skills;
- write ownership and fan-in gates;
- human decision points.

Novel stacks may use a sealed ephemeral generalist Agent 2. Repeated methods
graduate into a skill. HELPS_HUMANS may propose a dedicated SOFTWARE_DEV Agent
1 only after project trials demonstrate stable manager semantics that
WORKING_ITEMS cannot safely carry.

## Profile schema

Profiles use `chirality-software-workflow/v1` JSON:

```json
{
  "schema": "chirality-software-workflow/v1",
  "project_root": ".",
  "workspace_root": ".",
  "checks": {
    "unit": {"cwd": ".", "command": ["python3", "-m", "pytest", "-q"]}
  },
  "always_checks": [],
  "path_rules": [
    {"paths": ["src/**"], "checks": ["unit"]}
  ]
}
```

`project_root` defines project-relative path rules. `workspace_root` is the
outer containment boundary for registered check working directories and may
include repository-level governance checks. Commands are argument arrays
executed without a shell. A profile is a
registered tool surface, not permission to run unlisted commands. Agent briefs
still declare the checks and write targets allowed for the run.

## Canonical tool responsibilities

- `discover_repository.py`: manifests and test surfaces.
- `select_affected_checks.py`: deterministic path-rule selection.
- `run_registered_checks.py`: registered checks and normalized JSON evidence.
- `validate_change_scope.py`: changed-path containment.
- `compare_structured.py`: JSON API/schema/migration comparison.
- `verify_generated_manifest.py`: generated-file digest drift.

Tool output is generated evidence. It becomes accepted workflow state only
through the owning manager's validation and applicable human gates.
