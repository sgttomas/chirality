<!-- PACKET
id: P-10
cluster: CL-10
title: Rows waiting on existing or pending decisions
question: For rows that name an existing decision, do you agree that rows on unruled D-APP-116..119 stay held, and that rows on already-ruled decisions are repaired to what those decisions settle?
recommended: A — hold a; repair b and c
depends_on: none
decision_type: owner; WORKING_ITEMS (review)
tier: GOVERNING
-->
# P-10 — Rows waiting on existing or pending decisions

Cluster CL-10 · no named question · draft by TASK D2 for HELP_HUMAN review; not a ruling.

**Question.** These rows name an existing decision as what they wait on. The packet asks you to confirm how each group is handled; it does not re-rule those decisions.

Three sub-questions, split by script (`R4/_work/D2_scripts/d2_p10_subq.py`; `R4/_work/SUBQ/P-10_subq.csv`):
- **P-10.a (8 rows):** the row names D-APP-116, 117, 118 or 119. These are still AWAITING_RULING, so the rows stay held.
- **P-10.b (5 rows):** otherwise, the row names D-APP-127 or D-GOV-43. Those decisions are ruled and already retired the row's premise.
- **P-10.c (5 rows):** otherwise, the row names another ruled decision: D-APP-73, D-APP-43 or D-APP-121.

## What we found
- **Held until ruled.** D-APP-116 (tool-result audit policy), 117 (per-attempt decision evidence), 118 (facade retirement) and 119 (the organisation-layer boot seam, or deferral of DEL-07-01-V3-01) are AWAITING_RULING (`execution/_Coordination/_DECISIONS/_REGISTER.md:132-137`); the D-APP-128 ruling §5.5.4 holds their rows from R5 (RUN_BASIS §1). [GOVERNING]
- **D-APP-127 (b).** It applies D-GOV-43 to the App and retires per-root consent, daemon credential custody and the typed login transport (register row 152). The four DEL-04-05 rows and `DEL-08-02#REM-1` still describe those premises. Their Notes read MOOT under D-APP-127. [GOVERNING]
- **D-GOV-43 (b).** For `DEL-04-05#CLM-022.4`, D-GOV-43 item 4 now states the network mechanism, so the open ruling request in the text is overtaken. [GOVERNING]
- **D-APP-73 (c).** It moved sessions to a central store and made D-APP-41 historical. The rows `DEL-05-01#CLM-027` and `#CLM-032` still describe the older project-local design. `CLM-032` is an amendment written 2026-09-03 that went to legacy-only App code (row Notes). [run finding]
- **D-APP-43 (c).** It closed REQ-06-03-015 (explicit absence of dependency rows). `DEL-06-03#CLM-010.15` matches. [GOVERNING]
- **D-APP-121 (c).** It is RULED, with its dependent effect HELD. The built-in PDF viewer is still off (`frontend/electron/preload.ts:77`, `inlinePdfPreview: false`). `DEL-09-06#REM-4` matches. `#CLM-014` is partly built, because its SEC-1 and AC-001 disagree about whether the built-in PDF proof applies to this release. [code]
- Ten more rows elsewhere also name D-APP-116..119 alongside an R4-Qn token: 9 in P-09 and 1 in P-05. The same hold applies to them. [run finding]

