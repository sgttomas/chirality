# PEC — Chirality Coordination Plane

PEC is the coordination plane of the Chirality operating system: a
deterministic, rebuildable projection of governed file truth, plus an
ephemeral presence layer, embodying **Step 0 (Discover)** and the
deterministic parts of **Step 1** of the canonical development loop. It is
consumed by harnesses on behalf of agents and by the human owner through
dashboards — and it is deliberately **the coordination plane that doesn't
need to exist**: files and Git remain the sole authority, every consumer has
a file-native fallback, and deleting PEC degrades throughput, never
correctness.

Product definition of record: [`docs/PRD.md`](docs/PRD.md) — v2.0, adopted
2026-07-24 (`D-PEC-58`). **New here? Read [`docs/STATUS.md`](docs/STATUS.md)
first.**

## State

Pre-implementation. The next gate is decomposition (SOFTWARE_DECOMP over the
PRD, human-gated); build phases P1–P4 follow under per-tranche packets. See
the standing plan at
`_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md`.

## Layout

| Path | Contents |
|---|---|
| `docs/PRD.md` | Adopted product definition (v2.0, coordination plane) |
| `docs/STATUS.md` | Status & handoff — read first |
| `docs/.archive/` | Retired v0.4/v1.0 product docs (PRD v1.0, SPEC, TRACEABILITY, PILOT, ADRs, prototype README/STATUS) |
| `execution/_Coordination/` | Decision packets, register, coordination records |
| `core/`, `server/`, `web/`, `agent-sidecar/`, `tools/`, `fixtures/` | **Frozen reference corpus** — the v0.4-baseline prototype; read/cite only, quarried by citation in build briefs (PRD §13); run instructions preserved at `docs/.archive/README_v0.4_prototype.md` |
| `init/` | Loop launcher prompt (points at `_DomainEngines/pec/LOOP_INIT.md`) |

## Principles the build must keep (PRD §6, PEC-K-01..11)

Graceful absence (no governed act requires PEC) · files govern (rebuildable
projection; rulings file-native) · harness-owned polling · staleness is a SHA
comparison · two trust tiers, never blurred · observation, not participation
· ingest best-effort, reconciliation guaranteed · everything derived is
explainable · declared surface · content-minimal · mode-proportional.

## Governance

Decisions: `execution/_Coordination/_DECISIONS/_REGISTER.md` (pivot:
`D-PEC-57`; adoption: `D-PEC-58`). Receipts:
`_DomainEngines/pec/LOOP_RECEIPTS.md`. Project agent rules: `AGENTS.md`.
