# Coordination Record

**Representation:** Full graph
**Dependency tracking mode:** FULL_GRAPH
**External schedule / coordination artifact:** `docs/PLAN.md`
**Default maturity threshold (if computing blockers):** SEMANTIC_READY
**Dependency graph source:** Post-enrichment `TASK + dependency-extract`
**Decomposition authority:** `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
**Recorded:** 2026-05-20

## Human Rulings

- Use v3.2 as the SOFTWARE_DECOMP working surface.
- Use FULL_GRAPH dependency tracking.
- Treat upstream dependencies as satisfied only when the upstream deliverable is `SEMANTIC_READY`.
- Determine dependencies only after four-document authoring, semantic lensing, and enrichment.

## Reporting Rule

ORCHESTRATOR may report lifecycle state immediately. It must not compute blocked/available state until dependency extraction has produced valid `Dependencies.csv` registers and the merged FULL_GRAPH is acyclic.
