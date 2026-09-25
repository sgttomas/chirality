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
concordance adopted by `D-PEC-68`). The `D-PEC-79` PRD v2.3 §16.3 postimage
is adopted but not applied; live `docs/PRD.md` remains v2.2. **New here? Read
[`docs/STATUS.md`](docs/STATUS.md) first.**

## State

Early P1 implementation (present-current as of 2026-09-23, `D-PEC-86` §3
I-5). Decomposition revision 1.4 is the accepted current
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
`PEC-HOLD-001` was released by `D-PEC-70`. Current SCA-004 derivative state is
recorded in
`execution/_Coordination/PEC_CURRENCY_REPAIR_CLOSEOUT_2026-08-09/HANDOFF_STATE.md`:
incomplete only for TM-PEC-023. Lifecycle census: 32 `OPEN` / 26
`INITIALIZED` / 4 `CHECKING` / 2 `IN_PROGRESS`, none `ISSUED`. DEL-01-03 is
`IN_PROGRESS` with the `D-PEC-85` store/guard slice produced; DEL-01-05 is
`IN_PROGRESS` after the `D-PEC-84` L reversal; no artifact acceptance or
promotion follows from either. The three DEL-01-03 read-only evidence
inquiries are reported, and the owner ruled `D-PEC-87` on 2026-09-24: one
correction slice on seven existing files, the three inquiry rows to be
ticked, and review of the corrected bytes. The slice merged on 2026-09-24
(PR #893) and the three inquiry rows are ticked; a wider guard residual is
ruled for closure as `D-PEC-89` A, whose slice merged on 2026-09-25 (PR #897);
the L-2a review of the corrected bytes is next. Build phases P1–P4 remain
separately owner-gated. `D-PEC-80` made `projects/pec/loop/` the loop home:
follow `projects/pec/loop/LOOP_INIT.md` to discover
work from deliverable `## Remaining` surfaces. Retired plans live in
`projects/pec/plans/workplans/` as history only. PEC's adoption of the shared
development-loop method is deferred until SCA-005 closes (`D-PEC-86` §3 I-7).

**SCA-005** (feed-model rebaseline) is open under `D-PEC-86`. Its
checkpoint-group-1 package at `execution/_ScopeChange/SCA-005_2026-09-23_2139/`
proposes 76 actions; the owner accepted `Impact_Assessment.md` SHA-256
`0bcbe9bdced43fa887a859497b3edd197242a0eea8fa3a41fab7147b358239bf` on
2026-09-24 (`checkpoint_snapshots/SCA-005_GROUP-1_2026-09-24/`). Owner
checkpoints 2–3 remain. The owner selected the TM-PEC-023 objective values
and deferred the cmux adapter out of scope on 2026-09-24
(`checkpoint_snapshots/SCA-005_GROUP-1_AMENDMENT-1_2026-09-24/`); none is
applied yet. See `docs/STATUS.md` for current gates.

*Historical (2026-08-03; state as of that date):* superseding owner
direction on 2026-08-03 sends TM-PEC-023 to a dedicated
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
is closed here. Since then the currency lane completed on 2026-08-09,
TM-PEC-011/013/014 are archived `CLOSED / RESOLVED_WITH_CHANGE`, and
TM-PEC-023 moved into SCA-005 intake.

## Layout

| Path | Contents |
|---|---|
| `docs/PRD.md` | Adopted product definition (v2.2, coordination plane) |
| `docs/STATUS.md` | Status & handoff — read first |
| `docs/.archive/` | Retired v0.4/v1.0 product docs (PRD v1.0, SPEC, TRACEABILITY, PILOT, ADRs, prototype README/STATUS) |
| `execution/_Coordination/` | Decision packets, register, coordination records |
| `execution/_Decomposition/` | Accepted software decomposition revision 1.4 and authoritative companion registers |
| `execution/_ScopeChange/` | Immutable SCA-001/SCA-002/SCA-003/SCA-004 amendment evidence, the SCA-005 checkpoint-group-1 package and its accepted group-1 snapshot under `checkpoint_snapshots/`, and active scope-change pointer |
| `loop/` | Loop instruction surface (`LOOP_INIT.md`) and receipts ledger (`LOOP_RECEIPTS.md`), per `D-PEC-80` |
| `v2/` | P1 source from owner-ruled slices (`D-PEC-74`, `D-PEC-75`, `D-PEC-77`, `D-PEC-84`, `D-PEC-85`) |
| `core/`, `server/`, `web/`, `agent-sidecar/`, `tools/`, `fixtures/` | **Frozen reference corpus** — the v0.4-baseline prototype; read/cite only, quarried by citation in build briefs (PRD §13); run instructions preserved at `docs/.archive/README_v0.4_prototype.md` |
| `init/` | Loop launcher prompt (points at `projects/pec/loop/LOOP_INIT.md`) |

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
reconciliation and hold release: `D-PEC-69`/`D-PEC-70`; loop home: `D-PEC-80`;
first store/guard slice: `D-PEC-85`; SCA-005 opening: `D-PEC-86`). Receipts:
`projects/pec/loop/LOOP_RECEIPTS.md`. Project agent rules: `AGENTS.md`.
