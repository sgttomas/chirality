# Verifier verdict 01 — DEL-00-03 SPEC and Scope of Work (`MODE=VERIFY`)

Reviewer: fresh read-only `pec-reviewer` TASK (agent `ab48cb9eca5f17290`), `claude-opus-5-5`, high reasoning; brief `VERIFIER_BRIEF.md` (`2f7abd50…4af`). Reviewed at branch head `c4f9075b9` (observation `6c6cc1b00`). Transcribed by WORKING_ITEMS from the reviewer's hand-back; the manager's dispositions follow the verdict.

---

**VERDICT: FAIL.** There is one BLOCKING finding. It is a one-phrase fix in the draft proposal and needs no change to either candidate. Both candidates passed every mechanical check. The hunks are premise-only, true at `189f205ff` / `6c6cc1b00`, and I found no SCA-005 or SCA-006 premise left in place in the named or reviewed loci.

This was a read-only review. I ran every tool on my own `git archive 6c6cc1b00` export under `mktemp -d …/scratchpad/d1pv.uhagq5`, with `TMPDIR` set to it. The export had the candidates copied in; the directory is now removed. REPO `git status` is clean. All 95 `SHA256SUMS` entries verify.

## Findings

1. **BLOCKING — a false ground in owner question 4(a).** Draft L321 says "every current PEC contract pins `189f205ff`." At `6c6cc1b00`, of the 36 `*/1_Working/*/ScopeOfWork.md` files only 11 pin `189f205ff` (the S2 seven, DEL-02-08, DEL-02-09, DEL-08-06, DEL-10-13); 12 pin `11a494e9a` (including DEL-00-01 and DEL-00-03), 11 pin `3623b958b`, 2 pin `65955cceb` (`grep -h '^decomposition_basis' */1_Working/*/ScopeOfWork.md | sed 's/.*@//' | sort | uniq -c`). It is a stated ground for a reading the owner is asked to confirm and makes the rebind look like the norm. Repair: reword (e.g., every contract created or rebuilt since SCA-005 — 11 contracts — pins `189f205ff`, as do the S4 draft candidates) or drop the clause; the other ground (AC-002, AC-003, AC-005) is true and sufficient.
2. **NON-BLOCKING — wrong section locator.** Draft L59 row P03 says "PRD §9 carries 49 rows"; PEC-SVC is PRD v2.4 §10; §9 carries 43 rows and §§9–10 carry 49 (the count 49 is correct). Repair: "PRD §§9–10".
3. **NON-BLOCKING — REQ-004 and AC-004/VER-004 now point at different bases, undisclosed to the owner.** REQ-004 asks the seed to state the basis "it was born from" (revision 1.3 at `11a494e9a`); AC-004/VER-004 require the stated basis to equal the frontmatter (after the rebind, revision 1.6 at `189f205ff`) "or a later accepted successor". The SPEC meets both only if AC-004's "statement" is read as the premise-amendment note (SPEC L11–19). Mentioned only in "Loci examined". Repair: one sentence in question 4(a).
4. **NON-BLOCKING — the FORBID check reaches beyond the rule, bearing on REQ-001.** `verify_d1p_quotes.py` L115 forbids "at the basis" anywhere; the preimage REQ-001 would fail it with or without the rebind. The REQ-001 rewording is defensible as a consequence of the rebind and disclosed, but the tool would have forced an edit anyway. Repair: state that REQ-001 changed because of the rebind, not the check; consider limiting FORBID to hunk `post` texts in future packets.
5. **NON-BLOCKING — suggested disclosure for reading (a).** The accepted pair already mixed bases: `_REVIEW.md` L55–56 shows the 2026-08-09 rerun used revision 1.4 while the SOW frontmatter bound 1.3; preimage SPEC §6 "94: 72/14/8" are revision 1.4 counts and preimage SOW CLM-005 "71/14/9" are revision 1.3 counts. This supports the rebind and belongs in 4(a). Reading (a) goes beyond SCA-006 §B4's scope for DEL-00-03; the draft does disclose it (the P01 hunks are labelled "reading (a)"; the "Amend" option explains the coupling).
6. **NON-BLOCKING — minor asymmetry in role summaries.** P15/P18 extend PKG-04/PKG-08 roles; P19 keeps PKG-10's "Release proof and metrics" although revision 1.6 §4 names "the reliance-advertisement gate"; the reason given is acceptable. CLM-006's "in its revision 1.3 wording" is true (S17) but reads oddly; no change required.

