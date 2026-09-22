<!-- PACKET
id: P-21
cluster: CL-21
title: App-owned Runtime service, Runtime extraction, contracts facade
question: For rows still describing the per-user daemon, LaunchAgent, in-App runtime code or the harness-contract package where D-GOV-43 topology A2 and the Runtime extraction now apply, does the text follow the ruled design, with any still-missing parts recorded as open work?
recommended: B — A, but hold 3 rows for P-12 and P-04
depends_on: P-04, P-09, P-12
decision_type: owner; engineering (only for P-21.b rows the owner names)
tier: GOVERNING
-->
# P-21 — App-owned Runtime service, Runtime extraction, contracts facade

Cluster CL-21 · no named question · draft by TASK D4 for HELP_HUMAN review; not a ruling.

**Question.** These rows still describe the old architecture:
- a per-user daemon with a LaunchAgent and per-root homes;
- runtime behaviour inside the App;
- the `harness-contract` package as the contract source.

The ruled design has changed each of these. The App now starts and owns a Runtime service child (topology A2). The runtime lives in `projects/chirality-runtime`. `@chirality/runtime-contracts` is the contract package, and `harness-contract` is a deprecated facade. Does the owner authorize the text-repair class?
- **P-21.a** (125 rows): text out of date, built differently as ruled, retired or already permitted. Repair or confirm the text.
- **P-21.b** (14 rows): partly built. Record what is built and add the rest as open work, or name rows for code.

## What we found
- D-APP-127 applies D-GOV-43 topology A2: the App owns a Runtime service child, the LaunchAgent and installer (DEL-09-07, APP-HOLD-1) are retired, and per-root homes are superseded. [GOVERNING]
- The live service host is `frontend/electron/runtime-service-host.ts` (no LaunchAgent). [code]
- The App depends on `@chirality/runtime-contracts` (`file:../../chirality-runtime/packages/contracts`, `frontend/package.json:51`). [code]
- The `frontend/packages/harness-contract` facade is marked deprecated, with the message "Use @chirality/runtime-contracts… will be removed after one migration cycle". [code]
- Of the 20 "retired by a ruling" rows, 15 are DEL-09-07, whose text D-APP-127 preserves as history. Four are decision rows it supersedes, or keeps as history along with DEL-09-07 (D-APP-88, 100, 104 and 107). They need no text change beyond confirming the history label. [GOVERNING]
- 36 PRIMARY rows carry both LIVE and LEGACY_ONLY evidence. The retained daemon-era code sits beside the live service, but live code meets each of these claims, so none cites R4-Q1. [run finding]
- Two P-21.b rows are secret-handling gaps on the live path:
  - DEL-03-04#CLM-009.10: no secret avoidance was found on the live event writer;
  - DEL-05-03#CLM-010.5: live App Server stderr is redacted for e-mail addresses only.

  This is the same finding as the unredacted-event-storage cluster (CL-12). [run finding]
- SOW-064.2: the effective Codex home shares the user's configuration. This is the unfiltered `~/.codex` question in R4-Q6. [run finding]

