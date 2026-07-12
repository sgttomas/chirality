# Handoff State — D-GOV-11 Agent Hierarchy Refactor

Status: ACTIVE / PARTIALLY BLOCKED BY EXTERNAL INTEGRATION  
DecisionBasis: `docs/governance_harness/_DECISIONS/D-GOV-11_runtime_agent_hierarchy.md`; `docs/governance_harness/_DECISIONS/D-GOV-12_multi_agent_orchestration.md`
Branch: `codex/agent-governance-redesign`

## Accepted Direction

- HELP_HUMAN is sole Agent 0 Supervising Architect.
- Agent 1 managers are direct human entry points and may run under Agent 0.
- Agent 2 may be TASK, ephemeral generalist, or approved dedicated specialist.
- Standards are external constraints, not agents.
- Runtime delegation is hierarchical; filesystem and Git state provide many-to-many coordination.
- EVALUATION owns generic audit/reconciliation semantics.
- RECONCILIATION is reserved for deliverable-corpus concordance.
- PDF2MD and DRAWING_EXTRACT remain Agent 1.
- Terminal fan-out/fan-in and supervised many-to-many agency are complementary
  canonical patterns; mixed work graphs are allowed.
- WORKING_ITEMS is a package-level Agent 1 and SOFTWARE_DEV is deferred.

## Implemented in This Instruction Tranche

- Canonical doctrine in `AGENTS.md`; exact `CLAUDE.md` import and validator/export enforcement.
- HELPS_HUMANS consolidated component design, skill/tool design, context transposition, and decomposition-component design.
- HELP_HUMAN rewritten as sole read-only Agent 0 with durable launch-brief fallback.
- `docs/DECOMPOSITION_STANDARD.md` extracted; DECOMP_BASE persona removed and live managers rebound.
- EVALUATION expanded; old generic RECONCILIATION semantics transferred.
- RECONCILIATION activated from the ratified method and integrated app-dev and
  piping calibration/pause evidence.
- SCHEDULING merged into ORCHESTRATOR; SKILLMAKER, TOOLMAKER, CONTEXT_TRANSPOSE, and SCHEDULING persona files removed after live caller redirection.
- PDF2MD and DRAWING_EXTRACT source/target calibration and novel-generalist semantics added.
- D-GOV-12 doctrine, package-level WORKING_ITEMS, cross-package HELP_HUMAN,
  orchestration vocabulary, and managed-runtime record schema added.
- DBM, disposition matrix, TYPES, DIRECTIVE, README, professional-engineering mapping, roadmap, validators, skill/tool ownership, and export contract updated.

## Pending Internal Work

- Requalify each remaining non-TASK dedicated Agent 2 and migrate it only with callers, compatibility behavior, and tests.
- Continue slimming retained Agent 1 roles around human decisions and handoffs.
- Rerun and resolve full validation/export findings after all current-tranche edits.

## External Blockers

The concordance integration blocker is cleared. Managed delegation,
project-loop migration, software profiles/skills/tools, and combined
acceptance remain open.

## Required Resume Sequence

1. Update project indexes and loop instructions to the package-level paradigm.
2. Add software activation profiles, initial skills, and deterministic tools.
3. Implement the managed delegation runtime, compatibility adapter, metadata,
   persistence, and hierarchy/live-coordination tests.
4. Run root, app-dev, piping, and workflow acceptance scenarios.
5. Publish through CHANGE.

## Closure Verdict

Instruction tranche: OPEN until full validation passes.
RECONCILIATION activation: COMPLETE.
Runtime bridge: IN PROGRESS against integrated paused project state.
Overall D-GOV-11 implementation: OPEN.
