# WORKING-C2A Root Launch Brief

Parent: `HELP_HUMAN`
Role: `WORKING_ITEMS` (Agent 1)
Root run: `SOW-STAGE2-EXEC-20260712-01`
Project run: `SOW-STAGE2-EXEC-20260712-01-C2A`
Brief version: `1`
Dependency: `C1G_ACCEPTED`; C2R candidate exists in disjoint root paths

Activate exactly one bounded software integration package:

- PackageID: `APP-FRONTEND-RUNTIME`;
- PackagePath: `projects/chirality-app-dev/frontend`;
- Selected scope: the nine P0-classified runtime/test callers named in the
  project-local sealed brief;
- Objective: C2A App runtime consumer activation only.

The authoritative project-local orchestration record, graph, write targets,
checks, children, and return contract are under:

`projects/chirality-app-dev/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A/`

Read and execute that package. Report cross-package notices only to
HELP_HUMAN. Treat all current root-lane dirt under `agents/`, `skills/`,
`tools/`, `docs/`, `exports/`, and root execution evidence as external,
read-only state. Do not perform Git actions or update project receipts.
