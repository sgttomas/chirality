# Handoff State — D-GOV-11 Agent Hierarchy Refactor

Status: COMPLETE / PUBLICATION PENDING
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
- HELP_HUMAN rewritten as sole read-only Agent 0 with managed delegation and a durable launch-brief fallback.
- `docs/DECOMPOSITION_STANDARD.md` extracted; DECOMP_BASE persona removed and live managers rebound.
- EVALUATION expanded; old generic RECONCILIATION semantics transferred.
- RECONCILIATION activated from the ratified method and integrated app-dev and
  piping calibration/pause evidence.
- SCHEDULING merged into ORCHESTRATOR; SKILLMAKER, TOOLMAKER, CONTEXT_TRANSPOSE, and SCHEDULING persona files removed after live caller redirection.
- PDF2MD and DRAWING_EXTRACT source/target calibration and novel-generalist semantics added.
- D-GOV-12 doctrine, package-level WORKING_ITEMS, cross-package HELP_HUMAN,
  orchestration vocabulary, and managed-runtime record schema added.
- DBM, disposition matrix, TYPES, DIRECTIVE, README, professional-engineering mapping, roadmap, validators, skill/tool ownership, and export contract updated.
- App-dev and piping loops now use package-level WORKING_ITEMS work graphs.
- Project software profiles, five software TASK skills, and deterministic
  discovery/check/scope/comparison/drift tools are live.
- Managed child sessions, terminal/background execution, coordination notices,
  updates, amendments, acknowledgments, runtime records, actual named
  instruction loading, and the SDK compatibility adapter are implemented.
- D-GOV-13 requalifies the 14 retained dedicated Agent 2 packages against
  persistent output/recovery and live-reference compatibility evidence.

## Validation Evidence

- Root governance/tool suite: 757 tests passed before the D-GOV-13 metadata
  binding; the affected validator suite then passed 57 tests, with 33 agent
  packages at zero errors and zero warnings and all 43 live skills valid.
- App-dev runtime: TypeScript typecheck passed; the complete Vitest suite passed
  93 files (one skipped), 673 tests (four skipped); the final managed-delegation,
  descriptor, bridge, and instruction-integrity slice passed 29 tests.
- Piping: the complete evidence sweep passed 36 Rust crate tests, 459 Python
  tests, 471 desktop unit/component tests, 18 development browser-flow tests,
  the production-distribution WASM test, and the desktop production build.
- Path-anchor and instruction-entrypoint validators passed. `git diff --check`
  reported no whitespace errors.

## Deferred Evolution

- Continue slimming retained Agent 1 roles around human decisions and handoffs
  when use evidence identifies a safe replacement-first migration.
- Reconsider `SOFTWARE_DEV` only if WORKING_ITEMS plus the software activation
  profile, TASK skills, and deterministic tools prove insufficient in practice.

## External Blockers

None. Both paused concordance branches are integrated and combined validation
has passed. Public-export regeneration follows the publication commits.

## Required Resume Sequence

1. Bind D-GOV-13 to the implementation publication SHA.
2. Regenerate and validate the derivative public export.
3. Resume project work from this accepted hierarchy and orchestration basis.

## Closure Verdict

Instruction tranche: COMPLETE.
RECONCILIATION activation: COMPLETE.
Runtime bridge: IMPLEMENTED AND VALIDATED.
Overall D-GOV-11 implementation: COMPLETE, subject only to publication-SHA
binding and derivative-export regeneration.
