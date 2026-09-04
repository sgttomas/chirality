# Orchestration Plan — APPDEV_V3_NODE_O_2026-09-04

- **RunID:** `APPDEV_V3_NODE_O_2026-09-04`
- **Plan version:** 1, frozen before evidence execution.
- **Selection authority:** `HUMAN` — the owner authorized the established post-CSP preservation sequence; PR #695 merged the Node N product change at `e2f8317dadb8ac95b7aff5ac5637d967fb7e6d40`, satisfying the live `DEL-09-01-V3-01` revision trigger.
- **Execution class:** `delegated-harness-native`. HELP_HUMAN directly dispatched one descendant instructed to operate as a bounded ephemeral Agent-2 implementer. Agent-2 role is `role not mechanically enforced`; governed-workflow role evidence is `instruction-asserted`; K-SUBAGENT/non-delegation is instruction+config asserted, not mechanism-proven. The implementer is instructed not to delegate and has observed no descendant.
- **Implementer:** O1_IMPLEMENTER, OpenAI Codex, GPT-5 family (exact model identifier is not exposed to the implementer runtime).
- **Independent reviewer:** a future fresh read-only descendant will review 100% of the frozen basis-to-head diff. No verdict exists before that dispatch.
- **Posture:** sequential implementer → independent reviewer → remediation loop if needed → narrative-only closeout after supervisor `REVIEW_PASS`.
- **Basis/branch:** `e2f8317dadb8ac95b7aff5ac5637d967fb7e6d40`; `codex/app-v3-nodeO-section8-rev3-2026-09-04`.
- **Parent receipt:** Receipt 224. No Node O receipt is appended before post-review closeout.
- **Selected item:** `DEL-09-01-V3-01`, revision 3 only; the item remains open until G5 fan-in.

## Objective

Run the existing hardened bounded method `Evidence/Node_H_Section8_Preservation_2026-09-03/rerun-section8-local.sh` unchanged against the clean post-PR-#695 `main` basis. Retain durable, non-secret revision-3 bytes proving the Section 8 behavior projection remains equal to accepted revision 2. Record exact application, runner, evaluator, environment, command, result, cleanup, and manifest identities. PR #696 is included in the basis but is plan-only and did not trigger this revision.

## Write ownership before review

- DEL-09-01 `Evidence/Node_H_Section8_Preservation_2026-09-03/**`, limited to revision-3 additions and append-only narrative updates required to index them.
- DEL-09-01 `_run_records/TASK_RUN_2026-09-04_NODE_O.md`.
- This AgentRuns directory.
- Ignored/generated paths written by the accepted proof under `frontend/**`; no tracked frontend/product/test/CSS byte may change.
- Explicitly withheld until `REVIEW_PASS`: DEL-09-01 `_STATUS.md`, `MEMORY.md`, final handoff/manifest closeout, and `loop/LOOP_RECEIPTS.md`.

Prohibited: changes to the hardened runner, evaluator/product/test/runtime/workflow bytes, other deliverable state, plans, decisions/registers, decomposition/SCOPE_CHANGE, Root, Task Management, host capability/identity state, G5/G6a, versioning, signing, notarization, publication, distribution, or release-readiness claims.

## Fan-in gates

The freeze requires the real daemon-bound lifecycle and release-quality evidence, revision-2-to-revision-3 comparator, source/evaluator identities, manifest and cleanup proof, registered repo checks, exact scope, sanitation/fence scans, and a clean committed worktree. Publication requires a fresh independent review PASS with zero BLOCKER and zero MAJOR findings, later narrative-only closeout, CI, and owner merge.

## A1 consequence

Although no tracked `frontend/` byte is authorized to change, proof execution writes ignored/generated paths under `frontend/`. Under A1, historical staged R20 remains historical and this execution does not create a future proof-reliance claim without a newly staged procedure revision and fresh owner-executed proof.
