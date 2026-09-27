# Verifier verdict 02 — MODE=VERIFY on DEL-08-01, DEL-08-03, DEL-08-04 (S4P preparation)

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by the S4P WORKING_ITEMS manager in the foreground. It authored nothing in the packet. Its final report is transcribed below verbatim from its hand-back message.
- **Reviewed head:** `396c6f744`. Repairs follow in the next commit; dispositions are at the end.

## Report (verbatim)

## S4 prep review: MODE=VERIFY on DEL-08-01, DEL-08-03 and DEL-08-04

**Overall verdict: FAIL.** One blocking finding. All three contracts pass every mechanical check. The failure is one false routing sentence in DEL-08-03 CON-007, which came from the manager's reconciliation edit. It is a one-clause fix, followed by a re-hash and re-run for DEL-08-03 only. Everything else is non-blocking or a note.

I modified nothing. The only mutating git call was the `git fetch origin` the brief asked for, which updates remote refs only.

**origin/main has moved.** It is now `e548d4cfa` (PR #984), past `3488a236a`. The only file changed between `3488a236a` and `e548d4cfa` is `projects/chirality-piping/.../HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/WORK_GRAPH.md`. Nothing pinned changed.
- Between `125cfacc1` and `origin/main`, the PEC changes are limited to `docs/STATUS.md`, two `WORK_GRAPH.md` files, review returns and one receipt.
- None of the three candidates quotes or claims anything from those files.
- Worktree head is `396c6f744`.

### Findings

**BLOCKING 1: DEL-08-03 CON-007 sends a question to DEL-04-03's production declaration, but DEL-04-03 reserves that question for the owner.**
- **Where:** candidate `PREP/candidates/projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/ScopeOfWork.md` line 352. The draft repeats it at `PREP/DRAFT_D-PEC-102_s4_sow_currency_proposal.md` lines 197 and 201.
- **The sentence:** CON-007 raises three questions, the third being "how the file-fallback signal is expressed, given that `PEC-ORI-007` requires it "whenever PEC is absent, degraded or failing its own checks" while an absent PEC returns no response for any format to carry". It then ends: "The `DEL-04-03` contract leaves the envelope's representation to its production declaration (`DEL-04-03/TBD-005`, `DEL-04-03/REQ-023`), and these questions resolve there."
- **Why that is false for the third question:**
  - The DEL-04-03 postimage (line 317, CON-005) carries the absent-PEC case as the first of its three open parts. It says: "no accepted source says whether absence has any response-borne form … It settles none of the three. They resolve through the owner, in the first `DEL-10-13` Scope of Work … or in a later PEC scope change."
  - DEL-04-03 REQ-020 (line 284) also says what counts as absent, degraded or failing "are CON-005".
  - TBD-005 and REQ-023 cover only the signal's vocabulary and declared conditions.
- **Consequences:**
  - The draft tells the owner that the whole remainder is a production-declaration matter. Part of it is owner-reserved.
  - The candidate's text opens a path to settling a CON by production choice.
  - The first two questions (trust-tier structure; whether the stamp fields repeat or refer) are correctly routed to TBD-005 and REQ-023. DEL-04-03 REQ-017, REQ-019 and REQ-023 confirm this.
- **Repair:**
  1. Replace the last sentence of CON-007 with: "The `DEL-04-03` contract leaves the envelope's representation to its production declaration (`DEL-04-03/TBD-005`, `DEL-04-03/REQ-023`), where the first two questions resolve; whether PEC's absence has any response-borne form is `DEL-04-03/CON-005`, which resolves through the owner, not by production choice."
  2. Update draft line 201 to add `/CON-005`, and qualify line 197's "route the remainder to that sibling's production declaration".
  3. Re-run the validator, checklist, quote and claim verifiers and `check_sibling_ids.py`, then re-hash (`2031526ef7e3…` changes) and rebuild `apply_s4p.py`.

**NON-BLOCKING 2: DEL-08-03 REQ-018 conflicts with CON-005, and goes slightly beyond the sources.**
- **Where:** line 315 (REQ-018) against line 350 (CON-005).
- **The conflict:** REQ-018 says "The format shall be one format for the `PKG-08` API surface". CON-005 leaves open whether the format applies to every API response or only orientation responses, and says the contract "does not extend its outputs to other response kinds by assumption".
- **The extrapolation:** REQ-018 also requires the format to be identical "whatever access class a request is made under", allowing variation only with an accepted source. The sources support uniformity only between the harness path and the tool-call path (PEC-API-007 "over the same versioned API and responses"). They say nothing about owner and admin.
- **Repair:** reword to "one format for the responses it applies to (CON-005), applied identically whatever consumer path carries it — an enabled harness or the agent tool-call surface — and whatever access class …", or drop the access-class clause.

**NON-BLOCKING 3: DEL-08-04 VER-004 names an upstream question the contract no longer cites.**
- **Where:** line 365, which is byte-identical to the prior contract.
- **The problem:** VER-004 still searches for statements resolving "component entity sourcing". The prior CON-004 anchored that phrase to DEL-04-01's CON-001. The postimage's CLM-007 (line 256) and CON-004 (line 332) now cite only `DEL-04-01/CON-002` and `/CON-004`. The question still exists: the DEL-04-01 postimage CON-001 is the component-type gap. But DEL-08-04 no longer traces it.
- **Repair:** add `DEL-04-01/CON-001` to CLM-007 and CON-004. The sibling check will then cover it as well.

**NOTE 4: DEL-08-03 CLM-011's string-absence claim is true only case-sensitively.**
- **Where:** line 278, which says no file under `projects/pec/v2/` contains "citation".
- At `125cfacc1`, `Citation` appears in `v2/config/loops.schema.json`, and `SOURCE_CITATION` appears in `v2/src/pec_v2/core/content_minimal_guard.py`, `v2/tests/storage/test_content_minimal_guard.py` and `v2/docs/STORE_LIFECYCLE_AND_GUARD.md`.
- Claim S22 (a case-sensitive glob match) passes, and the conclusion (no format artifact exists) stands.
- **Optional repair:** add "(case-sensitive)".

**NOTE 5: two unchanged boundary requirements cite no claim naming their owner.**
- DEL-08-03 REQ-011 (line 308) and DEL-08-04 REQ-012 (line 304) name DEL-01-05 in their own text but cite no claim, although CLM-009 and CLM-011 name it. QA 21 expects the owner in a claim the requirement cites.
- **Optional repair:** append "(CLM-009)" and "(CLM-011)" respectively.

**NOTE 6: DEL-08-01 CON-003's resolution route is incomplete.**
- **Where:** line 177, which routes the question to the owner "through the first Scope of Work of `DEL-08-06` (work-graph node K2) or a later PEC scope change".
- Once decided, DEL-08-01's own REQ-008 and AC-008 would still need a revision to bind it.
- **Optional:** say so.

**NOTE 7: the page-is-a-response reading in DEL-08-03 REQ-016 (line 313) is defensible and consistent across siblings; no change needed.**
- It rests on PEC-API-006, which requires any truncation to be "stated in the response", so a partial page is treated as a response.
- It matches DEL-08-04 CON-007 and REQ-003 (timed extent: one response or the whole sequence, left open) and DEL-04-02 CON-007.
- It resolves no CON: whether a sequence holds one examined-through SHA stays TBD-005.

**NOTE 8: DEL-04-01 CON-008 (outside my three; for the DEL-04-01 reviewer).**
- It asks "whether a composition that states an absence or limitation (REQ-006) is itself a condition of the fallback signal" and routes that question to DEL-04-03's declaration or a scope change.
- The degraded/failing half of that question is `DEL-04-03/CON-005`, which the owner resolves. Worth the same check as Finding 1.

### Checks you asked for (all pass unless noted)

**External anchors**
- DEP-08-04-004 (quotes DEL-08-03 OUT-002, line 136) and DEP-08-04-006 / DEP-08-05-005 (quote DEL-08-01 OUT-001, line 100) are ACTIVE and remain raw one-line substrings.
- DEL-08-01 OUT-001 is byte-identical to the prior contract.
- The qualifying sentences after them are true: the "Socket server + auth + tests" `AnticipatedArtifacts` cell in DEL-08-01, and in DEL-08-03 the page/segment sentence plus CON-005.
- The draft's other statements about these rows are accurate.

**ID stability**
- No ID is retired in any of the three.
- I computed the changed-ID sets independently. They match AX-010 (DEL-08-01) exactly and are fully covered by AX-013 (DEL-08-03 and DEL-08-04).
- The DEL-08-04 AC-015 clause drop is disclosed and is true: D-PEC-62's status line records "RULED as drafted … including … the C-08 standing-node exclusion".

**Scope**
- No numeric budget appears anywhere; metrics are only examples.
- DEL-08-01 REQ-008 stays within PRD §8 and PEC-API-007.
- DEL-08-03 REQ-014..017 and REQ-020 track PEC-API-006, PEC-ORI-007 and PEC-K-03/-10. The one extrapolation is Finding 2.

**Reliance, lifecycle and the Remaining section**
- "verify-before-rely" appears only in not-built-around statements.
- Reliance is stated as available only after the §12 gate and never as authority; it is kept distinct from the hold control and from professional reliance.
- CHECKING appears only as the observed state of DEL-08-02 and DEL-10-01.
- No readiness claim appears. Remaining sections appear only as retired history.

**Cross-candidate consistency**
- Four access classes with `agent` read-only are consistent with DEL-10-03 REQ-013..015.
- Envelope ownership (DEL-04-03), carriage (DEL-08-03) and gate (DEL-10-13) are consistent. So is the seven-component return (DEL-08-04 counts no components).
- DEL-04-01 CON-008 → `DEL-08-03/CON-007` and DEL-04-02 CON-007 → `DEL-08-03/REQ-015`, `/TBD-005` and `/CON-006` are all accurate.
- Every DEL-04-03 and DEL-04-01 ID cited by DEL-08-03 or DEL-08-04 keeps the meaning described.

**Draft table**
- Hashes, line counts, per-prefix ID counts, quote/claim counts (32/161, 94/135, 73/74) and checklist hashes all reproduce.
- The claim of "fifteen blockquoted sibling records" in DEL-08-04 checks out: 7 from DEL-04-01, 2 from DEL-08-03, 6 from DEL-08-01.

### Commands run
All ran with `PYTHONDONTWRITEBYTECODE=1`, on `git archive` exports in my own scratch directory `.../scratchpad/s4prev.5oVIYP`: `pre` is `125cfacc1`; `post` is `125cfacc1` with the eight candidates copied in; `head` is `396c6f744`, used for the PREP scripts.

| Command | Exit | Result |
|---|---|---|
| `validate_scope_of_work.py` (DEL-08-01, 08-03, 08-04) | 0 each | `PASS format=SOW_V1` |
| `derive_review_checklist.py` ×2 each | 0, 0 each | byte-identical; hashes `11dbb856…741a`, `6398cceb…0f98`, `8c9c464f…66b1`, equal to the draft's |
| `check_boundary_owner_resolution.py` | 0 each | 0 UNRESOLVED_OWNER or UNDEFINED_CLAIM; see NOT_CHECKABLE below |
| `verify_s4p_quotes.py --observation 125cfacc1 --only <DEL>` | 0 each | `RESULT PASS 36/36`, `97/97`, `75/75` |
| `verify_s4p_state_claims.py --only <DEL>` | 0 each | `RESULT PASS 161/161`, `135/135`, `74/74` |
| `check_quote_currency.py` on the pre export | 0 | `SUMMARY active_execution_quotes_verbatim 127/127` |
| `check_quote_currency.py` on the post export | 0 | same; outputs `cmp`-identical; DEP-08-04-004, DEP-08-04-006 and DEP-08-05-005 PASS |
| `check_sibling_ids.py` | 0 | `RESULT PASS 54/54` |
| `scan_s2_quotes.py` | 0 | `SUMMARY stale=0 kept=2` |
| `scan_external_quotes.py` (informational) | 0 | stale=13, kept=25; every DEL-08 hit is already disclosed in the draft or is a heuristic artefact |
| `diff -rq` pre vs post | — | exactly the 8 `ScopeOfWork.md` files differ; `_STATUS.md` untouched (QA 3) |
| Whitespace scan | — | no trailing blanks or tabs; final newlines present |

**QA 21: hand resolution of the NOT_CHECKABLE items**
- DEL-08-03 REQ-004 → later D-PEC source packet (CLM-006 quotes §B8).
- REQ-008 → DEL-04-03 and DEL-06-05 (CLM-009).
- REQ-009 and REQ-017 → DEL-04-05 (CLM-009).
- REQ-018 → DEL-08-06 (CLM-009).
- REQ-020 → DEL-04-03 (CLM-007).
- DEL-08-03 REQ-011 and DEL-08-04 REQ-012 → DEL-01-05, named in the requirement text and in CLM-009 / CLM-011 but not cited (Note 5).

**QA 19 and QA 20**
- QA 19: my scan found no bare upstream ID in own-voice prose; every flagged token is a local parenthetical reference.
- QA 20: the only grouped matrix row is DEL-08-01 AC-001 with AC-005, and both are verified by VER-001 alone.
- QA 1: the validator's format resolution (single SOW_V1, no dual format) covers it; no separate variance artifact exists.

### Checked by hand

**Quotes (over 30), each located at `125cfacc1` with whitespace collapsed**
- ScopeLedger rows SOW-003 and SOW-040 (raw); SOW-080 and SOW-083 cells.
- PRD: §8 access block; §8 Agents bullet; §16.6; §12 gate phrases; §15 D-PEC-90 label.
- PRD rows: PEC-API-001, PEC-API-002, PEC-API-006, PEC-API-007, PEC-ORI-007; PEC-K-03 closing sentence; PEC-K-04, PEC-K-05, PEC-K-08, PEC-K-10 phrases.
- SOFTWARE_DECOMP: OI-006 row; §8 DEL-08-01 QA sentence; C9; §1.2; OI-013; PKG-04 and PKG-08 charters; response-budget vocabulary.
- SCA-006: IA §9.2; IA "**Not offered:**"; BUD-a line.
- D-PEC-91 carry-forward note.
- DEL-08-02 REQ-001, REQ-003, CLM-004, AX-005; DEL-10-01 REQ-010, AX-004.
- Exhibit rows E-A28 and E-N11; C-08 and C-05 text.
- D-PEC-62 status and §7 text.

**Claims (over 25)**
- DEL-08-01:
  - six downstream PREREQUISITE rows, including E-P84 DERIVED with the DEP-08-06-003 statement;
  - DEP-09-06-003 and DEP-10-03-003 refreshed under D-PEC-101;
  - no MEMORY.md;
  - v2 string absences (checked case-insensitively too) and the one AF_UNIX fixture;
  - DEL-08-06 and DEL-10-13 at OPEN with Dependencies.csv and no SOW;
  - D-PEC-101's "All strata require owner acceptance; this ruling is that acceptance";
  - A-31; DQ-a and DQ-b; DL-21;
  - `_CONTEXT.md` 1.1→1.6 trace; `_REFERENCES.md` 1.6 / v2.4;
  - PhaseHints for all 11 deliverables named.
- DEL-08-03:
  - Dependencies.csv has 5 rows with the stated cells; DEP-08-06-005 / E-P86 fields;
  - `_DEPENDENCIES.md` E-P86 line;
  - DEL-08-02 CHECKING (2026-08-01);
  - schema.json hash, `e9fec7fff` add, and the absent strings;
  - `1c50d4da6` is an ancestor;
  - SCA-005 §B4 cause "SOW-083 quotation" with empty tick columns;
  - SCA-006 IA §7.1 loci and §B4 combined class;
  - PhaseHints for 22 deliverables.
- DEL-08-04:
  - 6 register rows with the stated cells, including DEP-08-04-005 LastSeen 2026-09-25 and its D-PEC-95 note;
  - D-PEC-95 N3 / PR #924 `abfd0897b`;
  - D-PEC-65 executed 2026-07-25/26;
  - only its own Dependencies.csv names DEL-08-04; 16 EXECUTION edges seeded under D-PEC-101;
  - no v2 path names latency or orientation (a content match exists in `v2/docs/STORE_LIFECYCLE_AND_GUARD.md`, but the claim is about paths);
  - DEL-10-01 CHECKING with its two artifacts;
  - the bound appears in five loci; "the current corpus" appears six times; the six PRD §11 metrics;
  - rev-1.3 pin cells for SOW-041 and DEL-08-04;
  - D-PEC-99 exhibit hash and Part A placement;
  - SCA-005 cause "inherits DEL-04-01/08-01 refresh".

Scratch directory (kept for rerun; nothing else touched): `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/s4prev.5oVIYP`

## Disposition (WORKING_ITEMS)

| Finding | Disposition |
|---|---|
| BLOCKING 1 (DEL-08-03 CON-007 routing) | Repaired with the suggested sentence; the draft's reconciliation paragraph now names `DEL-04-03/CON-005` and says the owner-reserved part stays with the owner. Re-hashed, act script re-rendered, checks rerun; re-verified in verdict 05 |
| NON-BLOCKING 2 (DEL-08-03 REQ-018) | Repaired: "one format for the responses it applies to (CON-005), applied identically whatever consumer path carries it"; the access-class clause is dropped from REQ-018, AC-019, VER-018 and the matrix row |
| NON-BLOCKING 3 (DEL-08-04 component entity sourcing) | Repaired: `DEL-04-01/CON-001` added to CLM-007 and CON-004 |
| NOTE 4 (case-sensitive string absence) | Repaired: "(case-sensitive)" added to DEL-08-03 CLM-011 |
| NOTE 5 (REQ-011 / REQ-012 owner claims) | Repaired: "(CLM-009)" and "(CLM-011)" appended; the provenance lists name the two requirements |
| NOTE 6 (DEL-08-01 CON-003 route) | Repaired: CON-003 says a decided list binds only through a later revision of REQ-008 and AC-008 |
| NOTE 7 (page is a response) | Recorded; no change |
| NOTE 8 (DEL-04-01 CON-008 degraded/failing half) | Repaired: CON-008 now says that part is `DEL-04-03/CON-005`, left to the owner |
