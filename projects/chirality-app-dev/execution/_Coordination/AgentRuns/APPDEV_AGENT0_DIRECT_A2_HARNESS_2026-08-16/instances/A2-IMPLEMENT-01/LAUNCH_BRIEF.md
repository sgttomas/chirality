# Launch Brief — A2-IMPLEMENT-01

- Parent: `WI-PKG08-DEL0804`
- Agent form: bounded Agent 2 generalist using `software-bounded-implementation`
- Objective: minimally repair the App harness delegation type rules so Agent 0 may dispatch an allowlisted `TASK` Agent 2 and an ephemeral generalist Agent 2 only when `allow_generalist_agent2: true`; preserve Agent 0 to named Agent 1, Agent 1 to approved Agent 2, and fail-closed rejection of all unsupported role/type routes.
- Accepted basis: HEAD `44903bc69cf56d4ca794fe9629f26793a82bf1b3`; root `AGENTS.md`; `agents/AGENT_HELP_HUMAN.md`; TM-APP-044; DEL-08-04 live contract; APP-HOLD reliance `ALLOW`.
- Declared context: the two source files, directly focused tests, agent-instruction parsing helpers, root delegation doctrine, and DEL-08-04 read-only contract surfaces.
- Allowed writes (exact):
  - `projects/chirality-app-dev/frontend/src/lib/harness/managed-delegation.ts`
  - `projects/chirality-app-dev/frontend/src/lib/harness/subagent-governance.ts`
  - directly focused test files under `projects/chirality-app-dev/frontend/src/__tests__/lib/` or `projects/chirality-app-dev/frontend/src/__tests__/api/`
- Exclusions: all manifests/lockfiles; all deliverable and coordination records; all other product source; Git mutations; network/provider/release work.
- Required behavior:
  1. Agent 0 to allowlisted `TASK` Agent 2 succeeds through both governance evaluation and managed launch.
  2. Agent 0 to ephemeral generalist succeeds only when the Agent 0 instruction frontmatter explicitly sets `allow_generalist_agent2: true`.
  3. Agent 0 to named Agent 1 remains supported.
  4. Agent 1 behavior remains supported.
  5. Agent 2 delegation and unapproved/unallowlisted/dedicated or mismatched role/type routes remain fail-closed.
- Verification: focused Vitest for changed tests if dependencies are available; otherwise report the exact rerun. Run `git diff --check` and report exact changed paths.
- Return markers: `IMPLEMENTATION`, `FILES`, `CHECKS`, `SCOPE`, `RESIDUALS`.
- No delegation. Do not commit, push, or open a PR.
