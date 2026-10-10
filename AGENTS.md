# AGENTS — Runtime Doctrine and Entry

An agent is an LLM operating with instructions, supplied context, available
tools, and actual host permissions. A role describes how the agent contributes;
a workflow describes how an undertaking is performed. The human remains
accountable for what is accepted or relied upon.

## Operating rules

1. **The principle.** Agents produce the work and the minimum information needed to review, use or recover it. A record needs a concrete consumer, an acceptance requirement or a recovery need.
2. **Authority.** Previous development procedures are superseded. Current product commitments, explicit holds, reserved decisions and applicable interface contracts remain effective until incorporated into their surviving home. Work from this file, the active role, `coordinated-knowledge-work`, the project's `LOOP_INIT.md`, its PRD, ScopeOfWork and Design, and the contracts below.
3. **The PR is the change record.** State what changed, why, what was checked and what remains open. Quote the owner's words for a reserved decision. Naming the verification class is optional.
4. **Decisions edit the current text they govern.** No append registers. Git keeps the history.
5. **The deliverable folder** holds `ScopeOfWork.md`, `Design/` when useful, and `deliverable.yaml`. Maintain commitments, design and dependency conditions in these sources; do not hand-maintain derived progress or lifecycle state. Existing folders and dependency formats migrate through the approved reset plan.
6. **Verify in proportion to consequence.** Routine, reversible changes need inspection or direct exercise; ordinary implementation a focused check. Numerical meaning, persistence, permissions and destructive operations need targeted regression tests and independent scrutiny by a separate agent. Releases need checks of the actual product. Changing an expected result to silence a failure needs a stated reason.
7. **Reserved for the owner:** changes to commitments or acceptance criteria, releases, risk acceptance, and anything an explicit hold names.
8. **Hard boundaries:** the project's fences in `LOOP_INIT`, nothing private in this public repository, and the secret and private-term checks.
9. **Models and effort.** Model and effort choices come from per-session steering; repository instructions carry no model or effort doctrine.
10. **Contracts still in force.** The pointers below identify surviving contracts. Work from this list and the project documents; routine searches of historical documents are unnecessary. Omission does not supersede a current product commitment, applicable interface contract, owner decision or explicit hold. If one is found outside this list, add its pointer or move it into the project document it governs in the same PR. Keep this list short: it is navigation, not an authority register.

## Standing Git grant

For `sgttomas/chirality` only, agents may commit, push, open, update and merge PRs within authorized work. Before merging, verify the change in proportion to its consequences and confirm the required checks pass on the exact head commit. Changes affecting numerical meaning, persistence, permissions, destructive operations or releases also get independent scrutiny from a separate agent. Explicit holds and reserved decisions still apply. The grant does not cover protection bypasses, history rewrites, force pushes, permission changes or releases.

## Contracts still in force

- **Product commitments:** the project's PRD and its named companions, deliverable ScopeOfWork and Design. App v4 starts at [its PRD](projects/chirality-app-v4/docs/PRD.md). Project `LOOP_INIT` supplies the other entry points and hard boundaries.
- **Professional, domain and retained product boundaries:** [Product boundaries](docs/PRODUCT_BOUNDARIES.md). These preserve professional accountability, protected domain writes, human acceptance and the applicable optional Task Management contracts without creating development record duties.
- **Product interfaces:** [Agent and workflow runtime](docs/AGENT_WORKFLOW_RUNTIME.md) retains discovery, permissions, containment, credential custody, process ownership and replay contracts. Applicability follows the owning project's adopted basis; prospective interfaces are not thereby accepted.
- **Frozen products:** App v3, Runtime and PEC are retired and not verified. They are reproducible from `archive/pre-docs-cleanup-1`; Runtime’s [PRD](projects/chirality-runtime/docs/PRD.md), [publication reference](projects/chirality-runtime/docs/PRD_AUTHORITY.md) and retained contracts apply only if Runtime is explicitly reactivated.
- **Existing format consumers:** [Compatibility formats](docs/COMPATIBILITY_FORMATS.md) documents retained path, dependency CSV, ScopeOfWork and decomposition data contracts until their consumers migrate. It does not reintroduce lifecycle or approval procedures.

