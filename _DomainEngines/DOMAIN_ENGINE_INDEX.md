# Domain Engine Integration — Control Area Index

**Owner persona:** DOMAIN_ENGINE (`agents/AGENT_DOMAIN_ENGINE.md`), Type-1 manager subordinate to Type-0 `AGENT_HELPS_HUMANS`.
**Control root:** `{REPO_ROOT}/_DomainEngines/` (persona default `DOMAIN_CONTROL_ROOT`; created 2026-06-21 with explicit owner approval).
**Scope:** shared-root (tier-0) governance authoring only. Nothing here is project-runtime truth, and nothing here edits either project subtree (`projects/chirality-app-dev/**`, `projects/chirality-piping/**`).

> **Status of everything under this root: `PROPOSAL` / unratified.** No profile is `ADOPTED`. No decision is ruled. No approval, SHA, or professional status is claimed (APEGA ceiling, K-AUTH-1). Publication is handed to CHANGE; DOMAIN_ENGINE does not commit.

---

## Registered domain engines

| DOMAIN_ENGINE_ID | Engine | Profile | ProfileStatus | Integration level (today) |
|---|---|---|---|---|
| `open_pipe_stress` | OpenPipeStress piping-stress engine (`projects/chirality-piping/`) | `profiles/open_pipe_stress.DRAFT.yaml` | **ADOPTED** (validated + Gate-2 adopted 2026-06-21) | `MANUAL_BRIDGE` (L0) |

## Layout

```
_DomainEngines/
  DOMAIN_ENGINE_INDEX.md          ← this file
  _LATEST.md                      ← pointer to the latest accepted snapshot
  RULINGS_PUBLISHED.md            ← the 8 owner rulings (2026-06-21) + RES-RECONCILE; the green-light signal
  NEXT_INSTANCE_PROMPT.md         ← sequencing: how owner rulings flow to action
  profiles/
    open_pipe_stress.DRAFT.yaml   ← DRAFT generic-shape profile, bound to the real piping layout
  bridge/
    BRIDGE_2026-06-21_tier0-prep/ ← immutable snapshot for this prep run (see its RUN_SUMMARY.md)
      framework_maintenance/      ← FM-01..04 gated canon diffs (NOT applied)
      TOOLMAKER_BRIEF-*.md        ← profile-schema validator; headless CLI entrypoint
  proposals/
    open_pipe_stress/             ← (empty; no OperationProposals authored — L3 not reached)
  _DECISIONS/
    _REGISTER.md                  ← 8 tier-0 decision records (PROPOSAL; HumanRuling = TBD)
    D-T0-01..08_*.md
```

## Read order for a human or successor agent

1. `bridge/BRIDGE_2026-06-21_tier0-prep/RUN_SUMMARY.md` — what this run did + the readiness verdict.
2. `_DECISIONS/_REGISTER.md` — the decisions awaiting your ruling.
3. `bridge/.../CONTRACT_DIRECTION.md`, `BRIEF_human_decisions.md`, `PLAN_cross_tier.md` — the substance.
4. `bridge/.../framework_maintenance/FM-0{1..4}_*.md` — reviewable canon diffs (gated, **not applied**).
