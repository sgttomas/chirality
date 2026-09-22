<!-- PACKET
id: P-11
cluster: CL-11
title: Five smaller owner questions no named question covers
question: For each of five themes, which governing text or later direction stands, and so which side changes?
recommended: a amend SPEC; b-c amend text; d-e case by case
depends_on: P-04, P-09, P-21, P-23
decision_type: owner (incl. App governance amendment); WORKING_ITEMS (scope-change)
tier: GOVERNING
-->
# P-11 — Five smaller owner questions no named question covers

Cluster CL-11 · plain R4 rows · draft by TASK D3 for HELP_HUMAN review; not a ruling.

**Question.** These 26 rows need an owner ruling, but none of the named questions R4-Q1..Q6 covers them. They fall into five themes (`R4/_work/SUBQ/P-11_subq.csv`, rule in `R4/_work/D3_scripts/d3_subq_small.py`). Each sub-question asks which side stands.

- **P-11.a — Replay lens or continuation (11 rows; DEL-05-04, DEL-08-02).** SPEC §17.6 says selecting a recorded session opens a read-only lens and "MUST NOT … resume … the primary live session" (`docs/SPEC.md:1026-1032`). The live App resumes a compatible recorded session as the primary conversation, since `0ed1a1a7f` (2026-09-11). No register ruling records this; only v3 CONTEXT explains it. *Question:* keep continuation and amend SPEC §17.6 and PRD FR-008, or restore the read-only lens?
- **P-11.b — Topology text D-GOV-43 undercut without naming it (5 rows).** The unamended decomposition row for DEL-05-01 still asks for "App-client compatibility for daemon-centralized sessions" (`execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md:336`); PKG-06 scope still includes daemon hook conformance (SOW-057); DEL-04-01 still targets a packaged-daemon probe. D-GOV-43 retired the daemon (item 7) but names none of these. *Question:* confirm that D-GOV-43 supersedes these carriers, so the decomposition and deliverable text are amended?
- **P-11.c — Session folder layout (2 rows; DEL-05-01).** SPEC §8.2 (unamended) requires `session.json`, `events.jsonl`, `turns/`, `artifacts/`, `sdk/`. The live store follows the amended K-EVENT-4 Runtime store, and no ruling gives the subfolders. *Question:* amend SPEC §8.2 to the live layout, or require the subfolders in code?
- **P-11.d — Presentation rulings versus later trial direction (3 rows; DEL-02-01, DEL-02-02, DEL-02-05).** Three rulings differ from what shipped:
  - D-APP-108 Q5 ruled "ship the icon", but the trial direction was "no logo in the UI" (`DEL-02-01#REM-7`);
  - the Workflows-view Remaining item (`DEL-02-02#REM-3`);
  - D-APP-122's account-row status, superseded in part by D-APP-127 (`DEL-02-05#SEC-2.2`).

  The later direction is CONTEXT only. *Question:* does the ruling or the later direction stand, row by row?
- **P-11.e — Registry drift and a superseded ruling (5 rows).**
  - `hook.failed` is emitted by legacy code without a SPEC §9.4 amendment (`DEL-06-06#CLM-027`, `#CLM-030`).
  - D-APP-40 reserves `turn.cancelled`, which the live path never writes (`DEL-03-04#CLM-009.7`).
  - D-APP-112 item B's run-based PR boundary was displaced by the 2026-09-19 session-work-graph direction, which does not name it (`DEC:D-APP-112.2`).
  - A network-posture row still names the Anthropic path (`DEL-09-05#CLM-027`).

  *Question:* amend the registry and the ruling to match practice, or restore the ruled behaviour?

## What we found
- SPEC §17.6 and PRD FR-008 still forbid resuming from the replay lens (`docs/SPEC.md:1026-1032`; `docs/PRD.md:603`). [GOVERNING]
- Live continuation of a recorded session arrived in `0ed1a1a7f` (2026-09-11, "Repair trial plans, history, …"). [code]
- D-GOV-43 item 7 retires the daemon but names none of the P-11.b carriers (`docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md`, adopting items 1–14 as written). [GOVERNING]
- The trial direction behind P-11.d ("no logo in the UI") is recorded only in v3 CONTEXT sources, which never change a Disposition. [CONTEXT]
- The replay divergence is an unrecorded judgment: `DEL-05-04#REM-2` carries `CAUSE2:UNRECORDED_JUDGMENT`. [run finding]
- `DEL-06-04#STATE-2` is sealed "Governing texts disagree". Its verifiers read it as needing no owner decision; R3 kept the Disposition and restored plain R4 (R3_SUMMARY §8). The row restates the unamended decomposition, so it belongs to P-11.b. [run finding]
- `DEL-04-01#CLM-009`: the governing row still carries the retired packaged-daemon and supplier premises, so the target scope needs owner framing before repair. [run finding]

