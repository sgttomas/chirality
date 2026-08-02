# PEC — status & handoff

The single "where are we, what's next" file. Keep it current when substantial
work lands — durable state lives in repo files, not in chat history.

_Reset 2026-07-24 and amended 2026-07-27: the coordination-plane pivot
(`D-PEC-57`), PRD v2.0 adoption (`D-PEC-58`), directed-bootstrap
clarification to v2.1 (`D-PEC-61`), exact consumer-interface rows
(`D-PEC-67`), and surrounding concordance to v2.2 (`D-PEC-68`). The prior
prototype status file is preserved at
`docs/.archive/STATUS_2026-07-04_prototype.md`._

## Current state

**Product:** PEC is the **Chirality coordination plane** — a deterministic,
rebuildable projection of governed file truth plus an ephemeral presence
layer, embodying loop Step 0 (Discover) and the deterministic parts of Step 1
(gate review, decision-slate presentation). It is "the coordination plane
that doesn't need to exist": no governed act may ever require it.
**`docs/PRD.md` v2.2 is the product definition of record (v2.0 adopted
2026-07-24 by `D-PEC-58`; directed-bootstrap clarification adopted by
`D-PEC-61`; exact PEC-K-03/-11 rows adopted by `D-PEC-67`; surrounding
consumer-interface concordance adopted by `D-PEC-68`).**

**Implementation:** the first bounded P1 slice is reviewed and exact-byte
accepted under `D-PEC-74` O-A: the DEL-08-02 version-1 API JSON Schema,
standard-library additive compatibility tests/fixtures, and exact registered-
check profile. The five-item SELF_CHECK has zero findings; AC-005 is owner-
confirmed at its recorded MEDIUM confidence; the exact schema, test, and three
fixture bytes are accepted; and DEL-08-02 is `CHECKING`. No service, store,
transport, runtime integration, later P1 node, release, or professional
reliance is authorized. **D-PEC-75 is ruled O-A for DEL-01-06:** its bounded
contract-currency repair and SELF_CHECK are complete. Snapshot
`REV_DEL-01-06_2026-08-02_0954` records zero findings, AC-001 through AC-006
`PENDING FUTURE PRODUCTION`, and owner Gate 5 `HOLD` at `INITIALIZED`. The
owner accepted exact SOW SHA-256
`7dfa008b44d7425ab7e4fc47260d089c3d739416d666f52657d7093492ecf38a`
as the DEL-01-06 production contract. REVIEW and SOW acceptance independently
open no source. Source remains dormant until D-T0-27 becomes effective through
exact PR #459 merge identity and serialized manager fan-in. D-T0-27 O-A is
ruled and its exact PEC-v2 `ADOPTED / READ_ONLY` successor postimage is
materialized; D-T0-28/D-T0-29 application checks pass and are ready for
CHANGE, but the chain is not effective before that merge. D-PEC-76 points to that Tier-0 ruling;
following D-PEC-11 precedent, D-T0-27 owns the semantic profile act and
D-PEC-76 creates no duplicate adoption. D-PEC-75 grants no domain-profile,
source, project-workflow, lifecycle, or artifact-fitness act.
Decomposition revision
1.3 is the accepted current basis after `SCA-003` (2026-07-28; revision 1.2
was the `SCA-002` basis); PROJECT_SETUP remains released with `FULL_GRAPH`
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
   (`SOFTWARE_DECOMP.md` rev 1.3 `current_basis` after `SCA-003`
   + four CSV registers +
   `_LATEST.md` handoff state) is the authoritative downstream basis:
   11 packages (PKG-00..PKG-10), 64 deliverables, 94-row scope ledger.
