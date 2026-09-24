# Return A2 — PEC basis impact inventory (TASK, general-purpose/opus, high effort requested)

Outputs in `SCA-005_PREP_2026-09-23/`: `IMPACT_INVENTORY_PEC_BASIS.csv` (201 rows) SHA-256 `f0bba13aa7fbce3b618e4132a91a634e16d4558ba521393380e2f5894130e3bc`; `IMPACT_INVENTORY_PEC_BASIS.md` SHA-256 `b0ff83591dfbd9eddea50b8f9632e32f16f242d7aac484408f2d49eb56bd0484`. All 32 SOWs covered: 23 with touching claims, 9 with none (DEL-01-04, 03-02, 03-03, 03-06, 04-02, 08-02, 10-02, 10-03, 10-11). Excerpts verified against live text.

Counts by action: MODIFY 129, NOTE-ONLY 60, RECLASSIFY 9, ADD 3, REMOVE 0. By drift dimension (multi-tag): D1 38, D2 57, D3 16, D4 41, D5 84, D6 10, D7 12, D8 18, D9 23, none 6 (TM-PEC-023 carry-ins).

D-PEC-79 v2.3 postimage differs from live PRD in six places (+16 lines): header, status note, provenance note, §16/§16.3; hashes verified; still unapplied.

Candidate new scope (CANDIDATE only): C-1..C-4 WORK_GRAPH.md parser, WorkGraphs discovery, per-undertaking RECEIPT.md parser, MEMORY `## Runs` parser; C-5 reclassify Workplan/Step/Gate entity and DEL-02-06; C-6 PEC-owned Runtime client instance replacing shared-runtime seam and daemon SSE bridge; C-7 presence-tier rethink; C-8 reclassify OI-002/OI-006/OI-008; C-9 per-loop optional Remaining; C-10 2026-09-23 trials as fixtures; C-11 loop-set wording; C-12 event-contract home; C-13 Git/PR completion join; C-14 TM-register feed.

Decisions raised for the manager (HELP_HUMAN steer recorded in B1 addendum 2): TM-PEC-023 rows 1/4/7 ordering after daemon/shared-runtime disposition; D-PEC-79 apply-then-amend vs successor candidate; fixture eligibility (1 of 3 trials has RECEIPT.md); keep vs rename DEL-02-03/04/06 and DEL-07-02; add new feed items vs extend; DEL-01-06 fixes representation; route non-PEC-writable files (`pec.yaml`, sister `adapter.yaml`, PEC AGENTS.md Shared Runtime Boundary) via notices/TM; two SOW housekeeping fixes (16 SOWs pin unresolvable `@3623b958b`; 13 SOWs claim `_REFERENCES.md` names revision 1.1 while all 64 name 1.4).

Corrections after cross-reading A1: Piping `## Remaining` count 0/106; PEC ledger carries `receipt-contract-v2` so the PRD "pec is prose-structured" claim is stale; DEL-02-04 "no STATUS.json in PEC tree" stale (13 exist), moved to MODIFY.
