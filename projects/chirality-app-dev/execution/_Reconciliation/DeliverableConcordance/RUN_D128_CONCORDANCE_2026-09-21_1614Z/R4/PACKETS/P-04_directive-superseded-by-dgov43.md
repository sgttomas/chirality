<!-- PACKET
id: P-04
cluster: CL-04
title: Old App DIRECTIVE permission and provider clauses versus D-GOV-43
question: Do you confirm your recorded answer that D-GOV-43 superseded the unamended App DIRECTIVE §2.8, §2.10, §4.1, §4.2 and CONTRACT K-PERM-1/K-PERM-6, and if so, for which rows and in which repair direction?
recommended: A — confirm; narrow reach; text follows code
depends_on: none
decision_type: owner; external authority (Root docs, D-GOV rules)
tier: GOVERNING
-->
# P-04 — Old App DIRECTIVE permission and provider clauses versus D-GOV-43

Cluster CL-04 · named question R4-Q6 · draft by TASK D2 for HELP_HUMAN review; not a ruling.

**Question.** Do you confirm your recorded answer that D-GOV-43 (the 2026-09-11 Root ruling that re-platformed the App on a stock Codex App Server) superseded the unamended App DIRECTIVE §2.8, §2.10, §4.1, §4.2 and CONTRACT K-PERM-1 and K-PERM-6? If you do, which rows does it reach, and which way are they repaired?

This packet is **pre-answered**. It asks you to confirm four things, not to answer the question again:

- **P-04.1 The answer.** Your words, recorded in session on 2026-09-21 (`OWNER_DIRECTION.md` `r2_r4q6_answer`, SHA-256 `9ebeaaa1…27430`): "D-GOV-43 superseded the governance files for the very purpose of publishing this Codex-hosted App first, and in the future local-model hosting, and API after that or no sooner at least." [CONTEXT] It is not a ruling yet; it becomes one only when the R4 ruling record transcribes it.
- **P-04.2 Reach.** Does the answer cover only the six listed texts (the narrow reading), or App DIRECTIVE versus D-GOV-43 in general (the broad reading)? The broad reading adds K-PERM-3/4/5, K-NET-1 (network egress), K-SDK-1 (settings isolation) and DIRECTIVE §8 (the per-user daemon).
- **P-04.3 Rows.** See the counts below. Row set **a** holds the rows that cite a listed text; row set **b** holds the rows that belong here only under the broad reading. The sets a and b are not separate questions: your P-04.2 answer on reach decides whether set b is in.
- **P-04.4 Repair direction.** HELP_HUMAN has proposed that the deliverable text and the App DIRECTIVE/CONTRACT text change, and the code stands. That proposal is HELP_HUMAN's design, not your words (RUN_BASIS Addendum 11). You may change it.

## What we found
- The listed clauses are unamended at the frozen basis:
  - DIRECTIVE §2.8 (`docs/DIRECTIVE.md:115`): Chirality owns permission semantics; Claude is the key-aware default;
  - §2.10 (:144): provider-neutral core;
  - §4.1 (:227) and §4.2 (:250): Anthropic API-key access; no ambient settings and no shipped bypass mode;
  - CONTRACT K-PERM-1 (`docs/CONTRACT.md:90`) and K-PERM-6 (:95): no bypass mode shipped to ordinary users. [GOVERNING]
- D-GOV-43 item 3 runs Codex against the user's shared configuration, skills, MCP definitions and sessions, with "no effective-configuration veto". Item 4 makes approval and sandbox policy the user's choice, and says "Full access is available by explicit user choice". Neither item names the App clauses above (`docs/governance_harness/_PROPOSALS/D-GOV-43_…/D-GOV-43.proposed.md:172-195`, adopted by `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md`). [GOVERNING]
- The CONTRACT preamble (`docs/CONTRACT.md:15-17`) already calls the Claude/Anthropic default-provider rules "compatibility history". It does not amend K-PERM-1/6 or the DIRECTIVE. [GOVERNING]
- The live code follows D-GOV-43: the composer offers Full access (the danger-full-access sandbox; `frontend/src/components/shell/chat-panel.tsx:133`; spot-check items S2-013 and S2-043 in `R3/R3_SPOT_CHECK.md`). The Anthropic API-key settings component is still mounted (`frontend/src/components/shell/shell-frame.tsx:302`; non-hosted branch of `settings-view.tsx:35`); whether the hosted App reaches it was not established. [code]
- Because D-GOV-43 sits outside the DIRECTIVE §0 authority order, R2 and R3 marked these rows "Governing texts disagree" and did not choose between the sources (`R3/RUNWIDE_CALLS.md` call d). [run finding]
- Addendum 9 limits the answer to authority and sequence. Three live-path findings stay in their own packets: event redaction (P-12), protected paths (P-13) and the human gate (P-14). [run finding]