## Affected rows
<!-- COUNTS -->
**18 rows are decided in this packet** (PRIMARY); 23 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-10`.

| Package | Matches (`ALIGNED`) | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Total |
|---|---:|---:|---:|---:|---:|---:|
| EXT |  |  | 2 |  |  | 2 |
| PKG-02 |  |  | 1 |  |  | 1 |
| PKG-03 | 1 |  |  |  |  | 1 |
| PKG-04 |  | 1 |  | 3 | 1 | 5 |
| PKG-05 | 1 |  |  | 2 |  | 3 |
| PKG-06 | 1 |  |  |  |  | 1 |
| PKG-07 |  |  |  | 1 |  | 1 |
| PKG-08 | 1 |  |  |  | 1 | 2 |
| PKG-09 | 1 |  | 1 |  |  | 2 |
| **Total** | **5** | **1** | **4** | **6** | **2** | **18** |

By sub-question (`R4/PACKET_SUBQUESTIONS.csv`):

- P-10.a: 8 rows — Partly built 3, Matches 3, Written, not built 1, Text out of date 1
- P-10.b: 5 rows — Text out of date 3, To-do list out of step 2
- P-10.c: 5 rows — Text out of date 2, Matches 2, Partly built 1

ALSO/CONTEXT members by Disposition: Text out of date 15, Partly built 4, Written, not built 2, Verification out of date 1, Built differently 1.

<!-- /COUNTS -->
They are mostly Remaining items and status statements. Five "matches" rows are here only because they cite a decision: their open status is correct. The 23 ALSO rows are decided in their own packets, mostly the P-09 DEL-05-01 rows that cite D-APP-73.

## Options
**A. Hold a; repair b and c to their existing decisions.**
- *R5 would not touch* the 8 a-rows, or the 10 other rows that name D-APP-116..119.
- For b-rows, R5 would rewrite the text to D-APP-127 and D-GOV-43 terms, and close or retire the moot Remaining items and the dependency row (`DEL-04-05#REGISTER-4`).
- For c-rows, R5 would edit the text to D-APP-73 (DEL-05-01) and D-APP-121 (DEL-09-06 SEC-1/AC-001 tension). The two c-rows that match (`DEL-06-03#CLM-010.15`, `DEL-09-06#REM-4`) need no edit.

**B. Rule D-APP-116..119 now, each on its own record.**
- Each has its own packet in `_DECISIONS/`; any ruling is recorded on that decision's own ruling record and register row, not folded into the R4 record.
- *R5 would then* repair the a-rows to whatever you rule, once the register row reads RULED.
- This widens the present sitting beyond what the run's packets have prepared.

**C. Hold everything in this packet.** Nothing is repaired until a separate decision review.

## HELP_HUMAN recommendation (draft)
Option A:
- The held decisions have their own packets and gates.
- The b and c rows need no new ruling. They only need their text brought to decisions you already made.

**Left open:** D-APP-116..119 themselves, and `DEL-02-02#REM-1`, whose token also carries plain R4. That R4 concerns the provenance-label direction of 2026-09-07 (CONTEXT). It is not a ruling.

## Who decides
- **Owner:** confirms the handling in this packet. D-APP-116..119 remain the owner's own later rulings.
- **WORKING_ITEMS (review):** checks, row by row, that the b and c repairs match the ruling text.
- Nothing here is outside your App authority.

## On ruling
- **Where recorded.** The consolidated R4 ruling record (next free D-APP ID, committed by HELP_HUMAN) records the handling per sub-question, with the key sets from `P-10_subq.csv`. It also lists the 10 other held rows by key: `DEL-02-02#REM-2`, `DEL-04-04#SEC-1`, `DEL-04-04#REM-1`, `DEL-05-05#CLM-010.12`, `DEL-05-05#CLM-012.8`, `DEL-07-01#SEC-1`, `DEL-07-01#SEC-2`, `DEL-08-04#CLM-011`, `DEL-08-04#CLM-030` and `DEL-10-01#CLM-016.1`. `DEC:D-APP-101` (PRIMARY in P-23.c) is also held until D-APP-118 is ruled, although its HumanDecisionNeeded reads `NO`.
- **R5.** Tranche managers for PKG-04, 05, 08 and 09 edit only the b and c rows. R6 backchecks every edited row.
- **Held rows.** They reopen when the register row for D-APP-116, 117, 118 or 119 becomes RULED.
- No lifecycle transition.

## Risks, contested rows and dependencies
- `DEL-07-01#REM-1` names D-APP-119, but its latest decision is D-APP-127. The text is stale on both counts: a deleted file, and a retired daemon resolver. The stale part could be fixed now, but the packet keeps the whole row held for safety.
- `SOW:SOW-059.2` and `SOW:SOW-084.2` are partly built and wait on D-APP-116 and D-APP-119.
- `DEL-09-06#CLM-014` also cites done-declaration Q-02 (CONTEXT). [CONTEXT]
- There are no spot-check contests. The one owner-check change in the ALSO set (`DEL-09-06#CLM-021`) belongs to P-02.
