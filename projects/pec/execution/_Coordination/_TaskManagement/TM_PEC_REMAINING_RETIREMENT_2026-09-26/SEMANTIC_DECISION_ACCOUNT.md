# PEC Remaining — semantic decision account

**No disposition has been made.** `SEMANTIC_DECISION_ACCOUNT.csv` keeps all 92
census keys, with their exact text, `Depends:` value, gates, source path and
hash, and adds each key's assessed meaning, claim currency, one proposed
disposition, destination, exact destination text where one is needed, gate
survival and evidence. Every row says `HumanDecision=PENDING` and
`AppliedResult=NONE`. The draft packet
`DRAFT_D-PEC-99_remaining_retirement_proposal.md` turns the account into an
exact act. This file explains the groups and names every exception.

## Grouped proposals

| Group | Disposition | Keys | Ground |
|---|---|---:|---|
| Executed inquiries | (c) | 3 | DEL-01-03-REM-001..003 were ticked under `D-PEC-87` L-1a after each inquiry ran and was verified; `_STATUS.md` History (2026-09-24) names the three report hashes, which match the files. The History row stays after the section is removed |
| Closed by SCA-005 retirement | (c) | 4 | DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05 REM-001: "closed unexecuted by retirement, not completed" (`D-PEC-92`; SCA-005 checkpoint 3). Reinstatement conditions live in `ScopeLedger.csv`, `Deliverables.csv` and `SOFTWARE_DECOMP.md` (T-RT for three; owner direction plus accepted scope change for DEL-07-04) |
| Executed frozen repairs | (c) | 2 | DEL-01-05-REM-001/-002 (never applied, `D-PEC-83` F): both scanner repairs ran under `D-PEC-84` S-A in `52bb1dddc`; current bytes equal the recorded repair outputs; acceptance of the new bytes is still separate and DEL-01-05 stays IN_PROGRESS |
| Evidence inquiries | (d) → exhibit Part A | 71 | Owner-gated, read-only inquiry options that `D-PEC-83` E left unselected (70 applied + DEL-01-05-REM-003 from the frozen carrier). None was executed; none's linked claims were all retired. They move verbatim with gates to the decision-owned exhibit and remain selectable only by steering. Currency notes record partial supersession (for example DEL-00-02-REM-001, DEL-02-06-REM-001, DEL-09-05-REM-001's retired `SOW-049-B2`) and pending SCA-006 changes (DEL-08-01, 08-03, 10-03, 10-12) |
| Product obligations | (d) → Part B, S2 or S4 | 6 | DEL-02-07-REM-001..004 (S2) and DEL-04-01-REM-001/-002 (S4). Their SOWs already state almost all of each obligation. The carry-forward texts re-express them for the revision-1.5 scope, each with a cited basis: DEL-02-07 is now a parity-peer reader (SOW-017; the feed-manifest part is not carried; the declared grammar names `status_glob`; the fixture suite is registered in `software-workflow.json` per `projects/pec/AGENTS.md`), and DEL-04-01 follows SOW-004 (current REQ/AC/VER IDs traced to their successors, or removed only by an S4 owner ruling; "finite fixture limits" added) |
| Documentary corrections | (d) → Part B, S1 or S4 | 5 | DEL-03-02-REM-016, DEL-03-03-REM-004, DEL-04-05-REM-003 (S1); DEL-04-02-REM-002, DEL-04-03-REM-002 (S4). Each SOW paraphrase is still stale against the `D-PEC-65` register repair; `D-PEC-95` N3 did not touch these rows. Each carries exact replacement wording for its loci |
| Owner decision | (e) | 1 | DEL-03-06-REM-004: same kind of correction, but DEL-03-06's SOW is class `current` and in no pending node. Options: (a) carry it in Part B for S1 (recommended), (b) park it in Part A, unselected, (c) decline (packet question 1; generator `--q1 s1|park|decline`) |

Totals: (a) 0, (b) 0, (c) 9, (d) 82 (Part A 71, Part B 11), (e) 1 = 92.

## The sequencing rule

HELP_HUMAN directed (2026-09-26) that an item whose receiving Scope of Work a
pending currency node (S1, S2, S4 or D1 of graph
`HELP-HUMAN-PEC-20260925-POST-SCA005`) will rewrite takes (d): it moves into
the decision-owned exhibit and that node's packet absorbs it as an exact
carry-forward. That is why no key takes (a). Absorption: S1 — DEL-03-02-REM-016,
DEL-03-03-REM-004, DEL-04-05-REM-003 (+ DEL-03-06-REM-004 on question 1 (a));
S2 — DEL-02-07-REM-001..004; S4 — DEL-04-01-REM-001/-002, DEL-04-02-REM-002,
DEL-04-03-REM-002; D1 — none.

## Why no Task Management row

Each surviving meaning has a home: the exhibit under the retirement ruling
(Part A as `D-PEC-83` E's follow-up; Part B as a named node's input). The
federation preflight found no PEC finding. `TM-PEC-004` (DEL-04-01
feed-grammar owner) and `TM-PEC-005` (DEL-04-05 limitation inventory) relate
to items here but are different concerns; `TM-PEC-018` relates to
DEL-03-02-REM-016 without being closed by it; `TM-PEC-019` and `TM-PEC-024`
duplicate nothing.

## What is outside the account

The 73 held or conditional `D-PEC-83` residuals were never Remaining items;
they stay in the accepted report and are not lost (`CENSUS_COMPARISON.md`).

## Independent inputs

Four `pec-task` TASKs assessed disjoint key groups (G1 PKG-00..02, G2 PKG-03,
G3 PKG-04..07, G4 PKG-08..10) under one brief and returned CSV rows and notes;
the manager integrated them with `build_account.py`, adding the destination
class, the apply mode, the three decision columns and the removal readiness.
It changed no child cell except four exact repairs after verifier review 01,
each marked "[Manager repair after review 01 …]" in the row (DEL-04-01-REM-001
and -002, DEL-02-07-REM-004, DEL-01-05-REM-003). Hashes and attribution are in
`SEMANTIC_RUN_BASIS.md`. A child's evidence cites line numbers at the
checkout it read; the checks in `verify_d99.py` recompute what matters for
closure.
