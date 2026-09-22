<!-- PACKET
id: P-18
cluster: CL-18
title: Fix stale reference hashes, registers and metadata
question: Does the owner authorize R5 to repair the 513 register, reference-hash and metadata rows, including a D-APP-38 corpus version bump, and does the rule 2b reading behind 9 tie-break moves stand?
recommended: A — authorize the hygiene class, bump corpus
depends_on: none
decision_type: owner
tier: GOVERNING
-->
# P-18 — Fix stale reference hashes, registers and metadata

Cluster CL-18 · no named question · draft by TASK D4 for HELP_HUMAN review; not a ruling.

**Question.** These rows are records that say something no longer true about the documents themselves: a reference hash marked as matching, a dependency marked satisfied, a deleted file cited, a `TBD` left behind. Does the owner authorize R5 to bring them to the frozen-basis state, including the authority-corpus version bump that the D-APP-38 reference model requires? This packet also asks the owner to confirm or reverse one R3 reading (below).

## What we found
- D-APP-38 (Option D) sets the model. Authority-doc edits are allowed, but each one "triggers a corpus version bump", and deliverables are then re-reconciled to the new version. The tool and store are `execution/_Reconciliation/References/`. [GOVERNING]
- The corpus is at `current_version: v23` (`AUTHORITY_CORPUS.json`), last written by `23b3879b3` (2026-09-12, the D-GOV-43 tranche). Later commits `9eaddb596`, `95b342519` and `7f1e9f387` edited App PRD, SPEC and CONTRACT with no bump. [code]
- R2's recompute: 156 of 162 recorded `_REFERENCES.md` hashes for CONTRACT, SPEC and PRD fail to reproduce at the frozen basis, and the recorded values equal corpus v23 (XPF-029). The App scanner looks only for the literal `HASH_MISMATCH` and never recomputes, so the drift went unflagged. [run finding]
- Carriers still cite deleted documents: the four-document kit (deleted `8cb9cdaf0`) and `agents/AGENT_SOFTWARE_DECOMP.md` (deleted `d1166698d`) (XPF-034). [run finding]
- Register status fields lag the work in every package: dependency rows still `TBD`, or `SATISFIED` on code that is now legacy-only (XPF-035). [run finding]
- SoW frontmatter pins four different commits of the v3.2 decomposition, a known basis defect (XPF-030; RUN_BASIS §5). [run finding]
- All 513 PRIMARY rows need no owner decision. About 416 of them cite a hash recompute or REF-006 MATCH. [run finding]

## Affected rows
<!-- COUNTS -->
**513 rows are decided in this packet** (PRIMARY); 29 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-18`.

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | Old assessment overtaken (`STALE_ASSESSMENT`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Total |
|---|---:|---:|---:|---:|---:|---:|
| EXT |  | 1 | 2 |  | 4 | 7 |
| PKG-00 |  | 6 | 8 |  | 1 | 15 |
| PKG-01 |  | 4 | 38 | 2 | 5 | 49 |
| PKG-02 |  |  | 37 |  | 8 | 45 |
| PKG-03 | 2 |  | 30 |  | 4 | 36 |
| PKG-04 |  |  | 36 |  | 5 | 41 |
| PKG-05 |  |  | 34 |  | 6 | 40 |
| PKG-06 |  |  | 65 |  | 6 | 71 |
| PKG-07 |  | 2 | 61 |  | 4 | 67 |
| PKG-08 |  | 1 | 29 |  | 8 | 38 |
| PKG-09 |  | 1 | 57 |  | 14 | 72 |
| PKG-10 |  |  | 30 |  | 2 | 32 |
| **Total** | **2** | **15** | **427** | **2** | **67** | **513** |

ALSO/CONTEXT members by Disposition: Unknown 16, Text out of date 12, Partly built 1.

<!-- /COUNTS -->
Every package is affected. The rows are REGISTER rows plus the SoW, `_STATUS` and `_CONTEXT` sentences that restate them as current. The 15 "partly built" and 2 "written, not built" rows are self-checking requirements (for example "recheck on drift") whose trigger has fired. They are repaired by the same bump and re-pin, not by code.

## Options
**A. Authorize the hygiene class, with a D-APP-38 corpus bump.** *R5 would:*
1. Run the D-APP-38 tool once to mint the next corpus version from the frozen-basis authority docs.
2. Re-pin each listed `_REFERENCES.md` to it.
3. Replace stale MATCH, SATISFIED and "current" assertions, citations of deleted files, and lagging `TBD` and status fields, one package at a time.

The frontmatter pins are corrected to one stated basis, or are marked historical where a ruling preserves them.

**B. Authorize text edits, but no corpus bump.** R5 marks each hash row as drifted, for example "does not reproduce at v23; re-reconcile pending", instead of re-pinning. The drift stays visible, but the D-APP-38 model's own remedy is not applied.

**C. Defer.** The records stay false until a separate reference refresh.

## HELP_HUMAN recommendation (draft)
Option A. The D-APP-38 ruling already says what an authority-doc edit requires, so the bump carries out an existing ruling; it is not a new decision. Two points stay open:
- **Order.** If P-06 (or another packet) amends App SPEC, TYPES or PRD, that amendment makes the corpus bump again. So R5 should bump once, after the R4 governance amendments land, to avoid two re-pins.
- **Scanner.** Whether the scanner should recompute hashes is a separate engineering brief, and it is not proposed here.

**Rule 2b reading (confirm or reverse).** R3 read tie-break rule 2b so that a `TBD` placeholder or lagging count in a register, which says nothing false about the product, counts as "to-do list out of step", not "text out of date". Nine rows moved on that reading:
- here: DEL-05-03#REGISTER-3, DEL-06-03#REGISTER-2, DEL-09-02#REGISTER-3 and DEL-09-06#REGISTER-2;
- in P-19: four rows;
- in P-17: one row.

HELP_HUMAN recommends keeping the reading. The repair (edit the register text) is the same either way, so reversing it changes only the labels.

## Who decides
The owner. Nothing here is outside the owner's App authority. A scanner change, if ever wanted, would be engineering, through its own brief.

## On ruling
1. The consolidated R4 ruling record (the next free D-APP ID, with its register row, committed by HELP_HUMAN) carries a P-18 clause. It covers the hygiene class, the D-APP-38 corpus bump (one bump, after any R4 governance amendment) and the rule 2b reading.
2. A single R5 step runs the corpus tool: the new snapshot, and a status re-run that shows no drift.
3. Then R5 tranche managers per package edit the `PACKET_INDEX.csv` P-18 PRIMARY rows, merged with the P-17 edits of the same package.
4. Checks: the tool is idempotent (a second `apply` is a no-op), the ledger validator runs, R6 backchecks every listed row with `HASH-RECOMPUTE`, and `git diff --check` is clean.
5. No lifecycle transition; no D-APP-116..119 rows.

## Risks, contested rows and dependencies
- `DEL-02-02#REGISTER-6` (spot check S1-031, undecided between "to-do list out of step" and "text out of date"): it is the same `TBD`-placeholder pattern as the rule 2b rows, and the repair is the same under either label.
- `DEL-04-01#CLM-004.2`: the R3 tie-break was left undecided and both readings stand. The repair is the same.
- `DEL-05-04#CLM-027` (S1-076, "text out of date" or "nothing to check"): the conflict table says "None" while a SPEC-versus-K-EVENT-4 conflict exists. R5 should list the conflict, not delete the table.
- The 29 ALSO rows are decided elsewhere, mostly in P-02 (16). The 16 "unknown" rows among them wait on the owner-check outcome.
- This packet interacts with P-06 and any other governance amendment: see the order point above.
