# D-PEC-105 act — handoff state

Undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node D1 (the act),
2026-09-27. Manager: WORKING_ITEMS (Type 1) under HELP_HUMAN, brief
`AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/D1A_D105_PREMISE_ACT.md`
(`fbc69cee…3895`). Return: `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/D1A_D105_PREMISE_ACT.md`.

## State

- **Executed:** the D-PEC-105 act, option A with add-on P. One run of `apply_d1p.py`
  (`952a7512…9d4d`) with `--with-addon-p` put the tabled postimages into the DEL-00-03
  SPEC, the DEL-00-03 `ScopeOfWork.md`, the DEL-00-01 ADRs and the DEL-00-01
  `ScopeOfWork.md` (act commit `7c250e370`). Every row of the proposal's finite
  verification passed (`VALIDATION.md`), and so did the post-merge rechecks at
  `0adfbc747`. The independent verifier returned PASS WITH NOTES
  (`VERIFIER_VERDICT_01.md`), with nothing blocking; its one non-blocking record
  finding is repaired in `MANIFEST.md`.
- **Published:** branch `claude/pec-d105-d1-premise-act`, PR #1007
  (https://github.com/sgttomas/chirality/pull/1007) against `main`. **Not merged**
  (the brief reserves merge).
- **Not done here, by design:** add-on M (closeout node M1; no `MEMORY.md` created);
  any register row, work-graph, central-receipt, `docs/STATUS.md` or `README.md` record
  (HELP_HUMAN's); any lifecycle change (both deliverables stay `CHECKING`); any
  `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv` or `REV_*` write; a REVIEW act or
  any acceptance (RR1 grants nothing to this act; the REVIEW-before-merge variant was
  not selected).
- Completed execution is not acceptance: the ruling authorizes the bytes; no
  readiness, release, professional, product or operational reliance is claimed.

## For the caller to resolve

1. **PR review and merge.** Every PEC PR needs fresh-context independent review of the
   complete candidate diff. Verdict 01 covered `c58a6b535` (the act and all
   verification outputs). Later commits add the verdict, the `origin/main` merge, the
   post-merge rechecks, the run-root records and the return. Merge follows the standing
   Git authorization once CI passes and review has no blocking finding.
2. **Base currency.** The branch merges `origin/main` `0adfbc747`. If `origin/main`
   moves again, merge it without a rebase and confirm that no target, pin or quoted
   locus changed. Then rerun `apply_d1p.py --with-addon-p --check-only` on an export of
   the new base, `run_d1p_checks.sh` on that base's exports, and the quote and
   state-claim verifiers on the merged tree. On the merged tree itself `--check-only`
   refuses by design. The parallel `D-PEC-104` (S1) and X1 acts write no D1 target
   or pin.
3. **Acceptances lapse when this lands (ruling question 1).** Once the act is on
   `main`: the DEL-00-03 SOW and SPEC `ACCEPT_EXACT_BYTES` of 2026-08-09 (SOW
   `3e4f0efc…5741`, SPEC `cc9f4754…1bae`) lapse on the record's own terms, and AC-011
   is unsatisfied for the new bytes; the DEL-00-01 AC-007 acceptance of ADR
   `f63ecc27…5db5` lapses (hash-bound), and AC-007 is unsatisfied for the new bytes;
   DEL-00-01's SELF_CHECK SOW basis (`43346150…1740`) describes superseded bytes. Both
   deliverables' untouched `_REVIEW.md` and `Review_Findings.csv` keep describing the
   prior bytes (DEL-00-03 bound to checklist `1c4d4927…`).
4. **RR1 (selected; grants nothing here).** HELP_HUMAN's graph node for the later,
   separately authorized REVIEW of the new bytes for each deliverable: a fresh
   checklist derivation against the new artifact hashes (the act's checklists are
   DEL-00-03 `a3bc80a0db9a1917aa54337f62cd2057ce154bdc792f3802d982012f667121b1` and
   DEL-00-01 `6e99f93c37c761b140c60d870ab0048bae814427d65143a60364f36896bb8cf9`),
   recorded in `_REVIEW.md`, `Review_Findings.csv` and a new `REV_*` snapshot, then
   the owner's `ACCEPT_EXACT_BYTES` of the postimage hashes with the DEL-00-01 AC-007
   and DEL-00-03 AC-011 confirmations. Its own authorization names its review type and
   method basis. The proposal's "Lifecycle" account of the revised `review` edition
   (frozen-candidate rules; both deliverables entered `CHECKING` under the D-PEC-72
   override without a recorded frozen SHA) stays with that later review; this act makes
   no claim under that edition.
5. **Add-on M at node M1.** Create two `MEMORY.md` files, one each under
   `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/` and
   `…/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/`. Build each from
   `docs/templates/MEMORY_TEMPLATE.md` (`5a9564f4…6a5a`) with `{{DEL-ID}}` replaced and
   exactly the one `## Runs` row the proposal tables. The `{PR}` slot is this act's PR
   (#1007). `{D}` is the closeout date. The two link targets are the central receipt
   and the D-PEC-105 ruling record.
6. **Disclosed downstream consequences (proposal "External anchors and downstream
   consequences"), unchanged and for their own packets:**
   - DEL-01-01 `ScopeOfWork.md` CLM-009 anchors ADR `f63ecc27…5db5` and DEL-00-01
     contract `43346150…1740`: still a true anchored observation, but it describes
     superseded bytes once this lands. Its REQ-009 citations of `DEL-00-01/REQ-006` and
     `/AC-005` stay byte-identical.
   - DEL-01-05 TBD-005's "accepted `ADR-PEC-V2-001`" describes the prior bytes until RR1
     completes.
   - Historical records quoting changed text (the scan lists 99 STALE lines at the
     current base, all history) are not edited; SCA-005/006 line references refer to
     the accepted preimages.
7. **Other findings for later (proposal "Other findings", not changed here):** the
   DEL-00-01 SOW authoring-time lifecycle wording and SCA-004-era currency wording
   (named in AX-008); `ScopeLedger.csv` / `SOFTWARE_DECOMP.md` SOW-067 "Daemon owns
   execution (C13)"; `SOFTWARE_DECOMP.md` §1.4 intake posture 1 and the `Deliverables.csv`
   DEL-00-03 envelope note ("46"); the unresolving `3623b958b`; DEL-00-01 AX-002,
   DEL-01-05 AX-006 and DEL-10-01 AX-005 "revision 1.3"; `projects/pec/AGENTS.md`
   "client seam carries as a concept"; DEL-00-01 REQ-005's literal archive path; PRD
   v2.4 §13's ADR re-citation wording.
8. **Verifier notes carried (verdict 01 Notes 2–4), no action:** REQ-004 reaches
   K-RUNTIME-1 through CLM-005; AX-009 does not repeat the P02 SCA-004-era label (it
   lives in the ledger and the proposal); the uniform ADR note names SCA-005 and SCA-006
   although every ADR hunk is an SCA-005 cause.
9. **Open items carried, none resolved.** Every `CON` and `TBD` in the two contracts
   stays open; no dependency edge is added; no registry or profile tool is declared or
   invoked (the checks ran repository scripts and the bound check aids only).

## Rollback

Before merge: close PR #1007 and discard the branch. After merge, at owner direction: a
revert PR restores the four tabled preimages, and removes M's two files if M has run.
The lapsed acceptances do not revive by themselves; restoring the exact accepted bytes
makes the prior acceptance records describe the current bytes again, which the owner
may confirm. The ruling record and register row are never reverted; a rollback is its
own register row and record. The run root stays as non-current evidence with a
rollback note.
