# Launch brief — H1 HELPS_HUMANS / TM-ROOT-125

- Parent: `HELP_HUMAN`
- RunID: `ROOT_CROSS_LOOP_CARRIERS_2026-08-21`
- Objective: implement the smallest coherent Root workflow-component tranche
  that permits Agent 0 to allowlist canonical `TASK` and to opt into ephemeral
  generalist Agent 2 dispatch while preserving every other hierarchy
  rejection fail-closed.
- Accepted basis: `origin/main@e3e18d27740018efd12e73193c02395a9eca93c2`;
  Root `AGENTS.md`; `AGENT_HELP_HUMAN.md`; `TM-ROOT-125`; owner direction of
  2026-08-21.
- Required reads: `agents/AGENT_HELPS_HUMANS.md`,
  `docs/WORKFLOW_COMPONENT_STANDARD.md`, the current validator and tests, G4
  schema/validator/tests, the prior `ROOT-AGENT0-DIRECT-A2-ALIGN-20260816`
  manifest and notices, App Receipt 172 / commit `ac2cd801a...`, App
  DEL-08-04 Remaining, and affected pin/mirror surfaces.
- Exact writable scope: `agents/AGENT_HELP_HUMAN.md`;
  `tools/validation/validate_agent_instructions.py`;
  `tools/validation/test_validate_agent_instructions.py`; one new manifest
  under `docs/governance_harness/tranche_manifests/`; same-tranche notices in
  affected Root-owned project/domain coordination surfaces; and this
  instance's `RETURN.md` / `STATUS.json`.
- Required behavior: Agent 0 may name Agent 1 children and canonical `TASK`
  only; Agent 0 may set `allow_generalist_agent2: true`; Agent 0 to any other
  named Agent 2 remains rejected; Agent 1 and Agent 2 rules remain unchanged;
  unresolved roles remain rejected; `TASK` and generalist paths retain their
  existing sealed-brief/tool/scope gates.
- Required instruction change: add `TASK` to HELP_HUMAN `subagents`, add the
  explicit generalist opt-in, and remove the now-stale prose claim that Root
  validator/App harness still enforce Agent-1-only children. Do not broaden
  HELP_HUMAN write scope or human authority.
- Required tests: replace the superseded negative test; add explicit positive
  and negative coverage sufficient to prove the narrow exception and
  preserved fail-closed cases. Update any policy test pinning touched text.
- G4 / notice contract: ship a new manifest for this tranche; identify all
  live pins/mirrors of the touched agent file; route notices to every affected
  loop. The App notice must name the exact Root change and tell App to run the
  DEL-08-04 post-Root cross-surface integration check against already-landed
  commit `ac2cd801a06a0679bc86830c627218ccca78b658` / Receipt 172. Notices are
  coordination, not authority.
- Exclusions: no App harness edits, no foreign register edits, no runtime
  product code, no lifecycle/release/reliance act, no merge.
- Return: changed paths, behavioral matrix, pin/mirror census, exact checks
  and results, residual blockers, derivative disposition, and next owner.
