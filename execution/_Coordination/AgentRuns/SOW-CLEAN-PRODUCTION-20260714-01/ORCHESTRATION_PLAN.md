# Clean Scope-of-Work Production Orchestration Plan

Status: `ACTIVE`
Selection authority: `HUMAN`
Posture: `SINGLE_MANAGER_SEQUENTIAL`
Owner: `HELPS_HUMANS`
Basis: `main@7fea3356b465633dbf4b30cb61d547bfc978ccec`

## Objective

Separate four-document migration evidence from the final production
`ScopeOfWork.md`. Keep an evidence-rich conversion candidate for parity and
mapping, deterministically finalize it into a clean production contract, bind
all downstream verification to that clean artifact, and prevent integration
of an evidence-rich candidate.

## Work graph

1. Amend the Stage-2 method and governing standard at the newly clarified
   evidence/production boundary.
2. Implement deterministic finalization, external evidence reporting, clean
   contract parsing, and production-artifact bindings.
3. Update workflow instructions, manager contracts, tool registry, and active
   Stage-2 plan without changing any project deliverable.
4. Run focused regressions, corpus compatibility checks, instruction/path
   validation, and scoped Git hygiene checks.
5. Close through CHANGE and hold for the human.

All work is serialized in the active checkout. Existing unrelated equation
audit paths and `.claude-worktrees/**` are excluded from reads, writes,
staging, and interpretation.
