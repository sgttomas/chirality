# PEC — status & handoff

The single "where are we, what's next" file. Keep it current when substantial
work lands — durable state lives in repo files, not in chat history.

_Reset 2026-07-24: the coordination-plane pivot (`D-PEC-57`) and PRD v2.0
adoption (`D-PEC-58`). The prior prototype status file is preserved at
`docs/.archive/STATUS_2026-07-04_prototype.md`._

## Current state

**Product:** PEC is the **Chirality coordination plane** — a deterministic,
rebuildable projection of governed file truth plus an ephemeral presence
layer, embodying loop Step 0 (Discover) and the deterministic parts of Step 1
(gate review, decision-slate presentation). It is "the coordination plane
that doesn't need to exist": no governed act may ever require it.
**`docs/PRD.md` v2.0 is the product definition of record (adopted 2026-07-24,
`D-PEC-58`).**

**Implementation:** none yet. The coordination plane is pre-decomposition;
nothing in the PRD is an implementation mandate (each tranche needs its own
owner-ruled packet).

**The old application** (v0.4-baseline prototype: `core/`, `server/`, `web/`,
`agent-sidecar/`, `tools/`, `fixtures/`) is a **frozen reference corpus** —
read and cite only, no further feature work, retired product docs under
`docs/.archive/`. Source-tree archival is a future packet after Phase 2
(PRD v2 §13). Historical run instructions:
`docs/.archive/README_v0.4_prototype.md`.

## What's next (owner gates, in order)

1. **Decomposition** — SOFTWARE_DECOMP over PRD v2 with the owner at
   Gates 1–7 (`docs/DECOMPOSITION_STANDARD.md`); Gate 7 acceptance becomes
   the downstream basis for all build tranches.
2. **P1 — one-loop reconciler** (per-tranche packets): reconciler +
   orientation store + read-only API for one loop; parity-diffed against the
   practitioner harness; kill test standing.
3. P2 dashboards → P3 harness integration (falsification clause armed) →
   P4 streams, per the standing plan.

## Orient yourself (read-order)

1. `docs/PRD.md` — the adopted product definition (v2.0), including the
   invariants (PEC-K-01..11), modes ladder, and release strategy.
2. `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md` — the
   standing plan (loop protocol, gates, fences).
3. `execution/_Coordination/_DECISIONS/_REGISTER.md` — decision register
   (D-PEC-57/58 are the pivot and adoption rows).
4. `_DomainEngines/pec/LOOP_RECEIPTS.md` — handoff ledger.

## Governance & agent harness

Project-local agent rules: `AGENTS.md` (rewrite is a named follow-on packet).
Domain-engine profile `_DomainEngines/profiles/pec.yaml` is pending
supersession — its `chirality_readable_artifacts` enumeration predates the
2026-07-24 docs archive and is partially stale (recorded in the `D-PEC-58`
packet's coordination notice). Fences F-PEC-1..4 (`D-T0-15`) remain in force.
