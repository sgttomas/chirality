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
check profile. DEL-08-02 is `CHECKING`. D-PEC-77 later accepted the exact
DEL-01-05 enforcement inventory, confirmed AC-010 and AC-011 G-A, and advanced
DEL-01-05 to `CHECKING`. **D-PEC-75 remains ruled O-A for DEL-01-06.** Its
accepted revision-1.4 production contract is SHA-256
`5fdcfd96834509e32a4df1fc001932fe7a0c5d4c5d96becb9acca0be3c4a2fa8`.
The current SELF_CHECK snapshot
`execution/_Evaluation/Reviews/REV_DEL-01-06_2026-08-04_1113/` records
AC-001 through AC-006 `PASS`, RF-001 `RESOLVED` with exact VER-005 evidence,
and RF-002 `REVISE / RESOLVED`: the accepted successor maps SOW-077 and SOW-094
to DEL-01-06 and records OI-003 resolved by D-PEC-78 O-A. DEL-01-06 remains
`INITIALIZED` under HOLD; no product/source artifact, next P1 node, release, or
professional reliance is authorized. D-T0-27 remains `ADOPTED / READ_ONLY`
through PR #459 merge `d9dc65804a0719fdf869af1ef60d53dc8cb0a895`; D-PEC-76
creates no duplicate adoption. Decomposition revision 1.4 is the accepted
current basis after `SCA-004`. PROJECT_SETUP has completed the 64-context,
64-reference, and DEL-01-06 SOW-077-anchor subset; its closure handoff is
`execution/_Coordination/PROJECT_SETUP_SCA004_METADATA_ALIGNMENT_2026-08-03/HANDOFF_STATE.md`.
The nine TM-PEC-023 objective blanks remain held pending an exact
SCOPE_CHANGE mapping-or-retain-blank ruling. Nothing in the PRD is an
implementation mandate; each tranche needs its own owner-ruled packet.

**Superseding owner ruling, 2026-08-03:** TM-PEC-023 now proceeds through a
dedicated SCOPE_CHANGE mapping session; neither mappings nor blank retention is
ruled, the nine values and COV-062..COV-070 remain open, and no urgency or
downstream gate is implied. RF-002 disposition is `REVISE`, and execution plus
exact revised-SOW acceptance complete at `REV_DEL-01-06_2026-08-04_1113`;
RF-002 is `REVISE / RESOLVED`, Gate 5 remains HOLD, and DEL-01-06 remains
`INITIALIZED`. Metadata alignment is cleared. `DerivativePackageState` remains
`INCOMPLETE` for exactly two component categories: (1) the TM-PEC-023
mapping-session amendment and (2) ordinary SOW/SPEC currency already carried
by SCA-004 / TM-PEC-013/014 for DEL-02-07, DEL-03-01, DEL-04-01, and DEL-00-03.
TM-PEC-011 remains `OPEN` with stale source evidence pending a separate
TASK_MANAGEMENT disposition. No row is closed by this status note.

**The old application** (v0.4-baseline prototype: `core/`, `server/`, `web/`,
`agent-sidecar/`, `tools/`, `fixtures/`) is a **frozen reference corpus** —
read and cite only, no further feature work, retired product docs under
`docs/.archive/`. Source-tree archival is a future packet after Phase 2
(PRD v2 §13). Historical run instructions:
`docs/.archive/README_v0.4_prototype.md`.

## What's next (owner gates, in order)

0. ~~Decomposition~~ — **accepted 2026-07-24** (`D-PEC-60`, Gates 1–7).
   The canonical working package at `execution/_Decomposition/`
   (`SOFTWARE_DECOMP.md` rev 1.4 `current_basis` after `SCA-004`
   + four CSV registers +
   `_LATEST.md` handoff state) is the authoritative downstream basis:
   11 packages (PKG-00..PKG-10), 64 deliverables, 94-row scope ledger.
