# Verifier verdict 01 — MODE=VERIFY on DEL-04-01, DEL-04-02, DEL-04-03 (S4P preparation)

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by the S4P WORKING_ITEMS manager in the foreground. It authored nothing in the packet. Its final report is transcribed below verbatim from its hand-back message.
- **Reviewed head:** `396c6f744` (branch `claude/pec-s4-sow-currency-proposal`). Repairs follow in the next commit; dispositions are at the end.

## Report (verbatim)

**Verdict: FAIL.** There is one BLOCKING finding in the DEL-04-02 candidate. It is a small text fix, but the postimage hash, checklist hash, bound act script and draft tables all have to be regenerated after it. Apart from that, the three candidates pass the MODE=VERIFY items (1, 3, 4, 8, 9, 13, 16, 18–21). The D-PEC-99 Part B carry-forwards are verbatim, and both readings the owner is asked to confirm (seven components; envelope not a stamp field) are grounded.

**Target and basis**
- Head is `396c6f744`, worktree clean.
- `origin/main` has moved from `3488a236a` to `e548d4cfa`. The only change is PR #984, one piping `WORK_GRAPH.md`. Nothing under `projects/pec`, `docs`, `tools` or `workflows` changed.
- `apply_s4p.py --check-only`, run on an `origin/main` export, exits 0 with `CHECK preflight passed`. So all 8 preimages and all 19 pinned files are unchanged.
- Pin `189f205ff` is an ancestor of `125cfacc1`. The decomposition files and PRD hash identically at the pin, at `125cfacc1` and at `e548d4cfa`.

## Findings

### F1 — BLOCKING (correctness, cross-candidate)
DEL-04-02 still says `PEC-ORI-001` has **six** components in four places. PRD v2.4 PEC-ORI-001, revision-1.6 SOW-004 and the DEL-04-01 postimage REQ-001 all have seven (terminal completion was added).

File: `.../DEL-04-02_Delta_service_since_SHA/ScopeOfWork.md` (the prep-folder candidate):
- **L245, CLM-015:** "the per-loop orientation return of the six `PEC-ORI-001` components is `DEL-04-01`".
- **L286, REQ-011:** "compose no per-loop orientation return of the six `PEC-ORI-001` components". This also leaves the terminal-completion act out of the exclusion.
- **L302, AC-011:** "no per-loop orientation composition of the six PEC-ORI-001 components". The derived checklist carries this text.
- **L379, AX-008** (byte-identical to the prior): "`DEL-04-01` composes the six-component per-loop return".

Why it matters:
- DEL-04-02's own AX-014 (L385) says CLM-015 was "brought current" and that "the seven orientation requirements (CLM-002)" were updated.
- The draft says the eight "now state consistently … DEL-04-01's seven-component return" (DRAFT L208) and asks the owner to confirm seven (question 3a).
- None of the verifiers catches this.

Repair:
- In the four loci, write "seven `PEC-ORI-001` components" (or "the components `PEC-ORI-001` enumerates") and "seven-component".
- Add AX-008 to AX-014's list of kept IDs whose text changed.
- Add claims/quotes entries if a count is asserted.
- Regenerate: the postimage hash (DRAFT L102, L268), the DEL-04-02 checklist hash (DRAFT L503), `apply_s4p.py` and its SHA (DRAFT L325), and `SUMMARY.out`. Rerun all checks.

No external contract cites DEL-04-02's IDs, so nothing else is affected.

### F2 — NON-BLOCKING (inconsistent disclosure)
DEL-04-03 has the same imprecision the draft discloses only for DEL-04-02.
- The verbatim Part B correction (1) at L20 says the contract "was authored against revision 1.3".
- But DEL-04-03's first bytes at `fb6442f47` (2026-07-25) cite **revision 1.2**. The revision-1.3 bytes are `ea6b4b5d0` (2026-07-28), which I verified with `git show`.
- DEL-04-02 adds a qualifying sentence (L22–24). DEL-04-03 L21–24 does not.
- The draft's "One imprecision" paragraph (DRAFT L186) names only DEL-04-02.

Repair: add the same qualifying sentence, backed by claims at `fb6442f47`/`ea6b4b5d0`, after DEL-04-03 L20. Extend DRAFT L186 to cover both DEL-04-02 and DEL-04-03.

