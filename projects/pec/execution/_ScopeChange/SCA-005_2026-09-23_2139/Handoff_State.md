---
amendment_id: SCA-005
doc_kind: scope_change.handoff_state
decomp_variant: SOFTWARE
checkpoint_group: 3
created: 2026-09-23
status: checkpoint_3_prepared_awaiting_owner
---

# SCA-005 Checkpoint-group-3 Handoff State

This file accumulates the SCA-005 handoff state across all three checkpoint
groups. The sections from §Position to the eighth amendment describe the
checkpoint-1 and checkpoint-2 states as they were recorded; the current state
is §"Checkpoint-group-3 handoff state" at the end.

## Position

| Field | Value |
|---|---|
| Snapshot | `projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/` — interim checkpoint-1 package; **not** an active snapshot |
| Stage reached | checkpoint group 1 prepared (method parts A and B); owner acceptance **not** given |
| Gate 1 | opened by owner direction 2026-09-23 (D-PEC-86 §1; `Decision_Log.md` SCA005-G1) |
| Accepted decomposition basis | `SOFTWARE_DECOMP.md` revision 1.4 `current_basis`, SHA-256 `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81` (unchanged by this run) |
| Accepted predecessor | `_ScopeChange/SCA-004_2026-08-02_2325/` (pointer posture for a later checkpoint 3: `ACCEPTED_PREDECESSOR`) |
| Pre-change baseline | `_Evaluation/DecompCoverage/COV_SCA005_PRECHANGE_2026-09-23_2139/`; `Pre_Change_Coverage.json` is a byte copy of its `coverage_summary.json` |
| Impact Assessment for owner acceptance | `Impact_Assessment.md` SHA-256 `0bcbe9bdced43fa887a859497b3edd197242a0eea8fa3a41fab7147b358239bf` |
| Group-1 decision snapshot | not created (follows owner acceptance, under `_ScopeChange/checkpoint_snapshots/`) |
| Next owning actor | Owner (checkpoint-1 question set, `Impact_Assessment.md` §15), then WORKING_ITEMS (scope-change) for checkpoint-2 preparation from the accepted group-1 snapshot |

## Required state fields

| Field | Value | Note |
|---|---|---|
| `DecompositionTruthState` | `UNCHANGED_REVISION_1_4` | value set by brief B1; in contract terms no amendment has begun, so neither `INCOMPLETE` (in progress) nor `COMPLETE` describes it |
| `DerivativePackageState` | `INCOMPLETE` | nothing applied; every SCA-005 derivative obligation is future work (`Impact_Assessment.md` §7); SCA-004's own derivative state is governed by its handoff |
| `ContentRemediationState` | `NOT_REQUIRED` | SOFTWARE variant; no KTY lane |
| `DownstreamRerunState` | `FROZEN` | no downstream rerun authorized |
| `MetadataAlignmentState` | `NOT_STARTED` | for SCA-005 |
| `AuditState` | `WARNINGS` | pre-change baseline only: 0 blockers / 3 warnings / 69 info; post-change audit `NOT_RUN` |
| `ReadyForNextPhase` | `NO` | |

`Supersession_Delta.csv` is a checkpoint-2 artifact: none exists in this
checkpoint-1 package, so all 76 action rows carry
`SupersessionBindingPresent = NO`; the nine descriptions marked `SB-PENDING`
name the candidate bindings listed in `Impact_Assessment.md` §8.3, which are
finalized (or dropped if the PRD successor lands first) at checkpoint 2.
| Closure verdict | none — checkpoint 1 open | neither `CLOSED_FOR_SCOPE_CHANGE_ONLY` nor `OPEN_PENDING_DERIVATIVE_CLOSURE` applies before application |

## Snapshot file hashes (this file excluded)

| File | SHA-256 |
|---|---|
| `Brief.md` | `aaf2821bb99deb4ff8b640f5e8584338ebd5fc2d95c5c00dd1e2bd136ac43d50` |
| `Impact_Assessment.md` | `0bcbe9bdced43fa887a859497b3edd197242a0eea8fa3a41fab7147b358239bf` |
| `Amendment_Actions.csv` (PROPOSED) | `5c4ae0532eb65ea83d0529a9f6395da392ae2bf5b254cfb6b2de49e4fbff2be2` |
| `Pre_Change_Coverage.json` | `61163c96924e6dfb1f3fa6d1449b523c7280e808c92005cc77d64096858b5d9f` |
| `Decision_Log.md` | `85676c5326da5446e62698c70760a2c55eea011bc4e2810727e3509f393f4d7b` (after the checkpoint-3 package row, 2026-09-25; `db1a3518bf1c70e9d69f522846ce303172d8698c42bba6999b58ab667d7a56ac` after the checkpoint-2 acceptance, 2026-09-25; `7dcbc51dd30c66bb273e3528e8675e9adba317d974ec63a438ff816d15af371b` after the checkpoint-2 package row, 2026-09-25; `d8aced8d7cf196401525dd2ed5db0ad315ca042e0772d716bf453f949d1b8a11` after the D-PEC-90 note; after amendment 2 `6695e0344a247b3db9b22975781c8c3899b4873a9a396b9745aab4a0fcf50924`; after amendment 1 `321be32d0ca51377dc750938dfe9d9e66204d4da4a128af273c1804e682e96b4`; post-acceptance value `8508318a95c830a4cf8c7d665ab516f8ea376559e126c581fb8a9c5e6f6f7075`; pre-acceptance value `55551f5628608f1a6475f832b70721f7d055adb18ab0b55d80b7e7e3326b658f` is bound in the group-1 `ACCEPTED_MANIFEST.csv`) |

