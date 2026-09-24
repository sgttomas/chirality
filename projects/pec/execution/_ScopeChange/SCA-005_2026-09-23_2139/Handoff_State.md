---
amendment_id: SCA-005
doc_kind: scope_change.handoff_state
decomp_variant: SOFTWARE
checkpoint_group: 1
created: 2026-09-23
status: checkpoint_1_package_prepared_awaiting_owner
---

# SCA-005 Checkpoint-group-1 Handoff State

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
| `Decision_Log.md` | `2dc6fb3e78d21f78757382c72a862afdbb7d828483eb44de5ccd4139d636e029` |

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
`2dc6fb3e78d21f78757382c72a862afdbb7d828483eb44de5ccd4139d636e029`.
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
