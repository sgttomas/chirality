# PEC — Chirality Coordination Plane

PEC is the coordination plane of the Chirality operating system: a
deterministic, rebuildable projection of governed file truth, plus an
ephemeral presence layer, embodying **Step 0 (Discover)** and the
deterministic parts of **Step 1** of the canonical development loop. It is
available to explicitly enabled harnesses acting on behalf of agents and to
the human owner through dashboards — and it is deliberately **the
coordination plane that doesn't need to exist**: files and Git remain the
sole authority, every potential consumer has a file-native fallback, and
deleting PEC degrades throughput, never correctness.

Product definition of record: [`docs/PRD.md`](docs/PRD.md) — v2.2
(v2.0 adopted by `D-PEC-58`; directed-bootstrap clarification adopted by
`D-PEC-61`; exact consumer-interface rows adopted by `D-PEC-67`; surrounding
concordance adopted by `D-PEC-68`). **New here? Read
[`docs/STATUS.md`](docs/STATUS.md) first.**

## State

Pre-implementation. Decomposition revision 1.3 is the accepted current basis
after `SCA-003`; PROJECT_SETUP has materialized the owner-selected full DAG and
scaffolded 11 packages / 64 deliverables; 32 Phase 2.2 ScopeOfWork contracts
are initialized. The reference packets are pinned to PRD v2.2 / revision 1.3;
affected contracts remain stale-frozen under the active reliance hold. Build phases P1–P4 follow under per-tranche packets. See the
standing plan at
`_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md`.

## Layout

| Path | Contents |
|---|---|
| `docs/PRD.md` | Adopted product definition (v2.2, coordination plane) |
| `docs/STATUS.md` | Status & handoff — read first |
| `docs/.archive/` | Retired v0.4/v1.0 product docs (PRD v1.0, SPEC, TRACEABILITY, PILOT, ADRs, prototype README/STATUS) |
| `execution/_Coordination/` | Decision packets, register, coordination records |
| `execution/_Decomposition/` | Accepted software decomposition revision 1.3 and authoritative companion registers |
| `execution/_ScopeChange/` | Immutable SCA-001/SCA-002/SCA-003 amendment evidence and active scope-change pointer |
| `core/`, `server/`, `web/`, `agent-sidecar/`, `tools/`, `fixtures/` | **Frozen reference corpus** — the v0.4-baseline prototype; read/cite only, quarried by citation in build briefs (PRD §13); run instructions preserved at `docs/.archive/README_v0.4_prototype.md` |
| `init/` | Loop launcher prompt (points at `_DomainEngines/pec/LOOP_INIT.md`) |

## Principles the build must keep (PRD §6, PEC-K-01..11)

Graceful absence (no governed act requires PEC) · files govern (rebuildable
projection; rulings file-native) · pull-oriented interface with
consumer-owned use · staleness is a SHA comparison · two trust tiers, never
blurred · observation, not participation · ingest best-effort, reconciliation
guaranteed · everything derived is explainable · optional declared surface ·
content-minimal · mode-capable and never forced.

## Governance

Decisions: `execution/_Coordination/_DECISIONS/_REGISTER.md` (pivot:
`D-PEC-57`; adoption: `D-PEC-58`; directed bootstrap: `D-PEC-61`; exact
consumer rows: `D-PEC-67`; v2.2 concordance: `D-PEC-68`; accepted
decomposition successor: `SCA-003`). Receipts:
`_DomainEngines/pec/LOOP_RECEIPTS.md`. Project agent rules: `AGENTS.md`.
