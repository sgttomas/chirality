# Launch brief — K1_IMPLEMENTER

This file is the sealed, normalized form of the HELP_HUMAN dispatch received on
2026-09-03. The conversational dispatch remains the source for its full wording.

- **Requested by:** HELP_HUMAN (Agent 0), working directly with owner Ryan Tufts.
- **Agent:** bounded ephemeral Agent 2, TASK + `software-bounded-implementation`;
  no delegation.
- **Provider / engine / model:** OpenAI / Codex / GPT-5 family (exact model
  identifier not exposed to the agent runtime).
- **PackageID:** PKG-09.
- **DeliverableIDs:** DEL-09-06; item DEL-09-06-V3-06 only.
- **AcceptedBasis:** `fe0ce926d4475fa41cb91933ad1218b95083889b`
  (`origin/main`, PR #690 merge).
- **PROFILE_PATH:** `projects/chirality-app-dev/software-workflow.json`.
- **ApplyEdits:** true.

## Objective

Add exactly two negative cases to
`frontend/src/__tests__/scripts/run-packaged-security-proof.test.ts`:

1. a log with no `[egress-layer-probe]` line yields
   `egressProbePayloadCount: 0`, `egressProbeObserved: false`, and `pass: false`;
2. a malformed `[egress-layer-probe] not-json` line yields
   `egressProbeUnexpectedDestinations: [null]` and `pass: false`.

The summarizer product bytes must remain unchanged. This is a tests-only tranche.

## Allowed write targets before review

- `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-security-proof.test.ts`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_K_2026-09-03/**`
- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_run_records/TASK_RUN_2026-09-03_NODE_K.md`

No `_STATUS.md`, `MEMORY.md`, final `HANDOFF_STATE.md`, final manifest, or
`LOOP_RECEIPTS.md` update is authorized before `REVIEW_PASS`.

## Exclusions

- No product source or summarizer byte.
- No package configuration, plans, register, decision, Root, authority-corpus,
  or other deliverable write.
- No signing, notarization, publication, distribution, release, release-readiness,
  certification, or professional claim.
- No push, PR, merge, or scratch-worktree removal before HELP_HUMAN directs it.

## Acceptance criteria

- Both requested cases pass in the focused and full Vitest runs.
- Typecheck and all selected registered/governance checks pass.
- `git diff --check` and exact change-scope validation pass.
- APP-HOLD-1 remains ALLOW/PASS; authority corpus remains v20 with no drift;
  receipts ledger remains valid.
- No product byte changes and every changed path is in the sealed write scope.
- A fresh reviewer can inspect 100% of `basis..freeze`; implementation stops at
  `REVIEW_READY`.

## Expected return

`REVIEW_READY`, basis, branch, freeze HEAD, diff stat and changed paths,
pass/fail/skipped check results, model attribution, findings, and decisions.
