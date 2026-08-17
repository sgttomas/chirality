# Launch Brief — A2-REMEDIATE-02

- Parent: `WI-PKG08-DEL0804`
- Agent form: bounded Agent 2 generalist using `software-bounded-implementation`
- Trigger: integrated fresh-review BLOCK finding 1.
- Objective: make Agent 0 to `TASK` managed launch fail closed unless the resolved canonical TASK instruction declares `AGENT_TYPE: 2` and `AGENT_CLASS: TASK`.
- Accepted basis: current PKG-08 four-file candidate; integrated finding that `managed-delegation.ts` checks only `agentName === 'TASK'` and Type 2 while the success fixture omits class metadata.
- Allowed writes (exact):
  - `projects/chirality-app-dev/frontend/src/lib/harness/managed-delegation.ts`
  - `projects/chirality-app-dev/frontend/src/__tests__/lib/managed-delegation.test.ts`
- Required behavior:
  1. Canonical `TASK` name + Type 2 + `AGENT_CLASS: TASK` succeeds for Agent 0 when allowlisted.
  2. Missing TASK class fails closed.
  3. Non-TASK class fails closed.
  4. Existing Agent 0 named Agent 1, Agent 1 child, generalist-opt-in, allowlist, dedicated-role, tool/scope, and Agent 2 non-delegation semantics remain unchanged.
- Use the existing agent-instruction class parser; do not invent parallel metadata parsing.
- Verification: focused managed-delegation and subagent-governance tests; candidate whitespace and `git diff --check` for edited paths.
- Exclusions: all other source/tests, manifests/lockfiles, deliverable/coordination records, shared closeout, Git mutations.
- Return markers: `REMEDIATION`, `FILES`, `CHECKS`, `SCOPE`, `RESIDUALS`.
- No delegation.
