# PEC — status & handoff

The single "where are we, what's next" file. Keep it current when substantial
work lands — durable state lives in repo files, not in chat history.

_Reset 2026-07-24 and amended 2026-07-27: the coordination-plane pivot
(`D-PEC-57`), PRD v2.0 adoption (`D-PEC-58`), directed-bootstrap
clarification to v2.1 (`D-PEC-61`), exact consumer-interface rows
(`D-PEC-67`), and surrounding concordance to v2.2 (`D-PEC-68`). The prior
prototype status file is preserved at
`docs/.archive/STATUS_2026-07-04_prototype.md`. Present-current prose
refreshed 2026-09-23 under `D-PEC-86` §3 I-5 and again 2026-09-24 after the checkpoint-1 acceptance, after the `D-PEC-87` ruling, and after the TM-PEC-023/cmux acts (present-current lines only), and maintained from then on under the standing clause `D-PEC-88`; earlier paragraphs that no
longer describe the current state are labelled historical, not deleted._

## Current state

**Product:** PEC is the **Chirality coordination plane** — a deterministic,
rebuildable projection of governed file truth plus an ephemeral presence
layer, embodying loop Step 0 (Discover) and the deterministic parts of Step 1
(gate review, decision-slate presentation). It is "the coordination plane
that doesn't need to exist": no governed act may ever require it.
**`docs/PRD.md` v2.4 is the product definition of record.**
- It was adopted 2026-09-25 by the owner's SCA-006 checkpoint-2 acceptance
  (`execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`;
  `D-PEC-97`), applied on 2026-09-26 and settled by the owner's checkpoint-3
  acceptance the same day
  (`execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-3_2026-09-26/`).
- It carries `D-PEC-90` operational reliance, the read-only `agent` access
  class, PEC-ORI-007, PEC-API-006, PEC-API-007 and the standing §12
  reliance-advertisement gate.

Earlier versions: v2.3 (SCA-005, `D-PEC-92`), v2.0 `D-PEC-58` (2026-07-24),
v2.1 `D-PEC-61`, exact PEC-K-03/-11 rows `D-PEC-67`, v2.2 `D-PEC-68`.
`projects/pec/AGENTS.md` carries the SCA-006 instruction tranche
`PEC-SCA006-OPERATIONAL-RELIANCE-20260926`.

**Implementation:** the first bounded P1 slice is reviewed and exact-byte
accepted under `D-PEC-74` O-A: the DEL-08-02 version-1 API JSON Schema,
standard-library additive compatibility tests/fixtures, and exact registered-
check profile. DEL-08-02 is `CHECKING`. D-PEC-77 later accepted the exact
DEL-01-05 enforcement inventory, confirmed AC-010 and AC-011 G-A, and advanced
DEL-01-05 to `CHECKING`; the 2026-09-07 `D-PEC-84` L ruling then reversed
DEL-01-05 `CHECKING → IN_PROGRESS` for the bounded scanner repair completed
under `D-PEC-84` S-A (Receipts 174–175). That reversal accepts no repaired
artifact; DEL-01-05 is `IN_PROGRESS`. **D-PEC-75 remains ruled O-A for
DEL-01-06.** Its accepted revision-1.4 production contract is SHA-256
`5fdcfd96834509e32a4df1fc001932fe7a0c5d4c5d96becb9acca0be3c4a2fa8`.
The current SELF_CHECK snapshot
`execution/_Evaluation/Reviews/REV_DEL-01-06_2026-08-04_1113/` records
AC-001 through AC-006 `PASS`, RF-001 `RESOLVED` with exact VER-005 evidence,
and RF-002 `REVISE / RESOLVED`: the accepted successor maps SOW-077 and SOW-094
to DEL-01-06 and records OI-003 resolved by D-PEC-78 O-A. DEL-01-06 remains
`INITIALIZED` under HOLD; no product/source artifact, next P1 node, release, or
professional reliance is authorized. D-T0-27 remains `ADOPTED / READ_ONLY`
through PR #459 merge `d9dc65804a0719fdf869af1ef60d53dc8cb0a895`; D-PEC-76
creates no duplicate adoption. Decomposition revision 1.6 is the accepted
current basis after `SCA-006` (checkpoint 3 accepted 2026-09-26); revision 1.5
after `SCA-005` and revision 1.4 after `SCA-004` preceded it. PROJECT_SETUP has completed the 64-context,
64-reference, and DEL-01-06 SOW-077-anchor subset; its closure handoff is
`execution/_Coordination/PROJECT_SETUP_SCA004_METADATA_ALIGNMENT_2026-08-03/HANDOFF_STATE.md`.
The nine TM-PEC-023 objective blanks are carried into SCA-005 intake as
candidate MODIFY actions (`D-PEC-86` §3 I-3). The owner selected them on
2026-09-24 (SCA-005 Decision_Log rows `SCA005-A1-TM` and `SCA005-A1-CMUX`;
`execution/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-1_AMENDMENT-1_2026-09-24/`):
six rows map to objectives, rows 4, 6 and 7 are moot because their
deliverables retire, and cmux (SOW-037, DEL-07-04) is added to the deferred,
out-of-scope items. SOW-033 is mapped to OBJ-003 by amendment 2
(`checkpoint_snapshots/SCA-005_GROUP-1_AMENDMENT-2_2026-09-24/`), so no
in-scope item remains without an objective once SCA-005 applies. The objective fields and the SOW-037 / DEL-07-04 status
changed when SCA-005 applied (2026-09-25): SOW-037 is `OUT` and DEL-07-04
is `RETIRED`. Nothing in the PRD is an
implementation mandate; each tranche needs its own owner-ruled packet.

