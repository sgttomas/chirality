# Verifier verdict 03 — packet review

Reviewer: fresh read-only `pec-reviewer` TASK (agent `aec64367e74cc5052`), `claude-opus-5-5`, high reasoning; brief `VERIFIER_BRIEF.md` (`2f7abd50…4af`); D1P.md `d1cdf4e3…c1f1` and COMMON.md `51b70e46…b311` confirmed. Reviewed at branch head `c4f9075b9`. Transcribed by WORKING_ITEMS from the reviewer's hand-back (findings as given; the "checked" section condensed); the manager's dispositions follow.

**Boundary disclosure by the reviewer.** It ran `git -C REPO fetch -q origin` once (not on the brief's read-only list); that updates remote-tracking refs only (`origin/main` read `78e74f590` before and after). Nothing else was written; its own `mktemp -d` directory was removed.

---

**Verdict: FAIL.** Two findings are BLOCKING. Both can be fixed in the draft's text or its ledgers. The act machinery, the hashes, the checks and the lapse structure all hold up.

## Findings

1. **BLOCKING — false statement in the grounds for owner question 4(a) (L321).** "every current PEC contract pins `189f205ff`": at `6c6cc1b00` only 11 of 36 production contracts pin `189f205ff` (DEL-01-01, 01-06, 02-03..02-09, 08-06, 10-13); 12 pin `@11a494e9a` (both targets, DEL-01-05, 03-06, 04-02, 04-03, 08-01, 08-03, 08-04, 10-01, 10-10, 10-11), 11 `@3623b958b`, 2 `@65955cceb`. Repair: state it truly, e.g. "every contract written since SCA-006 checkpoint 3 (11 of 36 at `6c6cc1b00`, plus the eight S4 candidates) pins `189f205ff`" (all 8 S4 candidates checked).
2. **BLOCKING — some hunks are not premises under the rule, yet are presented as premise-only.** Rule 3 (text "already stale since SCA-004" is reported, not changed); rule 1 (true when accepted). Add-on P P01 (objective warrant; ledger cause "first made false by SCA-004 (revision 1.4)"); add-on P P02 (basis note; "first made false by the SCA-004 re-pin 1c6ecc6d9"; only its last sentence is a minimal consequence of P03/P04); DEL-00-03 SOW P02 first sentence (ledger WHY: "was already stale at acceptance (1c6ecc6d9 re-pinned to 1.4 on 2026-08-03)"; not in the same sentence as the rebind). The draft still calls every hunk premise-only (L7, L172); L85 labels DEL-00-03 P02 only "consequence of P01"; the departure is never named or put to the owner. Repair: (a) cut back to the minimal consequence and report the rest; or (b) disclose as a named reading (new 4(c)) and stop calling them premise-only.
3. **NON-BLOCKING — the owning-workflow account overstates conformity (L32).** In the 2026-08-09 route the candidate was REVIEWed before it became current; under ruling A the new bytes replace the accepted ones before any REVIEW, and R1 would review them only afterwards. Repair: say so; optionally offer a pre-act REVIEW variant.
4. **NON-BLOCKING — R1 and R2 underspecified (L153–155).** R2 asks only for `ACCEPT_EXACT_BYTES`; the prior DEL-00-01 act also carried AC-007's two confirmations, and the DEL-00-03 acceptance satisfied AC-011 — R2's words should cover these. R1 grants nothing now; say what selecting it records (e.g., a graph node for a later REVIEW packet) as distinct from R3.
5. **NON-BLOCKING — missed downstream consequence (L164).** DEL-01-05 `ScopeOfWork.md` L72 (TBD-005) reads "accepted `ADR-PEC-V2-001`"; once the ADR acceptance lapses, that wording goes stale. List it.
6. **NON-BLOCKING — stale-records list inexact (L166).** The scan's hits include `TM-PEC-014_SPEC_CURRENCY_2026-08-09/REVISION_01_RF-002_RF-003_2026-08-09/DEL-00-03_REVIEW_CHECKLIST.json:75` (old AC-003 text), omitted; DEL-00-03 `_REVIEW.md`, listed, is not a scan hit (it does quote the old AC-003 text).
7. **NON-BLOCKING — SPEC34 notice account incomplete (L47).** The notice says such a deliverable is "surfaced for a human ruling that records them, or for the reversal"; the draft drops "or for the reversal". Add as disclosure only, no prompt.
8. **NON-BLOCKING — ambiguous statement (L126).** "The only 'daemon' (L128) and 'cmux' (L128) mentions are gone" — the candidate SPEC still names cmux (L82, L140, L161, as deferred) and says "no daemon" (L171). Repair: "the preimage's daemon/cmux premise at L128 is replaced; the new text names them only as deferred or absent."
9. **NON-BLOCKING — evidence file trimmed but not disclosed (L330).** `evidence/run_main/scan_external_quotes.out` has 2,305 lines vs 41,596 raw; the 39,291 `KEPT` lines were dropped; everything else identical, including SUMMARY. Disclose.
10. **NON-BLOCKING — publication hygiene.** `SHA256SUMS` omits `VERIFIER_BRIEF.md` (committed later); regenerate at the end. L38, L276, L350 refer to `VERIFIER_VERDICT_*.md`, none present at `c4f9075b9`; ensure they exist before publication.
11. **NON-BLOCKING — main has moved.** `origin/main` is `78e74f590`: `D-PEC-102` ruled (A + M) and published. The status line (L3), L20 and L168 are true as observations at `6c6cc1b00`; refresh or annotate at publication. All 18 pinned files and all 4 preimages are byte-identical at `78e74f590`. The D-PEC-102 ruling records the owner accepting a lapse with no review opened — relevant context for question 3; present it neutrally if at all.
12. **NON-BLOCKING — add-on P framing could be sharper (L172, L318).** D1P's override says the packet touches "only the named artifacts and, if needed, DEL-00-03's `ScopeOfWork.md`"; question 2 recommends P without noting it goes beyond that touch limit. Otherwise honestly framed.
13. **NON-BLOCKING — minor wording.** The L12 "quote" joins two table cells with an em dash (not verbatim; mark as composed). On L20's `8f02609b5` statement the draft is correct (the commit touches 0 DEL-00-03 files); it could add that SCA-005 `Propagation_Plan.md` L964 makes the same miscitation.

## What was checked (condensed)

- All four candidate hashes equal the grant table, `targets.json` and `apply_d1p.py`'s TARGETS; preimages match at `6c6cc1b00`, `189f205ff` and current main; all 18 pins match (first five also at `189f205ff`); `189f205ff` is an ancestor of `6c6cc1b00`; between them PKG-00 changed only in DEL-00-02 `_STATUS.md` (`5066f895c`) and six contexts/references (`62230fa46`). Every aid hash, basis-table hash and method-source hash matches. `SHA256SUMS` verifies (coverage = tracked files minus itself and `VERIFIER_BRIEF.md`).
- `build_apply_d1p.py --basis 6c6cc1b00` re-render byte-identical (`e95c6e26…ed44`); code reading agrees with the stated failure semantics (inventory skips symlinks — minor).
- Own export: `test_apply_d1p.py` `RESULT PASS 24/24`; `render_candidates.py` `RESULT PASS fails=0`; `run_d1p_checks.sh` `OVERALL PASS`, `SUMMARY.out` byte-identical to the committed one; checklists as tabled.
- Records: both deliverables `CHECKING` via the D-PEC-72 override; acceptance records as quoted; no DEL-00-01 SOW acceptance found; owning-workflow records check out; register at `6c6cc1b00` as stated; D-PEC-99 Part B has no D1 item; no `Dependencies.csv` row references any target; SCA-005/006, D-PEC-90, D-PEC-94 quotations verbatim; reliance evidence 10× ALLOW.
- Nothing asks about CHECKING; no lifecycle change; REVISE disclosed in one line; R1/R2/R3 offered, not assumed; no ruling recorded that did not occur; observation commit and pin present.

---

## Manager dispositions (WORKING_ITEMS)

1. **Accepted; repaired** (question 4(a) now says: every contract created or rebuilt since SCA-005 — 11 of 36 at `6c6cc1b00` — pins `189f205ff`, as do the eight `D-PEC-102` candidates; 12 still pin `11a494e9a`, including both targets).
2. **Accepted; repaired.** Add-on P: option (a) — the objective-warrant and basis-provenance hunks are dropped and reported (see verdict 02, disposition 2). DEL-00-03 SOW P02: kept, because the rebind must restate that paragraph and its first sentence ("names revision 1.3 as the accepted `current_basis`") would otherwise contradict the rebound basis in the same paragraph; it is now labelled in the draft as a consequence of the rebind that also corrects text stale since SCA-004, and disclosed in question 4(a). The draft no longer describes that correction as a premise.
3. **Accepted; repaired** (the owning-workflow account says the new bytes land before any REVIEW; the Amend option names a pre-act REVIEW variant).
4. **Accepted; repaired** (R2 states the owner's words must cover AC-007's two confirmations and AC-011; R1 records a graph node for a later REVIEW packet, distinct from R3).
5. **Accepted; repaired** (DEL-01-05 TBD-005 listed).
6. **Accepted; repaired** (the TM-PEC-014 checklist JSON added; `_REVIEW.md` described as a non-hit record that quotes the old AC-003 text).
7. **Accepted; repaired** (disclosure only).
8. **Accepted; repaired.**
9. **Accepted; repaired** (disclosed; the raw file is reproducible with the runner).
10. **Accepted; repaired** at publication (`SHA256SUMS` regenerated; verdict files present).
11. **Accepted; repaired** (the draft records the recheck at `78e74f590`, the `D-PEC-102` ruling and publication, and that no pin or preimage moved; question 3 mentions the D-PEC-102 precedent neutrally).
12. **Accepted; repaired** (question 2 says P goes beyond the brief's touch limit and is for HELP_HUMAN to present or withhold).
13. **Accepted; repaired** (the L12 citation is marked as composed from two cells; the SCA-005 L964 miscitation is noted).
