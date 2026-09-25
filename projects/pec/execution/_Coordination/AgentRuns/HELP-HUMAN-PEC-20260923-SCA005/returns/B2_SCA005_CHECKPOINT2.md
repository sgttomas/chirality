# Return B2 — SCA-005 checkpoint-2 package (WORKING_ITEMS, `pec-manager`/opus)

HELP_HUMAN filing of the manager's final report, verbatim below the rule. The host required the manager to hand back before it could write this file, so HELP_HUMAN extracted the report from the manager's SubagentHandback call and filed it here unedited (extracted text SHA-256 `078b32c380ef525b35c7d178570c9144d226dd32897b59b1e557a193d3cf0755`, session scratchpad). After handback HELP_HUMAN updated the PR branch from `main` (`f9c31a5c8`, PR #906; no `projects/pec/` byte changed). The drafter returns T1 and T2 that HELP_HUMAN relayed remain in the session scratchpad only.

---

## B2 return: SCA-005 checkpoint-2 package (WORKING_ITEMS)

The checkpoint-2 package is complete, committed and published as PR https://github.com/sgttomas/chirality/pull/908. Head is `c81945fe8a5ce09e2eca90070cc8b4c97a041d4a` on branch `claude/pec-sca005-cp2-package`, based on `aa312755e`. The PR is not merged and applies nothing. Two verifier cycles returned PASS WITH MINOR, and every finding from both was repaired. The third check, a confirmation of the last repair delta, was still running when I handed back; its verdict is not in hand (see "Still open"). This return is not in the repo either: the host demanded handback before `B2_SCA005_CHECKPOINT2.md` and `B2_VERIFIER_VERDICT_03.md` were written under `returns/`.

**Brief:** `B2_SCA005_CHECKPOINT2.md`, SHA-256 `75a8f596712e00926358aa721455a296e6370ee69dda4b8c2eb7c57324e48f11`. The hash is recorded in `Handoff_State.md` and `Decision_Log.md`.

### Package files (SHA-256)
All under `projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/`:

| File | SHA-256 |
|---|---|
| `Amendment_Preview.md` | `ad48cc5621d796a662addc03640a32f7f4cdafbf627ad6fda3f60bdede65ebe4` |
| `Propagation_Plan.md` | `50cd0b1d91ea25cc8ecba28ce649278b376fb952feec09e007a26ca5bbf91350` |
| `Amendment_Actions_CP2.csv` | `7bb3bada88ed20adccab6a4077d77d2d7702f03637db230d88f862dea2a09987` |
| `Supersession_Delta.csv` | `cb2a3585a7d75a76c101c30777175ea683079aab0ff74e7ce7783bb55ce89a06` |
| `PRD_V2_3_SUCCESSOR_DIFF.md` | `153a4dedb4551102ffe20c26a4dd7d4d4dba9138b28ce47f2e0889925197eba2` |
| `CP2_CANDIDATE/docs/PRD.md` | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` |
| `CP2_CANDIDATE/_Decomposition/SOFTWARE_DECOMP.md` (rev 1.5) | `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660` |
| `CP2_CANDIDATE/_Decomposition/ScopeLedger.csv` | `83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df` |
| `CP2_CANDIDATE/_Decomposition/Deliverables.csv` | `b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a` |
| `CP2_CANDIDATE/_Decomposition/ContextBudgetQA.csv` | `2a1941050d06e5e07f6cde629d0abf0c2d80acde1983139e6c1918cfca9eb0df` |
| `CP2_CANDIDATE/_Decomposition/Companion_Inventory.csv` | `7c8a24a868ff03415c4440055dc099aaf7e2d87cca8dc0267e77d1a676976ef8` |
| `Decision_Log.md` (row SCA005-CP2 set to `PREPARED / AWAITING_OWNER`, with hashes) | `7dcbc51dd30c66bb273e3528e8675e9adba317d974ec63a438ff816d15af371b` |
| `Handoff_State.md` (seventh dated amendment; `DecompositionTruthState INCOMPLETE`, `ReadyForNextPhase NO`) | `fffb91da3e187532f52d7dc1a4cae9ac6f81225a1bea04db06417146bce449c9` |

- **Preimages, all verified to match:** SOFTWARE_DECOMP `7cca5cdb…5c81`, ScopeLedger `2103afa2…9e25`, Deliverables `49f90448…6b72`, ContextBudgetQA `5c8d3099…2bef`, Companion_Inventory `18793e15…ec23`, PRD v2.2 `6833553c…77ba`, `_Decomposition/_LATEST.md` `7abf65e6…d7a3`.
- **Other inputs verified:** the accepted Impact Assessment `0bcbe9bd…39bf`, the accepted intake `5c4ae053…be2`, the resolution note `af4e46d0…0ad2`, and every snapshot file.

**Commit covers:** the package files above; the final `SOFTWARE_DECOMP.md` differs from the candidate only in the `status:` and `accepted:` lines.

### Action counts
- **Intake:** 76 actions (8 ADD / 65 MODIFY / 3 REMOVE).
- **CP2 final:** 79 actions (8 ADD / 67 MODIFY / 4 REMOVE).
- **How they differ:**
  - Dropped: Seq 72 (Q9) and Seq 68 (moot under the cmux deferral). Both numbers stay reserved.
  - Added from the owner's amendments: Seq 77 and 78 (amendment 1) and Seq 79 (amendment 2).
  - Added because amendment 1's impact delta requires them: Seq 80 (the OBJ-004 view) and Seq 81 (the §2.4 bridges bullet).
  - Amendment 2 had counted 77 actions before Seq 80 and 81.
- **Supersession:** 26 actions are flagged YES, each with rows in `Supersession_Delta.csv` (29 rows). D-010 (SOW-077 against D-PEC-78/79) is `SUPPLEMENTARY_EXTENSION` under CP1-V; the rest are `SUPERSESSION`. The accumulator dry run exits 0 with 29 rows and 0 findings.

### Counts that change (rev 1.4 → rev 1.5 candidate)
- Scope items: 94 (72 IN / 14 OUT / 8 TBD) → 96 (70 / 18 / 8).
- Deliverable rows: 64 → 66 (62 active, 4 RETIRED: DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05).
- IN items without an objective: 11 → 0. Active deliverables without objectives: 9 → 0.
- Active envelopes: S 28 / M 34 / L 2 → S 28 / M 32 / L 2.
- Assigned to PKG-02 / PKG-06 / PKG-07: 7 / 7 / 6 → 9 / 6 / 3. PKG-07 active children: 2.
- Vocabulary terms: 22 → 26.
- Execution edges: 119 → 108 after the retirements (planned 111, or 112 with the optional edge; 0 SCCs).
- Unchanged: open/resolved issues 10 / 3; 11 packages; 6 objectives. The union rule holds on all 62 active rows.

### Blocker resolutions
- **RETIRED-row representation.** RESOLVED (preview §10): the row is kept, with a `[RETIRED — SCA-005]` description prefix, blank coverage and objective cells, and its envelope and PhaseHint kept. Deferred OUT ledger rows are cleared. The validator on the candidate overlay gives 0 errors and 2 expected DRB-008 warnings.
- **Does `audit-decomp` flag a zero-coverage retired row?** RESOLVED: no. At most it is INFO, and the Step 7 BLOCKER cannot fire. The post-change audit (C4) confirms this on the real files.
- **Dependency topology.** PLANNED (B3): 119 → 108 → 107 (`[E-P25]` retired, not re-pointed, because a re-point would duplicate DEP-03-01-007) → 111/112, 0 SCCs. Only the final row set is UNKNOWN.
- **SCA-004 downstream repairs.** VERIFIED: all were done by 2026-08-09 (`PEC_CURRENCY_REPAIR_CLOSEOUT_2026-08-09`). Only TM-PEC-023 remained, and SCA-005 carries it.
- **`v2/**` and DEL-01-03 under D-PEC-87/89/91.** None of these changes any action.
- **Found while preparing:**
  - `write_status.sh` and Root SPEC §3.2 reject RETIRED, so A3 is a hand-authored exact edit; this is Q-CP2-1.
  - Evidence corrections: IA §8.1 says 10 OBJ-003 supporters (actually 11, then 14 after the selections); IA §7.1 says 13 reference claims (actually 16).
  - The SOW currency count is 23, not 24: DEL-10-01 is current because Seq 72 was dropped.

### Checkpoint-2 owner question set (end of `Propagation_Plan.md`)
- **Q-CP2-A:** accept the preview, plan, CP2 CSV, delta, PRD candidate and postimages together, at the listed hashes. This includes the one PRD addition not in Annex B (the §7.1 WorkGraph/WorkNode row) and the slot hash rule. Recommendation: accept.
- **Q-CP2-1:** how RETIRED is recorded in `_STATUS.md`. Recommendation: (a) the hand-authored edits, plus a notice to Root.
- **Q-CP2-2:** keep the INV-116 correction riding Seq 12. Recommendation: (a) keep.
- **Q-CP2-3:** residual stale text that no accepted action or Annex B row drives. Recommendation: (a) carry it to the next PEC scope change (D-PEC-90), with bindings where the text is contradicted.
- **Q-CP2-4:** the group-2 snapshot plus a D-PEC register row is the packet that opens the write fence for Lane A (A1–A6 and the C4 audit folder) and records PRD v2.3's adoption. Recommendation: (a).

### Check results
All run from REPO_ROOT (the worktree) with `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3` (Python 3.13.7).

| Check | Exit | Result |
|---|---|---|
| `validate_decomposition_registers.py projects/pec/execution --strict`, live tree | 0 | 0 / 0 |
| Same validator on a scratch overlay with the candidates | 1 under `--strict` | 0 errors, 2 × DRB-008 (DEL-02-08/09), expected |
| `validate_scope_change_packet.py <snapshot>` | 1 | Schema does not fit: it expects the PKG-00 `Packet_*` files. Reported, not applied |
| `parse_check_actions.py` (both CSVs against the contract columns and enums, SB/delta parity) | 0 | clean |
| `check_invariants.py` | 0 | clean |
| `pec_reliance_hold.py --operation exact-correction-preparation`, for SOFTWARE_DECOMP, the 4 registers, `docs/PRD.md` and the snapshot | 0 ×7 | ALLOW |
| Preimage hash checks | — | all match |
| `git diff --cached --check` | 0 | clean |

### Verifier verdicts and cycles
- **Cycle 1:** PASS WITH MINOR, 9 minors (fence packet, WorkGraph row, supersession gaps, hunk wording, D-GOV lineage, replay claim, slot-hash rule, AGENTS.md notice, editorial). All repaired. Saved as `B2_VERIFIER_VERDICT_01.md`, sha `434958b9…3b60`.
- **Cycle 2:** PASS WITH MINOR. All 9 confirmed repaired; 1 new minor (a blank line at EOF in the diff doc) and 4 nits. All fixed. Saved as `B2_VERIFIER_VERDICT_02.md`, sha `e514d2aa…906a`.
- **Cycle 3:** a confirmation of that final delta, sent to the same verifier. Still running at handback; not yet saved.

### Containment
`git diff --name-only aa312755e..c81945fe8` lists only files under `projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/` (the new files, `CP2_CANDIDATE/**`, `Decision_Log.md`, `Handoff_State.md`) and `returns/B2_VERIFIER_VERDICT_0{1,2}.md`. `origin/main` has since advanced to `f9c31a5c8`; those 10 files are all outside `projects/pec`, so the basis is unaffected.

### Still open or routed to you
1. The cycle-3 verdict. If it reaches you, save it as `returns/B2_VERIFIER_VERDICT_03.md`. B2 did not record it.
2. This return is not yet in the repo as `returns/B2_SCA005_CHECKPOINT2.md`; the host demanded handback before I could write it.
3. The two new DEL-02-08/09 folders are still a Lane A4 act.
4. Notices go to Root about the RETIRED method/tool mismatch, and to `projects/pec/AGENTS.md` L28/L170.

### Delegation record
All children were Claude Code Agent tool children, parent B2, run in the background.

| Child | Type / model | Wrote | Return |
|---|---|---|---|
| T1 | `pec-task`, opus | PRD candidate and diff | relayed; saved in scratchpad as `B2/T1_RETURN_RELAYED.md` |
| T2 | `pec-task`, opus | the 5 postimages | relayed; saved as `B2/T2_RETURN_RELAYED.md` |
| T3 | `pec-task`, opus | read-only investigation, scratch only (its FINDINGS.md write was refused by the host) | direct to B2 |
| T4 | `pec-task`, opus | `_CONTEXT.md`/`_STATUS.md` edit data, scratch only | direct to B2 |
| Verifiers ×2 (+1 resume) | `pec-reviewer`, opus | read-only | cycles 1–2 relayed |

Model identity and the no-delegation rule were set by instruction, not enforced by the tool.

I, B2, made these edits myself: the R1 and Seq 74 fold, the cycle-1/2 repairs, and the preview, plan and CSV generators (kept in scratchpad `B2/`).
