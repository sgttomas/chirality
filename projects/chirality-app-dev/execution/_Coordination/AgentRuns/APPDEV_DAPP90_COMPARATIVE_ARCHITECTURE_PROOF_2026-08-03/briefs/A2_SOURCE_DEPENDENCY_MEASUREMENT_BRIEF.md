# Agent 2 Brief — Source, Dependency, and Measurement Review

Parent: `HELPS_HUMANS`

Objective: independently inspect the current App frontend tree and return a
path-grounded A/B/C dependency-map review plus reproducible measurements for
target leakage, duplicate composition, build matrix, and migration cost.

Read scope:

- D-APP-90 packet and ruling;
- this run's `ACTIVATION.md` and `WORK_GRAPH.md`;
- current `projects/chirality-app-dev/frontend/` source/config tree;
- prior D-APP-87 re-plan derivative package for context.

Write scope: only
`reviews/A2_SOURCE_DEPENDENCY_MEASUREMENT_RETURN.md`.

Required return:

- actual current entry points and common composition seams with exact paths;
- a source/package dependency map for A, B, and C without selecting one;
- explicit measurement definitions, formulas, counts, assumptions, and
  reproducible commands;
- candidate A/C profile/slot fields and B shared-core/shell extraction seams;
- uncertainty and elimination-test recommendations; and
- confirmation that no product or other forbidden path was written.

Do not delegate. Do not run builds or tests that mutate product artifacts. Do
not infer generic runtime semantics, Agent-2 Bash, packaging identity authority,
or first-domain UI requirements.
