# T_V_AUDIT hand-back (verbatim as delivered to the manager)

The add-on V TASK (`pec-task`, agent id `ab4bb2df021ca99e6`, brief `child_briefs/T_V_AUDIT.md`
`d9e3f4e7…4194`) delivered the report below through its SubagentHandback call. The host showed it
with every line indented; the text is reproduced with that indentation removed and nothing else
changed.

---

## Add-on V result: 0 BLOCKER; `overall_status WARNINGS`, `closure_readiness WARN`

The audit ran to completion and every part of the D-PEC-101 prediction held. I found no DEFECT in the D-PEC-101 bytes.

**Snapshot folder:** `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d101-act/projects/pec/execution/_Evaluation/DecompCoverage/COV_D101_POSTSETUP_2026-09-26_1651/`. This is the path `create_snapshot_folder.sh` printed when run from the worktree root at 16:51 MDT.

**Counts:** 78 findings: 0 BLOCKER, 3 WARNING, 73 INFO, 2 EXPECTED_CONSEQUENCE. All 12 checks have a verdict:
- PASS: 1, 2, 3, 4, 5, 7, 8, 9b, 10, 11
- WARNING: 6
- SKIPPED: 9 (not owned by the SOFTWARE variant)

**Files and SHA-256:**

| File | SHA-256 |
|---|---|
| Brief.md | `538f738eab2b94b96d661933ff5b25e8bfd0234ca148f520047fbf872d74dba5` |
| Decision_Log.md | `ebad352f2d9497915fb8e471e0e0bc52578234716cbe15762e0fe19627eba09c` |
| Decomp_Coverage_IssueLog.csv | `36da6ac7c8583329ad6284c68be772cb7f2893487fdbce0a029721996d23342f` |
| Decomp_Coverage_Matrix.csv | `9f9bc2f4231b74a39b47c29373cff825b8dd5835e493aff614cb7f04c2b3c83c` |
| Decomp_Coverage_Report.md | `3d84c97b031b1ef1c1dee5daaa33541901d04c148d4ebf669f116dfda8c5ec82` |
| PrePost_Comparison.md | `ea902b64fd1285ad4a05aaed1b9629d00118d9ce0eb0c457f3a9556c158af4e9` |
| QA_Report.md | `ab5ce75aaa365ec6d5894e4499bd0b85b90f9e3aeb0b7bcdcaae1563e150e5e8` |
| RUN_SUMMARY.md | `0b697514f08519a05c39b725b1b7308e9c4a2be5fa85745dd28d553e4f746b45` |
| coverage_summary.json | `e9090ac3f3fd7574ca120077f8e76037b81cb3cf7450b3b2a951e7d617392439` |
| inventory.json | `b741735d0a8da7d07d6adeca5fe84e69f5a80f4a5d3940354da9d7c28f6ccda3` |
| structure.json | `1359f9a1d1d1ed5c344bef40ad5b66ba66bf11f86bbd7744270ee16d04cf73a5` |

## Prior-ID dispositions

| Prior ID | What it was | Disposition | Cause |
|---|---|---|---|
| COV-003, COV-004 | DEL-08-06 and DEL-10-13 had no folder | RESOLVED | D-PEC-101 K1. 68/68 folders now exist; the structure tool passes 68/68; the strict validator reports 0 DRB-008 |
| COV-073, COV-074 | SOW-099 and SOW-100 pointed at folderless deliverables | RESOLVED | D-PEC-101 K1. Both now resolve to folders |
| COV-075, COV-076 | Two evidence quotes no longer matched their source | RESOLVED | D-PEC-101 K1 (B3). Both are verbatim; all 127 active execution quotes are verbatim |
| COV-077 | 63 contexts still at revision 1.5 | RESOLVED | D-PEC-101 K4. All 68 context provenance blocks end at revision 1.6 |
| COV-078 | 66 references still at revision 1.5 / PRD v2.3 | RESOLVED | D-PEC-101 K4 with add-on C. All 68 name revision 1.6 and PRD v2.4, and every active covers bullet equals its register cell |
| COV-080 | No register traced SOW-097..100 | RESOLVED | D-PEC-101 K1 (B2). All 74 IN items are traced by every deliverable they name |
| COV-008 (DEL-01-03), COV-010 (DEL-01-05), COV-046 (DEL-08-02) | The three Check-6 warnings | CARRIED as COV-006, COV-008 and COV-044, same severity and identical text | Pre-existing |

Across all 86 prior rows the delta is 64 carried, 8 changed, 14 resolved and 6 new. Some prior findings resolved for reasons other than D-PEC-101:
- COV-079 and COV-084 resolved through the SCA-006 checkpoint-3 acceptance and its A6 pointer moves.
- COV-085 resolved when SCA-006 completed its A5 step.
- COV-086 resolved because SCA-005 is now the historical predecessor and its snapshot is complete.

