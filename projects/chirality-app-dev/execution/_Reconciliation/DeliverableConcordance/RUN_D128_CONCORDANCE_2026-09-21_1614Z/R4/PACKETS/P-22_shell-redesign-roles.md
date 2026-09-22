<!-- PACKET
id: P-22
cluster: CL-22
title: Woven dialogue shell redesign, text catch-up
question: For shell-redesign rows under SCA-APP-010, D-APP-74 and D-APP-108 (and four role-adoption rows), does the text follow the woven dialogue shell as built, with still-missing parts recorded as open work?
recommended: A — text follows the built shell
depends_on: P-06
decision_type: owner; engineering (only for P-22.b rows the owner names)
tier: GOVERNING
-->
# P-22 — Woven dialogue shell redesign, text catch-up

Cluster CL-22 · no named question · draft by TASK D4 for HELP_HUMAN review; not a ruling.

**Question.** These rows describe the old shell: a matrix, Workbench and Pipeline surfaces, a sidebar toolkit and a working-root bar. D-APP-74 and SCA-APP-010, with D-APP-108 seating the latter, replaced that shell with the woven dialogue shell and its Agents coordination view. The rows need no new direction. Does the owner authorize the text-repair class?
- **P-22.a** (61 rows): text out of date, built differently as ruled, built but not written down, retired or already permitted. Repair or confirm the text.
- **P-22.b** (14 rows): partly built. A surface or display exists only on an unmounted legacy component. Record what the live shell does and add the rest as open work, or name rows for code.

## What we found
- D-APP-74 replaced the fixed shell and matrix with Woven Dialogue and a Work/Agents Coordination Panel. [GOVERNING]
- D-APP-108 seated the SCA-APP-010 shell-redesign items and ruled Q3: the retired `/workbench` and `/pipeline` routes "stay reachable by URL and unlisted; no 404". [GOVERNING]
- SCA-APP-010 is accepted, but its record reads `OPEN_PENDING_DERIVATIVE_CLOSURE` (RUN_BASIS §5). [GOVERNING]
- The 22 "retired by a ruling" rows are DEL-02-02 (the Workbench and Pipeline selection UX), whose text D-APP-108 preserves as history. The 15 "difference already permitted" rows (DEL-08-03 8, DEL-02-01 6, the D-APP-96 row 1) each cite a permitting ruling, and they need only a check that the text says so. [run finding]
- `app/not-found.tsx` still renders the legacy `AppShell`. Every other route renders only the woven shell (XPF-050). [code]
- The working-root controls in `components/shell/shell-frame.tsx` render only when `renderWorkspaceContent` is absent, which the live woven shell never leaves absent. [code]
- The P-22.b gaps:
  - DEL-01-03#CLM-009.1 and #CLM-009.6: the professional-posture wording, and the "does not confirm approvals" notice, are shown only on components that tests reach;
  - DEL-02-04#CLM-005.1: the toolkit panel mounts only under `not-found`;
  - DOC:RELIANCE#13.1, #13.4 and #13.6: the Work projection and context receipts are retired fields.

  [run finding]
- 4 rows (DEL-08-01#CLM-006, #CLM-009.3, #REM-1 and #REGISTER-5) come from the 2026-09-09 role adoption. Their text follows whatever P-06 rules. [run finding]

## Affected rows
<!-- COUNTS -->
**75 rows are decided in this packet** (PRIMARY); 73 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-22`.

| Package | Built, not written down (`IMPLEMENTED_UNDOCUMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Difference already permitted (`ACCEPTED_DIVERGENCE`) | Retired by a ruling (`RETIRED_BY_RULING`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| EXT |  | 4 |  |  | 1 |  |  | 5 |
| PKG-01 |  | 2 |  |  |  |  |  | 2 |
| PKG-02 |  | 4 | 2 | 13 | 6 | 22 | 1 | 48 |
| PKG-05 |  |  |  |  |  |  | 1 | 1 |
| PKG-07 |  | 2 |  |  |  |  |  | 2 |
| PKG-08 | 1 | 2 |  | 4 | 8 |  | 1 | 16 |
| PKG-09 |  |  |  |  |  |  | 1 | 1 |
| **Total** | **1** | **14** | **2** | **17** | **15** | **22** | **4** | **75** |

By sub-question (`R4/PACKET_SUBQUESTIONS.csv`):

- P-22.a: 61 rows — Retired by a ruling 22, Text out of date 17, Difference already permitted 15, To-do list out of step 4, Built differently 2, Built, not written down 1
- P-22.b: 14 rows — Partly built 14

ALSO/CONTEXT members by Disposition: Partly built 24, Built differently 20, Written, not built 18, Verification out of date 5, Retired by a ruling 3, Text out of date 2, Old assessment overtaken 1.

<!-- /COUNTS -->
PKG-02 (48) and PKG-08 (16) have the most rows. The split is by Disposition (`_work/SUBQ/P-22_subq.csv`; rule in `_work/D4_scripts/subq.py`): "partly built" rows go to P-22.b. The 73 ALSO rows are mostly P-06 PRIMARY rows (66) and are decided there.

## Options
**A. Text follows the built woven shell; gaps recorded as open.** *R5 would:* rewrite the P-22.a text to the woven dialogue shell, Agents view and retired-route posture. It confirms the history labels on the retired DEL-02-02 rows and records the one undocumented dispatch contract (DEL-08-03#CLM-006). For P-22.b, R5 states what the live shell shows and adds a Remaining item for each display the shell still owes, or marks it retired where D-APP-108 or SCA-APP-010 retired it.
**B. As A, plus a code brief for named P-22.b rows.** The most likely candidate is the professional-posture and "does not confirm approvals" wording (DEL-01-03#CLM-009.1 and #CLM-009.6), because it is a reliance notice the live shell does not show. A small brief could also point `not-found` at the woven shell.
**C. Defer.**

## HELP_HUMAN recommendation (draft)
Option A, with the owner considering B for DEL-01-03#CLM-009.1 and #CLM-009.6. The redesign is ruled and shipped, and the text only lags. The reliance-notice rows are the exception worth a look. They concern what a user is told about professional reliance, and the live shell shows no such statement.

## Who decides
The owner authorizes the class and names any rows for code. Engineering decides the implementation through a bounded brief. Nothing here is outside the owner's App authority. The role-adoption rows inherit P-06's answer, including its Root boundary.

## On ruling
1. The consolidated R4 ruling record (the next free D-APP ID, committed by HELP_HUMAN) carries a P-22 clause for the `PACKET_INDEX.csv` P-22 PRIMARY keys, by sub-question.
2. R5 tranche managers for PKG-02, PKG-08 and the other packages make the edits in the same tranche as the P-06 rows of those deliverables, and after the P-06 ruling.
3. Checks: the validator, an R6 backcheck of every listed row, and an independent review.
4. No lifecycle transition; no D-APP-116..119 rows.

## Risks, contested rows and dependencies
- `DEL-02-03#CLM-009.3` (spot check S1-024 refuted): the sealed value is "built differently", but the checker reads the row as matching, because clearing the root sets it to null and the composer then blocks. The sealed value stands, and the owner may accept the checker's reading. The text repair is small either way.
- DEL-02-01#REM-6 (least confident): the index-plus-polling design may already be what "spans every known root" meant. If so, R5 closes the item instead of rewording it.
- This packet depends on P-06: if P-06 chooses B (restore the old model in code), the 4 role-adoption rows and the P-06 overlap reverse direction.
