# D-PEC-95 P + R — Revision-1.5 Currency Act Handoff State

**Act date:** 2026-09-25
**Coordinator:** WORKING_ITEMS (Type 1), node U1 of HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005` (graph nodes N1–N3 and T1)
**Branch / basis:** `claude/pec-d95-currency-act` from `origin/main` `590ec52c15f86d812ce3c5d4919b475fe9cf3985`
**Publication:** through its own PR under the standing Git authorization of 2026-09-12; not merged by this act.

## D-PEC-95 item ledger

| Item | State after this act |
|---|---|
| N1 — `_Decomposition/_LATEST.md`, `_ScopeChange/_LATEST.md`, `_Coordination/_COORDINATION.md` (with the human-owned Notes line, "include") | DONE — generator bytes; item 14 records the SCA-005 `Handoff_State.md` and `RUN_SUMMARY.md` by hash as superseded for current state |
| N1 — SCA-005 `Handoff_State.md` / `RUN_SUMMARY.md` appends | NOT DONE, by ruling ("P+R (don't append)"); both byte-unchanged |
| N2 — re-pin 42 `_CONTEXT.md` and 64 `_REFERENCES.md` to revision 1.5 (references also PRD v2.3) | DONE — 66/66 contexts and 66/66 references at revision 1.5 |
| R — the four retired deliverables' "covers" bullets | DONE — "covers none — retired under SCA-005, formerly SOW-0NN" in DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05 |
| N3 — 19 stale evidence quotes in 10 registers | DONE — 111/111 ACTIVE EXECUTION quotes verbatim; `DEP-10-05-004` refreshed as prepared |
| T1 — TM-PEC-023 | DONE — `CLOSED` / `RESOLVED_BY_DECISION` on the ruling's "confirm TM-PEC-023", then archived to `REGISTER_CLOSED.csv` |
| Re-audit / `_Evaluation/DecompCoverage/_LATEST.md` | NOT DONE, by ruling ("no re-audit"); the pointer still names `COV_SCA005_POSTSETUP_2026-09-25_1606`, whose INFO findings COV-068/069/072/073 the N1 texts record as addressed without a further audit |

## Residuals (recorded, not repaired here)

1. **`DEP-10-05-004` warrant.** Its refreshed quote is verbatim in its
   unchanged locus (`Deliverables.csv` DEL-10-05 Description) but supports
   the DEL-10-05 → DEL-04-01 edge only implicitly (proposal finding 2). The
   ruling accepts it as prepared; re-locating its evidence to `ScopeLedger.csv`
   SOW-085 stays a carry-forward for a later dependency packet.
2. **Quotes citing Scope of Work files (proposal finding 3).** Eleven ACTIVE
   EXECUTION rows cite a deliverable `ScopeOfWork.md` (six of DEL-01-01's, two
   of DEL-08-01's, one each of DEL-01-06's, DEL-08-02's and DEL-08-03's). SOW
   currency work (graph S nodes) can make them stale again; the proposal
   recommends each SOW packet run this generator's corpus-wide quote check or
   `verify_d95.py` as an acceptance check.
3. **SCA-005 snapshot text.** Under P, `Handoff_State.md` and `RUN_SUMMARY.md`
   keep their checkpoint-3 wording (COV-073's snapshot half), which claims
   less closure than has happened, never more. `_COORDINATION.md` item 14 and
   the two `_LATEST.md` pointers carry current state.
4. **Audit-ID collision (proposal finding 4).** `COV-072` means the plan-count
   defect in the checkpoint-3 audit and SCA-005's own records, and the
   quote-currency finding in the post-setup audit. The N1 texts name the audit
   each time.
5. **Ordering with SCA-006 (proposal finding 5).** An SCA-006 `audit-decomp`
   pre-change baseline run before this act merges would again report the INFO
   findings this act clears.
6. **Loop records.** The work graph, central receipt, `docs/STATUS.md` and
   `README.md` lines (D-PEC-88) and any register-row status wording after
   merge are HELP_HUMAN's; this act writes none of them. No MEMORY row is
   opened by D-PEC-95.

## Execution disclosures

- **Brief.** `U1_D95_CURRENCY_ACT.md` (HELP_HUMAN session scratchpad, not in
  the repository), SHA-256
  `6cdf4c63cdc8c993319dd069db6938c701b4d619da5985a8918811a03986553e`, verified
  before work began.
- **Instruction sources read.** Root `AGENTS.md` `c8ce87ef…1dffd`,
  `CLAUDE.md` `336cc4fb…ab49`, `projects/pec/AGENTS.md`
  `c9d3b44d…197a`, `agents/AGENT_WORKING_ITEMS.md` `9ae4bea2…9665`, the
  task-management workflow files named in `VALIDATION.md`, and the D-PEC-93
  run root as format precedent.
- **Generator executor.** The proposal's administrative grant assigns the run
  to one WORKING_ITEMS instance; this manager ran it once, with
  `--repo .` as the brief states. No TASK author was dispatched.
- **Task Management additions.** Beyond the brief's validate / archive /
  validate sequence, the manager ran the workflow's federation preflight (a
  derived projection written only into this run root) and an `archive
  --dry-run` before the real archive. Neither writes a register.
- **Check helpers.** `check_preimages.py`, `check_byte_identity.py`,
  `run_holds.sh`, `run_schema.sh`, `diffcheck.py` and `containment.py` were
  written by the manager for this run, are read-only, and are committed here
  so each check can be rerun.
- **Pre-run preimage check.** A working-tree check of the 243 pins in
  `genP.tsv` returned 0 mismatches but printed to the terminal only; the
  saved record is `checks/preimages_at_590ec52c1.out` (126/126 against the
  pre-act export) and the generator's fail-closed guard.

## Rollback (proposal §Rollback)

- **Before merge:** close the PR and discard the branch and worktree.
- **After merge (owner direction):** a revert PR of this act restores the 119
  preimages tabled in `MANIFEST.md` and, because T1 rides this PR,
  `REGISTER.csv` `d350d007…799d` and `REGISTER_CLOSED.csv` `ea730ae0…afd94`.
  The act created and deleted no product file, so the revert removes nothing
  there. This run root stays as non-current evidence, with a rollback note
  appended here. No history reset; no silent downstream repair.

## Independent verification

Pending at the time of writing; recorded in `VERIFIER_VERDICT_NN.md` and
summarized here when returned.

## Not claimed

No CHECKING, ISSUED, artifact acceptance, readiness or reliance. Nothing here
prompts about CHECKING.
