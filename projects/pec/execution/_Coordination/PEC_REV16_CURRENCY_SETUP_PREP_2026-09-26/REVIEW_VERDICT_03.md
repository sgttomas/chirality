# D-PEC-101 preparation — review 03 (PR #962 review by HELP_HUMAN's reviewer)

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `a02cff6923b31dcb147d8b18e2aad8c7d2b204c4`.
- **SHA-256 of the report text below (UTF-8, trailing newline stripped):** `9785a5e764833215c40d64113ebb4e6164e4a81750348f53fe98a0343905b1cb`.

## Report (verbatim)

## Review 02 of PR #962 at head a02cff6923b31dcb147d8b18e2aad8c7d2b204c4: CHANGES REQUESTED

There is one BLOCKING finding. It is mechanical, and it sits in the review-01 N1 repair itself. Every bound byte, hash and aggregate reproduces, and the other repairs are correctly applied.

Paths below are relative to `projects/pec/execution/_Coordination/PEC_REV16_CURRENCY_SETUP_PREP_2026-09-26/` unless given in full. `DRAFT` means `DRAFT_D-PEC-101_rev16_currency_setup_proposal.md`, SHA-256 `bcaf5327…1f15`, which I recomputed and which matches.

### BLOCKING

**B1. N1 was only half repaired: `DRAFT` line 361 promises a PASS that the K4 verifier cannot give.**
- **The claim.** Line 361 says: "When both parts ride one act in the recommended order (K1 then K4), run the K4 verifier with the K1-applied tree as its before-state (PASS)".
- **What I got.** I rendered K1 and then K4+C on a fresh export of main, then ran `verify_d101_k4.py <K1-applied tree> <K1+K4+C tree> --covers --allow-k1`.
  - It exits 1 with two FAIL lines:
    - `pre-state census  68 contexts / 68 references; std 61, d93 2, refs 66`
    - `the 64 D-PEC-62-scaffolded contexts share one provenance block  66 contexts, 3 distinct`
  - The cause: the verifier counts K1's two new `_CONTEXT.md` files, which carry the D-PEC-101 provenance.
  - It fails the same way without `--allow-k1`, and with K4 alone (no C) after K1.
- **No recorded evidence supports the PASS.** `k1/evidence/verify_k4_on_both.out` is the other configuration: the original export as before-state, run without `--covers`.
- **The rest of line 361 holds.** Against the original export (with `--covers`), the K4 verifier gives exactly one FAIL, on the containment line (149 vs 129).
- **Why it blocks.** An act following the recommended order would miss its own required result and have to stop and route. The independent verifier (`DRAFT` line 379, "gets the same results") would diverge. Review 01 blocked for the same reason: owner-ruled text stating a check result that the named tool cannot give.
- **Knock-on.** The return file's line 45 ("All findings repaired") needs qualifying.
- **Fix, either way:**
  - state the exact expected two FAILs for this configuration; or
  - make the original-export run (1 containment FAIL) the prescribed check on a combined tree.

### NON-BLOCKING

**N1. `git diff --check origin/main...HEAD` is not clean.**
- 13 files and about 381 lines are flagged, all under `k1/evidence/` and `k1/evidence_aca930622/`:
  - CRLF line endings in `K1_hubs.csv` and `K1_isolated.csv`;
  - trailing tabs in the TSV reports `genK1`, `genR`, `checkonly` and `k1_after_k4AC`;
  - diff context lines in `K1_vs_base.diff`.
- `k4/.gitattributes` exempts `k4/evidence/**` with `-whitespace`, but there is no equivalent for `k1/`.
- Checked from a checkout without HEAD's attributes, `k4/evidence` also shows hits.
- This is not a gate (`projects/pec/AGENTS.md` §"Development checks and evidence"; root `.gitattributes` line 6), and review-01 note 5 already recorded it. It does not meet your item-5 expectation of a clean result.

**N2. `DRAFT` line 367 asks for a clean `git diff --check` at act time, which probably cannot be met.**
- The administrative grant (line 386) puts the generator stdout reports and the closure output in the run root.
- Those same kinds of file are what produce the hits in N1:
  - K1's report ends each READ row with an empty field, which leaves a trailing tab;
  - the closure CSVs are CRLF, and only `Dependencies.csv` has `cr-at-eol`.
