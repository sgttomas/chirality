# Handoff State — D-GOV-11 Agent Hierarchy Refactor

Status: COMPLETE
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
- HELP_HUMAN rewritten as sole read-only Agent 0 with managed delegation; durable launch briefs are runtime evidence, not an execution fallback.
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
- Completion-audit hardening enforces child read scopes and write targets at
  permission/hook boundaries, fails closed on unbounded managed Bash, validates
  return markers, versions replans, injects updates at safe turn boundaries,
  requires acknowledgments, reconstructs handoff state, and isolates failures.
- Current generic audit and REVIEW snapshots write under `_Evaluation/`;
  historical generic `_Reconciliation/` snapshots remain immutable evidence.
  RECONCILIATION alone owns new deliverable-corpus concordance runs.
- D-GOV-13 requalifies the 14 retained dedicated Agent 2 packages against
  persistent output/recovery and live-reference compatibility evidence.

## Validation Evidence

- Root governance/tool suite: 762 tests passed. Agent hierarchy/output-root,
  project-loop/entrypoint, skill, and path validators pass with 33 agent
  packages at zero errors and zero warnings and all 43 live skills valid.
- App-dev runtime: TypeScript typecheck passed; the complete Vitest suite passed
  94 files (one skipped), 682 tests (four skipped). The unsigned desktop package
  built; packaged instruction-root integrity passed; the live premerge probe
  passed 8 Section 8 scenarios and 16 Section 9 gates.
- Piping: the complete evidence sweep passed 36 Rust crate tests, 459 Python
  tests, 471 desktop unit/component tests, 18 development browser-flow tests,
  the production-distribution WASM test, and the desktop production build.
- Path-anchor and instruction-entrypoint validators passed. `git diff --check`
  reported no whitespace errors.
- Public derivative regenerated from the audit-repair commit with 585 manifest
  entries and zero boundary findings. Its staging tree independently passed the
  agent, instruction-entrypoint, skill-metadata, and path-anchor validators.

## Deferred Evolution

- Continue slimming retained Agent 1 roles around human decisions and handoffs
  when use evidence identifies a safe replacement-first migration.
- Reconsider `SOFTWARE_DEV` only if WORKING_ITEMS plus the software activation
  profile, TASK skills, and deterministic tools prove insufficient in practice.

## External Blockers

None. Both paused concordance branches are integrated, combined validation has
passed, and the public derivative has been regenerated and independently checked.

## Required Resume Sequence

1. Resume project work from this accepted hierarchy and orchestration basis.

## Closure Verdict

Instruction tranche: COMPLETE.
RECONCILIATION activation: COMPLETE.
Runtime bridge: IMPLEMENTED AND VALIDATED.
Overall D-GOV-11 implementation: COMPLETE.
