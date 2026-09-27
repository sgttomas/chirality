# Review 01 of PR #990, transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `243078f014a8da1562a75ae1a82b483a33621a43`. The repairs listed under Disposition, this file, the `SHA256SUMS` update and a merge of `origin/main` follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `38fced8861b78a81369de36475a1ce36d8552438c0ace729a37b37a8a697f69a`.

## Report (verbatim)

## PR #990 review (S4 SOW currency packet, provisional D-PEC-102), head 243078f01

**Verdict: PASS WITH NOTES.** Nothing blocks. There are two NON-BLOCKING disclosure gaps in the draft and five NOTES. The only CI failures come from the known "Update the PR base" failure.

I modified no file, made no git writes and checked nothing out. I ran `git fetch` and `gh`, both read-only. I made one mistake: one early `mktemp -d` ran before I had set `TMPDIR`, so it landed in `/var/folders/...`. I deleted it straight away and empty. My scratch directory under the session scratchpad (`rev.unfeQO`) is now deleted too. The worktree is clean.

### 1. Reproduction
- **Checks at current main.** `run_s4p_checks.sh` at `origin/main` `3e861f53c` (observation `125cfacc1`, `TMPDIR` set to my directory) gives **OVERALL PASS**. The results:
  - the act: check-only 0, apply 0, second run refused with 1;
  - containment: 8 files, all `ScopeOfWork.md`;
  - validate, checklist and boundary pass for all 8;
  - quotes 740/740, state claims 1144/1144, IDs 57/57, S2 scan stale=0;
  - strict (exit 1, 0 errors, 26 XRG-013 warnings), harness and receipts are identical before and after;
  - quote currency 127/127, whitespace clean, fault injection 9/9.
