# Review 01 of PR #997, transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `26c38d6ce4ee935a82096d4a70344de8b4a3631b`. The D1P manager's repairs (to `92c0fe864`) and this file follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `5a2f6744d8526c07f6860c28f825fe0009c3a3748c1759673082f6bf65cacfa9`.

## Report (verbatim)

**PR #997 review, head `26c38d6ce4ee935a82096d4a70344de8b4a3631b`. Verdict: PASS WITH NOTES.** Nothing blocking. I made no edits and no git writes. I exported with `git archive` into my own mktemp directory under the scratchpad, with `TMPDIR` set to it, and deleted that directory afterwards. The worktree is clean.

Paths below are relative to `projects/pec/execution/_Coordination/`. `DRAFT` means `PEC_D1_PREMISE_PREP_2026-09-26/DRAFT_D-PEC-105_d1_premise_amendment_proposal.md`. Line numbers are head bytes.

## Reproduction (check 1)
- **Harness.** `run_d1p_checks.sh` against `origin/main` `f0a6159c9`: **OVERALL PASS**, exit 0.
  - Script re-render matches.
  - Ledger renderings match: SPEC 22, DEL-00-03 SOW 15, ADR 6 and P 3 hunks.
  - Mode A changes exactly 3 files and mode AP exactly 4.
  - Validate, checklist (`522917133070…`, `d48881d992bd…`) and boundary checks pass.
  - Quotes 74/74; state claims 124/124.
  - Strict registers (0 errors, 26 warnings, exit 1), harness and receipts are identical before and after.
  - Quote currency 127/127, with 0 active rows citing a target.
  - Fault injection 24/24.
  - All four `diff_*.patch` files are byte-identical to the committed evidence.
- **SHA256SUMS.** `shasum -a 256 -c` passes: 100 entries, and the file list matches the folder exactly.
- **Hashes I recomputed.**
  - Draft: `710f2134…032f`. `apply_d1p.py`: `399a088b…4f1a`. Brief: `d1cdf4e3…c1f1`, as the draft cites.
  - All four preimages are identical at `6c6cc1b00`, `189f205ff` and `f0a6159c9`.
  - All four postimages equal the tabled hashes and line counts (207, 172, 183, 152).
  - All 18 pinned hashes in `apply_d1p.py` match at both `f0a6159c9` and the PR head.
- **Nothing outside the hunks changes.** `render_candidates.py` reports `RESULT PASS fails=0`, so no byte changes outside the listed hunks.

## Specific premises (check 3) — all verified against sources
- **K-03 row.** It matches PRD v2.4 L230, L302–304 and L451ff: reliance only within the pin, coverage and trust tier (PEC-ORI-007), only past the §12 gate, never authority (PEC-K-02), with files as the fallback. "Verify-before-rely" is removed, and nothing claims reliance now. Only K-03 changed among the K rows between `e92a82ca9` and `189f205ff`.
- **46 → 49.** PRD v2.4 has 49 `PEC-*-NNN` rows (ORI 7, RCN 6, GAT 4, PRS 7, STR 5, API 7, DSH 7, SVC 6).
- **ADR postures 3 and 4.** They match Root `docs/CONTRACT.md` K-RUNTIME-1, `docs/DIRECTIVE.md` L323–329 (D-GOV-43 A2: Codex custodies credentials, local-model residency retired), PRD §4.2 and §15 (L184, L545–548), and §13 L501 (the client seam is deferred behind T-RT; SOW-087 is OUT).
- **Daemon and cmux removals.** They match PRD PEC-STR-003, §12 P4, and ScopeLedger SOW-035/037 (cmux deferred by owner direction on 2026-09-24).
- **SPEC §4 WorkGraph/WorkNode.** It matches revision 1.6 SOW-001 and PRD §7.1 L257 and L267.
- **Counts.** The 100 / 74 / 18 / 8 scope counts, the 68 deliverable rows, the four retired rows and the §8 OI-002/006/008 text all match revision 1.6 §5, §7 and §10.

## BLOCKING
None.

