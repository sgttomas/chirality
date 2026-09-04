# Launch Brief — Node L implementer

- **Requested by:** HELP_HUMAN (Agent 0), following Ryan Tufts's two-wave slate-3 selection on 2026-09-03.
- **Role:** bounded ephemeral Agent 2, `TASK + software-bounded-implementation`; no delegation.
- **Basis:** `fe0ce926d4475fa41cb91933ad1218b95083889b`.
- **Branch/worktree:** `codex/app-v3-nodeL-consent-fake-guards-2026-09-03` at `/private/tmp/chirality-app-v3-slate3-20260903/nodeL`.
- **PackageID / DeliverableIDs:** `PKG-02` / `DEL-02-05` (`DEL-02-05-V3-04`).
- **Profile:** `software-workflow.json` under the root software-workflow contract.
- **ApplyEdits:** true, only within the write locus in `ORCHESTRATION_PLAN.md`.

## Objective

Implement the live V3-04 fake-only follow-on: (F2) require granted consent to resolve a network prompt and decide/document fake staleness posture; (F3) make a fresh post-revocation grant set the new generation's private home to `present`; (F4) accept test-control network prompts only under `askPerDestination`; add one focused test per fix.

## Acceptance criteria

- Minimal, coherent change within the exact fake/fixture/test fence.
- F2 decision rationale and materially important rejected alternative recorded.
- Focused and full Vitest, typecheck, APP-HOLD integrity, harness self-check and pytest, whitespace, exact change-scope, corpus, and receipt validation pass or any failure is reported exactly.
- Fixtures remain secret-free and use reserved `.test` hosts; no panel or vocabulary byte changes.
- A1 re-stage declaration precedes product mutation; F-APP-2 remains intact.
- Commit and return `REVIEW_READY`; do not close out, push, merge, or remove the scratch worktree.