## Affected rows
<!-- COUNTS -->
**139 rows are decided in this packet** (PRIMARY); 172 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-21`.

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Old assessment overtaken (`STALE_ASSESSMENT`) | Verification out of date (`STALE_VERIFICATION`) | Difference already permitted (`ACCEPTED_DIVERGENCE`) | Retired by a ruling (`RETIRED_BY_RULING`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| EXT | 2 | 1 | 5 |  |  | 1 | 5 |  | 14 |
| PKG-01 |  |  | 3 | 2 |  |  |  |  | 5 |
| PKG-02 |  | 2 | 3 |  |  |  |  | 1 | 6 |
| PKG-03 | 5 | 11 | 34 | 1 |  |  |  |  | 51 |
| PKG-04 |  | 1 | 3 |  |  |  |  |  | 4 |
| PKG-05 | 5 |  | 16 |  |  | 3 |  |  | 24 |
| PKG-06 |  |  | 6 |  |  |  |  |  | 6 |
| PKG-08 |  |  | 3 |  |  |  |  |  | 3 |
| PKG-09 | 2 | 2 | 5 |  | 2 |  | 15 |  | 26 |
| **Total** | **14** | **17** | **78** | **3** | **2** | **4** | **20** | **1** | **139** |

By sub-question (`R4/PACKET_SUBQUESTIONS.csv`):

- P-21.a: 125 rows — Text out of date 78, Retired by a ruling 20, Built differently 17, Difference already permitted 4, Old assessment overtaken 3, Verification out of date 2, To-do list out of step 1
- P-21.b: 14 rows — Partly built 14

ALSO/CONTEXT members by Disposition: Partly built 43, Text out of date 39, Built differently 32, Written, not built 26, Governing texts disagree 20, To-do list out of step 6, Verification out of date 4, Unknown 2.

<!-- /COUNTS -->
PKG-03 (51), PKG-09 (26) and PKG-05 (24) have the most rows. The split is by Disposition (`_work/SUBQ/P-21_subq.csv`; rule in `_work/D4_scripts/subq.py`): "partly built" rows go to P-21.b. The 172 ALSO rows are decided in their own packets (P-09 74, P-15 19, P-02 15, P-12 13, P-05 11 and others).

## Options
**A. Text follows the ruled A2 and extraction design; gaps recorded as open.** *R5 would:* rewrite the P-21.a text to the App-owned service, the Runtime package location and `runtime-contracts`. The daemon and LaunchAgent wording is kept as history where D-APP-127 preserves it, and the history labels on the retired DEL-09-07 rows are confirmed. For P-21.b, R5 states what is built and records each missing part as a Remaining item, or marks it no longer required where D-GOV-43 retires the premise.
**B. As A, but hold the secret-handling and shared-home rows for their packets.** DEL-03-04#CLM-009.10 and DEL-05-03#CLM-010.5 wait for P-12 (redaction on the live path). SOW:SOW-064.2 waits for P-04 (R4-Q6). If either packet chooses a code change, the brief there covers these rows.
**C. Defer the class.**

## HELP_HUMAN recommendation (draft)
Option B. It is Option A for everything except three rows whose right answer depends on a live-path or authority ruling made elsewhere. The architecture itself is ruled and built, so the rest is text catch-up. Removing the facade once its "one migration cycle" has passed is an engineering choice, not proposed here.

## Who decides
The owner authorizes the class. Engineering decides any code change through a bounded brief (for example, from P-12). The Runtime package's own records (`projects/chirality-runtime/execution/**`) belong to the Runtime loop and are not touched. D-GOV-43 is Root's and is applied here, not amended.

## On ruling
1. The consolidated R4 ruling record (the next free D-APP ID, committed by HELP_HUMAN) carries a P-21 clause for the `PACKET_INDEX.csv` P-21 PRIMARY keys, by sub-question. It names the three rows held under B.
2. R5 tranche managers per package make the edits, after P-04, P-09 and P-12 in any deliverable that shares their rows.
3. Checks: the validator, an R6 backcheck of every listed row, and an independent review. For gate status that belongs to the Runtime, R5 cites App surfaces only (run rule MR-6: Runtime gate status comes only from App records).
4. No lifecycle transition; no D-APP-116..119 rows.

## Risks, contested rows and dependencies
- The contested members are all ALSO rows and are decided in their own packets:
  - DEL-02-05#CLM-003.2 and #CLM-011.3 (spot-refuted: the checker reads them as matching; P-05);
  - DEL-02-05#CLM-025 (S1-035, undecided);
  - DEL-09-04#CLM-022 (S2-031, undecided);
  - DEL-10-01#REM-1 (S3-002: DIRECTIVE §8 per-user daemon versus A2, plausibly an R4-Q6 matter);
  - DEL-06-04#STATE-2, DEL-09-04#CLM-022 and #CLM-023.3 (governing texts disagree, owner question restored by R3).
- DIRECTIVE §8 still describes the per-user daemon (D-GOV-20). Any row whose repair means changing DIRECTIVE wording is a governance amendment (see P-04), not R5 text repair.
