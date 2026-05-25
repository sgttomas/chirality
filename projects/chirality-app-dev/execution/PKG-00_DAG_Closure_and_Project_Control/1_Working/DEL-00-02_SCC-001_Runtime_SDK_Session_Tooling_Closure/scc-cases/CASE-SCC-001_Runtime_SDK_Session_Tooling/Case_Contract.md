# Case Contract: CASE-SCC-001 Runtime SDK Session Tooling

## Purpose

This SCC Resolution Case is the PKG-00 receptacle for repeated bounded TASK work, human rulings, candidate remedies, and owner-workflow handoffs for SCC-001. It preserves three existing scope-change packets as seed evidence for runtime/SDK core, session/audit records, and tooling/permissions/MCP concerns.

## Authority Limits

- The case may collect findings, evidence, open questions, candidate remedies, rulings, and handoff payloads.
- The case may be updated by WORKING_ITEMS through bounded `TASK + scc-resolution-case` work.
- The case does not update product deliverables, dependency registers, decomposition truth, `_ScopeChange/`, or `_Reconciliation/`.
- The case does not initiate SCOPE_CHANGE. A human must explicitly initiate any SCOPE_CHANGE workflow.
- The case does not close SCC-001. Closure can only be reported from a later accepted DepClosure snapshot.

## Write Boundary

Allowed writes are limited to this case folder and scoped run records under the owning `DEL-00-02` control deliverable. Seed packet folders under `case-seeds/` are read-only evidence unless a later explicit maintenance task names them as the target.

## Non-Goals

- No product dependency row is changed here.
- No SDK/runtime/session/tooling deliverable is reclassified here.
- No project-wide blocker state is computed here.
- No packet, case, or TASK output substitutes for decomposition truth.

## Expected Use

TASK agents working in affected deliverables should deposit source-grounded findings into `Task_Findings.csv` and cite evidence in `Evidence_Register.csv`. Human rulings belong in `Ruling_Register.csv`. Candidate remedies stay provisional until an owner workflow accepts responsibility through `Owner_Workflow_Handoff.md`.