## Affected rows
<!-- COUNTS -->
**26 rows are decided in this packet** (PRIMARY); 22 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-11`.

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Difference already permitted (`ACCEPTED_DIVERGENCE`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| EXT |  |  |  | 1 |  |  | 1 |
| PKG-02 | 1 | 1 |  |  |  | 1 | 3 |
| PKG-03 |  | 1 |  |  |  |  | 1 |
| PKG-04 |  |  | 1 |  | 1 |  | 2 |
| PKG-05 | 5 | 3 | 1 |  |  | 1 | 10 |
| PKG-06 |  | 2 |  |  |  | 1 | 3 |
| PKG-08 | 2 | 3 |  |  |  |  | 5 |
| PKG-09 |  |  | 1 |  |  |  | 1 |
| **Total** | **8** | **10** | **3** | **1** | **1** | **3** | **26** |

By sub-question (`R4/PACKET_SUBQUESTIONS.csv`):

- P-11.a: 11 rows — Built differently 6, Partly built 5
- P-11.b: 5 rows — Text out of date 2, Governing texts disagree 2, To-do list out of step 1
- P-11.c: 2 rows — Partly built 2
- P-11.d: 3 rows — Built differently 1, Partly built 1, Governing texts disagree 1
- P-11.e: 5 rows — Built differently 3, Difference already permitted 1, Text out of date 1

ALSO/CONTEXT members by Disposition: Governing texts disagree 10, Partly built 8, Text out of date 3, Built differently 1.

<!-- /COUNTS -->
All 26 PRIMARY rows cite plain R4.

Three rows you might expect here are **not** PRIMARY here:
- **S2-047** (`DEL-10-04#CLM-016.1`) and **S2-059** (`DEL-10-02#CLM-024`) are decided in P-09. S2-047 is an ALSO member here.
- The **"Claude/Anthropic default" statement** belongs to **P-04**. Its 11 rows marked "Governing texts disagree" are all PRIMARY in P-04. The 23 marked "Text out of date" are in P-20 (18) and P-09 (5).

## Options
For each sub-question:

**A. Change the governing or decomposition text** (governance amendment) to match what shipped. *R5 would:* edit the deliverable rows after the amendment tranche lands.

**B. Change the code** back to the governing text. *R5 would:* hold the rows until a separate implementation brief lands.

**C. Accept the divergence**, with the ruling naming the rows. *R5 would:* record the acceptance.

**D. Structural.** Relevant only to P-11.b, where a decomposition row or SOW-057 is retired. This goes as a scope-change handoff.

## HELP_HUMAN recommendation (draft)
- **a: A.** Continuation shipped deliberately, and the trial relied on it. Amend SPEC §17.6 and PRD FR-008 so resuming is governed, keeping the in-flight clobber guard that already holds.
- **b: A, with D for SOW-057.** Confirm that D-GOV-43 supersedes the daemon carriers.
- **c: A.** Amend SPEC §8.2 to the live Runtime store layout.
- **d: decide row by row.** HELP_HUMAN has no basis to prefer trial direction over a ruling.
- **e: A** for the registry names; confirm or retire D-APP-112 item B.

## Who decides
The owner decides each sub-question. Amending App PRD or SPEC text goes through a governance amendment. Retiring a decomposition row or SOW item goes to WORKING_ITEMS (scope-change). Any code is an engineering matter. The decomposition file is App GOVERNING (v3_2), so all of this is within App authority.

## On ruling
1. HELP_HUMAN records each sub-question's answer in the consolidated R4 ruling record: the next free D-APP ID, with its register row.
2. An App governance-amendment tranche handles SPEC §17.6, §8.2 and §9.4, PRD FR-008 and the decomposition rows, by the corpus-bump procedure (D-APP-38 under D-APP-56).
3. The R5 tranche managers for PKG-02, 03, 04, 05, 06, 08, 09 and EXT then edit the P-11 PRIMARY key set in `PACKET_INDEX.csv`, by SubQ.
4. Structural items go by scope-change handoff. Code items go by implementation brief.
5. R6 backchecks every listed row. There is no lifecycle transition.

## Risks, contested rows and dependencies
- `DEL-06-04#STATE-2` was restored to R4 against its verifiers. The owner may instead rule it "no decision needed" under P-11.b.
- ALSO members `DEL-09-04#CLM-022` (S2-031, undecided) and `#CLM-023.3` are decided in their own packets.
- Dependencies:
  - **P-04:** `DEL-02-05#SEC-2.2` and the network row;
  - **P-09:** `hook.failed` is emitted only by legacy code;
  - **P-21:** A2 topology;
  - **P-23:** v3 release scope, for the Remaining items.