**First store/guard slice:** `D-PEC-85` P-A (ruled 2026-09-08) produced the
first P1 store lifecycle and content-minimal guard slice for PKG-01 /
DEL-01-03 (Receipt 177). DEL-01-03 is `IN_PROGRESS`; no artifact fitness
acceptance, `CHECKING`, issuance, or release follows from that slice. Under
`D-PEC-86` §3 I-4 its three read-only evidence inquiries DEL-01-03-REM-001..003
produced reports under
`execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/REMAINING_EVIDENCE_DEL-01-03-REM-00{1,2,3}/`,
each with an independent verifier verdict of PASS
(`execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/C1_DEL0103_INQUIRIES.md`).
Their obligations O-1-1..O-1-10, O-2-1..O-2-8 and O-3-1..O-3-14, including
O-2-2 (the guard does not bound path length or line structure), were triaged
on 2026-09-24 and the owner ruled `D-PEC-87` the same day
(`execution/_Coordination/_DECISIONS/D-PEC-87_RULING_2026-09-24.md`): C-A
opens one correction slice on seven existing files (R1–R8, X-1); L-1a
authorizes WORKING_ITEMS to tick the three REM rows, independently of the
slice's completion; L-2a lands the corrected bytes and then reviews them. The owner reserves any CHECKING declaration for DEL-01-03 to
their own initiative; it is not an owner gate agents raise, and it holds no
other work. The C-A slice merged on 2026-09-24 (PR #893, `0517e0752`;
evidence under DEL-01-03 `_run_records/P1_STORE_GUARD_02/`, independent
verifier PASS after three cycles): O-2-2 is closed for exact-string paths
and the three REM rows are ticked; DEL-01-03 stays `IN_PROGRESS`. The slice
found one wider residual that R1 does not cover: a caller that passes a
`str` subclass can still place arbitrary text in the store, a channel present
since `D-PEC-85` and documented in `v2/docs/STORE_LIFECYCLE_AND_GUARD.md`.
Its closure, with three port-error gaps (two routed by the slice, one found
in preparation) and the echo of invalid identifiers, was proposed as
`D-PEC-89`, which the owner ruled A on 2026-09-24
(`execution/_Coordination/_DECISIONS/D-PEC-89_RULING_2026-09-24.md`). That
slice merged on 2026-09-25 (PR #897, `e8562c068`; evidence under DEL-01-03
`_run_records/P1_STORE_GUARD_03/`, independent verifier PASS in one cycle):
the guard now accepts only exact `str`/`tuple` caller values, rejections name
positions instead of echoing input, and the three port-error gaps are closed.
The one case left open is outside the stated threat boundary. DEL-01-03 stays
`IN_PROGRESS`. The L-2a review of the corrected bytes then ran (2026-09-25,
`execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/L2A_REVIEW_DEL-01-03.md`)
and found defects: a COUNT value longer than the interpreter's integer-string
limit makes the guard raise an unlocated error and lose the batch (F-1,
major), and the documentation does not state that deliberately encoded
content can pass through admitted field classes (F-2, minor), with smaller
items. The five registered checks pass. The owner ruled the repairs as
`D-PEC-91` A-53 on 2026-09-25: COUNT accepts only an exact integer from 0 to
`2**53 - 1` (the range JSON consumers read exactly), anything else becomes a
located rejection, plus a read-only-checkout test and documentation of the
encoding residual. That slice merged on 2026-09-25 (PR #903, `97344617f`;
evidence under DEL-01-03 `_run_records/P1_STORE_GUARD_04/`, independent
verifier PASS in one cycle). DEL-01-03 stays `IN_PROGRESS`. Carried residuals:
one sentence in `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` (lines 122–123) is broader than the new bound and needs a later
granted edit; the read-only-checkout test runs only where directory
permissions are enforced; hosted CI still runs no v2 Python check.

