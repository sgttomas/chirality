<!-- PACKET
id: P-19
cluster: CL-19
title: Differences that predate v3
question: For divergences already present before 2026-08-22, does the text follow the code (text-shaped rows), and are the unbuilt or partly built parts recorded as open work rather than built now?
recommended: A — text follows code; gaps recorded as open
depends_on: P-18
decision_type: owner; engineering (only for rows the owner names under P-19.b)
tier: mixed
-->
# P-19 — Differences that predate v3

Cluster CL-19 · no named question · draft by TASK D4 for HELP_HUMAN review; not a ruling.

**Question.** These divergences already existed before the v3 push began on 2026-08-22. No v3 mechanism explains them, and for 94 of the rows no decision record explains them either. Which side changes?
- **P-19.a** (208 rows): rows whose defect is the text — text out of date, a to-do list out of step, an old assessment or verification, plus rows already retired or permitted. Should the text follow the code?
- **P-19.b** (52 rows): rows where part of what the deliverable asks for was never built, or was built differently: "partly built", "built differently" or "written, not built". Should the missing part be recorded as open work in the deliverable, or should code be written?

## What we found
- In 94 PRIMARY rows, the worker searched the App register and the CONTEXT sources and found no direction (LatestDecision `NONE_FOUND`). Most of the rest cite D-APP-56, the July concordance ruling, whose repairs predate v3. [run finding]
- Many gaps trace to the initial repository import, `7bee9ae41` (2026-05-18): DEL-07-05 register reading (invalid registers read without findings) and DEL-02-03 typed-error display. [code]
- DEL-07-03#CLM-030: the code deliberately reports an OPEN baseline with no production contract as not valid. This came in with `bb8ae7424` (2026-07-13), while SPEC §3.1 still describes the older behaviour. [code]
- DEL-09-05#CLM-010.4: the App-local premerge workflow (`projects/chirality-app-dev/.github/workflows/`, unchanged since `7bee9ae41`) still pins Node 20 and sets `ANTHROPIC_API_KEY`, while `frontend/package.json` requires Node `>=22.19.0`. [code]
- DEL-03-03: the SSE compatibility fixtures and UI event documents were never produced (two of the five documents exist). INSP-03 recorded the gap on 2026-06-20. [run finding]
- DEL-10-03: several rows restate CONTRACT K-DOMAIN-4 more narrowly (for example, omitting `ready-for-construction`), and no ruling narrows it. [GOVERNING]
- 70 PRIMARY rows are governance-invariant, and 11 are PRD-level. [run finding]

