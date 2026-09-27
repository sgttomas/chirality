# Return S1P — S1 Scope of Work currency packet (provisional D-PEC-104)

WORKING_ITEMS (Type 1) under HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, node S1; brief `briefs/S1P_SOW_CURRENCY_PROPOSAL.md` (SHA-256 `9718ab7307b8575b286369b99ae015f4c42d6edff0f3be546e83518786b79f17`). 2026-09-26. **Preparation only: nothing applied, no production file written, no ruling recorded.** Host-reported model: Opus 5.5 (`claude-opus-5-5`); roles and effort instruction-asserted. The final verdict state and PR head are stated in the manager's hand-back to HELP_HUMAN; this file records the packet as of its commit.

## Deliverables

- **PR:** https://github.com/sgttomas/chirality/pull/986 (branch `claude/pec-s1-sow-currency-proposal`; merges `origin/main` `7004eaeda`). Not merged.
- **Draft:** `execution/_Coordination/PEC_SOW_CURRENCY_S1_PREP_2026-09-26/DRAFT_D-PEC-104_s1_sow_currency_proposal.md` (hash in `SHA256SUMS`; filing name suggested in its header).
- **Bound act script:** `apply_s1p.py` `620034b1b5ea8c465ab78285c6c7037e6975f235aed04670c8a9695a5b7b3753`.
- **Candidates (postimages):** DEL-01-03 `65c7f4086f8a…a367`, DEL-01-04 `16ac1cd956c9…ca41`, DEL-01-05 `a0a73eb5537b…84bf`, DEL-02-01 `82caf28a3757…5872`, DEL-02-02 `84e55e58e663…fa86`, DEL-03-01 `5b71d3583b2e…8276`, DEL-03-02 `d823d55d9e71…73d0`, DEL-03-03 `c2b88cb65c71…9526`, DEL-03-06 `f9c3a0577172…8bd4`, DEL-04-05 `88029fead86c…eafd`, DEL-10-02 `f5590cf55b19…436e`, DEL-10-10 `813839a080d7…37c8` (full values in the draft's grant table and `apply_s1p.py`).

## Recommended option

**A** — the twelve exact replacements in one act, no lifecycle change; add-on M (MEMORY records at closeout: eleven created, one section appended to DEL-01-03's) offered separately. **A supersedes an owner-accepted contract without opening a review** (DEL-03-01; question 1 note, question 4).

## Lifecycle answer

Ten targets `INITIALIZED`, DEL-01-03 and DEL-01-05 `IN_PROGRESS` at `125cfacc1`; none `CHECKING` or `ISSUED`. No transition is implied or proposed; the act script refuses if any `_STATUS.md` differs. DEL-08-02 (a housekeeping-only contract) is `CHECKING` and excluded; DEL-10-03 is in S4. DEL-01-03 and DEL-01-05: REQ/AC/VER byte-identical to their preimages, so the produced artifacts' verification basis is unchanged; items that would change it are carried as open (DEL-01-05 REQ-007 "pending" wording; CON-002 clause; the "future enforcement" phrase).

## Part B landing table

| Item | Contract | Postimage lines |
|---|---|---|
| DEL-03-02-REM-016 | DEL-03-02 | L148, L150 |
| DEL-03-03-REM-004 | DEL-03-03 | L169, L347 |
| DEL-03-06-REM-004 (correction only) | DEL-03-06 | L220, L222–225, L229 (authored wording for the item's direction), L476 |
| DEL-04-05-REM-003 | DEL-04-05 | (1) L20 (bracket resolved to revision 1.6); (2) L116, L118–122; (3) L124; (4) L142; (5) L296; (6) L242, L332 |

Replacement strings byte-exact; each item's gate respected (its loci only; other changes come from the S1 currency causes); the ruling's acceptance of the exact wording is owner question 2.

## Downstream and anchor accounts

- **Dependency anchors:** no ACTIVE `Dependencies.csv` row cites an S1 contract; corpus-wide dependency quote currency 127/127 before and after.
- **Externally cited IDs kept:** `DEL-01-03/CON-001` (subject kept), `DEL-01-03/REQ-003` (byte-identical), `DEL-02-01/REQ-002` (admission-rule sentence byte-identical).
- **S2 quotation currency:** of the `D-PEC-100` fifteen, nine are S1 targets; eight brought current, DEL-03-06 has none (heuristic false positive); four are S4's; DEL-02-08/09 a later revision.
- **Consequences disclosed:** DEL-03-06's other stale text and two of its sibling quotations made non-verbatim by this act (correction-only scope); DEL-03-04 (S4) quotes DEL-03-01 `CON-005`; DEL-02-07 `CON-003`'s premise about DEL-02-01; DEL-04-05 quotes DEL-04-03 `CON-003` (S4 rebuild); REVIEW records of DEL-03-01 (acceptance lapses under its own terms) and DEL-01-05 (SOW binding no longer current).

## Check results (on `git archive` exports at `origin/main` `7004eaeda`, observation `125cfacc1`)

OVERALL PASS: act check-only 0 / apply 0 / rerun refuses 1; containment 12 contracts; validate, checklist (byte-identical reruns) and boundary ×12; quotes 884/884; state claims 897/897; qualified IDs 44/44; dependency quotes 127/127 pre and post; strict (exit 1, 0 errors, 26 `XRG-013`), harness and receipts identical before/after; whitespace clean; fault injection 9/9. Negative controls: 8 caught. Reliance preflight `exact-correction-preparation` ALLOW ×36.

## Verdicts

`VERIFIER_VERDICT_01..08.md` in the prep folder (reviewer returns with manager dispositions); a round-5 check of the round-4 repairs is `VERIFIER_VERDICT_09.md` when saved. No verdict records a ruling.

## Owner questions (in the draft)

1. A, amend or defer (A recommended; note: supersedes DEL-03-01's owner-accepted contract without opening a review). 2. Part B reading (confirm). 3. DEL-03-06 correction-only (keep). 4. Earlier REVIEW acceptances of DEL-03-01 and DEL-01-05 stay as history; no REVIEW file written (confirm). 5. Add-on M (recommended). 6. Model steer.

## For the caller

- The number D-PEC-104 is provisional; HELP_HUMAN publishes the draft with its register row.
- Stray files written outside their scratch directories by child agents of this run, left in place under the deletion rule: `…/scratchpad/sd.md` (a copy of `SOFTWARE_DECOMP.md` at `125cfacc1`), `/private/tmp/claude-501/grant.txt` (a copy of the draft's grant table), `/private/tmp/x` (a listing of the prep folder). This run's own scratch export `…/scratchpad/s1p.Bm2q` is deleted at hand-back.
