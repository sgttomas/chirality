# CHANGE-H1-G Sealed Launch Brief

Parent: `HELP_HUMAN`
Role: `CHANGE` (Agent 1)
Run: `SOW-STAGE2-EXEC-20260712-01`
Brief version: `1`
Basis: synchronized `main@054ef5dd2de62f0803569573e162d613258b1b40`

## Objective

Bind the exact human H1 ruling, graph v51, orchestration-plan update, and
Receipt 19 to remote `main` in one evidence-only commit. This publication must
precede I1 project integration. Do not modify the prepared candidate or any
project path.

## Scope and checks

Read root `AGENTS.md`, `agents/AGENT_CHANGE.md`, the standing workplan, H1
evidence package, `amendments/H1-APPROVAL-001.md`, graph v51, and Receipt 19.
Require local HEAD, `origin/main`, and remote main equal the basis; validate
the cited evidence/candidate/status hashes; parse JSON; run strict diff
hygiene and applicable root checks; prove the exact staged path set contains
only:

- `amendments/H1-APPROVAL-001.md`;
- `WORK_GRAPH.json`;
- `ORCHESTRATION_PLAN.md`;
- `LOOP_RECEIPTS.md`;
- `instances/CHANGE-H1-G/**`.

Write scope is those paths plus one routine evidence-binding commit and
fast-forward push to `main`. No project, candidate, prior evidence, lifecycle,
reissue, authentication, integration, release, reliance, retirement, or H2
write is permitted. Fix safe mechanical evidence defects in scope, retain
hashes/attempts, and continue; substantive drift blocks.

Return `PASS`, `BLOCKED`, or `DECISION_REQUIRED` with exact commit/ref state,
checks, containment, and a handoff that releases I1 only on PASS while
preserving every non-H1 fence.
