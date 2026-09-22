<!-- PACKET
id: P-09
cluster: CL-09
title: Retained legacy harness: history, compatibility or obligation
question: For claims that only the retained legacy harness meets, are they history, a documented compatibility surface, or obligations the live Codex path must meet?
recommended: D — a: compatibility (B); b: re-express guarantees; c: per part
depends_on: P-04, P-13, P-14, P-10
decision_type: owner (incl. App governance amendment); WORKING_ITEMS (scope-change); engineering; external authority (Root K-DOMAIN-2)
tier: GOVERNING
-->
# P-09 — Retained legacy harness: history, compatibility or obligation

Cluster CL-09 · named question R4-Q1 · draft by TASK D3 for HELP_HUMAN review; not a ruling.

**Question.** The App still carries the legacy harness: the in-process Claude Agent SDK / Pi code under `frontend/src/lib/harness/**` and some Runtime contract modules, which the live Codex path does not reach. For claims that only this code meets, is it **history** (retire the claims), **compatibility** (keep the code, document it as a non-product compatibility surface), or **obligation** (the live Codex path must meet the claims)?

- **P-09.a** (161 rows): features and engine-specific mechanisms only the legacy harness provides. Examples: SDK options, message mapping, the Anthropic key and base URL, the tool catalog, the tool-result store.
- **P-09.b** (136 rows): safety and control guarantees only the legacy harness provides: hooks, path containment, instruction-root protection, symlink rejection, permission and bash policy, redaction, approval gates.
- **P-09.c** (333 rows), a method question: live code meets part of the claim and only legacy code meets the rest. Is the claim judged whole or part by part?

**How rows got here (the subject test).** A claim is judged on the live product path whenever it names the App, a user, a session or a turn, an outcome, or a guarantee. It is judged as a module contract only when it describes one code unit and nothing else. A row carries this question when the only non-test code meeting it is legacy code (CONVENTIONS §2.4 rules 1–3; Addenda 6 and 8).

## What we found
- The App PRD, CONTRACT and SPEC each open with the same Codex-only basis: Claude/Anthropic and Pi/oMLX descriptions "describe compatibility history" and do not require shipping those engines (`docs/SPEC.md:15`, `docs/CONTRACT.md:15`, `docs/PRD.md:15`). [GOVERNING]
- The engine-neutral guarantees are unamended. CONTRACT K-ROOT-2 (ordinary execution must not change the instruction root), K-HOOK-1 (hooks fail closed) and K-PATH-2 (writes stay inside the project root) name Chirality hooks as their enforcement (`docs/CONTRACT.md:52,99,100,173`). SPEC §15.2 still lists required hooks (`docs/SPEC.md:847-860`). [GOVERNING]
- D-GOV-43 item 4 leaves approval and sandbox policy to the user, "Full access" included (`docs/governance_harness/_PROPOSALS/D-GOV-43_2026-09-11_codex_host_replatform/D-GOV-43.proposed.md:187-195`, adopted as written by `_DECISIONS/D-GOV-43_codex_host_replatform.md`). It names none of the clauses above. [GOVERNING]
- The live Runtime starts Codex threads with no Chirality tool servers (the Codex adapter starts each turn with an empty tool list and has no MCP wiring: `projects/chirality-runtime/packages/core/src/delegated-engine-adapter.ts:231`). So the in-process hook and tool layer never runs on the live path. [code]
- By script (`R4/_work/D3_scripts/d3_p09.py`): 285 PRIMARY rows are met only by legacy code, 333 by live and legacy code together, and 12 cite the question directly with no legacy tag. 96 of the 285 are "Matches" at module level only. [run finding]
- **Count effect of P-09.c.** If claims are judged whole, 316 of the 333 mixed rows would need no owner decision. The other 17 still cite D-APP-73, D-APP-116..119 or a plain R4 question. Their Dispositions would not change. Run-wide, 410 rows carry both tags and cite this question. R3's "428" was counted at an earlier build. [run finding]
- **The two reach readings.** The evidence pack (`REACHABILITY.csv`) marks a module reachable when a live file imports it. R3 call (a) marks it reachable only when a symbol the claim relies on is actually used (`R3/RUNWIDE_CALLS.md` (a)). 21 PRIMARY rows cite this question only under the symbol reading, 14 of them "Matches" (`R4/_work/D3_scripts/d3_reach.py`). [run finding]