- Fix: scope the check to product paths, or add a run-root `.gitattributes` as k4 does.

**N3. `origin/main` moved during the review.**
- It advanced to `5aa4285c2` (PR #963). That PR touches only `projects/chirality-piping/**`, so the "Update the PR base" CI check may trip again.
- Reproduction is unaffected: nothing under `projects/pec`, `tools`, `workflows`, `.agents` or `docs` changed, and all 161 preimages match current main.

### NOTE

1. **Short hashes (B1 of review 01) are fixed.**
   - `check_short_hashes.py` passes (45 short hashes, 0 unresolved) against exports of both `dfb089b8a` and `aca930622`.
   - The script is weak: it accepts a short hash if any file in the tree matches, not necessarily the file named, and it also counts full hashes quoted in the draft.
   - So I mapped every short-hash occurrence (`DRAFT` lines 10–20, 61–63, 108–118, 326, 371, 396, 421, 594) to the file it names. All are correct, including the eight from review 01. All 50 full hashes in the basis table check out at main where the file is unchanged.
2. **B3 wording.** `DRAFT` line 96 says the rows keep "every other cell", but line 100 (correctly, following the D-PEC-95 N3 practice) prepends to `Notes`. The plan's §B3 says only `EvidenceQuote` and `LastSeen` change.
3. **Method substitution is disclosed.** The plan's §B2/§B3 and RUN_SUMMARY §6 name `dependency-extract` as the owner. The draft instead binds the rows through its generator (the D-PEC-93 precedent) and discloses this at line 61. It adds no scope.
4. **The add-ons stay inside the brief.** Add-on C edits a covers bullet, which goes beyond B7's version-only re-pin; it is disclosed (finding 1), optional, adds no path, and follows the D-PEC-95 add-on R precedent. Add-on V is requested by brief line 16. Neither enlarges beyond Lanes B1/B2/B3/B7.
5. **Packet number.** `D-PEC-100` is unassigned in the register (the last row is `D-PEC-99`). The draft takes 101 provisionally without explaining why 100 is skipped. HELP_HUMAN should confirm the number before the ruling, because K1's bytes embed it (line 3 says so).
6. **Strata.** Using DERIVED for ID-named targets reached through "composes" stretches C-10's wording ("unique non-ID resolution"). It is disclosed at line 80, and review-01 note 3 judged it defensible.
7. **Unfilled placeholder.** `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/K14P_REV16_CURRENCY_SETUP_PROPOSAL.md` line 46 still reads `{{VERDICT02}}`. HELP_HUMAN fills it from this verdict.

### Verified

**Review-01 repairs**
- N2 is applied (lines 346, 348, 447).
- N3 is applied (line 14).
- N4 is applied: `evidence/hold_dispatch_k4_candidates.tsv` shows 132/132 ALLOW.
- N5 is applied (line 3).
- Note 1 is applied (line 5).
- Note 2 is applied (finding 7, line 119).
- Note 4 is applied: line 10 cites plan line 545, which is the Q-CP2-2 row.
- Note 6 is applied (lines 134 and 385).

**Integrity**
- `fill_draft.py` re-renders the draft byte for byte.
- Both `SHA256SUMS` files verify.
- The brief hashes to `3c16bb93…f38b1`.

**Reproduction on a fresh export of main** (`dfb089b8a`; its `projects/pec` and `tools` are identical at `5aa4285c2`)
- Both generators rebuild byte-identically: `075036f0…0e73` and `4892c6a3…cecb`.
- All 161 preimages match.
- All 129 K4 postimages match, for both A and A+C (the C rows are DEL-04-03 and DEL-08-03).
- All 32 K1 postimages at 2026-09-26 match.
- All nine aggregates match.

**Generator behaviour**
- Change sets equal the grant exactly: 129 files for K4, 32 for K1, nothing deleted.
- `--check-only` leaves the tree untouched.
- Reruns exit 1.
- A wrong date exits 1 and writes nothing.
- Running K1→K4 and K4→K1 gives identical trees, equal to the union of the two parts.
- Slot rule: rendering at 2026-09-27 with `--reproduction` changes exactly 14 files, all identical after substituting the date.

**Validators and closure**
- Strict validator, K4 alone: output byte-identical to base (0 ERROR, 26 XRG-013, 2 DRB-008).
- Strict validator, with K1: 0 ERROR, the same 26 XRG-013, 0 DRB-008; 68 registers and 285 rows (ANCHOR 146, EXECUTION 139).
- Closure, K4 alone: summary byte-identical to base.
- Closure, with K1: 127 edges, 68 nodes, 0 SCCs, 0 bidirectional pairs, 0 orphans; `declared_only_rows` 127, `declared_unread_count` 136; the same six isolated deliverables; hub DEL-03-01 only (degree 25).

**Grounding** (my own checker)
- Quote currency is 127/127 (109/111 today).
- No duplicate edges or pairs.
- COV-080: 74/74 IN scope items traced; today 4 are missing (SOW-097 to SOW-100).
- The quotes sit in the loci named: PRD line 385 (PEC-API-007), PRD §8 line 311, and the DEL-10-13 row in `Deliverables.csv`.
- The new B3 quote equals the revision-1.6 DEL-08-01 cell.
- E-P84 to E-P99 are unused; E-P83 appears only in D-PEC-93 records.
- The lifecycle census and the 63 + 66 re-pin population hold, with the three A2 mirrors excluded.
- The owner-act quotes, the RUN_SUMMARY §6 rows (B1–B3 and B7, FROZEN) and the COV rows cited all match.
- The `_COORDINATION.md` Notes text at lines 225–227 matches.

**Verifier runs**
- The K1 verifier passes on K1 alone and, with `--allow-k4`, on the combined tree.
- The K4 verifier passes on A and on A+C.

**Other checks**
- Harness self-check exits 0 and the receipts validator is VALID at HEAD.
- The reliance preflight gives 161/161 ALLOW for `candidate-validation`; the holds register has a header and no rows.

**Owner questions and limits**
- Question 4 is clearly outside the grant, and HELP_HUMAN applies it only on explicit owner authorization (lines 421 and 446; limit at line 411).
- INCREMENTAL is disclosed only (lines 63 and 409) and is not put to the owner.
- Nothing prompts about CHECKING (line 405).
- The only lifecycle change is the two new folders starting OPEN (line 404).

**Containment**
- Against main the PR is 135 additions, all in the prep folder plus the brief and the return.
- The merge commit's changes equal `aca930622..dfb089b8a` byte for byte.

### Disclosure
I modified nothing. I worked from `git archive` exports and one scratch detached worktree at HEAD, which I have removed; scratch files are in `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/r962.0hxY/`. During the review, something outside my work switched the primary checkout to branch `claude/pec-d101-hh` at `a02cff692`, and advanced `origin/main`.

## Disposition (HELP_HUMAN)

| Finding | Disposition (HELP_HUMAN, applied after the manager's forced handback) |
|---|---|
| BLOCKING B1 (combined-tree K4 verifier expectation) | Repaired: the verification row now prescribes the original export as the K4 verifier's before-state on a combined tree (exactly one containment FAIL listing K1's 20 paths) and states that a K1-applied before-state fails the census and one-provenance-block checks by design |
| Return overstates "All findings repaired" | Repaired: the return's review-01 line is qualified and its review-02 line filled |
| Embedding list incomplete; "K4's bytes" | Repaired: the list adds the `_REFERENCES.md` closing line, Declared Upstream text and DEL-10-13 Run Notes; K4's *output* bytes carry no number |
| `git diff --check` not clean in `k1/evidence*`; act-time whitespace row | Repaired: `k1/.gitattributes` exempts `evidence/**` and `evidence_aca930622/**` like `k4/`; the draft's whitespace row is scoped to product paths, with a run-root `.gitattributes` |
| B3 "every other cell" | Repaired: except the `Notes` prefix and `LastSeen` shown |
| Packet number 101 vs unassigned 100 | Repaired: the draft says `D-PEC-100` is provisionally taken by the concurrent S2 packet; HELP_HUMAN confirms the number on publication |
| `check_short_hashes.py` weak; K1 docstring wording; TSV metadata; placeholder name; strata; method substitution; add-ons | No change: preparation aids or disclosed choices; reviewers verified independently |
| `origin/main` moved | HELP_HUMAN updates the PR base before merge |
