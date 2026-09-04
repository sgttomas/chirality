# Sealed launch brief — J1_IMPLEMENTER

- **Requested by:** HELP_HUMAN (Agent 0), working directly with owner Ryan Tufts.
- **Execution form:** bounded ephemeral Agent 2 generalist after the recorded TASK preflight stop and Brief Amendment V2; no delegation.
- **Accepted basis:** `ede175910c67b384332324622b17695f69e6a715` (`origin/main`, PR #692 merge).
- **Branch/worktree:** `codex/app-v3-nodeJ-section8-revision2-2026-09-03` at `/private/tmp/chirality-app-v3-slate3-20260903/nodeJ`.

## Objective

1. Execute DEL-09-01-V3-02 by hardening the existing Section 8 local rerun method for recursive descendant termination, a port precondition before any build or daemon start, and anchored process matching or recorded-pid matching.
2. Execute DEL-09-01-V3-01 revision 2 with that hardened method against the accepted main basis, using one premerge-only run and durable recomputable evidence that covers PRs #687–#692.
3. Freeze all review-candidate bytes in one commit and return `REVIEW_READY`; do not close out before a fresh reviewer passes the complete diff.

## Authorized tracked writes before review

- the existing `Evidence/Node_H_Section8_Preservation_2026-09-03/rerun-section8-local.sh`
- one new revision-2 run folder under the same bundle
- the comparison/evidence surfaces required to add revision 2 and the bundle `MANIFEST.sha256`
- bounded DEL-09-01 `_run_records/**`
- `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_J_2026-09-03/**`

The method may mutate ignored/generated `frontend/` evidence paths while running. No tracked frontend/runtime product, test, fixture, evaluator, workflow, package, configuration, Root, plan, register, or decision-record byte may change. `_STATUS.md`, `MEMORY.md`, final handoff/check/manifest surfaces, and `loop/LOOP_RECEIPTS.md` are closeout-only after `REVIEW_PASS`.

## Required checks before freeze

- `bash -n` and `shellcheck -S warning` on the hardened script
- one daemon-bound premerge-only revision-2 run with a script-written verifying per-run manifest
- bundle manifest verification and behavior-projection comparison
- evaluator/product byte-identity proof
- applicable registered frontend gates, APP-HOLD integrity, corpus status, receipts validator, harness self-check, practitioner pytest, exact change-scope, strict JSON, `git diff --check`, and F-APP-2 grep
- honest skips; no required unavailable check is called a pass

## Return contract

Return basis, branch, freeze SHA, diff stat/path list, exact run identity, Section 8/premerge outcomes, manifest results, check table, A1/F-APP-2 posture, attribution (OpenAI / Codex / GPT-5 family; exact identifier unavailable), and findings. Do not push, close out, or remove the worktree.
