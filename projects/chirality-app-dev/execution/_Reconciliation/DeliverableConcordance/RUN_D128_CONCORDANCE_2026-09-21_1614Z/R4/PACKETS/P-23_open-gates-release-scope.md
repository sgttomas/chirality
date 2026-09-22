<!-- PACKET
id: P-23
cluster: CL-23
title: Open human gates and v3 release-scope wording
question: For rows describing open gates or v3 scope limits, which should R5 restate, leave open, or route elsewhere?
recommended: a fix text; b none; c keep open; d after Q-11
depends_on: P-03, P-24, P-10
decision_type: owner; WORKING_ITEMS (scope-change, for P-23.d if retired)
tier: mixed
-->
# P-23 — Open human gates and v3 release-scope wording

Cluster CL-23 · no named question · draft by TASK D1 for HELP_HUMAN review; not a ruling.

**Question.** These rows describe work that normally waits for a human gate, or state what v3 did and did not include. None of them needs a new ruling on authority. Which should R5 restate, which stay open, and which wait on another answer? Nothing here, and nothing in R5, moves any deliverable's lifecycle state.

- **P-23.a** — the text is out of date about v3 scope (8 rows).
- **P-23.b** — the difference is already permitted by a ruling (4 rows).
- **P-23.c** — the gate is open and the work is not done (14 rows).
- **P-23.d** — the gate is open for managed or descendant delegation work, which done-declaration Q-11 bears on (12 rows).

## What we found
- Every row's recorded owner-decision field is "no", and every row's cause is either "normal open human gate" or "explicitly in or out of v3 scope" (fact sheet P-23). [run finding]
- **(a)** The release documents still frame signing, notarization and publication as future choices. v3.0.0 was published as the latest stable release on 2026-09-13, and `desktop:dist` signs when an identity is supplied (`DOC:BUILDREL#1`, `#14`, `DOC:VALSTRAT#4.14`; `frontend/scripts/pack-electron.mjs:86-95`). [code]
- **(a)** Four DEL-08-02 rows still describe unknown persona labels passing through, the "PIPELINE" route and `REF-006 MATCH` as current. `DEL-02-01#REM-1` says the favicon is satisfied, but the App ships none. [run finding]
- **(b)** D-APP-50 excludes the domain `operation_applier.apply` step "outright", pending its own packet. The three DEL-10-01 human-approval rows are therefore already permitted: no apply path exists (`DEL-10-01#CLM-004.5`). `DEL-10-02#CLM-010.12` rests on D-APP-37's amendment gate. [GOVERNING]
- **(c)** Open items include:
  - in-panel PDF: `inlinePdfPreview: false` at `frontend/electron/preload.ts:77`, where D-APP-121's effect is held;
  - S-8 sign-in and sign-out evidence after the consolidated signed build (`DEL-02-05#REM-1`, D-APP-127);
  - the DEL-06-03 propose tool (D-APP-108);
  - the domain-boundary wording checks (DEL-10-04, DEL-10-05);
  - the behaviour-group coverage table (DEL-09-03);
  - three decision rows that are themselves open: `DEC:D-APP-101`, `DEC:D-APP-121` and `DEC:D-APP-125.1`. [code]
- **(c)** `DEC:D-APP-101`'s remaining work names an owner ruling on D-APP-118. D-APP-128 §5.5.4 holds rows touching D-APP-116..119 from R5 until those are ruled. [GOVERNING]
- **(d)** The rows cover the per-chat delegation policy (DEL-03-02, DEL-08-04), reconstructible records for managed and native descendants (DEL-08-05), and the Section 9 IDs for descendant classes (`DEL-09-02#REM-1`). The live Runtime states "native descent does not assign a role", and no per-descendant record carries the role-policy evidence (`chirality-runtime/packages/core/src/delegated-runtime.ts:321`; `DEL-08-05#CLM-018.3`). [code]
- Done-declaration Q-11 asks whether managed multi-child delegation is still part of v3, or was retired with the daemon path. The `DEL-09-02#REM-1` notes say Q-11 may make the managed-descendant part moot (P-24). [CONTEXT]

