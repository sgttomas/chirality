# RR1 return — PEC Remaining retirement account (INTERIM, INCOMPLETE)

Status: **INCOMPLETE — interim handback forced before the semantic account,
draft packet and verifier were finished.** Nothing was applied. This return
must not be read as a finished account or a passed review.

Brief: `scratchpad/closeout/RR1_REMAINING_RETIREMENT_ACCOUNT.md`, SHA-256
`e0bda78f24357181457409b5f035e7b2717d32f9e3c20ab6584a5ceca6486227` (verified).
Role WORKING_ITEMS (`agents/AGENT_WORKING_ITEMS.md` `9ae4bea2…9665`). Root
`AGENTS.md` `c8ce87ef…1dffd`; `projects/pec/AGENTS.md` `c9d3b44d…197a`.
Branch `claude/pec-remaining-retirement-account` from `origin/main` `6281273fa`.

## Done

- **Census** (`TM_PEC_REMAINING_RETIREMENT_2026-09-26/REMAINING_CENSUS.csv`,
  `b0e25361…45eb4`): 57 sections, 89 live items + 3 frozen DEL-01-05 carrier
  items = 92 unique keys. Matches D-PEC-83 exactly: 57 carriers / 89 items
  applied (Receipt 174), 1 frozen carrier (3 items) excluded, 92 proposed.
  Item text, `Depends:` and gates are byte-identical to `PROPOSED_ITEMS.csv`.
  Classes: ORDINARY_OPEN 82 (EVIDENCE 70, PRODUCT_OBLIGATION 6, DOCUMENTARY
  6); TICKED 3 (DEL-01-03, D-PEC-87 L-1a); RETIRED_CLOSED_UNEXECUTED 4
  (DEL-06-04, 07-02, 07-04, 07-05; SCA-005 cp3); FROZEN_UNAPPLIED 3.
  No section is on a CHECKING or ISSUED deliverable.
- **Comparison** (`CENSUS_COMPARISON.md`) and **federation preflight**
  (`FEDERATION_PREFLIGHT.md`: COMPLETE, 4 registers, 28 findings, none PEC,
  0 writes).
- Reliance-hold preflight: register empty; ALLOW for 102 targets under
  `historical-read-only-inspection` and `exact-correction-preparation`.
- Four `pec-task` semantic children dispatched (groups G1–G4) under brief
  `scratchpad/rr1/briefs/RR1_SEM_TASK_BRIEF.md` (`f39f7821…90c9`); still
  running at handback; their outputs are not integrated.

## Not done

- Semantic decision account, run basis, draft D-PEC-99 (provisional) packet
  and generator (template drafted in scratch only), verifier verdicts, PR.

## Dependencies and findings for the caller

- PR #943 (SCA-006 cp3) is open; its owner-approved amendment-1 hunk gives
  `projects/pec/AGENTS.md` `4400c4e9…139c`, the basis the instruction change
  must be drafted against. LOOP_INIT has no Remaining mention.
- Work-graph nodes S1/S2/S4 will rewrite SOWs that would receive transferred
  text (DEL-02-07 in S2; DEL-04-01/02/03 in S4): sequencing must be settled.
- Notices likely needed: Root (alignment manual line 60 describes PEC's loop
  as Remaining-based) and Runtime (DEL-02-06 pins `projects/pec/AGENTS.md`).
- 73 held/conditional D-PEC-83 residuals were never in Remaining; outside
  the census.