## Affected rows
<!-- COUNTS -->
**86 rows are decided in this packet** (PRIMARY); 0 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-04`.

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|---:|
| EXT |  |  |  | 8 | 8 |
| PKG-01 | 1 |  | 1 | 28 | 30 |
| PKG-02 | 2 | 1 |  | 10 | 13 |
| PKG-03 |  |  |  | 6 | 6 |
| PKG-04 |  |  | 1 | 2 | 3 |
| PKG-06 |  |  | 1 | 18 | 19 |
| PKG-09 | 1 |  | 1 | 4 | 6 |
| PKG-10 |  |  |  | 1 | 1 |
| **Total** | **4** | **1** | **4** | **77** | **86** |

By sub-question (`R4/PACKET_SUBQUESTIONS.csv`):

- P-04.a: 78 rows — Governing texts disagree 71, Partly built 3, Text out of date 3, Built differently 1
- P-04.b: 8 rows — Governing texts disagree 6, Text out of date 1, Partly built 1

<!-- /COUNTS -->
In every row, the deliverable text restates a pre-Codex permission, provider or settings clause, and the live Codex path does what D-GOV-43 says instead. Split, by script (`R4/_work/D2_scripts/d2_q6_pop.py`; `R4/_work/SUBQ/P-04_subq.csv`):

- **a, 78 rows:** the row's source or notes name a listed clause, Full access or the API key, directly or through a cross-referenced row.
- **b, 8 rows:** the row reaches D-GOV-43 only through other clauses. These are `DEL-04-05#CLM-009.10` (K-NET-1), `DEL-06-06#STATE-1`, `DEL-09-03#CLM-011`, `DEL-10-01#REM-1` (§8 daemon), `SOW:SOW-045.2`, `SOW:SOW-075.2` (the `~/.codex` memory link), and `DOC:RELIANCE#3.8` and `#4.8` (settings).

| Reading | Rows |
|---|---:|
| Narrow: sub-question a, plus the 4 rows the spot check found without R4-Q6 (3 Full access, 1 DIRECTIVE §2.8), now in P-09 (`DEL-04-05#CLM-024`, `DEL-07-01#CLM-011.4`, `#CLM-011.6`, `DEL-06-05#CLM-024`) | 82 |
| Broad: all 86, plus those 4, plus the other 56 "adjacent" rows in `RUNWIDE_CALLS.md` (d). The 59 adjacent rows outside this packet are 56 PRIMARY in P-09 and 3 in P-20; 3 of the 59 are Full-access rows. They are mostly K-ROOT/K-PATH, K-PERM-3/4/5 and K-BASH-1 rows in PKG-06/07 | 146 |

The R3 summary's rough estimate for the broad reading is superseded by the scripted split above. A further 23 "text out of date" rows repeat the same "Claude/Anthropic is the default" statement (R3 left open whether these are a conflict or just out-of-date text; 18 are in P-20 and 5 in P-09). They stay outside both counts.

## Options
**A. Confirm the answer, narrow reach; the text follows the code.** *R5 would:* rewrite the 82 rows' deliverable text to D-GOV-43 terms, package by package. Separately, one governed amendment tranche would amend DIRECTIVE §2.8, §2.10, §4.1, §4.2 and K-PERM-1/6 through the established corpus-bump procedure (D-APP-38, as used under D-APP-56). Sub-question-b rows would go to P-11 as unframed questions.
**B. Confirm, broad reach.** Same as A for 146 rows. The amendment also covers K-PERM-3/4/5, K-NET-1, K-SDK-1 and §8, and P-09 rows gain R4-Q6 alongside R4-Q1.
**C. Confirm, but the code changes (for example, withdraw Full access).** A separate implementation brief. The 82 or 146 rows wait on it. This goes against your recorded purpose.
**D. Defer.** The rows stay "governing texts disagree" and are held. Reopened by a later ruling.

## HELP_HUMAN recommendation (draft)
Option A. Your recorded words already give the authority and the sequence, and the live code follows D-GOV-43 items 3 and 4. The narrow reach keeps this ruling to the clauses you were actually asked about. The broader K-ROOT/K-PATH and K-PERM-3/4/5 rows then stay with R4-Q1 (P-09), where the legacy-harness question decides them anyway. **Left open:** sub-question b, and the 23 ED rows (P-20).

## Who decides
You decide P-04.1–P-04.4. Amending the App DIRECTIVE and CONTRACT is your App authority, through their own governed amendment tranche. Root `docs/DIRECTIVE.md` and D-GOV-43 itself are outside your App authority in this run. Any Root-side wording routes to Root / HELPS_HUMANS.

## On ruling
- **Where recorded.** HELP_HUMAN commits one consolidated R4 ruling record, with the next free register ID (D-APP-130 at the time of writing) and its register row, before any repair. Its R4-Q6 clause transcribes your answer, the reach and the key sets (from `PACKET_INDEX.csv` P-04, `P-04_subq.csv`, and the added P-09/P-20 keys).
- **R5.** One tranche manager per package edits ScopeOfWork, `_STATUS`, `_REFERENCES` and register text for the listed rows only. Under Option A, rows that turn only on the DIRECTIVE clause are recorded as "difference already permitted", citing the ruling. R6 backchecks every listed row.
- **Governance amendment.** A separate tranche amends the App DIRECTIVE and CONTRACT, with independent review, a validator run and a corpus version bump.
- **Held rows and lifecycle.** Rows that also name D-APP-116..119 stay held. No lifecycle transition follows.

## Risks, contested rows and dependencies
- `DEL-10-01#REM-1` (spot-check item S3-002): plain R4 under the narrow reading, R4-Q6 under the broad one.
- The 4 spot-check rows (3 Full access, 1 DIRECTIVE §2.8) sit in P-09, so P-09's ruling must carry the R4-Q6 token for them.
- 52 of the 86 rows also cite R4-Q1 (P-09), and 12 also cite R4-Q5 (P-05). A confirmed answer here does not settle those halves.
- Dependencies: P-05 (the event rows that cite §2.10), P-09 (R4-Q1) and P-11 (b rows under Option A).
