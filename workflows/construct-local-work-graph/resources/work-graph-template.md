# Work graph — <undertaking>

Save App/Piping local development graphs at
`execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`, relative to the
project. Commit this graph early in the undertaking's PR sequence, update it as
work proceeds, and return its path for continuation. LOOP_INIT remains evergreen.
Preserve older historical graphs and link their relevant evidence.

## Intent and selected route

- Stable run identity: <ID used by the graph, deliverable MEMORY rows and PR>.
- Intended result and completion conditions: <what the user wants to achieve>.
- Steering basis: <init/chat direction or decision; distinguish interpretation>.
- Priorities and approach: <what to advance first and why>.
- Included / left for later: <bounded scope and material exclusions>.
- Route through the project DAG: <starting point, prerequisites and affected consumers>.
- Open questions: <only ambiguities or decisions that matter to proceeding>.

## Deliverable scope

| Deliverable / basis | What exists | What this undertaking changes or resolves | Work nodes |
|---|---|---|---|
| <ID, folder and controlling scope> | <code and evidence checked> | <concrete output; future intent retained> | <IDs or mapping question> |

## Work

| ID / outcome | Deliverables and work scope | Needs / why | Completion check | State / result |
|---|---|---|---|---|
| W1 <capability or investigation> | <DEL IDs; files; write bounds> | <required input or predecessor result> | <observable result> | <state; evidence or blocker> |
| V1 <independent verification> | <affected behavior or interface> | <W1 candidate available> | <check and independence required> | <state; result and limits> |
| P1 <substantive PR integration> | <W1/V1 result and needed document/governance consequences> | <slice work and required review/checks> | <PR merged; graph and slice records current> | <PR and evidence links> |
| C1 <final bounded documentation/governance closeout> | <affected DEL folders and governing records> | <substantive implementation/evidence PRs integrated> | <warranted edits checked; consequences routed> | <state; changed files or decisions> |
| M1 <record this run> | <affected MEMORY.md Runs rows> | <C1 result> | <terse local work descriptions and central pointers> | <state; row/run identity> |
| F1 <final PR integration> | <integrated undertaking> | <all promised work complete; final review/checks and decisions> | <final PR merged> | <PR link; merge confirms loop completion> |

Use PLANNED, READY, ACTIVE, BLOCKED, UNCERTAIN and COMPLETE consistently.
State the condition behind a dependency or blocker. A reference or an agent's
ownership is not itself a prerequisite. Each substantive PR includes the
documentation, reconciliation and conditional Task Management work its slice
needs. C1, M1 and F1 represent the single final closeout stage; they do not impose
a formal reconciliation pass per production node. Add decision/integration nodes
as needed.
Name any selected method's source-qualified identity in the node or linked brief.

## Current state and recovery

- Checked basis: <source/candidate revision and relevant evidence>.
- Next work: <ready nodes and next safe action; holds and unresolved decisions>.
- Local/unmerged work: <branch/worktree, partial edits and outstanding checks>.
- Active operations and ownership: <what is still running; resources to transfer>.
- Graph maintainer: <who integrates returns; current revision when editing>.

| Completed work / node | What changed and was checked | Unresolved consequence |
|---|---|---|
| <ID> | <artifact/evidence; local, merged or accepted as applicable> | <next node, deliverable update or decision> |

Keep execution state here. Near the final PR, index what this run did in each
affected MEMORY.md, linking the central evidence and decisions rather than
duplicating them. Final PR merge confirms completion; do not require a later
commit solely to record that merge. Preserve
previous graph revisions and linked evidence. Do not copy execution state into
LOOP_INIT, memory or a separate routine handoff.
