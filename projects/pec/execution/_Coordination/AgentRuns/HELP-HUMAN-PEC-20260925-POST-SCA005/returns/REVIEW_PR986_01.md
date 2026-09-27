# Review 01 of PR #986, transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `8bdf8f6976367c6c0da1c721fe1cde597007130c`. The S1P manager's repairs (to `025cacba7`) and this file follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `f531385f9c016a14143d4ddd45ef7dd459ff99cc5128666f68cc5602bef99506`.

## Report (verbatim)

## PR #986 review (S1 SOW currency, provisional D-PEC-104), head 8bdf8f6976367c6c0da1c721fe1cde597007130c, against origin/main f0a6159c9

I stayed read-only. I made no edits, no git writes and no checkout. Everything ran on `git archive` exports inside my own `mktemp -d` directory (`…/scratchpad/rev986.CtedM7`, with TMPDIR set to it). I deleted that directory at the end, and the worktree is clean. Paths below are relative to `projects/pec/execution/_Coordination/`: the prep folder is `PEC_SOW_CURRENCY_S1_PREP_2026-09-26/` (P) and the run folder is `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/`.

### Reproduction (all confirmed)
- **Hashes.** Draft `1df935c1…1408`, `apply_s1p.py` `26b677a7…625f` and brief `9718ab73…9f17` all match. `shasum -a 256 -c SHA256SUMS` passes: 156 entries, which is every file in the prep folder except SHA256SUMS itself.
- **Check runner.** `run_s1p_checks.sh <repo> origin/main P <out>` exits 0 with **OVERALL PASS**:
  - the S4 overlay is a no-op for both files;
  - act 0/0/rerun 1; containment is 12 files;
  - validate, checklist and boundary pass ×12; quotes 884/884; state claims 905/905; qualified IDs 44/44; dependency quotes 127/127 before and after;
  - strict, harness and receipts output is identical before and after (strict exits 1 on the 26 known XRG-013 warnings);
  - whitespace clean; fault injection 9/9.
- **Negative controls.** `negative_controls.sh` against origin/main gives RESULT PASS: all 9 controls are caught.
- **Grant table, recomputed independently.** All 12 preimages equal main, all 12 candidates equal their postimages, and all **35/35 pins** hold at f0a6159c9, including DEL-04-01 `98a3a3ec…` and DEL-04-03 `10819cb2…`.
- **Quotes re-anchored to f0a6159c9.** Every 125cfacc1 and 91a2e8407 anchor moved to f0a6159c9 still gives 884/884.
- **Claims re-anchored.** 901/905. The four failures are exactly the ones the draft names: DEL-02-01 S57 and S58, DEL-04-05 S66 and DEL-10-02 S52.
- **All 14 quotations of S4 contracts** (DEL-04-05 Q53–56, Q60–62, Q76, Q77, Q80, Q82; DEL-10-02 Q57–59) are verbatim in the landed text.
- **Every-PR checks and holds.** On a head export, harness self-check and `validate_pec_loop_receipts` both exit 0. The hold preflight returns ALLOW ×12.
- **Containment.** The diff against origin/main adds 159 files, all in P, the brief or the return. `git diff --check` is clean.
- **CI at head 8bdf8f697.** All checks SUCCESS or SKIPPED (pec, harness, Harness pre-merge, Desktop E2E, coverage selectors). The PR is MERGEABLE.

### Findings

**BLOCKING-1 — DEL-01-05's owner acceptance of the contract itself is not disclosed. The draft answers HELP_HUMAN's "check every other S1 target for such a record" incorrectly.**
- On 2026-08-03, under D-PEC-77, the owner ruled: "DEL-01-05 contract fitness: ACCEPT SHA-256 53ba3be3…de53 as the DEL-01-05 production contract". Where it is recorded:
  - `_DECISIONS/D-PEC-77_del_01_05_enforcement.md` L133–150;
  - `DEL-01-05/_run_records/D-PEC-77_ACTIVATION.md` L8 and L12–14 ("accepted the exact `ScopeOfWork.md` bytes above as the DEL-01-05 production contract").
