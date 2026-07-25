# D-PEC-63 — DRAFT v2: PEC Phase 2.2 scope-of-work initialization wave

**Status:** DRAFT v2 — AWAITING_RULING. **The SCA-002 precondition is
DISCHARGED**: decomposition revision 1.2 accepted 2026-07-25 (D-PEC-64
closure, commit `3623b958b`); every wave deliverable carries non-empty
bare-token `SupportsObjectives` in register truth. Re-pins executed
2026-07-25: (1) `DECOMPOSITION_BASIS` = `SOFTWARE_DECOMP.md@3623b958b`
(companion plan §3); (2) objective-reference clauses read the amended
registers (union invariant 0 violations); (3) bare `OBJ-NNN` token
representation confirmed by post-state scan (0 non-conforming tokens
after `;`-split — the brief-construction rule in intake §5.1 governs the
`;`→inline-list conversion at dispatch).
(Drafted 2026-07-25 by PROJECT_SETUP; engine/model: claude-fable-5;
R1-refuted [26 findings] as v1.1; v2 refuted before presentation — logs
in companion plan §6.)
**Decision ID:** D-PEC-63
**Structure precedent:** `D-PEC-62` (ruled packet → sealed Agent 2 execution
→ calibrated deterministic verification → receipt + pointers)
**Companion plan:** `execution/_Coordination/PLAN_2026-07-25_pec_phase_2_2_sow_wave.md`
(wave design, brief template, SCA-002 inventory, refutation log)

## 1. Owner direction of record (2026-07-25 planning session)

1. Phase 2.2 wave accepted: **32 deliverables** (3 pre-P1 + 29 P1), pilot =
   the 9 DAG roots, halt-per-batch early cadence, P2–P4 deferred to later
   packets.
2. Objective-refs gap resolved by owner ruling **"SCA-002 first"**: the
   deliverable→objective mapping is completed in decomposition truth before
   authoring; the SOW-local attribution convention was declined.
3. D-PEC-62 committed and merged 2026-07-25 (`c5e3a6ebd`, local `main`
   fast-forward): "merge but it may be revised again before being put to
   use."
4. Standing steers: opus-5 for Agent 1/2 instances; adversarial refutation
   before every owner gate and closure.

## 2. Basis and preconditions

- Accepted decomposition basis at ruling time: `SOFTWARE_DECOMP.md`
  **revision 1.2** (`current_basis`, SCA-002 successor; accepted
  2026-07-25, D-PEC-64 closure). Pins: commit `3623b958b`; md5s
  `SOFTWARE_DECOMP.md` `961e8e959b7d1965cd1d4153c69a9c43`,
  `Deliverables.csv` `3f807d502df3ed1f35326baed890832a`,
  `ScopeLedger.csv` `9ece6f49fb5fc7f83f72fa897d01a325`. Wave topology
  (32 members, tiers) derives from the accepted DAG (D-PEC-62) and is
  unchanged by SCA-002 (verified: dep-closure values identical pre/post).
  All 32 wave members carry non-empty `SupportsObjectives`
  (wave-unmapped 17 → 0 at SCA-002 closure).
- D-GOV-16 **RULED APPROVED** 2026-07-12
  (`docs/governance_harness/_DECISIONS/_REGISTER.md:29`): the deliverable
  SOW standard is active; "New deliverables use `SOW_V1`"
  (`docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` §7). The pending Stage-2
  TYPES/SPEC patches and legacy-corpus conversion do not touch greenfield
  INIT.
- Precondition checks at ruling: SCA-002 closed
  (`CLOSED_FOR_SCOPE_CHANGE_ONLY`, evidence
  `execution/_ScopeChange/SCA-002_2026-07-25_1042/`, Receipt 109) with
  every wave deliverable carrying non-empty objective refs in register
  truth — **SATISFIED 2026-07-25**; clean `git status` baseline for the
  wave paths (satisfied at the SCA-002 closure commit `3623b958b`).

## 3. Ruled behavior (proposed)