## Affected rows
<!-- COUNTS -->
**630 rows are decided in this packet** (PRIMARY); 97 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-09`.

| Package | Matches (`ALIGNED`) | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Verification out of date (`STALE_VERIFICATION`) | Difference already permitted (`ACCEPTED_DIVERGENCE`) | Lifecycle needs reassessing (`LIFECYCLE_REASSESSMENT_REQUIRED`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| EXT | 6 | 6 |  | 12 | 14 | 1 | 3 |  |  |  | 42 |
| PKG-01 | 2 | 4 | 11 | 7 | 7 |  |  |  |  | 1 | 32 |
| PKG-02 |  | 3 | 3 |  |  |  |  |  |  |  | 6 |
| PKG-03 | 2 |  | 1 | 4 | 2 |  |  |  |  | 1 | 10 |
| PKG-04 | 47 | 1 | 36 | 12 | 30 | 1 |  | 2 |  | 1 | 130 |
| PKG-05 | 1 | 12 | 13 | 3 | 25 | 15 |  |  |  |  | 69 |
| PKG-06 | 5 | 10 | 34 | 36 | 20 | 3 |  |  | 1 | 49 | 158 |
| PKG-07 | 2 | 6 | 33 | 1 | 4 |  |  |  | 1 | 6 | 53 |
| PKG-08 | 9 | 6 | 30 | 10 | 9 |  |  |  | 3 | 3 | 70 |
| PKG-09 | 2 |  | 5 | 7 |  |  |  |  |  | 1 | 15 |
| PKG-10 | 21 |  | 13 | 2 | 2 |  | 1 |  |  | 6 | 45 |
| **Total** | **97** | **48** | **179** | **94** | **113** | **20** | **4** | **2** | **5** | **68** | **630** |

By sub-question (`R4/PACKET_SUBQUESTIONS.csv`):

- P-09.a: 161 rows — Matches 64, Partly built 39, Text out of date 30, Verification out of date 9, Written, not built 8, Governing texts disagree 6, Built differently 3, To-do list out of step 1, Difference already permitted 1
- P-09.b: 136 rows — Partly built 44, Matches 32, Text out of date 21, Written, not built 14, Built differently 12, Governing texts disagree 8, Verification out of date 4, Difference already permitted 1
- P-09.c: 333 rows — Partly built 96, Built differently 79, Text out of date 62, Governing texts disagree 54, Written, not built 26, Verification out of date 7, To-do list out of step 4, Lifecycle needs reassessing 2, Difference already permitted 2, Matches 1

ALSO/CONTEXT members by Disposition: Governing texts disagree 51, Built differently 18, Partly built 14, Written, not built 7, Text out of date 5, Verification out of date 2.

<!-- /COUNTS -->
All rows cite R4-Q1. The sub-question split is by script (`R4/_work/SUBQ/P-09_subq.csv`, built by `d3_p09_subq.py`):
- **c**: evidence tagged both live and legacy.
- **b**: otherwise, the claim text or normative source matches a guarantee keyword list (hooks, containment, instruction root, permission, redaction, approval, gate, credential, bash, and K-PATH/K-ROOT/K-HOOK/K-PERM/K-DOMAIN-2).
- **a**: all remaining rows.

The keyword split is a triage. Rows will move between a and b on review.

## Options
**A. History.** Retire every claim met only by legacy code. *R5 would:* mark the text as history with the ruling cited. Deliverables that are wholly legacy go to a scope-change handoff. The code stays until a separate brief removes it.

**B. Compatibility.** Keep the legacy code as a documented surface that is not part of the product. *R5 would:* re-word each claim as "retained compatibility, not on the live Codex path". The live-path claims stay as written.

**C. Obligation.** The live Codex path must meet these claims. *R5 would:* hold the rows until a separate implementation brief is ruled for each guarantee. The text stands.

**D. Split by sub-question.** Give P-09.a B, and give P-09.b a governance amendment. For P-09.c, judge part by part, so each row's legacy part takes the a or b answer.

## HELP_HUMAN recommendation (draft)
Option D.
- **P-09.a, compatibility.** The corpus's own Codex-only basis already calls these descriptions compatibility history, so B only carries it into deliverable text.
- **P-09.b, re-express the guarantees; do not quietly retire them.** K-ROOT-2, K-HOOK-1, K-PATH-2 and SPEC §15.2 are engine-neutral and unamended. Treating them as history would drop controls no ruling dropped. The owner rules which guarantees the Codex sandbox now carries and which are retired. An App governance amendment re-expresses those clauses. Any guarantee kept but unmet goes to an implementation brief (see P-13).
- **P-09.c, part by part.** This keeps the information about which part is legacy-only, and matches how R3 and the spot check read most rows.
- **Reach.** Keep the symbol reading R3 applied.

Left open:
- Which PKG-04 deliverables (DEL-04-01..04-05 are mostly legacy) should be retired rather than kept as compatibility.
- The Full-access and DIRECTIVE §2.8 rows, which wait on P-04.

## Who decides
The owner decides a, b, c and the reach reading. The App governing texts change only through a governance amendment the owner rules. Retiring a deliverable goes to WORKING_ITEMS (scope-change). Any new code is an engineering matter. K-DOMAIN-2 specializes a Root framework clause, so re-expressing it is external authority (Root / HELPS_HUMANS).

## On ruling
1. HELP_HUMAN records the answers to P-09.a–c and the reach reading in the consolidated R4 ruling record: the next free D-APP ID in `_DECISIONS/_REGISTER.md`, with its register row.
2. R5 tranche managers, one per package, edit ScopeOfWork, `_STATUS` and `_REFERENCES` text for the P-09 PRIMARY key set in `PACKET_INDEX.csv`, by SubQ.
3. A separate App governance-amendment tranche handles SPEC §15.2 and CONTRACT K-ROOT-2, K-HOOK-1 and K-PATH-2 by the established corpus-bump procedure (D-APP-38 under D-APP-56).
4. Retirements go by scope-change handoff. Code changes go by implementation brief.
5. R6 backchecks every listed row.
6. The 9 rows also citing D-APP-116..119 stay held (e.g. `DEL-04-04#SEC-1`, `DEL-07-01#SEC-1`). There is no lifecycle transition.

