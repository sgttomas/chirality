# Agent and Workflow Runtime Contract

Status: candidate replacement interface authorized for implementation by D-GOV-41.
App and Runtime adoption remains held until their owning loops accept compatible
consumers. This document describes configuration and loading, not host enforcement.

## Role configuration

`agents/registry.json` is the machine-readable role inventory. It has
`schema_version: 1` and a `roles` object keyed by the four role names. Each role
contains:

| Field | Meaning |
|---|---|
| `instruction` | Repository-relative path to its four-section instruction file |
| `type` | Integer 0, 1, or 2 |
| `direct_entry` | Whether the human may select this named role directly |
| `delegates_to` | Named roles eligible for managed delegation |
| `allow_generalist_agent2` | Whether bounded ephemeral Type 2 execution is eligible |
| `tools` | Role capability ceiling, using runtime capability names |
| `write_scope` | Scope ceiling description; actual writable targets come from the brief |

HELP_HUMAN is Type 0, directly selectable, with HELPS_HUMANS, WORKING_ITEMS, and
TASK as eligible named children. HELPS_HUMANS and WORKING_ITEMS are directly
selectable Type 1 roles and may dispatch TASK. These three roles may also use
bounded ephemeral Type 2 instances. TASK is Type 2, has no direct-entry or
delegation eligibility, and cannot launch another executor.

Native descendant creation and role assignment are distinct. The native
facility remains available under D-GOV-35; this registry states role conduct
and managed eligibility. A host must report the actual enforcement boundary.
The registry never grants a filesystem path or bypasses host permission checks.

## Workflow packages

The discoverable inventory consists of immediate `workflows/` subdirectories
containing `WORKFLOW.md`. Its YAML `name` matches the folder; `description`
explains the undertaking briefly. The body defines the method, including
branching, iteration, coordination, artifact contracts, and recovery when
applicable. Resources are optional and loaded as needed. Existing legacy
package status survives migration and is explicit in the workflow inventory.

Optional `execution.json` companions use `schema_version: 1`. They declare
`compatible_roles` and optional `tools` restrictions. `tools.capabilities` is a
list of runtime capability names. `tools.commands` is a list of legacy
`<interpreter> tools/path:<scope_glob>` expressions, preserved losslessly with
placeholders bound by the brief. Capability and command restrictions intersect
independently with their corresponding outer policies; never compare command
expressions with capability names. Missing restrictions inherit the applicable
outer policy; an explicit empty command list denies shell commands. A host that
cannot enforce an expression records the boundary as instruction-asserted. Absence of a companion means no additional workflow restriction;
it does not expand the role or brief. A workflow requiring delegation belongs
with a compatible manager. A TASK assignment selects a separately bounded child workflow or a bounded
brief. It cannot load an incompatible manager workflow by labelling the whole
workflow a bounded stage.

`Workflow: <name>` selects a workflow. `TaskSkill: <name>` is accepted by the
legacy-input adapter. If both select the same name, resolve once. Different
selections fail as conflicting input. Retired agent identifiers are resolved
through the migration ledger to a role and workflow, never re-registered as
roles. Historical evidence retains the identifiers actually used.

## Context and execution

The Root resolver returns the selected definition, its applicable execution
configuration, and source fingerprints. It reads only explicitly requested
resources for a stage. A selected resource must exist and remain within its
package after real-path resolution. Routine role context does not load the
workflow inventory, descriptions, or bodies. Explicit discovery is an operation
performed when selection needs it.

The run brief identifies purpose, governing basis, scope, required context,
tools, writable targets, expected outputs, acceptance checks, and return path.
A workflow may be omitted. Loading one does not grant permissions or alter role
type. Effective authorization is bounded by the host, role, workflow, and brief.
An empty explicit tool allowance permits no tools; a missing optional workflow
restriction adds no restriction. Write targets must be explicit and contained in
the authorized working root; `ScopePath` alone does not grant writes.

