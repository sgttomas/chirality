# MEMORY - DEL-07-04

## Runs

- 2026-09-26 — `APP-LIFECYCLE-DEPS-2026-09-26`: the transition validator, API and
  MCP tool now admit the human-ruled `CHECKING -> IN_PROGRESS` reversal for a
  HUMAN/USER/OPERATOR actor with an approval SHA and a `ruling` file inside the
  project root. `ISSUED -> IN_PROGRESS` and every other backward move stay
  rejected. REQ-004's open question, which record authorizes the scope-change
  route for `ISSUED -> IN_PROGRESS`, is answered by the owner's 2026-09-26
  decision (E, recorded in the receipt): an ACCEPTED amendment (checkpoint group
  3 accepted) whose accepted action register names the deliverable with action
  `MODIFY`; App SPEC §4.3 states it. Tool enforcement is pending: the tools keep
  refusing the move until an amendment-record check is implemented (App
  follow-up). This addresses the CHECKING part of CLM-011.4 and the
  `NOTICE_2026-09-26_REVIEW_SPEC34_REVERSAL.md` lag. Known limit: the App layer
  cannot verify that the ruling is committed or the SHA is a real commit, so
  HUMAN plus a well-formed SHA plus a real ruling path suffices, as for the
  CHECKING/ISSUED gates; the REQ-005 human-identity limit remains. The other App
  follow-ups (Runtime descriptor `ruling`, UI reversal input, SOW verification
  sentences) are in the work graph. No lifecycle change. Evidence:
  [receipt](../../../_Coordination/AgentRuns/APP-LIFECYCLE-DEPS-2026-09-26/RECEIPT.md),
  [work graph](../../../_Coordination/WorkGraphs/app-lifecycle-deps-2026-09-26/WORK_GRAPH.md),
  branch `wave3-app-lifecycle-deps`.

## Decisions And Evidence

- 2026-07-12 - D-APP-56 R4-P19 implemented exact HUMAN/USER/OPERATOR aliases; HUMAN-prefixed inventions fail with UNAUTHORIZED_ACTOR and approval-SHA evidence remains required. No lifecycle transition occurred.

- 2026-06-16 - Human project authority advanced this deliverable lifecycle from SEMANTIC_READY to IN_PROGRESS because active code implementation is underway. This does not imply CHECKING, ISSUED, release readiness, dependency satisfaction, professional approval, certification, sealing, authentication, or code-compliance acceptance.
- 2026-07-12 - D-APP-56 R5 P40 executed UPD-074, UPD-077: REF-006 current-state kit/register wording now agrees with D-APP-38 MATCH; dated source-warning and assessment history is preserved. No lifecycle transition.

- 2026-07-12 - D-APP-56 R5 P45 executed UPD-132: current kit/register metadata now reflects live ruled state; dated history and genuine TBD/gates remain preserved. No lifecycle transition occurred.
- 2026-07-12 - D-APP-56 consolidated decision-application tranche recorded the applicable ruled ownership, mapping, gate-reaffirmation, or dated-deferral result for DEL-07-04; proposal-only source rows were not treated as human rulings, no unruled work was executed, and no lifecycle transition occurred.

- 2026-09-22 — D-APP-131: bounded R5 repair and R6 backcheck recorded in `execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/R6_2026-09-22/`. Current work is only in `_STATUS.md ## Remaining`; prior evidence and lifecycle remain unchanged.

## Record closeout — 2026-09-22

D-APP-131/132 and D-GOV-43/D-APP-127 now govern the current ScopeOfWork and Remaining interpretation. Earlier SDK/daemon, four-file, matrix/default-role, source-MATCH and pre-release planning statements remain dated history. Current work, owning surface, checks and gates are in `_STATUS.md`; the W07_10_ROWS.csv derivative accounts for original residual keys. No lifecycle/approval-SHA refresh, product completion, new native result, or release is asserted.
