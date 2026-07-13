# BRIEF SCHEMA — scope-of-work

## Required fields

| Field | Meaning |
|---|---|
| `PURPOSE` | One candidate Stage-1 deliverable conversion or verification |
| `ScopePath` | Exact deliverable folder under an authorized pilot package |
| `TaskSkill` | `scope-of-work` |
| `AllowedWriteTargets` | Candidate and run-record paths only; never legacy or underscore files |
| `RuntimeOverrides.DELIVERABLE_PATH` | Same resolved deliverable folder as `ScopePath` |
| `RuntimeOverrides.DECOMPOSITION_BASIS` | Accepted decomposition path and commit |
| `RuntimeOverrides.PROJECT_SCOPE_REFS` | Non-empty accepted project-scope references |
| `RuntimeOverrides.PACKAGE_OBJECTIVE_REFS` | Non-empty accepted package-objective references |
| `RuntimeOverrides.PILOT_VARIANCE_REF` | Accepted, exact path-scoped variance |
| `RuntimeOverrides.SOURCE_STATE` | `IN_PROGRESS` |
| `ExpectedOutputs` | Candidate, claim map, parity report, deterministic REVIEW checklist, receipt, and structured return |

The brief also supplies or authorizes grounded determination of the initial
`OUT-*`, `AC-*`, and `VER-*` definitions. Tests may implement a verification
method but may not create scope or acceptance criteria.

## Optional fields

| Field | Meaning | Default |
|---|---|---|
| `RuntimeOverrides.RENDER_HTML` | Produce an on-demand derivative | `false` |
| `RuntimeOverrides.MODE` | `CONVERT`, `REFINE`, `VERIFY`, or `CHECKLIST` | `CONVERT` |
| `CustomInstructions` | Deliverable-specific emphasis within the frozen scope | none |

## Write boundary

Permitted targets are limited to:

- `ScopeOfWork.md` in the isolated pilot worktree;
- a requested untracked/on-demand `ScopeOfWork.html`; and
- run-local claim-map, parity, deterministic checklist, receipt, and return
  artifacts.

The four legacy documents and `_STATUS.md` are read-only inputs.
