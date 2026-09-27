# Verifier verdict 05 — re-verification of DEL-08-01, DEL-08-03 and DEL-08-04 after repairs (S4P preparation)

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by the S4P WORKING_ITEMS manager in the foreground. It authored nothing in the packet. Its final report is transcribed below verbatim from its hand-back message.
- **Reviewed head:** `cf23df7df`. Repairs follow in the next commit; dispositions are at the end.

## Report (verbatim)

## Verdict 05: re-verification of DEL-08-01, DEL-08-03 and DEL-08-04 after the verdict 02 repairs (S4P, head `cf23df7df`)

**Overall verdict: PASS WITH NOTES.** All of verdict 02's dispositions for these three are made and hold at their sources. That includes BLOCKING 1: DEL-08-03 CON-007 now matches DEL-04-03 CON-005, REQ-020, TBD-005 and REQ-023. Every mechanical check passes. The only thing to fix is one NON-BLOCKING leftover of the REQ-018 repair: two other records in DEL-08-03 still carry the access-class clause. The rest are notes.

I modified nothing. The only mutating git call was `git fetch origin`, which updates remote refs only. The worktree is clean at `cf23df7df`.

**origin/main has moved.** It is now `1c281c8ba` (PR #985), six commits past `e548d4cfa`, and `e548d4cfa` is an ancestor.
- The nine files that changed are all outside `projects/pec`: a Root tranche manifest, the chirality-app export, `tools/REGISTRY.md`, `tools/coordination/materialize_local_dependencies.py`, `validate_scc_resolution_case.py` and their tests, and `workflows/scc-resolution-case/resources/checks.md`.
- `git diff --name-only e548d4cfa 1c281c8ba -- projects/pec` is empty. No pinned file, preimage or `tools/scope_of_work` file changed, and the register still has no D-PEC-102 row.
- `apply_s4p.py` on a `1c281c8ba` export: `--check-only` exit 0, apply exit 0, "CHECK targets 8/8 byte-exact; … pinned 19/19 unchanged".

### Findings

**NON-BLOCKING 1: the REQ-018 repair left the access-class clause in two other DEL-08-03 records.**
- **Where:** candidate `PREP/candidates/projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/ScopeOfWork.md`.
  - Line 137 (OUT-003) still lists test coverage of "the single format across access classes and consumer paths".
  - Line 309 (REQ-012) still requires "any variation by access class or consumer path under REQ-018, with its accepted source".
- **The problem:** REQ-018 (line 315), AC-019 (340), VER-018 (403) and the matrix row (459) now cover consumer paths only.
  - OUT-003 therefore promises a test that no VER implements, and it brings back the access-class uniformity that verdict 02 Finding 2 said has no source.
  - REQ-012 sends access-class variation to a requirement that no longer covers it.
- **Repair:**
  1. OUT-003: change it to "the single format across consumer paths".
  2. REQ-012: change it to "any variation by consumer path under REQ-018, with its accepted source".
  3. Both IDs are already in AX-013's list of kept IDs whose text changed, so AX-013 needs no edit.
  4. Re-hash, re-run the DEL-08-03 checks, re-render `apply_s4p.py`, and update the draft's hash rows (lines 104 and 280) and its checklist hash (line 515).

**NOTE 2: the new CON-007 sentence does not route part of its third question.**
- **Where:** DEL-08-03 line 352.
- **What is right:** the sentence sends the first two questions to `DEL-04-03/TBD-005` and `/REQ-023`, and the absence question to `DEL-04-03/CON-005`, which the owner resolves. That is true to DEL-04-03 lines 258, 285, 288 and 318, and it no longer lets a production choice settle a CON.
- **What is missing:** the third question also asks how the signal is expressed. DEL-04-03 TBD-005 covers "the vocabulary of its … file-fallback signal". DEL-04-03 REQ-020 also puts what counts as degraded or failing, not only absent, in CON-005. The sentence routes neither.
- **Optional repair:** add "the signal's vocabulary and declared conditions are `DEL-04-03/TBD-005` and `/REQ-023`, within what `DEL-04-03/CON-005` leaves to the owner".

**NOTE 3: two QA-21 rows in the draft do not follow the draft's own convention.**
- **Where:** `PREP/DRAFT_D-PEC-102_s4_sow_currency_proposal.md` line 398.
- **The problem:** the header says a row notes it when a requirement does not cite a claim in its parentheses. Two rows list CLM-009 without that note:
  - "REQ-004 → `DEL-08-02` (CLM-006, CLM-009)": REQ-004 cites CLM-006 and TBD-006, not CLM-009.
  - "REQ-020 → `DEL-04-03` (CLM-007, CLM-009)": REQ-020 cites CLM-007, not CLM-009.
- The substance of QA 21 still holds: CLM-006 names DEL-08-02 and CLM-007 names DEL-04-03.
- **Repair:** add "(CLM-009 named, not cited)" to both rows, or drop CLM-009 from them.

**NOTE 4: the draft names `e548d4cfa` as current origin/main.**
- **Where:** draft lines 3, 47, 51, 81, 88, 288, 312, 384, 477, 480 and 530.
- Every statement made there is still true at `1c281c8ba`, because no PEC file changed.
- **Repair:** re-anchor these lines to the current origin/main when the draft is next refreshed. Otherwise add one line saying that `1c281c8ba` changed nothing under `projects/pec`.

**NOTE 5: verdict 02's disposition points to the wrong verdict.**
- **Where:** `PREP/VERIFIER_VERDICT_02.md` line 188 says the BLOCKING 1 repair was "re-verified in verdict 04". This re-verification is verdict 05.
- **Repair:** change it to "verdict 05" when this verdict is transcribed.

### Part 1: the repair diff (`git diff 396c6f744 cf23df7df`)
- **What the diff contains:** in these three candidates it holds exactly the hunks below. `claims/` and `quotes/` for DEL-08-0x are unchanged; only DEL-04-03.json and DEL-10-03.json changed. Nothing else in the three changed.
- **DEL-08-01** (one hunk):
  - CON-003 (line 177) gains "a decided list binds this deliverable only through a later revision of REQ-008 and AC-008 under its own packet".
  - REQ-008 (line 156) and AC-008 (line 169) exist.
  - CON-003 is new in AX-010. The clause is procedural and resolves nothing.
- **DEL-08-03:**
  - CLM-011 adds "(case-sensitive)". Re-checked on the `125cfacc1` export: 0 case-sensitive files contain any of the four strings under `v2/`; 4 files contain "citation" case-insensitively.
  - REQ-011 adds "(CLM-009)". CLM-009 names DEL-01-05.
  - REQ-018, AC-019, VER-018 and the matrix row are now consistent with CON-005 (line 350: the format is bound only to orientation responses, and the response set is left open) and with PEC-API-007's "over the same versioned API and responses".
  - CON-007 as in NOTE 2.
  - AX-013 now lists REQ-011. REQ-018, AC-019, VER-018 and CON-007 are new IDs.
- **DEL-08-04:**
  - CLM-007 and CON-004 add `DEL-04-01/CON-001`. This matches the DEL-04-01 postimage line 399, "Some components `SOW-004` requires have no declared record-tier type or field". VER-004's "component entity sourcing" is traced again.
  - REQ-012 adds "(CLM-011)". CLM-011 names DEL-01-05.
  - AX-013 now lists REQ-012.
- **ID meanings:** no ID is retired or renumbered. The kept IDs that changed are CLM-011, REQ-011, CLM-007, CON-004 and REQ-012; each keeps its meaning and each is disclosed.
- **Other citations of these IDs:** DEL-04-01 CON-008 (line 406) cites `DEL-08-03/CON-007` for "the element structure on the wire is left open", which is still accurate. No other contract cites a changed DEL-08-0x ID.

### Part 2: MODE=VERIFY commands
All ran with `PYTHONDONTWRITEBYTECODE=1` and Python 3.13.7 on `git archive` exports in my scratch directory:
- `pre` is `125cfacc1`.
- `post` is `pre` with the eight candidates copied in (`diff -rq` shows exactly the 8 `ScopeOfWork.md` files).
- `head` is `cf23df7df`, used for the PREP scripts.
- `act` is `1c281c8ba`.

| Command | Exit | Result |
|---|---|---|
| `validate_scope_of_work.py`, each of the three | 0 each | `PASS format=SOW_V1` |
| `derive_review_checklist.py`, twice each | 0/0 each | byte-identical: `2b5beadb…50b4`, `a6d3c537…ec7b`, `afe85efd…61c1`. Each is `cmp`-identical to `evidence/run_main`, binds the postimage sha256, and has 9/21/16 items, every AC once in source order |
| `check_boundary_owner_resolution.py --show-not-checkable` | 0 each | 0 UNRESOLVED_OWNER or UNDEFINED_CLAIM, 0 requirements citing no claim; NOT_CHECKABLE 0 / 7 / 1 |
| `verify_s4p_quotes.py --observation 125cfacc1 --only <DEL>` | 0 each | `RESULT PASS 36/36`, `97/97`, `75/75` |
| `verify_s4p_state_claims.py --only <DEL>` | 0 each | `RESULT PASS 161/161`, `135/135`, `74/74` |
| `check_sibling_ids.py <head PREP> <pre>` | 0 | `RESULT PASS 57/57`, including the new DEL-08-04 → `DEL-04-01/CON-001` and DEL-08-03 → `DEL-04-03/CON-005`; `cmp`-identical to evidence |
| `check_quote_currency.py` on the pre export | 0 | `SUMMARY active_execution_quotes_verbatim 127/127` |
| `check_quote_currency.py` on the post export | 0 | `cmp`-identical to pre; DEP-08-04-004, DEP-08-04-006 and DEP-08-05-005 PASS |
| `apply_s4p.py` on the `1c281c8ba` export | 0 / 0 | postimage hashes equal the draft's |

**QA items**
- **Items 1 and 4:** the validator resolves a single SOW_V1 format.
- **Item 3:** `_STATUS.md` is untouched, and its hashes match draft lines 299–301.
- **Items 8 and 9:** covered by the validator and the checklist.
- **Items 13 and 18:** covered by the checklist rows above.
- **Item 19:** my scan found 0 undefined bare ID tokens outside blockquotes in any of the three, and every added citation uses the qualified form.
- **Item 20:** the only grouped row is DEL-08-01 AC-001 with AC-005, both verified by VER-001 alone. In DEL-08-03, AC-019 maps to VER-018 only.
- **Item 21, by hand:**
  - DEL-08-03: REQ-009, REQ-011, REQ-017 and REQ-018 resolve through CLM-009, which each cites. REQ-004 resolves through CLM-006, REQ-008 through CLM-009, and REQ-020 through CLM-007.
  - DEL-08-04: REQ-012 resolves through CLM-011, which it now cites.
- **Whitespace:** no trailing blanks or tabs; final newline present in all three.
- **Item 16, where the findings fall:** no schema finding and no execution-substrate finding. NON-BLOCKING 1 and NOTES 2 and 3 are project content; NOTES 4 and 5 are record currency.

**Dependency quotes, checked independently:** all three ACTIVE `EvidenceQuote` values are raw substrings of exactly one postimage line: DEL-08-03 OUT-002, and DEL-08-01 OUT-001 for the other two.

### Part 3: the draft
- **Candidate table (lines 103–105):**
  - Preimage hashes reproduce at `125cfacc1`: `8ac1dc05…3d76`, `013c615a…3138`, `6d1ec1ad…222b`.
  - Postimage hashes, line counts (227/462/442), per-prefix ID counts, checklist counts (9/21/16) and quotes/claims counts (32/161, 94/135, 73/74) all reproduce.
- **Grant table (lines 279–281):** the full hashes match, as do the `apply_s4p.py` TARGETS. `apply_s4p.py` hashes to `3152effc…e449`, as stated.
- **Pinned files:** the `_STATUS.md` and `Dependencies.csv` hashes at lines 299–301 and 305–306 match.
- **Checklist hashes (lines 514–516):** match.
- **Reconciliation paragraph:**
  - Line 197's "except where the sibling reserves a question for the owner" and line 201's DEL-08-03 CON-007 statement are true.
  - Lines 206–210 match the diff. Line 206's "with no access-class clause" is true of REQ-018 itself; see NON-BLOCKING 1 for OUT-003 and REQ-012.
  - Line 209 (DEL-08-04 adds `DEL-04-01/CON-001`) is true.
- **QA-21 rows:** line 399 (DEL-08-04) is accurate. Line 398 (DEL-08-03) is correct on owners, apart from NOTE 3.

### Checked by hand
- DEL-04-03 postimage TBD-005, REQ-017, REQ-019, REQ-020, REQ-023 and CON-005 against DEL-08-03 CON-007.
- DEL-04-01 postimage REQ-001, REQ-006, REQ-011, REQ-012, CON-001, CON-002, CON-004, CON-008 and AX-009 against DEL-08-04 CLM-007 and CON-004.
- DEL-08-03 CON-005, REQ-005, REQ-019, CLM-009 and CLM-013 against the new REQ-018.
- DEL-08-04 CLM-011 names DEL-01-05; DEL-08-01 REQ-008 and AC-008.
- The v2 string absences, both case-sensitive and case-insensitive.
- Every other text in the three that mentions access classes or consumer paths.

Scratch directory, kept for rerun (nothing else touched): `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/s4prev.yxO3bw`. Raw outputs are in its `out/` folder.

## Disposition (WORKING_ITEMS)

| Finding | Disposition |
|---|---|
| NON-BLOCKING 1 (OUT-003, REQ-012 access-class clause) | Repaired with the suggested wording; DEL-08-03 re-hashed, act script re-rendered, checks rerun; re-verified in verdict 06 |
| NOTE 2 (CON-007 third question) | Repaired: CON-007 routes the signal's vocabulary and declared conditions to `DEL-04-03/TBD-005` and `/REQ-023` within `DEL-04-03/CON-005`, and names degraded/failing with absence as `DEL-04-03/CON-005` |
| NOTE 3 (QA-21 rows REQ-004, REQ-020) | Repaired: "(CLM-009 named, not cited)" |
| NOTE 4 (check commit) | Repaired: the draft is re-anchored to `origin/main` `b990b0c90` |
| NOTE 5 (verdict 02 cross-reference) | Repaired: verdict 02's disposition now says "verdict 05" |
| (transcription note) | The report's "`3152effc…e449`" is the reviewer's typo [sic: the hash bound at `cf23df7df` ends `…ce449`, as verdict 04 states]; the report text is kept verbatim |
