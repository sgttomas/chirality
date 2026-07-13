# REVIEW-C2F Launch Brief — v1

Role: `REVIEW` (Agent 1, lifecycle-neutral exact-consumer calibration)

## Objective and accepted special mode

Perform the single REVIEW compatibility calibration explicitly selected by the
accepted Stage-2 plan. Prove that the newly activated REVIEW consumer invokes
or consumes valid `chirality-review-checklist/v1` output without re-extracting,
paraphrasing, renumbering, reordering, adding, or omitting candidate `AC-*`
criteria. This is deterministic compatibility evidence only, not a formal
five-gate review or lifecycle acceptance.

## One bounded target

- Deliverable: App pilot `DEL-07-01` only.
- Frozen candidate source: Git object
  `fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26:projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-01_Working_Root_Validation_and_Instruction_Root_Protection/ScopeOfWork.md`.
- Expected source SHA-256:
  `9b75621a465553baf47b08b665bbbee8dc39f3d60a1d64b6610b9949c9226744`.
- Authorized isolated-migration basis:
  `D-GOV-15@58aa81d62f4a32e3c2d687e4356a1e4be8141674`.
- Comparison evidence:
  `execution/_Coordination/AgentRuns/SOW-STAGE1-20260712/instances/HELPS-CHECKLIST/evidence/checklists/DEL-07-01.json`.
- Activated tool and consumer source:
  `tools/scope_of_work/derive_review_checklist.py` and
  `agents/AGENT_REVIEW.md` in the C2R candidate diff.

Materialize the immutable Git blob only inside the permitted review evidence
folder, run the registered deterministic tool twice in fresh output paths with
the exact migration authority, and compare byte identity, schema, source hash,
item count/order, qualified IDs, exact text, and verification linkage. Compare
the result to the accepted Stage-1 checklist and explain any permitted
metadata-only delta. Also inspect the activated REVIEW instructions to verify
they consume the tool artifact and do not retain an agentic SOW extraction
path. No child delegation.

## Writes

Only:

- `execution/_Evaluation/Reviews/SOW-STAGE2-EXEC-20260712-01-C2F-CALIBRATION/**`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/REVIEW-C2F/RETURN.md`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/REVIEW-C2F/STATUS.json`

Do not create deliverable-local `_REVIEW.md` or `Review_Findings.csv`; do not
touch `_STATUS.md`; do not update `_LATEST.md`; do not write the parent-owned
P2 snapshot. The accepted plan's lifecycle-neutral calibration narrows the
normal REVIEW protocol and preserves every content and lifecycle fence.

## Denied and return

No human findings, dispositions, formal review gates, checklist acceptance,
lifecycle recommendation or transition, source/candidate edits, Git state
changes, release, H1/H2 action, or legacy retirement. Return `PASS | PARTIAL |
BLOCKED | DECISION_REQUIRED` with exact hashes/counts, byte/order/text/linkage
verdicts, consumer-source verdict, blockers, rerun requirement, and next owner.
