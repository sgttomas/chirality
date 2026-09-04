# Orchestration Plan — APPDEV_V3_NODE_L_2026-09-03

- **RunID:** `APPDEV_V3_NODE_L_2026-09-03`
- **Plan version:** 1 (frozen before any product write)
- **Selection authority:** `HUMAN` — Ryan Tufts selected the recommended two-wave slate in the HELP_HUMAN session on 2026-09-03: nodes K and L concurrently, then node J after both land. This is execution direction, not a new ruling.
- **Supervisor:** HELP_HUMAN (Agent 0).
- **Executor:** `L1_IMPLEMENTER`, bounded ephemeral Agent 2 using `software-bounded-implementation`; provider `OpenAI`, engine `Codex`, model `GPT-5 family (exact model identifier not exposed to the agent runtime)`; no delegation.
- **Independent reviewer:** a fresh read-only Agent 2 over 100% of the frozen diff, dispatched by HELP_HUMAN after this implementation freezes.
- **Basis:** `fe0ce926d4475fa41cb91933ad1218b95083889b` (`origin/main`, PR #690 merge).
- **Branch:** `codex/app-v3-nodeL-consent-fake-guards-2026-09-03`.
- **Item:** `DEL-02-05-V3-04` (`SELECTABLE` on the basis).

## Work graph

1. `L1_IMPLEMENTER` makes the sealed F2/F3/F4 fake and test repairs, runs the named checks, commits, and freezes at `REVIEW_READY`.
2. A fresh read-only reviewer checks the entire basis-to-freeze diff.
3. Findings, if any, return through HELP_HUMAN for remediation and a fresh review. `REVIEW_PASS` is required before closeout.

## Sealed write locus

- `projects/chirality-app-dev/frontend/src/lib/consent/fake-hosted-engine-consent-port.ts`
- `projects/chirality-app-dev/frontend/src/lib/consent/consent-ux-fixtures.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/consent/**`
- `projects/chirality-app-dev/frontend/src/__tests__/components/account-consent-settings*.test.ts`
- `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/{Evidence/**,_run_records/**}` when required by the live item
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_L_2026-09-03/**`

No panel, vocabulary, Root, plan, register, decision-record, lifecycle, release, signing, notarization, publication, or host-state write is authorized. `_STATUS.md`, `MEMORY.md`, final handoff/manifests, and `LOOP_RECEIPTS.md` remain untouched until `REVIEW_PASS`.

## Decision latitude

For F2, reset command-network posture to `off` and clear pending/session destination state whenever granted consent turns stale. This is the smallest fail-closed fake invariant aligned with non-reuse of stale consent. Rejected: retaining the posture while merely guarding prompt resolution, because it preserves a misleading `on` or session-accepted snapshot under a consent that cannot be reused and would require a deliberate stale-plus-on fixture for future live-adapter comparison.

The fake continues to retain its account posture across revocation; a fresh grant recreates the private home for the new generation. This repairs fixture self-consistency without deciding the Root-owned question of whether a real invalidation logs out the account. Root-owned configuration-digest semantics are also untouched.