### F3 — NON-BLOCKING (internal inconsistency)
DEL-04-01 AX-014 (L469) ends: "Sibling S4 obligations are cited by deliverable ID and register row, not by local ID." After the manager's reconciliation, CON-008 (L406) cites `DEL-04-03/REQ-016`..`/REQ-020`, `/TBD-005`, `/REQ-023` and `DEL-08-03/CON-007` by local ID.

Repair: reword to "`DEL-08-06` and `DEL-10-13` are cited by deliverable ID and register row only; sibling S4 obligations are cited by qualified ID against their postimages (CON-008)."

### F4 — NOTE (QA 21 hand-resolution table, DRAFT L385–386)
Some rows cite claims the requirement does not cite:
- **DEL-04-01 REQ-003** is listed as "→ DEL-03-01 (CLM-012, CLM-015)". REQ-003 cites CLM-006, CLM-007, CLM-011, CLM-012 and CON-001, not CLM-015. The owner of its excluded "feed grammar" act (DEL-02-01..09) is named only in CLM-015.
- **DEL-04-01 REQ-018:** the table adds CLM-015, which REQ-018 does not cite (CLM-023 alone suffices).
- **DEL-04-02 REQ-008** is listed with "CLM-011, CLM-015 … CLM-006", but REQ-008 cites only CLM-011 and CON-003.

The DEL-04-02 REQ-008 gap is carried byte-identical from the prior contract; the DEL-04-01 REQ-003 gap was touched only by the sixteen-types change. Repair: correct the table rows, or add CLM-015 to the two requirements' citations.

### F5 — NOTE (landing-table line numbers, DRAFT L175–176)
- DEL-04-02's qualifying sentences run L20–**24**, not L20–23.
- DEL-04-03's qualifying sentence runs L21–24.
- DEL-04-02 AX-014 (L386) says the opening is followed by "one qualifying sentence"; there are two (brought current; first version at `fb6442f47`).

Every other landing locus checks exactly: DEL-04-01 L273/275/277/281/283/285/289/291/293, trace table L297–344, praxeology L421–425; DEL-04-02 L172/174/307/381/385/389/446; DEL-04-03 L212, L214–222, L382, L387.

### F6 — NOTE (consequence disclosure, DRAFT L220)
DEL-04-05 CON-003 says neither the composing nor the stamping contract states where a response-level limitation statement lives. The new DEL-04-03 REQ-018 has the envelope carry, per feed, whether a limitation is stated. That premise may go partly stale; worth adding to the DEL-04-05 row. The draft's other DEL-04-05 statements are accurate:
- DEL-04-01 REQ-001 and CON-004 changed; REQ-006 is byte-identical.
- DEL-04-03 CON-003 changed; REQ-001, REQ-005 and REQ-008 are byte-identical.
- The CLM-013 "six components, no seventh added" text and CON-003 go stale.
- DEL-04-05's qualified citations are `DEL-04-01`/REQ-001, /REQ-006 and `DEL-04-03`/REQ-001, /REQ-008, /CON-003. All resolve in the postimages with their meaning kept.

### F7 — NOTE (DEL-04-02 CON-007, L327)
CON-007 routes the continuation question to DEL-08-03's declaration, and names a change to SOW-005 as the fallback. But if that declaration requires the delta service to accept a continuation position, the conflict is with DEL-04-02's own REQ-010, which forbids continuation. So the fallback is a revision of this contract, not only a SOW-005 scope change. Consider saying so.

### F8 — NOTE (draft, outside the three candidates)
- DRAFT L511 cites a `SHA256SUMS` file; none exists in the prep folder at `396c6f744`.
- DRAFT L79 and L396/L518 speak of `VERIFIER_VERDICT_01.md` onward as if they already exist; none do yet.
- DRAFT L3/L47 cite `origin/main` `3488a236a`; it is now `e548d4cfa`, with no pinned change.

## Checks I confirmed
- **Hashes (`shasum -a 256`)** match the draft for all three:
  - DEL-04-01: preimage `6f4e8c66…30ae`, postimage `13fa50fe…7ee8`, 510 lines.
  - DEL-04-02: preimage `a2b50f87…e65a`, postimage `8445deae…b19d`, 446 lines.
  - DEL-04-03: preimage `6ec7432b…ec6d`, postimage `bce89565…750f`, 442 lines.
  - `_STATUS.md` is byte-identical to its pin: `41510909…`, `d876ae1a…`, `c8a82497…`.
