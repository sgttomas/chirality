---
name: construct-local-work-graph
description: Work with the user to establish the intended outcome and route through a project's DAG, then turn the relevant deliverables and current work into an executable local graph.
---
# Construct a local work graph

Build the route from the human's intended result to examined, integrated work.
HELP_HUMAN develops that understanding and coordinates construction; a manager
can develop a selected portion, and TASK can inspect or draft a bounded part
without delegating. One graph carries the undertaking across sessions.
`LOOP_INIT.md` points to the actual current graph and governs its traversal.

## 1. Establish the intended result

Read the init steering, subsequent human directions and relevant decisions.
Establish the result, priorities, approach, limits and conditions for completion.
Recover a continuing undertaking through the current graph and compare its
position with actual work before planning it again. A missing target requires
recovery; a previous proposal or paused assignment is not new authorization.

State the reading of the undertaking briefly, distinguishing direction from
interpretation. Proceed where intent is clear. Investigate enough to make a
material scope or sequencing question concrete, then bring it to the human.
The user need not provide node IDs or a finished plan. Preserve the source of
steering and account for work displaced by a later change.

## 2. Find the work and its grounds

Use the project entry to locate relevant sources, then follow their references
for the selected outcome. Read each source for the question it can answer:

| Source | Why look here? |
|---|---|
| Current graph, branch/worktree, open or merged PRs and their evidence | Establish what has actually happened, what is unmerged, and what can continue without repeating earlier work. |
| Accepted project DAG/decomposition | Locate the intended contribution, required upstream inputs and affected downstream consumers. A diagram alone does not establish input readiness or grant scope. |
| Affected Scope of Work or another accepted production form | Identify the commitment served, expected outputs, criteria, interfaces and governing references. Keep an uncertain mapping visible rather than forcing it into an unrelated deliverable. |
| Deliverable dependency records and their cited evidence | Determine what a contribution needs, who supplies it and whether the needed condition is met. Ownership and informational relationships are not automatically prerequisites. |
| Implementation, tests and actual verification/validation results | Compare the intended result with what exists; distinguish missing behavior, missing evidence, defects and unresolved design. |
| Relevant decisions, scope changes, holds and MEMORY run pointers | Find controlling choices and prior results. Follow memory to its central sources; local summaries neither make decisions nor assign future work. |

Use the current source and candidate identity when sources disagree. Follow only
relationships material to the undertaking, far enough to understand their
consequences. Preserve accepted scope and explicit holds. If the desired route
has no deliverable home or contains an unresolved dependency cycle, identify the
necessary mapping/design decision before making dependent work executable.

Choose the route that serves the human's outcome. Explain the necessary enabling
work and what remains outside the undertaking; unrelated ready work is not
selected merely because it appears in a DAG. A design or diagnosis can be a node
whose question must be answered before its resulting implementation is defined.

## 3. Express an executable route

Give each node a meaningful result, stable ID, deliverable binding, prerequisites,
write boundary and owner, completion check, and actual state or evidence. State
provisional mappings and owner-held choices explicitly. Dependencies identify the
specific result or condition the next contribution needs. Arrange independent
work around actual inputs, shared writes and test resources, with one owner for
integration. A label such as "work on package" is not an assessable result.

Include the implementation, investigation, verification, validation where
applicable, independent review, repairs and integration needed for the result.
Plan substantive PRs, each carrying the documentation, reconciliation and
conditional Task Management consequences its slice needs. A PR boundary alone
requires neither a formal reconciliation pass nor a Task Management intake.

After the intended implementation/evidence PRs, plan one final bounded
closeout stage. It includes documentation/governance reconciliation through
`chirality-root:bundled:workflow:bounded-reconciliation`, conditional Task
Management, the invoking loop's central receipt, terse MEMORY run entries, and
the final PR. For App/Piping, use the graph's stable run ID for one receipt at
`execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md`; affected MEMORY entries
point to it. Other loops retain their adopted recording rules. Divide
deliverable
comparisons into bounded assignments as needed. Missing required production
returns to the graph for repair and an affected backcheck, not transfer-based
completion. Central decisions and intake outcomes retain their actual status.

Check the proposed route from its first contributions to the intended result:
required work and checks are represented, dependent inputs can be obtained,
executable dependencies are acyclic, and shared writes have an integration owner.
Keep blockers and uncertainty truthful while independent authorized work proceeds.
The final PR merge is the terminal condition after the promised work and required
review, checks and human decisions. Its candidate records readiness and the PR
URL; later Git/PR evidence establishes the actual merge.

## 4. Save and maintain the current graph

Use the [graph template](resources/work-graph-template.md). For App/Piping local
development, save the current graph exactly at
`execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`, relative to the
project. It is Git-tracked project state: include it early in the undertaking's
PR sequence for handoff, then update it in later PRs. Set LOOP_INIT's current
pointer to that actual path. If the pointer lies outside the executor's write
ceiling, return the precise update to its authorized owner before handoff.

Keep one current account of the ready work, holds and next safe action, bound to
the checked candidate. Link PRs, evidence, active operations and shared-resource
ownership needed to continue. Keep detailed launch histories, child attribution,
source hashes and old pauses in their owning run records rather than repeatedly
appending them to the current graph. Required execution provenance remains
recoverable through those links. One maintainer integrates changes against the
latest graph revision.

Preserve historical graphs at their original paths. A still-pinned undertaking
adopts this method through its actual owning authorization. On that explicit
adoption, carry its current scope/state into the required location and cite the
predecessor without maintaining another current copy. Keep the stable run identity that
relates the graph, central receipt/evidence, PRs and affected MEMORY rows. Preserve
needed evidence before a temporary worktree retires. Do not require a later
commit solely to write the final merge result back into its own candidate.

Return the saved graph and current pointer, selected route, material assumptions,
unresolved decisions and first ready work. Then resume the loop within the
human's direction. Graph construction changes no scope, hold, lifecycle or
release authority by itself.
