<!-- PACKET
id: P-17
cluster: CL-17
title: Carry D-APP-127 and D-GOV-43 into deliverable text
question: Does the owner authorize R5 to bring the carriers' ScopeOfWork, _CONTEXT, _REFERENCES, Dependencies and _STATUS text to the state D-APP-127 and D-GOV-43 already ruled, and route the one unseated SOW-079 row to scope-change?
recommended: A — authorize the text-repair class
depends_on: P-18
decision_type: owner; WORKING_ITEMS (scope-change) for P-17.b
tier: GOVERNING
-->
# P-17 — Carry D-APP-127 and D-GOV-43 into deliverable text

Cluster CL-17 · no named question · draft by TASK D4 for HELP_HUMAN review; not a ruling.

**Question.** The direction is already ruled. D-GOV-43 re-platformed the App on a Codex host with topology A2 (an App-owned Runtime service), and D-APP-127 applied that to the App. The ruling reached only the `_STATUS.md` files, so the rest of the deliverable text still describes the old design. Does the owner authorize R5 to repair that text to the ruled state?
- **P-17.a** (117 rows): repair the deliverable text to the ruled state.
- **P-17.b** (1 row, `SOW:SOW-079.1`): the SCA-APP-009 row SOW-079 (the live Codex version pin) is carried by no live deliverable. DEL-04-01, which the decomposition names, disclaims it. Which deliverable carries it?

## What we found
- The D-APP-127 ruling record lists "consequential applications": DEL-03-01 to 03-04, DEL-05-02 and DEL-02-05 "architecture-bound clauses revised", and DEL-09-04 to 09-06 revised. [GOVERNING]
- The R2 application map (`R2/_shared/EVIDENCE_PACK/D-APP-127_APPLICATION_MAP.csv`, 270 rows) found `_STATUS.md` revised in only the 11 named carriers. `ScopeOfWork.md`, `_CONTEXT.md` and `_REFERENCES.md` were revised in none of 54 deliverables, and `Dependencies.csv` in none of 52. [run finding]
- The code side of D-APP-127 landed: the App-owned service child (`frontend/electron/runtime-service-host.ts`), Codex-owned login (`chirality-runtime/packages/daemon/src/codex-login.ts`) and the retired hold rows. [code]
- Residue: the DEL-02-02 and DEL-08-02 `_STATUS.md` still gate on the retired D-APP-88 helper bundle. Their Checks lines still require the retired A1 re-stage declaration (`DEC:D-APP-127` row Notes). [run finding]
- Most rows are "text out of date" or "to-do list out of step". Every PRIMARY row needs no owner decision (the fact sheet shows 118 of 118 as `NO`). [run finding]
- Some rows point at later App rulings whose application stopped short in the same way: D-APP-109 (dependency edges), D-APP-111 (closure pointers) and D-APP-56. The same repair applies. [GOVERNING]
- `SOW:SOW-079.1`: the decomposition v3.2 §8 and §9 name DEL-04-01 for SOW-079. The DEL-04-01 `_STATUS.md` history for 2026-09-03 records "SCOPE_AMENDMENT_REQUIRED", and its ScopeOfWork does not cite SOW-079 (XPF-027). [run finding]

