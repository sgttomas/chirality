# R4 decision book — RUN_D128 deliverable concordance

**Read this first.** It is the owner's decision gate for the RUN_D128 concordance (activated by
D-APP-128). Everything below was prepared by agents: packets propose, and **you rule**. Each
recommendation is a HELP_HUMAN draft, labelled as such. Nothing is repaired, and no lifecycle
changes, until your rulings are recorded.

## 1. Overview

**What the run did.** Agents compared every live App deliverable (54 deliverables, 11 packages)
with the code as it stood at the frozen commit `00115c719` (App 3.0.1), with the governing
documents and with the recorded v3 direction. They also audited five other surfaces: the ruled
D-APP-86..127 decisions, the release and validation docs, the decomposition scope ledger, the
packaged `AGENTS.md`, and the harness developer docs. Every one of the 1,746 deliverable units and
221 extension units has a verdict. Each package was checked by an independent verifier, and then
by a run-wide spot check (315 confirmed, 12 refuted, 11 undecided out of 338 items).

**Census (3,568 verdict rows, after your owner-check answers).**

| Verdict | Rows |
|---|---:|
| Matches, or nothing to check | 1,275 |
| Text out of date (deliverable text says something now false) | 1,089 |
| Partly built, built differently, or written but not built | 762 |
| Governing texts disagree (needs a ruling) | 169 |
| To-do list or register out of step | 116 |
| Already retired or permitted by a ruling | 87 |
| Unknown (22 off-code events nobody can confirm; 1 visual-evidence row) | 23 |
| Other (old verification or assessment, lifecycle, agent-instruction matter, undocumented) | 47 |

967 rows name a decision they wait on. Most of them wait on one of six framed questions, R4-Q1 to
R4-Q6.

**Your owner-check answers are applied.** Your answers (OC-01..OC-20) are testimony about events,
not rulings, and they are now in the concordance. Two rows moved: the arm64 and minimum-OS
inspections happened, but nothing records their results, so both rows are now "partly built".
The other 61 rows gained a note recording your testimony, and 5 statements that an event "did not happen" were corrected to "no record". The 22 rows you could not answer stay Unknown, with your belief
noted. The detail is in `R3/OWNER_CHECK_APPLIED.md` and packet P-02.

**What is being asked.** 25 packets: one per cause cluster, plus an exceptions list. About a third
of them turn on a real governance question. The rest ask you to authorize a class of text repairs
that follow from decisions you have already made, mainly D-GOV-43 (the Codex-hosted App) and its
App application D-APP-127.

**Terms used throughout.**
- *Legacy harness*: the old in-process Claude SDK / Pi engine code that is still in the repository
  but that the shipped App no longer runs.
- *Live Codex path*: the code the shipped App actually runs.
- *R5*: the repair stage that follows your ruling. It edits deliverable text only. Code changes
  always go through a separate, bounded implementation brief.
- *Codes in packets*: clause IDs such as K-PERM-6 (CONTRACT) and §2.8 (DIRECTIVE) are sections of the App governing documents. D-APP-nn and D-GOV-nn are App and Root decisions. R4-Q1..Q6 are the six framed questions. XPF-nnn is an R3 cross-package finding, and S1-/S2-/S3-nnn is a spot-check item. Rules marked MR-n or "rule 2b" are run rules from `CONVENTIONS.md`, and each packet explains the one it uses.
- *PRIMARY rows*: the rows a packet decides. A row can touch several packets, but it is decided in
  exactly one.

**Worth knowing before you read.**
- Several code options change **Runtime** code (`projects/chirality-runtime`). This App run cannot
  edit Runtime code, so those implementation briefs go to the Runtime project loop (P-08, P-12,
  P-13, P-15, P-16 and P-20).
- R4-Q6 reach (P-04) matters: 82 rows are in scope under the narrow reading and 146 under the
  broad one.
- R3 counted 428 rows with both live and legacy evidence. The final count is 410; P-09 holds 333
  of them.
- Amending Root documents, D-GOV rules, agent role files or workflows is outside your App
  authority in this run. Those items are routed to Root or HELPS_HUMANS.
- Your rulings go into one consolidated ruling record, the next free D-APP ID (currently D-APP-130).
  HELP_HUMAN commits it before any repair. Rows tied to D-APP-116..119 stay on hold until those are
  ruled.
