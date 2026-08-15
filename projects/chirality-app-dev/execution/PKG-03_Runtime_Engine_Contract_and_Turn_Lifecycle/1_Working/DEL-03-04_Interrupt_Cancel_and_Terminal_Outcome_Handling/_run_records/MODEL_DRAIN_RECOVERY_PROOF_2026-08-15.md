# Model-drain recovery proof — 2026-08-15

- Run: `APPDEV_MODEL_DRAIN_RECOVERY_2026-08-15`
- Basis: `910c02129811a005da9b180c31e3c18dd365df6f`; APP-HOLD-1 dispatch preflight `ALLOW`.
- Product output: `frontend/src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts` now proves one accepted turn held during public model activation is interrupted by daemon stop, survives fresh-service daemon restart, and replays exactly one durable terminal event.
- Focused Vitest: PASS (`1` passed, `2` skipped).
- Full frontend Vitest with worktree-correct runtime aliases: PASS (`143` files passed, `1` skipped; `1116` tests passed, `4` skipped).
- Typecheck: PASS with temporary worktree path overlay; the first registered attempt exposed a stale external dependency symlink, not a product defect. The overlay and dependency symlink were removed.
- Registered always checks: PASS (`app-hold-integrity`, `harness-self-check`).
- Practitioner-harness pytest: PASS (`349` passed).
- Build: not selected by `software-workflow.json` for the test-only changed path.
- Review: fresh read-only `software-code-review` PASS; no actionable findings.
- Scope: PASS; Root `runtime/**` remained read-only. No provider, network, release, domain, decision, receipt, PKG-09, or lifecycle-state write occurred.
- Residual: deterministic fake engine/oMLX control proves graceful daemon recovery, not ungraceful process kill or live-provider behavior.
