---
amendment_id: SCA-005
doc_kind: scope_change.decision_log
decomp_variant: SOFTWARE
current_checkpoint_group: 2
status: checkpoint_1_accepted_checkpoint_2_preparation_authorized
---

# SCA-005 Decision Log

Only decisions that actually occurred are recorded as decided. Every other
row is `AWAITING_OWNER` or `NOT_STARTED`. Agent recommendations are not
rulings.

| DecisionRef | Checkpoint | Decision | Status | Authority |
|---|---|---|---|---|
| SCA005-G1 | Gate 1 intake | Open SCA-005 (SOFTWARE variant) under `chirality-root:bundled:workflow:scope-change` to rebaseline PEC's feed model | `OPENED BY OWNER DIRECTION` | Owner direction, 2026-09-23 (verbatim below); recorded in D-PEC-86 §1 |
| SCA005-CP1 | 1 | Confirm the parsed change set (`Amendment_Actions.csv`, SHA-256 `5c4ae0532eb65ea83d0529a9f6395da392ae2bf5b254cfb6b2de49e4fbff2be2`, 76 PROPOSED actions; Seq 72 dropped at checkpoint 2 under Q9; Seq 75 narrowed under Q10 (a): its §12 P1 (Q10 c) element dropped, R-04 control becomes Q10 (a)) and accept `Impact_Assessment.md` at SHA-256 `0bcbe9bdced43fa887a859497b3edd197242a0eea8fa3a41fab7147b358239bf`, with the resolution note's Section A as the selected options (HELP_HUMAN's reading of the act, recorded as interpretation in the group-1 `DECISION.md`) | `ACCEPTED` | Owner act, 2026-09-24 (verbatim below); group-1 snapshot `../checkpoint_snapshots/SCA-005_GROUP-1_2026-09-24/` |
| SCA005-CP1-Q1 | 1 | Feed model: **O-B2** (per-loop declared grammar in the PEC-owned registry) | `SELECTED VIA CP1-B` | Resolution note §A Q1: DEL-02-03 OUT-001; `adapter.yaml` header; D-PEC-78 O-A |
| SCA005-CP1-Q2 | 1 | `adapter.yaml` / SOW-017 / DEL-02-07: **(b)** parity-peer input only, DEL-02-07 re-purposed | `SELECTED VIA CP1-B` | Resolution note §A Q2 |
| SCA005-CP1-Q3 | 1 | Presence and streams under A2: **P-β** (deferred with the design note's three-part trigger) | `SELECTED VIA CP1-B` | Resolution note §A Q3 |
| SCA005-CP1-R | 1 | P-β deferral representation: **R1** (`OUT` + `**Deferred**` note; DEL-06-04 / DEL-07-02 / DEL-07-05 retired non-destructively at Gate 5) | `SELECTED VIA CP1-B` | Resolution note §A CP1-R: `ScopeLedger.csv` rows 82–85; scope-change contract |
| SCA005-CP1-Q4 | 1 | Orientation over graph node states: **(a)** READY/ACTIVE/BLOCKED with Git-derived terminal completion | `SELECTED VIA CP1-B` | Resolution note §A Q4: construct-local-work-graph §3–4 |
| SCA005-CP1-Q5 | 1 | External trials: **(a)** P1 pinned parser fixture suites only, three fixture classes | `SELECTED VIA CP1-B` | Resolution note §A Q5: PRD §12 P1 |
| SCA005-CP1-Q6 | 1 | A2 effects on PRD §16.2/16.6/16.8/16.9: **re-express as premise; each decision stays open** | `SELECTED VIA CP1-B` | Resolution note §A Q6: PRD §16 heading and closing line |
| SCA005-CP1-Q7 | 1 | Ref scope for in-flight graphs: **(b)** integration ref default, local refs opt-in and labelled | `SELECTED VIA CP1-B` | Resolution note §A Q7 (agent method choice) |
| SCA005-CP1-Q8 | 1 | PEC's own registry row: **(a)** declare `remaining-loop` now | `SELECTED VIA CP1-B` | Resolution note §A Q8: D-PEC-86 I-7; `loop/LOOP_INIT.md` §4 |
| SCA005-CP1-Q9 | 1 | Step-0 baseline loops: **no change to SOW-058; Seq 72 dropped** (Impact Assessment §12.4 option (b); neither design-note (a) nor manager (c)) | `SELECTED VIA CP1-B` | Resolution note §A Q9: DEL-10-01 `STEP0_COST_BASELINE_METHOD.md` §§1–2; PRD §11 |
| SCA005-CP1-Q10 | 1 | P1 parity comparable set: **(a)** self-check facts plus explained census absence; no PRD exit-test change | `SELECTED VIA CP1-B` | Resolution note §A Q10: PRD §12 P1 row; `harness.py` `OBSERVABLE_PROJECTS` |
| SCA005-CP1-D79 | 1 | D-PEC-79 path: **(b)** carry the six hunks into one successor v2.3 candidate; adopted bytes preserved as historical exact input | `SELECTED VIA CP1-B` | Resolution note §A CP1-D79; D-PEC-79 handoff and ruling; exact gate at checkpoint 2/3 |
| SCA005-CP1-TM | 1 | TM-PEC-023 nine rows carried as candidate MODIFYs, no option selected; Rows 4 and 7 (DEL-07-02, DEL-07-05) moot under R1; seven live rows selected by the owner at checkpoint 2 via mechanic M1 | `CONFIRMED` | Owner act 2026-09-24 (CP1); owner ruling 2026-08-03 reserves every selection |
| SCA005-CP1-X | 1 | New feed items: **ADD SOW-095/096 + DEL-02-08/09; central receipts in SOW-013 / DEL-02-03** | `SELECTED VIA CP1-B` | Resolution note §A CP1-X: decomposition standard artifact-kind granularity |
| SCA005-CP1-N | 1 | **Retain** IDs, names and paths of DEL-02-03/04/06/07; label drift recorded per MODIFY | `SELECTED VIA CP1-B` | Resolution note §A CP1-N: `ALLOW_RENUMBERING = false` |
| SCA005-CP1-V | 1 | Strict, versioned registry schema v2 is **within D-PEC-78 O-A; no supersession** | `SELECTED VIA CP1-B` | Resolution note §A CP1-V: D-PEC-78 `PACKET.md` §4.2 (ruled option O-A) |
| SCA005-CP1-O | 1 | Objectives for SOW-095/096 and DEL-02-08/09: **OBJ-001;OBJ-002** | `SELECTED VIA CP1-B` | Resolution note §A CP1-O: `Deliverables.csv` DEL-02-01..07 |
| SCA005-A1-TM | 1 (amendment 1) | TM-PEC-023 selections: row 1 DEL-00-02 `OBJ-003`; row 2 DEL-03-05 `OBJ-001`; row 3 DEL-05-01 `OBJ-004`; row 5 DEL-07-03 `OBJ-003`; row 8 DEL-08-05 `OBJ-001;OBJ-003`; row 9 DEL-10-08 `OBJ-001` (supersedes DL-14's objective-free rationale); rows 4, 6, 7 moot (retired); no typed non-mapping, so the surface's mechanic and objective-side-table rulings are moot | `SELECTED BY OWNER` | Owner acts 2026-09-24 (verbatim below); `../checkpoint_snapshots/SCA-005_GROUP-1_AMENDMENT-1_2026-09-24/DECISION.md` |
| SCA005-A1-CMUX | 1 (amendment 1) | Add to intake: Seq 77 SOW-037 IN to OUT `**Deferred**`; Seq 78 retire DEL-07-04 under R1; Seq 43 PKG-07 charter narrowed; Seq 68 dropped (moot); Seq 75 extended so PEC-STR-003 and §12 P4 record cmux as deferred | `DIRECTED BY OWNER` | Owner act 2026-09-24 (verbatim below); `../checkpoint_snapshots/SCA-005_GROUP-1_AMENDMENT-1_2026-09-24/Amendment_Actions_Addendum.csv` |
| SCA005-A2-SOW033 | 1 (amendment 2) | Add to intake: Seq 79 SOW-033 `ObjectiveIDs` to `OBJ-003` (DEL-07-01 unchanged at `OBJ-003`); no IN scope item remains without an objective after application | `DIRECTED BY OWNER` | Owner act 2026-09-24 (verbatim below); `../checkpoint_snapshots/SCA-005_GROUP-1_AMENDMENT-2_2026-09-24/DECISION.md` |
| SCA005-CP2 | 2 | Exact amendment and propagation plan (incl. PRD v2.3 successor candidate, `Supersession_Delta.csv`, carrying the owner-selected TM-PEC-023 values and amendments 1 and 2) | `PREPARATION AUTHORIZED / NOT_STARTED` | SCA005-CP1 acceptance 2026-09-24; acceptance itself is a later owner act |
| SCA005-CP3 | 3 | Audited poststate acceptance, pointer moves | `NOT_STARTED` | requires SCA005-CP2 acceptance |

## SCA005-G1 — owner direction of record (verbatim)

Owner, 2026-09-23 (as transcribed in D-PEC-86 §1):

> Proceed with SCA-005 and what follows in your recommendations.  You are
> Agent 0, so consider effective delegation to your Type 1 and Type 2
> instances.  Use `opus-5.5` models on `high` reasoning for all subagents.  You
> can continue working within your capacity of HELP_HUMAN, anticipating my
> needs and those of the agents under you.

D-PEC-86 §3 I-1 interprets this (Agent 0 interpretation, not owner text) as
opening SCA-005 at Gate 1 and authorizing preparation of the complete
checkpoint-group-1 package, with checkpoint groups 1–3 remaining owner
acceptances.

## SCA005-CP1 — owner acceptance of record (verbatim)

Owner, 2026-09-24, in the session chat, after HELP_HUMAN asked for acceptance
"at Impact Assessment hash `0bcbe9bd…39bf` with the note's resolutions as the
selected options":

> I accept checkpoint 1 and the Impact Assessment.  Explain to me the other decisions I face with the context I need.

HELP_HUMAN's interpretation, the accepted manifest and the boundary of the
act are recorded in `../checkpoint_snapshots/SCA-005_GROUP-1_2026-09-24/`
(`DECISION.md`, `ACCEPTED_MANIFEST.csv`, `Handoff_State.md`). The acceptance
authorizes checkpoint-2 preparation only.

## SCA005-A1 — owner acts of record (verbatim)

Owner, 2026-09-24, after HELP_HUMAN gave one read per TM-PEC-023 row:

> Row 6 should not move with row 5 because row 6 is optional and I do not want it as an objective.  I don't need cmux compatibility anytime soon (no plans for it).  Besides that, I reviewed and accept your  read for each mapping.

Owner, 2026-09-24, after HELP_HUMAN offered to mark cmux deferred and out of scope:

> yes add cmux to what's been deferred and out of scope.

HELP_HUMAN's per-row interpretation, the addendum actions and the boundary
are in `../checkpoint_snapshots/SCA-005_GROUP-1_AMENDMENT-1_2026-09-24/`. The accepted group-1 snapshot is unchanged.

## SCA005-A2 — owner act of record (verbatim)

Owner, 2026-09-24, after HELP_HUMAN asked whether to map SOW-033 to OBJ-003 and whether to keep the Status page and README current:

> yes map SOW-033 to OBJ-003 and yes maintain the Status page and README.

The first clause is amendment 2 (`../checkpoint_snapshots/SCA-005_GROUP-1_AMENDMENT-2_2026-09-24/`); the second is `D-PEC-88` and does not concern SCA-005.

## Non-decisions recorded for clarity

- The TM-PEC-023 selections (SCA005-A1-TM) are recorded but not applied: every objective field stays byte-identical until checkpoint 2/3 application.
- The D-PEC-79 postimage has not been applied and no PRD byte has changed.
- D-PEC-87 is not ruled by this acceptance.
- No decomposition, decomposition register, SOW, `_CONTEXT.md`, `_STATUS.md`,
  `v2/**` or foreign surface has changed; `_LATEST.md` still names SCA-004
  (the amendment-qualified `../SCA-005_GROUP-1_AUTHORIZED.md` pointer is new); `Amendment_Actions.csv` and
  `Impact_Assessment.md` in this snapshot are byte-unchanged from the
  accepted hashes.

Companion (2026-09-24): `../../_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/CHECKPOINT1_RESOLUTION_NOTE.md` records, per question, the accepted source that decided it. Its Section A became the selected options through the CP1-B acceptance above; its Section B TM-PEC-023 rows remain the owner's at checkpoint 2.
