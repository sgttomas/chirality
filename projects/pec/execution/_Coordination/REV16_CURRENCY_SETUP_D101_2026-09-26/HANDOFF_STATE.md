# PROJECT_SETUP — D-PEC-101 revision-1.6 currency and setup (K1, K4 with add-on C, add-on V): Handoff State

**Act date:** 2026-09-26
**Coordinator:** WORKING_ITEMS (Type 1), brief K14A, nodes K1 and K4 of HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`
**Branch / basis:** `claude/pec-d101-act` from `origin/main` `f392294b5` (PR #969); `origin/main` `17da1a013` merged at `dc68b5afd`
**Publication:** its own PR against `main` under the standing Git authorization of 2026-09-12; not merged by this act.

## SCA-006 Lane B close-out (B1, B2, B3, B7)

Per the proposal ("Administrative grant", "Records not opened"), the SCA-006 Lane B items this
packet covers are closed out here, not by editing the accepted SCA-006 snapshot
(`_ScopeChange/SCA-006_2026-09-25_1912/`), its `RUN_SUMMARY.md` §6 or either `_LATEST.md` under
`_Decomposition/` and `_ScopeChange/`:

| Item | State after this act |
|---|---|
| B1 — PROJECT_SETUP for DEL-08-06 and DEL-10-13 | DONE — two folders, 12 files; both `_STATUS.md` created at `OPEN` (`TASK+preparation`); minimum fileset PASS ×2. Re-audit COV-003/004/073/074 RESOLVED |
| B2 — dependency rows for the new deliverables and the SOW-097..100 anchors | DONE — 22 rows added (4 new-folder ANCHOR, 2 ANCHOR appended to DEL-04-03 and DEL-08-03, 16 EXECUTION E-P84..E-P99), with mirrors; 74/74 IN items traced. Re-audit COV-080 RESOLVED |
| B3 — re-quote DEP-09-06-003 and DEP-10-03-003 | DONE — both refreshed to the revision-1.6 DEL-08-01 Description; 127/127 ACTIVE EXECUTION quotes verbatim. Re-audit COV-075/076 RESOLVED |
| B7 — re-pin 63 `_CONTEXT.md` and 66 `_REFERENCES.md` to revision 1.6 / PRD v2.4 | DONE — 129 paths, with add-on C correcting the DEL-04-03 and DEL-08-03 covers bullets. Re-audit COV-077/078 RESOLVED |
| Re-audit (add-on V) | DONE — `_Evaluation/DecompCoverage/COV_D101_POSTSETUP_2026-09-26_1651/`, 0 BLOCKER, `overall_status` `WARNINGS` |
| `_Evaluation/DecompCoverage/_LATEST.md` | MOVED to `COV_D101_POSTSETUP_2026-09-26_1651` (condition "0 BLOCKERs" met) |
| B4 — Scope of Work contracts (including first contracts for DEL-08-06 and DEL-10-13, node K2) | OPEN — outside this packet |
| B5 (DEL-00-03 SPEC premise), B6 (tier-0 `pec.yaml` tool entry, node K3), B8 (additive API schema fields) | OPEN — outside this packet |

## Re-audit snapshot (immutable)

| File | SHA-256 |
|---|---|
| `Brief.md` | `538f738eab2b94b96d661933ff5b25e8bfd0234ca148f520047fbf872d74dba5` |
| `Decision_Log.md` | `ebad352f2d9497915fb8e471e0e0bc52578234716cbe15762e0fe19627eba09c` |
| `Decomp_Coverage_IssueLog.csv` (78 rows) | `36da6ac7c8583329ad6284c68be772cb7f2893487fdbce0a029721996d23342f` |
| `Decomp_Coverage_Matrix.csv` | `9f9bc2f4231b74a39b47c29373cff825b8dd5835e493aff614cb7f04c2b3c83c` |
| `Decomp_Coverage_Report.md` | `3d84c97b031b1ef1c1dee5daaa33541901d04c148d4ebf669f116dfda8c5ec82` |
| `PrePost_Comparison.md` | `ea902b64fd1285ad4a05aaed1b9629d00118d9ce0eb0c457f3a9556c158af4e9` |
| `QA_Report.md` | `ab5ce75aaa365ec6d5894e4499bd0b85b90f9e3aeb0b7bcdcaae1563e150e5e8` |
| `RUN_SUMMARY.md` | `0b697514f08519a05c39b725b1b7308e9c4a2be5fa85745dd28d553e4f746b45` |
| `coverage_summary.json` | `e9090ac3f3fd7574ca120077f8e76037b81cb3cf7450b3b2a951e7d617392439` |
| `inventory.json` | `b741735d0a8da7d07d6adeca5fe84e69f5a80f4a5d3940354da9d7c28f6ccda3` |
| `structure.json` | `1359f9a1d1d1ed5c344bef40ad5b66ba66bf11f86bbd7744270ee16d04cf73a5` |

The snapshot has not been independently reviewed beyond the manager's check of its counts and
the files' presence; the product bytes it audited are the independently verified ones.

## Residuals (recorded, not repaired here)

1. **Human-owned Notes line (re-audit COV-076, EXPECTED_CONSEQUENCE).** `_COORDINATION.md`
   L225–227 still names revision 1.5. The ruling (question 4 (a)) authorizes HELP_HUMAN to replace
   it with the with-K1 text in this PR now that the verifier has passed K1 (preimage
   `95ebe344…8a90c`, unchanged at the candidate and on `origin/main`). This act does not touch it.
2. **Stale Lane B descriptions outside this grant (re-audit COV-077, EXPECTED_CONSEQUENCE).**
   `_Decomposition/_LATEST.md` (L35 "no folders yet"; L53–55), `_ScopeChange/_LATEST.md` L15–19
   and the SCA-006 state fields still list B1/B2/B3/B7 as open. None is opened by D-PEC-101; this
   close-out is the record. They claim less than the evidence, not more.
3. **Other audit notes carried at INFO:** 26 D-GOV-48 XRG-013 warnings (owner defers; D-PEC-101
   forbids action); SCA-006 lacks the later-contract `AdjustedAuditState` field (edition drift);
   revision 1.6 still says PEC's registry row declares `remaining-loop`, which D-PEC-96 removed
   (the auditor kept it at INFO and noted a reviewer could raise it to WARNING).
4. **C-08 classification of DEL-10-13** (proposal findings 4 and 7) waits for node K2; the new
   `_DEPENDENCIES.md` records the observation without classifying.
5. **Later `dependency-extract` runs** would mirror legacy informational downstream bullets
   (the 16 new ones included) into `Origin=DECLARED` rows (proposal finding 5); no extraction ran.
6. **Tool drift on main.** `tools/scaffolding/write_status.sh` changed on main after the act (Root
   PR #968, D-GOV-51; `1857ad59…97bc` → `0bf835f5…`). The K1 writes stand; a K1 `--check-only` on
   post-merge main stops on the pin by design; reproduction is against an `aca930622` export.
7. **Ruling text observation (verifier).** The ruling's Grant paragraph under-lists the
   `projects/pec` and `tools/` changes between `aca930622` and `f392294b5` (it omits
   `docs/STATUS.md`, the D-PEC-101 records and three non-bound `tools/` files). No target, basis
   file or bound tool is affected. Routed to HELP_HUMAN.
8. **Loop records.** The register-row status after merge, the central receipt, the work graph and
   `docs/STATUS.md` / `README.md` are HELP_HUMAN's records under D-PEC-88; MEMORY rows are not
   opened (proposal, "MEMORY rows"). This act writes none of them.
9. **Brief portability (verifier note 6).** The child briefs use absolute machine paths; future
   briefs should use `{REPO_ROOT}`-relative anchors.

## Disclosed deviations (accepted by HELP_HUMAN as recorded)

1. The `rely-for-production` preflight ran after the K1 and K4 fan-in commits (16:31:49 MDT); the
   register was empty and identical at every commit, so the outcome could not differ. The V fan-in
   preflight ran before its fan-in.
2. The postimage verifiers used a `f392294b5` pre export (and a post export excluding the run
   root and brief copy) instead of an `aca930622` export; all 161 targets and basis files are
   identical at both commits, and the verifier reproduced byte-identical verifier output with an
   `aca930622` pre export.

## Execution disclosures

- **Forced interim handbacks.** The host twice forced this manager to hand back while the
  background verifier ran; both interim reports went to HELP_HUMAN, which relayed the verifier's
  verbatim verdict (`73b23f35…005c`) and the instruction to resume. No work was lost (every step
  was committed and pushed).
- **Auditor boundary note.** The V auditor ran `git fetch -q origin` (updating only the
  remote-tracking ref) and created and deleted one temporary file under `/tmp`; it disclosed both.
- **`--repo` argument.** Passed as the literal repository root; `git rev-parse --show-toplevel`
  printed the same path.
- **Hold targets.** `checks/hold_targets.txt` named the audit folder by its stem for the first
  three preflights and by its actual name for the last (`checks/41_…`).

## Rollback

- **Before merge:** close the PR and discard the branch and worktree.
- **After merge (owner direction):** a revert PR of this act restores the 149 modified preimages
  (129 K4, 20 K1), removes the two new folders (12 files) and restores
  `DecompCoverage/_LATEST.md` `f8469f88…a9dea`. The `COV_D101_POSTSETUP_*` snapshot and this run
  root stay as non-current evidence, with a rollback note appended here. No history reset; no
  silent downstream repair. HELP_HUMAN's Notes (a) commit is its own to revert.

## Not claimed

No CHECKING, ISSUED, artifact acceptance, readiness or reliance. Nothing here prompts about CHECKING.
