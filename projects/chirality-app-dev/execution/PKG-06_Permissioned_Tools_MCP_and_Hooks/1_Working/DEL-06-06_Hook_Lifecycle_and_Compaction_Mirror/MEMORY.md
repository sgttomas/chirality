# MEMORY - DEL-06-06

## Decisions And Evidence

- 2026-07-12 - D-APP-56 R4-P04 adopted `hook.progress`; mapper and JSONL replay tests preserve stdout, stderr, and output. No lifecycle transition occurred.

- 2026-06-21 - ADQ-11/D-APP-43 closed the PreCompact/Stop residual by accepting adapter message/status/result lifecycle mapping as the canonical implementation surface: `context.compaction.started`, `context.compacted`, `context.compaction.failed`, `turn.completed`, `turn.failed`, and D-APP-40 `turn.interrupted`. No synthetic SDK hook callback layer is required. Evidence: `../Evidence_ADQ-11_Permission_Tool_Residuals.md`. This does not imply CHECKING, ISSUED, release readiness, dependency satisfaction, professional approval, certification, sealing, authentication, or code-compliance acceptance.
- 2026-06-16 - Human project authority advanced this deliverable lifecycle from SEMANTIC_READY to IN_PROGRESS because active code implementation is underway. This does not imply CHECKING, ISSUED, release readiness, dependency satisfaction, professional approval, certification, sealing, authentication, or code-compliance acceptance.
- 2026-07-12 - D-APP-56 R5 P40 executed UPD-071, UPD-073: REF-006 current-state kit/register wording now agrees with D-APP-38 MATCH; dated source-warning and assessment history is preserved. No lifecycle transition.

- 2026-09-22 — D-APP-131: bounded R5 repair and R6 backcheck recorded in `execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/R6_2026-09-22/`. Current work is only in `_STATUS.md ## Remaining`; prior evidence and lifecycle remain unchanged.

## 2026-09-22 current record closeout

D-APP-131 lift (b), D-GOV-43/A2, D-APP-127 and applicable D-APP-132 dispositions applied to the current claim blocks. Earlier dated decisions, checks and lifecycle/approval evidence remain historical. Observe hook/compaction/terminal activity through the complete Runtime/Codex event stream and provide truthful App replay. Legacy SDK callback names do not prescribe native supplier hooks.

Current unfinished delivery: Deliver live named compaction/replay and terminal witnesses, identify which hook facts Codex actually emits, and close structural-redaction/artifact gaps with PKG-05. Record any absent native hook or enforcement subject without recreating retired SDK callbacks. See `_STATUS.md` Remaining and the W04_06 current row derivative; no new product test, native outcome, issuance or release is claimed.

2026-09-22 review repair: For each accepted turn, persist exactly one durable terminal outcome. Completion, Stop/finalization and interruption races must not append duplicate or contradictory terminal records. Verify a named completion-versus-Stop race fixture against the live Runtime event store, asserting exactly one terminal event and a truthful final result.
