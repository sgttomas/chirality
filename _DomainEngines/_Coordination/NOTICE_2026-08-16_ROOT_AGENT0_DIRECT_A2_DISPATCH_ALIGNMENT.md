# Tier-0 Coordination Notice — Root Agent 0 direct Agent 2 dispatch alignment

**Date:** 2026-08-16
**From:** Chirality Root / HELP_HUMAN (Agent 0, session minder)
**To:** Tier-0 / domain-engine loops (PEC has no notice inbox; prior root
notices to domain engines were placed here)
**Status:** coordination only; not authority

Root tranche `ROOT-AGENT0-DIRECT-A2-ALIGN-20260816` aligned the prose of
`agents/AGENT_HELP_HUMAN.md` with root `AGENTS.md` (2026-08-02 doctrine:
Agent 0 may directly dispatch bounded Agent 2 instances under the same
sealed-brief, declared-scope, and durable-evidence requirements as Agent 1
dispatch). Blob `503f70dbc00127d844e3a0327ed47655a9142278` →
`f3901408e7d5f040cb1d52e6033152ccb2bf3ade`. Changed clauses: the "Managers
own management" invariant ("Delegate only to named Agent 1 roles. Never
bypass Agent 1 to dispatch Agent 2." → permits direct bounded Agent 2
dispatch, forbids using it to bypass a manager's validation of owned work,
and states that the `subagents:` allowlist, the agent-instruction validator,
and the App harness type rule still enforce Agent-1-only children pending
their own tranches); "Hierarchy-mediated coordination" ("direct Agent 1
children" → "direct children"); SPEC 3 ("Only Agent 1 roles are direct
children." → named Agent 1 roles or bounded Agent 2 instances under sealed
briefs).

The frontmatter `subagents:` allowlist, WRITE_SCOPE, and "No project-content
writes" are unchanged (owner ruled Option 1, prose only, because the allowlist
change fails `tools/validation/validate_agent_instructions.py`
`AGENT0_CHILD_TYPE` and the App harness type rule still blocks at runtime).

Parked follow-ons, stated here for detection only: (i) ROOT —
`tools/validation/validate_agent_instructions.py` L270-280 and
`tools/validation/test_validate_agent_instructions.py` L167-183 with the
`subagents: … TASK` frontmatter alignment; (ii) APP —
`projects/chirality-app-dev/frontend/src/lib/harness/managed-delegation.ts`
L274, L289-290 and `subagent-governance.ts` L160-168 plus tests, an App
product-code tranche under App's review posture.

No Tier-0 decision, contract identity, profile, consumer pin, or domain-engine
scope is changed. PEC and other domain-engine loops adopt, acknowledge, amend,
decline, or defer any local follow-on through their own instruments and
cadence; no action is required by this notice.

Evidence: `docs/governance_harness/tranche_manifests/ROOT-AGENT0-DIRECT-A2-ALIGN-20260816.yaml`;
`execution/_Coordination/AgentRuns/ROOT_AGENT0_DIRECT_A2_ALIGN_2026-08-16/`.
