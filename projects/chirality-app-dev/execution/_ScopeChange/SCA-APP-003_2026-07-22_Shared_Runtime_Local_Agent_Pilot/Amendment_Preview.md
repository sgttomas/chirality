# SCA-APP-003 Amendment Preview

**Gate:** 3 — Amendment Approval
**Status:** `ACCEPTED_GOVERNANCE_PROPAGATED`
**Authority:** D-GOV-20, D-APP-73, D-T0-23, D-PEC-56

The owner accepted the complete Shared Runtime and Local-Agent Pilot by
explicitly instructing its implementation on 2026-07-22.

## Accepted amendment

- Root-owned provider-neutral runtime packages.
- One opt-in headless daemon using the packaged Electron identity and encrypted credential boundary.
- Authenticated project-scoped HTTP/1.1/SSE over a protected Unix socket; no TCP control listener.
- Tracked secret-free, machine-independent project manifests and explicit re-registration after authority changes.
- Central JSON/JSONL sessions with lazy non-destructive legacy reads/migration.
- Bundled CLI using Electron’s Node runtime and never accepting credential values initially.
- Explicit one-primary-model oMLX activation with drain, fail-closed `NO_MODEL`, no fallback, and residency epochs.
- Direct Agent 1 invocation and one required read-only Pi/oMLX Agent 2 delegation reviewed by the manager.
- PEC migration to the shared runtime while deterministic acts, RBAC, human-only acts, and data boundaries remain project-owned.
- Generic runtime public export after app-dev and PEC pilot validation.

## Deferred

Piping, automatic scheduling, local Agent 1, multiple simultaneous primary
local models, production PEC data/mutation, remote oMLX, and release remain
future governed milestones.
