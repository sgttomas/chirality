# MEMORY - DEL-07-04

## Runs

- 2026-09-27 — `APP-REMOVE-LEGACY-FORMS-2026-09-27` (SCA-APP-011 code change; checkpoint-group-3 candidate, lands with the SCA-APP-011 scope text after group-3 acceptance): removes the status and transition routes, the client fetch functions and the Workbench and Pipeline forms and their gate inputs (work-graph FU3 withdrawn, its D-APP-36 item moot). The library `deliverable-contracts.ts`, `lib/lifecycle` and the MCP tools stay. The route test's status and transition cases, including the `CHECKING` reversal and `ISSUED` reopening blocks, move to `frontend/src/__tests__/lib/deliverable-contracts.test.ts`; two request-body parsing rows (`INVALID_REQUEST`) retire with the routes. No lifecycle change. Evidence: [receipt](../../../_Coordination/AgentRuns/APP-REMOVE-LEGACY-FORMS-2026-09-27/RECEIPT.md); amendment `execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/`.
- 2026-09-27 — SCA-APP-011 checkpoint group 3 accepted (`execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-3_2026-09-27/`); landed in PR #995 (`78e74f590`). Run receipts: `execution/_Coordination/AgentRuns/APP-REMOVE-LEGACY-FORMS-2026-09-27/RECEIPT.md` (the change) and `execution/_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/RECEIPT.md` (this post-acceptance follow-up).
- 2026-09-26 — `APP-TRANSITION-FORMS-2026-09-26` (work-graph FU3, FU4):
  the Workbench and Pipeline transition forms offer the `CHECKING -> IN_PROGRESS`
  reversal (required `ruling`) and the `ISSUED -> IN_PROGRESS` reopening
  (required `amendment`), take an optional ruling on the forward gates, and show
  refusals with the amendment checker's code. Their help text says the actor is
  caller-asserted and `write_status.sh` is the anchored check. D-APP-36 component
  render tests and a static browser layout check are recorded. The forms are not
  mounted in the live App, so the D-APP-36 item stays open for the App loop.
  From the 3a review, a transition is now refused (`INVALID_STATUS_FORMAT`)
  unless the written file reads as the target state, the transition date and one
  more history entry. This catches a header with a lone CR, U+2028 or U+2029 that
  made the writer edit a different line than the parser reads. CLM-003 and
  CLM-008 now describe the implemented App SPEC §4.3 gates (FU4). No lifecycle
  change. Evidence:
  [receipt](../../../_Coordination/AgentRuns/APP-TRANSITION-FORMS-2026-09-26/RECEIPT.md).
- 2026-09-26 — `APP-AMENDMENT-REOPEN-2026-09-26` (work-graph FU1; owner D2):
  the validator, API, MCP tool and client admit `ISSUED -> IN_PROGRESS` only for
  a HUMAN actor with a valid approval SHA and an `amendment` that passes
  `amendment-reopen.ts`, a port of the working-tree mode of Root
  `check_amendment_reopen.py` (at `5038f2554`) with a parity test against it. Without an amendment the move stays `BACKWARD_TRANSITION`.
  History records the amendment, register row and SHAs. `Authorization Basis`,
  `Accepted Basis SHA` and `Accepted ScopeOfWork SHA-256` metadata now need a
  HUMAN actor. Known limit: no git, so the Root-only at-commit checks
  (`APPROVAL_SHA_UNREACHABLE`, `APPROVAL_SHA_NOT_ANCESTOR`, records read at the
  approval commit) are not made and uncommitted record edits are not detected;
  `write_status.sh` is the anchored check. Fixed here: a pre-existing defect
  where every transition rebuilt `_STATUS.md` and dropped trailing sections and
  unread history lines (including `write_status.sh` reopening lines). The
  writer now edits in place, and a transition that would drop a reopening
  marker is refused (`HISTORY_NOT_PRESERVED`). A lock-free check-to-write race
  remains a known limit. No lifecycle change. Evidence:
  [receipt](../../../_Coordination/AgentRuns/APP-AMENDMENT-REOPEN-2026-09-26/RECEIPT.md).
- 2026-09-26 — `APP-LIFECYCLE-DEPS-2026-09-26`: the transition validator, API
  and MCP tool now admit the human-ruled `CHECKING -> IN_PROGRESS` reversal for
  a HUMAN/USER/OPERATOR actor with an approval SHA and a `ruling` naming a
  non-empty file inside the project root other than the deliverable's own
  `_STATUS.md`; the reversal removes the `**Checking Approval SHA:**` field. The
  forward gates into `CHECKING` and `ISSUED` accept an optional ruling under the
  same checks. Status-field writes reject reserved labels and multi-line or
  control-character keys and values. `ISSUED -> IN_PROGRESS` and every other
  backward move stay rejected. REQ-004's open question, which record authorizes
  the scope-change route for `ISSUED -> IN_PROGRESS`, is answered by the owner's
  2026-09-26 decision (E, recorded in the receipt): an ACCEPTED amendment
  (checkpoint group 3 accepted) whose accepted action register names the
  deliverable with action `MODIFY`, or `RECLASSIFY` where the reclassification
  changes the deliverable's scope (D-GOV-50); App SPEC §4.3 states it. Tool
  enforcement is pending: the tools keep refusing the move until an
  amendment-record check is implemented (App follow-up). This addresses the
  CHECKING part of CLM-011.4 and the
  `NOTICE_2026-09-26_REVIEW_SPEC34_REVERSAL.md` lag. Known limit: the actor is
  caller-asserted and the App layer does not verify that the ruling is committed
  or the SHA is a real commit, so any caller able to write files in the project
  can satisfy the checks with HUMAN, a well-formed SHA and a non-empty ruling
  file, as for the CHECKING/ISSUED gates; the REQ-005 human-identity limit
  remains. The other App follow-ups (Runtime descriptor `ruling`, UI reversal
  input, SOW verification sentences) are in the work graph. No lifecycle change.
  Evidence:
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