The tool root is declared independently from the working directory. Commands
resolve against that root or their workflow package. Agents invoke them through
available session capabilities and interpret their results according to the
workflow. A documented command is not evidence that a host exposes it.

Freeze role instructions, selected workflow/resources, and brief revisions for
a run. Record actual supplied context and hashes where the mechanism exposes
it. Describe instruction-mediated loading as instruction-asserted, separately
from mechanically recorded loading. Amendments name changed basis and scope;
new role instructions take effect between runs.

## Structured brief compatibility

The Root utility `tools/workflow_runtime/resolve_workflow.py` accepts
`--root <instruction-root> --role <role>` and optional `--workflow`,
`--task-skill`, or `--legacy-agent`. Repeat `--resource <package-relative-path>`
to request stage resources. No resource selection overrides whole-workflow
role compatibility.

`--brief <json-file> --repo-root <active-checkout>` accepts structured inline
fields and an optional structured file brief. `InitTaskPath`/`INIT_TASK_PATH`
selects that file; otherwise the adapter checks `ScopePath/INIT-TASK.md` and then
`DeliverablePath/INIT-TASK.md`. File values fill omitted inline fields; inline
values take precedence, while inconsistent path fields or aliases fail.
The file is a YAML mapping or has YAML frontmatter. The caller interprets prose
briefs into explicit fields before using this adapter.

`DeliverablePath` supplies a context anchor when `ScopePath` is absent.
`TaskProfile: DELIVERABLE_TASK` remains a compatibility label and selects no
method. Unsupported profiles fail. Roots bind independently from CWD; explicit
working roots and resolved scopes remain contained in the active checkout.
The inferred project/domain root or checkout fallback establishes a path anchor,
not authority to maintain Root instructions or execute product work.

The structured adapter defaults `ApplyEdits` to false and then returns no
writable targets. With edits enabled, `AllowedWriteTargets` supplies explicit
contained targets; the host still enforces their effects. The read-only role
ceiling clears targets for HELP_HUMAN. `AllowedTools` supplies command
expressions, independently from capability names in `--policy`. The policy
object carries optional host/brief restrictions and placeholder bindings.

Command restrictions return as conjunctive `effective_tools.commands.all_of`
layers, each containing alternatives. This preserves intersecting scope rules
without approximating them as a single glob. The utility evaluates declared
command/target claims; a host must establish and enforce actual process effects.
The utility README specifies these interfaces and return fields. Resolver
success establishes input processing, not downstream adoption or model delivery.

## Coordination and evidence

Record actual parentage, objective, accepted source basis, write ownership,
dependencies, expected returns, and human decisions before dispatch. Actual
child execution is required for a multi-agent claim. Shared reads are allowed;
concurrent writes are disjoint or serialized through one integration owner.
Relay relevant information through the parent. A material scope or basis change
requires a versioned brief amendment under existing decision rights.

For governed phase boundaries preserve accepted source snapshots, derivative
status, closure verdict, rerun requirements, and blockers. Read-only executors
return evidence to an authorized recorder rather than writing outside their
scope. PARTIAL, blocked, and failed returns remain distinct from complete work;
an audit executing successfully does not establish that its subject passes.

## Adoption and compatibility

The new format has no prose metadata envelope for legacy parsers. Consumers that
parse the former frontmatter, Agent Type table, or retired role roster must keep
their accepted instruction basis until they adopt the registry, new loader,
workflow resources, and compatibility adapter together. Export staging includes
these surfaces and records the hold; staging is not publication or release.

Root publishes the replacement contract and routes affected-loop notices.
Each owning loop adopts, amends, or declines on its own authority and updates
its own pins and mirrors. Existing accepted snapshots and historical decisions
are preserved. The receiving loop must verify role discovery, direct entry,
capability intersection, selected-context loading, and generated brief handling
before clearing its adoption hold.
