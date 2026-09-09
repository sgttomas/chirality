# AGENTS — Roles and Runtime Entry

An agent is an LLM with instructions, declared context, tools, and permissions.
A role describes its contribution; a workflow describes how an undertaking is
performed. The human remains accountable for what is accepted or relied upon.

| Role | Type | Contribution |
|---|---|---|
| HELP_HUMAN | 0 | Meet the human, maintain alignment and continuity, coordinate managers |
| HELPS_HUMANS | 1 | Help conceive and design workflows, tools, and projects |
| WORKING_ITEMS | 1 | Organize implementation, delegate bounded work, integrate results |
| TASK | 2 | Execute a bounded assignment, with a workflow when applicable |

The human may start an untyped session or directly select HELP_HUMAN,
HELPS_HUMANS, or WORKING_ITEMS. TASK is a delegated executor. HELP_HUMAN may
coordinate the two managers or dispatch bounded Type 2 work directly. Managers
dispatch TASK or ephemeral Type 2 instances. Type 2 does not delegate.

Read the selected `agents/AGENT_<ROLE>.md`. The machine-readable inventory and
capability ceilings are in `agents/registry.json`. Each run's brief supplies
its actual context, permissions, write targets, outputs, and acceptance checks.
WORKING_ITEMS may manage a package, deliverables, or another bounded undertaking;
a named workflow is optional.

Select workflows explicitly with `Workflow: <name>` and load
`workflows/<name>/WORKFLOW.md`, then resources needed for the current stage.
Use `workflows/README.md` for deliberate discovery. Routine role context carries
no workflow catalog. Legacy `TaskSkill` selection is resolved by the compatibility
adapter. A workflow never changes role type or grants capabilities.

Executable delegation uses either Chirality-managed `delegate_agent` sessions
or the delegated-harness-native facility under D-GOV-35. Record the actual
mechanism, parentage, source basis, scopes, and returns. Native descent does not
assign a role; distinguish instruction-asserted boundaries from mechanically
enforced ones. An executing child and a written launch brief are different facts.

The shared governance remains in `docs/DIRECTIVE.md`, `docs/CONTRACT.md`,
`docs/SPEC.md`, and `docs/TYPES.md`, with accepted amendments. Component design is
specified in `docs/WORKFLOW_COMPONENT_STANDARD.md`; configuration, loading,
coordination, and adoption are specified in `docs/AGENT_WORKFLOW_RUNTIME.md`.
The decomposition standard governs applicable decomposition workflows.

Instruction changes require their own authorized scope and tranche manifest.
Notify each affected project loop whose authority corpus or contract mirrors pin
changed instructions. Notices communicate changes; each receiving loop decides
its adoption and updates its own accepted basis.

This four-role format is the D-GOV-41 candidate replacement. Incompatible App and
Runtime consumers remain on their accepted instruction basis until their owning
loops adopt the replacement interface. Root `CLAUDE.md` imports this file.