## Pre-change audit snapshot hashes (written by the TASK child)

| File | SHA-256 |
|---|---|
| `Brief.md` | `21e85243cb4a6e7da873a804ff676108247978c5febfc426fd46590ece396719` |
| `Decision_Log.md` | `55bf32404ec44b35b47eb8c3e1f1e333e954dcd9ecbfb9f590674678402d1270` |
| `coverage_summary.json` | `61163c96924e6dfb1f3fa6d1449b523c7280e808c92005cc77d64096858b5d9f` |
| `Decomp_Coverage_Report.md` | `08e26c2f3fe71b129d23f71835fe6333054210b403fc2e7c475a294fd80d85f7` |
| `Decomp_Coverage_IssueLog.csv` | `3bbebf6e6ecc668b27c3502997bfe159aa6b3072ed1d0d988f70dade49855f6d` |
| `Decomp_Coverage_Matrix.csv` | `96a3d7bf51f63c79c7ec8851b8edba4e5d8d3738c218a3a46addca81d6f8f373` |
| `QA_Report.md` | `bd85ac1ca0af8bf65a77d65d74650df3174d9f5ca3b978021f794b71e421d3ee` |
| `RUN_SUMMARY.md` | `5805ae4cc4436e898bf5d4d11df8541753925a616dde5e3be57ad259d18f2c6e` |

## Delegation record