## What was checked (condensed from the reviewer's report)

- Byte identity: `render_candidates.py --only DEL-00-03_SPEC DEL-00-03_SOW` exit 0, `RESULT PASS fails=0`; SOW 15 hunks `a6b57d3f…8156`, SPEC 22 hunks `f84c067b…f617`; preimages identical at `189f205ff` and `6c6cc1b00` and equal to the owner's `ACCEPT_EXACT_BYTES` in `_REVIEW.md` L32–37 and L149–154. `origin/main` had moved to `78e74f590`; no PKG-00, `_Decomposition` or PRD file changed after `6c6cc1b00`.
- Facts checked independently: 49 requirements / 11 invariants; ScopeLedger 100 rows 74/18/8 (94, 71/14/9 at revision 1.3); 68 deliverable rows with the four retired; DEL-02-08/09, DEL-08-06, DEL-10-13 present; SOW-029/035/037/087 OUT (IN at 1.3); SOW-095/096 SourceRef PEC-RCN-002; SOW-097..100 mappings; PEC-K-03 row matches PRD §6 and brief rule 7; PRD §12 P3/P4 and the gate; §7.1 WorkGraph/WorkNode; revision 1.6 §4 roles and §5 ranges; §10 OI-002/006/008 paraphrased accurately; CLM-009 re-quote verbatim at 1.6; `189f205ff` is the PR #954 merge. All 235 identifiers in the SPEC candidate resolve at the pin apart from the pre-existing DAG constraints C-05, C-06.
- Completeness: "PRD v2.2" survives in the SPEC only in Born-from; daemon/cmux only in negated/deferred statements; SOW "46"/"PRD v2.2" only in verbatim quotations or own-voice history; nothing outside the hunks changed.
- SOW `MODE=VERIFY` items 1, 3, 4, 8, 9, 13, 16, 18–21: `PASS format=SOW_V1`; checklist twice byte-identical `522917133070…fe11` (preimage `1c4d4927…` matches `_REVIEW.md` L52; diff is AC-003 text, line numbers and source hash only); boundary exit 0; IDs kept; AX-009 complete.
- Coherence with the amended SOW: AC-002, AC-003, AC-005 resolve; AC-004 through the premise note (finding 3); AC-006/007 unchanged; AC-008 decides nothing; AC-010 uses "work-domain packages"; AC-011 correctly shown as lapsed.
- Verifiers: quotes `RESULT PASS 45/45`; state claims `RESULT PASS 89/89`; every presented SOW quotation has an entry; weak entries noted (Q01/Q11 "v2 SPEC seed", Q10 partial, disclosed).
- No lifecycle/acceptance/readiness/CHECKING claim; no D-PEC number ≥ 90 in the candidates; nothing built around verify-before-rely; the uniform note matches the brief after whitespace normalization; no trailing whitespace; final newlines. The DEL-00-03 acceptance-lapse account is accurate (quotes `_REVIEW.md` L168–169 verbatim).

---

## Manager dispositions (WORKING_ITEMS)

1. **Accepted; repaired in the draft** (question 4(a) now states the true count and the post-SCA-005 practice; the AC-grounds stand on their own).
2. **Accepted; repaired** ("PRD §§9–10").
3. **Accepted; repaired** (question 4(a) states the REQ-004 / AC-004 split and how the SPEC meets both).
4. **Accepted; repaired** (the draft states REQ-001 changed as a consequence of the rebind, and discloses the FORBID reach as a check-aid limitation; the aid is not changed now, because it is cited with its hash).
5. **Accepted; repaired** (the mixed-basis history is added to question 4(a)).
6. **Noted; no change.**

No candidate changed in response to this verdict.