## NON-BLOCKING
1. **Check 8 fails literally: `git diff --check f0a6159c9 26c38d6ce` exits 2.** The only failures are in the four unified-diff evidence files, `evidence/run_main/diff_*.patch`. Their blank context lines are " " and a patch ends on a context line; that is inherent to the diff format. The candidates themselves pass. There is precedent: merged prep folders such as `PEC_CURRENCY_D95_PREP_2026-09-25/evidence/*.diff` and `PEC_REV16_…/k4/evidence/*.diff` have the same whitespace-only lines, and no CI job runs `diff --check`. The real problem is latent: DRAFT L271 (finite-verification check 12) requires `git diff --check origin/main...HEAD` to be clean at the act, while L289 puts "all outputs" in the run root, and those outputs include these patches. Either scope check 12 or keep the patches out of the run root.
2. **The pre-act REVIEW variant does not work with the bound script as tabled** (DRAFT L32, L180). A REVIEW recorded before the act writes `_REVIEW.md` and `Review_Findings.csv` for both deliverables. `apply_d1p.py` pins those files, so preflight would refuse, and L260 says no re-pin is pre-authorized. The variant would also clash with check 8 at L267 and with the Limits at L304. The departure itself, bytes landing before REVIEW, is disclosed clearly and fairly at L32. For comparison, on 2026-08-09 the SOW, SPEC and `_REVIEW.md` landed together in `e92a82ca9`. The variant needs a sentence saying it requires a re-rendered script, or a different order: act on the branch, then REVIEW, then acceptance, then merge.
3. **Reading 4(a) is disclosed but not called out as going beyond scope** (DRAFT L7, L84–93, L322). The rebind changes normative text: OUT-002, REQ-001 (reworded), REQ-002, REQ-003, AC-003 (checklist text) and the production sequence, and AC-002/004/005 and VER-002/004 now resolve against revision 1.6. That goes beyond SCA-006 §B4's "CLM-004/CLM-006 … premise only". The grounds are sound: without the rebind, the named SPEC loci would fail AC-002 and AC-005. But the owner-facing text frames it as "a reading … for confirmation", and L7 describes every hunk as a premise correction or minimal consequence. Only the return's caller item 2 says it plainly, and that item's claim "Disclosed to the owner" overstates. Add one sentence to 4(a). Relatedly, AX-009's "Every kept ID keeps its meaning" is arguable for REQ-001 and REQ-002.
4. **Posture 3 carries more than the amended contract enumerates.** The amended CLM-005 and REQ-004 in P list sessions, delegation, tools, turn locks and interruption. Posture 3 also names the `codex app-server` child, Codex credential custody and the retirement of model residency. REQ-004 says "carry forward only the accepted v2 boundary recorded in CLM-005", so a strict R1 REVIEW could flag this. It is a coherence risk for the verifier's check 5 (L283), not a false statement.

## NOTES
1. **DEL-00-01 SOW acceptance.** The statement "No owner exact-byte acceptance of the DEL-00-01 SOW was found" (L148; return L58) is true. However, the current bytes `43346150…` came from the D-PEC-69 R4 exact repair, owner-approved by standing direction (`_Reconciliation/DeliverableConcordance/PEC_SOW_V22_SCA003_RECON_2026-07-28/DECISION_PACKETS/R4_OWNER_APPROVED_REPAIR.md`; `POST_REPAIR_MANIFEST.sha256`). That is worth citing. Also, L36 ("every byte outside the hunks is the owner-accepted preimage") is loose for P. P's own AX-008 correctly says only "remain history".
2. **Add-on P is justified and separable.** The brief itself cites SCA-005 plan L828, which is the §B4 row for the DEL-00-01 contract (hash `433461504444…`, "C13/D-GOV-43 runtime-ownership premise"). The brief's touch limit is therefore arguably inconsistent with its own sources; the draft could say so at L173. Without P, REQ-004 "Root owns generic runtime semantics" contradicts the amended posture 3. Mode A leaves P at its preimage, as the containment check shows.
3. **Acceptance lapses are stated exactly.** DEL-00-03 SOW and SPEC `ACCEPT_EXACT_BYTES` lapse, AC-011 becomes unsatisfied (`_REVIEW.md` L149–168), and DEL-00-01 AC-007 lapses (hash-bound, `_REVIEW.md` L62–70). R1, R2 and R3 are offered fairly. R3 holds with no answer (L158). R2's departure from "a new checklist derivation and REVIEW rerun" is disclosed (L155). No CHECKING or lifecycle question is asked anywhere.
4. **Naming clash.** The re-review options R1/R2/R3 share names with work-graph nodes R1–R4, and L12 says "R3 met" while L158 says "R3 holds". Consider renaming the options, for example RR1–RR3.
5. **Post-verdict-05 edits (commit `4141b6428`).** All verified except one detail at L131. It says the Epistemology L92–94 wording dates from `01199c851`. Blame shows L92–93 come from `01199c851` (2026-07-25), but L94 comes from `ea6b4b5d0` (2026-07-28). The ordering conclusion still holds, since both predate `5942c5033` (2026-08-01). The `f0a6159c9` recheck (L3), the eight S4 contracts, the INV-065/130/132/178..183 list, and the Praxeology note are all correct.
6. **Counts that moved on current main** (the draft anchors them at `6c6cc1b00`):
   - The external-quote scan now reports 82 stale lines, not 75. The extra 7 are all `@11a494e9a` artefacts from the D-PEC-102 act run root.
   - Contract basis pins are now 19 at `189f205ff` and 7 at `11a494e9a`, against L322's 11 and 12.
   - L167's list of "the rest" of the hash anchors omits D-PEC-80/81, D83_D84, P1_PRODUCTION_PREP, the S2 records, the SCA plans and the TM-PEC-009/010 drafts. All are history.