## DEFECT

None. I checked all 161 granted product paths against the proposal's postimage tables (129 from K4, using the add-on C values; 20 modified and 12 created by K1), and every one matches. The branch's product diff against its merge base `f392294b5` contains exactly those paths, plus the run root and the K14A brief copy. These also passed:
- **Registers:** 68 registers, 285 rows; 0 ERROR; 26 XRG-013 warnings; 0 DRB-008.
- **Closure:** 127 edges, 68 nodes, 0 cycles, the same six isolated units; byte-identical to the run root's closure output.
- **Mirrors:** each active execution edge appears exactly once on each side.
- **Uniqueness:** no duplicate IDs or source–target pairs.
- **Anchors:** 138/138 assertions true.
- **Contexts:** 68/68 match the register.

## New findings

**Two EXPECTED_CONSEQUENCE rows, both citing D-PEC-101:**
- **COV-076:** the human-owned Notes line in `_COORDINATION.md` (L225–227, file `95ebe344…`) still says revision 1.5 is `current_basis`. Ruling question 4 (a) authorizes HELP_HUMAN to replace it in this PR. The verifier has passed K1, but the replacement is not yet in the tree.
- **COV-077:** the handoff records still describe Lane B as open:
  - `_Decomposition/_LATEST.md:35` says the two deliverables have "no folders yet", which is now false.
  - Lines 53–55 of the same file, `_ScopeChange/_LATEST.md:15-19` and the SCA-006 state fields all list B1, B2, B3 and B7 as open.
  - D-PEC-101 leaves these records unopened and puts the Lane B closeout in the run root's `HANDOFF_STATE.md`, which does not exist yet.
  - Because these surfaces claim less than the evidence rather than more, Check 10 still passes.

**New or changed INFO rows:**
- **COV-072:** 26 XRG-013 warnings for OUT/TBD ledger rows without a package, under Root D-GOV-48. These are newly measured because the validator changed since the prior run; the owner defers action and D-PEC-101 forbids it.
- **COV-078:** the SCA-006 snapshot lacks `AdjustedAuditState`. That field entered the scope-change contract after SCA-006 bound its edition (`4453a719`), so this is edition drift, not a defect.
- **COV-075 (changed from COV-083):** revision 1.6 still says PEC's registry row declares `remaining-loop`. D-PEC-96 has since been applied, so live `loops.json` no longer has it. The owner carried this text knowingly at checkpoint 3. I kept it at INFO, but that is a judgement call (Decision_Log D-10); a reviewer could fairly raise it to WARNING.

## Instruction hashes read

| File | SHA-256 |
|---|---|
| `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| audit-decomp `WORKFLOW.md` | `7ba6291c836973a6af0aeb81d56d60ede89466c3d006673d7ef07f09b984246b` |
| audit-decomp `contract.md` | `704929c7c006a20a5fbe3fc903d4f172e2edb4c6a451c4b6db40506b40004e75` |
| audit-decomp `method.md` | `51a0c69b389d0c641f88e8faa7bebbc2b3650518eede8882436853c583308827` |
| Brief | `d9e3f4e7…4194` (verified) |

Every parameter hash in the brief matched, and every audited input still had the same hash after the outputs were written.

## Anything unexpected

- **HEAD differs from the brief.** The worktree HEAD is `43b60687b` (the commit that added this brief), not the `fcc1cd26b` the brief names. `git diff 62230fa46 HEAD` touches only run-root files, so the product bytes audited are the ones the brief describes.
- **Run-root closeout files are missing.** `HANDOFF_STATE.md`, `MANIFEST.md` and `VALIDATION.md`, which the Administrative grant calls for, do not exist yet. COV-077 depends on the first of them.
- **Other packets changed the tree after the prior audit.** DEL-02-08 and DEL-02-09 moved OPEN to INITIALIZED with `SOW_V1` contracts (D-PEC-98). 57 `## Remaining` sections were removed from `_STATUS.md` files (D-PEC-99). D-PEC-96 changed files under `v2/` and added DEL-01-06 `MEMORY.md`, which has an empty Runs table.
- **Two boundary deviations, both disclosed:**
  - I ran `git fetch -q origin`, which fast-forwarded `refs/remotes/origin/main` from `bdae9d66b` to `efe938506`. No local branch, index or working tree changed. `origin/main` now also carries the D-PEC-100 ruling and a D-GOV-50 notice. Neither touches an audited input, but both matter for your containment check against `origin/main`.
  - I briefly created and then deleted one temporary file under `/tmp` while checking that `Brief.md` reproduces the brief verbatim.
- **Nothing else was written.** Writes went only to the snapshot folder and the scratch directory `…/scratchpad/d101act/audit/`. `_LATEST.md` was not touched, and I made no git add, commit, push or branch operation. No independent review of this snapshot was performed.
