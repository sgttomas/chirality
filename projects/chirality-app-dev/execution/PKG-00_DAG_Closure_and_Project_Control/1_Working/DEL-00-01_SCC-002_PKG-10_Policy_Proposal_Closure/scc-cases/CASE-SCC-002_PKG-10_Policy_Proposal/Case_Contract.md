# Case Contract: CASE-SCC-002 PKG-10 Policy Proposal

## Purpose

This SCC Resolution Case is the PKG-00 receptacle for repeated bounded TASK work, human rulings, candidate remedies, and owner-workflow handoffs for SCC-002. It preserves the existing scope-change packet as seed evidence and allows additional deliverable-local evidence to accumulate before any owner workflow is asked to mutate governed project state.

## Authority Limits

- The case may collect findings, evidence, open questions, candidate remedies, rulings, and handoff payloads.
- The case may be updated by WORKING_ITEMS through bounded `TASK + scc-resolution-case` work.
- The case does not update product deliverables, dependency registers, decomposition truth, `_ScopeChange/`, or `_Reconciliation/`.
- The case does not initiate SCOPE_CHANGE. A human must explicitly initiate any SCOPE_CHANGE workflow.
- The case does not close SCC-002. Closure can only be reported from a later accepted DepClosure snapshot.

## Write Boundary

Allowed writes are limited to this case folder and scoped run records under the owning `DEL-00-01` control deliverable. Seed packet folders under `case-seeds/` are read-only evidence unless a later explicit maintenance task names them as the target.

## Non-Goals

- No product dependency row is changed here.
- No source deliverable is reclassified here.
- No project-wide blocker state is computed here.
- No packet, case, or TASK output substitutes for decomposition truth.

## Expected Use

TASK agents working in affected deliverables should deposit source-grounded findings into `Task_Findings.csv` and cite evidence in `Evidence_Register.csv`. Human rulings belong in `Ruling_Register.csv`. Candidate remedies stay provisional until an owner workflow accepts responsibility through `Owner_Workflow_Handoff.md`.