**Lifecycle census** (recounted 2026-09-26 from the 66 deliverable
`_STATUS.md` files, after SCA-005's retirements, the `D-PEC-93` setup of
DEL-02-08 and DEL-02-09, and their `D-PEC-98` add-on S step to
`INITIALIZED`): 28 `OPEN` / 28 `INITIALIZED` / 4 `CHECKING`
(DEL-00-01, DEL-00-03, DEL-08-02, DEL-10-01) / 2 `IN_PROGRESS` (DEL-01-03,
DEL-01-05) / 4 `RETIRED` (DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05). No
deliverable is `ISSUED`.

**Loop:** PEC runs the shared development loop under `D-PEC-94` (2026-09-25):
the evergreen `loop/LOOP_INIT.md`, steering-selected undertakings, work graphs
under `execution/_Coordination/WorkGraphs/`, one central receipt per
undertaking and terse deliverable `MEMORY.md` rows; `loop/LOOP_RECEIPTS.md` is
historical, closed by Receipt 197. *Historical:* `D-PEC-80` A–D (ruled
2026-09-05) made `projects/pec/loop/` the loop home, adopted the run-based PR
boundary and retired the workplan overlay, with work selected from deliverable
`_STATUS.md` `## Remaining` (that selection is replaced under `D-PEC-94`.
Since SCA-006 amendment 1, PEC adds no new Remaining sections or entries and
no feed profile reads them. The owner opened the retirement undertaking
`HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT` on 2026-09-26 and ruled its
retirement packet `D-PEC-99` A the same day. The `D-PEC-99` act removed all
57 sections: each item was closed on record or moved verbatim, with its gate,
into the exhibit `execution/_Coordination/_DECISIONS/D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md`,
and deliverable `_STATUS.md` files now carry lifecycle and history only), and `plans/workplans/` is history only. `D-PEC-81` calibrated and `D-PEC-82`
reported the Remaining concordance; `D-PEC-83` R-A/A-A applied the 57
ordinary Remaining carriers (Receipt 174), with the frozen DEL-01-05 carrier
not applied. PEC adopted the shared 2026-09-22 development-loop method on
2026-09-25 under `D-PEC-94`, exercising `D-PEC-86` §3 I-7.

