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
| `Decision_Log.md` | `4968fe9d62be5151ee3f6832b82c8471b786f9be9061407915eb3bf87e26537c` (after the checkpoint-1 acceptance; `8a01bd653eca52bb8ffae947ffce28d83d7da6beaf690b35c72563f88615547a` at the owner's act) |

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
