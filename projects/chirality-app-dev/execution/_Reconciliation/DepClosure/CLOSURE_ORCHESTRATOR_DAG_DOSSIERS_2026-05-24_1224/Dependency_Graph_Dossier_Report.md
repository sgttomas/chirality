# Dependency Graph Dossier Report

## Verdicts

- Strict all-active execution graph: **CYCLIC**.
- Existing blocker-subset graph: **CYCLIC**.

The strict FULL_GRAPH reading still cannot support ORCHESTRATOR `BLOCKED/UNBLOCKED` reporting. The existing app blocker-subset reading is much closer: it has one 2-node blocker cycle, `DEL-03-01` and `DEL-04-01`.

## What Changed From The Prior Package

No source dependency rows changed. This package replaces the mechanical `RETIRE_ROW` cut-set with dossiers and ruling questions. It treats interface cycles as possible co-development/interface evidence rather than automatic retirement candidates.

## Key Counts

- Active execution deliverable rows: 129
- Active execution unique precedence edges: 114
- Strict SCC count: 2 with sizes [18, 2]
- Blocker-subset rows: 24
- Blocker-subset SCC count: 1 with sizes [2]
- Bidirectional pair dossiers: 13

## Human Rulings Needed

1. For `DEL-03-01` / `DEL-04-01`, choose precedence perspective or declare co-development. This is the only blocker-subset cycle.
2. For strict FULL_GRAPH closure, review all bidirectional pair dossiers in `Cycle_Dossiers.md` and `Human_Ruling_Workbook.csv`. Many appear to be interface/co-development couplings, not necessarily bad dependency rows.
3. Decide whether ORCHESTRATOR should continue to require the strict all-active execution graph to be acyclic, or compute blockers from the existing blocker-subset semantics while reporting interface SCCs separately.

## Artifacts

- `Cycle_Dossiers.md`
- `Human_Ruling_Workbook.csv`
- `Edge_Classification_Audit.csv`
- `Blocker_Subset_Edges.csv`
- `dossier_state.json`
