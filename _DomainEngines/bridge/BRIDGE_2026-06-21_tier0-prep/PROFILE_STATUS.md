# PROFILE_STATUS — open_pipe_stress

| Field | Value |
|---|---|
| Active profile | `_DomainEngines/profiles/open_pipe_stress.DRAFT.yaml` |
| ProfileStatus | **DRAFT** (not validated; not adopted) |
| Integration level (current, not yet ruled) | MANUAL_BRIDGE (L0) |
| Validator | none — deterministic profile-schema validator is a TOOLMAKER handoff (not built) |

## Boundary summary (DRAFT — pending Gate 2 adoption)

- **Authoritative (engine-owned, protected):** `core/**`, `schemas/**`, the engine project store (model states / analysis runs / comparisons per `project_persistence.schema.yaml`), `core/handoff/**`, solver outputs.
- **Chirality-readable:** analysis-run / model-state / comparison records (schema-defined; instances TBD), handoff package manifest (no private payload), on-demand exports, engine professional-boundary notices.
- **Agent-writable:** `_DomainEngines/proposals/open_pipe_stress/**`, `_DomainEngines/bridge/**` (review notes, TBD registers).
- **Declared tools:** `operation_applier` (validate/apply), `completeness_checker`, `rule_check_runner` (all Rust, verified), `headless_runner` (lib-only; entrypoint TBD).

## Human gates (persona Gates 2–5 — none yet passed)

profile adoption · protected-write policy · mutating tool calls (`operation_applier.apply`) · operation-proposal application · external-prover interpretation · professional reliance.

## Open profile issues

1. Not validated (no validator tool).
2. Readable run/state/comparison **instances** are TBD (schemas exist; produced on demand).
3. `operation_risk_class` is proposed, not implemented in the engine.
4. The persona's example binding diverges from this verified binding (FM-03).
5. Live binding (L2–L3) gated ×4 (tier-0 adoption · app-dev F3 · piping D-21 · DEC-041 automation condition).
