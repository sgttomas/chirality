# Routed Change Notice — Root Agent 0 direct Agent 2 dispatch alignment

Routed by: Root loop, 2026-08-16, owner-directed bounded tranche
`ROOT-AGENT0-DIRECT-A2-ALIGN-20260816`, under the `AGENTS.md` agent-index
change-notice rule (one `agents/` file changed).

This notice is coordination, never authority. The App loop adopts,
acknowledges, amends, declines, or defers any local response through its own
instruments and cadence.

## What changed

`agents/AGENT_HELP_HUMAN.md` prose was aligned with root `AGENTS.md`
(2026-08-02 doctrine: Agent 0 role-table row and "Delegation and Entry
Rules"), which already permits Agent 0 to directly dispatch bounded Agent 2
instances. Blob `503f70dbc00127d844e3a0327ed47655a9142278` →
`f3901408e7d5f040cb1d52e6033152ccb2bf3ade`.

- Invariant "Managers own management": "Delegate only to named Agent 1
  roles. Never bypass Agent 1 to dispatch Agent 2." → "Delegate to named
  Agent 1 roles; you may also directly dispatch bounded Agent 2 instances
  (ephemeral generalists or TASK) under the same sealed-brief,
  declared-scope, and durable-evidence requirements as Agent 1 dispatch
  (root `AGENTS.md`, Delegation and Entry Rules). Never use direct Agent 2
  dispatch to bypass a manager's validation of work that manager owns, and
  never let a child's capability become your own." plus a factual sentence
  stating that the `subagents:` allowlist, the agent-instruction validator,
  and the App harness type rule still enforce Agent-1-only children pending
  their own alignment tranches.
- Invariant "Hierarchy-mediated coordination": "relay only to its direct
  Agent 1 children" → "relay only to its direct children".
- SPEC item 3: "Only Agent 1 roles are direct children." → "Direct children
  are named Agent 1 roles or bounded Agent 2 instances (ephemeral
  generalists or TASK) under sealed briefs."

## What did not change

The frontmatter `subagents:` allowlist, WRITE_SCOPE, and the "No
project-content writes" invariant are untouched. No validator, harness,
skill, tool, or K-* invariant changed. Owner ruled Option 1 (prose alignment
only) after the dispatched agent reported that adding `TASK` to the
allowlist makes `tools/validation/validate_agent_instructions.py` exit 1
(`AGENT0_CHILD_TYPE`) and that the App harness type rule would still block
Agent 0 → Agent 2 at runtime.

## Parked follow-ons (stated, not routed as work)

1. ROOT — `tools/validation/validate_agent_instructions.py` L270-280 and
   `tools/validation/test_validate_agent_instructions.py` L167-183, with the
   `subagents: … TASK` frontmatter alignment, in a later root tranche.
2. APP — `frontend/src/lib/harness/managed-delegation.ts` L274, L289-290 and
   `frontend/src/lib/harness/subagent-governance.ts` L160-168 plus tests: an
   App product-code tranche under App's own review posture. Until then the
   App harness rejects Agent 0 → TASK/generalist delegation by type rule.

## Follow-on for this loop

None required by this notice. App HELP_HUMAN sessions read the live file;
App decides under its own instruments whether and when to schedule the App
harness follow-on above.

Evidence: `docs/governance_harness/tranche_manifests/ROOT-AGENT0-DIRECT-A2-ALIGN-20260816.yaml`;
`execution/_Coordination/AgentRuns/ROOT_AGENT0_DIRECT_A2_ALIGN_2026-08-16/`.
