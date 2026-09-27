# D-PEC-102 act — handoff state

Undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S4 (the act),
2026-09-26. Manager: WORKING_ITEMS (Type 1) under HELP_HUMAN, brief
`AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S4A_D102_SOW_ACT.md`
(`98f74488…932e`). Return: `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/S4A_D102_SOW_ACT.md`.

## State

- **Executed:** the D-PEC-102 act. One run of `apply_s4p.py` (`2b6792fe…4869`) put the
  tabled postimages into the eight `ScopeOfWork.md` files (act commit `5d13cfdb8`).
  Every row of the proposal's finite verification passed (`VALIDATION.md`), and so did
  the post-merge rechecks at `78e74f590`. The independent verifier returned PASS WITH
  NOTES (`VERIFIER_VERDICT_01.md`), with nothing blocking.
- **Published:** branch `claude/pec-d102-s4-sow-act`, PR #998
  (https://github.com/sgttomas/chirality/pull/998) against `main`. **Not merged**
  (the brief reserves merge).
- **Not done here, by design:** add-on M (closeout node M1; no `MEMORY.md` created);
  any register row, work-graph, central-receipt, `docs/STATUS.md` or `README.md` record
  (HELP_HUMAN's); any lifecycle change (all eight stay `INITIALIZED`); any `_REVIEW.md`
  write; CHECKING, ISSUED, a REVIEW gate or acceptance.
- Completed execution is not acceptance: the ruling authorizes the bytes; no
  professional, product or operational reliance is claimed.

## For the caller to resolve

1. **PR review and merge.** Every PEC PR needs fresh-context independent review of the
   complete candidate diff. Verdict 01 covered `a26ca1613` (the act and all verification
   outputs). Later commits add the verdict, the `origin/main` merge, the post-merge
   rechecks, the run-root records and the return. Merge follows the standing Git
   authorization once CI passes and review has no blocking finding.
2. **Base currency.** The branch merges `origin/main` `78e74f590`. If `origin/main`
   moves again, merge it without a rebase. Confirm that no target, pin or quoted locus
   changed. Then rerun `apply_s4p.py --check-only` on an export of the new base,
   `run_s4p_checks.sh` on that base's exports, and the quote and state-claim verifiers
   on the merged tree. On the merged tree itself `--check-only` refuses by design.
   The parallel S1, D1 and X1 preparations write only under their own prep folders.
3. **DEL-04-01 exact-byte acceptance lapses when this lands.** The owner's 2026-08-09
   `ACCEPT_EXACT_BYTES` of the prior contract (`6f4e8c66…30ae`) lapses on its own terms
   once the act is on `main`. The ruling records this. DEL-04-01's untouched
   `_REVIEW.md` and `Review_Findings.csv` will still describe the prior bytes. No review
   is opened, and whether one is wanted later is an ordinary steer.
4. **Add-on M at node M1.** Create eight `MEMORY.md` files, one each for DEL-04-01,
   DEL-04-02, DEL-08-01, DEL-08-03, DEL-08-04, DEL-04-03, DEL-03-04 and DEL-10-03.
   Build each from `docs/templates/MEMORY_TEMPLATE.md` (`5a9564f4…6a5a`) with
   `{{DEL-ID}}` replaced and exactly the one `## Runs` row the proposal tables. The
   `{PR}` slot is this act's PR (#998). `{D}` is the closeout date. The two link
   targets are the central receipt and the D-PEC-102 ruling record.
5. **Disclosed consequences (proposal "Consequences outside this packet"), unchanged:**
   - DEL-04-05 (S1): its quotations of DEL-04-01 `REQ-001`/`CON-004`, its own "six
     components" text and `REQ-013`, and its quotation of DEL-04-03 `CON-003` go stale
     when this lands.
   - DEL-10-11: its quotations of DEL-03-04 `CON-001`/`CON-005` go stale. Suggested as
     a later DEL-10-11 currency item.
   - DEL-03-04: its quotation of DEL-03-01 `CON-005` goes stale if the S1 revision
     lands. Suggested as a later DEL-03-04 currency item.
   - Stale text found in passing in DEL-01-05, DEL-01-03 and DEL-08-02 belongs to S1
     or its owning workflow.
6. **Currency notes for later revisions (not re-pinned; no re-pin is authorized).**
   - DEL-10-03 `REQ-013` names its owner `DEL-08-01` in its own text but cites only
     `CLM-011`. A later revision could cite `CLM-016` so the boundary tool can check
     it (verdict 01 F1).
   - All eight postimages carry dated "provisional / not yet ruled" wording (proposal
     L243; verdict 01 N4). It is true under each contract's `125cfacc1` observation
     clause.
7. **Open items carried, none resolved.** Every `CON`/`TBD` in the eight contracts
   stays open. That includes DEL-08-01 `CON-003`, DEL-04-03 `CON-005`/`CON-006`,
   DEL-03-04 `CON-001`/`CON-002`/`CON-007`, DEL-08-03 `CON-005`/`CON-006`, DEL-08-04
   `CON-007`/`CON-008`, DEL-04-02 `CON-008` and DEL-10-03 `CON-004`. No dependency edge
   is added.
8. **DEL-04-01 Part B gates still bind.** DEL-04-01-REM-001 and REM-002 production
   stays gated on a separate exact owner-ruled DEL-04-01 production packet on
   `origin/main`, WORKING_ITEMS activation and a current reliance preflight.

## Rollback

Before merge: close PR #998 and discard the branch. After merge, at owner direction: a
revert PR restores the eight tabled preimages, and removes M's eight files if M has run.
The ruling record and register row are never reverted; a rollback is its own register
row and record. The run root stays as non-current evidence with a rollback note.
