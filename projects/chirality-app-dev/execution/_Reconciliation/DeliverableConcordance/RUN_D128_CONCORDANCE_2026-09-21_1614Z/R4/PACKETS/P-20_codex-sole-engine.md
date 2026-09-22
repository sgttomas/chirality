<!-- PACKET
id: P-20
cluster: CL-20
title: Codex as the only engine, and Codex-held credentials
question: For rows where the deliverable text still assumes the Claude SDK, the Anthropic key or Pi, while D-GOV-43 and D-APP-127 made Codex the only engine and credential custodian, does the text follow the ruled Codex design, with any still-missing parts recorded as open work?
recommended: A — text follows ruled Codex design
depends_on: P-04, P-05, P-09
decision_type: owner; engineering (only for P-20.b rows the owner names)
tier: GOVERNING
-->
# P-20 — Codex as the only engine, and Codex-held credentials

Cluster CL-20 · no named question (the related ones are decided in P-04, P-05 and P-09) · draft by TASK D4 for HELP_HUMAN review; not a ruling.

**Question.** In these rows, the deliverable text still assumes the Claude Agent SDK, an Anthropic key, Pi or daemon-held login. The ruled design is different: Codex is the only engine, and Codex holds the login. The rows need no new direction. Does the owner authorize the text-repair class?
- **P-20.a** (100 rows): text out of date, or built differently in the way the ruling says. Repair the text to the ruled Codex design.
- **P-20.b** (17 rows): partly built. The live Codex path meets part of the claim, and the rest is either no longer required or not yet built. Record what is built, and record the rest as open work, or name rows for code.