- The DEL-01-05 candidate's own AX-009 (candidate L159) says the same thing: "the bytes the owner accepted as the production contract under `D-PEC-77` on 2026-08-03".
- The draft describes this record only as a `_REVIEW.md` header SOW binding for the owner's "exact-artifact acceptance" (P/DRAFT L116, L278). Its owner question 1 note (DRAFT L275) and the return (returns/S1P… L14, L36, L49) say that A supersedes "an owner-accepted contract", naming DEL-03-01 only.
- Under A, a second owner-accepted production contract is superseded without a review. Mitigations the draft can state: the D-PEC-77 record has no lapse clause, and DEL-01-05's REQ/AC/VER lines are byte-identical.
- **Repair (text only, no bound bytes change):** DRAFT L116, the L275 note, L278 question 4 and the matching return lines. Then regenerate SHA256SUMS.
- My search found no comparable owner acceptance for the other ten targets. The only other hits for prior hashes are verification pins, run records and D-PEC-99 exhibit loci.

**NON-BLOCKING-1 — The DEL-10-02 C-08 wording that D-PEC-103 routed to S1 is neither changed nor dispositioned.**
- The ruled D-PEC-103 proposal (`_DECISIONS/D-PEC-103_first_sows_…md` L184) records this inconsistency: DEL-10-02 calls C-08's force "unconfirmed", while D-PEC-62's ruling and DEL-10-02's `_DEPENDENCIES.md` say "owner-confirmed". It adds "The DEL-10-02 wording belongs to S1."
- The D-PEC-103 ruling (L25–26) records that HELP_HUMAN told the owner the same thing.
- The candidate keeps DEL-10-02 CON-001 (candidate L309, "force is unconfirmed") and AX-003 (L389). The draft never mentions this routed item (no C-08 or D-PEC-103 content beyond L3).
- On substance, keeping the wording is defensible. D-PEC-62's ruling text (L5, L215) confirms only the arithmetic exclusion and leaves the standing-node set "recorded-but-unresolved" (L29). DEL-10-13 CLM-012 also quotes that DEL-10-02 sentence.
- **Repair:** disclose the routed item and its disposition in "Findings for the owner's attention" (DRAFT L118) or put it to the owner.
- Related omission: DRAFT L117 lists the `_DEPENDENCIES.md` "(owner-confirmed at D-PEC-62 ruling)" phrase for DEL-01-05 and DEL-10-10 only. DEL-10-02's `_DEPENDENCIES.md` L22 carries it too.

**NOTE-1 — The option list still offers ruling S1 before S4, which is now impossible.** The "Amend" option at DRAFT L124 includes "rule S1 before S4 (needs a re-prepared DEL-04-05 and act script)". S4 has landed at f0a6159c9, so this path no longer exists.

**NOTE-2 — DEL-10-13's descriptions of the prior DEL-04-05 and DEL-10-02 bytes are not listed among the downstream consequences.**
- DEL-10-13 CLM-007 and CON-003 (its SOW L105 and L178) state, hash-anchored to `933c012cf16b` and `99730e4e85ce` at 125cfacc1, that neither contract mentions "DEL-10-13" or "SOW-100".
- The S1 postimages now name DEL-10-13 and SOW-100 (DEL-04-05 CLM-014, DEL-10-02 CLM-014).
- DEL-10-13's statements stay true as dated observations, but its CON-003 premise is partly overtaken.

**NOTE-3 — One sentence of the authored DEL-03-06 L229 paragraph reads oddly now that D-PEC-65 has filled the cells.** "This contract supplies no evidence for any of those cells, and no statement here may be read as filling them" is accurate. Otherwise the paragraph faithfully covers every element the exhibit directs. The draft's L228→L229 explanation is correct: prior L228 is blank.

**NOTE-4 — The DEL-04-05 REM-003 (1) locus carries more than the item's text.** The verbatim text sits at candidate L20. Lines L21–28 of the same opening locus are C2 pin and hash text, which belongs to S1 currency, not Part B. The DRAFT L94 landing table lists only the bracket resolution and the column placement as authored. It would be clearer to name L21–28 as C2 text.