- **ID counts** match the draft table. Every prior ID is kept (none retired or reused). Each rebuild-provenance AX's list of changed IDs matches my record-by-record diff against the prior contract.
- **Trace table (DEL-04-01 L297–344)** covers all 46 prior REQ/AC/VER. Every row marked "unchanged" is byte-identical to the prior contract, and every row marked changed differs.
- **Part B:**
  - Both DEL-04-01 clauses and Gate lines are exact blockquote lines (L281/283, L289/291).
  - The three verification sentences are verbatim at L421–425.
  - The gates are stated as still binding (L277).
  - All 7 + 4 replacement texts are present; none of the replaced old texts remain.
  - The E-P34 block is identical (prior L170–178 = post L214–222); the E-P33 row and the [E-P26] sentence are unchanged.
  - The qualifying facts are true: DEP-04-02-003 and DEP-04-03-004 cells; `11a494e9a` (2026-07-28, PR #396); revision 1.6 is `current_basis`.
- **Reading 3a (seven components) is grounded:** PRD v2.4 PEC-ORI-001, SOW-004 at revision 1.6, the `Deliverables.csv` description, and `DEL-01-01/REQ-014` at `14be02f5…8b88`.
- **Reading 3b (envelope not a stamp field) is grounded:** the SOW-097 Notes "distinct from SOW-006 stamping"; IA §13.2 (L544) "The envelope is a separately testable declaration, distinct from stamping."; and DL-21's acceptance "with DQ-a, ENV-a…".
- **Manager reconciliation edits** (DEL-04-03 CLM-011, DEL-04-01 CON-008, DEL-04-02 CON-006/CON-007): I read the diff `5f69edb61`→`396c6f744` against the DEL-04-03 and DEL-08-03 postimages (REQ-015/016/017/020/023, TBD-005, CON-006/007). All are correct and true.
- **Other semantics:** verify-before-rely appears only as a quotation of the prior text or of D-PEC-90, or in a "not built around" statement. Operational reliance is written only as available from a release past the §12 gate, and never as authority. No CHECKING, ISSUED, acceptance or readiness claim. Remaining sections appear only as retired history or as "never a source". No CON is resolved by assumption.

## Commands run
All on `git archive` exports in my own `mktemp -d` scratch directory (since deleted): `origin/main` plus the eight candidates.

| Command | Exit | Result |
|---|---|---|
| `validate_scope_of_work.py` ×3 | 0 | `PASS format=SOW_V1` ×3 |
| `derive_review_checklist.py` ×2 each | 0/0 ×3 | byte-identical; `809e6f00…0d9d`, `5135e209…ba0b`, `564a559c…a540` (match the draft); AC counts 19/16/23, each once, in order |
| `check_boundary_owner_resolution.py --show-not-checkable` ×3 | 0 | no UNRESOLVED_OWNER / UNDEFINED_CLAIM; NOT_CHECKABLE: DEL-04-01 REQ-003/005/006/011/018, DEL-04-02 REQ-006/007/008/010, DEL-04-03 REQ-006/008/021, hand-resolved (see F4) |
| `verify_s4p_quotes.py --only` | 0 | DEL-04-01 `RESULT PASS 151/151`, DEL-04-02 `101/101`, DEL-04-03 `98/98` |
| `verify_s4p_state_claims.py --only` | 0 | `RESULT PASS 202/202`, `158/158`, `149/149` |
| `check_sibling_ids.py` | 0 | `RESULT PASS 54/54` |
| `scan_s2_quotes.py --candidates` | 0 | `SUMMARY stale=0 kept=2` |
| `apply_s4p.py --check-only` on the `origin/main` export | 0 | `CHECK preflight passed` (script SHA `29a905c7…`) |

Also checked: QA 20 (no grouped AC rows); trailing whitespace, tabs and final newline (clean); item 1 (no pilot-variance, migration or marker tokens); QA 19 scan (all flagged IDs are local references).

## Checked by hand
**Claims (over 25):**
- lifecycle states: DEL-10-01 CHECKING; DEL-01-01, 03-01, 03-02, 04-01/02/03, 04-05 INITIALIZED; DEL-08-06, 10-13 OPEN;
- the three D-PEC-99 History rows, including "No lifecycle change";
- contract hashes: DEL-10-01 `40d47fb6` at `65955cceb` and `125cfacc1`; DEL-03-01 `56495523` at `e92a82ca9` and `125cfacc1`; DEL-01-01 `14be02f5` and `43f1f57a`;
- SOW-004 row identical at `5d2770350` and `125cfacc1`, different at `65955cceb`;
- Dependencies.csv rows for the three deliverables, plus DEP-08-06-006, DEP-10-13-004 (EXPLICIT), DEP-08-05-003; DEL-10-13 has no DEL-04-01 edge;
- `_DEPENDENCIES.md`: 8, 1 and 6 downstream relations;
- `v2/src` has no orientation/reconcile/examined/baseline mention; `v2/` has no "freshness"; registry file contents and three profiles; absent words in `loops*.json`;
- STEP0 artifacts exist; §7.1 has 12 rows; phase hints; ContextBudgetQA rows;
- prior pins `65955cceb` / `11a494e9a`; commit subjects of `e92a82ca9`, `5d2770350`, `73ed349ed`, `189f205ff`, `fb6442f47`, `ea6b4b5d0`, `11a494e9a`;
- SCA-005 §B4 rows (no ticks) and the SCA-006 §7.1/§B4 rows.

**Quotes (over 30):**
- PRD PEC-K-03 (both parts), §8 Agents bullet, access-class sentence, PEC-ORI-001/003/004/007, PEC-API-006, §12 gate sentences, §15 D-PEC-90 sentence, §7.1 Receipt/Gate/WorkGraph/OrientationSnapshot/DecisionRow/optional-field phrases, PEC-RCN-002 phrases;
- SOFTWARE_DECOMP OBJ-001/002 rows, PKG-04 charter, SOW-004/006/007/097 rows, DL-21, vocabulary phrases;
- D-PEC-90 grant item 1; SCA-005 A-02 and A-22 phrases and §B4 cause; SCA-006 §B4 two quotes; IA §13.2 and §9.2;
- exhibit two quotes, AGENTS.md three quotes, `loops.schema.json` two quotes, PLAN C-07 phrase, the prior CLM-016/AX-007 phrases, and DEL-01-01 REQ-003 identical at `ce934ac33`.

All match verbatim, modulo whitespace and blockquote markers.

Relevant path: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-s4-sow-currency/projects/pec/execution/_Coordination/PEC_SOW_CURRENCY_S4_PREP_2026-09-26/`, which holds `candidates/.../PKG-04_Orientation_Services/1_Working/DEL-04-0{1,2,3}_*/ScopeOfWork.md` and `DRAFT_D-PEC-102_s4_sow_currency_proposal.md`. I modified no file and ran no mutating git command.

## Disposition (WORKING_ITEMS)

| Finding | Disposition |
|---|---|
| F1 BLOCKING (DEL-04-02 "six" components ×4) | Repaired: CLM-015, REQ-011, AC-011 and AX-008 now say seven (`seven-component`); AX-014 names the four IDs as brought current. Postimage, checklist, act script and draft regenerated; all checks rerun; re-verified by a fresh reviewer (verdict 04) |
| F2 NON-BLOCKING (DEL-04-03 revision-1.2 first bytes) | Repaired: qualifying sentence added after the correction (1) text, with claims S151–S154 (`fb6442f47`, `ea6b4b5d0`, `11a494e9a`); the draft's imprecision paragraph now covers both contracts |
| F3 NON-BLOCKING (DEL-04-01 AX-014 sentence) | Repaired with the suggested wording |
| F4 NOTE (QA 21 table rows) | Repaired in the draft: the table cites the claims each requirement actually cites, and names the uncited owner claims as hand resolution |
| F5 NOTE (line numbers; "one qualifying sentence") | Repaired: landing table re-derived after the edits; DEL-04-02 AX-014 now says "qualifying sentences" |
| F6 NOTE (DEL-04-05 CON-003 premise) | Repaired: added to the DEL-04-05 row of the consequence table |
| F7 NOTE (DEL-04-02 CON-007 fallback) | Repaired: CON-007 now says a declaration requiring a continuation position conflicts with REQ-010 and this contract is then revised under its own packet |
| F8 NOTE (SHA256SUMS, verdict files, origin/main) | Recorded: `SHA256SUMS` and the verdict files are written at the end of preparation; the draft names the final check commit |
