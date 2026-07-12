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
- RECONCILIATION reserved fail-closed pending calibration evidence.
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

1. The final RECONCILIATION instruction requires stable accepted concordance handoffs from both `chirality-piping` and `chirality-app-dev` and their integration into the branch basis.
2. The managed delegation runtime must be implemented after those branches integrate and this branch is rebased, so app-dev runtime changes are made against the accepted instruction roster.

## Required Resume Sequence

1. Confirm both calibration lanes have stable handoffs and accepted changes on main.
2. Rebase `codex/agent-governance-redesign`.
3. Derive and validate the activated RECONCILIATION contract from the ratified method and calibration evidence.
4. Implement the managed `delegate_agent` runtime, compatibility adapter, metadata, and hierarchy tests.
5. Run root and app-dev validation and workflow acceptance scenarios.
6. Publish through CHANGE and backfill ruling SHAs.

## Closure Verdict

Instruction tranche: OPEN until full validation passes.  
RECONCILIATION activation: BLOCKED by external accepted evidence.  
Runtime bridge: SEQUENCED after rebase, not authorized against stale app-dev state.  
Overall D-GOV-11 implementation: OPEN.