## Affected rows
<!-- COUNTS -->
**260 rows are decided in this packet** (PRIMARY); 118 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-19`.

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Old assessment overtaken (`STALE_ASSESSMENT`) | Verification out of date (`STALE_VERIFICATION`) | Difference already permitted (`ACCEPTED_DIVERGENCE`) | Retired by a ruling (`RETIRED_BY_RULING`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| EXT |  |  |  | 6 |  |  |  | 2 |  | 8 |
| PKG-00 |  | 1 |  | 8 |  |  |  |  | 1 | 10 |
| PKG-01 |  | 2 |  | 11 |  |  |  |  |  | 13 |
| PKG-02 |  | 2 |  | 12 |  |  |  |  | 1 | 15 |
| PKG-03 |  | 8 |  | 5 |  |  |  |  |  | 13 |
| PKG-04 |  | 1 |  | 11 |  |  |  |  | 2 | 14 |
| PKG-05 |  | 2 |  | 9 |  |  |  |  |  | 11 |
| PKG-06 |  | 1 | 1 | 18 |  |  |  |  | 2 | 22 |
| PKG-07 | 1 | 12 | 3 | 16 | 1 |  | 1 |  | 1 | 35 |
| PKG-08 |  | 7 |  | 8 |  |  |  |  |  | 15 |
| PKG-09 |  | 4 |  | 25 |  |  |  |  | 2 | 31 |
| PKG-10 |  | 7 |  | 57 |  | 2 |  |  | 7 | 73 |
| **Total** | **1** | **47** | **4** | **186** | **1** | **2** | **1** | **2** | **16** | **260** |

By sub-question (`R4/PACKET_SUBQUESTIONS.csv`):

- P-19.a: 208 rows — Text out of date 186, To-do list out of step 16, Verification out of date 2, Retired by a ruling 2, Difference already permitted 1, Old assessment overtaken 1
- P-19.b: 52 rows — Partly built 47, Built differently 4, Written, not built 1

ALSO/CONTEXT members by Disposition: Partly built 61, Text out of date 44, Governing texts disagree 5, Verification out of date 4, Built differently 3, Unknown 1.

<!-- /COUNTS -->
Every package is affected; PKG-10 has the most (73). P-19.a and P-19.b are split by Disposition, with the rule written in `_work/D4_scripts/subq.py`: "partly built", "written, not built" and "built differently" rows go to P-19.b (`_work/SUBQ/P-19_subq.csv`). Most P-19.b rows are missing tests or fixtures, or missing validation reports, rather than missing product features.

## Options
**A. Text follows code; gaps recorded as open work.** *R5 would:* repair the P-19.a text to what the code does. For P-19.b, the requirement text stays; R5 corrects only false "built" or "done" assertions and adds the unbuilt part as a Remaining item under the `_STATUS` contract, with its gate. Any narrowing of a requirement goes to WORKING_ITEMS (scope-change). This leaves no false claim and builds nothing now.
**B. As A, plus a code brief for named rows.** The owner names the P-19.b rows whose gap should be closed in code. Candidates are the governance-invariant rows: DEL-07-05 register validation, DEL-07-01#CLM-011.11 (tree and scope routes skip the instruction-root check) and the DEL-10-03 K-DOMAIN-4 rows. A separate `software-bounded-implementation` brief carries them, and those rows wait for it.
**C. Accept the divergences.** The ruling permits them, and R5 records each one as "difference already permitted". This suits only rows where the code's behaviour is the better one, such as DEL-07-03#CLM-030.
**D. Defer.** The rows stay held.

## HELP_HUMAN recommendation (draft)
Option A as the class default, with B left open. These differences are old, and v3.0.0 and v3.0.1 shipped with them. Recording them truthfully as open work takes no position on building them, while writing code now would widen the v3 closeout. If the owner wants any rows built, B names them explicitly. The obvious candidate is DEL-07-01#CLM-011.11, because it concerns a path guarantee on the live path. HELP_HUMAN does not recommend C as a class, because it would turn unrecorded judgment into permitted difference without the owner looking at each row.

## Who decides
The owner, for the class and for any rows named under B. Engineering decides the implementation through a bounded brief. The premerge workflow row (DEL-09-05#CLM-010.4) concerns the App-local workflow file. CI actually runs from the repository-root workflow, which sits outside App scope. R5 edits only the deliverable text; changing either workflow file would need its own brief.

## On ruling
1. The consolidated R4 ruling record (the next free D-APP ID, committed by HELP_HUMAN) carries a P-19 clause. It records the chosen option per sub-question and lists any rows named for code under B.
2. R5 tranche managers per package edit the `PACKET_INDEX.csv` P-19 PRIMARY rows. P-19.a gets text repair. P-19.b keeps its requirement text; false "built"/"done" assertions are corrected and a Remaining item is added for each unbuilt part under the `_STATUS` contract, citing the ruling. Requirement narrowing, if wanted, is a scope-change handoff.
3. Rows named under B stay held until their implementation brief returns.
4. Checks: the validator, an R6 backcheck of every listed row, and an independent review per tranche. No lifecycle transition; no D-APP-116..119 rows.

## Risks, contested rows and dependencies
- `DEL-10-03#CLM-025.2` (spot check S1-172, undecided): is a narrower restatement of K-DOMAIN-4 "partly built" or "text out of date"? Under A, both are repaired by restating the clause in full.
- Four of the 9 rule 2b tie-break moves are here (DEL-06-04#REGISTER-2, DEL-07-02#REGISTER-2, DEL-09-03#REGISTER-3, DEL-10-05#REGISTER-3); see P-18.
- ALSO members are decided elsewhere, mostly in P-09 (80):
  - `DEL-06-02#CLM-005` is owner-deferred (P-01).
  - `DEL-06-04#CLM-027`: spot check S1-112 refuted its Disposition.
  - `DEL-10-04#CLM-016.1` (S2-047): governing texts disagree on who owns `pec.yaml`.
  - `DEL-09-05#CLM-010.8`: the owner-check reading is undecided (OC-05).
- Where a row's `_REFERENCES` hash is stale, the fix is the P-18 corpus bump.
