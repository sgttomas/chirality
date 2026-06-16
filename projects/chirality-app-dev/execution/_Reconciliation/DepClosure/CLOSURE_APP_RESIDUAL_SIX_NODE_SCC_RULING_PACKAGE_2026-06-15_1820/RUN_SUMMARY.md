# Run Summary - APP_RESIDUAL_SIX_NODE_SCC_RULING_PACKAGE

`RUN_STATUS = WARNINGS`

## Snapshot

`/Users/ryan/.codex/worktrees/3233/chirality/projects/chirality-app-dev/execution/_Reconciliation/DepClosure/CLOSURE_APP_RESIDUAL_SIX_NODE_SCC_RULING_PACKAGE_2026-06-15_1820`

## Commands Run

```bash
/Users/ryan/.codex/worktrees/3233/chirality/tools/scaffolding/scaffold_tool_root.sh /Users/ryan/.codex/worktrees/3233/chirality/projects/chirality-app-dev/execution _Reconciliation
```

```bash
/Users/ryan/.codex/worktrees/3233/chirality/tools/scaffolding/create_snapshot_folder.sh /Users/ryan/.codex/worktrees/3233/chirality/projects/chirality-app-dev/execution/_Reconciliation/DepClosure CLOSURE APP_RESIDUAL_SIX_NODE_SCC_RULING_PACKAGE
```

```bash
python3 /Users/ryan/.codex/worktrees/3233/chirality/tools/coordination/analyze_dep_closure.py /Users/ryan/.codex/worktrees/3233/chirality/projects/chirality-app-dev/execution --output-dir /Users/ryan/.codex/worktrees/3233/chirality/projects/chirality-app-dev/execution/_Reconciliation/DepClosure/CLOSURE_APP_RESIDUAL_SIX_NODE_SCC_RULING_PACKAGE_2026-06-15_1820/Evidence
```

```bash
/Users/ryan/.codex/worktrees/3233/chirality/tools/scaffolding/update_latest_pointer.sh /Users/ryan/.codex/worktrees/3233/chirality/projects/chirality-app-dev/execution/_Reconciliation/DepClosure CLOSURE_APP_RESIDUAL_SIX_NODE_SCC_RULING_PACKAGE_2026-06-15_1820
```

## Status

The deterministic closure analyzer completed successfully against the current execution root.

The strict active deliverable execution graph still contains one non-trivial SCC:

- `SCC-001`: `DEL-03-01`; `DEL-03-02`; `DEL-03-03`; `DEL-03-04`; `DEL-04-03`; `DEL-05-02`

This matches the prior residual closeout snapshot and is the SCC referenced by `D-APP-06`.

## Key Metrics

| Metric | Value |
|---|---:|
| Dependency registers discovered | 51 |
| Total dependency rows | 554 |
| Schema-valid registers | 51 |
| Active deliverable execution edges | 101 |
| Strict SCC count | 1 |
| SCC sizes | 6 |
| Bidirectional pair count | 0 |
| ID normalizations | 0 |
| Analyzer isolated/orphan deliverables | 5 |

## Blockers

No tool-execution blocker occurred. The closure blocker is substantive: strict graph acyclicity is not achieved while the residual six-node SCC remains active.
