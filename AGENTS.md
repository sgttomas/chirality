# AGENTS — Runtime Doctrine and Entry

An agent is an LLM operating with instructions, supplied context, available
tools, and actual host permissions. A role describes how the agent contributes;
a workflow describes how an undertaking is performed. The human remains
accountable for what is accepted or relied upon.

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
resources on demand. Record their actual origins and hashes in governed run
evidence so later inspection and replay can reconstruct the supplied history.
A role may consult another role's instructions deliberately when comparison,
design, migration, or coordination actually requires it, and must record that
wider consultation in the run evidence.

HELP_HUMAN may coordinate through Type 1 managers or dispatch bounded Type 2 work
directly. HELPS_HUMANS and WORKING_ITEMS may dispatch TASK or an ephemeral Type
2 instance. Type 2 does not delegate. Agents may investigate, draft, propose,
check, and carry authorized work forward on their own initiative. They return
to the human for decisions reserved by the governing workflow or accepted
instruments; uncertainty alone does not require an extra prompt.

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
Use is optional except for the workflow-authoring requirement below:

| Undertaking | Workflow |
|---|---|
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