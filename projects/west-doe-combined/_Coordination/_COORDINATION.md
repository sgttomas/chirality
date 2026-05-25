# Coordination Record

**Representation:** Declared critical dependencies
**Dependency tracking mode:** DECLARED
**External schedule / coordination artifact:** N/A
**Default maturity threshold (if computing blockers):** INITIALIZED

## Decomposition Authority

- Accepted upstream decomposition truth: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- Snapshot verdict: `APPROVED / FINAL PUBLISHED`
- Downstream setup consumes the Gate 7 package/scope/objective/deliverable/artifact/interface basis without reinterpreting the raw source corpus unless a later workflow explicitly requires source verification.

## Dependency Declaration Rules

- Mode: `DECLARED`
- Register convention: prefer deliverable-local `Dependencies.csv` when produced by `TASK + dependency-extract`; use `_DEPENDENCIES.md` as the human-readable view and run-history surface.
- Blocker computation is advisory and limited to declared dependency edges only.
- Undeclared relationships are not treated as blockers.
- Default maturity threshold is `INITIALIZED` unless the human changes it before blocker computation is first used.

## Notes (Human-Owned)

- Critical dependencies are recorded in-file only where they materially affect sequencing, estimation, review, reconciliation, or handoff.
- Full cross-deliverable graph completeness is not asserted.