- **Match with the recorded evidence.** My summary equals `evidence/run_main/SUMMARY.out` apart from the basis line. All eight checklist JSONs are byte-identical to the evidence copies and match the draft's hashes at L516–523.
- **Main has moved.** Since `d385b6a19`, main has changed only `projects/chirality-piping` (PR #983).
- **Negative controls** (`negative_controls.sh` at `3e861f53c`): 6/6 tripped.
- **`shasum -a 256 -c SHA256SUMS`:** all 107 files OK, and the list covers every file in the prep folder. The draft is `cc01a5fd…b1ba` and `apply_s4p.py` is `2b6792fe…4869`, as stated.
- **The grant.** I recomputed every hash in the grant table:
  - the 8 preimages hash as tabled at `125cfacc1`, `d385b6a19` and `3e861f53c`;
  - the 8 postimages equal the candidate files;
  - all 19 pins match at `125cfacc1` and at main;
  - the script holds exactly 35 distinct hashes (8 + 8 + 19), all as tabled.
- **The act script.** Apart from its hashes, `apply_s4p.py` differs from the D-PEC-100 `apply_s2p.py` only in targets, pins, the `.s4ptmp` suffix, the run-root prefix and its comments.
- **Extra check: K2 landing first.** I ran the full suite on top of the D-PEC-103 act branch (`claude/pec-d103-first-sows-act`, `5fc8424e1`). It gives OVERALL PASS, and the only change is that the consequence scan reports kept=26. That branch and PR #990 touch no common path. `apply_k2.py` and `apply_k2_c8.py` pin none of the S4 targets, and S4 pins none of K2's targets. Neither K2 contract cites an S4 local ID. The draft's "either act may land first" (L255) holds.

### 2. Substance (MODE=VERIFY)
- **DEL-04-01: seven components.**
  - PRD v2.4 PEC-ORI-001 (PRD L325) and revision-1.6 SOW-004 both name terminal completion. At revision 1.4 (`65955cceb`), SOW-004 listed six, which confirms CLM-002's history.
  - "Seven" and "no eighth" appear consistently in REQ-001, AC-001, VER-001/002, CON-004, the trace table and AX. In DEL-04-02 they appear in CLM-015, REQ-011, AC-011 and AX-008. DEL-04-03 CLM-011 and DEL-08-04 cite `DEL-04-01/REQ-001` without a count.
  - No stale "six components" text remains in any of the eight.
- **DEL-08-03 CON-007** (candidate L352) now matches DEL-04-03 CON-005 and TBD-005/REQ-023. It chooses nothing and leaves the absence and degraded questions to the owner.
- **DEL-04-03 envelope.** REQ-016 says the envelope is declared "beside the three-field stamp of REQ-001 and is not a stamp field". This is grounded in the SOW-097 Notes ("distinct from SOW-006 stamping") and in CLM-019. REQ-001, REQ-005 and REQ-008 are byte-identical to the preimage. Owner question 3(b) puts the reading to the owner.
- **Access classes and SOW-097/098.**
  - DEL-08-01 REQ-003 names four classes and REQ-008 makes `agent` read-only, matching PRD §8 L310–315.
  - CON-003 correctly leaves open whether the read list is exhaustive.
  - DEL-04-03 frontmatter is `[SOW-006, SOW-007, SOW-097]` and DEL-08-03 is `[SOW-043, SOW-098]`.
- **No open item decided by assumption, and no reliance, release or readiness claim.** A scan of all eight finds no readiness claim. "Verify-before-rely" appears only as a disclaimer or a quotation.
- **Verifier rigour.**
  - The quote verifier checks both sides. Every one of the 740 entries carries a commit (714 at `125cfacc1`), and none falls back to the working tree.
  - The state-claim verifier reads only named commits (1144 claims, 9 kinds) and also matches the claim text in the candidate.
  - Weak points: presence is checked anywhere in the candidate, not at a location, and some quotes are very short (for example "the current corpus").
  - I recomputed a sample independently: DEL-08-02 is `CHECKING` at `125cfacc1`; `schema.json` is `0a4e4273…5c67`; DEL-04-03's first bytes at `fb6442f47` cite revision 1.2 and `ea6b4b5d0` cites 1.3; all eight deliverables are `INITIALIZED` at main.

### 3. Part B carry-forwards (exhibit `69b646f8…f45e` at main)
- **DEL-04-01.**
  - Both S4 clauses appear verbatim, once each, at L281 and L289.
  - Both identical Gate lines appear, twice in total, at L283 and L291.
  - The three added verification sentences appear verbatim.
  - L277 states that the gates still bind.
  - The trace table (L299–344) maps all 46 prior REQ-001..015, AC-001..016 and VER-001..015 IDs.
- **DEL-04-02-REM-002 and DEL-04-03-REM-002.** Every replacement text is present verbatim and every replaced original is gone. The E-P33 and E-P34 exhibit blocks are kept. The draft's landing line numbers (L176–180) are correct.
- **The "authored against revision 1.3" imprecision.** The exhibit wording is kept verbatim. Qualifying sentences follow it (DEL-04-02 L20–24, DEL-04-03 L21–25), and the draft discloses the imprecision at L190. This is appropriate.

### 4. Owner-acceptance lapse
- **Disclosure.** The draft quotes `_REVIEW.md` accurately (L94–99): the ACCEPT_EXACT_BYTES of `6f4e8c66…`, the closure state, and "Any SOW byte change invalidates this acceptance…". Owner question 1 (L464) says explicitly that ruling A lets the owner's 2026-08-09 acceptance lapse. The return repeats this (L32).
- **The other seven.** None has an acceptance record. Only DEL-04-01 has `_REVIEW.md`, `Review_Findings.csv` or an `_Evaluation/Reviews` entry.
- **DEL-00-03.** Its `_REVIEW.md` L28–35 reproduces the same joint owner ruling, including DEL-04-01's hash. It applies only the DEL-00-03 lines, so nothing depends on it.

### 5. The draft
- **Grant, lifecycle, rollback and limits** are correct as verified above. No status is touched, and nothing asks about CHECKING.
- **Anchor and stale-quote accounts.** The consequences are real:
  - DEL-04-05 CLM-013 quotes DEL-04-01 REQ-001 and CON-004;
  - DEL-04-05 CLM-012 quotes DEL-04-03 CON-003;
  - DEL-10-11 CLM-014 quotes DEL-03-04 CON-001 and CON-005, and CON-005's "undetermined" wording is gone from the postimage.
  - Every anchor claimed as kept is byte-identical: DEL-04-01 REQ-006; DEL-04-03 REQ-001, REQ-005, REQ-008; DEL-03-04 REQ-003, REQ-007, REQ-013, CON-004, TBD-005; DEL-10-03 REQ-007 and OUT-001; DEL-08-03 REQ-010; DEL-08-01 OUT-001.
- **Verdict 07's text edits.** I re-reviewed the post-verdict-07 word diff (`e09b25efa..243078f01`); it is accurate.
  - The status line matches the register row (reserved, `NOT_PREPARED`).
  - The PR #989 bullet is accurate.
  - The K2 sentence's list of what D-PEC-103 writes matches the ruled register row.
  - The `[sic]` repairs in verdicts 04, 05 and 06 are correct: the bound hash ends `…7ce449`, so "…e449" is right and "…c449" is the slip.

### Findings

**NON-BLOCKING 1: the DEL-04-05 consequence row leaves out REQ-013.**
- **Where:** draft L234.
- The row lists CLM-013, the "six components, no seventh added" text and CON-003. It does not list DEL-04-05 **REQ-013** (main, DEL-04-05 `ScopeOfWork.md` L216, `933c012c…a579`), which says "the six components of the per-loop orientation return and the 'no seventh component' rule are the composing contract's (CLM-013)".
- That is a requirement, and it goes false when S4 lands.
- The S1 candidate (PR #986, `1d85874c1`, L225) also still carries it.
- **Repair:** add REQ-013 to the row, text only.

**NON-BLOCKING 2: the S1 ordering account covers only one direction.**
- **Where:** draft L240, return L61.
- The DEL-03-04 postimage quotes DEL-03-01 CON-005 in full (candidate L257: "every manifest-named feed").
- S1's own draft (PR #986, unmerged, L103) revises that record to "profile-declared feed" and states that DEL-03-04's quotation "goes stale here — for the S4 packet to absorb, or a later one".
- Under either ruling order, DEL-03-04 then carries a stale quotation that neither packet repairs.
- The quote is commit-anchored at `125cfacc1`, so the verifiers stay green; this is a disclosure gap, not a false claim.
- **Repair:** disclose it next to L240, and suggest a later DEL-03-04 currency item for the work graph, as the draft does for DEL-10-11.

**NOTE 3: seven of the eight contracts will say "not yet ruled" once they land.**
- **Where:** DEL-03-04 L391, DEL-04-01 L469, DEL-04-02 L385, DEL-04-03 L23 and L386, DEL-08-01 L214, DEL-08-03 L421, DEL-08-04 L391, DEL-10-03 L446. DEL-04-02 L20 says only "provisional".
- Under each contract's `125cfacc1` observation clause the wording is technically true, but it is false when the bytes land. The D-PEC-100 precedent said only "(provisional `D-PEC-100`)".
- Changing it would need a re-render, so at most disclose it. It is not worth reopening.

**NOTE 4: the review record will describe a superseded contract.**
- After the act, DEL-04-01's `_REVIEW.md` header will still read "EXACT-BYTE ARTIFACT ACCEPTANCE COMPLETE" beside a contract it no longer describes.
- The record is hash-bound and the packet correctly writes no review file.
- HELP_HUMAN may want to record the lapse in the graph or central receipt. Option A's text (L260) could also mention it, though Q1 already does.

**NOTE 5: two draft statements are dated.**
- L255, "its act is next": the D-PEC-103 act is now running.
- L3/L47 anchor to `d385b6a19`, and main is now `3e861f53c` (a Piping-only change).
- Refresh both at publication, as the return suggests.

**NOTE 6: the D-PEC-100 lapse is already surfaced.**
- D-PEC-100 replaced DEL-02-07's owner-accepted contract (`d044499…`; the ACCEPT_EXACT_BYTES record is at DEL-02-07 `_REVIEW.md` L39) without disclosing the lapse.
- The return already raises this (L113). It is outside this PR.

**NOTE 7: the S4 packet does not quote PRD §9.1's count.** DEL-04-05 CLM-002 says "one of six §9.1 requirements", which is stale under v2.4. That is S1's concern.

### 6. Containment and CI
- **Containment.** The diff `125cfacc1..243078f01` touches only the prep folder plus `briefs/` and `returns/S4P_SOW_CURRENCY_PROPOSAL.md`. The brief hashes to `d00a739a…dc67`, as cited.
- **`git diff --check`:** clean.
- **CI at head 243078f01:**
  - pass: `pec`, `harness`, `Harness pre-merge`, `Select PEC coverage`, `Select App coverage`;
  - fail: `Select source coverage`, with `ValueError: Update the PR base: event target base is missing, unavailable or not integrated into head` (base `125cfacc1`, target `3e861f53c`);
  - fail: `Desktop E2E (source mode)`, which fails only on "Require all planned coverage" as a consequence of the first failure;
  - the rest are skipped.
- **"Update the PR base" failure: present.** It should be reported, not repaired. The mergeable state is UNSTABLE.

### Paths
- Draft: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_SOW_CURRENCY_S4_PREP_2026-09-26/DRAFT_D-PEC-102_s4_sow_currency_proposal.md` (at `243078f01`; not checked out)
- Return: `…/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/S4P_SOW_CURRENCY_PROPOSAL.md`
- DEL-04-05 contract (main): `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/ScopeOfWork.md`
- DEL-04-01 review record: `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/_REVIEW.md`

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking. Dispositions:

- **NB-1 (DEL-04-05 REQ-013 missing): repaired.** The DEL-04-05 consequence row and the ordering bullet now name DEL-04-05 `REQ-013`, quoted. HELP_HUMAN has told the S1 preparer, whose DEL-04-05 candidate still carries it.
- **NB-2 (S1 ordering covers one direction): repaired.** A new bullet beside the ordering bullet discloses the other direction: the DEL-03-04 postimage quotes DEL-03-01 `CON-005`, which the S1 draft revises. Under either ruling order, DEL-03-04 would then carry a stale but commit-anchored quotation. It is suggested for the work graph as a later DEL-03-04 currency item.
- **Note 3 ("not yet ruled" wording): disclosed.** A new bullet says the postimages describe the packet as not yet ruled, which is true under their `125cfacc1` observation clause but dated once the act lands. The candidates are not re-rendered.
- **Note 4 (review record after the act): disclosed.** Option A now says DEL-04-01's untouched `_REVIEW.md` will still read "EXACT-BYTE ARTIFACT ACCEPTANCE COMPLETE" for the prior bytes. HELP_HUMAN will record the lapse in the graph and the central receipt.
- **Note 5 (dated statements): repaired.** The K2 sentence now says the `D-PEC-103` act is PR #992. A new source-state bullet records the recheck at `origin/main` `7004eaeda`: only Piping changed since `d385b6a19`, and this review's rerun at `3e861f53c` gave OVERALL PASS. The status line keeps its `d385b6a19` reservation fact, which is still true.
- **Notes 6 and 7: no change here.** Note 6 is carried in the work graph (PR #992) and goes to the owner. Note 7 is S1's, and HELP_HUMAN has passed it on.
- **CI "Update the PR base": repaired by HELP_HUMAN**, by merging `origin/main` into the branch without a rebase.

After the repairs the draft is `3e6943139a7d96ed8158674ec0c138f1b2615516d811324d83e1a92a24d88b81` (was `cc01a5fd…b1ba`), and `SHA256SUMS` is updated to match; all its entries pass `shasum -c`. No candidate, act script, check script or evidence file changed. The manager's return keeps the preparation-time draft hash as history. The repair head needs a fresh review before merge.

*Correction after review 02 (NB-1):* the note-3 disposition first said "seven postimages … (DEL-04-02 says 'provisional')", following review 01's heading. All eight contain the phrase (DEL-04-02 at L385); the draft bullet and this disposition were corrected. The report above is unchanged.