### 3.1 Contract authoring
One sealed `TASK + TaskSkill: scope-of-work, MODE=INIT` dispatch per
deliverable (ephemeral opus-5 Agent 2), per the canonical brief in the
companion plan §3. INIT is source-grounded authoring; the skill's
conversion machinery (claim map / parity / finalizer) is not invoked. Tool
sequence per run: author → `tools/scope_of_work/validate_scope_of_work.py`
(to PASS) → `derive_review_checklist.py` (stdout; item_count reported).
Batches B1–B8 per the companion plan §1; concurrency ≤ 4; canary-3 inside
B1; owner halts after B1 and B2; internal fan-in thereafter if clean.

### 3.2 Status advancement (separate deterministic act)
The scope-of-work skill's `_STATUS.md` prohibition is **honored, not
overridden**. After each batch's fan-in passes, one generic-shell TASK (no
skill, opus-5) with `ScopePath:
{WORKING_ROOT}/execution/_Coordination/WAVE_D-PEC-63` and
`AllowedWriteTargets` = the batch's explicit `<DEL_PATH>/_STATUS.md` list
**plus `{ScopePath}/_run_records/`** (TASK requires the run-record
enclosure) re-runs the validator per deliverable and, only on
`PASS format=SOW_V1`, runs
`tools/scaffolding/write_status.sh "<DEL_PATH>" INITIALIZED "TASK+status-advance"`
(the tool takes a path, not an ID; forward-only guard). On any FAIL: skip,
do not advance, report. Warrant: standard §8 — `INITIALIZED` means the
production contract exists and validates — under D-GOV-16; this is the
human-confirmed lifecycle policy contemplated by AGENT_PROJECT_SETUP
(scope-of-work INIT "may support INITIALIZED only after validated SOW_V1
… under the human-confirmed lifecycle policy").

### 3.3 Fan-in and cadence (PROJECT_SETUP-owned)
Per batch, before the status act: return-report conformance (RUN_STATUS,
resolved skill version `1`, three companion files found,
ToolPolicyCompliance PASS, WriteAuthorization ALLOWED_WRITE_TARGETS);
independent validator re-run; `git status --porcelain` against the batch
fence; contract reading (all of B1; ≥1 full read + every CON/TBD
thereafter); then status act; census + blocker snapshot; batch fan-in
record `WAVE_D-PEC-63/BATCH_B{n}_FANIN.md`; one scoped commit per batch.
Failure rules: single FAIL → deliverable stays OPEN, fresh re-dispatch
(no inline repair); two consecutive FAILs or any CONFLICT → owner halt;
any scope violation re-arms per-batch halts for the remainder.

### 3.4 Blocker-state advisory reporting
`execution/_Coordination/WAVE_D-PEC-63/report_blocker_state.py`
(report-only, packet-local, exit 0 always): EXECUTION/UPSTREAM/ACTIVE
edges from deliverable-local registers; lifecycle via the
`**Current State:**` line only; C-08 standing-target edges excluded and
counted; satisfied iff state ≥ RequiredMaturity (threshold `INITIALIZED`,
ruled). No register mutation — `SatisfactionStatus` refresh is explicitly
deferred to a later `TASK + dependency-extract` packet. Output is advisory
visibility only, never work assignment. Exit semantics: exit 0 on a
completed report; exit 2 on IO/parse failure — a non-zero exit is a halt
signal, never a blocker verdict.

### 3.5 Out of scope
No `_SEMANTIC.md` / `_SEMANTIC_LENSING.md` work, no P3 enrichment, no
source tree, no dependency-register edits, no `SatisfactionStatus` writes,
no P2–P4 deliverables, no decomposition edits. **F-PEC-1 stays closed** —
this packet authorizes contract authoring, not source work.

### 3.6 Git acts, receipt, and pointers
**Batch commits (R1a-F15):** this packet explicitly authorizes
PROJECT_SETUP to perform one scoped commit per batch (and the closure
commit) under the project closeout discipline (`projects/pec/AGENTS.md`
Closeout section): stage only the batch's declared fence paths, verify
scope-clean first, no push. Rollback granularity depends on these commits;
`write_status.sh` blocks backward transitions, so revert is the only
state walk-back.

**Receipt and pointers (at closure):**
One receipt appended to `_DomainEngines/pec/LOOP_RECEIPTS.md`; D-PEC-63
row added to `_DECISIONS/_REGISTER.md`; `_COORDINATION.md` gains a ruling
item; `docs/STATUS.md` "What's next" item 1 amended (wave executed; next
open gate = P1 implementation packets); companion-plan position marker and
closure verdict updated.

## 4. Exact fence (writes authorized when RULED)

```
projects/pec/execution/PKG-{00,01,02,03,04,08,10}_*/1_Working/{the 32 named DEL folders}/
    ScopeOfWork.md      — creation only
    _STATUS.md          — the single OPEN→INITIALIZED transition via write_status.sh only
    _run_records/       — TASK run records
projects/pec/execution/_Coordination/WAVE_D-PEC-63/**       — script, snapshots, fan-in records, run records
projects/pec/execution/_Coordination/PLAN_2026-07-25_pec_phase_2_2_sow_wave.md — position/log updates
projects/pec/execution/_Coordination/_DECISIONS/D-PEC-63_*.md — this packet's status updates
projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md  — one row at closure
projects/pec/execution/_Coordination/_COORDINATION.md         — one ruling item at closure
_DomainEngines/pec/LOOP_RECEIPTS.md                           — append one receipt
projects/pec/docs/STATUS.md                                   — item-1 amendment only
```
The 32 folders are exactly the companion plan §1 batch table. Explicitly
excluded: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`,
`Dependencies.csv`, `_SEMANTIC.md`, `execution/_Decomposition/**`,
`docs/PRD.md`, all P2–P4 deliverable folders, any source tree.

## 5. Verification (calibrated; empirical values re-confirmed at each batch)

1. Authoring: per batch, n/n `PASS format=SOW_V1` on independent re-run of
   `validate_scope_of_work.py`; n/n `derive_review_checklist.py` exit 0.
2. Census (`grep -h '^\*\*Current State:\*\*' …/_STATUS.md | sort | uniq -c`;
   never `count_workspace_state.sh` post-transition — history-substring
   defect): INITIALIZED ladder after B1→B8 = 9, 12, 18, 19, 25, 29, 31,
   **32**; final `32 INITIALIZED / 32 OPEN`.
3. Scope: per batch, `git status --porcelain` shows exactly n new
   `ScopeOfWork.md`, n modified `_STATUS.md`, n run-record additions + the
   declared coordination artifacts; zero other paths.
4. Blocker snapshots: baseline **54 BLOCKED / 10 UNBLOCKED** (9 roots +
   DEL-10-11, expected standing-edge divergence); closure **40 UNBLOCKED /
   24 BLOCKED with all 32 wave members UNBLOCKED**.
5. Structural invariant at every batch:
   `analyze_dep_closure.py projects/pec/execution` unchanged from D-PEC-62
   landing (64 files, 255 rows, 135 ANCHOR / 120 EXECUTION, 62 nodes /
   120 edges, orphans 2, SCCs 0).
6. Basis md5s (rev 1.2 pin) re-checked pre-batch; mismatch → halt and
   resurface.

## 6. Rollback

One scoped commit per batch. Rollback = revert the batch commit(s) in
reverse order, plus a follow-on commit annotating the receipt as
superseded (a revert alone deletes the receipt line — D-PEC-62 lesson),
plus manual removal of untracked `_run_records/` residue. `write_status.sh`
blocks backward transitions; file revert is the only state walk-back,
which is why batch commits are mandatory.

## 7. Human ruling

**PENDING — presented after SCA-002 closes and this draft is re-pinned to
revision 1.2 (draft v2) and refuted.** Proposed ruling text: "D-PEC-63 is
RULED as drafted: the Phase 2.2 wave (32 deliverables, B1–B8, pilot-first
cadence) may execute under the stated fence, status mechanism, and
verification set." The ruling presentation also carries policy questions
Q1 (semantic-phase posture 2.3–2.5) and Q2 (OI-013 tooling consolidation)
from the companion plan §5 — both answerable without blocking the wave.