| Child | Mechanism | Parent | Basis supplied | Write scope | Enforcement limits | Return |
|---|---|---|---|---|---|---|
| audit-decomp pre-change baseline (TASK, Type 2) | Claude Code Agent tool, `subagent_type: general-purpose`, `model: opus` (host maps to claude-opus-5-5); background | this WORKING_ITEMS instance (itself dispatched by HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`) | `workflows/audit-decomp/*`, SCA-004 prechange form, revision 1.4 hashes, lifecycle-census caution | exactly `_Evaluation/DecompCoverage/COV_SCA005_PRECHANGE_2026-09-23_2139/` | high reasoning effort and "never use the Agent tool" were instruction-asserted, not tool-enforced; write scope instruction-asserted (verified afterwards by `git status`) | 8 files; WARNINGS 0/3/69; lifecycle 26 INITIALIZED / 32 OPEN / 4 CHECKING / 2 IN_PROGRESS; contracts 32/32/0; artifact presence 4.6875 %; `_LATEST.md` untouched (its decision D-15) |

No other child was dispatched; the manager drafted every other file itself.

## Commands (cwd = REPO_ROOT `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5`; shell zsh; interpreter `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`, Python 3.13.7)

| # | Time (local; approximate except steps 12 and 17, stamped 21:42:01 and 21:57:54 -0600) | Command | Exit | Result |
|---:|---|---|---:|---|
| 1 | 21:39 | `date '+%Y-%m-%d_%H%M'` | 0 | `2026-09-23_2139` |
| 2 | 21:39 | `mkdir -p projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139` | 0 | folder created (prior listing: SCA-001..SCA-004 + `_LATEST.md`) |
| 3 | 21:39 | `mkdir -p projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA005_PRECHANGE_2026-09-23_2139` | 0 | empty folder handed to the child |
| 4 | 21:39 | `git rev-parse HEAD` | 0 | `d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b` |
| 5 | 21:39 | `shasum -a 256 projects/pec/execution/_Decomposition/* projects/pec/docs/PRD.md` | 0 | decomposition, ScopeLedger, Deliverables and PRD equal the brief and `SUPPLIED_BASIS.json` values |
| 6 | 21:40 | `bash tools/query/scan_next_amendment_id.sh projects/pec/execution/_ScopeChange/` | 2 | script is zsh (`#!/bin/zsh`); bash syntax error |
| 7 | 21:40 | `zsh tools/query/scan_next_amendment_id.sh projects/pec/execution/_ScopeChange/` | 0 | `SCA-006` (run after step 2 created SCA-005's folder; SCA-005 was the next free ID before it) |
| 8 | 21:40 | `python3 tools/validation/validate_scope_change_packet.py --help` | 0 | validates a "PKG-00 Scope Change Consumable Packet" (ten `Packet_*`/`SCOPE_CHANGE_INIT.md`/CSV files) |
| 9 | 21:40 | `python3 projects/pec/execution/_Scripts/pec_reliance_hold.py --help` | 0 | operations listed |
| 10 | 21:41 | `python3 projects/pec/execution/_Scripts/pec_reliance_hold.py --register projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md --operation exact-correction-preparation` | 0 | `{"operation": "exact-correction-preparation", "status": "ALLOW"}` |
| 11 | 21:42 | same command for targets `…/ScopeLedger.csv`, `…/Deliverables.csv`, `projects/pec/docs/PRD.md`, `projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139` | 0 ×4 | `ALLOW` ×4 (register `f877d931…1cbc` holds a header and no rows) |
| 12 | 21:42 | `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` (before) | 0 | 64 registers, 255 dependency rows (136 ANCHOR / 119 EXECUTION), 0 errors, 0 warnings |
| 13 | 21:40–21:49 | child: `pec_reliance_hold.py … --target …/SOFTWARE_DECOMP.md --operation consume`; `validate_decomposition_registers.py … --strict`; `shasum -a 256` | 0 / 0 / 0 | as reported by the child (its `QA_Report.md`) |
| 14 | 21:52 | `python3 <scratchpad>/gen_actions.py projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/Amendment_Actions.csv` | 0 | 76 rows (script SHA-256 `7481af5b381e0990ffdc375e2a9fd5a897e50c99f89bbabb65d43533113dd766`, session scratchpad only) |
| 15 | 21:53 | `python3 <scratchpad>/validate_actions.py . projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/Amendment_Actions.csv` | 0 | contract columns and enums OK; 76/76 PASS; ADD 8 / MODIFY 65 / REMOVE 3 (script SHA-256 `15daeac2480bfa381d36642c0e44d96960645906b6c9a6a987f7ff4aba0a9155`, session scratchpad only) |
| 16 | 21:53 | `cp …/COV_SCA005_PRECHANGE_2026-09-23_2139/coverage_summary.json …/SCA-005_2026-09-23_2139/Pre_Change_Coverage.json`; `cmp` | 0 / 0 | byte-identical; both `61163c96…5d9f` |
| 17 | 21:57 | `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` (after) | 0 | unchanged: 64 / 255 / 0 errors / 0 warnings |
| 18 | 21:57 | `python3 tools/validation/validate_scope_change_packet.py projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139` | 1 | FAIL: ten missing `Packet_*`-family files — the tool's PKG-00 consumable-packet schema does **not** fit a scope-change amendment snapshot; not applied further |
| 19 | 21:57 | `shasum -a 256 projects/pec/execution/_Decomposition/* projects/pec/docs/PRD.md projects/pec/execution/_ScopeChange/_LATEST.md projects/pec/execution/_Evaluation/DecompCoverage/_LATEST.md` | 0 | all unchanged (`_Decomposition/_LATEST.md` `7abf65e6…d7a3`; `_ScopeChange/_LATEST.md` `721a14dc…6280`; DecompCoverage `_LATEST.md` `0084d218…7432`) |
| 20 | 21:57 | `git status --porcelain`; `git diff --stat` | 0 | new: this snapshot and the COV folder; no tracked file changed by this run (see containment) |
| 21 | 21:58 | `shasum -a 256` of this snapshot's files and the two scripts | 0 | original hashes (superseded by the correction below) |
| 22 | 22:17 | `python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir <scratchpad>/depclosure` | 0 | `run_status COMPLETE`, `subject_status PASS`; 64 files / 255 rows (136 ANCHOR, 119 EXECUTION); 119 graph edges over 64 nodes; 0 SCCs; 0 bidirectional pairs; 0 orphans; 2 isolated; 1 hub; schema valid 64/64 |
| 23 | 22:18 | Python `csv` scan of all 64 `Dependencies.csv` for `DEL-06-04`/`DEL-07-02`/`DEL-07-05` in any cell; `grep` of surviving `_DEPENDENCIES.md` | 0 / 0 | only surviving dependant row: DEL-09-05 `DEP-09-05-005` → DEL-06-04 (EXECUTION/UPSTREAM/PREREQUISITE, ACTIVE); rows owned by retired registers: DEP-06-04-003..006, DEP-07-02-003/004, DEP-07-05-003/005 (8 EXECUTION); 8 surviving consumer mirrors name the retired DELs |
| 24 | 22:19 | in-place edit of `Amendment_Actions.csv` Seq 34/35/36/38 (Python `csv`); then `python3 <scratchpad>/validate_actions.py <REPO_ROOT> Amendment_Actions.csv` | 0 / 0 | Seq 38 DownstreamReruns gains `dependency-extract`; Seq 34–36/38 descriptions name the edges; 76/76 PASS, counts unchanged |
| 25 | 22:20 | in-place edit of `Impact_Assessment.md` §4 (Seq 34–36, 38), §5, §6, §7.2, §8.1, §12.2; `sed` hash replacement in `Decision_Log.md` and this file; `shasum -a 256` | 0 | table below |

Reads used `cat`/`sed`/`grep`/`awk` and the Read tool; they changed nothing.

## Correction after independent review F1 (PASS WITH MINOR)

The reviewer found that the method part-B REMOVE trace did not name
DEL-09-05 `DEP-09-05-005`, a PREREQUISITE on the retired DEL-06-04, and
that Seq 38 lacked `dependency-extract`. Steps 22–25 repaired this inside
this snapshot only. Superseded hashes: `Impact_Assessment.md`
`803cb65b…75bd7` → `0bcbe9bdced43fa887a859497b3edd197242a0eea8fa3a41fab7147b358239bf`;
`Amendment_Actions.csv` `e4013f25…cd30` →
`5c4ae0532eb65ea83d0529a9f6395da392ae2bf5b254cfb6b2de49e4fbff2be2`;
`Decision_Log.md` `44a87380…7ab6` →
`55551f5628608f1a6475f832b70721f7d055adb18ab0b55d80b7e7e3326b658f`.
`Brief.md` quotes neither hash and is unchanged.

## Write containment

`git status` at step 20 shows, besides this run's two new folders, only
paths that belong to concurrent nodes of HELP_HUMAN run
`HELP-HUMAN-PEC-20260923-SCA005` and pre-existed or were written by them:
`_DECISIONS/_REGISTER.md` (D-PEC-86 row), DEL-01-03 `MEMORY.md` and three
`REMAINING_EVIDENCE_DEL-01-03-REM-00{1,2,3}/` folders (node C1), the
assessment, the run folder, the prep folder, D-PEC-86 and
`NOTICE_TRIAGE_2026-09-23.md`. This run read DEL-01-03 `MEMORY.md` (paired
read) but did not write it. Decomposition, registers, pointers, PRD, SOWs,
`_CONTEXT.md`, `_STATUS.md`, `v2/**`, `_DomainEngines/**` and all foreign
paths are byte-unchanged.

## Remaining blockers and owner decisions

1. Owner answers to the checkpoint-1 question set (`Impact_Assessment.md`
   §15): CP1-A/B, Q1–Q10, CP1-R, CP1-D79, CP1-TM, CP1-X, CP1-N, CP1-V, CP1-O.
2. After acceptance: write the group-1 decision snapshot (`DECISION.md`,
   `ACCEPTED_MANIFEST.csv`, `Handoff_State.md`) under
   `_ScopeChange/checkpoint_snapshots/`; only then prepare checkpoint 2.
3. Known limits: the checkpoint-2 plan must specify the RETIRED-row
   representation against XRG-003/005/007/008 and whether `audit-decomp`
   flags a zero-coverage retired row (UNKNOWN now); dependency topology after
   re-extraction is UNKNOWN; which SCA-004 downstream repairs have happened
   since 2026-08-03 was not verified here.

Amendment 2026-09-24 (HELP_HUMAN): `Decision_Log.md` gained a companion pointer to the run-record note `AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/CHECKPOINT1_RESOLUTION_NOTE.md` (kept outside this snapshot per D-PEC-86 §4); its hash above is updated from `701ae542…` to `2dc6fb3e…`. `Impact_Assessment.md` and `Amendment_Actions.csv` are unchanged.

Amendment 2026-09-24 (second, HELP_HUMAN): after the companion note was relocated to the run record, `Decision_Log.md` hashes `55551f5628608f1a6475f832b70721f7d055adb18ab0b55d80b7e7e3326b658f`; the value above is updated again (earlier interim value `2dc6fb3e…` superseded). `Impact_Assessment.md` and `Amendment_Actions.csv` remain unchanged.

Amendment 2026-09-24 (third, HELP_HUMAN): the owner accepted checkpoint group 1 in the session chat (verbatim in `Decision_Log.md` §"SCA005-CP1 — owner acceptance of record"). The group-1 decision snapshot now exists at `../checkpoint_snapshots/SCA-005_GROUP-1_2026-09-24/` (`DECISION.md`, `ACCEPTED_MANIFEST.csv`, `Handoff_State.md`); the "Group-1 decision snapshot: not created" and "Stage reached" rows above describe the pre-acceptance state. `Decision_Log.md` hashes `8508318a95c830a4cf8c7d665ab516f8ea376559e126c581fb8a9c5e6f6f7075` (CP1 rows moved from `AWAITING_OWNER` to `ACCEPTED` / `SELECTED VIA CP1-B` / `CONFIRMED`; earlier value `55551f56…` identifies the pre-acceptance log and is kept in `ACCEPTED_MANIFEST.csv`; the hash table above is updated in place, as the earlier amendments did). The amendment-qualified pointer `../SCA-005_GROUP-1_AUTHORIZED.md` is written per the scope-change method; `_LATEST.md` is untouched. `Impact_Assessment.md`, `Amendment_Actions.csv`, `Brief.md` and `Pre_Change_Coverage.json` are unchanged. Next owning actor: WORKING_ITEMS (scope-change) for checkpoint-2 preparation from the accepted group-1 snapshot; state fields above otherwise unchanged (`ReadyForNextPhase = NO` until checkpoint 3).

Amendment 2026-09-24 (fourth, HELP_HUMAN): the owner selected the TM-PEC-023 values and deferred cmux (verbatim in `Decision_Log.md` §"SCA005-A1 — owner acts of record"). The additive group-1 amendment snapshot is `../checkpoint_snapshots/SCA-005_GROUP-1_AMENDMENT-1_2026-09-24/` (`DECISION.md`, `ACCEPTED_MANIFEST.csv`, `Amendment_Actions_Addendum.csv`, `Handoff_State.md`); the group-1 snapshot is unchanged. `Decision_Log.md` now hashes `321be32d0ca51377dc750938dfe9d9e66204d4da4a128af273c1804e682e96b4` (rows SCA005-A1-TM and SCA005-A1-CMUX added; CP2 row reworded; non-decisions updated); the hash table above is updated in place. `Impact_Assessment.md`, `Amendment_Actions.csv`, `Brief.md` and `Pre_Change_Coverage.json` are unchanged. Next owning actor unchanged: WORKING_ITEMS (scope-change) for checkpoint-2 preparation, consuming the group-1 snapshot and amendment 1 together.

Amendment 2026-09-24 (fifth, HELP_HUMAN): the owner mapped SOW-033 to OBJ-003 (verbatim in `Decision_Log.md` §"SCA005-A2 — owner act of record"). The additive snapshot is `../checkpoint_snapshots/SCA-005_GROUP-1_AMENDMENT-2_2026-09-24/`; the group-1 snapshot and amendment 1 are unchanged. `Decision_Log.md` now hashes `6695e0344a247b3db9b22975781c8c3899b4873a9a396b9745aab4a0fcf50924` (row SCA005-A2-SOW033 added; CP2 row reworded); the hash table above is updated in place. Next owning actor unchanged: WORKING_ITEMS (scope-change) for checkpoint-2 preparation, consuming the group-1 snapshot and amendments 1 and 2 together.

Amendment 2026-09-25 (sixth, HELP_HUMAN): the owner ruled `D-PEC-90` R-A (verbatim in `Decision_Log.md` §"SCA005-D90 — owner act of record"). Row SCA005-D90-NOTE carries a preparation note into checkpoint 2: DEL-04-01 and the PRD §8 refresh are not rebuilt around verify-before-rely, and the reliance text is amended by a later PEC scope change. No snapshot is created and no intake action changes. `Decision_Log.md` now hashes `d8aced8d7cf196401525dd2ed5db0ad315ca042e0772d716bf453f949d1b8a11`; the hash table above is updated in place. Next owning actor unchanged: WORKING_ITEMS (scope-change) for checkpoint-2 preparation, consuming the group-1 snapshot and amendments 1 and 2, and carrying the D-PEC-90 note.

Amendment 2026-09-25 (seventh, WORKING_ITEMS B2): the checkpoint-group-2 package is prepared and independently verified, awaiting the owner. Brief `B2_SCA005_CHECKPOINT2.md` SHA-256 `75a8f596712e00926358aa721455a296e6370ee69dda4b8c2eb7c57324e48f11`. `Decision_Log.md` row SCA005-CP2 moved to `PREPARED / AWAITING_OWNER` with the package hashes (its new hash is in the table above). Nothing is applied: live decomposition revision 1.4, registers, PRD v2.2, every SOW, `_CONTEXT.md`, `_STATUS.md`, `v2/**`, both `_LATEST.md` pointers and the checkpoint snapshots are byte-unchanged. `Impact_Assessment.md`, `Amendment_Actions.csv`, `Brief.md` and `Pre_Change_Coverage.json` are unchanged.

### State fields after checkpoint-2 preparation (2026-09-25)

| Field | Value | Note |
|---|---|---|
| `DecompositionTruthState` | `INCOMPLETE` | exact amendment prepared as candidate postimages; not applied |
| `DerivativePackageState` | `INCOMPLETE` | every derivative obligation is future work (`Propagation_Plan.md` Lane B) |
| `ContentRemediationState` | `NOT_REQUIRED` | SOFTWARE variant |
| `DownstreamRerunState` | `FROZEN` | no downstream rerun authorized |
| `MetadataAlignmentState` | `NOT_STARTED` | 22 direct `_CONTEXT.md` mirrors and 4 `_STATUS.md` retirements planned (Lane A2/A3), not applied |
| `AuditState` | `WARNINGS` | pre-change baseline only; candidate register validation 0 errors / 2 expected DRB-008 warnings; post-change audit `NOT_RUN` |
| `ReadyForNextPhase` | `NO` | |

Next owning actor: the owner (checkpoint-2 question set), then HELP_HUMAN (group-2 decision snapshot, D-PEC register row, receipt, STATUS/README), then WORKING_ITEMS for checkpoint-3 preparation from the accepted group-2 snapshot.

Amendment 2026-09-25 (eighth, HELP_HUMAN): the owner accepted checkpoint group 2 (verbatim in `Decision_Log.md` §"SCA005-CP2 — owner acceptance of record"): Q-CP2-A accept, Q-CP2-1..3 (a), Q-CP2-4 (a) with Lane A4 deferred. The group-2 decision snapshot is `../checkpoint_snapshots/SCA-005_GROUP-2_2026-09-25/` (`DECISION.md`, `ACCEPTED_MANIFEST.csv`, `Handoff_State.md`) with the amendment-qualified pointer `../SCA-005_GROUP-2_AUTHORIZED.md`; register row `D-PEC-92` makes it the D-PEC packet opening Lane A except A4. `Decision_Log.md` now hashes `db1a3518bf1c70e9d69f522846ce303172d8698c42bba6999b58ab667d7a56ac` (SCA005-CP2 row `ACCEPTED`, SCA005-CP3 row `PREPARATION AUTHORIZED / NOT_STARTED`); the hash table above is updated in place. No checkpoint-2 artifact changed. Next owning actor: WORKING_ITEMS (scope-change) for checkpoint-3 preparation. State fields: `DecompositionTruthState` `INCOMPLETE`; `DerivativePackageState` `INCOMPLETE`; `ContentRemediationState` `NOT_REQUIRED`; `DownstreamRerunState` `FROZEN`; `MetadataAlignmentState` `NOT_STARTED`; `ReadyForNextPhase` `NO`.

Amendment 2026-09-25 (ninth, WORKING_ITEMS B3): checkpoint-3 preparation executed under brief `B3_SCA005_CHECKPOINT3.md` (SHA-256 `69c2296749cee727e1bd84b13f7a4ebcad93400f8ceb6267519e79601811b17f`) and the accepted group-2 snapshot. The heading and front matter above now name checkpoint group 3; the earlier sections are unchanged records of their stages. `Decision_Log.md` row SCA005-CP3 moved to `PREPARED / AWAITING_OWNER` (hash table above updated in place, as the earlier amendments did).

## Checkpoint-group-3 handoff state

### Candidate and pointer posture

| Field | Value |
|---|---|
| Candidate snapshot | `projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/` — complete, **not active** |
| Pointer posture | `ACCEPTED_PREDECESSOR` |
| Accepted predecessor snapshot | `_ScopeChange/SCA-004_2026-08-02_2325/` (`_ScopeChange/_LATEST.md` `721a14dc27b4b595be79f591f49b7374a121c52a77eb0451d32d9aa32a9e6280`, unchanged) |
| Accepted group-2 decision snapshot | `../checkpoint_snapshots/SCA-005_GROUP-2_2026-09-25/` (with the group-1 snapshot and amendments 1 and 2); register row `D-PEC-92` |
| Expected pre-acceptance pointer state | `_ScopeChange/_LATEST.md` names SCA-004; `_Decomposition/_LATEST.md` names revision 1.4 (`7abf65e641a5a247f0c783192808ae1f9186f76ebe0d09d6e84e2983fffcd7a3`); both unchanged — confirmed |
| Artifact completeness (C5) | all present — table below |

### Authoritative truth changed in this run

Live `_Decomposition/SOFTWARE_DECOMP.md` is revision 1.5 in pre-acceptance form (`37ea1084a8219943a69057be377646c69a609a76728241963045d7cfb015a6cc`; `status: candidate_pending_checkpoint_3`; accepted form `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660`); the four registers and `docs/PRD.md` v2.3 equal their accepted postimages; 22 `_CONTEXT.md` mirror the accepted rows; DEL-06-04, DEL-07-02, DEL-07-04 and DEL-07-05 `_STATUS.md` read `RETIRED`. Revision 1.4 remains the accepted basis until the owner's checkpoint-3 acceptance. Per-path pre/post hashes: `RUN_SUMMARY.md` §"Actions taken".

### Derivative-package state

| Package | Owner | Status | Evidence | Next required action |
|---|---|---|---|---|
| Decomposition + 4 registers | SCOPE_CHANGE | applied; `CURRENT` after checkpoint 3 | C1, C2, C3 | owner Q-CP3-A; A6 restores the two front-matter lines |
| PRD v2.3 | owner-adopted (group 2) | applied | C1 | — |
| 22 direct `_CONTEXT.md` | SCOPE_CHANGE | applied (provenance already reads revision 1.5 `current_basis`; audit COV-076) | C1 | restore on refusal |
| 4 retired `_STATUS.md` | SCOPE_CHANGE | `RETIRED` | C1; audit Check 11 | — |
| 42 other `_CONTEXT.md` (the plan says 40; audit COV-072, evidence correction), 64 `_REFERENCES.md` | PROJECT_SETUP | `STALE_REPIN_REQUIRED` | audit `context_provenance_revision` 1.5: 22 / 1.4: 42 | B1 |
| DEL-02-08/09 folders | PROJECT_SETUP (own packet) | `NOT_CREATED` — A4 deferred | audit COV-001/002/070/071; DRB-008 ×2 | A4 with B3 |
| Dependency registers and mirrors | dependency-extract / PROJECT_SETUP | `STALE_REBUILD_REQUIRED` (pre-B3: 119 edges, `DEP-09-05-005` present) | C2 | B3 |
| 23 SOWs needing currency work + 5 housekeeping-only | WORKING_ITEMS + artifact gates | `STALE_REVIEW_REQUIRED` / `STALE_REBUILD_REQUIRED` | plan B4 | B4 |
| DEL-00-01 ADRs, DEL-00-03 SPEC | owning workflows | `STALE_REVIEW_REQUIRED` | plan B5 | B5 |
| Registry source | later D-PEC packet | `STALE_SOURCE_PACKET_REQUIRED` | plan B6 | B6 |
| P1 fixture suites | DEL-02-08/09/03 SOWs | `NOT_STARTED` | plan B7 | B7 |
| Post-change audit | TASK audit-decomp | done: `COV_SCA005_POSTCHANGE_2026-09-25_1344` | `coverage_summary.json` `912610ff55e7e53788cb07c972a5a27afe5e246ecadb042932d57776cc0c4deb` | re-audit after A4/B3 |
| Pointers | SCOPE_CHANGE via HELP_HUMAN | unchanged | C1 | A6 after acceptance |
| TM-PEC-023; README/STATUS; D-PEC-90 amendment; `projects/pec/AGENTS.md` L28/L170 | task-management; HELP_HUMAN; next scope change; instruction tranche | open | plan B8 | after checkpoint 3 |
| Foreign notices (Root ×2; App and Piping `adapter.yaml`) | HELP_HUMAN | drafted in the B3 return; not written by B3 (outside its boundary) | — | HELP_HUMAN writes them in checkpoint-3 preparation, before or with the checkpoint-3 presentation (group-2 `DECISION.md` §Notices) |

### Active derivative-surface state

| Surface | Classification | Status | Evidence |
|---|---|---|---|
| `SOFTWARE_DECOMP.md` | `DIRECT_EDIT` | applied (pre-acceptance form) | `37ea1084…a6cc` |
| `ScopeLedger.csv`, `Deliverables.csv`, `ContextBudgetQA.csv`, `Companion_Inventory.csv` | `DIRECT_EDIT` | applied byte-for-byte | C1 |
| `docs/PRD.md` | `DIRECT_EDIT` (owner-adopted bytes) | applied | `fff27a66…fdc32` |
| 22 `_CONTEXT.md`, 4 `_STATUS.md` | `DIRECT_EDIT` | applied | C1 |
| this snapshot | `RECOMPUTE` | complete | table below |
| `COV_SCA005_POSTCHANGE_2026-09-25_1344/` | `RECOMPUTE` | written by TASK audit-decomp | 9 files |
| `_Decomposition/_LATEST.md`, `_ScopeChange/_LATEST.md` | `RECOMPUTE` after acceptance | unchanged | C1 |
| all other `_STATUS.md` and `_CONTEXT.md`, SOWs, dependency registers, `_REFERENCES.md`, `v2/**` | `NO_CHANGE` | unchanged | C1 |

KTY remediation manifest and KTY metadata alignment: not applicable (SOFTWARE variant).

### Snapshot artifact hashes (C5)

| File | SHA-256 |
|---|---|
| `Brief.md` | `aaf2821bb99deb4ff8b640f5e8584338ebd5fc2d95c5c00dd1e2bd136ac43d50` |
| `Impact_Assessment.md` | `0bcbe9bdced43fa887a859497b3edd197242a0eea8fa3a41fab7147b358239bf` |
| `Amendment_Preview.md` | `ad48cc5621d796a662addc03640a32f7f4cdafbf627ad6fda3f60bdede65ebe4` |
| `Propagation_Plan.md` | `50cd0b1d91ea25cc8ecba28ce649278b376fb952feec09e007a26ca5bbf91350` |
| `Amendment_Actions.csv` | `5c4ae0532eb65ea83d0529a9f6395da392ae2bf5b254cfb6b2de49e4fbff2be2` |
| `Amendment_Actions_CP2.csv` | `7bb3bada88ed20adccab6a4077d77d2d7702f03637db230d88f862dea2a09987` |
| `Supersession_Delta.csv` | `cb2a3585a7d75a76c101c30777175ea683079aab0ff74e7ce7783bb55ce89a06` |
| `Supersession_Map.csv` | `4ca705ba090cafb9a74870a0095be490c1d507149767dac32ec52879c487240c` |
| `Pre_Change_Coverage.json` | `61163c96924e6dfb1f3fa6d1449b523c7280e808c92005cc77d64096858b5d9f` |
| `Post_Change_Coverage.json` | `912610ff55e7e53788cb07c972a5a27afe5e246ecadb042932d57776cc0c4deb` |
| `PRD_V2_3_SUCCESSOR_DIFF.md` | `153a4dedb4551102ffe20c26a4dd7d4d4dba9138b28ce47f2e0889925197eba2` |
| `RUN_SUMMARY.md` | `e3480b782b9e219af1a0dcb569829df8d6014f617ffe826f2afc33529107196a` |
| `Decision_Log.md` | `85676c5326da5446e62698c70760a2c55eea011bc4e2810727e3509f393f4d7b` |
| `CP2_CANDIDATE/_Decomposition/SOFTWARE_DECOMP.md` | `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660` |
| `CP2_CANDIDATE/_Decomposition/ScopeLedger.csv` | `83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df` |
| `CP2_CANDIDATE/_Decomposition/Deliverables.csv` | `b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a` |
| `CP2_CANDIDATE/_Decomposition/ContextBudgetQA.csv` | `2a1941050d06e5e07f6cde629d0abf0c2d80acde1983139e6c1918cfca9eb0df` |
| `CP2_CANDIDATE/_Decomposition/Companion_Inventory.csv` | `7c8a24a868ff03415c4440055dc099aaf7e2d87cca8dc0267e77d1a676976ef8` |
| `CP2_CANDIDATE/docs/PRD.md` | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` |

Every checkpoint-1 and checkpoint-2 artifact above is byte-identical to its accepted hash; besides the three new A5 files, only `Decision_Log.md` and this file changed: additive sections, with the front matter, this file's heading, the SCA005-CP3 row and the hash-table row updated in place (disclosed in the ninth amendment).

### State fields at checkpoint-3 preparation

| Field | Value | Note |
|---|---|---|
| `DecompositionTruthState` | `COMPLETE` | revision 1.5 applied; front matter in pre-acceptance form |
| `DerivativePackageState` | `INCOMPLETE` | Lane B open; A4 deferred |
| `ContentRemediationState` | `NOT_REQUIRED` | SOFTWARE variant |
| `DownstreamRerunState` | `FROZEN` | no Lane B item authorized |
| `MetadataAlignmentState` | `IN_PROGRESS` | 22 mirrors + 4 retirements done; B1 (42 contexts, 64 references) open |
| `AuditState` | `BLOCKED` | audit `BLOCKERS` / `FAIL` by the count rule (2 / 6 / 74); classification-adjusted reading beside it: both blockers EXPECTED_CONSEQUENCE of the A4 deferral, otherwise 0 blockers / 4 warnings (`WARN`) |
| `ReadyForNextPhase` | `NO` | |

### Closure verdict

`OPEN_PENDING_DERIVATIVE_CLOSURE` until the owner acts. On acceptance the recommended verdict is `CLOSED_FOR_SCOPE_CHANGE_ONLY`, with A4 and every Lane B item recorded open (owner choice Q-CP3-1 in `RUN_SUMMARY.md`).

### Remaining blockers and owner decisions

1. Owner: Q-CP3-A (accept the audited poststate) and Q-CP3-1 (closure verdict), `RUN_SUMMARY.md` §"Checkpoint-3 owner question".
2. HELP_HUMAN, in checkpoint-3 preparation (group-2 `DECISION.md` §Notices), before or with presenting checkpoint 3: write the three foreign notices from the drafts in the B3 return (outside B3's write boundary; not written when B3 handed back), and commit brief `B3_SCA005_CHECKPOINT3.md` (`69c22967…11b17f`) to the run record's `briefs/`. On acceptance, HELP_HUMAN: record the act; A6 with the acceptance date (both `_LATEST.md` pointers; the decomposition's `status:`/`accepted:` lines and four date slots, slot hash rule); refresh orientation surfaces.
3. On refusal: restore every Lane A path to its preimage, including the 22 A2 mirrors (COV-076); pointers stay on revision 1.4 / SCA-004 (`RUN_SUMMARY.md` §"Rollback on refusal").
4. Evidence correction COV-072: B1 re-pins 42 `_CONTEXT.md`, not 40; the accepted plan's bytes are not edited.

### Next owning workflows

HELP_HUMAN (foreign notices and the B3 brief now; owner checkpoint 3; then A6); PROJECT_SETUP under its own packet (A4 with B3; B1); dependency-extract (B3); WORKING_ITEMS with artifact gates (B4, B5); a later D-PEC source packet (B6); task-management (TM-PEC-023); the next PEC scope change (D-PEC-90 reliance text); `audit-decomp` re-run after A4/B3.

Repair 2026-09-25 (WORKING_ITEMS B3, after verifier verdict 01, PASS WITH MINOR): `RUN_SUMMARY.md` now records the actual `git diff --check` result (CRLF in the accumulator output only), states where the B3 brief is held, places the foreign notices in checkpoint-3 preparation as group-2 `DECISION.md` §Notices says, describes the in-place edits, and closes out audit COV-075 and the deferred C4 isolated-node sub-expectation; this file's items above are aligned. Hashes: `RUN_SUMMARY.md` 89c1ed8c1660e5d0b7f962190e94a1660927146b8c7fbcf24c5492339144d984 → e3480b782b9e219af1a0dcb569829df8d6014f617ffe826f2afc33529107196a; `Decision_Log.md` c285e66299b6a3290685764ce9585bdd19e44707b5037afe7842b4c9c1fa505f → 85676c5326da5446e62698c70760a2c55eea011bc4e2810727e3509f393f4d7b (only the two `RUN_SUMMARY.md` hash citations changed). No Lane A byte changed.