## Affected rows
<!-- COUNTS -->
**118 rows are decided in this packet** (PRIMARY); 43 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-17`.

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | Verification out of date (`STALE_VERIFICATION`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Total |
|---|---:|---:|---:|---:|---:|---:|
| EXT | 1 | 1 |  |  |  | 2 |
| PKG-00 |  |  | 10 |  |  | 10 |
| PKG-01 |  | 2 | 8 | 1 | 1 | 12 |
| PKG-02 |  |  | 25 |  | 3 | 28 |
| PKG-03 |  |  | 6 |  | 2 | 8 |
| PKG-04 |  |  | 8 |  | 1 | 9 |
| PKG-05 |  |  | 5 |  | 1 | 6 |
| PKG-06 |  |  | 1 |  |  | 1 |
| PKG-07 |  |  | 22 |  | 3 | 25 |
| PKG-08 |  |  | 9 |  | 1 | 10 |
| PKG-09 |  |  | 6 |  | 1 | 7 |
| **Total** | **1** | **3** | **100** | **1** | **13** | **118** |

By sub-question (`R4/PACKET_SUBQUESTIONS.csv`):

- P-17.a: 117 rows — Text out of date 100, To-do list out of step 13, Partly built 3, Verification out of date 1
- P-17.b: 1 rows — Written, not built 1

ALSO/CONTEXT members by Disposition: Text out of date 32, To-do list out of step 8, Partly built 3.

<!-- /COUNTS -->
The rows are spread across every package; PKG-02 and PKG-07 have the most. All of them state a pre-D-APP-127 fact as current: a daemon, LaunchAgent, per-root home, helper bundle, A1 gate, old closure pointer or old dependency status. P-17.b is the single SOW-079 row; P-17.a is every other row (`_work/SUBQ/P-17_subq.csv`).

## Options
**A. Authorize the text-repair class, and route SOW-079 to scope-change.** *R5 would:* in package tranches, rewrite each listed row's ScopeOfWork, `_CONTEXT`, `_REFERENCES`, Dependencies and `_STATUS` text to the ruled state. Each edit cites D-APP-127, D-GOV-43, D-APP-109 or D-APP-111 as the row records, and prior text stays as history where a ruling says to preserve it. For P-17.b, R5 does nothing: a scope-change handoff to WORKING_ITEMS decides whether DEL-04-01 is amended to carry SOW-079 or the row is re-seated.
**B. Authorize P-17.a only; defer P-17.b.** SOW-079 stays held until a separate scope-change is opened.
**C. Defer the whole class.** The rows stay held. This would leave carriers contradicting rulings that are already in force.

## HELP_HUMAN recommendation (draft)
Option A. It needs no new direction: the rulings exist, the code matches them, and only the text lags. SOW-079 is a structural gap (no deliverable owns the row), so it belongs with scope-change, not R5. The only open point is sequencing: the `_REFERENCES` hash edits in these rows use the same corpus bump as P-18, so R5 should run both repairs together, per package.

## Who decides
The owner authorizes the repair class. WORKING_ITEMS (scope-change workflow) decides P-17.b after the ruling. Nothing here is outside the owner's App authority.

## On ruling
1. The consolidated R4 ruling record (the next free D-APP ID, with its register row, committed by HELP_HUMAN) carries a P-17 clause. The clause authorizes the text-repair class for the P-17.a keys in `PACKET_INDEX.csv` and routes P-17.b.
2. One R5 tranche manager per package edits only the listed rows' ScopeOfWork, `_CONTEXT`, `_REFERENCES`, Dependencies and `_STATUS` text, merged with the P-18 edits of the same package.
3. Checks: the ledger validator on each tranche, an R6 backcheck of every listed row, and an independent review per tranche.
4. HELP_HUMAN issues a scope-change handoff for SOW-079 to WORKING_ITEMS.
5. No lifecycle transition. No rows here touch D-APP-116..119.

## Risks, contested rows and dependencies
- `DEL-06-06#STATE-2` (an ALSO member here; its PRIMARY row is in another packet): the tie-break is undecided, and both readings stand (R3_SUMMARY §8).
- `DEL-07-01#REGISTER-3` is one of the 9 moves resting on the rule 2b reading (see P-18). The repair is the same under either reading.
- The 43 ALSO rows are decided in their own packets, mostly P-03 (16) and P-09 (9), with the rest in P-02, P-06 and others. Where those packets change the code or hold the rows, R5 must not "repair" that text to the D-APP-127 state first.
- Depends on P-18 for the hash re-pin mechanism.