7. **Anchors and consequences.**
   - No active `Dependencies.csv` row cites any target as its evidence file. The two active rows that target DEL-00-01 (DEP-00-02-003, DEP-01-01-003) quote `SOFTWARE_DECOMP.md` and are unaffected; they could be named.
   - The accounts of DEL-01-01 CLM-009 and REQ-009 and DEL-01-05 TBD-005 (L164–165) are accurate.
   - No code, tool or CI depends on the target bytes.
8. **Wording and cause citations.**
   - The ADR and SPEC premise notes say "SCA-005 and SCA-006", but SCA-006 made no ADR premise false; the claim is vacuously true for the ADR.
   - The inventory table cites INV-131/132/179–182/184 as causes without saying the inventory marks them NOTE-ONLY. The accepted §B5 and §B4 rows are the operative authority, and they cover these loci.
9. **Rollback** (L298) does not say that under R2 a revert would also lapse the R2 re-acceptance.
10. **Containment and CI.** 104 files change, all in the prep folder plus the brief and the return. The merge brings in no extra PR content. GitHub reports `MERGEABLE`/`CLEAN`, review decision empty. CI on the head: `pec`, `harness`, Harness pre-merge, Desktop E2E (source mode) and the Select App, PEC and source coverage jobs pass; the rest are skipping.
11. **Disclosed boundary event.** The return (L92) records that a child agent wrote a PRD copy under `/var/folders/.../T/prd.md` and left it there. HELP_HUMAN may want to remove it.

I did not rerun `negative_controls.sh`.

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; nothing blocking. HELP_HUMAN sent every finding and note back to the D1P manager. It repaired them at head `92c0fe864`, and its fresh verdict 06 (PASS WITH NOTES) is in the prep folder. In summary:

- **NB-1:** the stored diffs are now `.diff.txt` files stripped of trailing whitespace. A runner row now fails on any trailing whitespace, and check 12 is worded to match.
- **NB-2:** the variant is restated as REVIEW-before-merge. The act runs on the branch, then REVIEW and acceptance happen there, and only then does the branch merge. A REVIEW before the act would need a re-rendered script, which is not granted.
- **NB-3:** reading 4(a) is stated plainly as going beyond SCA-006 §B4's premise-only scope, at L7 and in question 4(a). AX-009 is tempered.
- **NB-4:** posture 3 is narrowed to the premise's own elements, and add-on P's CLM-005 and REQ-004 are aligned with it. The three changed candidates were re-rendered, re-hashed and re-verified; the SPEC is unchanged.
- **Notes 1–10:** applied as the manager's return describes, or needing no repair. Note 11: HELP_HUMAN removed the child's `/var/folders/…/T/prd.md` (byte-identical to the repository PRD) on 2026-09-26. The re-review options are renamed RR1–RR3.

The repair head needs a fresh HELP_HUMAN review before merge.

*Correction after review 02 (NB-b):* the disposition first said "All four candidates" and "Notes 1–9"; it now says three changed candidates and covers notes 10 and 11. The report above is unchanged.