### Substance confirmed
- **DEL-04-05:**
  - seven components and "no eighth" in CLM-013, REQ-013 and CON-003;
  - CLM-012 and CLM-013 quote the landed S4 text;
  - CLM-002 is correct: PRD v2.4 §9.1 has exactly PEC-ORI-001..007, and SOW-097 belongs to DEL-04-03;
  - all six REM-003 landings are verbatim at L20, L116/118–122, L124, L142, L298, L244 and L334.
- **DEL-01-03 and DEL-01-05:**
  - REQ, AC and VER lines are byte-identical (hash-compared: 10/10/9 and 12/11/9);
  - the only matrix change is DEL-01-03's OUT-003 row, which gains AX-007 (disclosed);
  - DEL-01-03 CON-001 and REQ-003 are kept;
  - DEL-01-05 REQ-007 still reads "pending", CON-002 stays open and the TBD lines are unchanged.
- **DEL-03-01 and DEL-10-02 sibling quotations:** DEL-03-01 CON-005 now reads "profile-declared feed", and DEL-10-02's sibling quotation matches it. This is consistent with the D-PEC-102 proposal L242 (landed DEL-03-04 L257 still reads "manifest-named").
- **Part B:**
  - DEL-03-02 L148/L150 and DEL-03-03 L169/L347 are byte-exact, and the old strings are gone;
  - DEL-03-06 differs from its preimage only at L220, L222–225, L229 and L476;
  - the register cells quoted match the repaired rows at main.
- **DEL-03-01 acceptance lapse:** `_REVIEW.md` L38–41, L194–195 and L203–204 are accurately quoted.
- **Lifecycle:** 10 INITIALIZED and 2 IN_PROGRESS, matching the draft.
- **Readiness and open items:** no readiness or reliance claim; no CON is resolved; nothing prompts the owner about CHECKING.
- **Post-verdict-13 edits:** DRAFT L27, L114 and L313 plus return L45 are all true at f0a6159c9. This includes the four claims, #998 changing WORK_GRAPH.md, and the [E-A22] quotation at PLAN L144.

### Verdict: **FAIL**
BLOCKING-1 is a text-only repair in the draft and return; no candidate, pin or bound byte needs to change. Once it and NON-BLOCKING-1 are fixed and SHA256SUMS is regenerated, I would expect PASS WITH NOTES.

## Disposition (HELP_HUMAN)

Verdict **FAIL**, with one blocking finding (text only). HELP_HUMAN sent every finding and note back to the S1P manager. It repaired them at head `025cacba7`. Its fresh verdicts are in the prep folder: 14 (FAIL, on two new false sentences, since repaired) and 15 (PASS WITH NOTES). In summary:

- **BLOCKING-1 (DEL-01-05's owner acceptance undisclosed): repaired.**
  - The draft, question 1, question 4 and the return now say that A supersedes two owner-accepted contracts: DEL-03-01 and DEL-01-05 (`D-PEC-77`, 2026-08-03).
  - The mitigations are stated: no lapse clause, and byte-identical REQ, AC and VER lines.
  - No comparable acceptance exists for the other ten targets.
- **NON-BLOCKING-1 (DEL-10-02 C-08 wording routed from `D-PEC-103`): dispositioned.** The wording is kept, and the draft says so under "Findings for the owner's attention", with the D-PEC-62 grounds. The DEL-10-02 `_DEPENDENCIES.md` L22 phrase is added to the list.
- **Notes 1–4: applied.**
  - The S1-before-S4 amend path is removed.
  - The DEL-10-13 CLM-007/CON-003 consequence is added.
  - The DEL-03-06 L229 rewording is disclosed.
  - The DEL-04-05 L21–28 lines are labelled as currency text.

No candidate, pin or act-script byte changed; `apply_s1p.py` is still `26b677a7…625f`. The repair head needs a fresh HELP_HUMAN review before merge.