1. **PROJECT_SETUP / first build tranches** — materialize the owner-selected
   full dependency DAG from revision 1.1 (topology preserved through
   revision 1.2 / `SCA-002` and revision 1.3 / `SCA-003`) before scaffolding
   and the P1 slice
   *(amended by `D-PEC-62`, 2026-07-25: owner-ruled deliverable-local
   storage makes materialization co-land **with** scaffolding — DAG gate
   ruled, 11 packages / 64 deliverables scaffolded `OPEN`, local
   `Dependencies.csv` v3.1 registers seeded)*
   *(amended by `D-PEC-63`, 2026-07-25: the Phase 2.2 scope-of-work
   initialization wave executed — all 32 wave deliverables (3 pre-P1 +
   29 P1) carry validated `ScopeOfWork.md` production contracts at
   `INITIALIZED`; batches B1–B8 each closed with per-batch fan-in,
   adversarial refutation, and scoped commits; terminal census 32
   INITIALIZED / 32 OPEN; advisory blocker state 40 UNBLOCKED / 24
   BLOCKED with all wave members unblocked; P1 build-slice packets
   remain the open gate — `F-PEC-1` still fences source work, and
   WORKING_ITEMS is the post-wave owning workflow)*
   *(amended by `D-PEC-65`, 2026-07-25/26: the 120 seeded EXECUTION register evidence rows repaired — validator exit 0, 119 repaired + 1 declared waiver; evidence Receipt 111)*
   *(amended by `D-PEC-66`, 2026-07-26: E-N13 declined (254 rows / 119 edges, zero waivers, validator fully clean incl. `--strict`), DEL-10-10 REQ-011 repaired, all 21 QA-item-20 rows dispositioned; evidence Receipt 112)*
   *(amended 2026-07-28 after SCA-003: revision 1.3 is accepted;
   PROJECT_SETUP re-pinned all 64 `_REFERENCES.md` packets to PRD v2.2 /
   revision 1.3; `D-PEC-69` reconciled the 11 affected complete contracts
   and `D-PEC-70` released `PEC-HOLD-001` after full-corpus validation.)*
   *(amended by `D-PEC-72`, 2026-08-01: the three C-05 pre-P1 obligations
   completed SELF_CHECK and exact-hash owner acceptance; DEL-00-01,
   DEL-00-03, and DEL-10-01 are `CHECKING`; the owner closed C-05 at the
   post-acceptance handoff. No deliverable is `ISSUED` and no P1 node or
   source/profile path is opened.)*
   (32 deliverables: parsers, reconciler + parity, orientation core,
   socket API, kill test, bootstrap self-ingest; plus pre-P1 DEL-00-01
   ADRs, DEL-00-03 SPEC seed, DEL-10-01 Step-0 baseline). **D-PEC-74 is ruled
   O-A for the first actual P1 source slice.** Only DEL-08-02 is selected and
   activated as the API-contract canary under the packet's exact
   `projects/pec/v2/` paths, exact `software-workflow.json` content, checks,
   owner gates, rollback, and authority fence. WORKING_ITEMS has completed the
   exact producer slice: both registered checks pass, additive evolution
   passes, and seeded removal/meaning changes fail with located explanations.
   PR #455 merged the five-item SELF_CHECK with zero findings. Owner Gate 5
   advanced DEL-08-02 to `CHECKING`; AC-005's MEDIUM-confidence OBJ-001
   attribution is confirmed with alternatives unadopted; and only the exact
   schema/test/three-fixture bytes recorded in the D-PEC-74 handoff are
   accepted. DEL-08-02 remains short of `ISSUED`, and every later P1 node,
   release, and professional-reliance act remains separately gated.
   `F-PEC-1` remains closed outside the exact O-A fence.
   **D-PEC-75 O-A selects DEL-01-06 as the second slice.** Its exact repaired
   SOW is owner-accepted as the production contract, but Gate 5 holds
   lifecycle at `INITIALIZED`; all six ACs remain pending future production.
   The exact source fence remains dormant until D-T0-27 becomes effective by
   PR #459 merge identity and WORKING_ITEMS verifies the serialized gates.
2. P2 dashboards → P3 opt-in consumer-integration capability (falsification
   clause armed; receiving consumers retain their own authority and cadence) →
   P4 streams, per the standing plan and the deliverables' PhaseHints.

## Orient yourself (read-order)

1. `docs/PRD.md` — the adopted product definition (v2.2), including the
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
2026-07-24 under `D-PEC-61`; objective-mapping amendment `SCA-002` closed
2026-07-25 under `D-PEC-64`; SCA-003 closed 2026-07-28 and revision 1.3
is `current_basis`; all three sessions' immutable evidence lives under
`execution/_ScopeChange/`. `D-PEC-67` adopted exact pull-oriented /
consumer-owned invariant rows; `D-PEC-68` reconciled the surrounding PRD;
SCA-003 propagated C3/C15 and direct mirrors into accepted decomposition
truth without changing topology, dependencies, lifecycle, or implementation.
`D-PEC-69` then reconciled the complete affected ScopeOfWork population;
`D-PEC-70` released the exceptional reliance hold. P1 source work remains
separately owner-gated and fenced by `F-PEC-1`.
Domain-engine profile `_DomainEngines/profiles/pec.yaml` contains the exact
D-T0-27 O-A PEC v2 `ADOPTED / READ_ONLY` postimage and is validator `VALID`,
and D-T0-28/D-T0-29 application checks pass, but the application is not
effective before exact PR #459 publication, committed-range checks, and merge
identity. The frozen v0.4 profile is preserved as
historical preimage lineage.
Fences F-PEC-1..4 (`D-T0-15`) remain in force.