## What we found
- The App CONTRACT preamble, as amended under D-GOV-43, requires Codex account sign-in. The App hosts the stock, lockfile-pinned `codex app-server` inside a Runtime service the App starts and owns (`docs/CONTRACT.md:17`). [GOVERNING]
- D-APP-127 applies D-GOV-43 to the App. It supersedes D-APP-126 (daemon credential custody) and D-APP-125 item 3. [GOVERNING]
- K-KEY-1 (amended) treats credentials, OAuth tokens and App Server keyring state as private, non-project state. Under DIRECTIVE §0 it prevails over unamended SPEC §12.3 and PRD FR-031, so those rows are text-out-of-date, not a conflict (worker reading on DEL-05-03#CLM-004). [GOVERNING]
- Live login is Codex's own (`chirality-runtime/packages/daemon/src/codex-login.ts`), and tools, approvals, sandbox and writes are Codex built-ins answered through the request card (SOW-047.2 to SOW-062.2 rows). [code]
- 40 PRIMARY rows (32 in P-20.a, 8 in P-20.b) carry both live Codex path and legacy harness evidence. The legacy harness still holds the Claude and Anthropic paths, but live code meets each of these claims, so none cites R4-Q1 (the named question on the legacy harness, P-09). [run finding]
- What the P-20.b rows are missing on the live path:
  - DEL-05-03#CLM-010.4: typed failures, without the seven-class taxonomy;
  - DEL-06-05#CLM-009.11: a command timeout cannot be told apart from other failures;
  - DEL-02-05#CLM-013.2: the key panel is never shown in hosted Settings.

  [run finding]

## Affected rows
<!-- COUNTS -->
**117 rows are decided in this packet** (PRIMARY); 517 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-20`.

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Old assessment overtaken (`STALE_ASSESSMENT`) | Verification out of date (`STALE_VERIFICATION`) | Retired by a ruling (`RETIRED_BY_RULING`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| EXT | 2 | 8 | 5 |  |  | 2 |  | 17 |
| PKG-01 | 2 | 4 |  |  |  |  | 1 | 7 |
| PKG-02 | 1 | 4 | 7 |  |  |  |  | 12 |
| PKG-03 |  |  | 31 |  |  |  |  | 31 |
| PKG-04 |  | 1 | 5 |  |  |  |  | 6 |
| PKG-05 | 1 | 3 |  |  | 2 |  |  | 6 |
| PKG-06 | 1 | 3 | 4 | 1 |  |  |  | 9 |
| PKG-08 | 2 |  |  |  |  |  |  | 2 |
| PKG-09 | 8 |  | 14 |  |  |  |  | 22 |
| PKG-10 |  |  | 5 |  |  |  |  | 5 |
| **Total** | **17** | **23** | **71** | **1** | **2** | **2** | **1** | **117** |

By sub-question (`R4/PACKET_SUBQUESTIONS.csv`):

- P-20.a: 100 rows — Text out of date 71, Built differently 23, Verification out of date 2, Retired by a ruling 2, To-do list out of step 1, Old assessment overtaken 1
- P-20.b: 17 rows — Partly built 17

ALSO/CONTEXT members by Disposition: Partly built 147, Governing texts disagree 143, Built differently 84, Text out of date 71, Written, not built 52, Verification out of date 15, Difference already permitted 3, Lifecycle needs reassessing 2.

<!-- /COUNTS -->
The rows cover engine choice, SDK session and tool wording, provider keys and login custody. PKG-03 (31) and PKG-09 (22) have the most. The split is by Disposition (`_work/SUBQ/P-20_subq.csv`; rule in `_work/D4_scripts/subq.py`): "partly built" rows go to P-20.b. The 517 ALSO rows are decided in their own packets (P-09 342, P-04 75, P-05 39, P-08 20 and others), not here.

## Options
**A. Text follows the ruled Codex design; gaps recorded as open.** *R5 would:* rewrite the P-20.a text to the Codex-hosted design, citing D-GOV-43, D-APP-127 or amended K-KEY-1 as each row records. Claude, Anthropic and Pi wording is kept as history where a ruling preserves it, and otherwise removed. For P-20.b, R5 states what is built and adds a Remaining item for each part still required, or marks it no longer required where D-GOV-43 retires its premise (`MOOT:` in the record).
**B. As A, plus a code brief for named P-20.b rows.** The candidates are the failure taxonomy (DEL-05-03#CLM-010.4) and timeout distinction (DEL-06-05#CLM-009.11). A separate implementation brief, issued in the Runtime project loop (these are live Runtime paths), carries them, and those rows wait for it.
**C. Defer.** The rows stay held until P-04, P-05 and P-09 are ruled.

## HELP_HUMAN recommendation (draft)
Option A. D-GOV-43 and D-APP-127 already rule the direction, the code follows them, and R3 found no owner question on any PRIMARY row. The sequence the owner gave for R4-Q6 (Codex-hosted first, local models later, an API path no sooner) points the same way. That answer is CONTEXT until the R4 ruling records it, and it is not relied on here. A leaves open whether the P-20.b gaps are worth building, which the owner can take up under B.

## Who decides
The owner authorizes the class and names any rows for code. Engineering decides the implementation through a bounded brief. D-GOV-43 is a Root decision: this packet applies it and does not amend it, and any change to D-GOV-43 itself routes to Root.

## On ruling
1. The consolidated R4 ruling record (the next free D-APP ID, committed by HELP_HUMAN) carries a P-20 clause for the `PACKET_INDEX.csv` P-20 PRIMARY keys, by sub-question.
2. R5 tranche managers per package make the edits. Where a deliverable also holds P-04 (R4-Q6), P-05 (R4-Q5) or P-09 (R4-Q1) rows, its tranche runs after those rulings, so one section is not rewritten twice or in opposite directions.
3. Checks: the validator, an R6 backcheck of every listed row, an independent review, and the secret scanner on every tranche (placeholder credential URLs; see RUN_BASIS Addendum 11).
4. No lifecycle transition; no D-APP-116..119 rows.

## Risks, contested rows and dependencies
- **P-05 dependency.** DEL-06-06#CLM-004.2, #CLM-010.1 and #CLM-025.1 describe unfamiliar Codex payloads kept raw instead of translated. That is the R4-Q5 matter, so their text direction should follow P-05's answer even though they are PRIMARY here.
- **P-04 dependency.** DEL-02-05#CLM-013.2 (the Anthropic key panel) touches the R4-Q6 key-UI question, so it follows P-04.
- The contested and spot-refuted members are all ALSO rows and are decided in their own packets:
  - S1-022, S1-055, S2-009, S2-013, S2-028 and S2-043;
  - the undecided items DEL-04-04#CLM-024 and DEL-04-05#CLM-024;
  - S1-070 and S2-059;
  - `DEL-06-02#CLM-032` (owner-deferred, P-01).
- R3 left one reading open: 11 rows treat the "Claude/Anthropic default" statement as governing texts disagreeing, and 23 as text out of date (RUNWIDE_CALLS call d). Any of them that are PRIMARY here are repaired as text only after P-04 confirms the reading.
