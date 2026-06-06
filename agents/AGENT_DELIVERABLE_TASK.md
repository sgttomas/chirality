---
description: "Compatibility pointer for legacy DELIVERABLE_TASK briefs"
---
[[DOC:AGENT_INSTRUCTIONS]]
# AGENT INSTRUCTIONS — DELIVERABLE_TASK Compatibility Pointer
AGENT_TYPE: 2

`DELIVERABLE_TASK` is deprecated and is no longer a separate operational agent
pathway or active task profile.

Use canonical `TASK` (`agents/AGENT_TASK.md`) for bounded Type 2 work. Legacy
briefs may still include `TaskProfile: DELIVERABLE_TASK`; `TASK` records that
value as compatibility metadata only. It does not load this file, activate a
deliverable-local mode, read a deliverable truth set, or authorize writes.

Deliverable-specific reads, memory updates, lifecycle edits, closeout fields,
and artifact write limits must be stated in the effective bounded task brief or
in the selected `TaskSkill` contract. The brief's write authorization controls
the run.

For tranche orchestration, `WORKING_ITEMS` remains the Type 1 parent posture:
it proposes a bounded tranche, waits for human approval, dispatches canonical
`TASK` workers with explicit brief-defined limits, and fans in review/audit
results.