## Risks, contested rows and dependencies
- Spot-check refutations, with sealed values kept:
  - `DEL-02-04#CLM-005.5` (S1-022, proposes "Partly built");
  - `DEL-06-04#CLM-027` (S1-112, proposes "Built differently").
- Undecided at R3:
  - `DEL-04-04#CLM-024` and `DEL-04-05#CLM-024`: R4-Q1;
  - `DEL-06-03#CLM-010.4`: subject test;
  - `DEL-06-06#STATE-2`: tie-break;
  - `DEL-05-03#CLM-010.14` (S1-070): "Built differently" or "Written, not built";
  - `DEL-10-02#CLM-024` (S2-059) and `DEL-10-04#CLM-016.1` (S2-047): AUTHORITY_CONFLICT or not.
- Four rows lack the R4-Q6 citation that the spot check proposes: `DEL-07-01#CLM-011.4`, `#CLM-011.6` and `DEL-06-05#CLM-024` (Full access), and `DEL-04-05#CLM-024` (DIRECTIVE §2.8). They depend on P-04.
- 5 P-09 rows carry the "Claude/Anthropic default" note, which is decided in P-04.
- Dependencies:
  - P-13 (protected paths and hooks) and P-14 (human gate) must agree with the P-09.b answer;
  - the rows citing D-APP-73 depend on P-10.
