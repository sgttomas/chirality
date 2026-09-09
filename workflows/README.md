# Workflows

A workflow describes how to carry an undertaking through: its methods, decisions,
relationships, artifacts, and recovery. It can branch, iterate, and coordinate
several contributions. Agents bring the role; workflows bring the method; a brief
binds both to the present work.

## Select and load

Select explicitly with `Workflow: <name>`. The inventory is the immediate
subdirectories containing `WORKFLOW.md`. Discover names when needed; routine role
context loads no workflow catalog or bodies.

Resolve a selected workflow from any working directory:

```bash
python3 "$INSTRUCTION_ROOT/tools/workflow_runtime/resolve_workflow.py"   --root "$INSTRUCTION_ROOT" --role TASK --workflow deliverable-consistency
```

Supply `--resource CONTRACT.md` or another package-relative resource only when the
current stage needs it. The resolver returns selected context and fingerprints.
A workflow can be omitted for an assignment expressed entirely through its brief.

WORKING_ITEMS owns orchestration. TASK performs a bounded contribution, including
a separately specified stage of a larger workflow. HELPS_HUMANS can use a
compatible workflow while developing the design. Loading a method grants no
additional capabilities or decision rights.

## Package form

Each `workflows/<name>/WORKFLOW.md` begins with YAML `name` and `description`.
The body explains the undertaking in the structure it needs. Optional resources
hold detailed contracts, templates, examples, or helpers. There is no compulsory
set of companion documents.

Optional `execution.json` provides compatible roles and capability/command
restrictions. Stage-specific resources are selected explicitly without changing
role compatibility. See
[the runtime contract](../docs/AGENT_WORKFLOW_RUNTIME.md). A command is invoked
through the available session tools, against the declared tool root. A documented
operation does not imply that the host exposes or enforces it.

## Compatibility and maintenance

`TaskSkill: <name>` remains a legacy input spelling. Supplying both fields with
different selections fails. [The legacy agent map](legacy-agents.json) resolves
retired names to the executing role and workflow or deterministic audit tool;
those names are not additional roles.

Existing package names and legacy status survive this migration. In particular,
`dbm-concordance-seed` remains legacy; `four-documents` serves legacy production
compatibility while `scope-of-work` carries the current SOW_V1 method. Historical
briefs, snapshots, and pinned evidence retain their original identifiers.

HELPS_HUMANS helps develop or revise workflows; WORKING_ITEMS coordinates their
implementation. Validate a package with the Root workflow validator and review
whether its particular method, outputs, and recovery fit its intended use.

The Root replacement format is held for adoption by incompatible App and Runtime
consumers. Their owning loops must adopt the registry and loading contract before
using these files as their runtime basis. Export staging is not a release.
