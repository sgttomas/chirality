# PEC — status & handoff

The single "where are we, what's next" file. Keep it current when substantial
work lands — durable state lives in repo files, not in chat history.

_Reset 2026-07-24: the coordination-plane pivot (`D-PEC-57`), PRD v2.0
adoption (`D-PEC-58`), and directed-bootstrap clarification to v2.1
(`D-PEC-61`). The prior prototype status file is preserved at
`docs/.archive/STATUS_2026-07-04_prototype.md`._

## Current state

**Product:** PEC is the **Chirality coordination plane** — a deterministic,
rebuildable projection of governed file truth plus an ephemeral presence
layer, embodying loop Step 0 (Discover) and the deterministic parts of Step 1
(gate review, decision-slate presentation). It is "the coordination plane
that doesn't need to exist": no governed act may ever require it.
**`docs/PRD.md` v2.1 is the product definition of record (v2.0 adopted
2026-07-24 by `D-PEC-58`; directed-bootstrap clarification adopted by
`D-PEC-61`).**

**Implementation:** none yet. Decomposition revision 1.1 is the accepted
current basis after `SCA-001`; PROJECT_SETUP is released with `FULL_GRAPH`
already selected. Nothing in the PRD is an implementation mandate (each
tranche needs its own owner-ruled packet).

**The old application** (v0.4-baseline prototype: `core/`, `server/`, `web/`,
`agent-sidecar/`, `tools/`, `fixtures/`) is a **frozen reference corpus** —
read and cite only, no further feature work, retired product docs under
`docs/.archive/`. Source-tree archival is a future packet after Phase 2
(PRD v2 §13). Historical run instructions:
`docs/.archive/README_v0.4_prototype.md`.

## What's next (owner gates, in order)

0. ~~Decomposition~~ — **accepted 2026-07-24** (`D-PEC-60`, Gates 1–7).
   The canonical working package at `execution/_Decomposition/`
   (`SOFTWARE_DECOMP.md` rev 1.1 `current_basis` + four CSV registers +
   `_LATEST.md` handoff state) is the authoritative downstream basis:
   11 packages (PKG-00..PKG-10), 64 deliverables, 94-row scope ledger.
1. **PROJECT_SETUP / first build tranches** — materialize the owner-selected
   full dependency DAG from revision 1.1 before scaffolding and the P1 slice
   (32 deliverables: parsers, reconciler + parity, orientation core,
   socket API, kill test, bootstrap self-ingest; plus pre-P1 DEL-00-01
   ADRs, DEL-00-03 SPEC seed, DEL-10-01 Step-0 baseline). **Each tranche
   requires its own owner-ruled `D-PEC` packet** — nothing is authorized
   yet; `F-PEC-1` remains the outer fence.
2. P2 dashboards → P3 harness integration (falsification clause armed) →
   P4 streams, per the standing plan and the deliverables' PhaseHints.

## Orient yourself (read-order)

1. `docs/PRD.md` — the adopted product definition (v2.1), including the
   invariants (PEC-K-01..11), modes ladder, and release strategy.
2. `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md` — the
   standing plan (loop protocol, gates, fences).
3. `execution/_Coordination/_DECISIONS/_REGISTER.md` — decision register
   (D-PEC-57/58 are the pivot and adoption rows).
4. `_DomainEngines/pec/LOOP_RECEIPTS.md` — handoff ledger.

## Governance & agent harness

Project-local agent rules: `AGENTS.md` (rewritten 2026-07-24, `D-PEC-59`).
Decomposition session ruled and closed 2026-07-24 (`D-PEC-60`, Gates 1–7
accepted; `execution/_Decomposition/**` opened by its fence for the
canonical working package). Directed-bootstrap amendment `SCA-001` closed
2026-07-24 under `D-PEC-61`; revision 1.1 is `current_basis` and its
immutable evidence lives under `execution/_ScopeChange/`.
Domain-engine profile `_DomainEngines/profiles/pec.yaml` was amended
2026-07-24 (`D-PEC-59`: post-archive readable-artifact paths + pivot notes;
validator VALID); full supersession remains pending v2 implementation shape.
Fences F-PEC-1..4 (`D-T0-15`) remain in force.
