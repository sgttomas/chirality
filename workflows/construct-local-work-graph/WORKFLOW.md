---
name: construct-local-work-graph
description: Work with the user to establish the intended outcome and route through a project's DAG, then turn the relevant deliverables and current work into an executable local graph.
---
# Construct a local work graph

Produce a graph that tells the development loop what to accomplish, why that
work is selected, what it depends on, and how to recognize completion. Begin
with the user's intent. The project DAG supplies relationships and obligations;
the user's direction determines which part to advance and to what end.

HELP_HUMAN develops that understanding with the user and coordinates graph
construction. A manager can develop a selected portion; a TASK can investigate
or draft a bounded contribution without delegating. Keep one graph for the
undertaking across sessions. `LOOP_INIT.md` points to it and governs traversal.

## 1. Understand how the user wants to proceed

Read the init-prompt steering, subsequent chat directions and any relevant
recorded decisions. Recover an existing graph through the loop pointer before
planning a replacement. A missing target needs recovery, including validation
required for any historical receipt used as a cursor; it is not an empty slate.
With no selected graph, check known relevant work so it is not planned twice.

Form a concrete reading of the user's intent:

- What result are they trying to reach, and what would make this phase of work useful?
- Which capabilities or deliverables matter first, and why?
- What approach or constraints have they expressed, including what to leave for later?
- How far should this undertaking go, and what would count as enough?

Infer answers from the conversation where there is adequate support. State your
reading briefly, distinguishing explicit direction from your interpretation.
Ask focused questions where different answers would materially change scope,
ordering, effort or completion. Use project discovery to make those questions
concrete. Do not require the user to supply node IDs or a finished specification.
Proceed within clear direction without asking for approval of every routine
choice. Follow a requested planning checkpoint; a proposal or tentative idea
is not a ruling, and a pause remains in force until the user resumes the work.

Retain this intent and its source in the graph so the next session can understand
why the work was chosen. Later steering can revise it; preserve completed work
and account for obligations displaced by the change.

## 2. Select a route through the project DAG

Locate the deliverables that serve the intended result. Read their scope and
follow the phase DAG upstream to necessary inputs and unresolved prerequisites,
then downstream far enough to see affected interfaces and consumers. Check the
actual state of those inputs; a diagram or lifecycle label alone is insufficient.

Choose the smallest coherent set of work that can reach the intended result.
Explain the starting point, the proposed order, what can proceed independently,
and what stays outside this undertaking. A user's priority does not itself
satisfy a prerequisite: include the necessary enabling work or surface the conflict.
Do not select unrelated ready work merely because the DAG makes it available.

If the desired result has no clear deliverable home, record that mismatch and
include a bounded scope/design decision or investigation. Do not force it into
an unrelated deliverable or quietly amend the accepted DAG. Genuine dependency
cycles need resolution before the affected work can be made executable.

## 3. Develop enough scope to make the work executable

For the selected deliverables, read the controlling parts of `ScopeOfWork.md`
(or the active legacy document kit), `_STATUS.md`, dependency records and relevant
decisions. Inspect the corresponding code, tests, specifications and existing
work, including unmerged changes when they affect the undertaking.

Determine what exists, what is missing or incorrect, what is only planned, and
what remains uncertain. Resolve enough detail to name concrete outputs and
checks. If a design or diagnosis is needed before implementation can be scoped,
make that the next node with the question it must answer; do not invent certainty.

Express each work node as a meaningful result: for example, implement a bounded
user capability, resolve a design question, verify an interface, or update named
deliverable sections after a change. Identify the deliverable(s), relevant files,
inputs, write boundary and completion evidence. Avoid nodes that say only
"work on package" or name an agent without specifying the work.

## 4. Build and check the local graph

Use stable node IDs. State dependencies as the specific result or condition a
node needs; keep informational links and ownership distinct from prerequisites.
Check that executable dependencies are acyclic and that shared writes or test
resources have an integration owner. Record uncertain mappings and owner-held
choices explicitly, while leaving independent authorized work available.

Include the implementation, investigation, review, verification and integration
work the result actually needs. Plan `bounded-reconciliation` nodes throughout
the undertaking, using its deliberately selected source-qualified workflow.
Each reconciliation node names the affected deliverable folders and document
sections, the stable code/evidence it will consume, and the updates it is to make.
Place it after a coherent result and before work that relies on those updated
records. It can run alongside independent implementation. Do not defer every
deliverable update to a single final documentation task.

Walk the proposed graph from its starting nodes to the intended outcome. Check
that no required work or verification is missing and that every dependent can
obtain its inputs. Mark ready work, blockers and questions truthfully. A node
completes against its own conditions; implementation and deliverable
reconciliation completion remain distinct.

## 5. Save the graph and return to the loop

Adapt the [graph template](resources/work-graph-template.md). Keep a useful
existing graph in place, including JSON. For a new one, prefer the project path
`execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`; place supporting
results beside it when appropriate. Retain revisions through Git or the host's
available history and preserve needed evidence before temporary worktrees retire.

Include the intended outcome and route, work nodes, deliverable mappings,
completion conditions, and enough current state to continue: checked source
revision, local/unmerged work, active operations, holds, and next safe actions.
Keep detailed evidence linked and required execution attribution separate from
the work description. One maintainer integrates graph updates against its latest
revision rather than overwriting another contributor's changes.

Update the loop's current-graph pointer within the assignment, or return that
precise edit if it lies outside the write scope. Present a short explanation of
the selected scope and route, material assumptions, unresolved decisions and
first ready work. Then return to the development loop for traversal within the
user's direction. Constructing a graph does not itself lift a hold, accept a
scope amendment, start another phase or authorize release.