## Affected rows
<!-- COUNTS -->
**38 rows are decided in this packet** (PRIMARY); 72 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-23`.

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | Difference already permitted (`ACCEPTED_DIVERGENCE`) | Unknown (`UNKNOWN`) | Total |
|---|---:|---:|---:|---:|---:|---:|
| EXT | 2 | 1 | 3 |  |  | 6 |
| PKG-02 |  | 2 | 1 |  | 1 | 4 |
| PKG-03 | 1 | 2 |  |  |  | 3 |
| PKG-06 | 1 |  |  |  |  | 1 |
| PKG-08 | 3 | 6 | 4 |  |  | 13 |
| PKG-09 | 1 | 1 |  |  |  | 2 |
| PKG-10 | 1 | 4 |  | 4 |  | 9 |
| **Total** | **9** | **16** | **8** | **4** | **1** | **38** |

By sub-question (`R4/PACKET_SUBQUESTIONS.csv`):

- P-23.a: 8 rows — Text out of date 8
- P-23.b: 4 rows — Difference already permitted 4
- P-23.c: 14 rows — Partly built 9, Written, not built 4, Unknown 1
- P-23.d: 12 rows — Partly built 7, Written, not built 5

ALSO/CONTEXT members by Disposition: Partly built 33, Built differently 20, Difference already permitted 10, Written, not built 5, Unknown 2, Governing texts disagree 1, Text out of date 1.

<!-- /COUNTS -->
38 rows across 7 package groups. Sub-question split by script, `R4/_work/SUBQ/P-23_subq.csv`, rule stated in `R4/_work/D1_scripts/d1_subq_p23.py`: (a) text out of date; (b) difference already permitted; (d) other rows in DEL-03-02, DEL-08-04, DEL-08-05 and DEL-09-02; (c) everything else.

## Options
**For P-23.a:**
- **A1. Change the deliverable text.** *R5 would:* restate the release documents for the signed and published v3.0.0, following P-03, and rewrite the DEL-08-02 examples and the `DEL-02-01` favicon note.
- **A2. Defer.** The rows stay held.

**For P-23.b:**
- **B1. Confirm.** *R5 would:* change nothing. The rows are already "difference already permitted".

**For P-23.c:**
- **C1. Keep the gates open.** *R5 would:* change only wording that is wrong inside the gate text, such as "daemon" becoming the App-owned Runtime service, or a retired Root dependency. The work itself becomes separate implementation briefs when you choose to start it.
- **C2. Close or retire chosen gates** by naming them in the ruling. This is structural, so it goes as a scope-change handoff to WORKING_ITEMS.

**For P-23.d:**
- **D1. Wait on your answer to Q-11 (P-24).** If managed multi-child delegation stays in v3, handle these as C1. If it is retired, they go as a scope-change handoff to retire or rewrite the managed-descendant scope.
- **D2. Treat as C1 now,** keeping the managed-descendant wording until Q-11 is addressed.

## HELP_HUMAN recommendation (draft)
- **a: A1.** The facts are recorded, and the three release-document rows take P-03's answer.
- **b: B1.**
- **c: C1.** Hold `DEC:D-APP-101` from R5 until D-APP-118 is ruled.
- **d: D1.** Rewriting delegation text before you say whether managed delegation survives would likely mean writing it twice.
- Left open: when, if ever, each open gate is taken up. That is ordinary scheduling, not an R4 matter.

## Who decides
- **Owner:** which gates are closed or retired, and the answer to Q-11.
- **WORKING_ITEMS:** executes any retirement through the scope-change workflow.
- **Engineering:** opening work on an open item takes its own bounded implementation brief.
- **Outside your App authority:** D-APP-125 items 1, 4 and 5 may be finalized through Runtime or Root instruments (`DEC:D-APP-125.1`).

## On ruling
- **Ruling record.** The consolidated R4 ruling record (the next free D-APP ID, committed by HELP_HUMAN before any repair) carries a P-23 clause per sub-question. It lists the rows by `PACKET_INDEX.csv` P-23 and `R4/PACKET_SUBQUESTIONS.csv`.
- **R5.** Package tranche managers (PKG-02, 03, 06, 08, 09, 10 and EXT) edit ScopeOfWork, `_STATUS` Remaining and document text for (a) and (c). For (d), R5 edits only after Q-11 is answered; a retirement goes to WORKING_ITEMS.
- **Held.** `DEC:D-APP-101` is held while D-APP-118 is unruled.
- **Checks.** R6 backchecks every listed row. No lifecycle transition and no code change.

## Risks, contested rows and dependencies
- No contested or spot-check-refuted rows.
- Depends on:
  - P-03, for `DOC:BUILDREL#1` and `DOC:VALSTRAT#4.14`;
  - P-24, for Q-11 (d) and Q-04 (the S-8 part of `DEL-02-05#REM-1`);
  - P-10, for the decision-held rows D-APP-121 and D-APP-125.
- 72 further rows are ALSO members here. They are decided in their own packets: P-06 (26), P-09 (18), P-11 (12), P-13 (9), P-02 (4), P-10 (2) and P-03 (1).