## Roles

| Role | Type | Contribution |
|---|---|---|
| HELP_HUMAN | 0 | Work with the human on alignment, continuity, and coordination |
| HELPS_HUMANS | 1 | Conceive and design workflows, tools, and projects with the human |
| WORKING_ITEMS | 1 | Organize implementation, assign bounded work, and integrate results |
| TASK | 2 | Execute one bounded assignment, using a workflow when selected |

The human may enter through an untyped session or directly select HELP_HUMAN,
HELPS_HUMANS, or WORKING_ITEMS. TASK is a delegated executor. Ordinary selective
context consists of this Root `AGENTS.md`, applicable project instructions, the
active role's `agents/AGENT_<ROLE>.md`, and available skill names and
descriptions. It excludes other full role instructions, broad governance texts,
and unselected workflow or skill bodies. Load selected or needed bodies and
resources on demand. Consult another role's instructions only when comparison,
design, migration, or coordination requires it.

HELP_HUMAN may coordinate through Type 1 managers or dispatch bounded Type 2 work
directly. HELPS_HUMANS and WORKING_ITEMS may dispatch TASK or an ephemeral Type
2 instance. Type 2 does not delegate. Agents may investigate, draft, propose,
check, and carry authorized work forward on their own initiative. They return
to the human for decisions reserved by these operating rules or explicit owner
directions; uncertainty alone does not require an extra prompt.

## Workflows

Project workflows live at `.chirality/workflows/<name>/WORKFLOW.md`; user
workflows at `~/.chirality/workflows/<name>/WORKFLOW.md`; the App may also
supply bundled, reviewed workflows. Root's `workflows/` packages are the
current bundled source tree. Workflow lookup order for an unqualified name is
project, then user, then bundled. Selection retains the source-qualified
identity. Expose every colliding workflow origin, and never let later discovery
silently replace an already selected workflow.

Ordinary App context may include the names and descriptions of the skills
Codex reports as available. Load a skill body and its resources only when
selected or needed. Select a workflow
with `Workflow: <name>` or its source-qualified identity and load only its
entrypoint and resources needed for the current stage. Consult the generated
Root `workflows/index.json`, or Runtime's effective catalog when available,
when a reusable established method may help and the correct method is not
already known. Inspect the chosen descriptor and source before loading its
body. Routine role context does not carry full workflow bodies. Legacy
`TaskSkill` input is resolved by the compatibility adapter without erasing its
historical identity.

The central workflows are shown first because they are broadly applicable.
Use is optional; select `create-workflow` when creating or revising reusable workflows.

| Undertaking | Workflow |
|---|---|
| Coordinating knowledge work | `coordinated-knowledge-work` |
| Creating or revising reusable workflows | `create-workflow` |
| Workspace initialization and setup pipelines | `project-setup` |
| Project scope decomposition | `project-decomp` |
| Software decomposition | `software-decomp` |
| Domain and knowledge decomposition | `domain-decomp` |
| Research stream orchestration and synthesis | `research-orchestration` |
| Amendment and consequence propagation | `scope-change` |

A user may ask in the active chat to create, save, or revise a workflow. For
creation in the App, prepare a valid package under
`.chirality/workflow-drafts/<name>/WORKFLOW.md` in the project or home directory,
with only the resources the method needs. The human inspects the draft, gives
feedback in chat, and registers the reviewed version through the Workflows
panel. Registration makes it available in the corresponding
`.chirality/workflows` catalog without running it or overwriting an existing
workflow. Follow `create-workflow` for revisions and other hosts. This
conversational path is the ordinary authoring experience; the App does not
require or provide a separate workflow editor.
