# D-APP-130 Ruling: RUN_D128 R4 gate (decision book accepted as the R5 basis; packet rulings are R5's first task)

**Status:** RULED
**Date:** 2026-09-22
**Decision ID:** D-APP-130
**RuledBy:** Ryan Tufts (owner), in-session direction to the HELP_HUMAN (Agent 0) session on 2026-09-22
**Run:** `execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/`, activated by D-APP-128, with R2 scale-out under D-APP-129
**Decision basis:** the R4 decision book and packets as merged to main by PR #841 (`1b63e075c`):
- `…/R4/R4_DECISION_BOOK.md` (SHA-256 `3daab45ceac4571054cbaca5f5c0cbf550a906edb80ac561175ef6e7d090537a`);
- `…/R4/PACKETS/` (25 packets, P-01..P-24 and P-EX), indexed by `…/R4/PACKET_INDEX.csv` (SHA-256 `b17789eb6c6775a36c4ad986e0d423eff4b6218a6e1deea00cd8e696cd399457`);
- the synthesized concordance `…/R3/CLAIM_CONCORDANCE.csv` (SHA-256 `a6f6cdda685173cac3aa8ab75d8dd823143feadbde2c44a755571337936dd852`), with `R3/` and `R4/` QA and review records.

## Ruling basis

The owner's words, verbatim, as recorded with SHA-256 in
`execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/OWNER_DIRECTION.md`
(`r4_gate_acceptance`):

> I accept this as the basis for R5 once rulings are made, but I want that to be the starting task in R5.  So I want to consider that R4 is complete with my acceptance of this decision book, and to merge via PR what you've done.

The SHA-256 of this text is `e53bd5b32d3d02817ff3096e446bb058900478b7382338692c4c542af635fe25`.

This record transcribes that direction and does not broaden it (K-AUTH-1; D-GOV-04).

## Recorded outcome

1. **R4 is complete.** The owner accepts the decision book and its 25 packets, at the revision
   above, as the basis for R5.
2. **Packet rulings are the first task of R5.** No packet is ruled by this record. The owner rules
   the packets (the decision book §4 ruling form) as R5's opening step. Those rulings are
   transcribed verbatim into their own ruling record, the next free D-APP ID. That record is
   merged to main before any repair is dispatched.
3. **No repair is authorized yet.**
   - No deliverable text, `## Remaining`, lifecycle state, governing document, code, hold or
     release claim changes under this record.
   - The packets' recommendations remain HELP_HUMAN drafts until ruled.
   - The owner's recorded R4-Q6 answer (RUN_BASIS Addendum 9) remains CONTEXT until the packet
     ruling transcribes it.
4. **Merge.** The owner directs that the work done so far be merged by PR, under the standing Git
   authorization of 2026-09-12. PR #840 (R2) and PR #841 (R3 and R4) are already merged. This
   record, its register row and the run-state updates follow by their own PR.
5. **Unchanged:**
   - rows tied to D-APP-116..119 stay held until those decisions are ruled (packet P-10);
   - the two owner-deferred DEL-06-02 keys remain for the owner (packet P-01);
   - all 54 lifecycle states are unchanged.

## Consequences

- The D-APP-128 register visibility cell reads R4 COMPLETE, with R5 opening on packet rulings.
- The run's R5 plan is:
  - (a) owner packet rulings, recorded and merged;
  - (b) a repair manifest derived from the ruled options and PACKET_INDEX;
  - (c) repair tranches partitioned by owning deliverable, text only; code options become separate
    `software-bounded-implementation` briefs (Runtime code routes to the Runtime loop, and Root or
    D-GOV items route to Root or HELPS_HUMANS);
  - (d) R6 backcheck.