1. **PROJECT_SETUP / first build tranches** — materialize the owner-selected
   full dependency DAG from revision 1.1 (topology preserved through
   revision 1.2 / `SCA-002`, revision 1.3 / `SCA-003`, and revision 1.4 /
   `SCA-004`) before scaffolding
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
   *(amended 2026-08-03 after SCA-004: revision 1.4 is accepted under
   D-PEC-78 O-A; PROJECT_SETUP aligned 64/64 context provenance blocks,
   64/64 reference packets, and the DEL-01-06 non-gating SOW-077 anchor.
   TM-PEC-023 remains held pending an exact mapping-or-retain-blank ruling;
   DEL-01-06 RF-002 was later resolved by exact successor acceptance at
   `REV_DEL-01-06_2026-08-04_1113`.)*
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
   SOW is owner-accepted as the production contract, D-T0-27 is effective by
   PR #459 merge identity, and WORKING_ITEMS completed only packet §§5.3–5.6.
   PR #463 merged exact REVIEW source
   `922ca0ea68d255b65292d59db89a98ef4cf59bc5` as
   `a753a7b0894371437a6add0f92653037e2df2dec`. DEL-01-05 later became
   available and the mandatory SELF_CHECK rerun passed: AC-001..006 pass,
   RF-001 is resolved without waiving VER-005, and exact evidence is recorded
   in `REV_DEL-01-06_2026-08-03_1458`. SCA-004 then exposed RF-002: the
   revision-1.3 SOW was stale against revision 1.4 and D-PEC-78 O-A. The
   separately scheduled WORKING_ITEMS + REVIEW act accepted exact successor
   SHA-256 `5fdcfd96834509e32a4df1fc001932fe7a0c5d4c5d96becb9acca0be3c4a2fa8`
   and resolved RF-002 at `REV_DEL-01-06_2026-08-04_1113`; Gate 5 continues to
   hold DEL-01-06 at `INITIALIZED`. No product/source artifact, next P1 node,
   release, or professional reliance is authorized.
2. P2 dashboards → P3 opt-in consumer-integration capability (falsification
   clause armed; receiving consumers retain their own authority and cadence) →
   P4 streams are historical phase orientation; live work is discovered from
   deliverable `## Remaining` surfaces under `loop/LOOP_INIT.md`.

## Orient yourself (read-order)

1. `docs/PRD.md` — the adopted product definition (v2.2), including the
   invariants (PEC-K-01..11), modes ladder, and release strategy.
2. `projects/pec/loop/LOOP_INIT.md` — protocol, gates, fences and deliverable
   discovery. `projects/pec/plans/workplans/` is history only.
3. `execution/_Coordination/_DECISIONS/_REGISTER.md` — decision register
   (D-PEC-57/58 are the pivot and adoption rows).
4. `projects/pec/loop/LOOP_RECEIPTS.md` — handoff ledger.

## Governance & agent harness

Project-local agent rules: `AGENTS.md` (rewritten 2026-07-24, `D-PEC-59`).
Decomposition session ruled and closed 2026-07-24 (`D-PEC-60`, Gates 1–7
accepted; `execution/_Decomposition/**` opened by its fence for the
canonical working package). Directed-bootstrap amendment `SCA-001` closed
2026-07-24 under `D-PEC-61`; objective-mapping amendment `SCA-002` closed
2026-07-25 under `D-PEC-64`; SCA-003 closed 2026-07-28; and SCA-004 closed
for scope change on 2026-08-03 with revision 1.4 as `current_basis` under
D-PEC-78 O-A. All four sessions' immutable evidence lives under
`execution/_ScopeChange/`. `D-PEC-67` adopted exact pull-oriented /
consumer-owned invariant rows; `D-PEC-68` reconciled the surrounding PRD;
SCA-003 propagated C3/C15 and direct mirrors into accepted decomposition
truth without changing topology, dependencies, lifecycle, or implementation.
`D-PEC-69` then reconciled the complete affected ScopeOfWork population;
`D-PEC-70` released the exceptional reliance hold. SCA-004 resolved OI-003
in decomposition truth, the metadata subset is current, and DEL-01-06 RF-002
is resolved by exact successor acceptance; the nine TM-PEC-023 objective
blanks remain separately owner-gated. P1
source work remains separately owner-gated and fenced by `F-PEC-1`.
Domain-engine profile `_DomainEngines/profiles/pec.yaml` contains the exact
D-T0-27 O-A PEC v2 `ADOPTED / READ_ONLY` postimage and is validator `VALID`,
effective through PR #459 merge
`d9dc65804a0719fdf869af1ef60d53dc8cb0a895`; D-T0-28/D-T0-29 are effective
supporting amendments. The profile creates no invocation by itself. The
frozen v0.4 profile is preserved as historical preimage lineage.
Fences F-PEC-1..4 (`D-T0-15`) remain in force.