**Scope change SCA-005 (closed for scope change only, 2026-09-25):**
opened at Gate 1 on 2026-09-23 under
`D-PEC-86` (owner direction of record, §1) to rebaseline PEC's feed model on
the shared App/Piping development-loop file shapes and the A2 Runtime
topology. Its checkpoint-group-1 package is
`execution/_ScopeChange/SCA-005_2026-09-23_2139/`: `Impact_Assessment.md`
SHA-256 `0bcbe9bdced43fa887a859497b3edd197242a0eea8fa3a41fab7147b358239bf`
and 76 PROPOSED actions in `Amendment_Actions.csv`. The owner accepted
checkpoint group 1 on 2026-09-24 (verbatim in its `Decision_Log.md`; group-1
snapshot `execution/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-1_2026-09-24/`),
as HELP_HUMAN had asked, which HELP_HUMAN records as selecting the
resolution note's Section A options (interpretation in the group-1
`DECISION.md`); the owner accepted checkpoint 2 on 2026-09-25 (see What's next). The pre-change audit is
`execution/_Evaluation/DecompCoverage/COV_SCA005_PRECHANGE_2026-09-23_2139/`
(`WARNINGS`: 0 blockers / 3 warnings). The design note
`execution/_Coordination/SCA-005_PREP_2026-09-23/FEED_MODEL_V2_DESIGN_NOTE.md`
recommended feed model O-B2 with presence option P-β; both were selected at
checkpoint 1. The owner accepted checkpoint 2 (exact amendment and propagation
plan) and checkpoint 3 (audited poststate) on 2026-09-25; SCA-005 is closed for
scope change only. `_ScopeChange/_LATEST.md` named it until SCA-006's
checkpoint-3 acceptance (2026-09-26) and now names SCA-006. The `D-PEC-79` hunks
are applied as part of PRD v2.3.

On 2026-09-24 HELP_HUMAN answered the checkpoint-1 question set from the accepted sources in `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/CHECKPOINT1_RESOLUTION_NOTE.md`: every Q1–Q10 and manager item resolves to one option by citation, leaving the owner CP1-A/CP1-B acceptance (given 2026-09-24) and the TM-PEC-023 row selections (nine rows reduced to seven live choices, still the owner's at checkpoint 2). The DEL-01-03 obligations were triaged the same way (15 settled, 13 folded into eight repairs proposed as D-PEC-87, 4 reduced to two lifecycle choices).

**Task Management** (`execution/_Coordination/_TaskManagement/`): the live
register holds 9 rows (8 `OPEN`, 1 `DEFERRED`) and the archive 16 `CLOSED`
rows. The 2026-09-23 notice triage (`NOTICE_TRIAGE_2026-09-23.md`) added no
rows. TM-PEC-022 stays `DEFERRED`. TM-PEC-023 was closed
`RESOLVED_BY_DECISION` on the owner's confirmation (`D-PEC-95`, 2026-09-25)
and archived by the PR #924 act; its selections are applied in the accepted
revision 1.5 registers.

**Historical — superseding owner ruling, 2026-08-03 (state as of that
date):** TM-PEC-023 now proceeds through a
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
*Later state:* the 2026-08-09 currency-repair closeout completed the SOW/SPEC
currency lane and left SCA-004 derivative state incomplete only for
TM-PEC-023 (`execution/_Coordination/PEC_CURRENCY_REPAIR_CLOSEOUT_2026-08-09/HANDOFF_STATE.md`);
TM-PEC-011, TM-PEC-013 and TM-PEC-014 are archived `CLOSED /
RESOLVED_WITH_CHANGE` in `_TaskManagement/REGISTER_CLOSED.csv`; TM-PEC-023 is
carried into SCA-005 intake as described above, and was closed
`RESOLVED_BY_DECISION` on 2026-09-25 under `D-PEC-95`.

**The old application** (v0.4-baseline prototype: `core/`, `server/`, `web/`,
`agent-sidecar/`, `tools/`, `fixtures/`) is a **frozen reference corpus** —
read and cite only, no further feature work, retired product docs under
`docs/.archive/`. Source-tree archival is a future packet after Phase 2
(PRD v2 §13). Historical run instructions:
`docs/.archive/README_v0.4_prototype.md`. The corpus and fences F-PEC-1..4
are unchanged; P1 source lives under `projects/pec/v2/`, from the slices
granted by `D-PEC-74`, `D-PEC-75`, `D-PEC-77`, `D-PEC-84` S-A and `D-PEC-85`
P-A.

## What's next (owner gates, in order)

Current owner gates (2026-09-26; none is accepted or inferred here):

- **SCA-005 follow-on work (each separately gated):** SCA-005 closed for
  scope change only on 2026-09-25
  (`execution/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-3_2026-09-25/`).
  Done: DEL-02-08/09 preparation with the dependency rerun and a re-audit
  (`D-PEC-93` A, merged 2026-09-25 as PR #914: registers 0 errors / 0
  warnings, 111 dependency edges with no cycles; re-audit
  `execution/_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_2026-09-25_1606/`
  0 blockers; `_Evaluation/DecompCoverage/_LATEST.md` named it until the
  SCA-006 checkpoint-3 acceptance moved it to
  `COV_SCA006_POSTCHANGE_2026-09-26_0051`).
  Done under `D-PEC-95` P + R (act merged 2026-09-25 as PR #924,
  `abfd0897b`; run root
  `execution/_Coordination/CURRENCY_REV15_D95_2026-09-25/`):
  - `_Decomposition/_LATEST.md`, `_ScopeChange/_LATEST.md` and
    `_COORDINATION.md` were brought to the post-setup state (since
    superseded: both pointers name revision 1.6 and SCA-006);
  - all 66 contexts and 66 references name revision 1.5. Since the SCA-006
    application, three contexts (DEL-04-03, DEL-08-01, DEL-08-03) also carry
    the revision-1.6 successor clause;
  - the 19 stale dependency evidence quotes are refreshed, so all 111 active
    execution quotes are verbatim;
  - TM-PEC-023 is closed `RESOLVED_BY_DECISION` and archived.

  No re-audit ran, by owner ruling. SCA-006's post-change audit
  (`COV_SCA006_POSTCHANGE_2026-09-26_0051`) has since observed this state. The SCA-005 `Handoff_State.md` and
  `RUN_SUMMARY.md` stay unchanged at their current bytes, and
  `_COORDINATION.md` records them as superseded for current state.

  Open:
  - SOW currency (S1, S2, S4). Done: the first SOWs for DEL-02-08/09
    (`D-PEC-98` A + S + M, ruled 2026-09-26): both contracts written,
    re-pinned to revision 1.6, validated and independently verified, and
    both deliverables `INITIALIZED` (run root
    `execution/_Coordination/SOW_INIT_D98_2026-09-26/`); their `MEMORY.md`
    files come at the undertaking's closeout;
  - DEL-00-01/00-03 derivative review;
  - done: the loop registry source packet, `D-PEC-96`. The owner ruled revision 4
    (option A, PEC's row migrated to `shared-dev-loop`) on 2026-09-26, and its
    act merged the same day as PR #950
    (`execution/_Coordination/_DECISIONS/D-PEC-96_registry_schema_v2_feed_profiles_proposal_2026-09-25.md`);
  - P1 fixtures;
  - done: residual `projects/pec/AGENTS.md` corrections, applied in the
    SCA-006 instruction tranche and accepted with checkpoint 3;
  - the D-PEC-90 reliance amendment. This is scope change SCA-006. The
    owner accepted checkpoint 1 on 2026-09-25 (DQ a, ENV a, BUD a, GATE a,
    INS a, R-C excluded;
    `execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/`),
    and the owner accepted checkpoint 2 on 2026-09-25 (`D-PEC-97`;
    `execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`);
    checkpoint 3 was applied and audited on 2026-09-26, on the pinned
    scope-change edition (audit `WARNINGS`: 0 blockers;
    `execution/_Evaluation/DecompCoverage/COV_SCA006_POSTCHANGE_2026-09-26_0051/`).
    The owner approved the `AGENTS.md` Remaining-sections paragraph
    ("approve hunk") and accepted checkpoint 3 on 2026-09-26
    (`execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-3_2026-09-26/`).
    SCA-006 is closed for scope change only: the pointers and the audit
    pointer name revision 1.6, SCA-006 and its post-change audit. Its Lane B
    items (the DEL-08-06 and DEL-10-13 folders, dependency work, SOW currency,
    the DEL-00-03 SPEC premise, the tier-0 profile entry, the revision-1.6
    re-pin and the API schema fields) and the correction of the stale
    `remaining-loop` design text stay open, each under its own packet.
  - Retiring the 57 `## Remaining` sections, as App and Piping did: the owner
    opened it on 2026-09-26 as undertaking
    `HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT`. Its census and decision
    account merged as PR #951, and the owner ruled the retirement packet
    `D-PEC-99` A on 2026-09-26. Done: the act removed all 57 sections and
    replaced the `AGENTS.md` paragraph (run root
    `execution/_Coordination/REMAINING_RETIREMENT_D-PEC-99_2026-09-26/`).
    Still open from it: the 71 unselected evidence inquiries stay in the
    exhibit until steering selects one, and the 12 Scope of Work
    carry-forwards are absorbed by the S1, S2 and S4 SOW-currency packets.

  These are organized in the work graph
  `execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`.
- **Other lifecycle and P1 acts:** DEL-01-05 repaired-artifact acceptance,
  DEL-01-06 Gate 5 (HOLD at `INITIALIZED`), DEL-08-02 short of `ISSUED`, and
  every later P1 node each need their own owner-ruled act.
- **Agent reliance on PEC data:** the owner ruled `D-PEC-90` R-A on
  2026-09-25: agents may act on PEC record-tier data as true as of the
  response's examined-through commit, within stated bounds, and authority
  stays file-native; agents may eventually query PEC directly through tool
  calls. Reliance begins at a PEC release whose gates prove parity and
  coverage, not now. The PRD and `projects/pec/AGENTS.md` text (PEC-K-03, §8, §9, §12) is
  amended by scope change SCA-006. The owner accepted its checkpoint 1 on
  2026-09-25 with a read-only `agent` access class for direct query, and its
  checkpoint 2, the exact PRD v2.4 text (`D-PEC-97`), the same day. The text
  was applied, and the owner accepted checkpoint 3, on 2026-09-26 (see
  above). Operational reliance still begins only at a release
  that passes the §12 gate. SCA-005's checkpoint 2 carried a note so DEL-04-01 and the §8
  refresh are not rebuilt around verify-before-rely.

Gate lineage (historical record; the current gates are listed above):

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
   P4 streams are historical phase orientation; live work is selected by the
   human's steering and carried in work graphs under `loop/LOOP_INIT.md`
   (`D-PEC-94`).

## Orient yourself (read-order)

1. `docs/PRD.md` — the adopted product definition (v2.3), including the
   invariants (PEC-K-01..11), modes ladder, and release strategy.
2. `projects/pec/loop/LOOP_INIT.md` — the evergreen development-loop
   procedure (`D-PEC-94`); `projects/pec/AGENTS.md` holds fences and authority
   rules. `projects/pec/plans/workplans/` is history only.
3. `execution/_Coordination/_DECISIONS/_REGISTER.md` — decision register
   (D-PEC-57/58 are the pivot and adoption rows; D-PEC-86 opened SCA-005;
   D-PEC-94 adopted the shared loop).
4. The current undertaking's work graph under
   `execution/_Coordination/WorkGraphs/` and its central receipt under
   `execution/_Coordination/AgentRuns/`; `projects/pec/loop/LOOP_RECEIPTS.md`
   is the historical ledger (closed at Receipt 197).

## Governance & agent harness

Project-local agent rules: `AGENTS.md` (rewritten 2026-07-24, `D-PEC-59`; loop, record and Runtime-boundary sections amended 2026-09-25 under `D-PEC-94`; the SCA-006 operational-reliance instruction tranche 2026-09-26; the Remaining paragraph replaced 2026-09-26 under `D-PEC-99`).
Decomposition session ruled and closed 2026-07-24 (`D-PEC-60`, Gates 1–7
accepted; `execution/_Decomposition/**` opened by its fence for the
canonical working package). Directed-bootstrap amendment `SCA-001` closed
2026-07-24 under `D-PEC-61`; objective-mapping amendment `SCA-002` closed
2026-07-25 under `D-PEC-64`; SCA-003 closed 2026-07-28; and SCA-004 closed
for scope change on 2026-08-03 with revision 1.4 as `current_basis` under
D-PEC-78 O-A. All four sessions' immutable evidence lives under
`execution/_ScopeChange/`. SCA-005 opened at Gate 1 on 2026-09-23 under
`D-PEC-86`; the owner accepted its checkpoint group 1 on 2026-09-24
(`checkpoint_snapshots/SCA-005_GROUP-1_2026-09-24/`, amended additively the same day by
`SCA-005_GROUP-1_AMENDMENT-1_2026-09-24/`); the owner accepted checkpoint 2 (`D-PEC-92`) and checkpoint 3 on 2026-09-25, closing SCA-005 for scope change only with revision 1.5 as `current_basis`.
`D-PEC-67` adopted exact pull-oriented / consumer-owned invariant rows; `D-PEC-68` reconciled the surrounding PRD;
SCA-003 propagated C3/C15 and direct mirrors into accepted decomposition
truth without changing topology, dependencies, lifecycle, or implementation.
`D-PEC-69` then reconciled the complete affected ScopeOfWork population;
`D-PEC-70` released the exceptional reliance hold. SCA-004 resolved OI-003
in decomposition truth, the metadata subset is current, and DEL-01-06 RF-002
is resolved by exact successor acceptance; the nine TM-PEC-023 objective
blanks now carry owner selections (SCA-005 amendment 1), applied in revision 1.5. P1
source work remains separately owner-gated and fenced by `F-PEC-1`.
Loop instruction surface: `loop/LOOP_INIT.md`, the shared development loop under `D-PEC-94` (loop home from `D-PEC-80`).
Domain-engine profile `_DomainEngines/profiles/pec.yaml` contains the exact
D-T0-27 O-A PEC v2 `ADOPTED / READ_ONLY` postimage and is validator `VALID`,
effective through PR #459 merge
`d9dc65804a0719fdf869af1ef60d53dc8cb0a895`; D-T0-28/D-T0-29 are effective
supporting amendments. The profile creates no invocation by itself. The
frozen v0.4 profile is preserved as historical preimage lineage.
Fences F-PEC-1..4 (`D-T0-15`) remain in force.
