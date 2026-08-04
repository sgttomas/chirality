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

Early P1 implementation. Decomposition revision 1.4 is the accepted current
basis after `SCA-004` under `D-PEC-78` O-A; PROJECT_SETUP has materialized the
owner-selected full DAG, scaffolded 11 packages / 64 deliverables, and completed
the SCA-004 metadata-alignment subset: 64/64 context provenance blocks and
64/64 reference packets are current, and DEL-01-06 carries the non-gating
SOW-077 requirement anchor. Thirty-two Phase 2.2 ScopeOfWork contracts are
initialized. DEL-01-06 now has the accepted revision-1.4 production contract
at SHA-256 `5fdcfd96834509e32a4df1fc001932fe7a0c5d4c5d96becb9acca0be3c4a2fa8`;
RF-001 and RF-002 are resolved, while Gate 5 remains HOLD at `INITIALIZED`.
The earlier
eleven-contract reconciliation remains historical under `D-PEC-69`, and
`PEC-HOLD-001` was released by `D-PEC-70`. Current derivative state is recorded
in `execution/_Coordination/PROJECT_SETUP_SCA004_METADATA_ALIGNMENT_2026-08-03/HANDOFF_STATE.md`
and the WORKING_ITEMS currency-sweep handoff. Build phases P1–P4 remain
separately owner-gated. See the standing plan at
`_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md`.

Superseding owner direction on 2026-08-03 sends TM-PEC-023 to a dedicated
SCOPE_CHANGE mapping session: neither mappings nor blanks are ruled, all nine
values and COV-062..COV-070 remain open, and no downstream gate or urgency is
created. RF-002 owner disposition `REVISE` is resolved: the SOW revision and
exact REVIEW acceptance are complete at snapshot
`REV_DEL-01-06_2026-08-04_1113`; Gate 5 remains HOLD at unchanged
`INITIALIZED`. Metadata alignment itself is cleared. Derivative state remains
`INCOMPLETE` only for two component categories: the TM-PEC-023 mapping-session
amendment and the ordinary SOW/SPEC currency lane under TM-PEC-013/014 for
DEL-02-07, DEL-03-01, DEL-04-01, and DEL-00-03. TM-PEC-011 remains `OPEN` with
stale source evidence pending a separate TASK_MANAGEMENT disposition; no row
is closed here.

## Layout

| Path | Contents |
|---|---|
| `docs/PRD.md` | Adopted product definition (v2.2, coordination plane) |
| `docs/STATUS.md` | Status & handoff — read first |
| `docs/.archive/` | Retired v0.4/v1.0 product docs (PRD v1.0, SPEC, TRACEABILITY, PILOT, ADRs, prototype README/STATUS) |
| `execution/_Coordination/` | Decision packets, register, coordination records |
| `execution/_Decomposition/` | Accepted software decomposition revision 1.4 and authoritative companion registers |
| `execution/_ScopeChange/` | Immutable SCA-001/SCA-002/SCA-003/SCA-004 amendment evidence and active scope-change pointer |
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
consumer rows: `D-PEC-67`; v2.2 concordance: `D-PEC-68`; loop-registry ruling:
`D-PEC-78`; accepted decomposition successor: `SCA-004`; historical contract
reconciliation and hold release: `D-PEC-69`/`D-PEC-70`). Receipts:
`_DomainEngines/pec/LOOP_RECEIPTS.md`. Project agent rules: `AGENTS.md`.
