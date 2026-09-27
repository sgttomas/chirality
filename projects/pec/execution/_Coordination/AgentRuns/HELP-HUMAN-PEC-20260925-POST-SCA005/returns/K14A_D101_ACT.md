# Return — K14A D-PEC-101 act (WORKING_ITEMS)

Brief `briefs/K14A_D101_ACT.md` (`b2537971…d2ec`). Branch `claude/pec-d101-act`. PR
**#976** (https://github.com/sgttomas/chirality/pull/976), against `main`, not merged. Run root
`projects/pec/execution/_Coordination/REV16_CURRENCY_SETUP_D101_2026-09-26/`; its `MANIFEST.md`,
`VALIDATION.md` and `HANDOFF_STATE.md` carry the detail.

## Result

- **K1** (TASK `TASK+preparation`, `gen_d101_k1.py --act-date 2026-09-26`, once, 16:25:08 MDT;
  commit `345266081`): exit 0; report byte-identical to preparation `genK1.tsv`; 32/32 postimages
  as tabled; `all_K1` `483ec239…0234`, `modified_K1` `186d9c72…6e8f`, `created_K1` `e72fc7e9…e887`.
- **K4 with C** (manager, `gen_d101_k4.py --covers`, once, 16:27:10 MDT; commit `62230fa46`):
  exit 0; 129/129 postimages as the A+C column; `all_A+C` `01bd1f7b…6b3d`.
- **Finite verification:** every row gives the required result (strict registers exit 1, 0 ERROR,
  the same 26 XRG-013, 0 DRB-008, 68 registers / 285 rows; closure 127 edges / 68 nodes / 0 SCCs,
  PASS; quotes 127/127; COV-080 closed; K1 verifier PASS; K4 verifier on the original export exactly
  one FAIL, containment 149 vs 129, the 20 extras being K1's MODIFY set; schema VALID ×6; fileset
  PASS ×2; harness and receipts identical; byte identity 161/161; containment PASS; whitespace clean).
- **Independent verifier:** `VERIFIER_VERDICT_01.md` (`73b23f35…005c`) **PASS WITH NOTES; K1
  passes; K4 with C passes; no BLOCKING**; same-day reproduction on a fresh `aca930622` export,
  161/161 byte-identical. The verifier passed K1 as recorded in commit `39e30684d`. Seven
  non-blocking notes disposed in `VERIFIER_VERDICT_01_DISPOSITIONS.md` (records-only repairs).
- **Add-on V:** `_Evaluation/DecompCoverage/COV_D101_POSTSETUP_2026-09-26_1651/` (11 files): 0
  BLOCKER, 3 WARNING (pre-existing Check-6), 73 INFO, 2 EXPECTED_CONSEQUENCE; `overall_status`
  `WARNINGS`; coverage 100 %; prior COV-003/004/073–078/080 RESOLVED; no DEFECT. **Pointer moved**
  (`DecompCoverage/_LATEST.md` `f8469f88…a9dea` → `e5ad5190…c8e`; commit `674de6a90`).
- **Merge:** `origin/main` `17da1a013` merged at `dc68b5afd`; no act path changed on main; post-merge
  strict registers and closure identical, 161/161 bytes, containment with V PASS.
- **Containment:** the 161 granted paths with their tabled act, the run root, the audit folder and
  pointer, this return and the brief copy; nothing else. `_COORDINATION.md` untouched.

## For HELP_HUMAN

1. Apply the Notes (a) replacement of `_COORDINATION.md` L225–227 in PR #976 (preimage
   `95ebe344…8a90c`, unchanged at the candidate and on `origin/main`; re-audit COV-076 records the
   line as the expected pending consequence).
2. The PR needs its own fresh-context review of the complete candidate diff (including your Notes
   commit) and required CI before merge; the act's verifier reviewed `b56dad37d`, and the later
   commits are records, the V audit folder, the pointer and the merge.
3. Disclosed deviations you accepted are recorded in `VALIDATION.md` and `HANDOFF_STATE.md`.
4. Ruling text observation from the verifier: the Grant paragraph under-lists `aca930622` →
   `f392294b5` changes (`docs/STATUS.md`, the D-PEC-101 records, three non-bound `tools/` files); no
   preimage affected.
5. Stale Lane B wording in `_Decomposition/_LATEST.md` and `_ScopeChange/_LATEST.md` (re-audit
   COV-077) is outside D-PEC-101; the close-out is in `HANDOFF_STATE.md`.
6. Register-row status after merge, the receipt, the work graph and `docs/STATUS.md`/`README.md`
   remain yours; no MEMORY rows are opened.

## Not claimed

No CHECKING, ISSUED, artifact acceptance, readiness or reliance claim.
