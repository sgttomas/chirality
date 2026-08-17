# Return — A2-IMPLEMENT-01

IMPLEMENTATION: Agent 0 may launch allowlisted canonical `TASK` Agent 2 children and explicitly opted-in ephemeral generalists. Named Agent 1, existing Agent 1 behavior, allowlist enforcement, and all unsupported routes remain fail-closed.

FILES:

- `frontend/src/lib/harness/managed-delegation.ts`
- `frontend/src/lib/harness/subagent-governance.ts`
- `frontend/src/__tests__/lib/managed-delegation.test.ts`
- `frontend/src/__tests__/lib/harness-subagent-governance.test.ts`

CHECKS: focused Vitest passed 2 files / 29 tests; `git diff --check` passed.

SCOPE: exactly the four declared files; no manifest, lockfile, deliverable, coordination, agent-instruction, or Git mutation.

RESIDUALS: root-side `HELP_HUMAN` metadata/validator alignment remains an integrated dependency; no broad frontend gates claimed.
