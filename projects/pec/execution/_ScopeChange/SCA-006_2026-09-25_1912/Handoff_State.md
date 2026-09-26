---
amendment_id: SCA-006
doc_kind: scope_change.handoff_state
decomp_variant: SOFTWARE
checkpoint_group: 1
created: 2026-09-25
status: checkpoint_1_package_prepared_awaiting_owner
---

# SCA-006 Checkpoint-group-1 Handoff State

## Position

| Field | Value |
|---|---|
| Snapshot | `projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/`: an interim checkpoint-1 package, **not** an active snapshot |
| Stage reached | checkpoint group 1 prepared (method parts A and B); owner acceptance **not** given |
| Gate 1 | opened by owner direction under `D-PEC-90` R-A and `D-PEC-94` (`Decision_Log.md` SCA006-G1; reading them as opening SCA-006 is HELP_HUMAN's interpretation) |
| Accepted decomposition basis | `SOFTWARE_DECOMP.md` revision 1.5 `current_basis`, SHA-256 `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660` (unchanged by this run) |
| Accepted predecessor | `_ScopeChange/SCA-005_2026-09-23_2139/`; pointer posture for a later checkpoint 3 is `ACCEPTED_PREDECESSOR` |
| Pre-change baseline | `_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_2026-09-25_1606/` (reused; audit inputs are byte-identical since its audited commit, per Impact Assessment §2.1); `Pre_Change_Coverage.json` is a byte copy of its `coverage_summary.json` |
| Impact Assessment for owner acceptance | `Impact_Assessment.md`, at the SHA-256 in the table below |
| Group-1 decision snapshot | not created; it follows owner acceptance, under `_ScopeChange/checkpoint_snapshots/` |
| Next owning actor | the owner (question set, Impact Assessment §15); then WORKING_ITEMS (scope-change) prepares checkpoint 2 from the accepted group-1 snapshot |
| Blockers | the owner's checkpoint-1 decision is the only blocker. The package has no internal blocker: independent verification reported no BLOCKING findings in any round (`returns/B4_VERIFIER_VERDICT_*.md`) |
| Basis commit | prepared at `origin/main` `13df8b795`; branch merged `origin/main` `bec8bdd65` before publication with no material drift (Impact Assessment §2.2) |

## Required state fields

| Field | Value | Note |
|---|---|---|
| `DecompositionTruthState` | `UNCHANGED_REVISION_1_5` | mirrors the SCA-005 checkpoint-1 convention. No amendment has begun, so neither `INCOMPLETE` nor `COMPLETE` describes it |
| `DerivativePackageState` | `INCOMPLETE` | nothing applied. Every SCA-006 derivative obligation is future work (Impact Assessment §7). SCA-005's own derivative state is governed by its handoff |
| `ContentRemediationState` | `NOT_REQUIRED` | SOFTWARE variant; no KTY lane |
| `DownstreamRerunState` | `FROZEN` | no downstream rerun authorized |
| `MetadataAlignmentState` | `NOT_STARTED` | for SCA-006 |
| `AuditState` | `WARNINGS` | pre-change baseline only: 0 blockers / 3 warnings / 70 info. Post-change audit `NOT_RUN` |
| `ReadyForNextPhase` | `NO` | |
| Closure verdict | none; checkpoint 1 is open | neither `CLOSED_FOR_SCOPE_CHANGE_ONLY` nor `OPEN_PENDING_DERIVATIVE_CLOSURE` applies before application |

`Supersession_Delta.csv` is a checkpoint-2 artifact, and none exists in this
package. All 54 action rows therefore carry `SupersessionBindingPresent = NO`.
The candidate bindings SB-1..SB-6 are listed in Impact Assessment §9.3.

## Snapshot file hashes (this file excluded)

| File | SHA-256 |
|---|---|
| `Brief.md` | `205a46c04f2db6d34bead78db3064a02ff9d9d66a5e54fa9ff06b5c6314a1831` |
| `Impact_Assessment.md` | `93253b7d016de041b2295307af5564808fdc3d9a4e392f1cf92892363fecb691` |
| `Amendment_Actions.csv` (PROPOSED) | `c5f90801989ee9948ccdd375917ba052fdb5838183e387ed373d8c7c2b824891` |
| `Pre_Change_Coverage.json` | `b7b432a2b9e9ae13a911c7193b02776e64cd07e247135b3c98caf77882f4128d` |
| `Decision_Log.md` | `b4b75e3569a210597ba87b8c0bd223b81bb3f98db18444b63ca73e1e389465df` (after the checkpoint-2 acceptance; `dc6e89fe74059e9a016cbcd69b0019dc567a7048062c626c83daa6225d5b170e` at the checkpoint-2 act; `8a01bd653eca52bb8ffae947ffce28d83d7da6beaf690b35c72563f88615547a` at the checkpoint-1 act) |

## Basis hashes not repeated elsewhere

| File | SHA-256 |
|---|---|
| Root `docs/PRD_ROOT.md` | `b6fa4e3d5ec5c20a4aa1dbfdfd43bed5a13d8287bc78f4635e3d944fb6c11931` |
| Root `docs/CONTRACT.md` | `64747d2a3c58ae93194bd5c7118d89a591b7b4ebe8cec7e88cb6a95dc55895bd` |
| `_Coordination/_DECISIONS/_REGISTER.md` | `031adae37d3984c26545a21662d010b7377532aefefe79c5c7addeccca4ba2f7` at base; `19a385c898d50b9dfc8d754a5cc9c84c29f0116e321eeafe29eed21a00dc64a3` at `bec8bdd65` |
| `WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` at `bec8bdd65` | `f669ebe53d483419799e5c947ea903996187570e608f3ee2b849030c0ec00f78` |
| `_ScopeChange/_LATEST.md` | `a2b5b789d996d52aa43c86419c9a4f02d1aa01f438f1616f3d51921e34f84268` |
| `_Evaluation/DecompCoverage/_LATEST.md` | `2b43dc3bb34163ae51067f6176ebf235430b59aa668890c1e65d7cc9d3cf1450` |
| `_Decomposition/_LATEST.md` | `1f2cdcba31b3db2fd8818b16202d2bbc89c3f4a20702a962d133a73e10f556b6` |
| SCA-005 `Decision_Log.md` / `Handoff_State.md` / `RUN_SUMMARY.md` | `09f99fb175c0b81c23b4f680babd04272a8e1e4126887f30582d7a072bb95a6e` / `a86ae910d0c9ae7bf20a7ebb47de3edb345d1a6067cb1988fc04d5c1d213328a` / `e9a0224ec0152bba75c78b84e2c9abe7a5996014eec602b46de4fe3153c1e518` |
| `ACTIVE_RELIANCE_HOLDS.csv` / `pec_reliance_hold.py` | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` / `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` |
| `projects/pec/loop/LOOP_INIT.md` | `c97d49fff5c2fabca1c9c05b44bcde958e46fccb067d512ce93779d4cfad821b` |

## Delegation record

| Child | Mechanism | Parent | Basis supplied | Write scope | Enforcement limits | Return |
|---|---|---|---|---|---|---|
| A1 locus inventory (TASK, Type 2) | Claude Code Agent tool, `subagent_type: pec-task`, `model: opus` (host maps to claude-opus-5-5); background | this WORKING_ITEMS instance, itself dispatched by HELP_HUMAN for node R1 of `HELP-HUMAN-PEC-20260925-POST-SCA005` | child brief SHA-256 `7e9cafa8da8995b10118a1058572455891fbe7e47898719830b4445f9ada9e67`, plus two manager messages relaying the HELP_HUMAN addenda | the manager's scratchpad only; read-only on the repository | read-only use and "no Git state change" were instruction-asserted, not tool-enforced; verified afterwards by `git status` (only this snapshot folder is untracked) | `INVENTORY.csv` 232 rows (`bfcad344fe0715c18c8c375ff3b07c402b1f2ed5474737631b235f9e556ac682`), `SOW_POPULATION.csv` 32 rows (`5829902f0938e7c51b3a99d20913bf3ddb6c8b0883e9f64caaa9ab07c9764143`), `INVENTORY.md` (`3c1cce98228953793a05ad47084a22a543d150d833b29e3c1426c78ecd13d16c`); quote verifier `failures=0` over 264 checks |
| Independent verifier, round 1 (TASK, read-only) | Agent tool, `subagent_type: pec-reviewer`, `model: opus` | this WORKING_ITEMS instance | candidate `e2855e552` and brief B4 | none (the reviewer agent type has no write tools) | tool-enforced: no Edit or Write | PASS WITH MINOR: 7 MINOR, 5 NOTE, 0 BLOCKING (`returns/B4_VERIFIER_VERDICT_01.md`). All MINOR findings and NOTEs 8–12 repaired; NOTE 10 is met by the return commit |
| Independent verifier, round 2 (TASK, read-only; same instance, resumed) | as round 1 | this WORKING_ITEMS instance | candidate `64677504b` | none | as round 1 | PASS WITH MINOR: 2 MINOR, 2 NOTE, 0 BLOCKING (`returns/B4_VERIFIER_VERDICT_02.md`); all repaired |
| Independent verifier, round 3 (same instance, resumed) | as round 1 | this WORKING_ITEMS instance | the round-2 repair | none | as round 1 | recorded in `returns/B4_VERIFIER_VERDICT_03.md` |

No audit-decomp child ran; the baseline was reused. The manager drafted every
snapshot file itself.

## Checks (cwd = REPO_ROOT of the worktree; shell zsh; interpreter `python3` 3.13.7)

| # | Check | Exit | Result |
|---:|---|---:|---|
| 1 | `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` (before and after) | 0 | 66 registers, 263 rows, 0 errors, 0 warnings; unchanged |
| 2 | Preimage hashes of the accepted basis (Impact Assessment §2) recomputed | — | all match `_Decomposition/_LATEST.md`, the D-PEC-90 pins and the ruling's selected proposal hash |
| 3 | `Amendment_Actions.csv` parsed against the contract columns and enums (manager script `check_csv.py`) | 0 | 54 rows, 9 columns, 0 errors |
| 4 | Part-A validation (manager script `gen_actions.py`) | 0 | 54/54 PASS; 8 quote spot-checks byte-present |
| 5 | `python3 tools/validation/validate_scope_change_packet.py <snapshot>` | 1 | schema does not fit: the tool validates a PKG-00 "Scope Change Consumable Packet" (`Packet_Contract.md`, `Proposed_SCA_Actions.csv`, …), not a scope-change snapshot. This is expected, as in SCA-005 |
| 6 | `pec_reliance_hold.py --operation exact-correction-preparation` for the PRD, `AGENTS.md`, `SOFTWARE_DECOMP.md`, `ScopeLedger.csv`, `Deliverables.csv`, the DEL-04-01 SOW, the SPEC and this snapshot's IA and actions (run from `projects/pec`) | 0 ×9 | `ALLOW`; the register has a header and no rows |
| 7 | `git diff --check` (snapshot files marked intent-to-add) | 0 | clean |
| 8 | `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` | 0 | pre-existing REVIEW findings only; none concerns this snapshot |
| 9 | `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` | 0 | VALID; the closed ledger is unchanged |
| 10 | Containment: `git status --porcelain --untracked-files=all` | 0 | only this snapshot folder and the run's `returns/` files |
| 11 | `zsh tools/query/scan_next_amendment_id.sh projects/pec/execution/_ScopeChange/` (before the folder existed) | 0 | `SCA-006` |
| 12 | `git diff --name-only 995af4f36 13df8b795` over the audit inputs | 0 | empty (baseline reuse) |

Manager scripts are in its scratchpad and not in the repository:
- `gen_actions.py`, `check_csv.py`, `showlines.py`;
- the check outputs.

A reviewer can rerun the part-A checks by re-reading the cited lines and
registers.

## Checkpoint-1 acceptance (HELP_HUMAN, 2026-09-25; appended)

The owner accepted checkpoint group 1 on 2026-09-25:
"SCA-006 CP1: accept; DQ a; ENV a; BUD a; GATE a; INS a; R-C excluded". The group-1 decision
snapshot is `../checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/`, and the
amendment-qualified pointer is `../SCA-006_GROUP-1_AUTHORIZED.md`.

- The next owning actor is WORKING_ITEMS, which prepares checkpoint 2.
- Checkpoint-2 preparation is authorized. `ReadyForNextPhase` stays `NO`
  until checkpoint 3, and the other state fields in the table above are
  unchanged.
- The Position rows "Stage reached", "Group-1 decision snapshot", "Next
  owning actor" and "Blockers" describe the pre-acceptance state. After the
  acceptance: the stage reached is checkpoint group 1 accepted, the snapshot
  exists, the next owning actor is WORKING_ITEMS, and there is no blocker to
  checkpoint-2 preparation.
- The `D-PEC-95` act post-dates this package's reused baseline; see the
  baseline note in the group-1 `DECISION.md`.
- This file's hash at the owner's act was
  `4526797c0bab914906b13cf095078508f9df2f8ea606fb4a4542dda5ce55f9df`.

## Checkpoint-2 preparation (WORKING_ITEMS B5, 2026-09-25; appended)

The checkpoint-group-2 package is prepared and awaits the owner. Nothing is applied.

- **Brief:** `B5_SCA006_CHECKPOINT2.md` (HELP_HUMAN scratchpad), SHA-256 `142d6be0b0f44c459e895d067081a004df8fa229ac455349e4cc8b26e8abefb4`.
- **Basis:** `origin/main` `4d5f7b91102b7106ff74b98118b2bda2fe873f36` (PR #926 merged).
- **Branch:** `claude/pec-sca006-cp2-package`.
- **Decision log:** row SCA006-CP2 moved to `PREPARED / AWAITING_OWNER`. The package hashes are in `Decision_Log.md` §"SCA006-CP2 — package prepared (not a decision)".
- **Unchanged here:** `Impact_Assessment.md`, `Amendment_Actions.csv`, `Brief.md` and `Pre_Change_Coverage.json`.

**Basis statement (`D-PEC-95`).** This package's §2.1 byte-identity statement no longer holds exactly, because the `D-PEC-95` act changed 119 derivative paths after the reused baseline audit. No text SCA-006 amends changed. The checkpoint-3 audit attributes the resolution of COV-068/069/072/073 to `D-PEC-95` (see `Amendment_Preview.md` §13 and `Propagation_Plan.md` §"Basis currency since checkpoint 1").

### State fields after checkpoint-2 preparation

| Field | Value | Note |
|---|---|---|
| `DecompositionTruthState` | `INCOMPLETE` | exact amendment prepared as candidate postimages; not applied |
| `DerivativePackageState` | `INCOMPLETE` | every derivative obligation is future work (`Propagation_Plan.md` Lane B) |
| `ContentRemediationState` | `NOT_REQUIRED` | SOFTWARE variant |
| `DownstreamRerunState` | `FROZEN` | no downstream rerun authorized |
| `MetadataAlignmentState` | `NOT_STARTED` | 3 direct `_CONTEXT.md` mirrors planned (Lane A2), not applied |
| `AuditState` | `WARNINGS` | pre-change baseline only. The candidate register validation gives 0 errors and 2 expected DRB-008 warnings. The post-change audit is `NOT_RUN` |
| `ReadyForNextPhase` | `NO` | |
| Closure verdict | none | checkpoints 2 and 3 are open |

### Checks (cwd `REPO_ROOT` of the worktree; shell zsh; interpreter `python3` 3.13.7)

| # | Check | Exit | Result |
|---:|---|---:|---|
| 1 | `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` (live tree) | 0 | 66 registers, 263 rows, 0 errors, 0 warnings |
| 2 | The same on a scratch copy of `projects/pec/execution` with the five candidate decomposition files overlaid (byte-identical, checked with `cmp`) | 1 | 0 errors, 2 WARNING DRB-008 (DEL-08-06 and DEL-10-13 have no folder until PROJECT_SETUP, B1); expected, as in SCA-005 |
| 3 | `python3 tools/coordination/analyze_dep_closure.py <scratch>/execution --output-dir <scratch>` (TASK T2) | 0 | COMPLETE/PASS, 111 edges, 66 nodes, 0 SCCs, identical to the live run; the dependency registers do not change |
| 4 | Preimage hashes recomputed: the decomposition, four registers, PRD, `projects/pec/AGENTS.md`, both `_LATEST.md` and the three A2 `_CONTEXT.md` | — | all equal the values in `Propagation_Plan.md` §"Checkpoint-3 preconditions" |
| 5 | `python3 tools/validation/validate_scope_change_packet.py <snapshot>` | 1 | the schema does not fit: the tool validates a PKG-00 consumable packet (`Proposed_SCA_Actions.csv`, `Affected_Surfaces.csv`, …), not a scope-change snapshot (as in SCA-005 and at checkpoint 1) |
| 6 | Parse check of `Amendment_Actions.csv` and `Amendment_Actions_CP2.csv` against the contract columns and enums (manager script `check_csv.py`) | 0 | 54 + 54 rows, 0 errors. The CP2 identity columns equal the intake, every CP2 row cites its intake Seq, and the `Supersession_Delta.csv` DecisionIDs equal the 16 `YES` rows |
| 7 | `validate_instruction_entrypoints.py` on a scratch `git archive` copy with each `AGENTS.md` candidate in place (TASK T3) | 0 | PASS for the preimage, the without-I1 candidate and the with-I1 candidate; entrypoint pytest 24 passed |
| 8 | `validate_instruction_tranche_manifest.py` on scratch copies with the draft manifest and notices (TASK T3) | 0 | CI mode PASS (115 manifests); `--added-manifests-only` diff mode PASS. A negative control with a notice removed gives BLOCK (exit 1) |
| 9 | `validate_instruction_entrypoints.py .` and `validate_instruction_tranche_manifest.py` (CI mode) on the live tree | 0 / 0 | PASS; nothing in the instruction surface changed |
| 10 | `pec_reliance_hold.py --operation exact-correction-preparation` for the decomposition, its four registers, `docs/PRD.md` and `AGENTS.md` (run from `projects/pec`) | 0 ×7 | `ALLOW`; the register has a header and no rows |
| 11 | `accumulate_supersession_map.py` dry run to scratch (prior SCA-005 map + this delta) | 0 | 45 rows, 0 findings |
| 12 | Proof scripts: `prove_preview.py` (43 markdown hunks + 17 register rows reproduce the candidates) and PRD `prove_diff.py` (17 hunks reproduce the PRD candidate); `AGENTS.md` `build_candidates.py` | 0 / 0 / 0 | byte-for-byte |
| 13 | EvidenceQuote scan (`evidence_quotes.py --prd <PRD candidate>`) | 0 | exactly DEP-09-06-003 and DEP-10-03-003 break; DEP-09-06-004 and DEP-10-12-004 stay verbatim |
| 14 | `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check`; `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` | 0 / 0 | pre-existing findings only, none about this snapshot; VALID |
| 15 | `git diff --check origin/main` and containment of `git diff --name-only origin/main` | — | recorded in the run return |

Scripts from the manager and the TASK children are in the session scratchpad (`…/scratchpad/B5/`) and are not in the repository. A reviewer can re-check by recomputing the hashes and by applying the diff documents' hunks to the preimages.

### Delegation record

| Child | Mechanism | Basis supplied | Write scope | Enforcement | Return |
|---|---|---|---|---|---|
| T1, PRD v2.4 candidate (TASK) | Claude Code Agent tool, `subagent_type: pec-task`, `model: opus` (host maps to claude-opus-5-5); background | brief `BRIEF_T1_PRD.md` (`3d594cf2…`), shared canon `CANON.md` (`5617eb1c…`) | `CP2_CANDIDATE/docs/PRD.md`, `PRD_V2_4_SUCCESSOR_DIFF.md`, scratch | instruction-asserted; verified by `git status` and hashes | candidate `ae49b806…`, diff `a743a527…` after one manager-directed revision (F-16 keeps "non-authoritative" in §8 Agents; F-17 defines the v2.4 block's `PROPOSED`) |
| T2, decomposition revision 1.6 and preview (TASK) | as T1 | brief `BRIEF_T2_DECOMP.md` (`a8ff54e9…`), canon, one addendum (provenance tail, paired MEMORY read) | `CP2_CANDIDATE/_Decomposition/**`, `Amendment_Preview.md`, scratch | as T1 | five candidates, preview `25cf2e84…` (filled by the manager afterwards) |
| T3, `projects/pec/AGENTS.md` candidate (TASK) | as T1 | brief `BRIEF_T3_AGENTS.md` (`50876109…`), canon, one revision (PRD §12 wording; `amended:` line) | `CP2_CANDIDATE/AGENTS.candidate*.md`, `AGENTS_MD_CANDIDATE_DIFF.md`, scratch | as T1 | candidates `49ce993a…` / `a8b8d906…`, diff `7c57a1b2…` (revision 2 re-verified the I1 role/method names at `7f33b4dd5`) |
| Independent verifier (TASK, read-only) | Agent tool, `subagent_type: pec-reviewer`, `model: opus`, fresh instance | the package at its commit and brief B5 | none (no write tools) | tool-enforced | `returns/B5_VERIFIER_VERDICT_NN.md` |

The manager wrote `Amendment_Actions_CP2.csv`, `Supersession_Delta.csv` and `Propagation_Plan.md`. It filled the preview's placeholders and made these additive updates.

### Next owning actor

1. The owner decides the checkpoint-2 question set (`Propagation_Plan.md`).
2. HELP_HUMAN then writes the group-2 decision snapshot, the D-PEC register row, the graph and STATUS/README updates.
3. WORKING_ITEMS then prepares checkpoint 3 from the accepted group-2 snapshot.

### Merge basis (2026-09-25/26)

The package was prepared from `origin/main` `4d5f7b911`. Before verification the branch merged `origin/main` `7f33b4dd5` (merge `005a45445`), which carries the Root tranches `ROOT-WORKFLOW-DUPLICATE-RETIREMENT-20260926` and `ROOT-WORKFLOW-WAVE2A-EXECUTION-20260926`. Between the two bases no PEC decomposition, register, PRD, `projects/pec/AGENTS.md`, SOW, `_CONTEXT.md`, `Dependencies.csv` or pointer changed; the only PEC path added is the notice `execution/_Coordination/NOTICE_2026-09-26_WORKFLOW_WAVE2A_EXECUTION.md`. Every preimage hash in `Propagation_Plan.md` §"Checkpoint-3 preconditions" still holds. The merge made one I1 row stale (it named the retired `software-bounded-implementation` workflow and the pre-skill forms of `software-code-review` / `software-defect-diagnosis`); T3 revision 2 corrected only the I1 WORKING_ITEMS and CHANGE rows of `AGENTS.candidate.md`, and the without-I1 candidate is unchanged. Observation not carried: Root `docs/SOFTWARE_WORKFLOW_PROFILE.md` L22 still says "software-* workflows executed by TASK" (Root-owned).

## Checkpoint-2 acceptance (HELP_HUMAN, 2026-09-25; appended)

The owner accepted checkpoint group 2 on 2026-09-25:
"SCA-006 CP2: accept; Q1 a; Q2 a". The group-2 decision snapshot is
`../checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`, the amendment-qualified
pointer is `../SCA-006_GROUP-2_AUTHORIZED.md`, and the Lane A packet row is
`D-PEC-97`.

- The next owning actor is WORKING_ITEMS, for checkpoint-3 preparation.
- `ReadyForNextPhase` stays `NO` until checkpoint 3, and
  `DerivativePackageState` is `INCOMPLETE`, and `DownstreamRerunState` is
  `FROZEN`.
- Some lines in the checkpoint-2 preparation section above describe the
  pre-acceptance state. They are: "The checkpoint-group-2 package is
  prepared and awaits the owner"; the closure-verdict note "checkpoints 2
  and 3 are open"; and the "Next owning actor" list. After the acceptance,
  checkpoint 2 is accepted, checkpoint 3 is open, HELP_HUMAN has written the
  group-2 snapshot, the `D-PEC-97` row, the graph and the STATUS/README
  updates, and the next owning actor is WORKING_ITEMS for checkpoint-3
  preparation.
- Open before checkpoint-3 dispatch: the owner's choice of scope-change
  method edition. See the group-2 `DECISION.md`.
- At the owner's act, this file's hash was `0043e9b1fcf453678e120461ae7809a220091ee35060131fcd1518576af479a9`.

## Group-2 amendment 1 and checkpoint-3 edition (HELP_HUMAN, 2026-09-26; appended)

- **Method edition:** the owner chose the pinned edition ("SCA-006 pinned").
- **AGENTS.md:** the owner directed that the correction to the Remaining sections ride the checkpoint-3 instruction tranche. The owner must explicitly approve its exact hunk before the application PR merges. The record is `../checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/`.
- **Next:** WORKING_ITEMS runs checkpoint-3 preparation.
- **State fields:** `ReadyForNextPhase` stays `NO`, and the other state fields are unchanged.

## Checkpoint-3 preparation (WORKING_ITEMS B6, 2026-09-26; appended)

Lane A is applied and audited. The package awaits the owner's checkpoint-3
acceptance. Nothing is accepted: revision 1.5, SCA-005 as `_LATEST.md` and
fences F-PEC-1..4 stay the accepted basis until then.

- **Brief:** `briefs/B6_SCA006_CHECKPOINT3.md` on `origin/main` `94e9255b6`, SHA-256 `8bdc718105f05dd2f72378e50fea246eb99a38a937938da72afa221bb8872df4`.
- **Method:** the pinned scope-change edition (`WORKFLOW.md` `58f5d1d5…`, `contract.md` `4453a719…`, `method.md` `34187e83…`, read from `4d5f7b911`); the current `audit-decomp` for C4 (`7ba6291c…`, `704929c7…`, `51a0c69b…`).
- **Branch / PR:** `claude/pec-sca006-cp3-execution`; https://github.com/sgttomas/chirality/pull/943 (not merged).
- **Candidate snapshot and posture:** this folder; `ACCEPTED_PREDECESSOR` (SCA-005, `_ScopeChange/_LATEST.md` `e92b3b16…7d24`, unchanged). Accepted group-2 decision: `../checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/` with amendment 1.
- **Authoritative truth changed (candidate):** decomposition revision 1.6 in pre-acceptance form, its four registers, PRD v2.4 and `projects/pec/AGENTS.md`. Hashes are in `RUN_SUMMARY.md` §3.
- **Owner hunk approval:** given 2026-09-26 ("approve hunk"), recorded in `Decision_Log.md` row SCA006-G2-A1. Amendment 1's pre-merge gate is satisfied.
- **Decision log:** SCA006-CP3 is `PREPARED / AWAITING_OWNER`; the question set is `RUN_SUMMARY.md` §9.

### State fields after checkpoint-3 preparation

| Field | Value | Note |
|---|---|---|
| `DecompositionTruthState` | `COMPLETE` | revision 1.6 applied; the two accepted front-matter lines return at A6 |
| `DerivativePackageState` | `INCOMPLETE` | Lane B B1–B8 open, plus the COV-083 follow-up |
| `ContentRemediationState` | `NOT_REQUIRED` | SOFTWARE variant |
| `DownstreamRerunState` | `FROZEN` | no Lane B item authorized |
| `MetadataAlignmentState` | `IN_PROGRESS` | 3 direct mirrors done; the B7 re-pin (63 `_CONTEXT.md`, 66 `_REFERENCES.md`) is open |
| `AuditState` | `WARNINGS` | `COV_SCA006_POSTCHANGE_2026-09-26_0051`: 0 BLOCKER, 3 pre-existing WARNING, 71 INFO, 12 EXPECTED_CONSEQUENCE |
| `ReadyForNextPhase` | `NO` | |
| Closure verdict | `OPEN_PENDING_DERIVATIVE_CLOSURE` | becomes `CLOSED_FOR_SCOPE_CHANGE_ONLY` only on the owner's checkpoint-3 acceptance |

### Derivative-package state

| Package | Owner | Status | Evidence | Next required action |
|---|---|---|---|---|
| Decomposition + registers | SCOPE_CHANGE | applied, pending acceptance | `RUN_SUMMARY.md` §3–4 | owner checkpoint 3; A6 |
| PRD v2.4 | owner-adopted; applied | applied | `RUN_SUMMARY.md` §3 | none |
| `projects/pec/AGENTS.md` tranche | integration owner (B6) | applied; hunk approved | manifest `PEC-SCA006-OPERATIONAL-RELIANCE-20260926` | merge after review and CI |
| 3 direct `_CONTEXT.md` | SCOPE_CHANGE | applied | A2 hashes | none |
| 63 `_CONTEXT.md`, 66 `_REFERENCES.md` | PROJECT_SETUP | `STALE_REPIN_REQUIRED` | audit COV-077, COV-078 | B7 |
| DEL-08-06 / DEL-10-13 scaffolds | PROJECT_SETUP | `NOT_CREATED` | audit COV-003, COV-004 | B1 packet |
| New dependency rows; DEP-09-06-003, DEP-10-03-003 | dependency-extract | `STALE_REBUILD_REQUIRED` | audit COV-075, COV-076, COV-080 | B2, B3 |
| 9 affected SOWs; first SOWs for the new deliverables | WORKING_ITEMS + gates | per plan §B4 | plan §B4 | B4 |
| DEL-00-03 SPEC | owning workflow | `STALE_REVIEW_REQUIRED` | plan §B5 | B5 |
| Tier-0 `pec.yaml` | tier-0 owner | `CURRENT` until a tool is declared | plan §B6 | B6 |
| `v2/**` API schema | later D-PEC packet | `STALE_SOURCE_PACKET_REQUIRED` when built | plan §B8 | B8 |
| `remaining-loop` design text (SOW-094, DEL-01-06, §9) | a later PEC scope change | stale by owner direction. `D-PEC-96` has since been ruled (2026-09-26, PR #946): PEC's row is migrated, and the ruling routes these sentences to graph node S2 and a later scope change. The approved `AGENTS.md` hunk contradicts them until then | audit COV-083; `RUN_SUMMARY.md` Q-CP3-1 | a later PEC scope change |
| Pointers | HELP_HUMAN | unchanged | C1 | A6 on acceptance (and `_Evaluation/DecompCoverage/_LATEST.md` if Q-CP3-2 (a)) |

### Active derivative-surface state

| Surface | Classification | Status | Evidence |
|---|---|---|---|
| `SOFTWARE_DECOMP.md` | `DIRECT_EDIT` | applied (pre-acceptance form) | `3ef0412a…9b29` |
| `ScopeLedger.csv`, `Deliverables.csv` | `DIRECT_EDIT` | applied | candidate hashes |
| `ContextBudgetQA.csv`, `Companion_Inventory.csv` | `RECOMPUTE` | applied as candidate bytes | candidate hashes |
| `Supersession_Map.csv` | `RECOMPUTE` (accumulator) | generated | `010ce5c4…ab92` |
| `Post_Change_Coverage.json` | `RECOMPUTE` | copied from the audit | `b9a068c0…09cf0` |

KTY remediation and metadata-alignment summaries: not applicable (SOFTWARE variant).

### A6 instructions for HELP_HUMAN (after the owner's checkpoint-3 acceptance only)

1. Write `_Decomposition/_LATEST.md` as the revision-1.6 handoff, and `_ScopeChange/_LATEST.md` naming SCA-006.
2. Restore `status: current_basis` and the accepted `accepted:` line in `SOFTWARE_DECOMP.md`. The line's first token is an acceptance-date slot: set it to the checkpoint-3 acceptance date.
3. If the acceptance date is later than 2026-09-26, also substitute it at `date:` (L7), the §7 Revision row (L574) and the DL-21 date cell (L700), so that all four acceptance-date slots (`Amendment_Preview.md` §"Acceptance-bound tokens") carry it. With acceptance on 2026-09-26, the accepted file hashes `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1`. The earlier `86de50c3…` is withdrawn (verifier verdict 01, finding 1).
4. If the owner answers Q-CP3-2 (a), move `_Evaluation/DecompCoverage/_LATEST.md` to `COV_SCA006_POSTCHANGE_2026-09-26_0051`.
5. Rollback if checkpoint 3 is returned: the plan's §"Failure and rollback". Also include the three A2 provenance lines "then by revision 1.6 (`current_basis`, SCA-006 successor)" (audit COV-079) and the instruction-tranche revert. The Runtime notice's present-tense "decomposition revision 1.6 adds …" wording needs a withdrawal notice.

### Remaining blockers and human decisions

- The owner's checkpoint-3 decision (Q-CP3-A, Q-CP3-1, Q-CP3-2).
- HELP_HUMAN's notice review and its `docs/STATUS.md` correction under `D-PEC-88`, before merge.
- A known Root consequence outside SCA-006: the branch merged `origin/main` `f90320c1d`, which carries Root `D-GOV-48` (PR #942). Its updated `validate_decomposition_registers.py` reports 26 XRG-013 warnings for PEC's OUT/TBD ledger items without a PackageID. They are the same 26 IDs as at revision 1.5, SCA-006's four new items are IN with packages, and the owner defers action (`NOTICE_2026-09-26_PACKAGE_HOME_D-GOV-48.md`). PEC's registers are not edited.

### Next owning workflows

The owner (checkpoint 3), then HELP_HUMAN (A6), then the Lane B owners under their own packets.

### Lane C results and snapshot hashes (final rerun at the merged head)

- **C1:** `CP3_EVIDENCE/c1_containment.py` over `git diff --name-status origin/main HEAD` (after the `f90320c1d` merge), exit 0. Every changed path allowed (46 at the final rerun, before the return and verifier files; `CP3_EVIDENCE/c1_result.json`); 34 hash checks pass; no deletion.
- **C2:** 0 ERROR; 2 DRB-008 (planned); 26 XRG-013 (pre-existing, `D-GOV-48`). Closure: 111 edges, 0 SCCs.
- **C3:** 31/31 PASS (`CP3_EVIDENCE/c3_result.json`).
- **C4:** `COV_SCA006_POSTCHANGE_2026-09-26_0051`, `WARNINGS` (0 BLOCKER).
- **C4.3:** PASS WITH MINOR, 0 BLOCKING (`CP3_EVIDENCE/C4_3_REVIEW.md`, with dispositions).
- **C5:** `CP3_EVIDENCE/c5_completeness.py`, exit 0. The hashes of this folder's files are in the final return `returns/B6_SCA006_CHECKPOINT3.md`, because this file and `Decision_Log.md` cannot quote their own final hashes.
- **Independent verification:** fresh `pec-reviewer` verdicts in `returns/B6_VERIFIER_VERDICT_NN.md`.
