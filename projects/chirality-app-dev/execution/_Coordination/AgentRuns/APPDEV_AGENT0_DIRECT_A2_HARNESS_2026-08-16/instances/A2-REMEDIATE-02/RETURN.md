# Return — A2-REMEDIATE-02

REMEDIATION: Agent 0 `TASK` launch now requires canonical name, Agent Type 2, and `AGENT_CLASS: TASK` through the shared `parseAgentClass()` parser. Missing and `PERSONA` class fixtures fail closed; canonical TASK succeeds.

FILES:

- `frontend/src/lib/harness/managed-delegation.ts`
- `frontend/src/__tests__/lib/managed-delegation.test.ts`

CHECKS: manager focused Vitest PASS, 2 files / 30 tests; candidate whitespace PASS; `git diff --check` PASS.

SCOPE: exact two-file remediation; no other source, manifest, lockfile, shared closeout, or Git mutation.

RESIDUALS: fresh full corrected-diff review required before fan-in.
